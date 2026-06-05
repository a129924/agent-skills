# Requirements: phase-2-safe-canonical-batch

## Status

- **Status**: frozen for technical translation
- **Topic**: `phase-2-safe-canonical-batch`
- **Date**: 2026-06-05
- **Scope**: planning baseline for the first Phase 2 execution slice

## Problem Statement

The umbrella baseline is approved and names `phase-2-safe-canonical-batch` as
the first execution slice after `phase-2-umbrella`. The repository now needs a
repo-visible planning baseline for that first slice so later execution can
start from one bounded topic plan rather than infer scope from Phase 1 and
umbrella artifacts alone.

This slice is not implementation in the current turn. The missing outcome is a
planning baseline that:

1. freezes the exact nine-skill safe canonical batch,
2. states that this topic still sits at planning stage only,
3. preserves `skills/` as canonical and `.github/skills/` plus
   `.codex/skills/` as non-authority surfaces,
4. keeps later slices out of scope,
5. and records where later implementation may need human review if exact write
   scope would otherwise require guessing.

## Evidence Read

The baseline uses the following repo-visible evidence:

- `AGENTS.md`
- `docs/repo-positioning.md`
- `plan/agent-handoff-workflow.md`
- `plan/topic-plan-contract.md`
- `plan/phase-2-umbrella/phase-2-umbrella.plan.md`
- `plan/phase-2-umbrella/phase-2-umbrella.step.md`
- `docs/agent-skills-convergence/phase-1/00-summary.md`
- `docs/agent-skills-convergence/phase-1/06-convergence-candidates.md`
- `docs/agent-skills-convergence/phase-1/07-phase-2-inputs.md`
- `.github/prompts/create-analysis.prompt.md`
- `.github/prompts/create-agent-plan.prompt.md`

## Actors

| Actor | Role | What must be true after this topic |
| --- | --- | --- |
| Repository maintainer | Owns first-slice planning baseline | Can point to one bounded plan for the first execution slice without treating planning completion as implementation approval |
| Planning actor | Authors the first slice plan | Can define exact safe-batch scope and out-of-scope boundaries without reopening umbrella decisions |
| Reviewer | Reviews the first slice plan | Can validate that the topic stays inside the frozen safe list and does not widen into merge, projection, runtime, or copilot-only work |
| Creator | Later executes bounded convergence work only after planning and review gates pass | Can see that the safe list is exact and that any guessed write scope is blocked pending human review |
| Human operator | Approves execution after planning stage | Can see where Phase 1 low-risk evidence is sufficient and where later implementation details still require explicit confirmation |

## Frozen Requirements

| ID | Requirement | Acceptance signal |
| --- | --- | --- |
| R1 | This topic must create a repo-visible planning baseline for the first Phase 2 execution slice. | `plan/phase-2-safe-canonical-batch/phase-2-safe-canonical-batch.plan.md` exists and is reviewable. |
| R2 | This current turn must remain planning only. | The topic plan explicitly states that no canonical convergence implementation starts in this turn. |
| R3 | The topic must branch from the approved umbrella baseline. | The topic plan records parent baseline `feat/andrew/phase-2-umbrella` at `9d1d784` as upstream planning authority input. |
| R4 | The safe canonical batch list must be frozen exactly. | The topic plan lists exactly the nine provided skills with no additions or removals. |
| R5 | `skills/` must remain the canonical target and `.github/skills/` / `.codex/skills/` must remain non-authority surfaces. | The topic plan records the canonical and non-authority model explicitly. |
| R6 | Later implementation under this topic must stay bounded to the frozen safe list only. | The topic plan blocks any skill work outside the nine listed skills. |
| R7 | Later slices remain out of scope. | The topic plan explicitly excludes `phase-2-merge-into-skills-batch` and `phase-2-planning-spine-exceptions`. |
| R8 | Projection materialization, runtime adaptation, planning-spine exception handling, and copilot-only work remain out of scope. | The topic plan explicitly excludes `.codex/skills/` materialization, runtime adaptation, planning-spine exception handling, and `copilot-instructions-init` style work. |
| R9 | `docs/status.md` remains optional only. | The topic plan states that `docs/status.md` is not required for execution truth or topic success. |
| R10 | If later implementation write scope would require guessing beyond Phase 1 + umbrella evidence, the plan must not invent it. | The topic plan marks the affected item `human_review_required` instead of fabricating an exact write scope. |
| R11 | No file outside the declared write set may be modified in this planning turn. | Only the four allowed analysis / plan files change. |

## Resolved Contradictions

### C1 - This is the first execution slice, but the current turn is not execution

- Conflict: the topic is the first execution slice after umbrella, but the user
  explicitly asked for planning workflow only.
- Resolution: freeze the slice as planning-stage only in the current workflow
  and defer any actual convergence edits to later execution under this topic.

### C2 - Phase 1 says these skills are low risk, but low risk does not define exact write scope by itself

- Conflict: Phase 1 evidence supports bounded canonical convergence planning,
  but it does not necessarily define every exact implementation path.
- Resolution: allow the plan to assume no semantic-drift reconciliation is
  needed, while routing any guessed implementation write-scope detail to
  `human_review_required`.

### C3 - `.codex/skills/` may later need projection handling, but projection stays out of scope here

- Conflict: some safe skills could later have optional projection follow-up,
  but this topic must not widen into projection work.
- Resolution: keep projection materialization out of scope and treat
  `.codex/skills/` as a non-authority partial projection surface only.

## Explicit Assumptions

- A1: the approved umbrella baseline under `feat/andrew/phase-2-umbrella` at
  commit `9d1d784` is the immediate parent planning authority for this topic.
- A2: the nine safe-batch skills remain low-risk canonical candidates exactly
  as recorded in Phase 1 and umbrella evidence.
- A3: because Phase 1 classified these nine skills as low risk, no
  semantic-drift reconciliation work is assumed inside this topic unless later
  evidence contradicts that assumption.
- A4: exact implementation write scope for later execution is not fully
  derivable from the current evidence set alone and must trigger
  `human_review_required` when guessing would otherwise be required.

## Non-goals

- Do not modify `skills/**`.
- Do not modify `.github/skills/**`.
- Do not modify `.codex/skills/**`.
- Do not modify `.github/agents/**`.
- Do not modify `.codex/agents/**`.
- Do not modify shared contract files.
- Do not modify umbrella topic artifacts.
- Do not begin canonical convergence implementation in this turn.
- Do not handle `phase-2-merge-into-skills-batch`.
- Do not handle `phase-2-planning-spine-exceptions`.
- Do not perform projection materialization.
- Do not perform runtime adaptation.
- Do not handle copilot-only work.

## Extreme-Boundary Checks

| Boundary | Requirement result |
| --- | --- |
| A planner reads only umbrella + Phase 1 reports | The first-slice plan must still show the exact safe list and first-slice boundaries |
| A creator tries to include a tenth skill because it looks similar | The plan must still block anything outside the frozen nine-skill list |
| A maintainer wants to plan `.codex/skills/` updates here | The plan must still state that projection materialization remains out of scope |
| A later executor cannot infer exact implementation write scope from current evidence | The plan must still route that item to `human_review_required` instead of guessing |

## Success Signals

This topic is frozen successfully when:

1. the first-slice planning baseline is repo-visible,
2. the exact nine-skill safe list is frozen,
3. current work is explicitly planning-stage only,
4. later implementation is bounded to the safe list only,
5. later slices and non-safe work remain excluded,
6. and guessed implementation write scope is surfaced as
   `human_review_required` rather than invented.
