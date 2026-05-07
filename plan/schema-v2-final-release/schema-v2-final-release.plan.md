# schema v2 final release

**Semantic warning**: `analysis/schema-v2-final-release/requirements.md` and `analysis/schema-v2-final-release/technical-spec.md` are both absent. This plan is authored without the optional analysis layer and uses the merged migration state on `feature/skill-migration-v1` as the planning baseline.

## Goal / Outcome

- Publish the completed schema v2 migration from `feature/skill-migration-v1` to `dev` through a final integration PR.
- Update human-facing release surfaces so the repository clearly reflects that all 45 stable skills are now schema v2 compliant.
- Release the repository as version `0.48.0` and create tag `v0.48.0` after the merge is complete and explicitly resumed.

## Scope

- **In scope**:
  - `plan/schema-v2-final-release/schema-v2-final-release.plan.md`
  - `README.md`
  - `VERSION`
  - final integration PR from `feature/skill-migration-v1` to `dev`
  - git tag `v0.48.0` as the release action after merge

- **Out of scope**:
  - `.github/skills/**`
  - `files/migration-tracker.md` content changes
  - additional schema migration work
  - governance-file edits such as `.github/copilot-instructions.md`, `agent-skill-creator`, `agent-skill-reviewer`, `agent-skill-template`, `folder-contract.md`, or `blueprint.md`
  - direct merge to `dev` without a PR

## Locked Decisions

- This topic is a **stable-library-affecting topic with release timing**.
- Final version for this migration release is **`0.48.0`**.
- Final git tag for this release is **`v0.48.0`**.
- This release should go through a **final PR**: `feature/skill-migration-v1` -> `dev`; do not bypass the PR with a direct merge.
- `README.md` must include complete human-facing release information for the schema v2 migration completion, not only a terse one-line summary.
- `files/migration-tracker.md` is already in the correct `45/45 complete` state and stays unchanged in this topic unless a new factual inconsistency is discovered.
- Release/tag actions occur only in Phase 10 after merge is complete and a new explicit human resume message is received.

## Boundaries / Exclusions

- Creator owns only the repo-visible draft changes in `README.md`, `VERSION`, and the plan file; creator must not self-approve.
- Reviewer owns only the independent verdict on the final release draft and plan alignment.
- Main Agent owns commit/push/PR creation, post-merge sync, tag creation, and release routing.
- Do not reopen already-merged migration topics or broaden this topic into further skill rewrites.
- Do not create the tag before the PR is merged into `dev`.
- Do not treat `feature/skill-migration-v1` being up to date as permission to skip the final PR lane.

## Status / Allowed Transitions

- **Current**: `planned`
- **Execution model**: plan-reviewer -> creator -> reviewer -> publish -> pr-open -> merged -> released
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

- Before any README/VERSION edit is treated as execution-ready, this topic plan should be sent to `plan-reviewer`.
- Use the standard Phase 4.5 planner-alignment rule after reviewer approval to confirm the changed file set still matches the locked artifact paths.
- STOP POINT 1 applies before commit / push / PR creation.
- STOP POINT 2 applies after merge handoff; release/tag work may resume only after a new explicit human message confirms merge completion and requests continuation.

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/schema-v2-final-release/schema-v2-final-release.plan.md` | Planning actor | Repo-visible execution contract for the final integration/release topic |
| Stable-library summary | `README.md` | Creator | Final human-facing migration completion summary and any required release-facing README updates |
| Repo version baseline | `VERSION` | Creator | Canonical version bump from `0.47.1` to `0.48.0` |

Artifact path notes:

- This topic does **not** modify `.github/copilot-instructions.md` or any skill folder.
- `files/migration-tracker.md` is intentionally excluded because it already reflects `45/45 complete`.
- If execution requires files outside the listed paths, stop and repair the plan before continuing.
- Note: this topic adds no new modifications to `.github/skills/**` or `files/migration-tracker.md`; those paths appear in the PR only because they are part of the accumulated migration history on the source branch, not because this topic's implementation steps touched them. Exception: tracker rows corrected under the plan's own locked-decision exception clause are permitted.

## Stable library metadata

- `README row`: no `Current skills` row changes; instead add a complete schema v2 migration completion summary in `README.md` that states all 45 stable skills are now migrated and points readers to the stable library context already listed there
- `VERSION bump`: `0.47.1` -> `0.48.0`
- `timing`: `README.md` and `VERSION` at `publish-in-progress`; git tag `v0.48.0` at `release`
- `rationale`: the repository now exposes a fully upgraded stable skill library with backward-compatible capability improvements across all existing stable skills, which fits a MINOR bump better than a PATCH wording/fix release
- `release notes`: PR description should summarize the completed 45-skill schema v2 migration, mention final deferred-skill closure via PR #63, and note that the tag is created only after merge + explicit resume

## Implementation Steps

1. Work on the dedicated final-release worktree for branch `release/schema-v2-final-integration`.
2. Send `plan/schema-v2-final-release/schema-v2-final-release.plan.md` to `/fleet @.github/skills/plan-reviewer/` and repair it if needed before creator work begins.
3. Send the approved plan to `/fleet @.github/skills/agent-skill-creator/` for the final release draft:
   - update `README.md` with complete migration-completion information
   - update `VERSION` to `0.48.0`
   - keep edits tightly scoped to the listed artifact paths
4. Send the creator result to `/fleet @.github/skills/agent-skill-reviewer/` for an independent verdict.
5. If reviewer returns `needs-rework`, route fixes back to creator and repeat reviewer pass until verdict is `approved`.
6. After approval, stop at STOP POINT 1 for explicit human authorization before commit, push, and final PR creation to `dev`.
7. After the PR merges and a new explicit human resume message arrives, perform post-merge sync and create tag `v0.48.0`.

## Validation / Acceptance Checks

- The final draft changes only the listed artifact paths.
- `plan-reviewer` accepts the topic plan before creator work starts.
- `README.md` clearly states the schema v2 migration is complete and uses complete human-facing wording rather than a terse placeholder.
- `VERSION` is exactly `0.48.0`.
- No skill folder, governance file, or tracker content changes are introduced in this topic.
- `agent-skill-reviewer` returns `approved`.
- Final PR target is `dev`, not another integration branch.
- Tag creation is deferred until after merge + explicit resume, not performed early.

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

## Post-merge / release actions

- After the final PR is merged into `dev`, stop and wait for a new explicit human resume message.
- On valid resume, run post-merge local sync for the release branch/worktree as needed.
- Create annotated or lightweight git tag `v0.48.0` according to the repository's existing tagging practice.
- Ensure local `dev` and `feature/skill-migration-v1` state are synchronized as appropriate for post-release cleanup.

## Open Questions / Unresolved Items

- None for planning. If creator finds that `README.md` needs broader structural changes than a scoped completion summary, stop and ask before widening the plan.
