---
topic: phase-2-merge-into-skills-batch
status: review-ready
created: 2026-06-10
---

# Phase 2 Merge Into Skills Batch Steps

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
- [X] Use managed worktree `/Users/andrew/code/python/agent-skills.worktrees/agent-20260610-phase-2-merge-into-skills-batch`
- [X] Keep all work inside the declared merge-batch write set

### analysis
- [X] Read repo governance, workflow, and topic-plan contract artifacts
- [X] Read umbrella baseline artifacts and confirm this topic is a child slice under the approved coordination baseline
- [X] Read Phase 1 merge-batch candidate, semantic-drift, and runtime-dependency evidence
- [X] Freeze the exact ten-candidate merge-batch set
- [X] Freeze the initial planning baseline before bounded canonical convergence begins

### plan
- [X] Create `analysis/phase-2-merge-into-skills-batch/requirements.md`
- [X] Create `analysis/phase-2-merge-into-skills-batch/technical-spec.md`
- [X] Create `plan/phase-2-merge-into-skills-batch/phase-2-merge-into-skills-batch.plan.md`
- [X] Create `plan/phase-2-merge-into-skills-batch/phase-2-merge-into-skills-batch.step.md`
- [X] Record that semantic / alias / behavior drift must not be silently collapsed
- [X] Record that exact later merge policy and exact later write scope are `human_review_required` where evidence is insufficient

### draft-plan-commit-by-topic
- [X] Commit the merge-batch planning artifacts by topic before formal review routing
- [X] Record the draft planning commit in this step artifact once it exists: `87509b1`

### review
- [X] Route the current bounded execution truth for independent review
- [X] Confirm the topic remains bounded to canonical `skills/` edits and does not widen into projection work, runtime adaptation, or shared-contract edits

### final-gate
- [ ] Confirm the committed execution truth stays within canonical `skills/` only and the declared write set
- [ ] Confirm compatibility-surface differences do not block progress when canonical `skills/` content is already correct

### human-check
- [ ] Obtain explicit human approval before using this plan as the execution parent for later creator merge work

## Handoff / Gate Notes

- The planning baseline for this topic was completed and used as the execution
  parent for the current bounded canonical convergence slice.
- The exact candidate set is frozen to:
  - `agent-skill-creator`
  - `agent-skill-template`
  - `python-blueprint-authoring`
  - `python-library-architecture`
  - `python-package-layout`
  - `python-plan-authoring`
  - `python-pre-commit`
  - `python-pyproject-toolconfig`
  - `python-tdd-test-authoring`
  - `python-blueprint-review`
- `skills/` remains the canonical convergence target.
- `.github/skills/` and `.codex/skills/` remain non-authority surfaces.
- `.codex/skills/` remains a partial projection surface only.
- Semantic drift / merge policy discussion is expected in later execution and
  must not be silently collapsed away.
- Projection materialization, runtime adaptation, and copilot-only work remain
  out of scope.
- `docs/status.md` remains optional only.
- Draft planning artifacts were committed by topic as `87509b1`.
- Canonical edits were completed only for:
  - `agent-skill-template` at commit `0528a54`
  - `agent-skill-creator` at commit `0f841da`
- The following candidates were checked and required no canonical edit:
  - `python-pyproject-toolconfig`
  - `python-blueprint-authoring`
  - `python-library-architecture`
  - `python-package-layout`
  - `python-plan-authoring`
  - `python-pre-commit`
  - `python-tdd-test-authoring`
  - `python-blueprint-review`
- No `.github/**` or `.codex/**` files were modified in this bounded execution
  slice.
- Remaining compatibility-surface differences do not block progress when
  canonical `skills/` content is already correct.
- Focused re-review has passed; no critical or major findings remain.
- Next formal workflow step is `final-gate`.
- `final-gate` and `human-check` remain pending on the updated execution
  truth.
- No additional execution beyond this bounded canonical convergence slice is
  authorized before final-gate review completes.
- If exact later merge policy cannot be derived honestly from evidence, route
  that item to `human_review_required`.
- If exact later write scope cannot be derived honestly from evidence, route
  that item to `human_review_required`.
- If later review requires `review-log.md` or `summary.md` for this topic, do
  not create them under current scope; route to `human_review_required`.
