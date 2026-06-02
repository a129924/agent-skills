# Requirements: git-post-merge-workflow-canonicalize

**Status**: FROZEN — child-topic baseline ready; execution remains bounded to canonical copy work
**Topic**: `git-post-merge-workflow-canonicalize`
**Date**: 2026-06-01

---

## Problem Statement

`git-post-merge-workflow` is the post-merge cleanup candidate because it
standardizes STOP POINT 2 resume checks, fast-forward-only sync, and branch
cleanup after a merge is already confirmed.

The current gap is that the candidate exists only under
`.github/skills/git-post-merge-workflow/` even though the target architecture
expects canonical source material under `skills/`.

This child topic therefore freezes one bounded move contract that creates a
canonical copy without widening into active-path cutover, branch-policy
redesign, or release-gate changes.

## Frozen Requirements

### R1 — Topic scope is one candidate only

This topic MUST stay locked to `git-post-merge-workflow` only.

### R2 — The topic creates a canonical `skills/` copy

The move outcome MUST be the creation of `skills/git-post-merge-workflow/` as
the canonical copy.

### R3 — Post-merge workflow contract must remain preserved

This topic MUST NOT change STOP POINT 2, verified-merge requirements,
`--ff-only` sync behavior, or cleanup boundaries.

### R4 — Full candidate surface must be copied

The canonical copy MUST preserve the full surface:

- `SKILL.md`
- `examples.md`
- `references/stop-point-2-checklist.md`

### R5 — `.github/skills/` remains the compatibility layer

`.github/skills/git-post-merge-workflow/` must remain unchanged during this topic.

### R6 — Broader workflow repair remains deferred

This topic defers any active-path, branch-policy, or release-related transition
work.

### R7 — Shared governance and release surfaces remain untouched

Do not edit `AGENTS.md`, `docs/repo-positioning.md`, `README.md`, `VERSION`,
or `.codex/skills/`.

### R8 — The topic must leave repo-visible evidence

Leave a migration report that states what moved, what stayed deferred, and that
the compatibility layer remained in place.

## Locked Decisions

- bounded canonical copy only
- target root is `skills/git-post-merge-workflow/`
- active runtime behavior stays on `.github/skills/git-post-merge-workflow/`
- the canonical copy must include `references/stop-point-2-checklist.md`

## Non-goals

- no STOP POINT 2 semantic changes
- no branch deletion policy changes
- no release-gate changes
- no shared governance or release metadata changes

## Success Signals

- the target tree exists with the full file set
- `.github/skills/git-post-merge-workflow/` is unchanged
- migration evidence makes the preserved compatibility layer obvious
