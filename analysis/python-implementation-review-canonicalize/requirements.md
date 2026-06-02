# Requirements: python-implementation-review-canonicalize

**Status**: FROZEN — child-topic baseline ready; execution remains bounded to canonical copy work
**Topic**: `python-implementation-review-canonicalize`
**Date**: 2026-06-01

---

## Problem Statement

`python-implementation-review` is a Wave 2 governance-and-review candidate that
must remain sequenced ahead of `python-code-review`, because its purpose is to
verify whether an implementation matches an approved plan before any code-quality
review begins.

The current gap is not missing behavior. The current gap is that the candidate
exists only under `.github/skills/python-implementation-review/` even though the
target architecture expects canonical source material under
`skills/python-implementation-review/`.

This candidate is also a confirmed runtime/tooling and approval/step-gate
blocker because its live contract still depends on transition-era surfaces and
gates, including:

- formal approval from `python-plan-review` before traceability begins
- optional `plan/<topic>/<topic>.step.md` step gating before review can proceed
- BLOCKED refusal semantics when pending implementation steps remain
- sequencing that explicitly keeps `python-implementation-review` ahead of
  `python-code-review`

Therefore this child topic must freeze one bounded move contract that creates a
canonical copy without widening into active-path cutover, approval-gate
redesign, step-gate redesign, refusal-output repair, or sequencing repair.

## Actors

| Actor | Role |
| --- | --- |
| Child-topic planning actor | Defines the bounded canonicalization contract for this candidate |
| Main Agent / implementer | Later performs only the authorized copy and preservation work |
| Downstream implementation-review consumers | Continue relying on the existing `.github/skills/...` contract during transition |
| Human operator | Preserves the no-cutover boundary and approves later execution |

## Frozen Requirements

### R1 — Topic scope is one candidate only

This topic MUST stay locked to `python-implementation-review` only.

- Actor: child-topic planning actor
- Condition: the candidate move contract is authored
- Observable: no second skill candidate is included in the topic scope
- Acceptance: later implementation cannot silently absorb
  `copilot-instructions-init`, `python-code-review`, or `python-async-planning`
- Failure meaning: the topic widens beyond a bounded child topic

### R2 — The topic creates a canonical `skills/` copy

The move outcome for this candidate MUST be the creation of
`skills/python-implementation-review/` as the target-architecture canonical
copy.

- Actor: later implementer
- Condition: this child topic is executed
- Observable: a new `skills/python-implementation-review/` tree exists
- Acceptance: the canonical copy contains the same functional skill surface as
  the current `.github/skills/python-implementation-review/` candidate
- Failure meaning: the candidate remains absent from the target canonical source

### R3 — Transition-era approval, step-gate, and sequencing semantics must remain preserved

This topic MUST NOT change the live contract semantics for:

- requiring formal plan approval before tracing begins
- optional `plan/<topic>/<topic>.step.md` gating before review can proceed
- BLOCKED plain-text refusal behavior when pending implementation steps remain
- the sequencing rule that `python-implementation-review` runs before
  `python-code-review`

- Actor: later implementer
- Condition: the canonical copy is created
- Observable: no artifact in this topic claims that
  `skills/python-implementation-review/` is already the active runtime path or
  changes pre-review gating behavior
- Acceptance: transition-era behavior remains on the existing
  `.github/skills/...` surface during this topic
- Failure meaning: the topic turns a bounded copy into an unplanned gate or
  sequencing cutover

### R4 — Full candidate surface must be copied

The canonical copy MUST preserve the full candidate surface needed to represent
the skill truthfully:

- `SKILL.md`
- `examples.md`
- `reference.md`
- `references/contract-deviation-rules.md`
- `references/plan-section-structure.md`
- `references/semantic-boundaries.md`
- `references/traceability-status.md`

- Actor: later implementer
- Condition: file-copy boundaries are defined
- Observable: the canonical copy includes the full contract, examples,
  overview reference, and all four split references
- Acceptance: no required candidate file is omitted from the canonical copy
- Failure meaning: the canonical source becomes an incomplete mirror

### R5 — `.github/skills/` remains the compatibility layer in this topic

This topic MUST preserve `.github/skills/python-implementation-review/`
unchanged as the live transition-era compatibility surface.

- Actor: later implementer
- Condition: the bounded canonical copy is executed
- Observable: source files remain present and unmodified after the copy
- Acceptance: this topic does not imply immediate runtime-path or repo-wide
  source-of-truth cutover
- Failure meaning: the topic collapses compatibility and canonical-source roles

### R6 — Runtime/tooling, approval-gate, and step-gate repair remains deferred

This topic MUST explicitly defer broader runtime/tooling and gate-coupling
work, including:

- changing approval proof requirements away from the current `python-plan-review`
  contract
- changing `plan/<topic>/<topic>.step.md` gating semantics or pending-step
  detection rules
- changing BLOCKED refusal output semantics
- changing the sequencing dependency between
  `python-implementation-review` and `python-code-review`
- changing downstream projection, release, or active-path assumptions

- Actor: child-topic planning actor
- Condition: boundaries are frozen
- Observable: deferred blocker lanes are named explicitly
- Acceptance: later execution does not need to guess whether gate repair is
  included
- Failure meaning: the topic invites hidden gate, path, or tooling changes

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
  report
- Acceptance: the move remains a bounded canonicalization topic
- Failure meaning: the topic widens into repo-wide migration governance

### R8 — The topic must leave repo-visible evidence of what moved and what stayed deferred

The execution topic derived from this baseline MUST leave enough evidence that
another agent can tell:

- what was copied into `skills/`
- that `.github/skills/` remained the compatibility layer
- which runtime/tooling, approval-gate, and step-gate blockers were
  intentionally deferred
- that confirmed-blocker status remained evidence context rather than being
  erased

- Actor: later implementer
- Condition: the move work finishes
- Observable: a topic-local migration report exists
- Acceptance: the resulting state is inspectable without hidden chat context
- Failure meaning: later agents cannot distinguish completed copy work from
  deferred blocker work

## Locked Decisions

- This is a bounded canonical-copy topic, not an active-path cutover topic.
- The candidate remains a confirmed runtime/tooling blocker for future path,
  approval-gate, step-gate, and sequencing-transition work.
- The topic is allowed to create `skills/python-implementation-review/`.
- The topic is not allowed to rewrite approval proof rules, step-gate rules,
  BLOCKED refusal behavior, or sequencing with `python-code-review`.
- The canonical copy must include `reference.md` and all four split references,
  not only `SKILL.md` and examples.

## Non-goals

- Do not switch the active skill execution path to
  `skills/python-implementation-review/`.
- Do not modify approval-gate semantics, step-gate semantics, refusal output
  behavior, or review sequencing behavior in this topic.
- Do not rewrite downstream `.github/skills/` review contracts or release
  metadata.
- Do not update `.codex/skills` mapping, `README.md`, `VERSION`, or release
  metadata.
- Do not widen into `python-code-review` or `python-async-planning`.

## Resolved Contradictions

### C1 — canonical copy vs step-gate / approval-gate policy

- Conflict: creating a canonical `skills/` copy can look like permission to
  rewrite approval proof, step-gate, or BLOCKED refusal behavior
- Resolution: this topic creates the canonical copy only; transition-era gate
  behavior remains unchanged

### C2 — bounded child topic vs sequencing / runtime repair topic

- Conflict: the candidate clearly exposes step-gate and sequencing coupling
  that could tempt this topic to absorb broader repair
- Resolution: preserve blocker status and defer repair to separate future topics

## Explicit Assumptions

- A1: the current `.github/skills/python-implementation-review/` surface is the
  only live transition-era contract during this topic
- A2: creating a canonical copy in `skills/` is still useful even when active
  behavior remains on `.github/skills/`
- A3: approval-gate, step-gate, and sequencing transition work will require
  separate future topics once the canonical copy exists
