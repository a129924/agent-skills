# codex-migration-copilot-residue-low

## Goal / Outcome

- Freeze the low-residue candidate set.
- Produce a branch-local report for low Copilot-residue skills.
- Prepare bounded remediation work limited to low-residue cleanup.

## Scope

- **In scope**:
  - `analysis/codex-migration-copilot-residue-low/requirements.md`
  - `plan/codex-migration-copilot-residue-low/codex-migration-copilot-residue-low.plan.md`
  - `docs/migration/codex-migration-copilot-residue-low-report.md`
  - `.github/skills/git-commit-convention/`
  - `.github/skills/git-branch-naming/`

- **Out of scope**:
  - direct-move skills
  - medium/high residue skills
  - Copilot-specific branches
  - runtime/tooling blocker repair

## Locked Decisions

- This branch handles only class `B1. low Copilot residue`.
- The candidate set is locked to:
  - `.github/skills/git-commit-convention/`
  - `.github/skills/git-branch-naming/`
- Allowed remediation is limited to light wording, examples, projection notes,
  and local path cleanup.
- Any candidate needing workflow or contract redesign must leave this branch.
- This topic is review-ready-only with no stable-library release action.

## Boundaries / Exclusions

- Do not repair runtime/tooling blockers here.
- Do not treat creator/reviewer/template redesign as low-residue cleanup.
- Do not implement repo-wide cutover from this branch.

## Status / Allowed Transitions

- **Current**: `planned`
- **Execution model**: follow the canonical creator -> reviewer -> publish ->
  merge path for contract compatibility, but active execution for this topic
  stops at `approved`
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

- Branch target: `feat/andrew/codex-migration-copilot-residue-low`
- Base branch: `feat/andrew/codex-skills-spec-worktree`
- Active execution stop point: `approved`
- `publish-in-progress`, `pr-open`, and `merged` remain listed only for
  canonical contract compatibility; they are not exercised in this topic

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/codex-migration-copilot-residue-low/codex-migration-copilot-residue-low.plan.md` | Planning actor | Repo-visible execution contract for this branch topic |
| Requirements baseline | `analysis/codex-migration-copilot-residue-low/requirements.md` | Planning actor | Branch-local classification baseline |
| Migration report | `docs/migration/codex-migration-copilot-residue-low-report.md` | Implement Agent | Skill verdicts, remediation notes, and follow-up items |
| Low-residue skill | `.github/skills/git-commit-convention/` | Implement Agent | Allowed low-residue candidate path |
| Low-residue skill | `.github/skills/git-branch-naming/` | Implement Agent | Allowed low-residue candidate path |

Artifact path notes:

- This topic does not require `VERSION` changes.
- This topic does not require `README.md` changes before the candidate set is frozen.

## Implementation Steps

1. Collect candidate skills that fit the low-residue class.
2. Freeze the allowed remediation boundary for each skill.
3. Produce the branch-local report with explicit cleanup tasks.
4. Implement only the low-residue cleanup that remains inside the frozen scope.

## Validation / Acceptance Checks

- Every skill has a low-residue rationale.
- No workflow or contract redesign is hidden in branch implementation.
- Rejected candidates are redirected with explicit reasons.

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
- No post-merge action is expected inside this topic because active execution
  stops at `approved`.

## Open Questions / Unresolved Items

- No open candidate-list question remains; later changes require explicit
  reclassification.
