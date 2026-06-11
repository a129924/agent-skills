# Technical Specification: phase-2-merge-into-skills-batch

**Status**: frozen - execution truth aligned, merged, and terminal
**Topic**: `phase-2-merge-into-skills-batch`
**Source baseline**: `analysis/phase-2-merge-into-skills-batch/requirements.md`

---

## Baseline Summary

The frozen baseline now describes an execution-active bounded canonical
convergence topic for the merge-required Phase 2 candidate batch. The purpose
is to record the bounded canonical convergence result for candidates whose
Phase 1 evidence shows semantic drift, path drift, reference-set expansion, or
runtime / projection sensitivity, without widening into compatibility-surface,
runtime, or projection implementation.

The implementation-facing translation is:

- preserve one repo-visible topic plan and progression artifact for the merge
  batch,
- freeze the exact ten-candidate set,
- preserve the canonical and read-only compatibility-surface model,
- allow bounded path convergence, semantic convergence, or both together under
  canonical `skills/` only,
- record the two completed canonical edit commits and the eight checked
  `no canonical edit needed` candidates,
- exclude projection materialization, runtime adaptation, planning-spine
  exception handling, and copilot-only work,
- and treat remaining compatibility-surface differences as non-blocking when
  canonical `skills/` is already correct.

---

## Requirement Traceability

| Requirement | Technical realization | Dependencies | Cost / burden | Status |
| --- | --- | --- | --- | --- |
| R1 merge-batch execution truth exists | Preserve `plan/phase-2-merge-into-skills-batch/phase-2-merge-into-skills-batch.plan.md` and `.step.md` as current execution truth | workflow contract, topic-plan contract | low | feasible |
| R2 bounded execution stays canonical-only | Restrict convergence to canonical `skills/<skill-name>/...` and keep `.github/**` / `.codex/**` read-only | user instruction, workflow contract | low | feasible |
| R3 candidate set is frozen exactly | Record the exact ten candidates in requirements and plan | Phase 1 `06`, topic facts | low | feasible |
| R4 canonical / compatibility model stays explicit | State `skills/` canonical and `.github/**`, `.codex/**` read-only compatibility surfaces | governance and positioning baseline | low | feasible |
| R5 `.codex/skills/` stays partial projection only | Record that projection concerns may exist but projection work is not authorized here | repo positioning, runtime inventory | low | feasible |
| R6 drift handling is explicit | Use semantic drift and runtime inventory as bounded execution inputs and reject silent collapse | Phase 1 `04` and `05` | medium | feasible |
| R7 out-of-scope work stays excluded | Exclude safe batch, planning-spine exceptions, projection, runtime, and copilot-only work | umbrella baseline, topic facts | low | feasible |
| R8 canonical edits are recorded exactly | Record `agent-skill-template` `0528a54` and `agent-skill-creator` `0f841da` as the only canonical edit commits | topic-local execution truth | low | feasible |
| R9 checked no-edit candidates are recorded exactly | Record the eight frozen candidates that required no canonical edit | topic-local execution truth | low | feasible |
| R10 compatibility-surface differences do not block progress | Keep `.github/**` / `.codex/**` read-only and mark residual differences as non-blocking | user instruction, topic-local execution truth | low | feasible |

---

## Required Technical Tasks and Artifacts

### Workstream A - Preserve merge-batch requirements truth

Create and preserve:

- `analysis/phase-2-merge-into-skills-batch/requirements.md`
- `analysis/phase-2-merge-into-skills-batch/technical-spec.md`

These files capture the bounded execution policy for merge-required candidates
and remove dependence on hidden chat context.

### Workstream B - Maintain merge-batch topic plan truth

Create:

- `plan/phase-2-merge-into-skills-batch/phase-2-merge-into-skills-batch.plan.md`

That plan should define:

- the exact candidate set,
- canonical `skills/` as the only convergence target,
- `.github/**` and `.codex/**` as read-only compatibility surfaces,
- the two completed canonical edit commits,
- the eight `no canonical edit needed` determinations,
- exact out-of-scope boundaries,
- and the merged terminal close-out truth on repo-visible artifacts.

### Workstream C - Maintain progression truth

Create:

- `plan/phase-2-merge-into-skills-batch/phase-2-merge-into-skills-batch.step.md`

That artifact should:

- mark analysis and plan authoring complete for this slice,
- record review and final-gate as complete,
- record human-check as complete,
- and state that no broader execution beyond the bounded canonical convergence
  slice is authorized yet.

### Workstream D - Preserve evidence-backed drift boundaries

The topic truth must incorporate evidence that:

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
| Preserve merge-batch requirements truth | low | already complete | very low |
| Maintain merge-batch topic plan truth | medium | core repo-visible contract | low |
| Maintain progression truth | low | same topic-local sync | very low |
| Preserve drift boundaries | medium | required for correctness | low |

Estimated effort is low-to-moderate for the bounded canonical convergence slice
and subsequent truth sync. The main risk is pretending that residual
compatibility-surface differences still require canonical edits when canonical
`skills/` truth is already correct.

---

## Architecture Compliance Self-Check

| Dimension | Result | Notes |
| --- | --- | --- |
| Governance ownership | fits | `AGENTS.md` remains canonical |
| Canonical skill target | fits | `skills/` remains the convergence target |
| Non-authority surface model | fits | `.github/skills/` and `.codex/skills/` remain non-authority |
| Drift visibility | fits | semantic and behavior drift stays explicit |
| Projection/runtime boundary | fits | risks recorded but implementation deferred |
| Execution-active bounded slice | fits | canonical convergence under `skills/` completed without widening into projection/runtime |

### Compliance notes

- Fit: the bounded canonical convergence and topic-local truth sync fit inside
  the provided write set.
- Mismatch risk: some candidates still carry compatibility/runtime differences,
  but those differences do not by themselves require canonical edits when
  `skills/` truth is already correct.

---

## Conflicts, Blockers, and Rollback-to-Alignment Triggers

### Current blockers

None for bounded canonical convergence truth sync. Current evidence is
sufficient to record the completed canonical edits, no-edit-needed
determinations, and merged terminal close-out truth.

### Rollback triggers

Return to alignment before any further execution proceeds if any of the
following becomes true:

1. a candidate outside the frozen ten-skill set is proposed for inclusion;
2. later execution tries to collapse alias/path/behavior drift without an
   explicit merge rationale;
3. a change would require editing `.github/**`, `.codex/**`, projection, or
   runtime surfaces;
4. a maintainer tries to pull projection, runtime adaptation, or copilot-only
   work into this topic.

### Conflict handling note

If later execution needs broader surface edits or policy decisions that the
current evidence cannot support directly, stop and request
`human_review_required` instead of widening this bounded canonical slice.

---

## Recommended Next Step

No further topic-local workflow step remains; treat the current repo-visible
execution truth as merged close-out state.
