# codex-migration-copilot-residue-medium requirements baseline

Status: FROZEN
Topic: `codex-migration-copilot-residue-medium`
Base branch: `feat/andrew/codex-skills-spec-worktree`

## Problem statement

The repository needs a branch-local path for skills that are migratable but
still contain medium-level Copilot residue in workflow or contract semantics.

## Goal

Freeze the medium-residue baseline so that implementation can distinguish
bounded contract remediation from work that should be escalated into high
residue or blocker topics.

## Candidate skill set

The medium-residue candidate set is frozen to:

- `.github/skills/agent-skill-creator/`
- `.github/skills/agent-skill-reviewer/`
- `.github/skills/agent-skill-template/`
- `.github/skills/worktree-manager/`

## Actors

- Human decision-maker
- Planning / analysis agent
- Implement Agent for this branch
- Reviewer

## Measurable requirements

| ID | Requirement | Observable result | Pass rule |
| --- | --- | --- | --- |
| R1 | Every candidate has a medium-residue rationale | The report explains which workflow/contract assumptions remain | No skill is classified as medium without named residue |
| R2 | Medium residue excludes executable blockers | The report distinguishes contract residue from runtime/tooling blockers | No blocker is silently treated as medium residue |
| R3 | Branch output defines bounded remediation | Each skill has a finite remediation plan and follow-up path | Another agent can implement without rediscovering scope |
| R4 | High-residue skills are redirected out | Skills with strong platform coupling are marked for another branch | Medium branch does not absorb high-residue scope |

## Classification baseline

Skills in this topic:

- are still migratable
- require workflow or contract remediation
- do not require runtime/tooling blocker repair
- do not require platform-specific semantics to remain intact

If executable path or generator assumptions become mandatory, the skill must
leave this branch and be reclassified.

## Non-goals

- high-residue redesign
- Copilot-specific reference-only extraction
- runtime/tooling transition work
- repo-wide cutover

## Assumptions and blockers

- Existing migration documents remain the primary evidence set.
- If executable path or generator assumptions appear, reclassify the skill into
  a blocker-bearing path instead of widening this branch.
