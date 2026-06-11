---
topic: skills-canonical-inventory
status: planned
created: 2026-06-11
current_plan_input: plan/skills-canonical-inventory/skills-canonical-inventory.plan.md
---

# Skills Canonical Inventory Steps

## Workflow Stages

- [X] create worktree
- [X] `.github/prompts/create-analysis.prompt.md`
- [X] `.github/prompts/create-agent-plan.prompt.md`
- [X] draft plan commit by topic
- [ ] `(subAgent) .codex/skills/plan-reviewer review the plan and requirement doc and then feedback`
- [ ] `(subAgent) skills/plan-creator fix and update and feedback`
- [ ] `(subAgent) planner final gate`
- [ ] wait human check

## Actionable Steps

### create worktree

- [X] Use managed worktree
  `/Users/andrew/code/python/agent-skills.worktrees/agent-20260611-skills-canonical-inventory`
- [X] Use branch `feat/andrew/skills-canonical-inventory`

### `.github/prompts/create-analysis.prompt.md`

- [X] Freeze `analysis/skills-canonical-inventory/requirements.md`
- [X] Freeze `analysis/skills-canonical-inventory/technical-spec.md`
- [X] Lock the topic to canonical `skills/` inventory only
- [X] Lock later implementation targets to:
  - `scripts/build_skills_inventory.py`
  - `artifacts/skills-inventory.jsonl`

### `.github/prompts/create-agent-plan.prompt.md`

- [X] Materialize `plan/skills-canonical-inventory/skills-canonical-inventory.plan.md`
- [X] Materialize `plan/skills-canonical-inventory/skills-canonical-inventory.step.md`
- [X] Materialize `plan/skills-canonical-inventory/skills-canonical-inventory.checklist.md`
- [X] Record strict-mode analysis prerequisites and SHA-256 values in the topic
  plan
- [X] Record exact implementation artifact paths and non-release intent in the
  topic plan

### draft plan commit by topic

- [X] Draft one planning-only commit for:
  - `analysis/skills-canonical-inventory/requirements.md`
  - `analysis/skills-canonical-inventory/technical-spec.md`
  - `plan/skills-canonical-inventory/skills-canonical-inventory.plan.md`
  - `plan/skills-canonical-inventory/skills-canonical-inventory.step.md`
  - `plan/skills-canonical-inventory/skills-canonical-inventory.checklist.md`
- [X] Do not enter implementation before the planning-artifact commit exists

### `(subAgent) .codex/skills/plan-reviewer review the plan and requirement doc and then feedback`

- [ ] Run independent plan review against:
  - `plan/skills-canonical-inventory/skills-canonical-inventory.plan.md`
  - `plan/skills-canonical-inventory/skills-canonical-inventory.step.md`
  - `plan/skills-canonical-inventory/skills-canonical-inventory.checklist.md`
  - `analysis/skills-canonical-inventory/requirements.md`
  - `analysis/skills-canonical-inventory/technical-spec.md`
- [ ] Return reviewer feedback without widening scope beyond canonical
  `skills/` inventory
- [ ] If reviewer feedback begins to control routing or creates a multi-round
  rework loop, stop and amend the topic plan to add an exact
  `review-log.md` path before continuing

### `(subAgent) skills/plan-creator fix and update and feedback`

- [ ] Apply plan-only corrections inside the topic planning artifacts if review
  returns `needs-rework`
- [ ] Keep fixes bounded to plan contract repair; do not begin implementation
- [ ] Re-run independent plan review after each bounded planning fix until the
  verdict returns `approved`

### `(subAgent) planner final gate`

- [ ] Run final gate only after approved review state is reflected in repo-
  visible truth
- [ ] Confirm the accepted plan still maps 100% to
  `analysis/skills-canonical-inventory/technical-spec.md`
- [ ] Confirm the implementation write set remains exactly:
  - `scripts/build_skills_inventory.py`
  - `artifacts/skills-inventory.jsonl`

### wait human check

- [ ] Stop and wait for explicit human check after planner final gate passes
- [ ] Do not enter implementation before human check authorizes it

## Handoff / Gate Notes

- Current progression truth ends at the completed `draft plan commit by topic`
  stage.
- The next required action is `(subAgent) .codex/skills/plan-reviewer review
  the plan and requirement doc and then feedback`.
- The analysis artifacts remain frozen prerequisites and must not be reopened
  during planning review unless a separate scope change is approved.
- `plan/skills-canonical-inventory/skills-canonical-inventory.review-log.md`
  is intentionally absent because reviewer-routing state is not yet active.
- This `*.step.md` is the progression artifact for the human-locked planning
  workflow above and must be updated from repo-visible facts only.
