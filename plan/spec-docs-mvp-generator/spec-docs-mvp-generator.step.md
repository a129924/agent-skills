---
topic: spec-docs-mvp-generator
status: planned
created: 2026-06-16
current_plan_input: plan/spec-docs-mvp-generator/spec-docs-mvp-generator.plan.md
---

# Spec Docs MVP Generator Steps

## Workflow Stages

- [X] create worktree
- [X] `.github/prompts/create-analysis.prompt.md`
- [X] `.github/prompts/create-agent-plan.prompt.md`
- [X] `(subAgent) skills/plan-reviewer review the plan and return reviewer handoff`
- [X] `(subAgent) skills/plan-creator fix and update and feedback`

## Actionable Steps

### create worktree

- [X] Use managed worktree
  `/Users/andrew/code/python/agent-skills.worktrees/agent-20260616-spec-docs-mvp-generator`
- [X] Use branch `feat/andrew/spec-docs-mvp-generator`
- [X] Keep all planning work inside this worktree only

### `.github/prompts/create-analysis.prompt.md`

- [X] Freeze `analysis/spec-docs-mvp-generator/requirements.md`
- [X] Freeze `analysis/spec-docs-mvp-generator/technical-spec.md`
- [X] Lock the topic to canonical `skills/spec-docs-mvp-generator/` only
- [X] Lock the later implementation write set to:
  - `skills/spec-docs-mvp-generator/SKILL.md`
  - `skills/spec-docs-mvp-generator/reference.md`
  - `skills/spec-docs-mvp-generator/examples.md`
  - `skills/spec-docs-mvp-generator/templates/spec-template.md`
  - `skills/spec-docs-mvp-generator/templates/data-ownership-map-template.md`
- [X] Record that later planning must create
  `plan/spec-docs-mvp-generator/spec-docs-mvp-generator.step.md`
  and that analysis itself must not create planning artifacts

### `.github/prompts/create-agent-plan.prompt.md`

- [X] Materialize `plan/spec-docs-mvp-generator/spec-docs-mvp-generator.plan.md`
- [X] Materialize `plan/spec-docs-mvp-generator/spec-docs-mvp-generator.step.md`
- [X] Record strict-mode analysis prerequisites and SHA-256 values in the topic
  plan
- [X] Map `Artifact Paths` and `Implementation Steps` 100% to
  `analysis/spec-docs-mvp-generator/technical-spec.md`
- [X] Record non-stable intent, exact implementation write set, and explicit
  out-of-scope exclusions
- [X] Keep the planning batch bounded to planning artifacts only, with no
  reviewer, commit, or implementation work claimed

### `(subAgent) skills/plan-reviewer review the plan and return reviewer handoff`

- [X] Run independent plan review against:
  - `analysis/spec-docs-mvp-generator/requirements.md`
  - `analysis/spec-docs-mvp-generator/technical-spec.md`
  - `plan/spec-docs-mvp-generator/spec-docs-mvp-generator.plan.md`
  - `plan/spec-docs-mvp-generator/spec-docs-mvp-generator.step.md`
- [X] Verify the plan does not reopen canonical/path/projection/runtime
  decisions and does not expand into a full architecture docs suite
- [X] Verify the exact implementation write set matches the technical baseline
  and excludes extra scripts, tests, release files, and projection surfaces
- [X] Return reviewer feedback without entering implementation
- [X] Reviewer feedback already controlled routing once for this topic, so the
  exact handoff path
  `plan/spec-docs-mvp-generator/spec-docs-mvp-generator.review-log.md`
  is now part of the topic contract
- [X] Materialize the reviewer verdict history at
  `plan/spec-docs-mvp-generator/spec-docs-mvp-generator.review-log.md`
  before the next re-review handoff continues

### `(subAgent) skills/plan-creator fix and update and feedback`

- [X] If review returns `needs-rework`, repair only the planning artifacts
  needed to satisfy the contract:
  - `plan/spec-docs-mvp-generator/spec-docs-mvp-generator.plan.md`
  - `plan/spec-docs-mvp-generator/spec-docs-mvp-generator.step.md`
- [X] Keep all fixes aligned to
  `analysis/spec-docs-mvp-generator/technical-spec.md`
  and `analysis/spec-docs-mvp-generator/requirements.md`
- [X] Repair the planning contract coverage for skill package and template work:
  - keep the exact implementation paths for `SKILL.md`, `reference.md`,
    `examples.md`, `templates/spec-template.md`, and
    `templates/data-ownership-map-template.md`
  - keep the step breakdown explicit for creating the skill package and both
    template files only
- [X] Repair the planning contract coverage for input contract and refusal rules:
  - keep required `spec-name`, optional background inputs, and stop-and-ask
    behavior when `spec-name` is missing
  - keep explicit refusal / reroute coverage for out-of-scope outputs and
    projection/runtime requests
- [X] Repair the planning contract coverage for safe rerun / merge rules:
  - keep first-creation, missing-section backfill, and missing-header backfill
    behavior explicit
  - keep non-destructive merge rules explicit: preserve existing content, avoid
    duplicate fixed headings, and forbid whole-file overwrite
- [X] Repair the planning contract coverage for examples and reviewer validation:
  - keep the four required example classes explicit in planning artifacts
  - keep reviewer-checkable validation points aligned to the technical spec
- [X] Do not widen scope into implementation, projection work, runtime
  behavior, or a larger docs suite during plan repair
- [X] Re-submit the repaired planning artifacts for reviewer confirmation

## Handoff / Gate Notes

- Current progression truth now includes the repaired `step.md`, the
  materialized `review-log.md`, and the latest approved re-review verdict.
- `plan/spec-docs-mvp-generator/spec-docs-mvp-generator.step.md` now exists as
  the required workflow progression artifact from requirement `R8`.
- One `needs-rework` plan-review verdict has already happened, so reviewer
  routing is now active for this topic.
- The exact repo-visible handoff path for that re-review loop is
  `plan/spec-docs-mvp-generator/spec-docs-mvp-generator.review-log.md`.
- The review-log handoff path has now been materialized at
  `plan/spec-docs-mvp-generator/spec-docs-mvp-generator.review-log.md`, and
  the latest repo-visible reviewer verdict is `approved`.
- The next allowed role is `Planner final gate`.
- The next remaining repo-visible gap is executing the planner final gate
  against the now contract-aligned `plan.md`, `step.md`, and `review-log.md`.
- No publish, merge, or implementation progress has happened yet in repo-visible
  truth.
- This progression artifact does not define a separate draft-plan-commit gate
  and does not treat `.codex/**` as workflow authority.
- The frozen analysis artifacts remain prerequisites and must not be reopened
  unless a separate scope change is explicitly approved.
- This `*.step.md` is the workflow progression artifact only; it must be
  updated from repo-visible facts and must not be used to infer hidden
  approvals or completed gates.
