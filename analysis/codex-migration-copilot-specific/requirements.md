# codex-migration-copilot-specific requirements baseline

Status: DRAFT
Topic: `codex-migration-copilot-specific`
Base branch: `feat/andrew/codex-skills-spec-worktree`

## Problem statement

The repository needs a branch-local path for skills that primarily serve
Copilot-era behavior and may not be appropriate to migrate directly into the
Codex-oriented skill surface. Current migration evidence also identifies the
frozen candidate in this topic as a confirmed runtime/tooling blocker, so this
branch must preserve blocker visibility instead of treating the candidate as a
normal migration target.

## Goal

Freeze the Copilot-specific baseline and separate these skills into
`reference-only` versus `do-not-migrate` conclusions before any migration work
starts, while recording confirmed-blocker status as part of the branch-local
report.

## Candidate skill set

The Copilot-specific candidate set is frozen to:

- `.github/skills/copilot-instructions-init/`

## Actors

- Human decision-maker
- Planning / analysis agent
- Implement Agent for this branch
- Reviewer

## Measurable requirements

| ID | Requirement | Observable result | Pass rule |
| --- | --- | --- | --- |
| R1 | Every candidate gets a Copilot-specific verdict | The report marks `reference-only` or `do-not-migrate` for each skill | No candidate is left ambiguous |
| R2 | Portable ideas are separated from platform lock-in | The report names what may be reused conceptually and what must not migrate | Another agent can extract references safely |
| R3 | No forced migration happens in this branch | This topic does not treat Copilot-specific skills as mandatory migration targets | The branch preserves the option to reject migration |
| R4 | Blocker status stays visible | The report records whether the candidate is a confirmed blocker and what that means for follow-up | Runtime/tooling dependency is not hidden behind a generic Copilot-only label |
| R5 | Follow-up work is explicit | Each candidate has a concrete next action or no-action decision | Human review can make portfolio decisions quickly |

## Classification baseline

Skills in this topic:

- primarily serve Copilot-era platform behavior
- are not good direct migration candidates
- may also be confirmed runtime/tooling blockers
- must be split into `C1. reference-only` or `C2. do-not-migrate`

If a candidate turns out to be portable after all, it must leave this branch
and be reclassified.

## Non-goals

- direct migration implementation
- runtime/tooling blocker repair
- repo-wide cutover

## Assumptions and blockers

- Existing migration documents remain the primary evidence set.
- `.github/skills/copilot-instructions-init/` is currently classified by
  repo-visible migration evidence as a `confirmed-blocker` runtime/tooling
  surface.
- This branch may document blocker status and follow-up expectations, but it
  must not perform blocker repair.
- If a skill turns out to be portable after all, it should be reclassified into
  another branch rather than forced to stay Copilot-specific.
