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
- [X] review
- [X] final-gate
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
- [X] Reviewer subAgent `Lovelace` ran round-1 independent plan review
- [X] Reviewer round 1 returned `needs-rework`
- [X] Reviewer findings were materialized at `plan/skills-canonical-positioning/skills-canonical-positioning.review-log.md`
- [X] Reviewer subAgent `Kepler` ran round-2 re-review
- [X] Reviewer round 2 returned `approved`

### final-gate
- [X] Final gate subAgent `James` ran independent final gate
- [X] Final gate verdict: `approved`
- [X] Final gate result: `GO for human check`
- [X] Remaining risks were recorded from the final gate output

### human-check
- [ ] Human review remains pending

## Handoff / Gate Notes

- This topic has completed review and final gate, and is now waiting for human check.
- The only editable repo files authorized by the topic plan are:
  - `AGENTS.md`
  - `docs/repo-positioning.md`
  - `.github/copilot-instructions.md`
  - `README.md`
- Forbidden scope includes `.github/skills/**`, `.codex/skills/**`, `skills/**`,
  `.github/guides/MAIN-AGENT-WORKFLOW.md`, any `agent-skill-*`, and all
  runtime/tooling/install/sync/projection automation surfaces.
- Final gate remaining risks:
  - the latest plan / step / review-log updates are not yet reflected in a new topic commit
  - contradictory wording under `.github/skills/**`, `.codex/skills/**`, and `skills/**` remains intentionally unresolved for this topic
- No implementation work should begin until human check completes.
