---
topic: spec-docs-mvp-generator
status: approved
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
- [X] `(Implementer) repair implementation progression truth and return for re-review`
- [X] `(Implementer) apply bounded human minor patch for platform-path policy and progression truth`
- [X] `(Publisher) execute bounded pr-comment publish slice`

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

### `(Implementer) create canonical skill package and update progression truth`

- [X] Create `skills/spec-docs-mvp-generator/SKILL.md` with the single-spec v1
  contract:
  - require one explicit `spec-name`
  - lock downstream output to
    `docs/01-specs/<spec-name>.md` and
    `docs/02-spec-relations/data-ownership-map.md`
  - stop and ask when `spec-name` is missing
  - refuse out-of-scope output families and projection/runtime requests
- [X] Create `skills/spec-docs-mvp-generator/reference.md` with deterministic
  local-only write and merge semantics:
  - first-create rules for both downstream files
  - safe rerun, missing-section backfill, and missing-header backfill rules
  - preserve authored content, avoid duplicate fixed headings, and forbid
    destructive whole-file overwrite
- [X] Create `skills/spec-docs-mvp-generator/templates/spec-template.md` with
  the exact nine required sections and non-empty starter content
- [X] Create
  `skills/spec-docs-mvp-generator/templates/data-ownership-map-template.md`
  with the exact five required sections, the fixed ownership-table header, and
  non-empty seed content
- [X] Create `skills/spec-docs-mvp-generator/examples.md` with required
  scenario coverage:
  - new single-spec generation
  - existing spec missing-section backfill
  - existing ownership-map missing-header backfill
  - out-of-scope refusal
- [X] Create the canonical implementation artifacts inside the exact write set
- [X] Repair this `step.md` so implementation workflow truth matches the latest
  reviewer verdict from repo-visible evidence only
- [X] Keep implementation inside the exact write set with no scripts, tests,
  CLI, runtime orchestration, projection work, or broader docs-suite scope

### `(Implementer) apply bounded human minor patch for platform-path policy and progression truth`

- [X] Repair `skills/spec-docs-mvp-generator/SKILL.md` so skill-package
  instructions rely on this skill package's local references and templates,
  not a fixed repo-root `skills/` runtime path
- [X] Add an explicit platform path policy to `SKILL.md` that:
  - allows placeholder `.<platform>/skills/<skill-name>/` only for authoring,
    templates, and adapter examples
  - forbids treating the placeholder as runtime discovery
  - requires adapters or installers to resolve placeholders before execution
  - records the Codex projection mapping rule to
    `.agents/skills/<skill-name>/`
  - forbids hard-coding `skills/`, `.agents/skills/`, `.github/skills/`, or
    `.claude/skills/` as fixed runtime paths except when describing mappings
- [X] Keep skill-internal references package-relative, including
  `reference.md`, `examples.md`, and `templates/...`
- [X] Leave `skills/spec-docs-mvp-generator/reference.md` unchanged because it
  already avoids fixed runtime path claims and needs no extra policy sync for
  this bounded patch
- [X] Update this `step.md` from repo-visible truth only and do not claim
  reviewer completion or final gate completion

### `(Publisher) execute bounded pr-comment publish slice`

- [X] Confirm the publish scope is limited to this topic's implementation
  artifacts plus
  `plan/spec-docs-mvp-generator/spec-docs-mvp-generator.step.md`
- [X] Confirm the bounded publish work runs only in managed worktree
  `/Users/andrew/code/python/agent-skills.worktrees/agent-20260616-spec-docs-mvp-generator`
- [X] Record this `pr-comment` workflow slice in repo-visible truth before
  commit
- [X] Commit by topic on branch `feat/andrew/spec-docs-mvp-generator`
- [X] Push branch `feat/andrew/spec-docs-mvp-generator` to `origin`
- [X] Open a Ready PR to the repo default branch from repo-visible local
  evidence
- [X] Stop the next route at `wait human Merge or human feedback pr-comments`

## Handoff / Gate Notes

- Current progression truth includes the materialized `review-log.md`, but that
  file is evidence for the latest plan-review re-review only and must not be
  treated as implementation-review approval evidence.
- `plan/spec-docs-mvp-generator/spec-docs-mvp-generator.step.md` now exists as
  the required workflow progression artifact from requirement `R8`.
- One `needs-rework` plan-review verdict has already happened, so reviewer
  routing is now active for this topic.
- The exact repo-visible handoff path for that re-review loop is
  `plan/spec-docs-mvp-generator/spec-docs-mvp-generator.review-log.md`.
- The review-log handoff path has been materialized at
  `plan/spec-docs-mvp-generator/spec-docs-mvp-generator.review-log.md`, but
  its latest repo-visible verdict `approved` applies to plan review, not to
  implementation review for this progression-truth repair.
- The latest reviewer verdict for the bounded human minor patch is
  independently `approved`, and this `step.md` is the repo-visible workflow
  truth artifact carrying that implementation-review result.
- The earlier `needs-rework` implementation-review state has been superseded
  by the latest independent reviewer `approved` verdict for the bounded human
  minor patch.
- A later bounded human minor patch rework has now been applied to align
  `SKILL.md` with local-package reference semantics and explicit platform-path
  policy, while leaving canonical artifact layout and runtime decisions closed.
- `plan/spec-docs-mvp-generator/spec-docs-mvp-generator.review-log.md`
  remains plan-review evidence only and does not carry this implementation
  reviewer approval.
- The next allowed role for this implementation slice is `Planner final gate`.
- Independent implementation review for the bounded human minor patch is now
  complete at `approved`, but no final gate or human-check completion is
  claimed here.
- Canonical implementation artifacts now exist at:
  - `skills/spec-docs-mvp-generator/SKILL.md`
  - `skills/spec-docs-mvp-generator/reference.md`
  - `skills/spec-docs-mvp-generator/examples.md`
  - `skills/spec-docs-mvp-generator/templates/spec-template.md`
  - `skills/spec-docs-mvp-generator/templates/data-ownership-map-template.md`
- No publish, merge, or post-review final-gate progress has happened yet in
  repo-visible truth.
- The canonical implementation artifacts are present, and the implementation
  workflow progression truth is now `approved` for the bounded human minor
  patch, pending Planner final gate.
- This topic's bounded `pr-comment` publish scope is limited to:
  - `skills/spec-docs-mvp-generator/SKILL.md`
  - `skills/spec-docs-mvp-generator/reference.md`
  - `skills/spec-docs-mvp-generator/examples.md`
  - `skills/spec-docs-mvp-generator/templates/spec-template.md`
  - `skills/spec-docs-mvp-generator/templates/data-ownership-map-template.md`
  - `plan/spec-docs-mvp-generator/spec-docs-mvp-generator.step.md`
- The bounded publish work for this slice is executed only from managed
  worktree
  `/Users/andrew/code/python/agent-skills.worktrees/agent-20260616-spec-docs-mvp-generator`
  on branch `feat/andrew/spec-docs-mvp-generator`.
- Repo-visible local evidence shows `origin/HEAD` targets `origin/dev`, so the
  Ready PR base for this publish slice is `dev` unless later human direction
  explicitly changes it.
- This progression artifact records the `pr-comment` workflow publish slice as:
  `commit by topic -> push -> open ready PR -> wait human Merge or human
  feedback pr-comments`.
- After push and Ready PR creation, the next route for this topic is
  `wait human Merge or human feedback pr-comments`.
- This progression artifact does not define a separate draft-plan-commit gate
  and does not treat `.codex/**` as workflow authority.
- The frozen analysis artifacts remain prerequisites and must not be reopened
  unless a separate scope change is explicitly approved.
- This `*.step.md` is the workflow progression artifact only; it must be
  updated from repo-visible facts and must not be used to infer hidden
  approvals or completed gates.
