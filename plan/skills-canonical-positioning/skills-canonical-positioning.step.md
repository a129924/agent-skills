---
topic: skills-canonical-positioning
status: planned
created: 2026-06-02
---

# Skills Canonical Positioning Steps

## Workflow Stages

- [X] worktree
- [X] analysis
- [X] plan
- [ ] review
- [ ] final-gate
- [ ] human-check

## Actionable Steps

### worktree
- [X] Create managed worktree at `/Users/andrew/code/python/agent-skills.worktrees/agent-20260602-skills-canonical-positioning`
- [X] Create branch `feat/andrew/skills-canonical-positioning`

### analysis
- [X] Freeze `analysis/skills-canonical-positioning/requirements.md`
- [X] Freeze `analysis/skills-canonical-positioning/technical-spec.md`
- [X] Lock the business baseline to four editable files only
- [X] Lock `.github/skills/**`, `.codex/skills/**`, and `skills/**` as forbidden scope

### plan
- [X] Materialize `plan/skills-canonical-positioning/skills-canonical-positioning.plan.md`
- [X] Materialize `plan/skills-canonical-positioning/skills-canonical-positioning.step.md`
- [X] Record strict-mode analysis prerequisites and SHA-256 values in the topic plan
- [X] Encode editable scope and forbidden scope in the topic plan

### review
- [ ] Reviewer has not run yet
- [ ] No reviewer verdict artifact exists yet

### final-gate
- [ ] Final gate has not run yet
- [ ] No gate verdict exists yet

### human-check
- [ ] Human review remains pending

## Handoff / Gate Notes

- This topic is currently at the end of plan creation and has **not** entered
  review or final gate.
- The only editable repo files authorized by the topic plan are:
  - `AGENTS.md`
  - `docs/repo-positioning.md`
  - `.github/copilot-instructions.md`
  - `README.md`
- Forbidden scope includes `.github/skills/**`, `.codex/skills/**`, `skills/**`,
  `.github/guides/MAIN-AGENT-WORKFLOW.md`, any `agent-skill-*`, and all
  runtime/tooling/install/sync/projection automation surfaces.
- No implementation work should begin until review and final gate complete.
