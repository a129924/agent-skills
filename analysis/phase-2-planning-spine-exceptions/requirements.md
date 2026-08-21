# phase-2-planning-spine-exceptions requirements

## Purpose

Freeze the final Phase 2 planning and execution baseline for the remaining
planning-spine exceptions without widening into unrelated skills, compatibility
surfaces, projection work, or runtime adaptation.

This topic exists because `plan-creator` and `plan-reviewer` were explicitly
deferred from the safe canonical batch and merge-into-skills batch due to
high-risk authority, workflow, and handoff drift.

## Accepted upstream baseline

- `skills/` is the canonical convergence target.
- `.github/skills/` and `.codex/skills/` are not authority source trees.
- `.codex/skills/` is only a partial projection surface.
- `phase-2-umbrella` is the approved coordination parent.
- `phase-2-safe-canonical-batch` is complete.
- `phase-2-merge-into-skills-batch` is complete.
- Slice PR order is strictly serialized.
- `phase-2-planning-spine-exceptions` is the final Phase 2 execution slice.

## Frozen skill set

This topic is limited to:

- `skills/plan-creator/**`
- `skills/plan-reviewer/**`

No other skill surface may be modified under the initial planning baseline for
this topic.

## Problem statement

Phase 1 recorded high-risk drift for both planning-spine skills:

- `plan-creator`
  - fallback contract source differs between surfaces
  - behavioral impact was classified as high
  - runtime mode was classified as `projection_required`
- `plan-reviewer`
  - review basis path and blocked behavior differ between surfaces
  - behavioral impact was classified as high
  - runtime mode was classified as `projection_required`

Human review also established:

- shared planning authority must live in one repo-level contract
- `plan-creator` and `plan-reviewer` must not depend on each other as required
  contract sources
- repo-level plan-contract authority now lives above both skills

## Requirements

| ID | Requirement | Acceptance signal |
| --- | --- | --- |
| R1 | The topic must define planning-spine convergence only for `skills/plan-creator/**` and `skills/plan-reviewer/**`. | The topic plan lists only those two skill surfaces as later execution targets. |
| R2 | The topic must preserve `skills/` as the only canonical convergence target. | The topic plan states `.github/**` and `.codex/**` are read-only reference inputs only. |
| R3 | The topic must identify which authority, workflow, fallback, handoff, review, and close semantics can be safely converged inside `skills/`. | The technical spec separates direct canonical edits from unresolved authority decisions. |
| R4 | The topic must not silently collapse semantic drift, behavior drift, or authority drift. | Open questions and unresolved items are explicitly marked `human_review_required`. |
| R5 | The topic must remain bounded to topic-local planning artifacts during the initial workflow. | The plan and step artifacts declare an initial write set limited to topic-local `analysis/` and `plan/` files. |
| R6 | The topic must define what later execution may modify if human approval is obtained. | The topic plan limits later execution to `skills/plan-creator/**` and `skills/plan-reviewer/**`. |
| R7 | The topic must explicitly preserve prior Phase 2 baselines and serial slice ordering. | The topic plan treats umbrella, safe batch, and merge batch artifacts as frozen read-only parents. |
| R8 | The topic must stay non-stable and non-release-bearing. | The topic plan states that no README, VERSION, release, or tagging work belongs to this topic. |

## In scope

- Create:
  - `analysis/phase-2-planning-spine-exceptions/requirements.md`
  - `analysis/phase-2-planning-spine-exceptions/technical-spec.md`
  - `plan/phase-2-planning-spine-exceptions/phase-2-planning-spine-exceptions.plan.md`
  - `plan/phase-2-planning-spine-exceptions/phase-2-planning-spine-exceptions.step.md`
- Freeze the bounded skill set:
  - `skills/plan-creator/**`
  - `skills/plan-reviewer/**`
- Define canonical convergence rules for these two skills inside `skills/`.
- Record which issues still require explicit human review before bounded
  execution may proceed.

## Out of scope

- Any edit under `.github/**`
- Any edit under `.codex/**`
- Any edit under `.github/agents/**`
- Any edit under `.codex/agents/**`
- Any projection materialization
- Any runtime adaptation
- Any copilot-only convergence
- Any direct convergence for unrelated skills
- Any broad repo-level governance rewrite outside the bounded exception topic

## Human-review-required areas

The planning baseline must preserve these as unresolved unless later evidence
becomes decisive:

- exact canonical wording when a skill-local instruction appears to restate or
  reinterpret repo-level authority
- whether any existing `plan-creator` or `plan-reviewer` checklist/reference
  text changes blocked behavior rather than just wording
- whether any fallback or review-basis statement inside either skill still
  conflicts with `plan/topic-plan-contract.md`
- whether any topic-local execution should touch examples, templates, or
  references beyond what is strictly necessary for canonical convergence
- whether future compatibility-surface alignment should happen at all

## Non-stable intent

This topic does not affect stable-library release surfaces.

- no `README.md` update
- no `VERSION` update
- no release note or tag work
