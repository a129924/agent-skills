# Technical Specification: phase-2-umbrella

**Status**: frozen - ready for plan authoring
**Topic**: `phase-2-umbrella`
**Source baseline**: `analysis/phase-2-umbrella/requirements.md`

---

## Baseline Summary

The frozen baseline requires a Phase 2 umbrella topic that coordinates later
slice planning without performing convergence work itself.

The implementation-facing translation is:

- define one repo-visible umbrella plan as a coordination baseline only,
- freeze the three later execution slices and their sequence,
- freeze the exact safe canonical batch list,
- require each later slice to branch from umbrella baseline and carry its own
  plan / review / human-check / PR,
- keep `docs/status.md` optional only,
- and keep all implementation work outside the umbrella topic's writable scope.

This is not a convergence implementation topic. It is a coordination baseline.

---

## Requirement Traceability

| Requirement | Technical realization | Dependencies | Cost / burden | Status |
| --- | --- | --- | --- | --- |
| R1 repo-visible umbrella baseline exists | Create `plan/phase-2-umbrella/phase-2-umbrella.plan.md` and `plan/phase-2-umbrella/phase-2-umbrella.step.md` | repo workflow contract, topic-plan contract | low | feasible |
| R2 umbrella stays coordination-only | Lock scope to planning artifacts and forbid skill / projection / runtime edits | `AGENTS.md`, `docs/repo-positioning.md` | low | feasible |
| R3 `skills/` stays canonical target | Record canonical target and non-authority surfaces in plan locked decisions | Phase 1 summary and Phase 2 inputs | low | feasible |
| R4 later slices and order are explicit | Encode the three slice topics and make `phase-2-safe-canonical-batch` first | `docs/agent-skills-convergence/phase-1/07-phase-2-inputs.md` | low | feasible |
| R5 safe batch list is frozen | List the nine skills exactly in requirements and plan | `docs/agent-skills-convergence/phase-1/06-convergence-candidates.md`, `07-phase-2-inputs.md` | low | feasible |
| R6 PR order is serialized | Add a locked rule that slice PRs are strictly serialized | workflow contract and topic plan | low | feasible |
| R7 each slice has its own workflow loop | State that umbrella topic does not satisfy later slice review or human gates | workflow contract | medium | feasible |
| R8 `docs/status.md` stays optional | Treat it as optional overview only; do not list it as required execution truth | artifact-role facts | low | feasible |
| R9 artifact-role model is explicit | Restate `summary.md`, `step.md`, and `docs/status.md` roles in topic plan | workflow contract | low | feasible |
| R10 write set stays bounded | Restrict writes to `analysis/phase-2-umbrella/*` and `plan/phase-2-umbrella/*` only | user write set | low | feasible |

---

## Required Technical Tasks and Artifacts

### Workstream A - Freeze umbrella requirements

Create and preserve the bounded planning baseline through:

- `analysis/phase-2-umbrella/requirements.md`
- `analysis/phase-2-umbrella/technical-spec.md`

These files capture Phase 2 coordination facts so later slice plans do not
depend on hidden chat context.

### Workstream B - Author umbrella topic plan

Create:

- `plan/phase-2-umbrella/phase-2-umbrella.plan.md`

That plan should define:

- umbrella topic purpose and coordination-only scope,
- exact later slice names and order,
- exact safe canonical batch membership,
- serialized slice PR rule,
- exact statement that each later slice needs its own plan / review /
  human-check / PR.

### Workstream C - Create progression truth

Create:

- `plan/phase-2-umbrella/phase-2-umbrella.step.md`

That artifact should:

- record that this topic is a planning baseline,
- state current actionable next work as later slice plan authoring rather than
  implementation,
- preserve the strict ordering that starts with
  `phase-2-safe-canonical-batch`.

### Workstream D - Enforce non-goals and write-set boundaries

The umbrella plan must explicitly forbid:

- edits under `skills/**`
- edits under `.github/skills/**`
- edits under `.codex/skills/**`
- edits under `.github/agents/**`
- edits under `.codex/agents/**`
- convergence implementation
- projection materialization
- runtime adaptation
- any treatment of umbrella as a fourth implementation line

---

## Dependency and Integration Notes

- `AGENTS.md` remains the governance canonical source.
- `docs/repo-positioning.md` confirms that `skills/` is canonical and
  platform-facing surfaces are compatibility or projection only.
- `plan/agent-handoff-workflow.md` governs workflow states and truth-artifact
  semantics for later slice execution.
- `plan/topic-plan-contract.md` governs the required structure and blocking
  semantics for the umbrella topic plan.
- `docs/agent-skills-convergence/phase-1/06-convergence-candidates.md` and
  `docs/agent-skills-convergence/phase-1/07-phase-2-inputs.md` provide the
  frozen candidate grouping and Phase 2 slice input.

---

## Cost-of-Realization Assessment

| Workstream | Complexity | Sequencing pressure | Operational / maintenance burden |
| --- | --- | --- | --- |
| Freeze umbrella requirements | low | must happen first | very low |
| Author umbrella topic plan | medium | core outcome | low |
| Create progression truth | low | same planning pass | very low |
| Enforce non-goals and write-set boundaries | low | must remain explicit | very low |

Estimated effort is low. The main risk is scope drift into implementation or
confusing cross-topic status tracking with execution truth.

---

## Architecture Compliance Self-Check

| Dimension | Result | Notes |
| --- | --- | --- |
| Governance ownership | fits | `AGENTS.md` remains canonical |
| Repository positioning | fits | `skills/` stays canonical; platform surfaces stay non-authority |
| Workflow alignment | fits | later slices still require normal plan/review/human/PR flow |
| Umbrella topic scope | fits | coordination-only; no implementation |
| Projection/runtime boundary | fits | still deferred |
| Write-set boundary | fits | no shared contract files or skill surfaces need edits |

### Compliance notes

- Fit: the umbrella topic can be completed inside the provided write set.
- Mismatch risk: if a later reviewer insists on adding shared-contract changes
  or implementation artifacts under this topic, that would require
  `human_review_required` instead of widening scope by assumption.

---

## Conflicts, Blockers, and Rollback-to-Alignment Triggers

### Current blockers

None from the current evidence set. The umbrella baseline is plannable inside
the declared write set.

### Rollback triggers

Return to alignment before implementation proceeds if any of the following
becomes true:

1. a later slice cannot be described honestly without changing umbrella facts
   about order, safe batch membership, or artifact roles;
2. execution under this topic would require editing any skill or projection
   surface;
3. a maintainer tries to use `docs/status.md` as execution truth instead of
   `step.md` or `summary.md`;
4. a reviewer or executor treats umbrella scope as permission to start direct
   convergence work.

### Conflict handling note

If a future slice needs updated grouping, expanded batch membership, or a
different serialized order, raise a new planning repair topic instead of
silently editing downstream slice plans against umbrella truth.

---

## Recommended Next Step

Author `plan/phase-2-umbrella/phase-2-umbrella.plan.md` in strict mode so it
freezes the Phase 2 coordination baseline, then use
`phase-2-safe-canonical-batch` as the first later slice topic for separate plan
authoring.
