# Requirements: git-release-management-canonicalize

**Status**: FROZEN — child-topic baseline ready; execution remains bounded to canonical copy work
**Topic**: `git-release-management-canonicalize`
**Date**: 2026-06-01

## Problem Statement

`git-release-management` is the release gate candidate because it enforces
version synchronization, clean-workspace checks, tag safety, and emergency-path
rules before PR or tagging actions proceed.

The candidate exists only under `.github/skills/git-release-management/` even
though the target architecture expects canonical source material under `skills/`.

This child topic freezes a bounded move contract that creates a canonical copy
without widening into release-policy redesign or active-path cutover.

## Frozen Requirements

### R1 — Topic scope is one candidate only

This topic MUST stay locked to `git-release-management` only.

### R2 — The topic creates a canonical `skills/` copy

The move outcome MUST be the creation of `skills/git-release-management/` as the
canonical copy.

### R3 — Release gate contract must remain preserved

This topic MUST NOT change normal-path gates, emergency-path allowance, tag
uniqueness checks, version synchronization, or clean-workspace requirements.

### R4 — Full candidate surface must be copied

The canonical copy MUST preserve the full surface:

- `SKILL.md`
- `examples.md`
- `references/gate-contract.md`
- `references/version-sources.md`
- `references/version-bump-guidance.md`
- `references/emergency-path.md`

### R5 — `.github/skills/` remains the compatibility layer

`.github/skills/git-release-management/` must remain unchanged during this topic.

### R6 — Broader release repair remains deferred

This topic defers any release-policy redesign, tag-policy redesign, or
active-path transition work.

### R7 — Shared governance and release surfaces remain untouched

Do not edit `AGENTS.md`, `docs/repo-positioning.md`, `README.md`, `VERSION`,
or `.codex/skills/`.

### R8 — The topic must leave repo-visible evidence

Leave a migration report that states what moved, what stayed deferred, and that
the compatibility layer remained in place.

## Locked Decisions

- bounded canonical copy only
- target root is `skills/git-release-management/`
- active behavior stays on `.github/skills/git-release-management/`
- the canonical copy must include all four reference files, not just `SKILL.md`

## Non-goals

- no release-gate semantic changes
- no emergency-path policy changes
- no tag or version-policy changes
- no shared governance or release metadata changes

## Success Signals

- the target tree exists with the full file set
- `.github/skills/git-release-management/` is unchanged
- migration evidence makes the preserved compatibility layer obvious
