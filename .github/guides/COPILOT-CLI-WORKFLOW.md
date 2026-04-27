---
description: Practical Copilot CLI workflow guide for this repository: reduce repeated context, choose the right command lane, and pair `workflow-gate` with `/pr`, `/review`, `/fleet`, and `/tasks`.
---

# Copilot CLI Workflow

This guide is the practical operating layer for using Copilot CLI in this
repository without repeatedly pasting the same workflow context.

It assumes the repository workflow remains canonical in:
- `plan/agent-handoff-workflow.md`
- `.github/guides/MAIN-AGENT-WORKFLOW.md`

Use this guide when you want shorter prompts, clearer command routing, and fewer
repeated `skill-context` blocks.

## Core idea

In this repository, the safest prompt is usually **short but anchored**:

- name the exact topic plan, skill folder, PR, or branch
- say the current phase if it matters
- say the required output shape if review or triage is involved

That is usually enough. You do **not** need to keep pasting the same workflow
contract or full skill contents when the relevant repo-visible artifact already
exists.

## Use `workflow-gate` as the default entry point

Use `/agent` and select `workflow-gate` when:

- you know the repository workflow matters, but the next lane is still unclear
- you want the agent to decide whether the next step is plan review, creator
  work, `/review`, `/pr`, or post-merge handling
- you want shorter prompts without dropping workflow stop points

Good examples:

```text
Use workflow-gate on @plan/cli-workflow-alignment/cli-workflow-alignment.plan.md and move to the correct next phase.
```

```text
Use workflow-gate for the current branch. If the plan is approved, continue until the next required human stop point.
```

## When to use `/pr`

Use `/pr` when the work is already attached to a pull request or should be
evaluated through the PR state:

- PR created and you want the current comments or checks handled
- the user says "PR 下來了 你處理吧"
- the branch is merge-adjacent and PR state matters more than raw local diff
- post-merge follow-up needs the actual PR reference

Use `/pr` **before** improvising from local assumptions, because it binds the
conversation to the real PR state for the current branch.

Good examples:

```text
/pr
處理目前 PR 的 review comments，只處理 blocking items；若需要 reviewer re-entry，請明講。
```

```text
/pr
看目前 PR 的 checks 和 comments，幫我判斷是直接修、回 reviewer，還是準備 merge handoff。
```

## When to use `/review`

Use `/review` when the question is about the **current changes themselves**:

- the branch diff needs a contract or logic pass
- you want an opinion on whether the current edits are ready for the next phase
- you want a diff-oriented review before or alongside PR work

In this repository, `/review` is especially useful when the branch changed but
the work has not yet reached the formal reviewer handoff, or when you want a
fast diff pass before invoking a dedicated repo reviewer path.

Good examples:

```text
/review
Focus on workflow or contract-breaking issues only. Ignore style unless it changes meaning.
```

```text
/review
Review the current changes against @plan/cli-workflow-alignment/cli-workflow-alignment.plan.md and flag only issues that block review-ready.
```

## When to use `/fleet`

Use `/fleet` when independence matters or parallel review helps:

- a topic plan needs an independent verdict before execution proceeds
- a draft should not be graded by the same agent that just wrote it
- multiple review threads can be checked in parallel

In this repository, `/fleet` is the cleanest way to preserve the
creator-versus-reviewer boundary.

Good examples:

```text
/fleet 根據 plan-reviewer 的規則評審 @plan/cli-workflow-alignment/cli-workflow-alignment.plan.md，只回傳 JSON verdict。
```

```text
/fleet 根據 reviewer checklist 與 plan 評審目前 draft，確認 artifact paths、examples 深度、以及是否需要 needs-rework。
```

## When to use `/tasks`

Use `/tasks` when background work may already exist:

- a shell command is still running
- an independent reviewer was launched earlier
- you are not sure whether the agent is waiting, idle, or finished

This prevents duplicate review runs and redundant shell work.

Good examples:

```text
/tasks
```

```text
/tasks
Check whether the reviewer or shell work for this topic is still running before starting another pass.
```

## Four common repository scenarios

### 1. Plan / workflow gate

Use when a topic plan exists and the next phase matters more than immediate
editing.

Recommended pattern:

```text
Use workflow-gate on @plan/<topic>/<topic>.plan.md. Decide the correct next workflow phase and continue until a required stop point.
```

### 2. Review-ready validation

Use when draft files exist and you want to know whether they should enter the
independent reviewer step.

Recommended pattern:

```text
/review
Check the current diff against @plan/<topic>/<topic>.plan.md and flag only issues that block review-ready.
```

If an independent verdict is required, escalate to `/fleet` rather than asking
the same agent to self-approve.

### 3. PR comment triage

Use when the PR already exists and the next step depends on actual PR comments
or checks.

Recommended pattern:

```text
/pr
Handle the current PR comments. Apply direct fixes when safe; if the feedback changes review ownership, say so explicitly.
```

### 4. Post-merge follow-up

Use only **after** a human explicitly says the PR was merged.

Recommended pattern:

```text
The PR is manually merged. Resume the workflow from post-merge sync only.
```

At this point, the workflow may use `/pr` for concrete PR state and `/tasks` if
background work already exists, but must still respect STOP POINT 2:
there is no silent waiting for merge completion.

## When "請繼續" is enough

Short follow-ups such as these are enough only when all three stay unchanged:

1. the current workflow phase
2. the target artifact set
3. the required output shape

Good examples:

- `請繼續`
- `你再看一次，還是只看 workflow transitions`
- `處理剩下的 blocking issues`

## When short follow-ups are **not** enough

Restate scope explicitly when any of these changed:

- the phase changed, such as creator -> reviewer or PR -> post-merge
- the target artifact changed, such as from topic plan to skill folder
- the output shape changed, such as from prose review to JSON verdict
- a stop point was crossed and human confirmation resumed the workflow

Better examples:

```text
PR 已經 merge。只從 post-merge sync 繼續，不要重跑 creator 或 review。
```

```text
現在不要再看 diff，改成對 @plan/<topic>/<topic>.plan.md 做獨立 plan review，只回傳 JSON。
```

## Replace repeated `skill-context` blocks with anchored prompts

Instead of repeatedly pasting long `skill-context` blocks, prefer:

- the skill name
- the target path
- the required output shape

Better patterns:

```text
Use plan-reviewer on @plan/cli-workflow-alignment/cli-workflow-alignment.plan.md and return JSON only.
```

```text
Use agent-skill-reviewer on @.github/skills/python-decorators/ with @plan/python-decorators/python-decorators.plan.md as the contract.
```

```text
Use git-post-merge-workflow for the current branch after merge confirmation. Do not continue past the next human stop point.
```

## Boundaries

- This guide does not replace `plan/agent-handoff-workflow.md`.
- This guide does not redefine what each specialized skill owns.
- This guide does not try to document every Copilot CLI feature.
- This guide is intentionally limited to the command lanes that most directly
  improve this repository's current workflow: `/pr`, `/review`, `/fleet`, and
  `/tasks`.
