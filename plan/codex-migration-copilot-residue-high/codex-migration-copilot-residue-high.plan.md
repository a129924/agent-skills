# codex-migration-copilot-residue-high

## Goal / Outcome

- Freeze the high-residue candidate set.
- Produce a branch-local report for high Copilot-residue skills.
- Prepare bounded redesign-oriented implementation planning where appropriate.

## Scope

- **In scope**:
  - `analysis/codex-migration-copilot-residue-high/requirements.md`
  - `plan/codex-migration-copilot-residue-high/codex-migration-copilot-residue-high.plan.md`
  - `docs/migration/codex-migration-copilot-residue-high-report.md`
  - high-residue candidate skills selected by evidence inside this branch

- **Out of scope**:
  - direct-move and low/medium residue skills
  - Copilot-specific-only skills
  - runtime/tooling blocker repair
  - repo-wide cutover

## Locked Decisions

- This branch handles only class `B3. high Copilot residue`.
- The branch may analyze redesign paths but must not hide Copilot-specific-only
  conclusions.
- Runtime/tooling blocker repair remains out of scope.
- Implementation can proceed only after each skill has a branch-local redesign,
  defer, or reclassify verdict.
- This topic is review-ready-only with no stable-library release action.

## Boundaries / Exclusions

- Do not convert high-residue analysis into repo-wide cutover work.
- Do not absorb runtime/tooling transition work here.
- Do not force Copilot-specific skills into migration if evidence says
  reference-only or no-migrate.

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

- Branch target: `feat/andrew/codex-migration-copilot-residue-high`
- Base branch: `feat/andrew/codex-skills-spec-worktree`

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/codex-migration-copilot-residue-high/codex-migration-copilot-residue-high.plan.md` | Planning actor | Repo-visible execution contract for this branch topic |
| Requirements baseline | `analysis/codex-migration-copilot-residue-high/requirements.md` | Planning actor | Branch-local classification baseline |
| Migration report | `docs/migration/codex-migration-copilot-residue-high-report.md` | Implement Agent | Skill verdicts, redesign paths, and follow-up items |

Artifact path notes:

- This topic does not require `VERSION` changes.
- This topic does not require `README.md` changes before the candidate set is frozen.

## Implementation Steps

1. Collect candidate skills that fit the high-residue class.
2. Freeze redesign / defer / reclassify verdicts for each skill.
3. Produce the branch-local report with explicit redesign boundaries.
4. Implement only the work that remains inside the frozen high-residue scope.

## Validation / Acceptance Checks

- Every skill has a high-residue rationale.
- Copilot-specific-only skills are not forced through redesign.
- Blocker interactions are visible in the report.

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

## Open Questions / Unresolved Items

- Exact high-residue candidate skill list remains to be frozen by branch-local analysis.
