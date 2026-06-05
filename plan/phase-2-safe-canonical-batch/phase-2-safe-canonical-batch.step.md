---
topic: phase-2-safe-canonical-batch
status: planned
created: 2026-06-05
---

# Phase 2 Safe Canonical Batch Steps

## Workflow Stages

- [X] worktree
- [X] analysis
- [X] plan
- [X] draft-plan-commit-by-topic
- [X] review
- [ ] final-gate
- [ ] human-check

## Actionable Steps

### worktree
- [X] Use managed worktree `/Users/andrew/code/python/agent-skills.worktrees/agent-20260605-phase-2-safe-canonical-batch`
- [X] Keep all work inside the declared safe-batch write set

### analysis
- [X] Read repo governance, workflow, and topic-plan contract artifacts
- [X] Read umbrella baseline artifacts and confirm this topic is the first slice after umbrella
- [X] Read Phase 1 summary, convergence candidates, and Phase 2 inputs
- [X] Freeze the exact nine-skill safe canonical batch list
- [X] Freeze current turn as planning only

### plan
- [X] Create `analysis/phase-2-safe-canonical-batch/requirements.md`
- [X] Create `analysis/phase-2-safe-canonical-batch/technical-spec.md`
- [X] Create `plan/phase-2-safe-canonical-batch/phase-2-safe-canonical-batch.plan.md`
- [X] Create `plan/phase-2-safe-canonical-batch/phase-2-safe-canonical-batch.step.md`
- [X] Record that later implementation stays bounded to the frozen safe list only
- [X] Record that guessed later implementation write scope is `human_review_required`

### draft-plan-commit-by-topic
- [X] Commit the safe-batch planning artifacts by topic before formal review routing
- [X] Record the draft planning commit in this step artifact once it exists: `4a5160d`

### review
- [X] Route the first-slice planning baseline for independent review
- [X] Confirm the plan does not widen into implementation, later slices, or shared-contract edits

### final-gate
- [ ] Confirm the planning baseline stays within the declared write set
- [ ] Confirm the topic still records planning-only status for the current workflow stage

### human-check
- [ ] Obtain explicit human approval before using this plan as the execution parent for later creator work

## Handoff / Gate Notes

- This topic branches from approved umbrella baseline
  `feat/andrew/phase-2-umbrella` at `9d1d784`.
- This topic is the first execution slice after umbrella.
- The current turn is planning only and does not implement canonical
  convergence.
- The safe canonical batch list is frozen exactly to:
  - `agent-skill-reviewer`
  - `business-intent-alignment`
  - `business-to-technical-translation`
  - `git-branch-naming`
  - `git-commit-convention`
  - `git-post-merge-workflow`
  - `python-project-init-greenfield`
  - `python-project-retrofit`
  - `worktree-manager`
- `skills/` remains the canonical convergence target.
- `.github/skills/` and `.codex/skills/` remain non-authority surfaces.
- `.codex/skills/` remains a partial projection surface only.
- Later slices remain out of scope:
  - `phase-2-merge-into-skills-batch`
  - `phase-2-planning-spine-exceptions`
- Projection materialization, runtime adaptation, and copilot-only work remain
  out of scope.
- `docs/status.md` remains optional only.
- Draft planning artifacts were committed by topic as `4a5160d`.
- Formal review has passed on the committed safe-batch baseline.
- Next formal workflow step is `final-gate`.
- `final-gate` and `human-check` remain pending in the formal workflow order.
- No implementation work is authorized under this topic at the current
  planning stage.
- If later implementation write scope would require guessing beyond current
  Phase 1 + umbrella evidence, route that item to `human_review_required`.
- If planning-stage review later requires `review-log.md` or `summary.md` for
  this topic, do not create them under current scope; route to
  `human_review_required`.
