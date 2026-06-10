---
topic: phase-2-planning-spine-exceptions
status: review-ready
created: 2026-06-10
---

# Phase 2 Planning Spine Exceptions Steps

## Workflow Stages

- [X] worktree
- [X] analysis
- [X] plan
- [X] draft-plan-commit-by-topic
- [ ] review
- [ ] final-gate
- [ ] human-check

## Actionable Steps

### worktree
- [X] Use managed worktree `/Users/andrew/code/python/agent-skills.worktrees/agent-20260610-phase-2-planning-spine-exceptions`
- [X] Keep all work inside the declared planning write set

### analysis
- [X] Read repo governance, workflow, and topic-plan contract artifacts
- [X] Read umbrella baseline, safe-batch truth, merge-batch truth, and Phase 1 planning-spine evidence
- [X] Freeze the exact bounded skill set to `skills/plan-creator/**` and `skills/plan-reviewer/**`
- [X] Freeze unresolved authority and behavior items as `human_review_required`

### plan
- [X] Create `analysis/phase-2-planning-spine-exceptions/requirements.md`
- [X] Create `analysis/phase-2-planning-spine-exceptions/technical-spec.md`
- [X] Create `plan/phase-2-planning-spine-exceptions/phase-2-planning-spine-exceptions.plan.md`
- [X] Create `plan/phase-2-planning-spine-exceptions/phase-2-planning-spine-exceptions.step.md`
- [X] Record that later execution stays bounded to `skills/plan-creator/**` and `skills/plan-reviewer/**`
- [X] Record that workflow, authority, handoff, or blocked-behavior uncertainty remains `human_review_required`

### draft-plan-commit-by-topic
- [X] Commit the planning-spine exception artifacts by topic before formal review routing
- [X] Record the draft planning commit in this step artifact once it exists: `TO_BE_FILLED_AFTER_COMMIT`

### review
- [ ] Route the topic plan and requirement baseline for formal review
- [ ] Confirm no planning artifact widens into `.github/**`, `.codex/**`, unrelated skills, or shared-contract rewrites

### final-gate
- [ ] Confirm the committed planning baseline stays within the declared write set
- [ ] Confirm the topic preserves unresolved high-risk items as `human_review_required`

### human-check
- [ ] Obtain explicit human approval before using this plan as the execution parent for later canonical convergence

## Handoff / Gate Notes

- This topic is the final Phase 2 execution slice after the safe canonical batch
  and merge-into-skills batch.
- `skills/` remains the canonical convergence target.
- `.github/**` and `.codex/**` remain read-only compatibility surfaces.
- `.codex/skills/` remains a partial projection surface only.
- The bounded skill set is frozen exactly to:
  - `skills/plan-creator/**`
  - `skills/plan-reviewer/**`
- Later execution under this topic is not yet authorized.
- High-risk authority, workflow, handoff, fallback, and blocked-behavior
  questions remain `human_review_required` until later evidence proves a change
  is wording-only.
- No projection materialization, runtime adaptation, copilot-only convergence,
  or unrelated skill convergence is in scope.
- No `review-log.md` or `summary.md` is created under current scope.
- Next workflow step is formal review of the committed planning baseline.
