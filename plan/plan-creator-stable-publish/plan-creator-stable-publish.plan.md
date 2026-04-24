# Plan Creator Stable Publish Plan

## Goal / Outcome

Promote the already-approved and already-merged `plan-creator` skill into the
stable library.

When this topic is complete:

- `plan/plan-creator/plan-creator.plan.md` records the prior topic as `merged`
- `README.md` lists `plan-creator` in `## Current skills`
- `VERSION` is bumped from `0.15.0` to `0.16.0`
- the follow-up PR is merged
- annotated tag `v0.16.0` is created and pushed

## Scope

- **In scope**:
  - create this repo-visible follow-up topic plan
  - mark the prior `plan-creator` topic as `merged`
  - add `plan-creator` to `README.md`
  - bump `VERSION` to `0.16.0`
  - run the normal PR flow for this publish topic
  - create and push tag `v0.16.0` after merge

- **Out of scope**:
  - changing `.github/skills/plan-creator/` content
  - changing `.github/copilot-instructions.md`
  - changing `plan/agent-handoff-workflow.md`
  - writing release notes or GitHub Release prose
  - deleting old feature branches as part of this topic

## Locked Decisions

### 1. Topic type: stable-library publish and release only

- This is a follow-up topic for stable-library publication.
- It does **not** reopen `plan-creator` skill design.
- If a real skill-content defect is discovered, stop and create a separate
  corrective topic instead of expanding this publish topic.

### 2. Stable candidate is frozen input

- `.github/skills/plan-creator/` is treated as the approved artifact being
  promoted.
- This topic publishes that existing artifact; it does not revise its content.

### 3. README row is fixed

- Add this exact row to `README.md`:

  `| \`plan-creator\` | creates repo-visible topic plans with strict workflow, artifact, and stable-library timing contracts |`

- Position:
  - after `git-release-management`
  - before `python-naming`

### 4. Version and tag are fixed

- Current version baseline: `0.15.0`
- Bump direction: `MINOR`
- New version: `0.16.0`
- Release tag: `v0.16.0`
- Reason: `plan-creator` becomes a new stable skill and therefore adds a
  backward-compatible repository capability

### 5. Timing is fixed

- `README.md` and `VERSION` update at `publish-in-progress`
- tag creation happens in Phase 10 after merge
- This keeps stable-library file changes visible in the PR while preserving the
  actual release action for post-merge execution

### 6. Prior topic housekeeping is part of this follow-up

- `plan/plan-creator/plan-creator.plan.md` must move from `pr-open` to `merged`
  because PR `#19` is already merged on `dev`

## Boundaries / Exclusions

- Do not edit `.github/skills/plan-creator/` in this topic.
- Do not infer or change stable-library metadata outside this plan; update the
  plan first if publish or release intent changes.
- Do not fold branch-deletion cleanup into this topic; destructive cleanup stays
  separate from stable publication.
- Do not skip reviewer approval, planner contract alignment, PR review handling,
  or release-readiness checks.
- Do not treat tag creation as permission to bypass README / VERSION alignment.

## Status / Allowed Transitions

- **Current**: `released`
- **Execution model**: follow the canonical creator -> reviewer -> publish ->
  merge -> release path for a stable-library promotion topic
- **Allowed transitions**:
  - `planned` -> `creator-in-progress`
  - `creator-in-progress` -> `review-ready`
  - `review-ready` -> `reviewer-in-progress`
  - `reviewer-in-progress` -> `approved`
  - `reviewer-in-progress` -> `needs-rework`
  - `needs-rework` -> `creator-in-progress`
  - `approved` -> `creator-in-progress`
  - `approved` -> `publish-in-progress`
  - `publish-in-progress` -> `pr-open`
  - `publish-in-progress` -> `merged`
  - `pr-open` -> `needs-rework`
  - `pr-open` -> `merged`
  - `merged` -> `released`
  - `released` -> terminal

Routing notes:

- Use the standard Phase 4.5 planner contract alignment rule from
  `plan/agent-handoff-workflow.md`.
- If reviewer or planner alignment finds that `.github/skills/plan-creator/`
  needs substantive content changes, stop this topic and create a separate
  corrective topic rather than mutating the stable candidate here.
- If release gating fails because the README row, `VERSION`, or target tag is
  inconsistent, fix those publish surfaces inside this topic before tagging.

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/plan-creator-stable-publish/plan-creator-stable-publish.plan.md` | Planning actor | Repo-visible execution contract for this publish topic |
| Prior topic status record | `plan/plan-creator/plan-creator.plan.md` | Main Agent | Update the already-merged `plan-creator` topic to `merged` |
| Stable-library summary | `README.md` | Creator | Add the stable-library row for `plan-creator` |
| Repo version baseline | `VERSION` | Creator | Bump the repository version from `0.15.0` to `0.16.0` |

Artifact path notes:

- This topic does **not** modify `.github/skills/plan-creator/`,
  `.github/copilot-instructions.md`, or `plan/agent-handoff-workflow.md`.
- Tag `v0.16.0` is a release action, not a repo file path.
- The listed paths are an executable contract.
- If later work tries to change skill content or other repo-visible surfaces
  outside these paths, treat that as plan drift and stop for a separate topic.

## Stable library metadata

### README row

- Table: `## Current skills`
- Exact row:

  `| \`plan-creator\` | creates repo-visible topic plans with strict workflow, artifact, and stable-library timing contracts |`

- Position:
  - after `git-release-management`
  - before `python-naming`

### VERSION bump

- Current: `0.15.0`
- Direction: `MINOR`
- New: `0.16.0`
- Reason: new stable skill, non-breaking capability addition

### Timing

- README / VERSION timing: `publish-in-progress`
- Reason: the PR should show the exact stable-library surfaces being promoted
- Release action: create annotated tag `v0.16.0` in Phase 10 after merge

### Additional release metadata

- Tag style: annotated git tag with `v` prefix
- Release notes: no additional release-notes artifact in this topic

## Implementation Steps

### Creator Phase (after plan approval)

1. Confirm `plan-creator` is already merged on `dev` and treat the skill content
   as frozen input for this topic.
2. Update `plan/plan-creator/plan-creator.plan.md` so the prior topic status is
   `merged`.
3. Update `README.md` with the exact `plan-creator` row at the locked position.
4. Update `VERSION` from `0.15.0` to `0.16.0`.
5. Keep `.github/skills/plan-creator/` unchanged.

### Reviewer Phase (after creator delivers review-ready)

1. Verify this topic stayed inside its publish-only scope.
2. Verify `.github/skills/plan-creator/` did not change.
3. Verify the prior topic status now correctly says `merged`.
4. Verify the README row matches the exact locked text and position.
5. Verify the `VERSION` bump matches `0.15.0` -> `0.16.0` and the rationale is
   still a new stable skill.

### Main Agent publish and release flow

1. After reviewer approval and passing Phase 4.5 alignment, move this topic to
   `publish-in-progress`.
2. Stage:
   - `plan/plan-creator-stable-publish/plan-creator-stable-publish.plan.md`
   - `plan/plan-creator/plan-creator.plan.md`
   - `README.md`
   - `VERSION`
3. Commit, push, and open the publish PR against `dev`.
4. After merge, run post-merge local sync on `dev`.
5. Run the release gate for version `0.16.0` / tag `v0.16.0`.
6. Create and push annotated tag `v0.16.0`.

## Validation / Acceptance Checks

- `plan/plan-creator/plan-creator.plan.md` shows `**Current**: \`merged\``
- this follow-up topic plan contains all required workflow sections plus
  `## Stable library metadata`
- `README.md` contains the exact `plan-creator` row exactly once
- the new README row is placed after `git-release-management` and before
  `python-naming`
- `VERSION` equals `0.16.0`
- `.github/skills/plan-creator/` remains unchanged in this topic
- reviewer handoff stays a single JSON object
- tag `v0.16.0` does not already exist before release
- annotated tag `v0.16.0` exists after release and points at the merged publish
  commit on `dev`

## Reviewer Handoff

Reviewer should return one JSON object and focus on:

- whether this topic stayed publish-only
- whether the old topic status is correctly closed as `merged`
- whether the README row text and position match the locked metadata
- whether the version bump and release target stay aligned
- whether `.github/skills/plan-creator/` remained untouched

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

## Post-merge / release actions

1. After merge, run the normal post-merge local sync flow on `dev`.
2. Reconfirm the merged commit contains the locked README and `VERSION` changes.
3. Run release-readiness checks for version `0.16.0` and tag `v0.16.0`.
4. Create annotated tag `v0.16.0`.
5. Push the tag to origin.
6. Move this topic to `released`.

## Open Questions / Unresolved Items

- None. Version, tag, stable-library timing, and scope are locked for this topic.
