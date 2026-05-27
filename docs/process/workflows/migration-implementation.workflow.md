# Migration Implementation Workflow

## Purpose
Execute an approved migration topic through implementation, review, overlay
gates, and migration-status confirmation without expanding the approved scope.
Stop at `MIGRATION_STATUS_CONFIRMED` and hand later publish actions to the
publish workflow.

## Preconditions
- Must follow:
  - `docs/process/policies/migration-workflow-common-policy.md`
- If running inside `agent-skills` transition-era migration:
  - `docs/process/overlays/agent-skills-transition-overlay.md`
- Migration topic, risk level, approved plan, and target branch are already
  provided.
- Worktree is already prepared for the topic.

## Inputs
- migration topic
- risk level
- approved topic plan
- target branch
- prepared worktree

## Outputs
- migration implementation completed within approved scope
- review result captured
- repository-specific overlay gate result recorded when an overlay is bound
- migration status recorded
- topic is ready for publish handoff

## States
- `READY_TO_IMPLEMENT`
- `IMPLEMENTED`
- `REVIEW_REQUESTED`
- `REVIEW_PASSED`
- `OVERLAY_GATES_REQUIRED`
- `OVERLAY_GATES_PASSED`
- `OVERLAY_GATES_BLOCKED`
- `OVERLAY_GATES_DEFERRED`
- `MIGRATION_STATUS_CONFIRMED`
- `FINISHED`
- `HUMAN_FEEDBACK_REQUIRED`

## Step Sequence
1. Load the approved topic plan.
2. Implementer executes the migration.
3. Reviewer reviews the migrated output.
4. Run repository-specific overlay gates when an overlay is bound.
5. Confirm migration status.
6. Stop and hand off to publish workflow.
7. Finish.

## Stop Rules
Stop with `human-feedback-required` if:

- approved plan is missing
- target branch is missing
- worktree is not prepared
- implementation modifies out-of-scope files
- reviewer finds blocking behavior drift after allowed rounds
- required overlay gate fails after allowed rounds
- required overlay gate cannot produce a clear pass, block, or defer result
- migration status cannot be classified clearly

## Role Responsibility Boundaries
- Implementer performs the migration under the approved plan.
- Reviewer judges whether the implemented result stays within contract, and
  reviewer approval must remain independent of Main Agent orchestration.
- Main Agent stops this workflow at `MIGRATION_STATUS_CONFIRMED` and hands off
  any later commit, push, or PR progression to the publish workflow.
- Repository-specific overlays may require stricter readability or semantic
  parity gates, but those gates do not belong in this generic workflow body.

## Required `status.json` Fields
- `workflow`: `migration-implementation`
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

## Acceptance Criteria
- Implementation stayed within the approved topic scope.
- Reviewer pass completed within the allowed loop cap.
- Overlay-bound validation, when required, passed or was explicitly routed to a
  terminal blocking or defer state.
- Migration status was recorded with one of:
  - `moved`
  - `copied`
  - `remediated`
  - `deferred`
  - `blocked`
  - `skipped`
- Topic reached `MIGRATION_STATUS_CONFIRMED` and is ready for publish handoff.

## What Not To Do
- Do not select a migration topic.
- Do not infer a missing approved plan.
- Do not expand the topic into redesign.
- Do not commit, push, or open a Ready PR from this workflow body.
- Do not hardcode repository-specific overlay gates into the common workflow
  contract.
