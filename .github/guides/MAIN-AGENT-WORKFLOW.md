---
name: MAIN-AGENT-WORKFLOW
description: Executable specification for Main Agent orchestration across all 10 phases of skill creation
---

# Main Agent Workflow - Executable Specification

**Purpose**: Define how Main Agent (publisher / release actor / orchestrator) autonomously executes all 10 phases of the skill creation workflow based on a valid repo-visible `plan/<topic>/<topic>.plan.md` file.

**Audience**: Main Agent implementation logic, skill executors, workflow testers

---

## Table of Contents

1. [Overview](#overview)
2. [Status Model & Transitions](#status-model--transitions)
3. [Phase-by-Phase Execution](#phase-by-phase-execution)
4. [Key Mechanisms](#key-mechanisms)
   - [Phase 4: Two-Layer Review](#phase-4-two-layer-review)
   - [Phase 5-6: Pre-commit Staging](#phase-5-6-pre-commit-staging)
   - [Phase 7-8: PR Loop with Termination](#phase-7-8-pr-loop-with-termination)
   - [Error Handling & Recovery](#error-handling--recovery)
   - [Checkpoint-Based Resumability](#checkpoint-based-resumability)

---

## Overview

Main Agent reads a valid repo-visible `plan/<topic>/<topic>.plan.md` and
orchestrates 10 phases:

```
Phase 1-3: Planner → Creator (branch + initial SKILL draft)
Phase 4:   Copilot + Reviewer (two-layer review)
Phase 4.5: Planner contract alignment checkpoint
Phase 5-6: Stable-library handling + validate/stage (pre-commit checks)
           [STOP 1: User confirm before commit]
Phase 6:   Commit & push, open PR
Phase 7-8: PR loop + bounded observation
           [STOP 2: User confirm before manual merge]
Phase 8:   User merges (manual)
Phase 9-10: Post-merge + release
```

Main Agent remains the orchestrating actor through Phase 10. Human actions at the
two stop points authorize or complete specific transitions, but they do not replace
Main Agent as the owner of the surrounding publish, post-merge, and release phases.

Boundary note:
- `plan/agent-handoff-workflow.md` owns the canonical phase semantics and the
  trigger / input / output contract.
- This guide translates that contract into executable sequencing, command
  patterns, retries, checkpoints, and environment-specific notes.
- The guide assumes a valid repo-visible topic plan already exists; it does not
  define the full authoring methodology for a future planning-specific skill
  such as `plan-creator`.

**Key Decisions** (from workflow validation):
- ✅ Two-layer review: Copilot (code quality) + Reviewer (design quality)
- ✅ Planner contract alignment: independent checkpoint after reviewer approval
- ✅ Pre-commit stop points (avoid fake state in git history)
- ✅ PR loop max 3 iterations (prevent infinite loops)
- ✅ JSON-formatted SubAgent reports (structured, not fragile text parsing)
- ✅ Stable-library timing declared in topic plan (not guessed by Main Agent)
- ✅ Ask-user-only error handling (maximum transparency)

---

## Status Model & Transitions

```
planned
  ↓ (Phase 1-3: auto)
creator-in-progress
  ↓ (Phase 3: auto)
review-ready
  ↓ (Phase 4: two-layer review, auto-loop if needs-rework)
  ├─ [If needs-rework] → back to Phase 4
  └─ [If approved]
       ↓ (Phase 4.5: planner contract alignment)
       ├─ [If drift found] → creator-in-progress
       └─ [If aligned]
            ↓
            publish-in-progress (Phase 5-6, no commit yet)
          ↓ [STOP 1: User "Ready to push?"]
            ├─ [NO] → back to Phase 5
            └─ [YES] → commit + push, open PR
               ↓
                pr-open
                   ↓ (Phase 7-8: PR loop + bounded observation)
                  [STOP 2: Human merge handoff]
                    ├─ [NOT READY] → stop; human returns later
                    └─ [HANDOFF] → human merges on GitHub
                        ↓ [new human message confirms merge]
                        merged (Phase 9: post-merge sync)
                          ↓ (Phase 10: release if needed)
                          ↓
                           released (or terminal)
```

Ownership note:
- Main Agent owns the workflow from `planned` through `released`.
- Human actions affect the STOP 1 / STOP 2 transitions, especially manual merge,
  but they do not become a separate owner for Phase 9-10.

---

## Phase-by-Phase Execution

### Phase 1: Read Plan & Validate

**Input**: valid repo-visible `plan/<topic>/<topic>.plan.md`

**Task**:
1. Read the topic plan file
2. Validate all 11 required sections exist
3. Extract metadata:
   - `topic_name`, `skill_name`
   - `locked_decisions` → which skills/references to create
   - `artifact_paths` → executable output locations
   - `stable_library_metadata` → README/VERSION rules + timing

**Output**: Parsed plan data; Status check passes

**Error**: If plan missing/malformed → STOP, ask user to create/fix

**Boundary**:
- The plan may be authored by a human planning actor today or by a future
  planning-specific tool, but this guide starts once that repo-visible plan
  already exists.

---

### Phase 2: Prepare Branch

**Input**: `topic_name`, `skill_name`, current branch/worktree state, branch policy

**Task**:
1. Use `git-branch-naming` skill to choose a semantic development branch:
   `<type>/<username>/<short-description>`
2. Create or verify branch exists
3. Run a branch-preflight check before creator work:
   - current branch matches topic intent, or a repair path is chosen
   - branch naming policy has been applied
   - worktree state is understood and safe for this topic
   - unrelated dirty or untracked files are either intentionally preserved,
     explicitly approved, or treated as a stop condition
4. Treat the branch as semantic work naming, not a hard-coded `feature/...` shape
5. If preflight fails, STOP. Do not invoke creator until the branch/worktree state
   is explicitly safe.

**Output**: Semantic execution branch ready; Status: `planned` (no change yet)

---

### Phase 3: Creator Drafts Initial SKILL

**Input**: `skill_name`, locked decisions

**Task**:
1. Invoke `agent-skill-creator` as the creator drafting skill
    - Pass plan.md path
    - Output: .github/skills/<skill-name>/ with SKILL.md + examples/reference + optional files
2. Verify files exist

**Execution note**:
- In VS Code, this maps to `@file:agent-skill-creator <path/to/topic_plan.md>`.
- In CLI, this maps to `copilot skill agent-skill-creator <path/to/topic_plan.md>`.
- Phase 3 is a normal creator-skill invocation, not the independent reviewer-style
  SubAgent handoff used in Phase 4.

**Output**: Draft complete; Status → `creator-in-progress`

---

### Phase 4: Two-Layer Review (THREE-STEP PROCESS)

#### **Step 4a: Creator Ready Signal**

Main Agent verifies SKILL draft complete (all required files present).

#### **Step 4b: Copilot Review Agent Scans** (ONE-TIME)

1. Copilot scans the commits in the branch
2. Produces comments on code quality, style, formatting, links, etc.
3. Main Agent collects comments into memory
4. **Key**: Single scan, not continuous

```
Copilot comments:
  - [style] H1 title should be "Purpose" not "purpose"
  - [typo] "occured" → "occurred"
  - [meta] link format incorrect
```

#### **Step 4c: SubAgent Reviewer Evaluates**

1. Main Agent invokes `agent-skill-reviewer` SubAgent:
   ```
   /fleet 根據 review-checklist.md 與 plan 評審 .github/skills/<skill-name>/
   
   上下文：
   - Plan file: plan/<topic>/<topic>.plan.md
   - Copilot comments: [list above]
   
    評審內容：
    1. 符合 plan 的 Implementation steps？
    2. 例子和參考資料足夠深入？
    3. Copilot 的評論是否都妥當？ (address/discuss/skip)
    4. `Artifact paths` 是否有效且與實際輸出位置一致？
   
   回傳 JSON 格式。
   ```

2. Wait for reviewer verdict

**Reviewer Report (JSON)**:
```json
{
  "verdict": "approved|needs-rework",
  "blocking_issues": [
    {
      "issue": "Missing Boundaries section",
      "file": "SKILL.md",
      "fix": "Add per template"
    }
  ],
  "copilot_feedback_triage": {
    "ADDRESS": [
      {"comment": "H1 Title Case", "why": "repo standard"}
    ],
    "DISCUSS": [
      {"comment": "Add more examples", "optional": true}
    ],
    "SKIP": []
  }
}
```

#### **If `needs-rework`**:
- Back to Phase 3: Creator fixes blocking issues
- Repeat Steps 4a-4c

#### **If `approved`**:
- Creator applies `ADDRESS` feedback (required)
- Creator optionally applies `DISCUSS` feedback
- Creator skips `SKIP` feedback
- Main Agent commits:
  ```bash
  git commit -m "feat: address review feedback on <skill-name>
  
  - Fixed [items from ADDRESS]
  
  Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>"
  ```
- Continue to Phase 4.5

**Error Handling**:
- Reviewer crashed → use checkpoint to retry
- Network timeout → retry 3x with backoff

---

### Phase 4.5: Planner Contract Alignment

**Input**: Reviewer-approved draft plus latest topic plan

**Owner**: Main Agent

**Task**:
1. Verify locked decisions still match the current draft
2. Check contract / schema / record-shape semantics against the topic plan
3. Treat plan-level drift as a routing failure, not as a style-only comment

**Output**:
- If aligned → continue to Phase 5-6; Status → `publish-in-progress`
- If drift found → Status → `creator-in-progress`

**Error**: If planner alignment cannot be completed → STOP, resolve plan ambiguity first

---

### Phase 5-6: Validate & Stage (PRE-COMMIT)

**Phase 5: Validation**
1. Check all required files exist
2. Check SKILL.md has all sections
3. Check examples have positive + negative cases
4. Validate file sizes
5. Run lint (if applicable)

**Phase 6: Staging**
1. Stage only the allowed file set for the topic:
   - artifact paths locked in the topic plan
   - PR direct-apply files for the current loop
   - extra files explicitly approved by a human
   - `README.md` and `VERSION` are **not** automatic exceptions; each file is
     allowed only when it is explicitly listed in the topic plan `Artifact paths`
2. Do **not** use broad staging defaults such as `git add -A` or `git add .`
   in publish flow.
3. If `Stable library metadata` in plan with `publish-in-progress` timing:
   - Prepare `README.md` update only if `README.md` is explicitly listed in the
     topic plan `Artifact paths`
   - Prepare `VERSION` bump only if `VERSION` is explicitly listed in the topic
     plan `Artifact paths`
   - Stage only those prepared files that satisfy both conditions above
     (scheduled stable-library metadata **and** explicit `Artifact paths`
     listing)
4. If `Stable library metadata` uses `release` timing but the plan does not
   declare a release action:
   - STOP
   - Fix the plan before continuing
5. Final preview of staged files; if unrelated files are staged, unstage and
   repair before STOP POINT 1

**Output**: Validation ✅; Files staged; Status → `publish-in-progress`

**Error**: If validation fails → STOP, ask user to fix, retry Phase 5

---

### [STOP POINT 1] Confirm Before Commit

**Prompt to User**:
```
✅ PHASE 6: READY TO PUSH

Validation: ✅ PASSED
  - All required files present
  - Examples complete
  - Structure valid

Staged changes:
  - .github/skills/<skill-name>/SKILL.md
  - .github/skills/<skill-name>/examples.md
  - README.md (new row added, if publish timing)
  - VERSION (0.11.0 → 0.12.0, if publish timing)

Rule:
  - staged files must stay within the allowed file set for this topic
  - broad staging defaults (git add -A / git add .) are not allowed here

Ready to commit + push + open PR?
[Y] Yes, proceed
[N] No, back to Phase 5 (make more changes)
```

**If NO**: Discard staged changes (git reset); go back to Phase 5

**If YES**: Continue to Phase 6 final commit

---

### Phase 6: Commit, Push, Open PR

**Task**:
1. Commit: `git commit -m "feat: add <skill-name> skill..."`
2. Commit status: `git commit -m "chore: update plan status to pr-open"`
3. Push: `git push`
4. Open PR: `gh pr create --title "..." --body "..."`
5. Status → `pr-open`

**Error Handling**:
- Push fails (conflict) → STOP, ask user to manually resolve
- PR creation fails → STOP, ask user to create manually

---

### Phase 7-8: PR Loop with Bounded Observation

#### **Phase 7: PR Comment Check**

1. Fetch review comments, issue comments, and check runs from GitHub
2. Classify each comment:
    - **Direct-apply**: style, typo, meta, formatting
    - **Needs-reviewer**: logic, scope, trigger, examples, requirements
3. Failed checks or any other newly blocking PR state are blocking signals, not
   proof of a clean PR snapshot.
4. The bounded observation shape is `consecutive-empty-checks`, not a one-time
   empty fetch.

#### **Phase 8: Creator Fix Loop**

```
iteration = 0
max_iterations = 3
empty_checks = 0
observation_waits = [30, 60, 120]

LOOP:
  1. Fetch latest review comments, latest issue comments, and current check runs

  2. If any blocking signal exists:
     - Reset empty_checks = 0
     - Treat failed checks, unresolved blocking comment state, or other newly
       blocking PR state as NOT clean
     - Classify comments

     a. If ALL actionable items are direct-apply:
        - Creator applies fixes
        - Commit: git commit -m "fix: address PR comments"
        - Push: git push
        - iteration += 1
        - Loop back to step 1

     b. If ANY actionable item needs reviewer:
        - Route back to Phase 4 (reviewer re-check)
        - Reviewer produces new verdict
        - If approved: continue
        - If needs-rework: back to Phase 4

  3. If no blocking signal exists in the current snapshot:
     - empty_checks += 1
     - If empty_checks < 3:
        - Sleep observation_waits[empty_checks - 1]
        - Loop back to step 1
     - If empty_checks == 3:
        - Exit the bounded observation window
        - Report only:
          1. no new blocking signal was observed within the bounded window
          2. this is not a guarantee that later feedback will not arrive
          3. a human must decide whether to inspect the PR and hand off merge
        - Continue to the human merge-readiness confirmation gate

  4. If iteration >= max_iterations:
     - Display: "Max PR iterations reached (3)"
     - Stop the direct-apply loop
     - Remain in `pr-open` until a human decides the next step
```

**Output**: Either a patch/re-review route, or a bounded observation result that
is eligible for human merge-readiness confirmation while status remains
`pr-open`

---

### [STOP POINT 2] Confirm Before Merge

**Prompt to User**:
```
✅ PHASE 8: BOUNDED PR OBSERVATION COMPLETE

PR: #<number> <link>
Observation: 3 consecutive clean checks (`30s -> 60s -> 120s`)
Gate shape: `consecutive-empty-checks`
Signals checked: review comments, issue comments, check runs
Result: No new blocking signal observed within the bounded window

Important:
  - This is not a guarantee that later feedback will not arrive
  - Main Agent is not declaring the PR merge-ready on its own
  - A human must inspect the PR and decide whether to hand off merge

Next: Merge manually on GitHub; Main Agent stops here and resumes only after a
later explicit human message.

Ready to hand off to human merge?
[Y] Yes, hand off to human merge and stop here
[N] Not yet; stop here and a human may resume later with a new explicit message
```

**If NO**:
- Stop the current execution.
- Do not wait in the background.
- Do not poll or ask again automatically.
- A human may later resume from this stop point with a new explicit message.

**If YES**:
- Instruct user to inspect the PR and merge on GitHub if they judge it ready.
- Stop the current execution immediately after handoff.
- Do not wait for merge detection.
- Phase 9 resumes only when a human later sends a new explicit
  merge-confirmation message.

---

### Phase 9: Post-Merge Local Sync

**Input**: explicit human resume message plus PR merged on GitHub

**Task**:
1. Confirm the referenced PR or merge path actually merged before cleanup starts
2. Inspect worktree, untracked files, and preserved local state before sync
3. Distinguish upstream history change from local-only state
4. Capture any local state that still needs preservation
5. Main Agent invokes `git-post-merge-workflow` as a normal skill step
   (not an independent reviewer-style SubAgent handoff):
   - Sync default branch
   - Clean up working branch
6. Status → `merged`

**Error**: If git-post-merge-workflow fails → log; don't block release

---

### Phase 10: Release (If Applicable)

**Input**: Topic plan specifies release action

**Task**:
1. Check plan for release requirement
   - If NO → terminal at `merged` ✅
   - If YES → proceed

2. If `Stable library metadata` schedules README / VERSION at `release` timing:
   - Apply README.md update now
   - Apply VERSION bump now

3. Main Agent invokes `git-release-management` as a normal release skill step
   (not a separate operator-owned phase) and applies the 7 gates:
   1. Workspace clean
   2. Versions sync
   3. Tests pass
   4. Lint pass
   5. Type checks pass
   6. Tag unique
   7. Documentation updated

4. If all gates pass:
     - Create tag: `v<new-version>`
     - Push tag
     - Status → `released` ✅

5. If gates fail:
   - Display failures
   - Ask: "Fix and retry?" or "Manual later?"

6. If a late topic-plan or release-routing defect is discovered during Phase 10:
   - Stop release work immediately
   - Do not silently rewrite the original topic's locked intent
   - If the topic is `merged` but not yet `released`, route the next step with
     explicit human judgment (for example, limited rollback or a follow-up
     repair topic)
   - If the topic is already `released`, use a new repair topic instead of
     rolling the original topic back

---

## Key Mechanisms

### Checkpoint-Based Resumability

**Checkpoints** (in memory or local file):
```
PHASE_3_DRAFT_DONE: SKILL files exist
PHASE_4C_APPROVED: Reviewer approved
PHASE_4_5_PLANNER_ALIGNED: Planner checkpoint passed
PHASE_5_VALIDATION_DONE: All checks pass
PHASE_6_PR_OPEN: Push + PR created (status=pr-open)
PHASE_8_OBSERVATION_COMPLETE: Bounded observation window completed; human handoff gate ready
PHASE_9_MERGED: Merged (status=merged)
```

**Resume Logic** (when Main Agent restarts):
```
1. Read plan.md status field
2. Check which checkpoints completed
3. Find latest checkpoint
4. Resume from NEXT phase

Example:
  - plan.md status = pr-open
  - PHASE_6_PR_OPEN completed
  - Resume: Phase 7 (resume PR observation / comment triage)
```

---

### Error Handling Patterns

| Error Type | Example | Action |
|-----------|---------|--------|
| Recoverable (retry-able) | GitHub timeout | Retry 3x, exponential backoff |
| User-actionable | Missing examples.md | Display error + suggestion, wait for fix |
| Blocking | Reviewer needs-rework | Route back to Phase 4 |
| Manual intervention | PR needs human review | STOP + ask user |

**Ask-User-Only Pattern** (all errors):
```
When error detected:
  1. Display: "Error: [reason]"
  2. Suggest: "How to fix: [guidance]"
  3. Ask: "Ready to retry?" [Y/N]
```

---

### SubAgent Communication Format

#### Reviewer Report (JSON)

Main Agent expects:
```json
{
  "verdict": "approved|needs-rework",
  "blocking_issues": [
    {
      "issue": "Description",
      "file": "SKILL.md",
      "fix": "How to fix"
    }
  ],
  "copilot_feedback_triage": {
    "ADDRESS": [
      {
        "comment": "Text of comment",
        "location": "File:line",
        "why": "Why it matters"
      }
    ],
    "DISCUSS": [
      {
        "comment": "Text",
        "optional": true
      }
    ],
    "SKIP": [
      {
        "comment": "Text",
        "why": "Not applicable because..."
      }
    ]
  }
}
```

---

## Human Prompts (Exact Wording)

### After Phase 5: Validation Complete
```
✅ VALIDATION COMPLETE

All required sections present:
  ✅ SKILL.md: Purpose, Trigger, Inputs, Process, Examples, Outputs, Boundaries, Local references
  ✅ examples.md (or reference.md)
  ✅ Optional files valid

Staged for commit:
  - .github/skills/<skill-name>/
  - README.md (if applicable)
  - VERSION (if applicable)

Ready to push and open PR on GitHub?
[Y] Proceed with commit + push
[N] Back to Phase 5 (make more changes)
```

### After Phase 8: Bounded PR Observation Complete
```
✅ BOUNDED PR OBSERVATION COMPLETE

Branch: <type>/<username>/<short-description>
PR: #<number> (<link>)
Observation: 3 consecutive clean checks (`30s -> 60s -> 120s`)
Signals checked: review comments, issue comments, check runs
Result: No new blocking signal observed within the bounded window

Important:
  - This is not a guarantee that later feedback will not arrive
  - Main Agent is not declaring the PR merge-ready on its own
  - A human must inspect the PR and decide whether to hand off merge

If the human judges the PR ready, go to GitHub and merge manually.
Main Agent stops immediately after this handoff.

Ready to hand off to human merge?
[Y] Hand off to human merge and stop here
[N] Stop here; a human may resume later with a new explicit message
```

---

## Version History

- **v1.0** (2026-04-22): Initial release
  - Two-layer review (Copilot + Reviewer with JSON reports)
  - Pre-commit stop points
  - Max 3 PR iterations
  - Checkpoint-based resumability
  - Ask-user-only error handling
