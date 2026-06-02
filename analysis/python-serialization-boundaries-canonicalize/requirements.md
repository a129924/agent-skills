# Requirements: python-serialization-boundaries-canonicalize

**Status**: FROZEN — child-topic baseline ready; execution remains bounded to canonical copy work
**Topic**: `python-serialization-boundaries-canonicalize`
**Date**: 2026-06-01

## Problem Statement

`python-serialization-boundaries` is the semantic boundary candidate because it
defines how API payloads, DB rows, and queue messages become internal meaning
instead of leaking raw transport shape into business logic.

The candidate exists only under `.github/skills/python-serialization-boundaries/`
even though the target architecture expects canonical source material under `skills/`.

This child topic freezes a bounded move contract that creates a canonical copy
without widening into boundary-policy redesign or active-path cutover.

## Frozen Requirements

### R1 — Topic scope is one candidate only

This topic MUST stay locked to `python-serialization-boundaries` only.

### R2 — The topic creates a canonical `skills/` copy

The move outcome MUST be the creation of `skills/python-serialization-boundaries/`
as the canonical copy.

### R3 — Boundary contract must remain preserved

This topic MUST NOT change omitted/null/unchanged semantics, primitive
normalization rules, deep conversion guidance, or local-vs-shared schema policy.

### R4 — Full candidate surface must be copied

The canonical copy MUST preserve the full surface:

- `SKILL.md`
- `reference.md`
- `examples.md`
- `REVIEW.md`

### R5 — `.github/skills/` remains the compatibility layer

`.github/skills/python-serialization-boundaries/` must remain unchanged during this topic.

### R6 — Broader boundary repair remains deferred

This topic defers any active-path, adjacent-skill routing, or release-surface changes.

### R7 — Shared governance and release surfaces remain untouched

Do not edit `AGENTS.md`, `docs/repo-positioning.md`, `README.md`, `VERSION`,
or `.codex/skills/`.

### R8 — The topic must leave repo-visible evidence

Leave a migration report that states what moved, what stayed deferred, and that
the compatibility layer remained in place.

## Locked Decisions

- bounded canonical copy only
- target root is `skills/python-serialization-boundaries/`
- active behavior stays on `.github/skills/python-serialization-boundaries/`
- the canonical copy must include `REVIEW.md` in addition to the core skill files

## Non-goals

- no serialization-boundary semantic changes
- no adjacent-skill routing changes
- no shared governance or release metadata changes

## Success Signals

- the target tree exists with the full file set
- `.github/skills/python-serialization-boundaries/` is unchanged
- migration evidence makes the preserved compatibility layer obvious
