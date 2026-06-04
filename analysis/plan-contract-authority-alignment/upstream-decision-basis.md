# Upstream Decision Basis: plan-contract-authority-alignment

## Status

- **Status**: frozen read-only evidence snapshot
- **Topic**: `plan-contract-authority-alignment`
- **Date**: 2026-06-04

## Upstream Evidence Location

The accepted Phase 1 decision basis currently lives in the dedicated worktree:

- `/Users/andrew/code/python/agent-skills.worktrees/agent-20260603-agent-skills-convergence-phase-1`

This topic treats that worktree as accepted upstream evidence, not as an
editable surface.

## Exact Upstream Evidence Paths

### Accepted Phase 1 report bundle

- `/Users/andrew/code/python/agent-skills.worktrees/agent-20260603-agent-skills-convergence-phase-1/docs/agent-skills-convergence/phase-1/00-summary.md`
- `/Users/andrew/code/python/agent-skills.worktrees/agent-20260603-agent-skills-convergence-phase-1/docs/agent-skills-convergence/phase-1/01-skill-inventory.md`
- `/Users/andrew/code/python/agent-skills.worktrees/agent-20260603-agent-skills-convergence-phase-1/docs/agent-skills-convergence/phase-1/02-path-comparison.md`
- `/Users/andrew/code/python/agent-skills.worktrees/agent-20260603-agent-skills-convergence-phase-1/docs/agent-skills-convergence/phase-1/03-copilot-only-classification.md`
- `/Users/andrew/code/python/agent-skills.worktrees/agent-20260603-agent-skills-convergence-phase-1/docs/agent-skills-convergence/phase-1/04-semantic-drift-report.md`
- `/Users/andrew/code/python/agent-skills.worktrees/agent-20260603-agent-skills-convergence-phase-1/docs/agent-skills-convergence/phase-1/05-runtime-dependency-inventory.md`
- `/Users/andrew/code/python/agent-skills.worktrees/agent-20260603-agent-skills-convergence-phase-1/docs/agent-skills-convergence/phase-1/06-convergence-candidates.md`
- `/Users/andrew/code/python/agent-skills.worktrees/agent-20260603-agent-skills-convergence-phase-1/docs/agent-skills-convergence/phase-1/07-phase-2-inputs.md`
- `/Users/andrew/code/python/agent-skills.worktrees/agent-20260603-agent-skills-convergence-phase-1/docs/agent-skills-convergence/phase-1/08-phase-3-inputs.md`

### Accepted human review verdict

- `/Users/andrew/code/python/agent-skills.worktrees/agent-20260603-agent-skills-convergence-phase-1/docs/agent-skills-convergence/phase-1/09-human-review-verdict.md`

### Upstream workflow truth artifacts

- `/Users/andrew/code/python/agent-skills.worktrees/agent-20260603-agent-skills-convergence-phase-1/plan/agent-skills-convergence-phase-1/agent-skills-convergence-phase-1.review-log.md`
- `/Users/andrew/code/python/agent-skills.worktrees/agent-20260603-agent-skills-convergence-phase-1/plan/agent-skills-convergence-phase-1/agent-skills-convergence-phase-1.step.md`
- `/Users/andrew/code/python/agent-skills.worktrees/agent-20260603-agent-skills-convergence-phase-1/plan/agent-skills-convergence-phase-1/agent-skills-convergence-phase-1.summary.md`

## Accepted Decisions Carried Forward

The following decisions are accepted as upstream planning inputs for this topic:

1. `skills/` is the later canonical convergence target.
2. `.github/skills/` and `.codex/skills/` are not authority source trees.
3. `.codex/skills/` is a partial projection surface only.
4. `plan-creator` and `plan-reviewer` authority must move to one shared
   repo-level plan contract.
5. `python-blueprint-review` should later be absorbed into `skills/`, but not
   in this topic.
6. `copilot-instructions-init` remains `copilot_only` and `platform_native`.
7. Phase 1 planning inputs are decision inputs only and are not an approved
   implementation spec.

## Downstream Implications

- This topic may prepare governance baselines for later convergence work.
- This topic may not implement canonical convergence.
- This topic may not materialize projection surfaces.
- This topic may not implement runtime adaptation.
- This topic may not directly absorb `python-blueprint-review` into `skills/`.
- This topic may not perform generic convergence for
  `copilot-instructions-init`.

## Evidence Handling Rule

If any later work in this topic would require changing the accepted meaning of
the upstream Phase 1 bundle or its human review verdict, stop and create a new
decision topic instead of silently reinterpreting the upstream evidence.
