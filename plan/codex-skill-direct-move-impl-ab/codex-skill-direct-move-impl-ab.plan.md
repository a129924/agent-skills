# codex-skill-direct-move-impl-ab

## Goal / Outcome

- Implement the 2 A-class direct-move skills and the 5 B-class rewritten
  semantic skills under `skills/`, using the committed
  `codex-skill-direct-move-ab` baseline as current truth.
- Stop the later `migration-implementation` run at
  `MIGRATION_STATUS_CONFIRMED`; do not commit, push, or open a PR inside that
  workflow.

## Scope

- **In scope**:
  - `skills/python-package-layout/`
  - `skills/python-library-architecture/`
  - `skills/python-plan-authoring/`
  - `skills/python-blueprint-authoring/`
  - `skills/python-pre-commit/`
  - `skills/python-pyproject-toolconfig/`
  - `skills/python-tdd-test-authoring/`
  - `analysis/codex-skill-direct-move-impl-ab/requirements.md`
  - `analysis/codex-skill-direct-move-impl-ab/technical-spec.md`
  - `plan/codex-skill-direct-move-impl-ab/codex-skill-direct-move-impl-ab.plan.md`
  - `plan/codex-skill-direct-move-impl-ab/codex-skill-direct-move-impl-ab.step.md`
  - `plan/codex-skill-direct-move-impl-ab/codex-skill-direct-move-impl-ab.summary.md`
  - `.workflow-runs/<run-id>/` for the later implementation workflow

- **Out of scope**:
  - any modification under `.github/skills/`
  - any C-class skill
  - `AGENTS.md`, `docs/repo-positioning.md`, and `docs/process/`
  - repo-wide cutover, active-path flip, publish, release, cleanup, or merge
    work

## Locked Decisions

- Topic name is locked to `codex-skill-direct-move-impl-ab`.
- Risk level is locked to `medium` unless a future planner explicitly re-plans.
- The committed `codex-skill-direct-move-ab` artifacts are hard prerequisites.
- `.github/skills/` is read-only source context for this topic.
- `skills/` is the only authorized skill-content output location.
- `plan/codex-skill-direct-move-impl-ab/codex-skill-direct-move-impl-ab.step.md`
  is required before the later implementation workflow begins.
- Overlay handling is unresolved; this plan records the blocker but does not
  invent overlay rules.
- This topic must stop at `MIGRATION_STATUS_CONFIRMED` and hand later publish
  actions to the publish workflow.

## Boundaries / Exclusions

- Do not treat this topic as permission to rewrite governance or workflow
  policy.
- Do not modify `.github/skills/` to keep source and target paths in sync.
- Do not widen this topic into candidate discovery or migration-program design.
- Do not classify overlay absence as a pass condition.
- Do not commit, push, or open a PR from this planning turn.

## Status / Allowed Transitions

- **Current**: `planned`
- **Planned target branch**: `feat/andrew/codex-skill-direct-move-impl-ab`
- **Planned worktree path**:
  `/Users/andrew/code/python/agent-skills.worktrees/agent-20260529-codex-skill-direct-move-impl-ab`
- **Allowed workflow transitions once launched**:
  - `READY_TO_IMPLEMENT` -> `IMPLEMENTED`
  - `IMPLEMENTED` -> `REVIEW_REQUESTED`
  - `REVIEW_REQUESTED` -> `REVIEW_PASSED`
  - `REVIEW_PASSED` -> `OVERLAY_GATES_REQUIRED`
  - `OVERLAY_GATES_REQUIRED` -> `OVERLAY_GATES_PASSED`
  - `OVERLAY_GATES_REQUIRED` -> `OVERLAY_GATES_BLOCKED`
  - `OVERLAY_GATES_REQUIRED` -> `OVERLAY_GATES_DEFERRED`
  - `OVERLAY_GATES_PASSED` -> `MIGRATION_STATUS_CONFIRMED`
  - `OVERLAY_GATES_BLOCKED` -> `HUMAN_FEEDBACK_REQUIRED`
  - `OVERLAY_GATES_DEFERRED` -> `MIGRATION_STATUS_CONFIRMED`

## Input Artifacts

These committed artifacts must be loaded before the later implementation run:

- `analysis/codex-skill-direct-move-ab/requirements.md`
- `analysis/codex-skill-direct-move-ab/technical-spec.md`
- `plan/codex-skill-direct-move-ab/codex-skill-direct-move-ab.plan.md`
- `plan/codex-skill-direct-move-ab/codex-skill-direct-move-ab.migration-checklist.md`
- `plan/codex-skill-direct-move-ab/codex-skill-direct-move-ab.summary.md`
- `docs/process/overlays/agent-skills-transition-overlay.md`

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Requirements baseline | `analysis/codex-skill-direct-move-impl-ab/requirements.md` | Planner | Repo-visible implementation-topic business boundary |
| Technical specification | `analysis/codex-skill-direct-move-impl-ab/technical-spec.md` | Planner | Execution-facing boundary for later implementation and review |
| Topic plan | `plan/codex-skill-direct-move-impl-ab/codex-skill-direct-move-impl-ab.plan.md` | Planner | Approved topic contract input for the later implementation workflow |
| Progression artifact | `plan/codex-skill-direct-move-impl-ab/codex-skill-direct-move-impl-ab.step.md` | Implementer / Main Agent | Required workflow progression truth |
| Launch summary | `plan/codex-skill-direct-move-impl-ab/codex-skill-direct-move-impl-ab.summary.md` | Planner / Main Agent | Pre-launch handoff truth for blockers and next-step routing |

## Implementation Steps

1. Re-load the committed `codex-skill-direct-move-ab` baseline and keep A/B
   membership frozen.
2. Implement the A-class direct-move skills in `skills/`:
   - `python-package-layout`
   - `python-library-architecture`
3. Implement the B-class rewritten semantic skills in `skills/`:
   - `python-plan-authoring`
   - `python-blueprint-authoring`
   - `python-pre-commit`
   - `python-pyproject-toolconfig`
   - `python-tdd-test-authoring`
4. Keep `.github/skills/` untouched and use it only as read-only source
   context.
5. Request independent review against this topic plan.
6. Route the repository-specific overlay gate for this topic according to
   `docs/process/overlays/agent-skills-transition-overlay.md`; if overlay
   binding or gate outcome remains unclear from repo-visible inputs, stop with
   `human-feedback-required`.
7. Record migration status with one of the allowed workflow outcomes and stop
   at `MIGRATION_STATUS_CONFIRMED`.

## Validation / Acceptance Checks

- `plan/codex-skill-direct-move-impl-ab/codex-skill-direct-move-impl-ab.step.md`
  exists before implementation progression advances.
- No file under `.github/skills/` is modified by the implementation topic.
- Only the 7 frozen A/B skills are implemented under `skills/`.
- A-class outputs preserve direct-move semantics without workflow-coupled
  contracts.
- B-class outputs preserve rewrite semantics while removing the frozen workflow
  couplings from the bootstrap baseline.
- No artifact claims the repository has already cut over to `skills/`.
- Overlay handling ends with a clear `passed`, `blocked`, or `deferred`
  conclusion; otherwise the workflow stops for human feedback.

## Review Handoff

Reviewer must judge:

- whether implementation stayed inside the frozen write set
- whether `.github/skills/` remained read-only
- whether each A/B skill outcome matches the frozen bootstrap intent
- whether overlay binding and overlay outcome were derived from repo-visible
  inputs and remained consistent with `AGENTS.md` and `docs/repo-positioning.md`

## Open Questions / Unresolved Items

- The target branch and worktree are planned but not created in this turn.
