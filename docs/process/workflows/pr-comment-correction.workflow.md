# PR Comment Correction Workflow

## Purpose
Handle PR comments through bounded correction routing so feedback does not cause
 silent scope drift.

## Preconditions
- Must follow:
  - `docs/process/policies/migration-workflow-common-policy.md`
- If running inside `agent-skills` transition-era migration:
  - `docs/process/overlays/agent-skills-transition-overlay.md`
- Migration topic, risk level, approved plan, and target branch are already
  provided.
- A PR for the topic is already open.

## Inputs
- migration topic
- risk level
- approved topic plan
- target branch
- PR comments and related review context

## Outputs
- planner triage decision for each actionable PR comment
- no-correction routing result recorded when correction is not required
- bounded correction applied when required
- reviewer re-check completed when required
- planner final review completed
- correction committed by topic
- branch pushed

## States
- `PR_COMMENTS_FOUND`
- `PLANNER_TRIAGE`
- `PLANNER_TRIAGE_COMPLETED`
- `NO_CORRECTION_REQUIRED`
- `CORRECTION_REQUIRED`
- `CORRECTION_IMPLEMENTED`
- `REVIEW_PASSED`
- `PLANNER_FINAL_ACCEPTED`
- `COMMITTED`
- `PUSHED`
- `WAIT_HUMAN_MERGE`
- `HUMAN_FEEDBACK_REQUIRED`

## Step Sequence
1. Check PR comments.
2. Planner triages each actionable comment.
3. Mark planner triage as completed.
4. Route each comment as required correction, non-blocking note, out-of-scope,
   or human-decision-required.
5. If all actionable comments are non-blocking or out-of-scope, record
   no-correction routing and wait for human merge.
6. Apply bounded correction when required.
7. Review the correction.
8. Complete planner final review.
9. Commit correction by topic.
10. Push.
11. Wait for human merge.

## PR Comment Classification
- `REQUIRED_CORRECTION`
- `NON_BLOCKING_NOTE`
- `OUT_OF_SCOPE`
- `HUMAN_DECISION_REQUIRED`

## Stop Rules
Stop with `human-feedback-required` if:

- approved plan is missing
- PR comment requires scope expansion
- PR comment conflicts with the approved plan and cannot be resolved safely
- the correction loop reaches terminal escalation
- planner final review cannot confirm the correction is bounded

## Role Responsibility Boundaries
- Planner triages PR comments before correction work begins.
- Implementer or creator applies only the bounded correction chosen by planner
  routing.
- Reviewer re-checks the corrected output, and both reviewer re-check and
  bounded correction execution must remain independent roles relative to Main
  Agent.
- Main Agent manages commit, push, and wait-for-human-merge handoff.

## Required `status.json` Fields
- `workflow`: `pr-comment-correction`
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
- Every actionable PR comment was triaged before correction.
- PR comments could conclude in no-correction routing when all actionable
  comments were non-blocking or out-of-scope.
- Required corrections stayed bounded to the approved topic.
- Reviewer re-check passed when correction was applied.
- Planner final review confirmed no scope drift.
- Correction commit stayed by topic and branch was pushed.

## What Not To Do
- Do not treat PR comments as direct implementation instructions.
- Do not skip planner triage.
- Do not expand the approved topic through comment handling.
- Do not auto-merge after push.
