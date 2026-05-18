# codex-migration-direct-move

## Goal / Outcome

- Freeze the branch-local direct-move verification set.
- Produce a migration report for the direct-move class.
- Verify whether the promoted planning skills are already satisfied by the base
  branch instead of assuming that branch-local skill migration is still needed.

## Scope

- **In scope**:
  - `analysis/codex-migration-direct-move/requirements.md`
  - `plan/codex-migration-direct-move/codex-migration-direct-move.plan.md`
  - `docs/migration/codex-migration-direct-move-implement-agent-handoff.md`
  - `docs/migration/codex-migration-direct-move-report.md`
  - `skills/business-intent-alignment/`
  - `skills/business-to-technical-translation/`
  - `skills/plan-creator/`
  - `skills/plan-reviewer/`

- **Out of scope**:
  - residue-low / medium / high branches
  - Copilot-specific branches
  - runtime/tooling blocker repair
  - repo-wide cutover

## Locked Decisions

- This branch handles only class `A. direct move`.
- Confirmed runtime/tooling blockers are excluded from branch-local
  implementation here.
- The verification set is locked to:
  - `skills/business-intent-alignment/`
  - `skills/business-to-technical-translation/`
  - `skills/plan-creator/`
  - `skills/plan-reviewer/`
- The branch must produce explicit `already satisfied`, `no move required`, or
  `needs follow-up` decisions with reasons.
- The branch does not perform direct content migration for those four promoted
  planning skills unless the branch-local handoff contract is proven stale and
  is re-planned by the planner.
- This topic is review-ready-only with no stable-library release action.

## Boundaries / Exclusions

- Do not reclassify other migration branches from inside this topic.
- Do not repair creator/reviewer/template or runtime/tooling contracts here.
- Do not rewrite the four promoted planning skills as part of ordinary
  branch-local execution.
- Do not declare repo-wide active-path cutover from this branch.

## Status / Allowed Transitions

- **Current**: `pr-open`
- **Execution model**: follow the canonical creator -> reviewer -> publish ->
  merge path for contract compatibility; verification work for this topic is
  complete at `approved`, while branch packaging and PR handoff may continue
  afterward without widening the topic into skill migration
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
- Verification completion point: `approved`
- `publish-in-progress`, `pr-open`, and `merged` remain valid downstream branch
  packaging states after verification is complete; they do not authorize new
  branch-local skill migration work in this topic
- This topic should merge back into its feature branch line, not `dev`.

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/codex-migration-direct-move/codex-migration-direct-move.plan.md` | Planning actor | Repo-visible execution contract for this branch topic |
| Requirements baseline | `analysis/codex-migration-direct-move/requirements.md` | Planning actor | Branch-local classification baseline |
| Implement agent handoff | `docs/migration/codex-migration-direct-move-implement-agent-handoff.md` | Planning actor | Worktree path, reading order, and output-path contract for the implement agent |
| Migration report | `docs/migration/codex-migration-direct-move-report.md` | Implement Agent | Candidate verification verdicts and follow-up notes |
| Verification target | `skills/business-intent-alignment/` | Implement Agent | Read/verify target for direct-use readiness |
| Verification target | `skills/business-to-technical-translation/` | Implement Agent | Read/verify target for direct-use readiness |
| Verification target | `skills/plan-creator/` | Implement Agent | Read/verify target for direct-use readiness |
| Verification target | `skills/plan-reviewer/` | Implement Agent | Read/verify target for direct-use readiness |

Artifact path notes:

- This topic does not require `VERSION` changes.
- This topic does not require `README.md` changes before the candidate set is frozen.
- The four verification-target skill paths are read/verify scope by default, not
  writable migration targets.
- If execution drifts into branch-local skill migration, stop and repair the
  plan first.

## Implementation Steps

1. Verify the four promoted planning skills against current runway evidence and
   the migration base branch.
2. Classify each candidate as `already satisfied`, `no move required`, or
   `needs follow-up`.
3. Write the branch-local migration report with those verification verdicts and
   reasons.
4. Freeze the final direct-move report.
5. Do not perform branch-local skill migration unless the planner explicitly
   re-plans the topic.

## Validation / Acceptance Checks

- Every candidate skill has a verification verdict and evidence.
- No confirmed blocker is implemented in this branch.
- The report distinguishes `already satisfied`, `no move required`, and
  `needs follow-up`.
- No branch-local skill migration is performed under ordinary execution.

## Reviewer Handoff

```json
{
  "verdict": "approved",
  "blocking_issues": [],
  "copilot_feedback_triage": {
    "ADDRESS": [],
    "DISCUSS": [
      {
        "comment": "If later implementation expands beyond the four locked skill paths, update Artifact Paths and Requirements together before continuing.",
        "optional": true,
        "why": "The current contract is consistent, but this branch is especially sensitive to silent candidate-set growth."
      }
    ],
    "SKIP": []
  }
}
```

## Post-merge / release actions

- No repository release action is part of this topic.
- No post-merge action is expected inside this topic because active execution
  stops at `approved` after the report is complete.

## Open Questions / Unresolved Items

- No open candidate-list question remains; later changes require explicit
  reclassification or planner-directed replan.
