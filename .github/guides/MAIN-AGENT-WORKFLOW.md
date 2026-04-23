---
name: MAIN-AGENT-WORKFLOW
description: Executable specification for Main Agent orchestration across all 10 phases of skill creation
---

# Main Agent Workflow - Executable Specification

**Purpose**: Define how Main Agent (Creator role) autonomously executes all 10 phases of the skill creation workflow based on a `plan/<topic>/<topic>.plan.md` file.

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

Main Agent reads `plan/<topic>/<topic>.plan.md` and orchestrates 10 phases:

```
Phase 1-3: Planner → Creator (branch + initial SKILL draft)
Phase 4:   Copilot + Reviewer (two-layer review)
Phase 4.5: Planner contract alignment checkpoint
Phase 5-6: Stable-library handling + validate/stage (pre-commit checks)
           [STOP 1: User confirm before commit]
Phase 6:   Commit & push, open PR
Phase 7-8: PR comment loop (max 3 iterations)
           [STOP 2: User confirm before manual merge]
Phase 8:   User merges (manual)
Phase 9-10: Post-merge + release
```

Main Agent remains the orchestrating actor through Phase 10. Human actions at the
two stop points authorize or complete specific transitions, but they do not replace
Main Agent as the owner of the surrounding publish, post-merge, and release phases.

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
                 ↓ (Phase 7-8: PR loop, max 3 iterations)
                 [STOP 2: User "Ready to merge?"]
                   ├─ [NO] → wait
                   └─ [YES] → user merges on GitHub
                       ↓
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

**Input**: `plan/<topic>/<topic>.plan.md`

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

---

### Phase 2: Prepare Branch

**Input**: `topic_name`, `skill_name`

**Task**:
1. Use `git-branch-naming` skill to choose a semantic development branch:
   `<type>/<username>/<short-description>`
2. Create or verify branch exists
3. Ensure workspace clean
4. Treat the branch as semantic work naming, not a hard-coded `feature/...` shape

**Output**: Branch ready; Status: `planned` (no change yet)

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
1. If `Stable library metadata` in plan with `publish-in-progress` timing:
   - Prepare README.md update
   - Prepare VERSION bump
   - Stage both (do NOT commit)
2. If `Stable library metadata` uses `release` timing but the plan does not
   declare a release action:
   - STOP
   - Fix the plan before continuing
3. Final preview

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

### Phase 7-8: PR Loop with Termination (MAX 3 ITERATIONS)

#### **Phase 7: PR Comment Check**

1. Fetch PR comments from GitHub
2. Classify each comment:
   - **Direct-apply**: style, typo, meta, formatting
   - **Needs-reviewer**: logic, scope, trigger, examples, requirements

#### **Phase 8: Creator Fix Loop**

```
iteration = 0
max_iterations = 3

LOOP:
  1. Fetch PR comments
  
  2. If NO comments:
     → PR approved ✅ → exit loop
  
  3. If comments exist:
     
     a. If ALL are direct-apply:
        - Creator applies fixes
        - Commit: git commit -m "fix: address PR comments"
        - Push: git push
        - iteration += 1
        - Loop back to step 1
     
     b. If ANY need reviewer:
        - Route back to Phase 4 (reviewer re-check)
        - Reviewer produces new verdict
        - If approved: continue
        - If needs-rework: back to Phase 4
  
  4. If iteration >= max_iterations:
     - Force exit
     - Display: "Max PR iterations reached (3)"
     - Exit loop
```

**Output**: No blocking comments; Status → `pr-approved`

---

### [STOP POINT 2] Confirm Before Merge

**Prompt to User**:
```
✅ PHASE 8: PR READY FOR MERGE

PR: #<number> <link>
Status: All checks ✅ green
Comments: All addressed ✅

Next: Merge manually on GitHub, then confirm here.

Ready to merge?
[Y] Yes, go merge on GitHub, I'll continue after
[N] Not yet, ask again later
```

**If NO**: Wait (check every 30 sec); ask again

**If YES**: Instruct user to merge on GitHub; wait for merge detection

---

### Phase 9: Post-Merge Local Sync

**Input**: PR merged on GitHub

**Task**:
1. Detect merge (poll GitHub or git fetch)
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
PHASE_8_APPROVED: No blocking comments
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
  - Resume: Phase 7 (check PR comments)
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

### After Phase 8: PR Approved
```
✅ PR READY FOR MERGE

Branch: <type>/<username>/<short-description>
PR: #<number> (<link>)
Status: All checks ✅ green
Comments: All addressed ✅

Go to GitHub and merge manually.
Confirm when merged and I'll continue.

Ready to proceed after merge?
[Y] Waiting for merge, then continue to Phase 9
[N] I'll merge later and restart
```

---

## Version History

- **v1.0** (2026-04-22): Initial release
  - Two-layer review (Copilot + Reviewer with JSON reports)
  - Pre-commit stop points
  - Max 3 PR iterations
  - Checkpoint-based resumability
  - Ask-user-only error handling
