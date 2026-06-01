# Requirements: python-retrofit-plan-review-canonicalize

**Status**: FROZEN — child-topic baseline ready; execution remains bounded to canonical copy work
**Topic**: `python-retrofit-plan-review-canonicalize`
**Date**: 2026-06-01

---

## Problem Statement

`python-retrofit-plan-review` is the third Wave 1 canonicalization candidate
because it is the retrofit quality gate between authoring and execution.

The current gap is not missing behavior. The current gap is that the candidate
exists only under `.github/skills/python-retrofit-plan-review/` even though the
target architecture expects canonical source material under `skills/`.

This candidate is part of the planning spine and semantically coupled to:

- `python-retrofit-plan-authoring` through the authored Retrofit V2 contract it reviews
- `python-project-retrofit` through executor handoff expectations
- `sense-env-scaffold` through supported `yaml [sensing-assertions]` kind boundaries

Therefore this child topic must freeze one bounded move contract that creates a
canonical copy without widening into review-verdict redesign, downstream
executor changes, or active-path cutover.

## Actors

| Actor | Role |
| --- | --- |
| Child-topic planning actor | Defines the bounded canonicalization contract for this candidate |
| Main Agent / implementer | Later performs only the authorized copy and preservation work |
| Downstream planning-spine consumers | Continue relying on the existing `.github/skills/` surface during transition |
| Human operator | Preserves the no-cutover boundary and approves later execution |

## Frozen Requirements

### R1 — Topic scope is one candidate only

This topic MUST stay locked to `python-retrofit-plan-review` only.

- Actor: child-topic planning actor
- Condition: the candidate move contract is authored
- Observable: no second skill candidate is included in the topic scope
- Acceptance: later implementation cannot silently absorb
  `python-retrofit-plan-authoring` or `python-project-retrofit`
- Failure meaning: the topic widens beyond a bounded child topic

### R2 — The topic creates a canonical `skills/` copy

The move outcome for this candidate MUST be the creation of
`skills/python-retrofit-plan-review/` as the target-architecture canonical copy.

- Actor: later implementer
- Condition: this child topic is executed
- Observable: a new `skills/python-retrofit-plan-review/` tree exists
- Acceptance: the canonical copy contains the same functional skill surface as
  the current `.github/skills/python-retrofit-plan-review/` candidate
- Failure meaning: the candidate remains absent from the target canonical source

### R3 — Review-verdict and Retrofit V2 review semantics must remain preserved

This topic MUST NOT change the live contract semantics for:

- the single-JSON verdict output shape
- Retrofit V2 section-order review checks
- `yaml [migration-strategy]` review rules
- supported `yaml [sensing-assertions]` kind boundaries
- lane-fit and reroute behavior

- Actor: later implementer
- Condition: the canonical copy is created
- Observable: no artifact in this topic claims a new or revised review contract
- Acceptance: the move preserves current semantics rather than redesigning them
- Failure meaning: the topic turns a bounded copy into contract-surface rework

### R4 — Full candidate surface must be copied

The canonical copy MUST preserve the full candidate surface needed to represent
the skill truthfully:

- `SKILL.md`
- `examples.md`
- `checklist.md`
- `references/`

- Actor: later implementer
- Condition: file-copy boundaries are defined
- Observable: the canonical copy includes the full contract, examples,
  checklist, and references
- Acceptance: no required sub-surface is omitted or replaced by summary prose
- Failure meaning: the canonical copy becomes structurally incomplete

### R5 — Existing `.github/skills/` surface remains the transition compatibility layer

This topic MUST preserve `.github/skills/python-retrofit-plan-review/` as the
transition-era compatibility surface after the canonical copy exists.

- Actor: later implementer
- Condition: the move work is executed
- Observable: the `.github/skills/` candidate remains present after the copy
- Acceptance: the topic documents compatibility retention without claiming
  retirement or repo-wide source-of-truth cutover
- Failure meaning: the topic collapses compatibility and canonical-source roles

### R6 — Downstream coupled surfaces remain deferred

This topic MUST explicitly defer broader coupled-surface work, including:

- `python-retrofit-plan-authoring` synchronization beyond bounded copy
- `python-project-retrofit` synchronization beyond bounded copy
- `sense-env-scaffold` assertion-kind or CLI behavior changes
- any rewrite of downstream plan or review guidance that merely references this skill

- Actor: child-topic planning actor
- Condition: boundaries are frozen
- Observable: deferred coupled lanes are named explicitly
- Acceptance: later execution does not need to guess whether downstream
  synchronization is included
- Failure meaning: the topic invites hidden planning-spine edits

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
- which coupled planning-spine lanes were intentionally deferred

- Actor: later implementer
- Condition: the move work finishes
- Observable: a topic-local migration report or equivalent explicit evidence
  exists
- Acceptance: the resulting state is inspectable without hidden chat context
- Failure meaning: later agents cannot distinguish completed copy work from deferred coupled-lane work

## Locked Decisions

- This is a bounded canonical-copy topic, not a review-contract redesign topic.
- The topic is allowed to create `skills/python-retrofit-plan-review/`.
- The topic is not allowed to rewrite `python-retrofit-plan-authoring`,
  `python-project-retrofit`, or `sense-env-scaffold`.
- The canonical copy must include checklist and references, not only `SKILL.md`
  and examples.

## Non-goals

- Do not switch the active authored/reviewed path to `skills/`.
- Do not modify review-verdict contract, Retrofit V2 review checks, or sensing
  assertion-kind rules in this topic.
- Do not rewrite downstream planning-spine or executor surfaces.
- Do not update `.codex/skills` mapping, `README.md`, `VERSION`, or release metadata.
- Do not widen into `python-retrofit-plan-authoring` or `python-project-retrofit`.

## Resolved Contradictions

### C1 — canonical copy vs planning-spine gate redesign

- Conflict: this candidate is semantically central enough that a move could
  tempt broader contract cleanup
- Resolution: preserve semantics exactly and limit this topic to bounded copy

### C2 — single-candidate move vs coupled downstream references

- Conflict: downstream authoring and executor artifacts reference the same review semantics
- Resolution: keep those coupled lanes explicit but deferred

## Explicit Assumptions

- A1: the current `.github/skills/python-retrofit-plan-review/` surface is the
  only live transition-era contract during this topic
- A2: creating a canonical copy in `skills/` is still useful even when active
  authoring and review references remain on `.github/skills/`
- A3: downstream synchronization work will require separate later topics
- A4: work for this child topic should also happen in a dedicated worktree, not
  on repo-root `dev`

## Success Signals

This child topic is ready for execution planning when:

1. the bounded copy goal is frozen separately from contract redesign
2. the full candidate surface to be copied is explicit
3. compatibility retention under `.github/skills/` is explicit
4. deferred downstream coupled lanes are named explicitly
5. shared governance surfaces remain out of scope
