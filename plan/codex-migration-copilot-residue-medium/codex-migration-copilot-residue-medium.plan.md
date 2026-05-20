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
  - `.github/skills/agent-skill-creator/`
  - `.github/skills/agent-skill-reviewer/`
  - `.github/skills/agent-skill-template/`
  - `.github/skills/worktree-manager/`

- **Out of scope**:
  - direct-move and low-residue skills
  - high-residue skills
  - runtime/tooling blocker repair
  - repo-wide cutover

## Locked Decisions

- This branch handles only class `B2. medium Copilot residue`.
- The candidate set is locked to:
  - `.github/skills/agent-skill-creator/`
  - `.github/skills/agent-skill-reviewer/`
  - `.github/skills/agent-skill-template/`
  - `.github/skills/worktree-manager/`
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

- **Current**: `approved`
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

- Branch target: `feat/andrew/codex-migration-copilot-residue-medium`
- Base branch: `feat/andrew/codex-skills-spec-worktree`
- Active execution stop point: `approved`
- `publish-in-progress`, `pr-open`, and `merged` remain listed only for
  canonical contract compatibility; they are not exercised in this topic

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/codex-migration-copilot-residue-medium/codex-migration-copilot-residue-medium.plan.md` | Planning actor | Repo-visible execution contract for this branch topic |
| Requirements baseline | `analysis/codex-migration-copilot-residue-medium/requirements.md` | Planning actor | Branch-local classification baseline |
| Migration report | `docs/migration/codex-migration-copilot-residue-medium-report.md` | Implement Agent | Skill verdicts, remediation boundaries, and follow-up items |
| Medium-residue skill | `.github/skills/agent-skill-creator/` | Implement Agent | Allowed medium-residue candidate path |
| Medium-residue skill | `.github/skills/agent-skill-reviewer/` | Implement Agent | Allowed medium-residue candidate path |
| Medium-residue skill | `.github/skills/agent-skill-template/` | Implement Agent | Allowed medium-residue candidate path |
| Medium-residue skill | `.github/skills/worktree-manager/` | Implement Agent | Allowed medium-residue candidate path |

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
- No post-merge action is expected inside this topic because active execution
  stops at `approved`.

## Open Questions / Unresolved Items

- No open candidate-list question remains; later changes require explicit
  reclassification.
