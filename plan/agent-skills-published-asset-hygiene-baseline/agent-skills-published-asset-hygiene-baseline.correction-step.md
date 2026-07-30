# Agent Skills Published Asset Hygiene Baseline — Correction Steps

## Correction Workflow

- [X] Planner classified the all-files scope drift as `medium` and froze
  `PLANNER_REPLAN`.
- [X] Planner updated parent current truth with the 24-path non-skill inventory,
  four added published-skill hygiene changes, exact exceptions, and all
  correction artifacts.
- [X] Implementer retains the original 42 published-skill asset changes and
  root config, and retains only final-LF changes for the three newly scoped
  `python-pre-commit` template copies plus the GitHub-only serialization review
  exception.
- [X] Implementer restores exactly the eight newly observed non-skill rewrites
  specified in the parent plan, without repairing the other 16 blocker paths.
- [X] Implementer runs the parent-plan validation suite and records factual
  command results here.
- [ ] Separate Reviewer reviews the bounded correction and appends the exact
  JSON verdict to the review log.
- [ ] Planner confirms parent/correction synchronization and marks this
  historical correction `resolved`, or returns it to `PLANNER_REPLAN`.

## Handoff / Gate Notes

- Current routing: `creator-in-progress` under `PLANNER_REPLAN`.
- The all-files full-repository gate is intentionally expected to fail on the
  frozen 24 non-skill blockers. The consumer-like published-asset gate must
  pass with no worktree changes.
- Any unexpected target, semantic diff, missing projection, or validation
  result outside the frozen contract stops work and returns to Planner.

## Implementer Evidence — 2026-07-29

- Restored exactly the eight named restore-only paths to their `HEAD`
  pre-hook baseline. The original 42 published-asset changes, root config,
  three `python-pre-commit` final-LF copies, and GitHub-only serialization
  review hygiene change were retained.
- With `PRE_COMMIT_HOME=/private/tmp/agent-skills-precommit-home` and
  `/private/tmp/agent-skills-precommit-env/bin/pre-commit`,
  `pre-commit validate-config` passed and `git diff --check` reported no
  whitespace errors.
- Byte comparisons passed for each locked canonical/projection pair, except
  the documented GitHub `plan-step-tracker` CLI-path divergence and the
  GitHub-only serialization review exception.
- A fresh full-repository temporary Git clone, with only in-scope published
  assets and root config overlaid before its baseline commit, made
  `pre-commit run --all-files` fail and modify exactly the frozen 24-path
  non-skill inventory; no published-skill path was modified. That temporary
  workspace was restored clean after capture.
- A consumer-like temporary Git workspace containing all `skills/**`,
  `.github/skills/**`, `.codex/skills/**`, and root config passed
  `pre-commit run --all-files`; both `git status --short` and
  `git diff --exit-code` were clean.
- Stop condition: the feature worktree still contains 16 pre-existing
  non-skill dirty paths outside this correction's approved write set. They
  were neither repaired nor restored because the frozen correction authorizes
  restoration of only the eight named paths. Planner/Main Agent must classify
  this remaining worktree-state conflict before independent review.
