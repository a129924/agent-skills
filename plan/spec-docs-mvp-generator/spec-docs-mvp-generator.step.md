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
- [ ] draft plan commit by topic
- [ ] `(subAgent) .codex/skills/plan-reviewer review the plan and requirement doc and then feedback`
- [ ] `(subAgent) skills/plan-creator fix and update and feedback`
- [ ] `(subAgent) planner final gate`
- [ ] wait human check

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

### draft plan commit by topic

- [ ] Prepare one planning-only commit for:
  - `analysis/spec-docs-mvp-generator/requirements.md`
  - `analysis/spec-docs-mvp-generator/technical-spec.md`
  - `plan/spec-docs-mvp-generator/spec-docs-mvp-generator.plan.md`
  - `plan/spec-docs-mvp-generator/spec-docs-mvp-generator.step.md`
- [ ] Confirm the commit scope does not include implementation files under
  `skills/spec-docs-mvp-generator/`
- [ ] Do not enter implementation before the planning-artifact commit exists

### `(subAgent) .codex/skills/plan-reviewer review the plan and requirement doc and then feedback`

- [ ] Run independent plan review against:
  - `analysis/spec-docs-mvp-generator/requirements.md`
  - `analysis/spec-docs-mvp-generator/technical-spec.md`
  - `plan/spec-docs-mvp-generator/spec-docs-mvp-generator.plan.md`
  - `plan/spec-docs-mvp-generator/spec-docs-mvp-generator.step.md`
- [ ] Verify the plan does not reopen canonical/path/projection/runtime
  decisions and does not expand into a full architecture docs suite
- [ ] Verify the exact implementation write set matches the technical baseline
  and excludes extra scripts, tests, release files, and projection surfaces
- [ ] Return reviewer feedback without entering implementation
- [ ] If reviewer feedback begins to control routing or creates a multi-round
  rework loop, stop and amend the topic plan to add an exact
  `review-log.md` path before continuing

### `(subAgent) skills/plan-creator fix and update and feedback`

- [ ] If review returns `needs-rework`, repair only the planning artifacts
  needed to satisfy the contract:
  - `plan/spec-docs-mvp-generator/spec-docs-mvp-generator.plan.md`
  - `plan/spec-docs-mvp-generator/spec-docs-mvp-generator.step.md`
- [ ] Keep all fixes aligned to
  `analysis/spec-docs-mvp-generator/technical-spec.md`
  and `analysis/spec-docs-mvp-generator/requirements.md`
- [ ] Do not widen scope into implementation, projection work, runtime
  behavior, or a larger docs suite during plan repair
- [ ] Re-submit the repaired planning artifacts for reviewer confirmation

### `(subAgent) planner final gate`

- [ ] Run final gate only after approved review state is reflected in repo-
  visible truth
- [ ] Confirm the accepted plan still maps 100% to
  `analysis/spec-docs-mvp-generator/technical-spec.md`
- [ ] Confirm the implementation write set remains exactly:
  - `skills/spec-docs-mvp-generator/SKILL.md`
  - `skills/spec-docs-mvp-generator/reference.md`
  - `skills/spec-docs-mvp-generator/examples.md`
  - `skills/spec-docs-mvp-generator/templates/spec-template.md`
  - `skills/spec-docs-mvp-generator/templates/data-ownership-map-template.md`
- [ ] Confirm non-stable intent remains explicit and no release action was
  introduced
- [ ] Final gate verdict must be repo-visible before the topic can move to
  human check

### wait human check

- [ ] Stop and wait for explicit human check after planner final gate passes
- [ ] Do not enter implementation before human check authorizes it
- [ ] After authorization, hand off to creator with the locked plan and keep
  `step.md` as the current progression artifact

### future creator execution after human check

- [ ] Create the canonical skill package skeleton at
  `skills/spec-docs-mvp-generator/` and add the two template files:
  - `skills/spec-docs-mvp-generator/templates/spec-template.md`
  - `skills/spec-docs-mvp-generator/templates/data-ownership-map-template.md`
- [ ] Define the skill input contract and refusal rules in
  `skills/spec-docs-mvp-generator/SKILL.md`:
  - require `spec-name`
  - allow only optional bounded background inputs
  - target only `docs/01-specs/<spec-name>.md` and
    `docs/02-spec-relations/data-ownership-map.md`
  - refuse architecture principles, multi-spec maps, interfaces, flows, state
    machines, ADRs, implementation notes, and projection/runtime work
- [ ] Define safe rerun / merge semantics in
  `skills/spec-docs-mvp-generator/reference.md`:
  - create missing files from templates
  - preserve existing user-authored content
  - backfill only missing fixed sections or table header
  - avoid duplicate fixed headings
  - avoid destructive whole-file rewrite
  - stay local-only with no network dependency
- [ ] Add example coverage and reviewer verification points in
  `skills/spec-docs-mvp-generator/examples.md`:
  - new spec generation
  - existing spec missing-section backfill
  - existing ownership-map missing-header backfill
  - out-of-scope refusal / reroute
- [ ] Update this `step.md` from repo-visible facts as creator execution
  progresses, without marking any of the above complete before they actually
  happen

## Handoff / Gate Notes

- Current progression truth stops after
  `.github/prompts/create-agent-plan.prompt.md`.
- `plan/spec-docs-mvp-generator/spec-docs-mvp-generator.step.md` now exists as
  the required workflow progression artifact from requirement `R8`.
- The next allowed role is `Plan-Reviewer`.
- No reviewer verdict, plan-repair loop, planner final gate, human check,
  commit, or implementation progress has happened yet in repo-visible truth.
- The unchecked `future creator execution after human check` items are required
  workflow-ready implementation categories from the technical baseline; they
  are planning guidance only until human authorization exists.
- The frozen analysis artifacts remain prerequisites and must not be reopened
  unless a separate scope change is explicitly approved.
- This `*.step.md` is the workflow progression artifact only; it must be
  updated from repo-visible facts and must not be used to infer hidden
  approvals or completed gates.
