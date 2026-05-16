# codex-migration-copilot-residue-low requirements baseline

Status: DRAFT
Topic: `codex-migration-copilot-residue-low`
Base branch: `feat/andrew/codex-skills-spec-worktree`

## Problem statement

The repository needs a branch-local path for skills that are migratable but
still contain low-level Copilot residue such as wording, examples, or minor
path assumptions.

## Goal

Freeze the low-residue classification baseline and define what qualifies as
light remediation before implementation begins.

## Actors

- Human decision-maker
- Planning / analysis agent
- Implement Agent for this branch
- Reviewer

## Measurable requirements

| ID | Requirement | Observable result | Pass rule |
| --- | --- | --- | --- |
| R1 | Every candidate has a low-residue verdict | The report names why the skill is `low`, not `direct` or `medium` | No skill is accepted without residue rationale |
| R2 | Remediation stays light | Required changes are limited to wording, examples, local path cleanup, or projection notes | No contract rewrite is hidden inside this branch |
| R3 | Blockers remain excluded | Confirmed blockers are deferred or rejected with reasons | No blocker is implemented as low residue |
| R4 | The report is implementation-ready | Each skill has remediation notes and an explicit next action | Another agent can implement without reclassifying first |

## Classification baseline

Skills in this topic:

- are migratable
- still carry light Copilot-specific residue
- do not require creator/reviewer/runtime contract redesign
- do not require blocker repair

## Non-goals

- medium/high residue remediation
- runtime/tooling transition work
- Copilot-specific reference-only extraction
- repo-wide cutover

## Assumptions and blockers

- Existing migration documents remain the primary evidence set.
- If a candidate requires contract or workflow rewrites, reclassify it out of
  this branch instead of widening the branch boundary.
