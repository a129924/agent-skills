---
topic: phase-2-umbrella
status: planned
created: 2026-06-05
---

# Phase 2 Umbrella Steps

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
- [X] Use managed worktree `/Users/andrew/code/python/agent-skills.worktrees/agent-20260605-phase-2-umbrella`
- [X] Keep all work inside the declared umbrella write set

### analysis
- [X] Read repo governance, workflow, and topic-plan contract artifacts
- [X] Read Phase 1 summary, convergence candidates, and Phase 2 inputs
- [X] Freeze umbrella topic as governance / coordination only
- [X] Freeze later execution slice names, order, and safe canonical batch membership

### plan
- [X] Create `analysis/phase-2-umbrella/requirements.md`
- [X] Create `analysis/phase-2-umbrella/technical-spec.md`
- [X] Create `plan/phase-2-umbrella/phase-2-umbrella.plan.md`
- [X] Create `plan/phase-2-umbrella/phase-2-umbrella.step.md`
- [X] Record that each later slice requires its own plan / review / human-check / PR
- [X] Record that slice PR order is strictly serialized

### draft-plan-commit-by-topic
- [X] Commit the umbrella planning artifacts by topic before formal review routing
- [X] Record the draft planning commit in this step artifact once it exists: `46688da`

### review
- [ ] Route the umbrella planning baseline for independent review after draft-plan-commit-by-topic completes
- [ ] Confirm the plan does not widen into implementation or shared-contract edits as part of the formal review stage

### final-gate
- [ ] Confirm the umbrella baseline stays within the declared write set
- [ ] Confirm later slices remain separate topics rather than inherited execution approval

### human-check
- [ ] Obtain explicit human approval before treating umbrella baseline as the planning parent for later slices

## Handoff / Gate Notes

- `phase-2-umbrella` is a coordination layer only and must not be treated as a
  fourth implementation line.
- `skills/` remains the canonical convergence target.
- `.github/skills/` and `.codex/skills/` remain non-authority surfaces.
- `.codex/skills/` remains a partial projection surface only.
- Later execution slices are frozen to:
  - `phase-2-safe-canonical-batch`
  - `phase-2-merge-into-skills-batch`
  - `phase-2-planning-spine-exceptions`
- `phase-2-safe-canonical-batch` is the first later execution slice.
- The safe canonical batch skill list is frozen to:
  - `agent-skill-reviewer`
  - `business-intent-alignment`
  - `business-to-technical-translation`
  - `git-branch-naming`
  - `git-commit-convention`
  - `git-post-merge-workflow`
  - `python-project-init-greenfield`
  - `python-project-retrofit`
  - `worktree-manager`
- Later slice PR order is strictly serialized.
- `plan/<topic>/<topic>.step.md` remains topic progression truth.
- `plan/<topic>/<topic>.summary.md` remains topic close outcome / handoff truth.
- `docs/status.md` is optional cross-topic overview only.
- Draft planning artifacts were committed by topic as `46688da`.
- Any earlier reviewer or final-gate result for this umbrella baseline is
  preflight evidence only and does not replace formal workflow stage
  completion.
- Next formal workflow step is `review`.
- `review`, `final-gate`, and `human-check` remain pending until they run in
  the formal workflow order after draft plan commit by topic.
- No direct implementation work is authorized or next under this topic.
- If any later umbrella work would require files outside the declared write set
  or any shared-contract-file edit, stop and route to `human_review_required`.
