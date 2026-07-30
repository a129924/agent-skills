# Agent Skills Published Asset Hygiene Baseline — Correction Plan

## Classification

- **Severity:** `medium`
- **Routing state:** `PLANNER_REPLAN`
- **Trigger:** Actual root `pre-commit run --all-files` added four
  published-skill hygiene changes and eight new non-skill rewrites beyond the
  earlier two-group baseline. The full observed non-skill inventory is now 24
  paths.
- **Parent truth:** `agent-skills-published-asset-hygiene-baseline.plan.md` and
  its `.step.md` remain the execution-facing current truth. This file and the
  correction step are retained historical truth.

## Frozen Correction Direction

1. Retain the original 42 published-skill asset normalizations and root
   `.pre-commit-config.yaml` without semantic edits.
2. Add final-LF-only hygiene normalization for:
   - `skills/python-pre-commit/templates/pre-commit-config.yaml`
   - `.github/skills/python-pre-commit/templates/pre-commit-config.yaml`
   - `.codex/skills/python-pre-commit/templates/pre-commit-config.yaml`
3. Retain hygiene-only normalization for
   `.github/skills/python-serialization-boundaries/REVIEW.md`; preserve its
   existing GitHub-specific Date semantic divergence and do not modify or
   invent canonical/Codex counterparts.
4. Restore the eight new non-skill hook rewrites listed in the parent plan;
   they are out of scope. Do not repair any of the 24 inventory files.
5. Keep the root hook configuration unrestricted: version `v4.6.0`, the two
   named hooks, and no `exclude`.

## Boundaries

- The Implementer may not change skill semantics, paths, Markdown structure,
  cross-references, functional behavior, release flow, CI, fixtures, README,
  VERSION, tag, or release metadata.
- The Implementer may not edit the parent plan, this correction plan, topic
  step, or review log; it may update only the correction step as factual
  progression evidence.
- Any all-files inventory path outside the frozen 24, any published-skill
  rewrite outside the exact parent write set, or any new semantic divergence
  returns to Planner rather than expanding the correction.

## Required Handoff and Closure

- A separate Implementer completes the frozen correction and reports command
  results, retained/restored paths, and consumer-like evidence.
- A separate Reviewer returns the exact JSON verdict and records its result in
  the review log.
- Parent/correction path alignment and all validation checks must pass before
  this correction may be marked `resolved` by Planner. The artifact is then
  retained; it must not be deleted.
