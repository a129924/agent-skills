# codex-migration-copilot-residue-high requirements baseline

Status: FROZEN-FOR-IMPLEMENTATION
Topic: `codex-migration-copilot-residue-high`
Base branch: `feat/andrew/codex-skills-spec-worktree`

## Problem statement

The repository needs a branch-local path for skills that remain migratable in
principle but still have high Copilot residue through strong platform, path, or
workflow coupling.

## Goal

Freeze the high-residue baseline so that branch-local work can separate
redesign-worthy skills from skills that should be reclassified as
Copilot-specific or blocker-driven follow-up.

This branch is report-first and classification-only. It does not authorize
branch-local modification of the candidate skill content.

## Candidate skill set

The high-residue candidate set is frozen to:

- `.github/skills/git-post-merge-workflow/`

## Actors

- Human decision-maker
- Planning / analysis agent
- Implement Agent for this branch
- Reviewer

## Measurable requirements

| ID | Requirement | Observable result | Pass rule |
| --- | --- | --- | --- |
| R1 | Every candidate has a high-residue rationale | The report names the strong coupling that prevents easier migration | No high-residue verdict is left vague |
| R2 | Branch output separates redesign from no-migrate cases | Each skill gets `redesign`, `defer`, or `reclassify` style next-step guidance | Another agent can continue without rediscovery |
| R3 | Runtime/tooling blockers remain visible | Blocker interactions are flagged even if the skill stays in this branch for analysis | No blocker-bearing dependency is hidden |
| R4 | Copilot-specific skills are redirected when necessary | Skills that exist mainly for Copilot are not forced into redesign by default | High-residue branch stays analytically honest |
| R5 | Report-only execution stays explicit | The branch produces classification and redesign-boundary output without editing the candidate skill | Implement execution mode is not ambiguous |

## Classification baseline

Skills in this topic:

- are not direct, low, or medium residue
- still appear potentially portable after significant redesign
- may depend on current `.github/skills/` semantics or Copilot-era workflow
- must not be silently promoted if they are actually Copilot-specific only

If a candidate is found to be blocker-driven or Copilot-specific-only, it must
leave this branch and be reclassified.

Reclassification triggers are frozen to the following repo-visible conditions:

- the candidate requires runtime/tooling blocker repair to remain viable
- the candidate's remaining value is reference-only or Copilot-specific-only
- a credible redesign path cannot be described without changing repo-wide
  cutover semantics, widening the candidate set, or editing artifacts outside
  the locked report path
- the branch-local files cannot describe a bounded redesign objective from the
  current repo-visible evidence set alone

## Non-goals

- branch-local modification of `.github/skills/git-post-merge-workflow/`
- blocker repair itself
- Copilot-specific-only migration
- repo-wide cutover

## Assumptions and blockers

- Existing migration documents remain the primary evidence set.
- The Implement Agent may read `.github/skills/git-post-merge-workflow/` for
  classification and report-writing, but must not modify that skill in this
  branch.
- If a skill is actually reference-only or non-portable, reclassify it out of
  this branch instead of forcing a redesign plan.
