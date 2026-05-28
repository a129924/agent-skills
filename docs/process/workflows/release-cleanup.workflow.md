# Release Cleanup Workflow

## Purpose
Perform post-merge cleanup and release follow-up actions only after explicit
human merge confirmation and safety checks, then finish any required topic-close
semantics without pretending merge or release alone closed the topic.

## Preconditions
- Must follow:
  - `docs/process/policies/migration-workflow-common-policy.md`
- If running inside `agent-skills` transition-era migration:
  - `docs/process/overlays/agent-skills-transition-overlay.md`
- Migration topic, risk level, approved plan, and target branch are already
  provided.
- Human merge confirmation is available before cleanup begins.

## Inputs
- migration topic
- risk level
- approved topic plan
- target branch
- merged topic branch reference
- human merge confirmation

## Outputs
- target branch synchronized
- worktree deleted when safe
- local topic branch deleted when safe
- remote topic branch deleted when safe
- version updated from post-merge target branch when required
- related docs updated when required
- tag created and pushed when required
- required topic-close `summary artifact` written or validated when the topic
  contract requires it
- final close outcome recorded as fully closed or explicit close with
  follow-up

## States
- `WAIT_HUMAN_MERGE`
- `MERGE_CONFIRMED`
- `TARGET_BRANCH_SYNCED`
- `WORKTREE_DELETED`
- `BRANCHES_DELETED`
- `VERSION_UPDATED`
- `VERSION_UPDATE_SKIPPED`
- `DOCS_UPDATED`
- `DOCS_UPDATE_SKIPPED`
- `TAG_CREATED`
- `TAG_SKIPPED`
- `TAG_PUSHED`
- `FINISHED`
- `HUMAN_FEEDBACK_REQUIRED`

## Step Sequence
1. Confirm human merge.
2. Sync the target branch.
3. Delete the worktree.
4. Delete the local topic branch.
5. Delete the remote topic branch.
6. Update project version based on the post-merge target branch when required.
7. Update related docs when required.
8. Create the tag when required.
9. Push the tag when required.
10. Create or validate the required topic-close `summary artifact` when the
    topic closes with a handoff or has `required follow-up`.
11. Finish.

## Destructive Operation Guard
- No cleanup unless human merge confirmation is present.
- Target branch must be synced.
- Worktree must have no uncommitted changes.
- Topic branch must be verified as merged or explicitly safe to delete.
- Remote branch deletion target must be unambiguous.
- Tag name must not already exist.
- Version base must be the post-merge target branch.
- Otherwise stop with `human-feedback-required`.

## Stop Rules
Stop with `human-feedback-required` if:

- human merge confirmation is missing
- target branch cannot be synced
- worktree contains uncommitted changes
- topic branch is not verified as merged or explicitly safe to delete
- remote branch deletion target is ambiguous
- version base is not the post-merge target branch
- tag name already exists
- required topic-close `summary artifact` is missing
- `required follow-up` exists but the close state is not explicitly recorded as
  close with follow-up

## Role Responsibility Boundaries
- Main Agent performs cleanup and release follow-up only after human merge
  confirmation.
- Human operator remains the authority for merge confirmation and destructive
  safety overrides.
- This workflow must not infer merge completion from local branch state alone.
- Topic close truth comes from the required `summary artifact` when one is
  required; cleanup completion alone is not enough.

## Required `status.json` Fields
- `workflow`: `release-cleanup`
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
- Cleanup did not start before human merge confirmation.
- Target branch was synced before cleanup actions.
- Worktree had no uncommitted changes before deletion.
- Topic branch deletion was verified as safe.
- Remote branch deletion target was unambiguous.
- Version base came from the post-merge target branch.
- Tag name did not pre-exist before creation.
- Optional version, docs, and tag actions were either completed when required
  or explicitly recorded as skipped.
- If topic-close handoff or `required follow-up` applied, the required
  `summary artifact` existed before the topic was treated as closed.
- Topics with `required follow-up` closed only through an explicit close with
  follow-up record.

## What Not To Do
- Do not run cleanup before explicit human merge confirmation.
- Do not infer safety for destructive operations.
- Do not use the topic branch as the version base.
- Do not continue after a destructive operation guard fails.
- Do not treat merge, cleanup, or release completion alone as topic close when
  a required `summary artifact` is still missing.
