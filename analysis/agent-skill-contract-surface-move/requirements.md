# agent-skill-contract-surface-move requirements baseline

Status: LOCKED
Topic: `agent-skill-contract-surface-move`
Base branch: `dev`
Target branch: `feat/andrew/agent-skill-contract-surface-move`
Risk level: `medium`

## Problem statement

The repository has already completed bounded low-risk promotion for selected
skills, but the next move candidates with meaningful migration value are still
stuck at contract-surface level under `.github/skills/`.

What is missing is one bounded move topic that creates target-architecture
copies for the three authoring-contract surfaces without widening into:

- repo-wide active-path cutover
- runtime/tooling blocker repair
- planning-spine edits
- README / VERSION / projection metadata reconciliation

## Goal

Produce one bounded move topic that:

- creates `skills/agent-skill-creator/`
- creates `skills/agent-skill-reviewer/`
- creates `skills/agent-skill-template/`
- preserves `.github/skills/` as the transition-era compatibility surface
- records the move boundary separately from any later cutover or projection
  switch work

## Frozen candidate set

Only these three candidates are in scope:

- `.github/skills/agent-skill-creator/`
- `.github/skills/agent-skill-reviewer/`
- `.github/skills/agent-skill-template/`

No fourth candidate may be absorbed into this topic.

## Actors

- Human decision-maker
- Planning actor
- Creator / implementer
- Independent topic-plan reviewer

## Measurable requirements

| ID | Requirement | Observable result | Pass rule |
| --- | --- | --- | --- |
| R1 | The topic stays inside the three locked candidates | `skills/agent-skill-creator/`, `skills/agent-skill-reviewer/`, and `skills/agent-skill-template/` are the only new target-architecture folders created | No unrelated skill path is added or edited |
| R2 | The move is recorded separately from active-path cutover | The plan and final report state that `skills/` gains target-architecture copies while `.github/skills/` remains the current active compatibility surface | No artifact claims repo-wide cutover or retirement of `.github/skills/` |
| R3 | Contract-surface move does not widen into tooling repair | Runtime/tooling blocker surfaces remain untouched | No edit lands in `sense-env-scaffold`, `plan-step-tracker`, `python-project-init-greenfield`, `python-project-retrofit`, or `copilot-instructions-init` |
| R4 | Shared migration/governance surfaces remain stable during the move | Bootstrap and implementation artifacts stay topic-local | No edit lands in `AGENTS.md`, `docs/repo-positioning.md`, `README.md`, `VERSION`, `.codex/*`, or checklist-wide migration trackers |
| R5 | The topic leaves repo-visible migration evidence | A migration report exists and states candidate set, move result, preserved compatibility boundary, and deferred follow-up lanes | Another agent can tell exactly what moved and what stayed deferred |

## Locked decisions

- This is an implementation topic, not an inventory-only topic.
- Only the three authoring-contract candidates are allowed move targets.
- The branch may create `skills/` copies for those three candidates.
- `.github/skills/` remains the transition-era active compatibility surface in
  this topic.
- `.codex/skills` mapping and provenance updates are deferred.
- README / VERSION / release-tag handling is deferred to later release work.

## Non-goals

- runtime/tooling blocker repair
- repo-wide active authored/reviewed workflow cutover away from
  `.github/skills/`
- planning-spine dependency rewrites
- same-name divergence resolution for already-promoted skills
- `.codex/skills` projection switching
- migration-runway checklist rewrites

## Assumptions and blockers

- `docs/migration/migration-runway-checklist.md` remains the authoritative
  runway snapshot.
- The current medium-residue evidence remains valid:
  - `docs/migration/codex-migration-copilot-residue-medium-report.md`
- No local or remote `feat/andrew/copilot-to-codex-migration` base branch is
  available in this repository snapshot, so `dev` is the only verifiable target
  branch for bootstrap.
- If implementing the move requires editing shared migration/governance files or
  runtime/tooling blocker surfaces, stop and re-plan instead of widening scope.
