# codex-migration-direct-move requirements baseline

Status: LOCKED
Topic: `codex-migration-direct-move`
Base branch: `feat/andrew/codex-skills-spec-worktree`

## Problem statement

The repository needs a branch-local verification path for skills that already
have target-architecture promotion results and may already satisfy direct-use
or direct-projection expectations from the migration base branch.

This topic exists to verify whether additional branch-local migration work is
actually required, rather than assuming that the promoted planning skills still
need content-moving implementation.

## Goal

Produce a branch-local, reviewable baseline that identifies which skills belong
to the direct-move verification set and what evidence is required before the
branch can conclude `already satisfied`, `no move required`, or
`needs follow-up`.

## Candidate skill set

The direct-move verification set is frozen to:

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
| R1 | Every in-scope skill has an explicit verification verdict | The report lists `already satisfied`, `no move required`, or `needs follow-up` for each candidate skill | No candidate is left implicit |
| R2 | The verification is evidence-based | Each verdict cites source-path, dependency type, and blocker status | No verdict relies on intuition-only wording |
| R3 | Report-only execution excludes branch-local skill migration | The branch verifies and reports instead of editing the four promoted skills | No promoted planning skill is silently rewritten in this branch |
| R4 | The branch produces a reusable report | A branch-local migration report exists with skill, verdict, why, and follow-up fields | Another agent can continue from the report without rediscovery |
| R5 | Follow-up cases are surfaced explicitly | Any skill that is not already satisfied is marked `needs follow-up` with a reason | No unresolved gap is hidden behind a false direct-move claim |

## Classification baseline

Skills in this topic must be evaluated against all of the following:

- fit class `A. direct move`
- are already promoted into `skills/`
- may still remain `tracked-dependency` in runway evidence without requiring new
  branch-local content migration
- must be verified against current base-branch projection and migration
  evidence before any move is declared necessary

If a candidate is not already satisfied, it stays in the report as
`needs follow-up`; it is not migrated in this branch.

## Non-goals

- medium/high residue remediation
- Copilot-specific reference extraction
- runtime/tooling blocker repair
- repo-wide cutover
- direct editing of the four promoted planning skills unless the handoff
  contract itself is proven stale

## Assumptions and blockers

- The source-of-truth inputs come from existing migration artifacts, especially
  `docs/migration/platform-coupling-inventory.md`,
  `docs/migration/migration-runway-checklist.md`, and
  `docs/migration/codex-skills-spec-worktree.md`.
- The branch may conclude that no additional move is required for one or more
  candidates.
- If the verification evidence conflicts with the branch-local handoff
  contract, mark the branch as blocked and return to planning instead of
  editing the promoted planning skills.
