# Technical Specification: git-release-management-canonicalize

**Status**: READY FOR EXECUTION PLANNING
**Topic**: `git-release-management-canonicalize`
**Date**: 2026-06-01
**Baseline Reference**: `analysis/git-release-management-canonicalize/requirements.md`

## Source Baseline Summary

The frozen baseline requires one bounded child topic that promotes
`git-release-management` into `skills/` as a canonical copy while preserving
the existing `.github/skills/...` contract during transition.

## Requirement Traceability

| Requirement | Technical realization | Status |
| --- | --- | --- |
| R1 scope | lock edits to the single candidate | feasible |
| R2 canonical copy | create `skills/git-release-management/` | feasible |
| R3 preserve contract | keep normal-path and emergency-path semantics intact | feasible |
| R4 full surface | copy `SKILL.md`, `examples.md`, and four references | feasible |
| R5 compatibility layer | leave `.github/skills/...` unchanged | feasible |
| R6 defer repair | record deferred release-policy / active-path work | feasible |
| R7 protect governance | avoid shared surfaces | feasible |
| R8 leave evidence | emit topic-local migration report | feasible |

## Copy Boundary

Source root: `.github/skills/git-release-management/`

Target root: `skills/git-release-management/`

Required copied paths:

- `SKILL.md`
- `examples.md`
- `references/gate-contract.md`
- `references/version-sources.md`
- `references/version-bump-guidance.md`
- `references/emergency-path.md`

## Execution Model

1. verify the source inventory
2. create the target tree
3. copy the full required file set
4. verify unchanged compatibility content
5. emit a topic-local migration report

## Verification Contract

- `skills/git-release-management/SKILL.md` exists
- `skills/git-release-management/examples.md` exists
- all four reference files exist in `skills/git-release-management/references/`
- `.github/skills/git-release-management/` remains unchanged
- no release-gate semantics were changed

## Deferred Blocker Inventory

- active-path switching
- release-policy redesign
- tag/version-policy changes

## Ready-for-next-step Decision

This specification is sufficient for bounded canonical copy execution.
