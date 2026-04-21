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
| Publisher / release actor | Handle commit, push, PR, review-comment triage, merge follow-up, and release/version actions | Change planning intent retroactively without updating the plan |

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
| `publish-in-progress` | Approved work is being committed, pushed, and prepared for PR / stable-surface updates | Publisher / release actor | `pr-open`, `merged` |
| `pr-open` | PR is open and comment triage is active | Publisher / release actor | `needs-rework`, `merged` |
| `merged` | Changes are merged; local sync and optional release follow-up remain | Publisher / release actor / human | `released`, terminal |
| `released` | Version and tag actions are complete when the change requires them | Publisher / release actor | terminal |

Notes:
- `merged` is terminal for changes that do not require a release action.
- `released` is required when a merge also performs a repository release step.
- Reviewer comments on an open PR may send the work back to `needs-rework`.

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

### 4. Reviewer pass (Independent SubAgent review)

The reviewer role is independent from the creator and ensures quality gate before publishing.

#### In VS Code
- Open a SubAgent directly (within the same Copilot context)
- SubAgent reads the skill folder and applies `review-checklist.md`
- Returns: `approved` or `needs-rework` with explicit reasoning

#### In Copilot CLI
- Use the `/fleet` orchestrator for independent parallel review
- Command pattern:
  ```
  /fleet 根據 .github/skills/agent-skill-reviewer/review-checklist.md 評審 .github/skills/<skill-name>/
  
  決策：approved 或 needs-rework
  (附 blocking issues 如需修正)
  ```
- This ensures reviewer logic is separate from creator's session context

#### Decision routing
1. If verdict is `needs-rework`: route feedback to creator; move topic to `creator-in-progress`
2. If verdict is `approved`: proceed to next phase; move topic to `publish-in-progress`

**Note**: Reviewer is not creator. Reviewer does not approve own work.

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

### 6. Commit, push, and PR

1. Commit all approved changes (skill files + stable-library updates if applicable)
   using `git-commit-convention` skill
2. Push the branch to remote
3. Open a PR against the default branch
4. Move the topic to `pr-open`

### 7. Creator patches on PR (Direct application only)

After PR is open, comments may arrive (Copilot reviewer, CI checks, or human review).

#### Direct-apply (no reviewer loop needed)
Creator may directly commit fixes for:
- **Style**: H1 Title Case, code fence type (` ```py `), imports formatting, whitespace
- **Typo**: spelling, grammar, punctuation errors in text
- **Meta**: link corrections, file path updates, example titles, numbering
- **Formatting**: indentation, blank lines, table alignment, list structure

#### Do NOT directly apply (requires reviewer re-check)
- **Trigger logic**: changes to when the skill should be used
- **Core examples**: changes to core decision logic in SKILL.md or examples.md
- **Process or Boundaries**: changes to skill definition or scope
- **Scope expansion**: new sections, new features, or changed responsibilities

If a comment requires changes outside direct-apply scope, open a discussion or route back to reviewer.

Each direct-apply fix gets a new commit or amend (per your preference).

### 8. Merge

Human merges the PR when ready.

### 9. Post-merge local sync

Run `git-post-merge-workflow` skill to synchronize local branches and clean up.

### 10. Release (if applicable)

If topic plan specified a release action:
1. Run `git-release-management` skill to validate release readiness
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

## Fixed reviewer report schema
Reviewer output should use this shape:

```markdown
Verdict: approved | needs-rework

Blocking issues
- none
- or a short numbered list of blocking issues

Evidence
| Check | Result | Evidence | Notes |
| --- | --- | --- | --- |
| Required core | Pass / Fail | file paths or sections | concise rationale |
| Scope / boundaries | Pass / Fail | file paths or sections | concise rationale |
| Example depth | Pass / Fail | file paths or sections | concise rationale |
| Portability / independence | Pass / Fail | file paths or sections | concise rationale |

Optional polish
- short non-blocking suggestions only

Handoff
- if `approved`: safe to publish / merge according to the topic plan
- if `needs-rework`: return to creator with the blocking issues only
```

## VS Code and CLI notes
- VS Code may orchestrate multiple main/sub-agents from one broad task, but the
  workflow still depends on repo-visible artifacts rather than hidden tab state.
- CLI may launch separate agents more explicitly, but the workflow should read
  the same topic plan and use the same status model.
- Worktrees are optional execution mechanics, not part of the canonical contract.

## Boundaries
- This document does not define one mandatory shell command sequence.
- It does not replace `.github/copilot-instructions.md` or skill-local rules.
- It does not let creator and reviewer collapse into one role.
- It does not treat PR comments as a replacement for the reviewer verdict.
