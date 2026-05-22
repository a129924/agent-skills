# worktree-manager-move requirements baseline

Status: LOCKED
Topic: `worktree-manager-move`
Base branch: `dev`
Target branch: `feat/andrew/worktree-manager-move`
Risk level: `medium`

## Problem statement

`worktree-manager` is currently available only from the transition-era
`.github/skills/` surface even though it is readable, portable enough for
target-architecture promotion, and useful for future multi-worktree migration
execution.

What is missing is one bounded move topic that creates a `skills/` copy for
`worktree-manager` without widening into:

- repo-wide active-path cutover
- runtime/tooling blocker repair
- unrelated contract-surface batch work
- README / VERSION / projection metadata reconciliation

## Goal

Produce one bounded move topic that:

- creates `skills/worktree-manager/`
- preserves `.github/skills/worktree-manager/` as the transition-era
  compatibility surface
- records the move boundary separately from any later projection switch or
  governance update

## Frozen candidate set

Only this candidate is in scope:

- `.github/skills/worktree-manager/`

No second candidate may be absorbed into this topic.

## Actors

- Human decision-maker
- Planning actor
- Creator / implementer
- Independent topic-plan reviewer

## Measurable requirements

| ID | Requirement | Observable result | Pass rule |
| --- | --- | --- | --- |
| R1 | The topic stays inside the locked candidate | `skills/worktree-manager/` is the only new target-architecture folder created | No unrelated skill path is added or edited |
| R2 | The move is recorded separately from active-path cutover | The plan and final report state that `skills/` gains a target-architecture copy while `.github/skills/` remains the current active compatibility surface | No artifact claims repo-wide cutover or retirement of `.github/skills/` |
| R3 | The move does not widen into runtime/tooling blocker repair | Known runtime/tooling blocker surfaces remain untouched | No edit lands in `sense-env-scaffold`, `plan-step-tracker`, `python-project-init-greenfield`, `python-project-retrofit`, or `copilot-instructions-init` |
| R4 | Shared migration/governance surfaces remain stable during the move | Bootstrap and implementation artifacts stay topic-local | No edit lands in `AGENTS.md`, `docs/repo-positioning.md`, `README.md`, `VERSION`, `.codex/*`, or checklist-wide migration trackers |
| R5 | The topic leaves repo-visible migration evidence | A migration report exists and states candidate verdict, move result, preserved compatibility boundary, and deferred follow-up lanes | Another agent can tell exactly what moved and what stayed deferred |

## Locked decisions

- This is an implementation topic, not an inventory-only topic.
- Only `worktree-manager` is an allowed move target.
- The branch may create a `skills/` copy for that candidate.
- `.github/skills/` remains the transition-era active compatibility surface in
  this topic.
- `.codex/skills` mapping and provenance updates are deferred.
- README / VERSION / release-tag handling is deferred to later release work.

## Non-goals

- runtime/tooling blocker repair
- repo-wide active authored/reviewed workflow cutover away from
  `.github/skills/`
- creator / reviewer / template contract-surface batch work
- planning-spine dependency rewrites
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
