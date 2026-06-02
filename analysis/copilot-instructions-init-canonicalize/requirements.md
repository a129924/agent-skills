# Requirements: copilot-instructions-init-canonicalize

**Status**: FROZEN — child-topic baseline ready; execution remains bounded to canonical copy work
**Topic**: `copilot-instructions-init-canonicalize`
**Date**: 2026-06-01

---

## Problem Statement

`copilot-instructions-init` is the first Wave 2 canonicalization candidate
because it governs generation or refresh of a target project's
`.github/copilot-instructions.md` after the Python project lane is in place.

The current gap is not missing behavior. The current gap is that the candidate
exists only under `.github/skills/copilot-instructions-init/` even though the
target architecture expects canonical source material under
`skills/copilot-instructions-init/`.

This candidate is also a confirmed runtime/tooling blocker because its live
contract still depends on transition-era surfaces and gates, including:

- writing exactly one target-project `.github/copilot-instructions.md`
- stale-fact validation against `.github/skills/` summary fingerprints
- overwrite / keep / manual-merge behavior tied to current target-path policy
- managed-block handling for existing target-project instruction content

Therefore this child topic must freeze one bounded move contract that creates a
canonical copy without widening into active-path cutover, stale-check redesign,
target output-path changes, or merge-policy repair.

## Actors

| Actor | Role |
| --- | --- |
| Child-topic planning actor | Defines the bounded canonicalization contract for this candidate |
| Main Agent / implementer | Later performs only the authorized copy and preservation work |
| Downstream target-project consumers | Continue relying on the existing `.github/skills/...` contract during transition |
| Human operator | Preserves the no-cutover boundary and approves later execution |

## Frozen Requirements

### R1 — Topic scope is one candidate only

This topic MUST stay locked to `copilot-instructions-init` only.

- Actor: child-topic planning actor
- Condition: the candidate move contract is authored
- Observable: no second skill candidate is included in the topic scope
- Acceptance: later implementation cannot silently absorb
  `python-project-init-greenfield`, `python-implementation-review`, or
  `python-code-review`
- Failure meaning: the topic widens beyond a bounded child topic

### R2 — The topic creates a canonical `skills/` copy

The move outcome for this candidate MUST be the creation of
`skills/copilot-instructions-init/` as the target-architecture canonical copy.

- Actor: later implementer
- Condition: this child topic is executed
- Observable: a new `skills/copilot-instructions-init/` tree exists
- Acceptance: the canonical copy contains the same functional skill surface as
  the current `.github/skills/copilot-instructions-init/` candidate
- Failure meaning: the candidate remains absent from the target canonical source

### R3 — Transition-era target output and stale-fact contracts must remain preserved

This topic MUST NOT change the live contract semantics for:

- generating or refreshing exactly one target-project `.github/copilot-instructions.md`
- stale-fact validation against Git `HEAD`, `pyproject.toml` / `uv.lock`, and
  `.github/skills/` summary fingerprints
- managed-block versus non-managed-block detection for existing instructions
- the overwrite choice set of `full overwrite`, `keep current content`, or
  `manual merge by the human`

- Actor: later implementer
- Condition: the canonical copy is created
- Observable: no artifact in this topic claims that
  `skills/copilot-instructions-init/` is already the active runtime or output
  path
- Acceptance: transition-era behavior remains on the existing `.github/skills/...`
  surface during this topic
- Failure meaning: the topic turns a bounded copy into an unplanned target
  output or stale-gate cutover

### R4 — Full candidate surface must be copied

The canonical copy MUST preserve the full candidate surface needed to represent
the skill truthfully:

- `SKILL.md`
- `checklist.md`
- `examples.md`
- `references/input-sources-and-priority.md`
- `references/instruction-layering.md`
- `references/merge-and-conflict-policy.md`

- Actor: later implementer
- Condition: file-copy boundaries are defined
- Observable: the canonical copy includes the full contract, checklist,
  examples, and all three references
- Acceptance: no required sub-surface is omitted or replaced by summary prose
- Failure meaning: the canonical copy becomes structurally incomplete

### R5 — Existing `.github/skills/` surface remains the transition compatibility layer

This topic MUST preserve `.github/skills/copilot-instructions-init/` as the
transition-era compatibility and active skill surface after the canonical copy
exists.

- Actor: later implementer
- Condition: the move work is executed
- Observable: the `.github/skills/` candidate remains present after the copy
- Acceptance: the topic documents compatibility retention without claiming
  retirement or repo-wide source-of-truth cutover
- Failure meaning: the topic collapses compatibility and canonical-source roles

### R6 — Runtime/tooling and policy-coupling repair remains deferred

This topic MUST explicitly defer broader runtime/tooling and policy-coupling
work, including:

- changing the target output destination away from
  target-project `.github/copilot-instructions.md`
- changing stale-fact coupling away from `.github/skills/` summary fingerprints
- changing managed-block marker policy or materially-different classification behavior
- changing overwrite / keep / manual-merge decision policy
- changing downstream projection, release, or active-path assumptions

- Actor: child-topic planning actor
- Condition: boundaries are frozen
- Observable: deferred blocker lanes are named explicitly
- Acceptance: later execution does not need to guess whether blocker repair is
  included
- Failure meaning: the topic invites hidden path, policy, or tooling changes

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
- which runtime/tooling and policy-coupling blockers were intentionally deferred
- that confirmed-blocker status remained evidence context rather than being erased

- Actor: later implementer
- Condition: the move work finishes
- Observable: a topic-local migration report exists
- Acceptance: the resulting state is inspectable without hidden chat context
- Failure meaning: later agents cannot distinguish completed copy work from
  deferred blocker work

## Locked Decisions

- This is a bounded canonical-copy topic, not an active-path cutover topic.
- The candidate remains a confirmed runtime/tooling blocker for future path,
  stale-check, and output-surface transition work.
- The topic is allowed to create `skills/copilot-instructions-init/`.
- The topic is not allowed to rewrite the target-project output destination,
  stale-fingerprint contract, managed-block policy, or overwrite decision model.
- The canonical copy must include `checklist.md` and all three references, not
  only `SKILL.md` and examples.

## Non-goals

- Do not switch the active skill execution or output path to
  `skills/copilot-instructions-init/`.
- Do not modify generation logic, stale-fact semantics, merge-policy behavior,
  or target-project write behavior in this topic.
- Do not rewrite downstream `.github/skills/` summary, merge policy, or output
  contracts.
- Do not update `.codex/skills` mapping, `README.md`, `VERSION`, or release metadata.
- Do not widen into `python-project-init-greenfield`,
  `python-implementation-review`, or `python-code-review`.

## Resolved Contradictions

### C1 — canonical copy vs target output-path policy

- Conflict: creating a canonical `skills/` copy can look like permission to
  change where the skill writes target-project instructions
- Resolution: this topic creates the canonical copy only; transition-era target
  output behavior remains unchanged

### C2 — bounded child topic vs stale-gate / merge-policy repair topic

- Conflict: the candidate clearly exposes `.github/...` and stale-check / merge
  policy coupling that could tempt this topic to absorb broader repair
- Resolution: preserve blocker status and defer repair to separate future topics

## Explicit Assumptions

- A1: the current `.github/skills/copilot-instructions-init/` surface is the
  only live transition-era contract during this topic
- A2: creating a canonical copy in `skills/` is still useful even when active
  behavior remains on `.github/skills/`
- A3: stale-fact, overwrite-policy, and output-path transition work will require
  separate later topics
- A4: work for this child topic should also happen in a dedicated worktree, not
  on repo-root `dev`
