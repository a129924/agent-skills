# Requirements: python-async-planning-canonicalize

**Status**: FROZEN — child-topic baseline ready; execution remains bounded to canonical copy work
**Topic**: `python-async-planning-canonicalize`
**Date**: 2026-06-01

---

## Problem Statement

`python-async-planning` is the async planning gate candidate because it freezes
Python async boundary, lifecycle, concurrency, failure, and cancellation
decisions before implementation starts.

The current gap is not missing behavior. The current gap is that the candidate
exists only under `.github/skills/python-async-planning/` even though the
target architecture expects canonical source material under `skills/`.

Therefore this child topic must freeze one bounded move contract that creates a
canonical copy without widening into active-path cutover, async-rule redesign,
or broader workflow changes.

## Actors

| Actor | Role |
| --- | --- |
| Child-topic planning actor | Defines the bounded canonicalization contract for this candidate |
| Main Agent / implementer | Later performs only the authorized copy and preservation work |
| Downstream planning consumers | Continue relying on the existing `.github/skills/...` contract during transition |
| Human operator | Preserves the no-cutover boundary and approves later execution |

## Frozen Requirements

### R1 — Topic scope is one candidate only

This topic MUST stay locked to `python-async-planning` only.

- Actor: child-topic planning actor
- Condition: the candidate move contract is authored
- Observable: no second skill candidate is included in the topic scope
- Acceptance: later implementation cannot silently absorb other Python planning topics
- Failure meaning: the topic widens beyond a bounded child topic

### R2 — The topic creates a canonical `skills/` copy

The move outcome for this candidate MUST be the creation of
`skills/python-async-planning/` as the target-architecture canonical copy.

- Actor: later implementer
- Condition: this child topic is executed
- Observable: a new `skills/python-async-planning/` tree exists
- Acceptance: the canonical copy contains the same functional skill surface as
  the current `.github/skills/python-async-planning/` candidate
- Failure meaning: the candidate remains absent from the target canonical source

### R3 — Async-planning contract must remain preserved during this topic

This topic MUST NOT change the live semantics for:

- the async-planning trigger / exemption decision
- the seven required async-planning subsections
- contradiction log handling
- retrofit-required handling for late-discovered async risk

- Actor: later implementer
- Condition: the canonical copy is created
- Observable: no artifact in this topic claims that `skills/python-async-planning/`
  is already the active runtime path or that the async rules changed
- Acceptance: transition-era behavior remains on the existing `.github/skills/...`
  surface during this topic
- Failure meaning: the topic turns a bounded copy into an unplanned rule migration

### R4 — Full candidate surface must be copied

The canonical copy MUST preserve the full candidate surface needed to represent
the skill truthfully:

- `SKILL.md`
- `reference.md`
- `examples.md`

- Actor: later implementer
- Condition: file-copy boundaries are defined
- Observable: the canonical copy includes the full contract, reference, and examples
- Acceptance: no required sub-surface is omitted
- Failure meaning: later users see a partial or misleading canonical source

### R5 — `.github/skills/` remains the compatibility layer

This topic MUST preserve `.github/skills/python-async-planning/` unchanged as the
transition-era compatibility surface.

- Actor: later implementer
- Condition: the canonical copy is created
- Observable: `.github/skills/python-async-planning/` still exists with no content changes
- Acceptance: the repo continues honoring the frozen positioning that `.github/skills/`
  remains current active authored / reviewed path during transition
- Failure meaning: the topic performs hidden cutover or damages the live source

### R6 — Runtime/tooling repair remains deferred

This topic MUST explicitly defer broader runtime/tooling transition work,
including any change to path governance, active-path switching, or workflow
integration that would alter how this skill is consumed.

- Actor: child-topic planning actor
- Condition: boundaries are frozen
- Observable: deferred blocker lanes are named explicitly
- Acceptance: later execution does not need to guess whether broader workflow
  repair is included
- Failure meaning: the topic invites hidden path or tooling changes

### R7 — Shared governance and release surfaces remain untouched

This topic MUST NOT edit shared governance or release surfaces.

Protected surfaces include:

- `AGENTS.md`
- `docs/repo-positioning.md`
- `README.md`
- `VERSION`
- `.codex/skills/`
- repo-wide migration checklists

- Actor: later implementer
- Condition: the move is executed
- Observable: all edits stay candidate-local except for a topic-local migration report
- Acceptance: the move remains a bounded canonicalization topic
- Failure meaning: the topic widens into repo-wide migration governance

### R8 — The topic must leave repo-visible evidence of what moved and what stayed deferred

The execution topic derived from this baseline MUST leave enough evidence that
another agent can tell:

- what was copied into `skills/`
- that `.github/skills/` remained the compatibility layer
- which runtime/tooling lanes were intentionally deferred
- that preserved async-planning semantics remained evidence context rather than being erased

- Actor: later implementer
- Condition: the move work finishes
- Observable: a topic-local migration report exists
- Acceptance: the resulting state is inspectable without hidden chat context
- Failure meaning: later agents cannot distinguish completed copy work from deferred blocker work

## Locked Decisions

- This is a bounded canonical-copy topic, not an active-path cutover topic.
- The topic is allowed to create `skills/python-async-planning/`.
- The topic is not allowed to rewrite async trigger/exemption decisions,
  required subsection names, or contradiction-log semantics.
- The canonical copy must include all three source files, not only `SKILL.md`.

## Non-goals

- Do not switch the active skill execution path to `skills/python-async-planning/`.
- Do not modify the async-planning rule set in this topic.
- Do not update `.codex/skills` mapping, `README.md`, `VERSION`, or release metadata.
- Do not widen into unrelated planning, implementation, or runtime topics.

## Resolved Contradictions

### C1 — canonical copy vs active-path cutover

- Conflict: creating a canonical `skills/` copy can look like permission to
  rewrite the active path immediately
- Resolution: this topic creates the canonical copy only; transition-era behavior
  remains unchanged

## Explicit Assumptions

- A1: the current `.github/skills/python-async-planning/` surface is the only
  live contract during this topic
- A2: creating a canonical copy in `skills/` is still useful even when active
  execution remains on `.github/skills/`
- A3: later execution work will require a separate topic
- A4: work for this child topic should also happen in a dedicated worktree, not
  on repo-root `dev`

## Success Signals

This child topic is ready for execution planning when:

- the canonical `skills/python-async-planning/` tree can be created from the
  current source inventory
- `.github/skills/python-async-planning/` remains the compatibility layer
- a topic-local migration report can state what moved and what stayed deferred
- no shared governance or release surface needs to change
