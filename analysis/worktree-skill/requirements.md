# worktree-skill requirements baseline

Status: FROZEN
Topic: `worktree-skill`
Target skill: `.github/skills/worktree-manager/`

## Problem statement

This repository needs a single-purpose Agent Skill that manages Git worktree
lifecycle operations safely enough for agent-driven task execution. The skill
must reduce accidental deletion, hidden state loss, and active-working-set
pollution while remaining portable and copy-friendly inside the repository's
skill library.

## Primary actor

- Primary actor: Main Agent acting as the planning / coordination agent
- Secondary actor: Human operator who confirms destructive actions or resolves
  ambiguous worktree state

## In-scope user intents

- Create a managed task worktree from the repository's target branch
- Inspect known worktrees and receive a safe recommendation
- Release a worktree from the active working set without implying deletion
- Remove a worktree only after explicit destructive-action approval

## Non-goals

- Feature implementation inside the worktree
- Automatic merge, push, branch deletion, or release-tag handling
- `.env.local`, port, database, or compose bootstrapping in v1
- Automatic destructive handling for unmanaged worktrees
- Repository-internal worktree placement such as `<repo>/.github/worktrees/...`

## Managed worktree path convention

Managed worktrees MUST use:

`../<repo-name>.worktrees/<prefix>-YYYYMMDD-<worktree-name>`

Default prefix:

`agent`

Example:

`../agent-skills.worktrees/agent-20260507-worktree-manager`

Path policy notes:

- Managed worktrees live outside the repository root
- `<prefix>` defaults to `agent` unless the human explicitly overrides it
- `<worktree-name>` is a task slug or branch slug

## Lifecycle vocabulary

- `get-worktree` = inspect current state
- `release worktree` = safely remove the worktree from the active working set
  without implying deletion
- `remove worktree` = destructive removal of the worktree directory and Git
  worktree registration

## Measurable requirements

| ID | Actor | Condition | Observable result | Metric / decision rule | Failure meaning |
| --- | --- | --- | --- | --- | --- |
| R1 | Main Agent | The current directory is a valid Git repository and the user asks to create a task worktree | A new worktree exists at the canonical managed path, a corresponding branch exists, and the response includes the next-step prompt for continuing work inside that worktree | PASS only if the path exists, the worktree is attached to the intended branch, and the returned output includes the worktree path, branch, and immediate next action | The agent may continue work in the wrong location or with an ambiguous branch state |
| R2 | Main Agent | The user asks to inspect worktrees | The response lists each relevant worktree with path, branch, status, dirty state, recommendation, reason, and next safe action | PASS only if the output contains `path`, `branch`, `status`, `dirty state`, `recommendation`, `reason`, and `next safe action` for every reported worktree | The operator cannot safely decide whether to keep, release, remove, or prune a worktree |
| R3 | Main Agent | The user asks to release a worktree | The response records release evidence, confirms whether the worktree can leave the active working set, and never treats release as deletion by default | PASS only if the fixed release evidence fields are filled and `destructive_action_allowed` remains `false` unless a separate remove path is explicitly authorized | The agent may silently turn a safe offboarding action into a destructive delete |
| R4 | Human operator + Main Agent | The user explicitly asks to remove a worktree | The agent performs or recommends removal only after safety checks pass and human destructive intent is explicit | PASS only if the worktree passes remove safety checks and the user has explicitly allowed destructive action | Uncommitted, untracked, or unmerged state could be destroyed |
| R5 | Main Agent | A worktree is evaluated for ownership | The skill labels the worktree as managed or unmanaged using path policy first | PASS only if managed status is decided from canonical path family; metadata and plan context may inform notes but do not replace path policy in v1 | The skill may over-claim ownership and perform unsafe actions on unrelated worktrees |
| R6 | Main Agent | The user triggers the skill outside a valid Git repository | The skill blocks the operation and says the user must switch to the correct repository first | PASS only if the operation stops with a blocked result and no worktree mutation occurs | The skill may create or inspect state against the wrong directory |
| R7 | Main Agent | A worktree is dirty, has untracked files, has unpushed commits, uses detached HEAD, has unknown branch state, or is locked | The skill returns `needs-human-decision` instead of guessing a safe destructive action | PASS only if ambiguous or risky states are surfaced explicitly and no destructive path proceeds automatically | The skill may hide risk and destroy state that still matters |
| R8 | Main Agent | A create, release, or inspect path touches files that may be shared across multiple worktrees | The skill reminds the operator that shared-file coordination belongs to the planner / observer role | PASS only if the response surfaces the coordination warning when shared-file risk is present or suspected | Parallel worktrees may produce uncontrolled edits to shared planning or governance files |
| R9 | Main Agent + Human operator | Create is requested but the preferred branch name already exists | The skill does not silently reuse the branch; it asks whether to reuse the existing lineage or create a new name | PASS only if the response presents a reuse-or-rename decision instead of silently proceeding | The new worktree may attach to the wrong task lineage |
| R10 | Main Agent | `get-worktree` inspects a missing path that Git still records as a worktree | The recommendation becomes `prune-candidate` with a reason and next safe action | PASS only if the output distinguishes a stale registration from a normal live worktree | The operator may misread stale metadata as an active task workspace |

## Recommendation matrix

| Condition | Recommendation | Reasoning expectation |
| --- | --- | --- |
| clean + branch still active + task ongoing | `keep` | worktree is still an active workspace |
| clean + task done + merged or explicitly abandoned | `release` | active use ended, but destructive removal is still a separate step |
| clean + already released / stale / no longer needed | `remove` | safe candidate for destructive cleanup once human intent is explicit |
| dirty | `needs-human-decision` | modified tracked files need review |
| untracked files | `needs-human-decision` | local state may still matter |
| unpushed commits | `needs-human-decision` | local commits may be lost or unpublished |
| branch not found / detached HEAD | `needs-human-decision` | lineage is ambiguous |
| unmanaged / unknown ownership | `needs-human-decision` | destructive ownership cannot be assumed |
| path missing but Git still records worktree | `prune-candidate` | metadata likely stale |
| locked worktree | `needs-human-decision` | another process or policy may own the state |

## Release evidence format

Release decisions MUST record:

```yaml
release_evidence:
  task_status: completed | paused | abandoned | unknown
  worktree_clean: true | false | unknown
  untracked_files: true | false | unknown
  branch_status: merged | unmerged | no_branch | unknown
  pr_status: merged | closed | open | none | unknown
  push_status: pushed | unpushed | no_remote | unknown
  user_intent: release | remove | keep | unknown
  destructive_action_allowed: true | false
  evidence_notes:
    - "<short note>"
```

Minimum release gate:

- `worktree_clean = true`
- `untracked_files = false`
- `branch_status = merged` OR `pr_status = merged` OR the human explicitly says
  the task is abandoned / does not need merge
- `destructive_action_allowed = false` by default

Release MUST NOT imply deletion. Remove requires a separate explicit destructive
gate.

## Unmanaged worktree policy

Unmanaged worktree = a worktree that does not match the canonical managed path
family.

Allowed actions:

- list
- inspect
- report status
- detect dirty / untracked / branch / HEAD state
- recommend next action

Forbidden automatic actions:

- release
- remove
- delete directory
- prune
- rename branch
- delete branch
- assume the task is done

Default rule:

- unmanaged worktrees are inspect-only until the human explicitly authorizes a
  destructive path

## Resolved contradictions

1. **Release vs remove**
   - Conflict: users may say "clean up" when they mean either safe offboarding or
     deletion
   - Resolution: `release` is non-destructive offboarding; `remove` is the
     separate destructive path
2. **Repository-local convenience vs workspace isolation**
   - Conflict: `<repo>/.github/worktrees/...` feels convenient but mixes
     workspaces with repo metadata and tool scanning
   - Resolution: managed worktrees live outside the repository root
3. **Instruction-only simplicity vs script determinism**
   - Conflict: scripts could reduce variation, but destructive automation
     increases maintenance and risk
   - Resolution: v1 stays instruction-first; only a read-only status script may
     be considered later if a plan repair justifies it

## Extreme-boundary checks

- target path already exists but is not a worktree
- branch already exists without the intended worktree lineage
- worktree is dirty, detached, diverged, or locked
- Git still records the worktree but the path is gone
- request arrives outside a repository root
- shared planning files may be edited from multiple worktrees
- unmanaged worktree is requested for destructive cleanup

## Freeze decision

This baseline is ready for technical translation.
