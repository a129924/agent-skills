# Technical Specification: phase-2-safe-canonical-batch

**Status**: frozen - ready for plan authoring
**Topic**: `phase-2-safe-canonical-batch`
**Source baseline**: `analysis/phase-2-safe-canonical-batch/requirements.md`

---

## Baseline Summary

The frozen baseline requires a planning-only topic for the first execution
slice after umbrella. The purpose is to define how later canonical convergence
work may proceed for the exact nine low-risk skills without widening into other
Phase 2 slices or any projection/runtime path.

The implementation-facing translation is:

- create one repo-visible topic plan for the first slice,
- freeze the exact nine-skill safe canonical batch,
- preserve the canonical and non-authority surface model,
- state that later implementation remains bounded to those nine skills only,
- exclude merge-into-skills, planning-spine exceptions, projection, runtime,
  and copilot-only work,
- and flag any later exact implementation write-scope guess as
  `human_review_required`.

This is not implementation in the current turn. It is planning baseline only.

---

## Requirement Traceability

| Requirement | Technical realization | Dependencies | Cost / burden | Status |
| --- | --- | --- | --- | --- |
| R1 first-slice planning baseline exists | Create `plan/phase-2-safe-canonical-batch/phase-2-safe-canonical-batch.plan.md` and `plan/phase-2-safe-canonical-batch/phase-2-safe-canonical-batch.step.md` | workflow contract, topic-plan contract | low | feasible |
| R2 current turn stays planning only | Lock current workflow stage to planning and forbid implementation in this turn | user instruction, workflow contract | low | feasible |
| R3 umbrella parent is explicit | Cite parent branch `feat/andrew/phase-2-umbrella` at `9d1d784` in requirements and plan | umbrella artifacts | low | feasible |
| R4 safe list is frozen exactly | Record the exact nine skills in requirements and plan | Phase 1 `06` and `07`, umbrella plan | low | feasible |
| R5 canonical / non-authority model stays explicit | State `skills/` canonical and `.github/skills/`, `.codex/skills/` non-authority in plan locked decisions | repo positioning baseline | low | feasible |
| R6 later implementation is bounded to safe list only | Add a lock that later execution may not widen beyond the nine skills | Phase 1 evidence and umbrella scope | medium | feasible |
| R7 later slices remain out of scope | Explicitly exclude `phase-2-merge-into-skills-batch` and `phase-2-planning-spine-exceptions` | umbrella baseline | low | feasible |
| R8 projection/runtime/copilot-only work stays out of scope | Explicitly exclude `.codex/skills/` materialization, runtime adaptation, and copilot-only work | repo positioning and Phase 1 evidence | low | feasible |
| R9 `docs/status.md` stays optional | Treat it as optional overview only | umbrella baseline, workflow truth model | low | feasible |
| R10 guessed implementation scope routes to human review | Add `human_review_required` note for later implementation scope items not exactly derivable from current evidence | current evidence limitations | medium | feasible |
| R11 write set stays bounded | Restrict edits to the four allowed files only | user write set | low | feasible |

---

## Required Technical Tasks and Artifacts

### Workstream A - Freeze first-slice requirements

Create and preserve:

- `analysis/phase-2-safe-canonical-batch/requirements.md`
- `analysis/phase-2-safe-canonical-batch/technical-spec.md`

These files capture the planning baseline for the first execution slice and
remove dependence on hidden chat context.

### Workstream B - Author first-slice topic plan

Create:

- `plan/phase-2-safe-canonical-batch/phase-2-safe-canonical-batch.plan.md`

That plan should define:

- current turn is planning-only,
- exact parent umbrella baseline,
- exact nine-skill safe list,
- exact exclusion of later slices and non-safe work,
- bounded rule that later implementation may target only the frozen safe list,
- and `human_review_required` routing for any exact implementation scope that
  would otherwise be guessed.

### Workstream C - Create progression truth

Create:

- `plan/phase-2-safe-canonical-batch/phase-2-safe-canonical-batch.step.md`

That artifact should:

- mark analysis and plan authoring complete for this turn,
- record that review / final-gate / human-check remain ahead,
- and state that no implementation starts from this step artifact alone.

### Workstream D - Enforce out-of-scope boundaries

The plan must explicitly forbid:

- edits under all skill and agent surfaces,
- merge-into-skills work,
- planning-spine exception handling,
- projection materialization,
- runtime adaptation,
- and copilot-only work.

---

## Dependency and Integration Notes

- `AGENTS.md` remains the governance canonical source.
- `docs/repo-positioning.md` confirms `skills/` as canonical truth and
  platform-facing surfaces as non-authority projection / compatibility paths.
- `plan/agent-handoff-workflow.md` defines workflow progression, stop points,
  and truth-artifact semantics.
- `plan/topic-plan-contract.md` defines the required plan sections and
  blocking semantics.
- `plan/phase-2-umbrella/phase-2-umbrella.plan.md` and
  `plan/phase-2-umbrella/phase-2-umbrella.step.md` define this topic as the
  first later execution slice after an approved umbrella baseline.
- `docs/agent-skills-convergence/phase-1/06-convergence-candidates.md` and
  `docs/agent-skills-convergence/phase-1/07-phase-2-inputs.md` provide the
  low-risk safe list and exclude later buckets from this topic.

---

## Cost-of-Realization Assessment

| Workstream | Complexity | Sequencing pressure | Operational / maintenance burden |
| --- | --- | --- | --- |
| Freeze first-slice requirements | low | must happen first | very low |
| Author first-slice topic plan | medium | core outcome | low |
| Create progression truth | low | same planning pass | very low |
| Enforce out-of-scope boundaries | low | must remain explicit | very low |

Estimated effort is low. The main risk is pretending that Phase 1 low-risk
classification fully determines exact later implementation write scope.

---

## Architecture Compliance Self-Check

| Dimension | Result | Notes |
| --- | --- | --- |
| Governance ownership | fits | `AGENTS.md` remains canonical |
| Canonical skill target | fits | `skills/` remains the convergence target |
| Non-authority surface model | fits | `.github/skills/` and `.codex/skills/` remain non-authority |
| Slice isolation | fits | later slices remain out of scope |
| Projection/runtime boundary | fits | still deferred |
| Planning-only current turn | fits | no implementation artifact is needed now |

### Compliance notes

- Fit: the planning baseline can be completed inside the provided write set.
- Mismatch risk: exact later implementation write scope cannot be fully locked
  from current evidence alone without guessing file paths, so that part must
  stay `human_review_required`.

---

## Conflicts, Blockers, and Rollback-to-Alignment Triggers

### Current blockers

None for planning baseline creation. Current evidence is sufficient to freeze
the first-slice planning contract.

### Rollback triggers

Return to alignment before implementation proceeds if any of the following
becomes true:

1. later evidence shows one of the nine safe-batch skills is not actually
   low-risk canonical;
2. later execution would require work outside the frozen nine-skill list;
3. exact implementation write scope cannot be stated honestly without guessing
   paths or widening into later slices;
4. a maintainer tries to add projection, runtime, or copilot-only work into
   this topic.

### Conflict handling note

If later execution needs per-skill path locking that current evidence does not
support exactly, stop and request `human_review_required` rather than inventing
an implementation write set.

---

## Recommended Next Step

Author `plan/phase-2-safe-canonical-batch/phase-2-safe-canonical-batch.plan.md`
in strict mode so the first safe canonical slice has one bounded planning
contract before any creator implementation begins.
