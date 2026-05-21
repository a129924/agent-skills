# codex-low-risk-skill-move requirements baseline

Status: LOCKED
Topic: `codex-low-risk-skill-move`
Base branch: `dev`

## Problem statement

After PR #85, the repository now has a repo-visible baseline that separates:

- move-to-`skills/` status
- Codex readability through `.codex/skills/`
- same-name dual-surface backlog

What is still missing is a bounded implementation topic that converts the first
truly low-risk candidates from `not-moved + readable` into `moved + readable`
without reopening same-name divergence, runtime/tooling blocker, or repo-wide
active-path cutover work.

## Goal

Produce one bounded low-risk move topic that:

- creates `skills/git-commit-convention/`
- creates `skills/git-branch-naming/`
- preserves `.github/skills/` as the transition-era compatibility surface
- keeps `.codex/skills` readable for both candidates
- records the move result in a repo-visible migration artifact

## Frozen candidate set

Only these two candidates are in scope:

- `.github/skills/git-commit-convention/`
- `.github/skills/git-branch-naming/`

No third candidate may be absorbed into this topic.

## Actors

- Human decision-maker
- Planning actor
- Creator / implementer
- Independent topic-plan reviewer

## Measurable requirements

| ID | Requirement | Observable result | Pass rule |
| --- | --- | --- | --- |
| R1 | The topic stays inside the two locked candidates | `skills/git-commit-convention/` and `skills/git-branch-naming/` are the only new target-architecture skill folders planned for creation | No same-name, medium-residue, high-residue, or blocker-bearing candidate is added |
| R2 | The move is recorded separately from active-path cutover | The plan and final report state that `skills/` gains canonical target copies while `.github/skills/` remains the transition-era active compatibility surface | No artifact claims repo-wide cutover or `.github/skills/` retirement |
| R3 | Codex readability remains intact after the move | `.codex/skills` mapping for both candidates still resolves to the intended upstream source after branch work | Neither candidate becomes `not-readable` or `stale-projection` |
| R4 | No higher-risk lane is silently absorbed | Same-name pass backlog, medium residue candidates, high residue candidates, and runtime/tooling blockers remain untouched | No unlisted skill path is edited |
| R5 | The topic leaves repo-visible migration evidence | A migration report exists and states candidate verdict, move result, readability result, and deferred follow-up boundaries | Another agent can tell exactly what moved and what remained deferred |

## Locked decisions

- This is an implementation branch, not an inventory-only branch.
- `git-commit-convention` and `git-branch-naming` are the only allowed move
  candidates.
- The branch may create `skills/` versions for those two skills.
- `.github/skills/` remains the transition-era active compatibility surface in
  this topic; this branch does not rewrite repo-wide current-path governance.
- `.codex/skills` may receive only minimal consistency updates required to keep
  mappings readable and provenance-backed.
- README / VERSION / tag handling is deferred to post-merge release workflow,
  not branch-local implementation.

## Non-goals

- same-name divergence resolution
- creator / reviewer / template path-transition redesign
- `git-post-merge-workflow` redesign
- runtime/tooling blocker repair
- repo-wide active authored/reviewed workflow cutover away from
  `.github/skills/`
- second-wave `.codex/skills` expansion

## Assumptions and blockers

- `docs/migration/codex-readability-baseline.md` is the authoritative baseline
  for low-risk candidate selection.
- The current low-residue evidence remains valid:
  - `docs/migration/codex-migration-copilot-residue-low-report.md`
- The two candidate skills do not require executable-path or generator-coupled
  repair before being copied into `skills/`.
- If implementing the move would require changing unlisted runtime/tooling or
  same-name surfaces, stop and re-plan instead of widening scope.
