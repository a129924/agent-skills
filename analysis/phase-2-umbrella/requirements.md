# Requirements: phase-2-umbrella

## Status

- **Status**: frozen for technical translation
- **Topic**: `phase-2-umbrella`
- **Date**: 2026-06-05
- **Scope**: governance / coordination baseline for Phase 2 slice planning

## Problem Statement

Phase 1 established that `skills/` is the canonical convergence target and
that `.github/skills/` and `.codex/skills/` are not authority source trees.
However, the repository still needs one repo-visible Phase 2 coordination
baseline that:

1. freezes the allowed execution slices and their order,
2. records that Phase 2 is not a fourth implementation line,
3. preserves the frozen safe canonical batch list,
4. states that each later slice needs its own plan, review, human check, and
   PR,
5. and keeps `docs/status.md` optional rather than required for success.

Without that umbrella baseline, later slice planning would have to infer scope
and routing from chat context or from Phase 1 reports alone.

## Evidence Read

The baseline uses the following repo-visible evidence:

- `AGENTS.md`
- `docs/repo-positioning.md`
- `plan/agent-handoff-workflow.md`
- `plan/topic-plan-contract.md`
- `docs/agent-skills-convergence/phase-1/00-summary.md`
- `docs/agent-skills-convergence/phase-1/06-convergence-candidates.md`
- `docs/agent-skills-convergence/phase-1/07-phase-2-inputs.md`
- `plan/plan-contract-authority-alignment/plan-contract-authority-alignment.summary.md`
- `.github/prompts/create-analysis.prompt.md`
- `.github/prompts/create-agent-plan.prompt.md`

## Actors

| Actor | Role | What must be true after this topic |
| --- | --- | --- |
| Repository maintainer | Owns Phase 2 coordination baseline | Can point to one umbrella planning topic that freezes slice order and boundaries without treating it as implementation approval |
| Planning actor | Authors later slice plans | Can create a later slice topic without guessing slice order, safe batch membership, or whether umbrella execution already covers implementation |
| Reviewer | Reviews later slice plans and drafts | Can verify that each slice has its own bounded plan/review/human-check/PR rather than relying on umbrella prose |
| Main Agent | Handles later publish / PR routing | Can treat slice PR order as serialized and avoid parallel Phase 2 execution |
| Human operator | Approves later slice progression | Can see what is deferred to later slice topics and what the umbrella baseline does not authorize |

## Frozen Requirements

| ID | Requirement | Acceptance signal |
| --- | --- | --- |
| R1 | This topic must create a repo-visible coordination baseline for Phase 2. | `plan/phase-2-umbrella/phase-2-umbrella.plan.md` exists and is reviewable as a governance topic. |
| R2 | The umbrella topic must remain governance / coordination only, not a fourth implementation line. | The topic plan explicitly forbids direct skill convergence, projection materialization, runtime adaptation, or generic implementation under umbrella scope. |
| R3 | The canonical convergence target must remain `skills/`. | The topic plan preserves `skills/` as canonical and states that `.github/skills/` and `.codex/skills/` are non-authority surfaces. |
| R4 | Later Phase 2 execution slices and their order must be explicit. | The topic plan names `phase-2-safe-canonical-batch`, `phase-2-merge-into-skills-batch`, and `phase-2-planning-spine-exceptions`, and makes the safe canonical batch first. |
| R5 | The safe canonical batch skill list must be frozen exactly. | The topic plan lists the nine frozen safe canonical batch skills exactly as provided. |
| R6 | Slice PR order must be strictly serialized. | The topic plan and step artifact both state that later slice PRs must not proceed in parallel. |
| R7 | Each later slice must require its own plan / review / human-check / PR loop. | The umbrella plan states that later slices branch from this baseline but do not inherit implementation approval or PR completion from it. |
| R8 | `docs/status.md` must stay optional only. | The topic plan treats `docs/status.md` as a cross-topic overview only and never as a success prerequisite or execution truth source. |
| R9 | Artifact-role semantics must stay explicit. | The topic plan states that `plan/<topic>/<topic>.summary.md` is topic close / handoff truth, `plan/<topic>/<topic>.step.md` is topic progression truth, and `docs/status.md` is overview only. |
| R10 | The umbrella topic must stay inside the declared write set. | No file outside `analysis/phase-2-umbrella/*` and `plan/phase-2-umbrella/*` is modified by this planning baseline. |

## Resolved Contradictions

### C1 - Phase 2 needs coordination, but coordination must not impersonate implementation

- Conflict: the repository needs a Phase 2 umbrella baseline, but writing one
  could be mistaken for approval to start a fourth implementation line.
- Resolution: freeze the umbrella topic as a coordination-only planning layer
  that authorizes later slice planning only.

### C2 - Phase 1 recommends Phase 2 actions, but those recommendations do not create direct execution authority

- Conflict: Phase 1 reports identify safe and unsafe convergence buckets, but a
  later slice still needs its own bounded execution contract.
- Resolution: the umbrella baseline carries forward Phase 1 routing facts while
  requiring each slice to create its own plan, review, human-check, and PR.

### C3 - Cross-topic visibility can help, but `docs/status.md` must not become source of truth

- Conflict: a status overview may be useful for humans, but it must not replace
  topic-local progression or close semantics.
- Resolution: keep `docs/status.md` optional only and preserve topic-local
  `step.md` and `summary.md` roles.

## Explicit Assumptions

- A1: the Phase 1 evidence under `docs/agent-skills-convergence/phase-1/`
  remains valid as planning input and is not being reopened in this topic.
- A2: `plan/plan-contract-authority-alignment/plan-contract-authority-alignment.summary.md`
  is sufficient evidence that repo-level plan-contract authority work is not a
  blocker for drafting this umbrella baseline.
- A3: later slice topics may add their own review-log or summary artifacts when
  their workflow conditions require them, without changing the umbrella topic's
  write set.

## Non-goals

- Do not modify `skills/**`.
- Do not modify `.github/skills/**`.
- Do not modify `.codex/skills/**`.
- Do not modify `.github/agents/**`.
- Do not modify `.codex/agents/**`.
- Do not start safe canonical convergence implementation.
- Do not start merge-into-skills implementation.
- Do not start planning-spine exception implementation.
- Do not materialize `.codex/skills/` projections.
- Do not perform runtime adaptation.
- Do not require `docs/status.md` for umbrella success.

## Extreme-Boundary Checks

| Boundary | Requirement result |
| --- | --- |
| A reader sees `phase-2-umbrella` without Phase 1 chat context | The umbrella plan must still show exact slice names, exact safe batch list, and serialized PR order |
| A later planner wants to open two slice PRs in parallel | The umbrella plan must still block that and require strict serialization |
| A maintainer wants to use `docs/status.md` as execution truth | The umbrella plan must still state that `docs/status.md` is optional overview only |
| A creator tries to treat umbrella scope as implementation scope | The umbrella plan must still force a stop and separate slice plan rather than allow direct skill edits |

## Success Signals

This topic is frozen successfully when:

1. the umbrella baseline is repo-visible,
2. later slices and their order are explicit,
3. safe canonical batch membership is frozen exactly,
4. implementation is clearly deferred to later slice topics,
5. artifact-role truth semantics are explicit,
6. and no downstream actor has to guess whether umbrella scope itself permits
   skill changes.
