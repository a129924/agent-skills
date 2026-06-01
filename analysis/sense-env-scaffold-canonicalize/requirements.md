# Requirements: sense-env-scaffold-canonicalize

**Status**: FROZEN — child-topic baseline ready; execution remains bounded to canonical copy work
**Topic**: `sense-env-scaffold-canonicalize`
**Date**: 2026-06-01

---

## Problem Statement

`sense-env-scaffold` is the first Wave 1 canonicalization candidate because it is
the environment-sensing foundation for downstream retrofit and greenfield flows.

The current gap is not missing behavior. The current gap is that the candidate
exists only under `.github/skills/sense-env-scaffold/` even though the target
architecture expects canonical source material under `skills/`.

This candidate is also a confirmed runtime/tooling blocker because:

- the executable CLI path `.github/skills/sense-env-scaffold/scripts/sense_env.py`
  is part of the published skill contract
- downstream skills and plans reference that exact path
- changing the active execution path would widen into broader runtime and
  governance transition work

Therefore this child topic must freeze one bounded move contract that creates a
canonical copy without widening into active-path cutover or runtime path repair.

## Actors

| Actor | Role |
| --- | --- |
| Child-topic planning actor | Defines the bounded canonicalization contract for this candidate |
| Main Agent / implementer | Later performs only the authorized copy and preservation work |
| Downstream skill callers | Continue relying on the existing `.github/skills/.../sense_env.py` path during transition |
| Human operator | Preserves the no-cutover boundary and approves later execution |

## Frozen Requirements

### R1 — Topic scope is one candidate only

This topic MUST stay locked to `sense-env-scaffold` only.

- Actor: child-topic planning actor
- Condition: the candidate move contract is authored
- Observable: no second skill candidate is included in the topic scope
- Acceptance: later implementation cannot absorb adjacent runtime/tooling
  blockers such as `python-project-retrofit` or `python-project-init-greenfield`
- Failure meaning: the topic silently widens beyond a bounded child topic

### R2 — The topic creates a canonical `skills/` copy

The move outcome for this candidate MUST be the creation of
`skills/sense-env-scaffold/` as the target-architecture canonical copy.

- Actor: later implementer
- Condition: this child topic is executed
- Observable: a new `skills/sense-env-scaffold/` tree exists
- Acceptance: the canonical copy contains the same functional skill surface as
  the current `.github/skills/sense-env-scaffold/` candidate
- Failure meaning: the candidate remains absent from the target canonical source

### R3 — Runtime command path must remain preserved during this topic

This topic MUST NOT change the live execution contract that calls:

- `.github/skills/sense-env-scaffold/scripts/sense_env.py`

- Actor: later implementer
- Condition: the canonical copy is created
- Observable: downstream callers still reference and can continue using the
  existing `.github/skills/...` executable path during transition
- Acceptance: no artifact in this topic claims that `skills/sense-env-scaffold/`
  is already the active runtime path
- Failure meaning: the topic turns a bounded copy into an unplanned runtime cutover

### R4 — Full candidate surface must be copied, not partially restated

The canonical copy MUST preserve the full candidate surface needed to represent
the skill truthfully:

- `SKILL.md`
- `examples.md`
- `references/`
- `scripts/sense_env.py`
- `scripts/sense_env_runtime/`

- Actor: later implementer
- Condition: file-copy boundaries are defined
- Observable: the canonical copy includes the full contract, references, CLI,
  and local runtime package
- Acceptance: no required sub-surface is omitted or replaced by summary prose
- Failure meaning: the canonical copy becomes structurally incomplete

### R5 — Existing `.github/skills/` surface remains the transition compatibility layer

This topic MUST preserve `.github/skills/sense-env-scaffold/` as the transition-era
compatibility surface after the canonical copy exists.

- Actor: later implementer
- Condition: the move work is executed
- Observable: the `.github/skills/` candidate remains present after the copy
- Acceptance: the topic documents compatibility retention without claiming
  retirement or repo-wide source-of-truth cutover
- Failure meaning: the topic collapses compatibility and canonical-source roles

### R6 — Runtime/tooling blocker repair remains deferred

This topic MUST explicitly defer broader runtime/tooling transition work,
including:

- downstream caller rewrites
- executable-path aliasing or replacement
- manifest-output policy changes
- active-path switching for acceptance or discovery commands

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

- Actor: later implementer
- Condition: the move work finishes
- Observable: a topic-local migration report or equivalent explicit evidence
  exists
- Acceptance: the resulting state is inspectable without hidden chat context
- Failure meaning: later agents cannot distinguish completed copy work from deferred transition work

## Locked Decisions

- This is a bounded canonical-copy topic, not an active-path cutover topic.
- The candidate remains a confirmed runtime/tooling blocker for future path
  transition work.
- The topic is allowed to create `skills/sense-env-scaffold/`.
- The topic is not allowed to retarget downstream callers away from
  `.github/skills/sense-env-scaffold/scripts/sense_env.py`.
- The canonical copy must include scripts and the local runtime package, not only
  documentation files.

## Non-goals

- Do not switch the active runtime path to `skills/sense-env-scaffold/`.
- Do not modify `sense_env.py` behavior, supported assertion kinds, or manifest
  schema in this topic.
- Do not rewrite downstream plans or skills that invoke the existing
  `.github/skills/.../sense_env.py` path.
- Do not update `.codex/skills` mapping, `README.md`, `VERSION`, or release metadata.
- Do not widen into `python-project-init-greenfield`,
  `python-retrofit-plan-authoring`, `python-retrofit-plan-review`, or
  `python-project-retrofit`.

## Resolved Contradictions

### C1 — canonical copy vs runtime cutover

- Conflict: creating a canonical `skills/` copy can look like permission to move
  the live CLI path immediately
- Resolution: this topic creates the canonical copy only; runtime path remains
  `.github/skills/...` during transition

### C2 — documentation-only copy vs full executable surface

- Conflict: a lighter move could copy only Markdown artifacts
- Resolution: copy the full executable candidate surface so the canonical source
  is structurally real, not a placeholder

### C3 — bounded child topic vs blocker-repair topic

- Conflict: confirmed runtime/tooling blocker evidence could tempt this topic to
  absorb downstream path repair
- Resolution: preserve blocker status and defer repair to a separate future topic

## Explicit Assumptions

- A1: the current `.github/skills/sense-env-scaffold/` surface is the only live
  runtime contract during this topic
- A2: creating a canonical copy in `skills/` is still useful even when active
  execution remains on `.github/skills/`
- A3: downstream caller updates will require a separate runtime/tooling transition
  topic
- A4: work for this child topic should also happen in a dedicated worktree, not
  on repo-root `dev`

## Success Signals

This child topic is ready for execution planning when:

1. the bounded copy goal is frozen separately from runtime cutover
2. the full candidate surface to be copied is explicit
3. compatibility retention under `.github/skills/` is explicit
4. deferred runtime/tooling blocker lanes are named explicitly
5. shared governance surfaces remain out of scope
