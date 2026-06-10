# Technical Specification: phase-2-merge-into-skills-batch

**Status**: frozen - ready for plan authoring
**Topic**: `phase-2-merge-into-skills-batch`
**Source baseline**: `analysis/phase-2-merge-into-skills-batch/requirements.md`

---

## Baseline Summary

The frozen baseline requires a planning-only topic for the merge-required Phase
2 candidate batch. The purpose is to define a bounded planning contract for
candidates whose Phase 1 evidence shows semantic drift, path drift,
reference-set expansion, or runtime / projection sensitivity, without forcing
an implementation merge policy prematurely.

The implementation-facing translation is:

- create one repo-visible topic plan for the merge batch,
- freeze the exact ten-candidate set,
- preserve the canonical and non-authority surface model,
- explicitly acknowledge drift and merge-policy discussion,
- exclude projection materialization, runtime adaptation, planning-spine
  exception handling, and copilot-only work,
- and mark unsupported exact merge policy or later exact write scope as
  `human_review_required`.

This is not merge implementation in the current turn. It is planning baseline
only.

---

## Requirement Traceability

| Requirement | Technical realization | Dependencies | Cost / burden | Status |
| --- | --- | --- | --- | --- |
| R1 merge-batch planning baseline exists | Create `plan/phase-2-merge-into-skills-batch/phase-2-merge-into-skills-batch.plan.md` and `.step.md` | workflow contract, topic-plan contract | low | feasible |
| R2 current turn stays planning only | Lock current workflow stage to planning and forbid merge implementation now | user instruction, workflow contract | low | feasible |
| R3 candidate set is frozen exactly | Record the exact ten candidates in requirements and plan | Phase 1 `06`, topic facts | low | feasible |
| R4 canonical / non-authority model stays explicit | State `skills/` canonical and `.github/skills/`, `.codex/skills/` non-authority | governance and positioning baseline | low | feasible |
| R5 `.codex/skills/` stays partial projection only | Record that projection concerns may exist but projection work is not authorized here | repo positioning, runtime inventory | low | feasible |
| R6 drift discussion is explicit | Use semantic drift and runtime inventory as planning inputs and reject silent collapse | Phase 1 `04` and `05` | medium | feasible |
| R7 out-of-scope work stays excluded | Exclude safe batch, planning-spine exceptions, projection, runtime, and copilot-only work | umbrella baseline, topic facts | low | feasible |
| R8 exact merge policy ambiguity routes to human review | Add `human_review_required` note when evidence does not determine policy | current evidence limitations | medium | feasible |
| R9 exact later write-scope ambiguity routes to human review | Add `human_review_required` note when exact downstream file scope would otherwise be guessed | current evidence limitations | medium | feasible |
| R10 write set stays bounded | Restrict edits to the four target files only | user write set | low | feasible |

---

## Required Technical Tasks and Artifacts

### Workstream A - Freeze merge-batch requirements

Create and preserve:

- `analysis/phase-2-merge-into-skills-batch/requirements.md`
- `analysis/phase-2-merge-into-skills-batch/technical-spec.md`

These files capture the planning baseline for merge-required candidates and
remove dependence on hidden chat context.

### Workstream B - Author merge-batch topic plan

Create:

- `plan/phase-2-merge-into-skills-batch/phase-2-merge-into-skills-batch.plan.md`

That plan should define:

- current turn is planning-only,
- exact candidate set,
- exact out-of-scope boundaries,
- expectation that semantic / alias / behavior drift review is required,
- and `human_review_required` handling for exact later merge policy or exact
  later write scope where current evidence is insufficient.

### Workstream C - Create progression truth

Create:

- `plan/phase-2-merge-into-skills-batch/phase-2-merge-into-skills-batch.step.md`

That artifact should:

- mark analysis and plan authoring complete for this turn,
- record review / final-gate / human-check as remaining,
- and state that no merge implementation begins from step artifact alone.

### Workstream D - Preserve evidence-backed drift boundaries

The plan must incorporate evidence that:

- `agent-skill-creator` and `agent-skill-template` have behavior-changing path
  drift,
- several Python authoring / tooling skills have GitHub-surface references,
  templates, scripts, tests, or broader wording that imply merge work rather
  than blind replacement,
- `python-blueprint-review` lacks a canonical counterpart under `skills/`,
- and some candidates carry `projection_required` runtime signals without
  authorizing projection work here.

---

## Dependency and Integration Notes

- `AGENTS.md` remains the governance canonical source.
- `docs/repo-positioning.md` confirms `skills/` as canonical truth and
  `.github/**` / `.codex/**` as non-authority compatibility or projection
  surfaces.
- `plan/agent-handoff-workflow.md` defines workflow progression, stop points,
  and truth-artifact semantics.
- `plan/topic-plan-contract.md` defines the required plan sections and
  blocking semantics.
- `plan/phase-2-umbrella/phase-2-umbrella.plan.md` and `.step.md` define this
  topic as a later slice under an approved coordination baseline.
- `docs/agent-skills-convergence/phase-1/06-convergence-candidates.md`
  identifies this exact batch as `Need merge into skills/`.
- `docs/agent-skills-convergence/phase-1/04-semantic-drift-report.md`
  provides behavior-changing drift evidence for a subset of candidates.
- `docs/agent-skills-convergence/phase-1/05-runtime-dependency-inventory.md`
  provides runtime / projection sensitivity inputs for some candidates.

---

## Cost-of-Realization Assessment

| Workstream | Complexity | Sequencing pressure | Operational / maintenance burden |
| --- | --- | --- | --- |
| Freeze merge-batch requirements | low | must happen first | very low |
| Author merge-batch topic plan | medium | core outcome | low |
| Create progression truth | low | same planning pass | very low |
| Preserve drift boundaries | medium | required for correctness | low |

Estimated effort is low-to-moderate for planning. The main risk is pretending
that different merge-required candidates can all follow one evidence-free merge
policy.

---

## Architecture Compliance Self-Check

| Dimension | Result | Notes |
| --- | --- | --- |
| Governance ownership | fits | `AGENTS.md` remains canonical |
| Canonical skill target | fits | `skills/` remains the convergence target |
| Non-authority surface model | fits | `.github/skills/` and `.codex/skills/` remain non-authority |
| Drift visibility | fits | semantic and behavior drift stays explicit |
| Projection/runtime boundary | fits | risks recorded but implementation deferred |
| Planning-only current turn | fits | no merge implementation artifact is needed now |

### Compliance notes

- Fit: the planning baseline can be completed inside the provided write set.
- Mismatch risk: current evidence does not fully determine one exact merge
  policy or one exact later per-file write scope across all candidates, so
  those decisions must stay `human_review_required`.

---

## Conflicts, Blockers, and Rollback-to-Alignment Triggers

### Current blockers

None for planning baseline creation. Current evidence is sufficient to freeze
topic boundaries and identify where later execution still needs explicit
judgment.

### Rollback triggers

Return to alignment before implementation proceeds if any of the following
becomes true:

1. a candidate outside the frozen ten-skill set is proposed for inclusion;
2. later execution tries to collapse alias/path/behavior drift without an
   explicit merge rationale;
3. exact merge policy or exact later file scope would need to be guessed from
   insufficient evidence;
4. a maintainer tries to pull projection, runtime adaptation, or copilot-only
   work into this topic.

### Conflict handling note

If later execution needs per-candidate merge policy or exact path locking that
the current evidence cannot support directly, stop and request
`human_review_required` instead of inventing a generic merge rule.

---

## Recommended Next Step

Author `plan/phase-2-merge-into-skills-batch/phase-2-merge-into-skills-batch.plan.md`
in strict mode so the merge-required batch has one bounded planning contract
before any creator merge execution begins.
