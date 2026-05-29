---
topic: codex-skill-direct-move-impl-ab
status: planned
created: 2026-05-29
---

# Codex Skill Direct Move Implementation AB Steps

## Workflow Stages

- [X] plan
- [ ] branch-ready
- [ ] implementation
- [ ] review
- [ ] overlay
- [ ] migration-status
- [ ] publish-handoff

## Actionable Steps

### plan
- [X] Freeze implementation topic name `codex-skill-direct-move-impl-ab`
- [X] Freeze planned target branch `feat/andrew/codex-skill-direct-move-impl-ab`
- [X] Freeze planned worktree path `/Users/andrew/code/python/agent-skills.worktrees/agent-20260529-codex-skill-direct-move-impl-ab`
- [X] Materialize `analysis/codex-skill-direct-move-impl-ab/requirements.md`
- [X] Materialize `analysis/codex-skill-direct-move-impl-ab/technical-spec.md`
- [X] Materialize `plan/codex-skill-direct-move-impl-ab/codex-skill-direct-move-impl-ab.plan.md`
- [X] Materialize `plan/codex-skill-direct-move-impl-ab/codex-skill-direct-move-impl-ab.summary.md`

### branch-ready
- [ ] Prepare or reuse the target branch `feat/andrew/codex-skill-direct-move-impl-ab`
- [ ] Prepare or reuse the target worktree `/Users/andrew/code/python/agent-skills.worktrees/agent-20260529-codex-skill-direct-move-impl-ab`
- [ ] Record worktree routing result under `.workflow-runs/<run-id>/status.json`

### implementation
- [ ] Re-load the committed `codex-skill-direct-move-ab` baseline artifacts
- [ ] Implement `python-package-layout` under `skills/`
- [ ] Implement `python-library-architecture` under `skills/`
- [ ] Implement the 5 B-class rewritten semantic skills under `skills/`
- [ ] Keep `.github/skills/` read-only throughout the topic

### review
- [ ] Request independent review against `plan/codex-skill-direct-move-impl-ab/codex-skill-direct-move-impl-ab.plan.md`
- [ ] Record whether the implementation stayed within the frozen write set

### overlay
- [ ] Determine whether the approved topic scope binds `docs/process/overlays/agent-skills-transition-overlay.md`
- [ ] If bound, record a clear `passed`, `blocked`, or `deferred` result
- [ ] If overlay binding or gate outcome remains unresolved from repo-visible inputs, stop with `human-feedback-required`

### migration-status
- [ ] Record one migration status result: `moved`, `copied`, `remediated`, `deferred`, `blocked`, or `skipped`
- [ ] Stop at `MIGRATION_STATUS_CONFIRMED`

### publish-handoff
- [ ] Do not commit, push, or open a PR in the implementation workflow
- [ ] Hand later publish actions to `migration-publish-handoff.workflow.md`

## Handoff / Gate Notes

- This `step.md` is required before any later `migration-implementation`
  workflow progression.
- The implementation topic may not start until branch/worktree preparation is
  explicit.
- The reviewed overlay file is part of the planning artifact set; later
  execution must still determine whether it is bound from the approved topic
  scope and repo-visible inputs.
- If any future implementation step requires `.github/skills/` edits, stop and
  re-plan rather than widening this topic silently.
