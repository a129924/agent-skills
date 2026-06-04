# Plan Contract Authority Alignment Review Log

## Round 1

- **Reviewer**: `Parfit`
- **Date**: 2026-06-04
- **Verdict**: `NEEDS_REWORK`
- **Scope**: planning artifacts only

## Blocking Findings

1. `Artifact Paths` used broad directory references
   (`skills/plan-creator/**` and `skills/plan-reviewer/**`) instead of exact
   repo-visible paths, which breaks the executable artifact-path contract and
   makes read-only evidence look like writable scope.

## Required Fixes

- Replace wildcard planning-skill evidence rows with exact repo-visible paths,
  or remove them from `Artifact Paths` if they are not part of the executable
  contract.
- Keep the governance-only boundary and read-only intent explicit after the
  artifact-path repair.
- Align `plan-contract-authority-alignment.step.md` so the
  `draft-plan-commit-by-topic` stage matches the recorded commit completion.

## Notes

- Required sections, strict-mode analysis routing, and non-stable intent were
  accepted.
- Reviewer did not request any widening into convergence, projection, runtime,
  or skill-local implementation work.
