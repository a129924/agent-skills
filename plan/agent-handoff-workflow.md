# Agent handoff workflow

## Purpose
Define the canonical repo-level workflow for planning, drafting, reviewing,
publishing, and releasing work in this repository when different agents operate
in different contexts.

## Scope
- This document defines the shared process for repo-visible handoff artifacts.
- It is platform-agnostic at the process level.
- It applies to both VS Code and CLI usage.
- It does not replace task-specific skill instructions inside
  `.github/skills/<skill-name>/`.

## Core principles
- Planning decisions must be captured in repo-visible files, not left in hidden
  session context.
- Creator and reviewer are separate roles and should not rely on one shared
  conversation state.
- Topic execution should start from `plan/<topic>/<topic>.plan.md`.
- Stable-library updates happen only after reviewer approval.
- The workflow should stay reusable and independent of one exact UI or launch
  command.

## Roles
| Role | Primary responsibility | Must not do |
| --- | --- | --- |
| Planning actor | Define scope, locked decisions, boundaries, and handoff artifacts | Skip the repo-visible plan file |
| Creator | Draft or revise the implementation from the topic plan until it is `review-ready` | Approve its own output |
| Reviewer | Evaluate the latest creator output and return `approved` or `needs-rework` | Author the final implementation directly |
| Main Agent (publisher / release actor) | Handle commit, push, PR, review-comment triage, merge follow-up, and release/version actions, while stopping for explicit human confirmations where the workflow requires them | Change planning intent retroactively without updating the plan |

## Canonical artifacts
| Artifact | Path | Purpose |
| --- | --- | --- |
| Repo workflow spec | `plan/agent-handoff-workflow.md` | Shared process contract |
| Topic handoff plan | `plan/<topic>/<topic>.plan.md` | Repo-visible execution contract for one topic |
| Skill draft | `.github/skills/<skill-name>/` | Creator output under repo policy |
| Stable-library summary | `README.md` | Human-facing stable skill list |
| Repo version baseline | `VERSION` | Canonical SemVer version for the repository |

## Topic plan contract
Every topic handoff plan must include these fixed sections:
- `Goal / outcome`
- `Scope`
- `Locked decisions`
- `Boundaries / exclusions`
- `Status / allowed transitions`
- `Artifact paths`
- `Implementation steps`
- `Validation / acceptance checks`
- `Reviewer handoff`
- `Post-merge / release actions`
- `Open questions / unresolved items`

## Status model
| Status | Meaning | Owner | Allowed next |
| --- | --- | --- | --- |
| `planned` | Topic plan is committed and ready for execution | Planning actor / human | `creator-in-progress` |
| `creator-in-progress` | Creator is drafting or revising the work | Creator | `review-ready` |
| `review-ready` | Creator finished the latest draft and hands it off | Creator | `reviewer-in-progress` |
| `reviewer-in-progress` | Reviewer is evaluating the latest draft | Reviewer | `approved`, `needs-rework` |
| `needs-rework` | Reviewer found blocking issues and returned the work | Reviewer | `creator-in-progress` |
| `approved` | Reviewer accepted the draft | Reviewer | `publish-in-progress` |
| `publish-in-progress` | Approved work is being committed, pushed, and prepared for PR / stable-surface updates | Main Agent (publisher / release actor) | `pr-open`, `merged` |
| `pr-open` | PR is open and comment triage is active | Main Agent (publisher / release actor) | `needs-rework`, `merged` |
| `merged` | Changes are merged; local sync and optional release follow-up remain | Main Agent (publisher / release actor) | `released`, terminal |
| `released` | Version and tag actions are complete when the change requires them | Main Agent (publisher / release actor) | terminal |

Notes:
- `merged` is terminal for changes that do not require a release action.
- `released` is required when a merge also performs a repository release step.
- Reviewer comments on an open PR may send the work back to `needs-rework`.
- Human interaction still exists at explicit stop points (for example, manual merge on
  GitHub), but those stop points do not transfer overall Phase 5-10 ownership away
  from Main Agent.

## Workflow phases

### 1. Plan the topic
1. Capture the topic in `plan/<topic>/<topic>.plan.md`.
2. Lock scope, decisions, and boundaries before execution.
3. Mark the topic as `planned`.

### 2. Prepare the branch
1. Create or repair the execution branch using the repository branch policy.
2. Keep the branch scoped to one topic or one tightly related change family.
3. Do not start creator work from uncommitted chat-only planning notes.

### 3. Creator implementation
1. Hand the topic plan plus relevant repo instructions to the creator.
2. The creator drafts or revises the work until it is `review-ready`.
3. The creator must keep the output within the locked boundaries from the topic plan.
4. Stable-library files such as `README.md` and `VERSION` stay untouched until
   reviewer approval unless the topic plan explicitly says otherwise.

Execution note:
- Phase 3 uses the creator skill as a normal drafting step (`@file:agent-skill-creator`
  in VS Code or `copilot skill agent-skill-creator` in CLI).
- Phase 3 is **not** the independent reviewer-style SubAgent handoff used in Phase 4.
- The explicit SubAgent boundary starts at reviewer pass, where independence from
  the creator context is required.

### 4. Reviewer pass (Two-Layer Independent Review)

The reviewer role is independent from the creator and ensures quality gate before publishing.

#### **New: Two-Layer Review Architecture** (as of v2.0)

This phase now includes **two complementary review layers**:

**Layer 1: Copilot PR Review Agent** (automatic)
- Scans code quality, formatting, style, links, typos
- Produces PR-like comments
- Single scan per phase (not continuous)

**Layer 2: Agent-Skill-Reviewer (SubAgent)** (independent)
- Evaluates SKILL design against `review-checklist.md`
- Reads topic plan to verify scope alignment
- Assesses Copilot feedback for reasonableness
- Returns structured verdict

#### **Three-Step Process**

**Step 4a: Creator Ready**
- SKILL draft complete (all required files present)
- Ready for independent review

**Step 4b: Copilot Scans**
- Copilot Review Agent scans commits one time
- Produces: code quality, formatting, link, typo comments
- Main Agent collects comments

**Step 4c: Reviewer Evaluates**
- SubAgent reads:
  - SKILL folder: `.github/skills/<skill-name>/`
  - Topic plan: `plan/<topic>/<topic>.plan.md`
  - Copilot feedback (for context)
- Produces: JSON verdict with detailed triage

#### In VS Code
- Open a SubAgent directly (within the same Copilot context)
- SubAgent reads the skill folder and topic plan
- Returns: JSON verdict with `approved` or `needs-rework`

#### In Copilot CLI
- Use the `/fleet` orchestrator for independent parallel review
- Command pattern:
  ```
  /fleet 根據 review-checklist.md 與 plan 評審 .github/skills/<skill-name>/
  
  路徑：
    - Skill folder: .github/skills/<skill-name>/
    - Topic plan: plan/<topic>/<topic>.plan.md
  
  評審內容：
    1. 符合 plan 的 Implementation steps？
    2. 例子和參考資料足夠深入？
    3. Copilot 的評論是否都妥當？(address/discuss/skip)
  
  回傳 JSON：
  {
    "verdict": "approved|needs-rework",
    "blocking_issues": [...],
    "copilot_feedback_triage": {
      "ADDRESS": [...],
      "DISCUSS": [...],
      "SKIP": [...]
    }
  }
  ```
- This ensures reviewer logic is separate from creator's session context

#### **Reviewer Report Format (JSON)**

```json
{
  "verdict": "approved|needs-rework",
  "blocking_issues": [
    {
      "issue": "Missing Boundaries section",
      "file": "SKILL.md",
      "fix": "Add Boundaries section per SKILL.md template"
    }
  ],
  "copilot_feedback_triage": {
    "ADDRESS": [
      {
        "comment": "H1 title should use Title Case",
        "location": "SKILL.md line 6",
        "why": "Matches repo standard for consistency"
      }
    ],
    "DISCUSS": [
      {
        "comment": "Consider adding more edge-case examples",
        "optional": true,
        "why": "Would help readers, but not required"
      }
    ],
    "SKIP": [
      {
        "comment": "Use Markdown tables instead of ASCII",
        "why": "Not applicable; already using tables in examples.md"
      }
    ]
  }
}
```

#### Decision routing
1. If verdict is `needs-rework`: 
   - Extract blocking issues
   - Route to creator; move topic to `creator-in-progress`
   - Creator fixes and loops back to Step 4a
2. If verdict is `approved`:
   - Creator applies `ADDRESS` feedback (required)
   - Creator optionally applies `DISCUSS` feedback
   - Creator skips `SKIP` feedback
   - Commit fixes with appropriate message
   - Move topic to `publish-in-progress`

**Note**: Reviewer is not creator. Reviewer does not approve own work.

#### Main Agent Implementation Detail

See `.github/guides/MAIN-AGENT-WORKFLOW.md` → Section "Phase 4: Two-Layer Review" for full orchestration logic including:
- How to invoke SubAgent with correct context
- How to parse JSON reviewer report
- How to route feedback back to creator
- Retry logic and error handling

### 5. Stable library update (if applicable)

Only applies when the skill is entering the stable library (per topic plan).

1. Read the topic plan's `Stable library metadata` section for:
   - README row format (exact table entry to add)
   - VERSION bump direction (MAJOR | MINOR | PATCH)
   - Rationale (why this bump)
2. Update `README.md` per the specified format
3. Update `VERSION` per the specified direction
4. Commit both changes together with skill files

**Note**: Topic plan MUST include the `Stable library metadata` section before this phase.
If topic plan lacks this section, the skill is not intended for stable library.

### 6. Commit, push, and PR (with Pre-Commit Gate)

#### Staging Phase (Phase 5-6: Pre-Commit Checks)

Before committing, validate and stage changes:

1. **Validation** (Phase 5):
   - Verify all required files exist (SKILL.md, examples or reference)
   - Check SKILL.md structure (all 8 required sections)
   - Verify examples have positive and negative cases
   - Run lint/type checks if applicable

2. **Staging** (Phase 6):
   - Stage approved SKILL files
   - If topic plan specifies stable-library update:
     - Stage README.md updates (per `Stable library metadata`)
     - Stage VERSION bump (per `Stable library metadata`)
   - Display final preview of all staged changes

#### **[STOP POINT 1]** Before Commit

Main Agent displays:
```
✅ VALIDATION COMPLETE

Staged changes:
  - .github/skills/<skill-name>/SKILL.md
  - .github/skills/<skill-name>/examples.md
  - README.md (new row added)
  - VERSION (bumped: 0.11.0 → 0.12.0)

Ready to commit + push + open PR on GitHub?
[Y] Proceed
[N] Back to Phase 5 (make more changes)
```

**If [N]**: Discard all staged changes; creator can modify further; ask again when ready

**If [Y]**: Proceed to commit

#### Commit and Push (Phase 6)

1. Commit all approved changes:
   ```bash
   git commit -m "feat: add <skill-name> skill to stable library
   
   - Implements [topic-name] plan
   - SKILL.md with all required sections
   - examples.md with positive/negative cases
   - README.md updated (new row per stable-library metadata)
   - VERSION bumped: [old] → [new]
   
   Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>"
   ```

2. Commit plan status update:
   ```bash
   git commit -m "chore: mark plan status as pr-open
   
   Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>"
   ```

3. Push the branch to remote:
   ```bash
   git push
   ```

4. Open a PR using GitHub CLI:
   ```bash
   gh pr create \
     --title "Add <skill-name> skill to stable library" \
     --body "Implements plan/<topic>/<topic>.plan.md

   See detailed spec in `.github/guides/MAIN-AGENT-WORKFLOW.md`" \
     --base main
   ```

5. Move topic to `pr-open`

### 7. Creator patches on PR with Termination Logic (Phase 7-8: MAX 3 ITERATIONS)

After PR is open, comments may arrive (Copilot reviewer, CI checks, or human review).

#### Direct-apply (no reviewer loop needed)
Creator may directly commit fixes for:
- **Style**: H1 Title Case, code fence type (` ```py `), imports formatting, whitespace
- **Typo**: spelling, grammar, punctuation errors in text
- **Meta**: link corrections, file path updates, example titles, numbering
- **Formatting**: indentation, blank lines, table alignment, list structure

#### Do NOT directly apply (requires reviewer re-check)
- **Trigger logic**: changes to when the skill should be used
- **Core examples**: changes to example's decision flow, assumption set, or logic
- **Missing requirements**: adding imports, dependencies, or prerequisites to examples
- **Process or Boundaries**: changes to skill definition or scope
- **Scope expansion**: new sections, new features, or changed responsibilities
- **Example behavior**: changes that affect whether example code is runnable

#### PR Comment Loop Logic (Phase 7-8)

```
iteration = 0
max_iterations = 3

LOOP:
  1. Fetch latest PR comments from GitHub
  
  2. If NO comments:
     → PR is clean ✅
     → Exit loop, proceed to [STOP POINT 2]
  
  3. If comments exist:
     a. Classify each comment (direct-apply? / needs-reviewer?)
     b. If ALL are direct-apply:
        - Creator applies fixes
        - Commit: git commit -m "fix: address PR feedback on [specific items]"
        - Push: git push
        - iteration += 1
        - Sleep 30 seconds (wait for Copilot to re-scan)
        - Loop back to step 1
     c. If ANY require reviewer re-check:
        - Route back to Phase 4 (invoke reviewer again)
        - Reviewer evaluates new issues
        - If approved: continue Phase 7-8 loop
        - If needs-rework: back to creator Phase 3
  
  4. If iteration >= max_iterations:
     - Display: "Reached max PR iterations (3)"
     - Force exit loop
     - Proceed to [STOP POINT 2]
```

**Iteration Limit**: After 3 loops of direct-apply fixes, Main Agent forces exit (prevents infinite loop).

**Reviewer Re-routing**: If any comment falls outside direct-apply, immediately route back to Phase 4 for re-evaluation.

#### **[STOP POINT 2]** Before Manual Merge

Main Agent displays:
```
✅ PR READY FOR MERGE

PR: #<number> <github.com/.../pull/<number>>
Branch: feature/<username>/<skill-name>
Status: All checks ✅ green
Comments: All addressed ✅
Iterations: 2/3 (within limit)

Next step: Merge manually on GitHub (human responsibility)

After merge, Main Agent will:
  - Run git-post-merge-workflow
  - Run git-release-management (if plan specifies)
  - Update local branches

Ready to merge?
[Y] Go merge on GitHub, then confirm here
[N] Not yet, ask me again later
```

**If [N]**: Main Agent waits, asks again every 30 seconds

**If [Y]**: 
- Instruct user: "Go to [PR link] and click Merge"
- Poll GitHub PR status until merged
- Continue to Phase 9

#### Each direct-apply fix gets a new commit

- Commits are atomic (one logical fix per commit)
- Commit message uses `git-commit-convention`
- Messages must reference the PR comment being fixed

### 8. Merge

Human merges the PR when ready.

### 9. Post-merge local sync

After the merge is confirmed, Main Agent continues the workflow and runs
`git-post-merge-workflow` as a normal post-merge skill step to synchronize local
branches and clean up. This is not a new reviewer-style independent SubAgent
handoff.

### 10. Release (if applicable)

If topic plan specified a release action:
1. Main Agent continues and runs `git-release-management` as a normal release
   skill step to validate release readiness
2. Create annotated tag with semantic version
3. Push tag to remote
4. Move topic to `released`

If no release action: topic is terminal at `merged`.

## Topic plan template

Every skill topic plan must include these fixed sections (11 required):

1. **Goal / outcome**
2. **Scope**
3. **Locked decisions**
4. **Boundaries / exclusions**
5. **Status / allowed transitions**
6. **Artifact paths**
7. **Implementation steps**
8. **Validation / acceptance checks**
9. **Reviewer handoff**
10. **Post-merge / release actions**
11. **Open questions / unresolved items**

### New: Stable library metadata (if applicable)

If the skill is intended to enter the stable library, add this section before Phase 5 (Stable library update):

```markdown
## Stable library metadata

When this skill is approved, it enters the stable library. Specify:

### README update
- Table/section name: Current Skills (or other location per repo policy)
- New row format (exact):
  ```
  | skill-name | Brief description of skill purpose | .github/skills/skill-name/ |
  ```
- Position: Alphabetical order by skill name (or other rule)

### VERSION bump
- Current version: (read from root `VERSION` file)
- Bump direction: MAJOR | MINOR | PATCH
- New version: (calculated)
- Reason: (e.g., "New stable skill" or "Backward-compatible feature addition")

**Example from python-context-management:**
```
### README update
- Table: Current Skills
- New row:
  ```
  | python-context-management | Synchronous context-manager design guidance | .github/skills/python-context-management/ |
  ```
- Position: Between python-class-design and python-error-handling (alphabetical)

### VERSION bump
- Current: 0.11.0
- Direction: MINOR (new stable skill)
- New: 0.12.0
- Reason: New stable skill (non-breaking capability)
```
```

**Note**: Reviewer will validate this section exists and is complete before approving.

## New: Main Agent Orchestration Specification

For detailed Main Agent implementation logic, including phase transitions, checkpoint-based resumability, error handling patterns, and SubAgent communication formats, see:

**`.github/guides/MAIN-AGENT-WORKFLOW.md`** (NEW in v2.0)

This guide covers:
- All 10 phases with executable logic
- Two-layer review architecture (Copilot + Reviewer)
- Pre-commit stop points (avoid fake git state)
- PR loop with max 3 iterations (prevent infinite loops)
- JSON-formatted SubAgent reports (structured communication)
- Checkpoint-based crash recovery
- Ask-user-only error handling (maximum transparency)

**When to use**:
- Main Agent developers: Reference for orchestration logic
- Skill creators: Understand phase flow and human stop points
- Reviewers: Understand what Main Agent expects from SubAgent
- Testers: Use for workflow verification and debugging

## Version History

### v2.0 (2026-04-22)
- **New**: `.github/guides/MAIN-AGENT-WORKFLOW.md` with full 10-phase executable spec
- **New**: Two-layer review architecture (Copilot + agent-skill-reviewer with JSON reports)
- **New**: Pre-commit stop points (Phase 6, BEFORE commit)
- **New**: PR loop max 3 iterations + termination logic
- **New**: Checkpoint-based resumability for crash recovery
- **Enhanced**: Phase 4 section with detailed three-step review process
- **Enhanced**: Phase 6-7 sections with stop points and loop termination
- **Updated**: Reviewer report format (JSON + Markdown)

### v1.0 (earlier)
- Initial workflow definition (single-review model)

## VS Code and CLI Workflow Examples

### VS Code Complete Workflow

Use this pattern in VS Code Copilot with `@file` and `@runSubagent` syntax:

```markdown
# Agent Skill Release Workflow (VS Code)

開發分支命名
  ↓ [User or auto-detect]
@file:git-branch-naming <skill_name>
  ↓
@file:agent-skill-creator <path/to/topic_plan.md>
  → Normal creator skill invocation (not `@runSubagent`)
  → Creator drafts skill files
  → Creator outputs: "This skill is review-ready"
  ↓
@runSubagent run @file:agent-skill-reviewer
  → Reviewer evaluates against review-checklist.md
  → Returns: approved or needs-rework
  ↓ [if approved, continue; if needs-rework, loop back to creator]
交互確認: 讀 topic plan 的 Stable library metadata
  → Confirm README row format
  → Confirm VERSION bump direction
  ↓ [User manual step]
手動或自動化:
  - 更新 README.md 按照 metadata 指定的 row format
  - 更新 VERSION 按照 metadata 指定的 bump direction
  ↓
@file:git-commit-convention
  → Draft or review commit message
  → Stage and commit all changes (skill files + README + VERSION)
  ↓
提交 commit + 開 PR
  → git push
  → gh pr create --base dev
  ↓ [Human review + merge via GitHub]
@file:git-post-merge-workflow
  → Main Agent continues after merge confirmation
  → Clean up local branches
  → Sync with remote
  ↓
@file:git-release-management
  → Main Agent continues with release checks
  → Validate release readiness
  → Create annotated tag
  → Push tag to remote
```

**Key interaction points:**
- After Phase 3 (Creator): User or automation triggers Reviewer
- After Phase 4 (Reviewer): User confirms metadata + manually updates README/VERSION (or automation)
- After Phase 5 (Publish): User decides commit scope (direct-apply rules from Phase 7 apply)
- After Phase 8 (Merge): User confirms merge; Main Agent continues with post-merge and release steps

### CLI Complete Workflow

Use this pattern in Copilot CLI with `/fleet` and `copilot skill` syntax:

```bash
#!/bin/bash
# Agent Skill Release Workflow (CLI)

SKILL_NAME="my-skill"
SKILL_PATH=".github/skills/${SKILL_NAME}"
TOPIC_PLAN="plan/${SKILL_NAME}/${SKILL_NAME}.plan.md"

# Phase 1: Plan (user-created; not automated)
# Expected: $TOPIC_PLAN exists with all 11 sections + Stable library metadata

# Phase 2: Branch
git checkout -b feat/a129924/${SKILL_NAME}

# Phase 3: Creator draft
# Normal skill invocation, not an independent /fleet SubAgent
copilot skill agent-skill-creator ${TOPIC_PLAN}
# Creator outputs: "This skill is review-ready"

# Phase 4: Reviewer (independent SubAgent via /fleet)
/fleet 根據 .github/skills/agent-skill-reviewer/review-checklist.md 評審 ${SKILL_PATH}
# Outputs: approved or needs-rework
# If needs-rework, loop back to Phase 3

# Phase 5: Stable library metadata confirmation (user manual)
echo "Confirm from $TOPIC_PLAN:"
grep -A 10 "## Stable library metadata" ${TOPIC_PLAN}
read -p "Press enter to confirm metadata, then manually update README.md and VERSION"

# Manual steps (or automation if parsing metadata):
# - Update README.md per metadata format
# - Update VERSION per metadata direction

# Phase 6: Commit + Push + PR
git add .
copilot skill git-commit-convention
# Review commit message, then:
git push origin feat/a129924/${SKILL_NAME}
gh pr create --base dev

# Phase 8: Merge (human via GitHub)
# After merge, continue:

# Phase 9: Post-merge workflow (Main Agent continues after merge)
# Normal skill invocation under Main Agent control, not a separate operator-owned handoff
copilot skill git-post-merge-workflow

# Phase 10: Release (if applicable; still Main Agent-controlled)
# Normal skill invocation under Main Agent control
copilot skill git-release-management
# Tag and push
```

**Key differences from VS Code:**
- `/fleet` launches independent SubAgent (vs `@runSubagent` in VS Code)
- Metadata confirmation is user manual (could be automated with parsing)
- Uses `copilot skill` command instead of `@file:` syntax
- Phase 9-10 remain Main Agent phases even when the CLI surface uses
  `copilot skill ...` syntax for the concrete skill invocation

### Tool Mapping

| VS Code | CLI | Purpose |
|---|---|---|
| `@file:<skill>` | `copilot skill <skill>` | Invoke skill |
| `@runSubagent` | `/fleet` (+ natural language) | Independent SubAgent |
| `@file:` file reference | shell variable + path | Pass context |
| Inline @runSubagent | Separate command | Sequence steps |

---

## Implementation Notes

1. **Topic plan metadata is mandatory** when skill enters stable library
   - Must include README row format, VERSION direction, rationale
   - Both VSCode and CLI workflows expect this section

2. **Direct-apply boundary** (Phase 7) applies to both environments
   - VSCode and CLI handle PR comments the same way
   - Only style/typo/meta fixes directly applied; others route back to reviewer

3. **Status model** is repo-visible (not session-specific)
   - topic plan status field updated consistently across environments
   - Both environments read the same review-checklist.md
4. **Phase 9-10 ownership** stays with Main Agent
   - post-merge and release are follow-up phases in the same workflow
   - command syntax does not change the actor model

## VS Code and CLI Notes

- VS Code may orchestrate multiple main/sub-agents from one broad task, but the
  workflow still depends on repo-visible artifacts rather than hidden tab state.
- CLI may launch separate agents more explicitly via `/fleet`, but the workflow should read
  the same topic plan and use the same status model.
- In both environments, Phase 9-10 are Main Agent continuation steps; only the
  reviewer pass requires the explicit independent SubAgent boundary.
- Worktrees are optional execution mechanics, not part of the canonical contract.

## Boundaries
- This document does not define one mandatory shell command sequence.
- It does not replace `.github/copilot-instructions.md` or skill-local rules.
- It does not let creator and reviewer collapse into one role.
- It does not treat PR comments as a replacement for the reviewer verdict.
