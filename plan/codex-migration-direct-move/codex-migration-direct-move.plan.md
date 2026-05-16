# codex-migration-direct-move

## Goal / Outcome

- Freeze the branch-local direct-move candidate set.
- Produce a migration report for the direct-move class.
- Prepare a bounded implementation path for skills that can move with minimal
  Codex-specific projection work and no blocker repair.

## Scope

- **In scope**:
  - `analysis/codex-migration-direct-move/requirements.md`
  - `plan/codex-migration-direct-move/codex-migration-direct-move.plan.md`
  - `docs/migration/codex-migration-direct-move-report.md`
  - direct-move candidate skills selected by evidence inside this branch

- **Out of scope**:
  - residue-low / medium / high branches
  - Copilot-specific branches
  - runtime/tooling blocker repair
  - repo-wide cutover

## Locked Decisions

- This branch handles only class `A. direct move`.
- Confirmed runtime/tooling blockers are excluded from migration execution here.
- Implementation starts only after the direct-move candidate set is frozen in
  the branch-local report.
- The branch must produce explicit `move` / `do-not-move` decisions with
  reasons.
- This topic is review-ready-only with no stable-library release action.

## Boundaries / Exclusions

- Do not reclassify other migration branches from inside this topic.
- Do not repair creator/reviewer/template or runtime/tooling contracts here
  unless a skill was explicitly misclassified as direct-move.
- Do not declare repo-wide active-path cutover from this branch.

## Status / Allowed Transitions

- **Current**: `planned`
- **Execution model**: follow the canonical creator -> reviewer -> publish ->
  merge path; stop this topic at branch-local review-ready or approved outputs
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
  - `merged` -> terminal

Routing notes:

- Branch target: `feat/andrew/codex-migration-direct-move`
- Base branch: `feat/andrew/codex-skills-spec-worktree`
- This topic should merge back into its feature branch line, not `dev`.

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/codex-migration-direct-move/codex-migration-direct-move.plan.md` | Planning actor | Repo-visible execution contract for this branch topic |
| Requirements baseline | `analysis/codex-migration-direct-move/requirements.md` | Planning actor | Branch-local classification baseline |
| Migration report | `docs/migration/codex-migration-direct-move-report.md` | Implement Agent | Candidate verdicts, move decisions, and follow-up notes |

Artifact path notes:

- This topic does not require `VERSION` changes.
- This topic does not require `README.md` changes before the candidate set is frozen.
- If implementation drifts outside the branch-local classification result, stop
  and repair the plan first.

## Implementation Steps

1. Collect candidate skills that plausibly fit the direct-move class.
2. Classify each candidate against repo dependency and blocker evidence.
3. Write the branch-local migration report with `move` / `do-not-move`
   decisions and reasons.
4. Freeze the final direct-move candidate set.
5. Implement only the migrations that remain inside the locked direct-move
   boundary.

## Validation / Acceptance Checks

- Every candidate skill has a verdict and evidence.
- No confirmed blocker is implemented in this branch.
- The report makes follow-up work explicit for rejected candidates.
- Branch-local implementation stays inside the frozen direct-move set.

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

- No repository release action is part of this topic.
- If approved, branch-local work may continue with implementation inside the
  frozen direct-move scope.

## Open Questions / Unresolved Items

- Exact candidate skill list remains to be frozen by branch-local analysis.
