# Migration Workflow Common Policy

## Purpose
Define the generic invariants shared by all migration workflows.

This policy is repository-agnostic. It must stay reusable across topics and
repositories.

## Scope
- Applies to reusable migration workflow execution contracts.
- Applies before workflow-specific steps begin and throughout execution.
- Does not define repository-specific transition constraints.

## Topic Selection Boundary
- Workflow must not select migration topics by itself.
- Migration topic, risk level, approved plan, and target branch are assumed to
  be provided before workflow execution starts.
- If any of those inputs are missing, the workflow must stop with
  `human-feedback-required`.

## Shared Invariants

### Branch and plan prerequisites
- Target branch must be decided before worktree creation.
- Approved plan must exist before implementation.
- Worktree lifecycle must be explicit from creation through cleanup.

### Scope control
- Workflow must not invent a new migration scope.
- Workflow must stop if scope expansion is required.
- Workflow must keep commit scope bounded by topic.

### Role iteration control
- Implementer, creator, planner, and reviewer loops must not exceed 3 rounds.
- If a role loop reaches the 3rd round, that round must converge.
- The 3rd round must end with one of:
  - `accepted`
  - `blocked`
  - `deferred`
  - `human-feedback-required`
- No 4th autonomous correction round is allowed.

### Blocking and escalation
- If the same blocking issue appears twice, the workflow must stop and request
  human feedback.
- `human-feedback-required` must end autonomous workflow progress until a human
  explicitly resumes it.

### Commit boundary
- Commit must be by topic.
- Unrelated migration work must not be mixed into the same commit or ordered
  commit set.

## Role Execution Model
- Planner is the workflow's decision and scope authority.
- Implementer, creator, reviewer, and checker roles are bounded execution or
  evaluation roles.
- Bounded roles must not select migration topics, change approved plans, expand
  scope, or redefine repository policy.
- If a bounded role detects missing inputs, scope expansion, repeated blocking
  issues, or policy conflict, it must return `human-feedback-required`.

## Required `status.json` Fields
Each workflow run must define a machine-readable status contract at
`.workflow-runs/<run-id>/status.json` with at least these fields:

- `workflow`
- `topic`
- `target_branch`
- `worktree`
- `current_state`
- `result`
- `rounds`
- `blocking_reason`
- `human_feedback_required`
- `last_completed_step`
- `next_step`

Workflow-specific files may add fields, but must not remove or rename the
required common fields.

### `status.json` Field Naming Conventions

- JSON field names use `snake_case` (e.g., `current_state`,
  `human_feedback_required`).
- `current_state` values use `SCREAMING_SNAKE_CASE` to match workflow state
  identifiers (e.g., `HUMAN_FEEDBACK_REQUIRED`, `FINISHED`).
- `result` values use lowercase with hyphens as needed (e.g., `moved`,
  `remediated`, `human-feedback-required`). Valid common values include
  `accepted`, `blocked`, `deferred`, and `human-feedback-required`.
  Workflow-specific values are allowed in addition to these.
- `human_feedback_required` is a boolean (`true` / `false`). Set it to `true`
  when `current_state` is `HUMAN_FEEDBACK_REQUIRED` or when any declared stop
  condition is triggered.

## Stop Conditions
Stop with `human-feedback-required` if:

- migration topic is missing
- risk level is missing
- approved plan is missing
- target branch is missing
- scope expansion is required
- the same blocking issue appears twice
- the workflow reaches a declared terminal escalation state

## What This Policy Must Not Do
- Must not encode repository-specific path semantics.
- Must not encode platform-specific parity or readability checks.
- Must not redefine any repository-specific overlay rules.
- Must not replace a workflow-specific state model.
