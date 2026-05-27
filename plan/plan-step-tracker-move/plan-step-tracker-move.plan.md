# plan-step-tracker-move

## Goal / Outcome

- Move `plan-step-tracker` into `skills/` as a one-to-one canonical copy of the skill folder.
- Keep `step_tracker.py` as part of the skill content itself, moved alongside the skill documents and tests.
- Remove only copied-content platform binding from the `skills/` version; do not introduce any compatibility bridge.
- Record the move result and the intentionally narrow scope in a repo-visible migration artifact.

## Scope

- **In scope**:
  - `plan/plan-step-tracker-move/plan-step-tracker-move.plan.md`
  - `docs/migration/plan-step-tracker-move.md`
  - `docs/process/workflows/migration-implementation.workflow.md`
  - `skills/plan-step-tracker/`
- **Out of scope**:
  - `.codex/*`
  - `README.md`
  - `VERSION`
  - publish / commit / push / PR handling
  - repo-wide active-path cutover
  - any shim / compatibility engineering

## Locked Decisions

- Topic name: `plan-step-tracker-move`
- Target branch: `feat/andrew/plan-step-tracker-move`
- Base branch: `dev`
- Risk level: `high`
- `.github/skills/plan-step-tracker/` is the source folder for this move and remains unchanged in this topic.
- `skills/plan-step-tracker/` is a one-to-one canonical copy with only platform-bound path wording removed or rewritten for the new location.
- `step_tracker.py` is a skill-local asset and must be copied directly with the skill, not converted into a shim, forwarder, or wrapper.
- `importlib`-based dynamic loading, runtime bridging, or path-preserving compatibility layers are forbidden in this topic.
- `.codex/skills` is not part of this topic.

## Boundaries / Exclusions

- Do not redesign `plan-step-tracker` behavior.
- Do not modify `.github/skills/plan-step-tracker/` to add compatibility routing.
- Do not create a second maintained execution path for `step_tracker.py`.
- Do not modify unrelated runtime/tooling, governance, or publish surfaces.
- If implementation requires scope expansion beyond a skill-folder move, stop and re-plan.

## Status / Allowed Transitions

- **Current**: `planned`
- **Allowed transitions**:
  - `planned` -> `creator-in-progress`
  - `creator-in-progress` -> `review-ready`
  - `review-ready` -> `reviewer-in-progress`
  - `reviewer-in-progress` -> `approved`
  - `reviewer-in-progress` -> `needs-rework`
  - `needs-rework` -> `creator-in-progress`
  - `approved` -> `publish-in-progress`
  - `publish-in-progress` -> `pr-open`
  - `publish-in-progress` -> `merged`
  - `pr-open` -> `needs-rework`
  - `pr-open` -> `merged`
  - `merged` -> terminal

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/plan-step-tracker-move/plan-step-tracker-move.plan.md` | Planning actor | Repo-visible execution contract |
| Migration report | `docs/migration/plan-step-tracker-move.md` | Creator | Move result and narrowed migration rationale |
| Workflow contract update | `docs/process/workflows/migration-implementation.workflow.md` | Creator | Align generic implementation workflow to stop at publish handoff instead of publishing directly |
| Source skill folder | `.github/skills/plan-step-tracker/` | Existing repo artifact | Source material for the one-to-one move |
| Target skill folder | `skills/plan-step-tracker/` | Creator | Canonical copied skill folder |

## Implementation Steps

1. Restore `dev` to a clean baseline and keep formal topic work only in the managed worktree for `feat/andrew/plan-step-tracker-move`.
2. Rebuild `skills/plan-step-tracker/` as a full copy of `.github/skills/plan-step-tracker/`, including:
   - `SKILL.md`
   - `reference.md`
   - `examples.md`
   - `scripts/step_tracker.py`
   - `tests/test_step_tracker.py`
3. In the copied `skills/` version only, replace path text that still points to `.github/skills/plan-step-tracker/...` with the canonical `skills/plan-step-tracker/...` path.
4. Leave `.github/skills/plan-step-tracker/` unchanged; do not add or retain any shim, forwarder, importlib loader, or compatibility wrapper.
5. Write `docs/migration/plan-step-tracker-move.md` to record:
   - what was copied
   - that `step_tracker.py` moved as normal skill content
   - which platform-bound references were normalized in the copied version
   - which broader transition concerns remain deferred
6. Update `docs/process/workflows/migration-implementation.workflow.md` so the generic implementation workflow stops at `MIGRATION_STATUS_CONFIRMED` and hands off publish actions instead of performing them directly.
7. After each completed implementation step group, leave a progress summary containing:
   - `目前進度`
   - `下一步`
   - `human check / blocking`

## Validation / Acceptance Checks

- `dev` is clean after removing the mistaken first attempt.
- Topic changes exist only in the managed worktree for `feat/andrew/plan-step-tracker-move`.
- `.github/skills/plan-step-tracker/` remains free of shim / forwarder / `importlib` bridging.
- `skills/plan-step-tracker/scripts/step_tracker.py` is the copied local script asset, not a bridge.
- `skills/plan-step-tracker/` and `.github/skills/plan-step-tracker/` remain semantically aligned except for platform-bound path wording normalized in the copied version.
- Both source and copied test suites pass.
- No changes are made to `.codex/*`, `README.md`, `VERSION`, or other unrelated surfaces.

## Reviewer Handoff

```json
{
  "verdict": "approved|needs-rework",
  "blocking_issues": [],
  "copilot_feedback_triage": {
    "ADDRESS": [],
    "DISCUSS": [],
    "SKIP": []
  }
}
```

## Post-merge / Release

- This topic does not include publish execution.
- `merged` remains terminal for the topic workflow, but publish steps are deferred and not executed here.

## Assumptions

- `.github/skills/plan-step-tracker/` remains the current source-side transition artifact during this topic.
- A one-to-one canonical copy may still normalize path wording that is only meaningful in the source platform layout.
- The move does not itself resolve repo-wide active-path or projection questions.
