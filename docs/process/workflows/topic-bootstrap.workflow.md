# Topic Bootstrap Workflow

## Purpose
Create the worktree and repo-visible planning contract required for a migration
topic to begin execution safely.

## Preconditions
- Must follow:
  - `docs/process/policies/migration-workflow-common-policy.md`
- If running inside `agent-skills` transition-era migration:
  - `docs/process/overlays/agent-skills-transition-overlay.md`
- Migration topic, risk level, approved plan input model, and target branch are
  already provided.
- Workflow is authorized to prepare the topic environment, not to implement the
  migration itself.

## Inputs
- migration topic
- risk level
- target branch
- planning inputs required to write or validate the approved topic plan

## Outputs
- worktree routing result recorded before lifecycle mutation
- worktree created from the decided target branch when required
- existing valid worktree reuse decision recorded when no new worktree is
  created
- first planning artifact set written or validated:
  - `analysis/<topic>/requirements.md`
  - `plan/<topic>/<topic>.plan.md`
  - `plan/<topic>/<topic>.step.md`
- plan review result captured
- planner final review completed
- plan artifacts committed by topic

## States
- `TOPIC_INPUTS_READY`
- `WORKTREE_ROUTING_CONFIRMED`
- `WORKTREE_CREATED`
- `PLAN_DRAFTED_OR_VALIDATED`
- `PLAN_REVIEW_REQUESTED`
- `PLAN_REVIEW_PASSED`
- `PLANNER_FINAL_REVIEW_PASSED`
- `COMMITTED`
- `FINISHED`
- `HUMAN_FEEDBACK_REQUIRED`

## Step Sequence
1. Confirm the target branch.
2. Route worktree handling first: either create the worktree from the target
   branch or record that no lifecycle mutation is required because the current
   context is already valid.
3. Write or validate the first planning artifact set following the repository
   topic-plan contract basis. The first batch must include:
   - `analysis/<topic>/requirements.md`
   - `plan/<topic>/<topic>.plan.md`
   - `plan/<topic>/<topic>.step.md`
   If intent, scope, or boundary ambiguity remains, stop for clarification. If
   those inputs are already frozen, no separate boundary-alignment step is
   required.
4. Review the plan.
5. Complete planner final review.
6. Commit plan artifacts by topic.
7. Finish.

## Stop Rules
Stop with `human-feedback-required` if:

- migration topic is missing
- risk level is missing
- target branch is missing
- worktree routing cannot determine a safe lifecycle action
- required worktree creation fails
- approved plan input model is incomplete
- plan scope is unclear
- any required first-batch planning artifact is missing
- reviewer says the plan is not implementation-ready after allowed rounds
- planner final review finds scope drift

## Role Responsibility Boundaries
- Planner defines or validates the topic plan contract.
- Reviewer judges plan readiness, must not implement the migration, and must be
  independent of Main Agent self-approval.
- An independent worktree role or subAgent handles worktree routing and any
  required lifecycle action.
- Main Agent manages workflow orchestration, records the worktree routing
  result, and manages later commit progression and commit boundary.
- This workflow must not perform migration implementation work.

## Required `status.json` Fields
- `workflow`: `topic-bootstrap`
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
- Worktree routing completed first, and any required lifecycle action was
  resolved safely.
- Worktree exists and is based on the decided target branch when creation was
  required.
- Existing valid worktree reuse was explicitly recorded when no new worktree
  creation was required.
- Topic plan exists or was explicitly validated as acceptable input.
- The first planning batch contains at least `requirements.md`, `plan.md`, and
  `step.md` at the repo-visible topic paths.
- Plan review completed within the allowed loop cap.
- Planner final review completed without unresolved scope drift.
- Plan artifacts were committed by topic.

## What Not To Do
- Do not select the migration topic.
- Do not infer missing risk level or target branch.
- Do not implement migration changes.
- Do not add release actions.
