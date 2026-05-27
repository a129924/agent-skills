# Migration Publish Handoff Workflow

## Purpose
Explicitly hand off one migration topic that already reached
`MIGRATION_STATUS_CONFIRMED` into the publish half of the workflow without
implicitly authorizing commit, push, or Ready PR creation.

## Preconditions
- Must follow:
  - `docs/process/policies/migration-workflow-common-policy.md`
- A repo-visible `migration-implementation` run already exists for the topic and
  is confirmed at `MIGRATION_STATUS_CONFIRMED`.
- The topic branch, target branch, and prepared worktree are already known.
- The approved topic contract artifacts needed for publish handoff are already
  identifiable.

## Inputs
- one migration topic already confirmed at `MIGRATION_STATUS_CONFIRMED`
- source `migration-implementation` run id
- topic branch
- target branch
- prepared worktree

## Outputs
- repo-visible publish handoff run created for one topic
- planner/publish alignment evidence recorded
- publish readiness artifact completeness recorded against the approved topic
  contract
- topic enters `publish-in-progress` as a topic-local handoff state only
- topic stops at topic-local `STOP POINT 1`
- publish handoff remains distinct from topic close
- no commit, push, or Ready PR occurs until a later explicit human approval

## States
- `READY_FOR_PUBLISH_HANDOFF`
- `PUBLISH_ALIGNMENT_IN_PROGRESS`
- `PUBLISH_IN_PROGRESS`
- `STOP_POINT_1_PENDING`
- `COMMITTED`
- `PUSHED`
- `READY_PR_OPENED`
- `FINISHED`
- `HUMAN_FEEDBACK_REQUIRED`

## Step Sequence
1. Load one topic already confirmed by a source `migration-implementation` run.
2. Run Main Agent planner/publish alignment against the approved topic contract.
3. Record the exact publish-ready artifact set for that one topic and whether it
   is complete against the approved contract, including any required `step.md`,
   correction artifacts, review log, and stable-surface metadata declared by
   the topic.
4. Enter `publish-in-progress` as the topic-local publish handoff state, not as
   topic close.
5. Stop at topic-local `STOP POINT 1`.
6. After a later explicit human approval for that topic, commit by topic.
7. Push the topic branch.
8. Open a Ready PR for that topic.
9. Finish.

## Stop Rules
Stop with `human-feedback-required` if:

- source `migration-implementation` run is missing
- source run is not at `MIGRATION_STATUS_CONFIRMED`
- planner alignment finds branch, worktree, or artifact drift
- the publish-ready artifact set is incomplete against the approved topic
  contract
- diff expands outside the approved topic write set
- shared governance or runtime surfaces would need to be touched to publish
- a later publish approval message is missing or ambiguous for that topic

## Role Responsibility Boundaries
- Implementer and reviewer work remains owned by the already completed source
  `migration-implementation` run.
- Main Agent owns publish handoff alignment, STOP POINT 1 enforcement, and
  later commit / push / Ready PR progression.
- Publish handoff records topic-local handoff state only; it must not claim
  topic-close truth or substitute for a later required `summary artifact`.
- Each topic must be published independently; no shared commit, push, or PR is
  authorized across topics.

## Required `status.json` Fields
- `workflow`: `migration-publish-handoff`
- `source_workflow_run`
- `topic`
- `branch`
- `target_branch`
- `worktree`
- `current_state`
- `result`
- `blocking_reason`
- `human_feedback_required`
- `last_completed_step`
- `next_step`
- `stop_point_1_approved`

## Acceptance Criteria
- Publish handoff references exactly one source `migration-implementation` run.
- Topic branch, target branch, worktree, and artifact set match the approved
  topic contract.
- Artifact completeness is recorded explicitly before the topic enters
  `publish-in-progress`.
- Topic reaches `STOP_POINT_1_PENDING` without committing, pushing, or opening
  a PR.
- Publish handoff is recorded as a topic-local handoff state and not as topic
  close.
- `stop_point_1_approved` remains `false` until a later explicit human approval
  for that topic.

## What Not To Do
- Do not re-run implementation or review work.
- Do not overwrite the source `migration-implementation` run state.
- Do not treat handoff creation as implicit publish approval.
- Do not treat publish handoff as topic close or as a replacement for a later
  required close `summary artifact`.
- Do not combine multiple topics into one publish handoff run.
