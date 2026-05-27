---
topic: workflow-artifact-standardization
status: review-ready
created: 2026-05-27
---

# Workflow Artifact Standardization Steps

## Workflow Stages

- [X] plan
- [X] branch-ready
- [X] creator
- [ ] review
- [ ] publish
- [ ] pr-open
- [ ] merged
- [ ] released

## Actionable Steps

### plan
- [X] Freeze topic name, worktree split, and planning-only stop point
- [X] Materialize `analysis/workflow-artifact-standardization/requirements.md`
- [X] Materialize `plan/workflow-artifact-standardization/workflow-artifact-standardization.plan.md`
- [X] Materialize `plan/workflow-artifact-standardization/workflow-artifact-standardization.step.md`

### branch-ready
- [X] Create managed worktree at `../agent-skills.worktrees/agent-20260527-workflow-artifact-standardization`
- [X] Create branch `feat/andrew/workflow-artifact-standardization`

### creator
- [X] Translate the frozen baseline into an exact shared-contract patch set after human permission
- [X] Identify which shared workflow files actually need modification within the bounded governance surface
- [X] Apply the bounded shared-governance workflow-contract updates in the authorized file set

### review
- [ ] Run independent review on the shared-contract patch set after creator work exists

### publish
- [ ] Apply any required review corrections and pass planner-alignment before publish progression

### pr-open
- [ ] Open and manage the PR after publish progression is authorized

### merged
- [ ] Complete merge and post-merge resume path if this topic later reaches merge

### released
- [ ] Record any release outcome only if a later topic revision explicitly declares release work

## Handoff / Gate Notes

- Human permission for shared workflow-contract edits was provided for this run,
  and the bounded creator-stage governance patch set is complete.
- `plan` and `branch-ready` are complete because the worktree, branch, and three planning artifacts already exist.
- `creator` is complete because the repo-level workflow contract and bounded
  workflow docs now reflect the frozen artifact-governance baseline.
- This `step.md` remains a progression artifact only; a future required
  `summary artifact` still owns close and handoff truth.
- A future `summary artifact` is required before topic close if this topic ends with topic-close handoff or `required follow-up`.
