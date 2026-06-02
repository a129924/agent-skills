# Requirements: python-code-review-canonicalize

**Status**: FROZEN — child-topic baseline ready; execution remains bounded to canonical copy work
**Topic**: `python-code-review-canonicalize`
**Date**: 2026-06-01

---

## Problem Statement

`python-code-review` is the second Wave 2 governance-and-review candidate and
must remain sequenced after `python-implementation-review`, because its purpose
is to judge Python code quality only after implementation-to-plan alignment has
already been approved.

The current gap is not missing behavior. The current gap is that the candidate
exists only under `.github/skills/python-code-review/` even though the target
architecture expects canonical source material under
`skills/python-code-review/`.

This candidate is also a confirmed runtime/tooling and sequencing/tooling
coupling blocker because its live contract still depends on transition-era
surfaces and gates, including:

- a hard sequencing gate that refuses to run before
  `python-implementation-review` approval
- tooling detection and severity calibration tied to current project-file
  inspection order and current downstream assumptions
- verdict behavior that maps any `blocking` finding to `needs-rework`
- cross-skill routing and observability/test-quality rules that remain live on
  the `.github/skills/...` surface

Therefore this child topic must freeze one bounded move contract that creates a
canonical copy without widening into active-path cutover, sequencing-gate
redesign, tooling-detection redesign, verdict-policy repair, or release-surface
repair.

## Actors

| Actor | Role |
| --- | --- |
| Child-topic planning actor | Defines the bounded canonicalization contract for this candidate |
| Main Agent / implementer | Later performs only the authorized copy and preservation work |
| Downstream code-review consumers | Continue relying on the existing `.github/skills/...` contract during transition |
| Human operator | Preserves the no-cutover boundary and approves later execution |

## Frozen Requirements

### R1 — Topic scope is one candidate only

This topic MUST stay locked to `python-code-review` only.

- Actor: child-topic planning actor
- Condition: the candidate move contract is authored
- Observable: no second skill candidate is included in the topic scope
- Acceptance: later implementation cannot silently absorb
  `python-implementation-review`, `python-async-planning`, or any Wave 3
  candidate
- Failure meaning: the topic widens beyond a bounded child topic

### R2 — The topic creates a canonical `skills/` copy

The move outcome for this candidate MUST be the creation of
`skills/python-code-review/` as the target-architecture canonical copy.

- Actor: later implementer
- Condition: this child topic is executed
- Observable: a new `skills/python-code-review/` tree exists
- Acceptance: the canonical copy contains the same functional skill surface as
  the current `.github/skills/python-code-review/` candidate
- Failure meaning: the candidate remains absent from the target canonical source

### R3 — Transition-era sequencing, tooling-detection, and verdict semantics must remain preserved

This topic MUST NOT change the live contract semantics for:

- requiring `python-implementation-review` approval before
  `python-code-review` can run
- tooling detection order across `pyproject.toml`, `Makefile`,
  `README.md` / `CONTRIBUTING.md`, then generic fallback
- strict-mode severity calibration for pyright / mypy and lint-tool-informed
  warnings
- verdict behavior where one or more `blocking` findings yields
  `needs-rework`

- Actor: later implementer
- Condition: the canonical copy is created
- Observable: no artifact in this topic claims that
  `skills/python-code-review/` is already the active runtime path or that
  sequencing / verdict behavior changed
- Acceptance: transition-era behavior remains on the existing `.github/skills/...`
  surface during this topic
- Failure meaning: the topic turns a bounded copy into an unplanned gate,
  tooling, or verdict-policy migration

### R4 — Full candidate surface must be copied

The canonical copy MUST preserve the full candidate surface needed to represent
the skill truthfully:

- `SKILL.md`
- `examples.md`
- `reference.md`
- `references/anti-patterns.md`
- `references/cross-skill-signposts.md`
- `references/observability.md`
- `references/test-quality.md`
- `references/tooling-detection.md`

- Actor: later implementer
- Condition: file-copy boundaries are defined
- Observable: the canonical copy includes the full contract, worked examples,
  overview reference, and all five split references
- Acceptance: no required reference is silently omitted
- Failure meaning: later users see a partial or misleading canonical source

### R5 — `.github/skills/` remains the compatibility layer

This topic MUST preserve `.github/skills/python-code-review/` unchanged as the
transition-era compatibility surface.

- Actor: later implementer
- Condition: the canonical copy is created
- Observable: `.github/skills/python-code-review/` still exists with no
  content changes
- Acceptance: the repo continues honoring the frozen positioning that
  `.github/skills/` remains current active authored / reviewed path during
  transition
- Failure meaning: the topic performs hidden cutover or damages the live source

### R6 — Runtime/tooling and sequencing/tooling repair remains deferred

This topic MUST explicitly defer broader runtime/tooling and
sequencing/tooling-coupling work, including:

- changing the sequencing gate away from `python-implementation-review`
  approval
- changing tooling detection priority order or strict-mode escalation behavior
- changing verdict mapping from `blocking` findings to `needs-rework`
- changing cross-skill routing or quality-dimension ownership rules
- changing downstream projection, release, or active-path assumptions

- Actor: child-topic planning actor
- Condition: boundaries are frozen
- Observable: deferred blocker lanes are named explicitly
- Acceptance: later execution does not need to guess whether blocker repair is
  included
- Failure meaning: the topic invites hidden gate, tooling, or verdict changes

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
- which runtime/tooling and sequencing/tooling blockers were intentionally
  deferred
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
- The candidate remains a confirmed runtime/tooling blocker for future
  sequencing-gate, tooling-detection, and verdict-policy transition work.
- The topic is allowed to create `skills/python-code-review/`.
- The topic is not allowed to rewrite sequencing-gate behavior, tooling
  detection, severity calibration, or verdict mapping.
- The canonical copy must include `reference.md` and all five split references,
  not only `SKILL.md` and examples.

## Non-goals

- Do not switch the active skill execution path to `skills/python-code-review/`.
- Do not modify sequencing-gate semantics, tooling-detection behavior, severity
  calibration, or verdict behavior in this topic.
- Do not rewrite downstream `.github/skills/` routing, observability, test
  quality, or anti-pattern contracts.
- Do not update `.codex/skills` mapping, `README.md`, `VERSION`, or release
  metadata.
- Do not widen into `python-implementation-review` or `python-async-planning`.

## Resolved Contradictions

### C1 — canonical copy vs sequencing/tooling policy

- Conflict: creating a canonical `skills/` copy can look like permission to
  rewrite review entry gates or tooling-detection behavior
- Resolution: this topic creates the canonical copy only; transition-era gate
  and tooling behavior remain unchanged

### C2 — bounded child topic vs verdict / quality-policy repair topic

- Conflict: the candidate clearly exposes strict-mode, verdict, and routing
  semantics that could tempt this topic to absorb broader review-policy repair
- Resolution: preserve blocker status and defer repair to separate future topics

## Explicit Assumptions

- A1: the current `.github/skills/python-code-review/` surface is the only live
  transition-era contract during this topic
- A2: creating a canonical copy in `skills/` is still useful even when active
  behavior remains on `.github/skills/`
- A3: sequencing-gate, tooling-detection, verdict-policy, and routing
  transition work will require separate later topics
- A4: work for this child topic should also happen in a dedicated worktree, not
  on repo-root `dev`
