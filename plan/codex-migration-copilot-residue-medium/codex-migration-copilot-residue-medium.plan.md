# codex-migration-copilot-residue-medium

## Goal / Outcome

- Freeze the medium-residue candidate set.
- Produce a branch-local report for medium Copilot-residue skills.
- Prepare bounded workflow/contract remediation work for implementation.

## Scope

- **In scope**:
  - `analysis/codex-migration-copilot-residue-medium/requirements.md`
  - `plan/codex-migration-copilot-residue-medium/codex-migration-copilot-residue-medium.plan.md`
  - `docs/migration/codex-migration-copilot-residue-medium-report.md`
  - medium-residue candidate skills selected by evidence inside this branch

- **Out of scope**:
  - direct-move and low-residue skills
  - high-residue skills
  - runtime/tooling blocker repair
  - repo-wide cutover

## Locked Decisions

- This branch handles only class `B2. medium Copilot residue`.
- Allowed remediation may include bounded workflow and contract updates.
- Runtime/tooling blocker repair is excluded.
- Skills with strong platform-binding that exceed bounded remediation must leave
  this branch.
- This topic is review-ready-only with no stable-library release action.

## Boundaries / Exclusions

- Do not absorb blocker repair into medium-residue implementation.
- Do not repair repo-wide path semantics from this branch.
- Do not treat Copilot-specific reference extraction as medium remediation.

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

- Branch target: `feat/andrew/codex-migration-copilot-residue-medium`
- Base branch: `feat/andrew/codex-skills-spec-worktree`

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/codex-migration-copilot-residue-medium/codex-migration-copilot-residue-medium.plan.md` | Planning actor | Repo-visible execution contract for this branch topic |
| Requirements baseline | `analysis/codex-migration-copilot-residue-medium/requirements.md` | Planning actor | Branch-local classification baseline |
| Migration report | `docs/migration/codex-migration-copilot-residue-medium-report.md` | Implement Agent | Skill verdicts, remediation boundaries, and follow-up items |

Artifact path notes:

- This topic does not require `VERSION` changes.
- This topic does not require `README.md` changes before the candidate set is frozen.

## Implementation Steps

1. Collect candidate skills that fit the medium-residue class.
2. Freeze workflow/contract remediation boundaries for each skill.
3. Produce the branch-local report with explicit remediation and redirect rules.
4. Implement only the bounded medium-residue changes.

## Validation / Acceptance Checks

- Every skill has a medium-residue rationale.
- Runtime/tooling blockers are not absorbed into branch execution.
- High-residue candidates are redirected with explicit reasons.

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

- Exact medium-residue candidate skill list remains to be frozen by branch-local analysis.
