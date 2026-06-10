# Requirements: phase-2-merge-into-skills-batch

## Status

- **Status**: frozen for technical translation
- **Topic**: `phase-2-merge-into-skills-batch`
- **Date**: 2026-06-10
- **Scope**: planning-only baseline for the merge-required Phase 2 batch

## Problem Statement

The approved umbrella baseline freezes `phase-2-merge-into-skills-batch` as a
later Phase 2 slice after the safe canonical batch. Phase 1 evidence already
shows that this candidate set is not low-risk same-name convergence. Instead,
these skills carry semantic drift, path/alias drift, reference-set drift, or
runtime / projection concerns that make blind collapse unsafe.

The missing outcome for this turn is not merge implementation. The missing
outcome is a repo-visible planning baseline that:

1. freezes the exact merge-batch candidate set,
2. states that current work is planning-only,
3. preserves `skills/` as canonical and `.github/skills/` /
   `.codex/skills/` as non-authority surfaces,
4. records that semantic drift and merge policy discussion are expected rather
   than suppressed,
5. and routes any under-evidenced later merge policy or exact write scope to
   `human_review_required`.

## Evidence Read

The baseline uses the following repo-visible evidence:

- `AGENTS.md`
- `docs/repo-positioning.md`
- `plan/agent-handoff-workflow.md`
- `plan/topic-plan-contract.md`
- `plan/phase-2-umbrella/phase-2-umbrella.plan.md`
- `plan/phase-2-umbrella/phase-2-umbrella.step.md`
- `docs/agent-skills-convergence/phase-1/06-convergence-candidates.md`
- `docs/agent-skills-convergence/phase-1/07-phase-2-inputs.md`
- `docs/agent-skills-convergence/phase-1/04-semantic-drift-report.md`
- `docs/agent-skills-convergence/phase-1/05-runtime-dependency-inventory.md`
- `.github/prompts/create-analysis.prompt.md`
- `.github/prompts/create-agent-plan.prompt.md`

## Actors

| Actor | Role | What must be true after this topic |
| --- | --- | --- |
| Repository maintainer | Owns merge-batch planning baseline | Can point to one bounded planning topic for merge-required candidates without implying merge implementation approval |
| Planning actor | Authors the merge-batch topic plan | Can freeze exact candidates, expected drift discussion, and non-goals without collapsing semantics by assumption |
| Reviewer | Reviews the planning baseline | Can verify that alias/path/behavior drift is surfaced and that unsupported merge policy guesses are blocked |
| Creator | Later executes bounded merge work only after planning and review gates pass | Can see that this topic is merge-required by evidence and that later file-scope ambiguity remains explicit |
| Human operator | Confirms unresolved merge policy and scope decisions | Can see where Phase 1 evidence is sufficient and where later merge behavior still needs explicit choice |

## Frozen Requirements

| ID | Requirement | Acceptance signal |
| --- | --- | --- |
| R1 | This topic must create a repo-visible planning baseline for the merge-required batch. | `plan/phase-2-merge-into-skills-batch/phase-2-merge-into-skills-batch.plan.md` exists and is reviewable. |
| R2 | The current turn must remain planning only. | The topic plan explicitly states that no merge implementation begins in this turn. |
| R3 | The exact merge-batch candidate set must be frozen. | The topic plan lists exactly: `agent-skill-creator`, `agent-skill-template`, `python-blueprint-authoring`, `python-library-architecture`, `python-package-layout`, `python-plan-authoring`, `python-pre-commit`, `python-pyproject-toolconfig`, `python-tdd-test-authoring`, `python-blueprint-review`. |
| R4 | `skills/` must remain canonical and `.github/skills/` / `.codex/skills/` must remain non-authority surfaces. | The topic plan records the canonical / non-authority model explicitly. |
| R5 | `.codex/skills/` must remain a partial projection surface only. | The topic plan records that `.codex/skills/` is not canonical and that projection work is not part of this topic. |
| R6 | Semantic drift, alias drift, and behavior drift must be surfaced, not silently collapsed. | The topic plan explicitly states that merge policy discussion is expected and that semantic / behavior drift cannot be erased by assumption. |
| R7 | Later slices and non-merge work remain out of scope. | The topic plan excludes safe canonical batch, planning-spine exceptions, projection materialization, runtime adaptation, and copilot-only work. |
| R8 | If exact merge policy cannot be derived from evidence, it must be routed to `human_review_required`. | The topic plan names merge-policy ambiguity as `human_review_required` rather than inventing a policy. |
| R9 | If exact later write scope cannot be derived from evidence, it must be routed to `human_review_required`. | The topic plan names later write-scope ambiguity as `human_review_required`. |
| R10 | No file outside the four target artifacts may be modified in this planning turn. | Only the four allowed analysis / plan files change. |

## Resolved Contradictions

### C1 - This batch must merge newer or divergent material, but current work is not merge execution

- Conflict: Phase 1 classified these candidates as `Need merge into skills/`,
  but the user explicitly requested planning only.
- Resolution: freeze the merge-required batch as a planning topic now and defer
  all actual merge work to later creator execution under a reviewed plan.

### C2 - Phase 1 gives reasons for merge-required status, but not one universal merge policy

- Conflict: the evidence shows multiple kinds of drift, including path drift,
  reference-set expansion, templates/scripts/tests addition, and missing
  canonical counterpart.
- Resolution: encode that merge policy discussion is expected and route any
  unsupported exact merge-policy choice to `human_review_required`.

### C3 - Some candidates carry runtime/projection concerns, but this topic must not widen into projection or runtime work

- Conflict: runtime dependency inventory shows `projection_required` or helper
  drift for some candidates, but current topic must remain bounded to planning
  the merge batch rather than designing projection/runtime changes.
- Resolution: preserve those concerns as planning inputs while keeping
  projection materialization and runtime adaptation out of scope.

## Explicit Assumptions

- A1: the umbrella coordination baseline is approved and may serve as the
  parent planning baseline for this topic.
- A2: the exact candidate set above is frozen from Phase 1 and should not be
  widened in this topic.
- A3: semantic drift / merge policy discussion is expected because Phase 1
  evidence shows behavior-changing differences for at least part of this batch.
- A4: current evidence is not sufficient to choose one exact merge policy or
  one exact later implementation write scope for every candidate without some
  human judgment.

## Non-goals

- Do not modify `skills/**`.
- Do not modify `.github/skills/**`.
- Do not modify `.codex/skills/**`.
- Do not modify `.github/agents/**`.
- Do not modify `.codex/agents/**`.
- Do not modify shared contract files.
- Do not modify umbrella topic artifacts.
- Do not begin merge implementation in this turn.
- Do not perform projection materialization.
- Do not perform runtime adaptation.
- Do not handle planning-spine exceptions.
- Do not handle copilot-only work.

## Extreme-Boundary Checks

| Boundary | Requirement result |
| --- | --- |
| A planner sees `merge_required` candidates and wants one blanket policy | The topic plan must still keep unsupported exact merge policy as `human_review_required` |
| A creator wants to treat `.github/skills/` as authority because it has newer content | The topic plan must still state that `.github/skills/` is not an authority source tree |
| A maintainer wants to collapse alias/path drift silently into `skills/` | The topic plan must still require explicit semantic drift discussion rather than silent collapse |
| A later executor cannot derive exact file scope for merge work | The topic plan must still route exact later write scope to `human_review_required` |

## Success Signals

This topic is frozen successfully when:

1. the merge-batch planning baseline is repo-visible,
2. the exact ten-candidate set is frozen,
3. current work is explicitly planning-only,
4. semantic / alias / behavior drift is acknowledged rather than hidden,
5. projection/runtime/copilot-only work remains excluded,
6. and unsupported later merge policy or exact write-scope decisions are
   surfaced as `human_review_required`.
