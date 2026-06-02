# Requirements: python-project-init-greenfield-canonicalize

**Status**: FROZEN — child-topic baseline ready; execution remains bounded to canonical copy work
**Topic**: `python-project-init-greenfield-canonicalize`
**Date**: 2026-06-01

---

## Problem Statement

`python-project-init-greenfield` is the Wave 1.5 canonicalization candidate
because it completes the Python project lane immediately after the Retrofit
spine without being a prerequisite for that spine.

The current gap is not missing behavior. The current gap is that the candidate
exists only under `.github/skills/python-project-init-greenfield/` even though
the target architecture expects canonical source material under `skills/`.

This candidate is also a confirmed runtime/tooling blocker because it embeds
transition-era output and acceptance contracts that still depend on:

- copied required skill folders under `.github/skills/`
- governance provenance at `.github/skills-provenance.json`
- placeholder guidance at `.github/copilot-instructions.md`
- acceptance through `python3 .github/skills/sense-env-scaffold/scripts/sense_env.py --mode acceptance --contract-file blueprint.md`

Therefore this child topic must freeze one bounded move contract that creates a
canonical copy without widening into active-path cutover, downstream output
surface redesign, or runtime/tooling repair.

## Actors

| Actor | Role |
| --- | --- |
| Child-topic planning actor | Defines the bounded canonicalization contract for this candidate |
| Main Agent / implementer | Later performs only the authorized copy and preservation work |
| Downstream greenfield-init consumers | Continue relying on the existing `.github/skills/...` skill contract during transition |
| Human operator | Preserves the no-cutover boundary and approves later execution |

## Frozen Requirements

### R1 — Topic scope is one candidate only

This topic MUST stay locked to `python-project-init-greenfield` only.

- Actor: child-topic planning actor
- Condition: the candidate move contract is authored
- Observable: no second skill candidate is included in the topic scope
- Acceptance: later implementation cannot silently absorb
  `sense-env-scaffold`, `python-project-retrofit`, or
  `copilot-instructions-init`
- Failure meaning: the topic widens beyond a bounded child topic

### R2 — The topic creates a canonical `skills/` copy

The move outcome for this candidate MUST be the creation of
`skills/python-project-init-greenfield/` as the target-architecture canonical
copy.

- Actor: later implementer
- Condition: this child topic is executed
- Observable: a new `skills/python-project-init-greenfield/` tree exists
- Acceptance: the canonical copy contains the same functional skill surface as
  the current `.github/skills/python-project-init-greenfield/` candidate
- Failure meaning: the candidate remains absent from the target canonical source

### R3 — Transition-era output and acceptance contracts must remain preserved

This topic MUST NOT change the live contract semantics for:

- copying required skills into `.github/skills/`
- writing governance provenance to `.github/skills-provenance.json`
- placeholder guidance expectations for `.github/copilot-instructions.md`
- acceptance through
  `python3 .github/skills/sense-env-scaffold/scripts/sense_env.py --mode acceptance --contract-file blueprint.md`
- leaving `blueprint.md` as the persistent design contract

- Actor: later implementer
- Condition: the canonical copy is created
- Observable: no artifact in this topic claims that `skills/python-project-init-greenfield/`
  is already the active runtime or output path
- Acceptance: transition-era behavior remains on the existing `.github/skills/...`
  surface during this topic
- Failure meaning: the topic turns a bounded copy into an unplanned runtime or
  downstream output cutover

### R4 — Full candidate surface must be copied

The canonical copy MUST preserve the full candidate surface needed to represent
the skill truthfully:

- `SKILL.md`
- `examples.md`
- `references/baseline-generation-rules.md`
- `references/blueprint-parsing-contract.md`

- Actor: later implementer
- Condition: file-copy boundaries are defined
- Observable: the canonical copy includes the full contract, examples, and
  both references
- Acceptance: no required sub-surface is omitted or replaced by summary prose
- Failure meaning: the canonical copy becomes structurally incomplete

### R5 — Existing `.github/skills/` surface remains the transition compatibility layer

This topic MUST preserve `.github/skills/python-project-init-greenfield/` as the
transition-era compatibility and active skill surface after the canonical copy
exists.

- Actor: later implementer
- Condition: the move work is executed
- Observable: the `.github/skills/` candidate remains present after the copy
- Acceptance: the topic documents compatibility retention without claiming
  retirement or repo-wide source-of-truth cutover
- Failure meaning: the topic collapses compatibility and canonical-source roles

### R6 — Runtime/tooling and downstream output repair remains deferred

This topic MUST explicitly defer broader runtime/tooling and output-surface work,
including:

- changing required-skill deployment away from `.github/skills/`
- moving governance provenance away from `.github/skills-provenance.json`
- changing `.github/copilot-instructions.md` output policy
- changing the canonical acceptance path away from
  `.github/skills/sense-env-scaffold/scripts/sense_env.py`
- changing downstream release, projection, or active-path assumptions

- Actor: child-topic planning actor
- Condition: boundaries are frozen
- Observable: deferred blocker lanes are named explicitly
- Acceptance: later execution does not need to guess whether blocker repair is
  included
- Failure meaning: the topic invites hidden path, tooling, or output-surface changes

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
- which runtime/tooling or downstream output blockers were intentionally deferred
- that confirmed-blocker status remained evidence context rather than being erased

- Actor: later implementer
- Condition: the move work finishes
- Observable: a topic-local migration report exists
- Acceptance: the resulting state is inspectable without hidden chat context
- Failure meaning: later agents cannot distinguish completed copy work from
  deferred blocker work

## Locked Decisions

- This is a bounded canonical-copy topic, not an active-path cutover topic.
- The candidate remains a confirmed runtime/tooling blocker for future path and
  output-surface transition work.
- The topic is allowed to create `skills/python-project-init-greenfield/`.
- The topic is not allowed to rewrite the `.github/skills/` deployment model,
  provenance file destination, Copilot placeholder destination, or acceptance
  CLI contract.
- The canonical copy must include both references, not only `SKILL.md` and examples.

## Non-goals

- Do not switch the active skill execution or output path to
  `skills/python-project-init-greenfield/`.
- Do not modify greenfield-init behavior, blueprint parsing semantics, or
  acceptance criteria handling in this topic.
- Do not rewrite downstream `.github/skills/` deployment, provenance, or
  Copilot-instructions outputs.
- Do not update `.codex/skills` mapping, `README.md`, `VERSION`, or release metadata.
- Do not widen into `sense-env-scaffold`, `python-project-retrofit`, or
  `copilot-instructions-init`.

## Resolved Contradictions

### C1 — canonical copy vs transition-era output model

- Conflict: creating a canonical `skills/` copy can look like permission to
  change where greenfield init writes installed skills and governance files
- Resolution: this topic creates the canonical copy only; transition-era
  `.github/...` output behavior remains unchanged

### C2 — bounded child topic vs blocker-repair topic

- Conflict: the candidate clearly exposes `.github/...` and acceptance-path
  coupling that could tempt this topic to absorb broader repair
- Resolution: preserve blocker status and defer repair to separate future topics

## Explicit Assumptions

- A1: the current `.github/skills/python-project-init-greenfield/` surface is
  the only live transition-era contract during this topic
- A2: creating a canonical copy in `skills/` is still useful even when active
  behavior remains on `.github/skills/`
- A3: runtime/tooling and downstream output transition work will require
  separate later topics
- A4: work for this child topic should also happen in a dedicated worktree, not
  on repo-root `dev`
