# Technical Specification: git-post-merge-workflow-canonicalize

**Status**: READY FOR EXECUTION PLANNING
**Topic**: `git-post-merge-workflow-canonicalize`
**Date**: 2026-06-01
**Baseline Reference**: `analysis/git-post-merge-workflow-canonicalize/requirements.md`

## Source Baseline Summary

The frozen baseline requires one bounded child topic that promotes
`git-post-merge-workflow` into `skills/` as a canonical copy while preserving
the existing `.github/skills/...` contract during transition.

## Requirement Traceability

| Requirement | Technical realization | Status |
| --- | --- | --- |
| R1 scope | lock edits to the single candidate | feasible |
| R2 canonical copy | create `skills/git-post-merge-workflow/` | feasible |
| R3 preserve contract | keep STOP POINT 2 and `--ff-only` semantics intact | feasible |
| R4 full surface | copy `SKILL.md`, `examples.md`, and checklist reference | feasible |
| R5 compatibility layer | leave `.github/skills/...` unchanged | feasible |
| R6 defer repair | record deferred branch-policy / active-path work | feasible |
| R7 protect governance | avoid shared surfaces | feasible |
| R8 leave evidence | emit topic-local migration report | feasible |

## Copy Boundary

Source root: `.github/skills/git-post-merge-workflow/`

Target root: `skills/git-post-merge-workflow/`

Required copied paths:

- `SKILL.md`
- `examples.md`
- `references/stop-point-2-checklist.md`

## Execution Model

1. verify the source inventory
2. create the target tree
3. copy the full required file set
4. verify unchanged compatibility content
5. emit a topic-local migration report

## Verification Contract

- `skills/git-post-merge-workflow/SKILL.md` exists
- `skills/git-post-merge-workflow/examples.md` exists
- `skills/git-post-merge-workflow/references/stop-point-2-checklist.md` exists
- `.github/skills/git-post-merge-workflow/` remains unchanged
- no STOP POINT 2 semantics were changed

## Deferred Blocker Inventory

- active-path switching
- branch-policy redesign
- release-surface changes

## Ready-for-next-step Decision

This specification is sufficient for bounded canonical copy execution.
