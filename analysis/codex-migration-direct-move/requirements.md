# codex-migration-direct-move requirements baseline

Status: DRAFT
Topic: `codex-migration-direct-move`
Base branch: `feat/andrew/codex-skills-spec-worktree`

## Problem statement

The repository needs a branch-local migration path for skills that can move
into the Codex-oriented validation surface with minimal or no Copilot-specific
remediation.

This topic exists to freeze the direct-move classification baseline before
implementation work starts.

## Goal

Produce a branch-local, reviewable baseline that identifies which skills belong
to the direct-move class and what evidence is required before those skills are
actually migrated.

## Candidate skill set

The direct-move candidate set is frozen to:

- `skills/business-intent-alignment/`
- `skills/business-to-technical-translation/`
- `skills/plan-creator/`
- `skills/plan-reviewer/`

The corresponding transition-era comparison inputs are:

- `.github/skills/business-intent-alignment/`
- `.github/skills/business-to-technical-translation/`
- `.github/skills/plan-creator/`
- `.github/skills/plan-reviewer/`

## Actors

- Human decision-maker
- Planning / analysis agent
- Implement Agent for this branch
- Reviewer

## Measurable requirements

| ID | Requirement | Observable result | Pass rule |
| --- | --- | --- | --- |
| R1 | Every in-scope skill has an explicit direct-move verdict | The report lists `move` or `do-not-move` for each candidate skill | No candidate is left implicit |
| R2 | Direct-move classification is evidence-based | Each verdict cites source-path, dependency type, and blocker status | No verdict relies on intuition-only wording |
| R3 | Direct-move scope excludes runtime/tooling blockers | Blocker-tagged skills are rejected or deferred with a reason | No confirmed blocker is silently promoted into this branch |
| R4 | The branch produces a reusable report | A branch-local migration report exists with skill, verdict, why, and follow-up fields | Another agent can continue from the report without rediscovery |
| R5 | Migration does not begin before the candidate set is frozen | The branch plan names the classification gate before implementation | No skill content is changed before classification is explicit |

## Classification baseline

Skills in this topic must satisfy all of the following before implementation:

- fit class `A. direct move`
- no `confirmed-blocker` status
- no high Copilot-residue dependency
- no mandatory Copilot-only role semantics
- no runtime CLI, generator, or acceptance-handoff dependency that would force
  a separate transition topic

If a candidate fails any of the above checks, it leaves this branch and must be
reclassified instead of being implemented here.

## Non-goals

- medium/high residue remediation
- Copilot-specific reference extraction
- runtime/tooling blocker repair
- repo-wide cutover

## Assumptions and blockers

- The source-of-truth inputs come from existing migration artifacts, especially
  `docs/migration/platform-coupling-inventory.md`,
  `docs/migration/migration-runway-checklist.md`, and
  `docs/migration/codex-skills-spec-worktree.md`.
- If the candidate set cannot be frozen without revisiting category boundaries,
  mark the branch as blocked and return to planning instead of implementing.
