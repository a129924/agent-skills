# Requirements: python-project-retrofit-canonicalize

**Status**: FROZEN — child-topic baseline ready; execution remains bounded to canonical copy work
**Topic**: `python-project-retrofit-canonicalize`
**Date**: 2026-06-01

---

## Problem Statement

`python-project-retrofit` is the fourth Wave 1 canonicalization candidate
because it is the retrofit execution lane that closes the authoring -> review ->
execution spine.

The current gap is not missing behavior. The current gap is that the candidate
exists only under `.github/skills/python-project-retrofit/` even though the
target architecture expects canonical source material under `skills/`.

This candidate is also a confirmed runtime/tooling blocker because:

- it hard-codes acceptance handoff through
  `python3 .github/skills/sense-env-scaffold/scripts/sense_env.py --mode acceptance --contract-file retrofit-plan.md`
- it owns destructive gates, delta-report semantics, and provenance expectations
  that downstream migration work must preserve or explicitly replace
- changing the active execution path would widen into broader runtime and
  governance transition work

Therefore this child topic must freeze one bounded move contract that creates a
canonical copy without widening into active-path cutover, runtime handoff
repair, or executor-behavior redesign.

## Actors

| Actor | Role |
| --- | --- |
| Child-topic planning actor | Defines the bounded canonicalization contract for this candidate |
| Main Agent / implementer | Later performs only the authorized copy and preservation work |
| Downstream runtime/tooling consumers | Continue relying on the existing `.github/skills/...` execution surface during transition |
| Human operator | Preserves the no-cutover boundary and approves later execution |

## Frozen Requirements

### R1 — Topic scope is one candidate only

This topic MUST stay locked to `python-project-retrofit` only.

- Actor: child-topic planning actor
- Condition: the candidate move contract is authored
- Observable: no second skill candidate is included in the topic scope
- Acceptance: later implementation cannot silently absorb
  `sense-env-scaffold`, `python-project-init-greenfield`, or
  `python-retrofit-plan-review`
- Failure meaning: the topic widens beyond a bounded child topic

### R2 — The topic creates a canonical `skills/` copy

The move outcome for this candidate MUST be the creation of
`skills/python-project-retrofit/` as the target-architecture canonical copy.

- Actor: later implementer
- Condition: this child topic is executed
- Observable: a new `skills/python-project-retrofit/` tree exists
- Acceptance: the canonical copy contains the same functional skill surface as
  the current `.github/skills/python-project-retrofit/` candidate
- Failure meaning: the candidate remains absent from the target canonical source

### R3 — Runtime execution contract must remain preserved during this topic

This topic MUST NOT change the live execution contract for:

- `python3 .github/skills/sense-env-scaffold/scripts/sense_env.py --mode acceptance --contract-file retrofit-plan.md`
- the three-gate execution model
- delta-report semantics
- provenance destination semantics

- Actor: later implementer
- Condition: the canonical copy is created
- Observable: no artifact in this topic claims that `skills/python-project-retrofit/`
  is already the active runtime path
- Acceptance: runtime behavior remains on the existing `.github/skills/...`
  surface during transition
- Failure meaning: the topic turns a bounded copy into an unplanned runtime cutover

### R4 — Full candidate surface must be copied

The canonical copy MUST preserve the full candidate surface needed to represent
the skill truthfully:

- `SKILL.md`
- `examples.md`
- `references/retrofit-conflict-resolution.md`
- `references/retrofit-plan-v2-contract.md`
- `references/retrofit-safety-guidelines.md`
- `references/sensing-delta-contract.md`

- Actor: later implementer
- Condition: file-copy boundaries are defined
- Observable: the canonical copy includes the full contract, examples, and all
  executor references
- Acceptance: no required sub-surface is omitted or replaced by summary prose
- Failure meaning: the canonical copy becomes structurally incomplete

### R5 — Existing `.github/skills/` surface remains the transition compatibility layer

This topic MUST preserve `.github/skills/python-project-retrofit/` as the
transition-era compatibility and active runtime surface after the canonical copy
exists.

- Actor: later implementer
- Condition: the move work is executed
- Observable: the `.github/skills/` candidate remains present after the copy
- Acceptance: the topic documents compatibility retention without claiming
  retirement or repo-wide source-of-truth cutover
- Failure meaning: the topic collapses compatibility and canonical-source roles

### R6 — Runtime/tooling blocker repair remains deferred

This topic MUST explicitly defer broader runtime/tooling transition work,
including:

- downstream replacement of the `.github/skills/sense-env-scaffold/scripts/sense_env.py`
  acceptance path
- executor-path aliasing or alternate active runtime path design
- provenance path-policy changes
- delta-report contract changes
- active-path switching for execution guidance

- Actor: child-topic planning actor
- Condition: boundaries are frozen
- Observable: deferred blocker lanes are named explicitly
- Acceptance: later execution does not need to guess whether blocker repair is
  included
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
- Observable: all edits stay candidate-local except for a topic-local migration
  report if one is authorized later
- Acceptance: the move remains a bounded canonicalization topic
- Failure meaning: the topic widens into repo-wide migration governance

### R8 — The topic must leave repo-visible evidence of what moved and what stayed deferred

The execution topic derived from this baseline MUST leave enough evidence that
another agent can tell:

- what was copied into `skills/`
- that `.github/skills/` remained the compatibility layer
- which runtime/tooling blockers were intentionally deferred
- that confirmed-blocker status remained evidence context rather than being silently erased

- Actor: later implementer
- Condition: the move work finishes
- Observable: a topic-local migration report or equivalent explicit evidence
  exists
- Acceptance: the resulting state is inspectable without hidden chat context
- Failure meaning: later agents cannot distinguish completed copy work from deferred blocker work

## Locked Decisions

- This is a bounded canonical-copy topic, not an active-path cutover topic.
- The candidate remains a confirmed runtime/tooling blocker for future path
  transition work.
- The topic is allowed to create `skills/python-project-retrofit/`.
- The topic is not allowed to retarget acceptance or provenance behavior away
  from the existing `.github/skills/...` execution surface.
- The canonical copy must include all executor references, not only `SKILL.md`
  and examples.

## Non-goals

- Do not switch the active runtime path to `skills/python-project-retrofit/`.
- Do not modify executor behavior, supported gates, delta-report schema, or
  provenance semantics in this topic.
- Do not rewrite downstream acceptance or runtime/tooling callers.
- Do not update `.codex/skills` mapping, `README.md`, `VERSION`, or release metadata.
- Do not widen into `sense-env-scaffold`, `python-project-init-greenfield`, or
  planning-spine redesign.

## Resolved Contradictions

### C1 — canonical copy vs runtime cutover

- Conflict: creating a canonical `skills/` copy can look like permission to move
  the live execution path immediately
- Resolution: this topic creates the canonical copy only; runtime execution
  remains on `.github/skills/...` during transition

### C2 — bounded child topic vs blocker-repair topic

- Conflict: confirmed runtime/tooling blocker evidence could tempt this topic to
  absorb acceptance-path or executor-path repair
- Resolution: preserve blocker status and defer repair to a separate future topic

## Explicit Assumptions

- A1: the current `.github/skills/python-project-retrofit/` surface is the only
  live runtime contract during this topic
- A2: creating a canonical copy in `skills/` is still useful even when active
  execution remains on `.github/skills/`
- A3: runtime/tooling transition work will require a separate later topic
- A4: work for this child topic should also happen in a dedicated worktree, not
  on repo-root `dev`

## Success Signals

This child topic is ready for execution planning when:

1. the bounded copy goal is frozen separately from runtime cutover
2. the full candidate surface to be copied is explicit
3. compatibility retention under `.github/skills/` is explicit
4. deferred runtime/tooling blocker lanes are named explicitly
5. shared governance surfaces remain out of scope
