# codex-migration-copilot-specific

## Goal / Outcome

- Freeze the Copilot-specific candidate set.
- Produce a branch-local report that separates `reference-only` from
  `do-not-migrate` skills.
- Prepare bounded follow-up work only where conceptual reuse is justified.

## Scope

- **In scope**:
  - `analysis/codex-migration-copilot-specific/requirements.md`
  - `plan/codex-migration-copilot-specific/codex-migration-copilot-specific.plan.md`
  - `docs/migration/codex-migration-copilot-specific-report.md`
  - `.github/skills/copilot-instructions-init/`

- **Out of scope**:
  - direct-move and residue branches
  - runtime/tooling blocker repair
  - repo-wide cutover

## Locked Decisions

- This branch handles only class `C. Copilot-specific`.
- The candidate set is locked to:
  - `.github/skills/copilot-instructions-init/`
- Every candidate must end as `reference-only` or `do-not-migrate` unless
  branch-local evidence supports reclassification.
- The branch must not force implementation migration for Copilot-specific-only
  skills.
- This topic is review-ready-only with no stable-library release action.

## Boundaries / Exclusions

- Do not absorb portable migration work that belongs in another branch.
- Do not perform repo-wide cutover or blocker repair from this branch.
- Do not hide `do-not-migrate` conclusions behind vague future-work wording.

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

- Branch target: `feat/andrew/codex-migration-copilot-specific`
- Base branch: `feat/andrew/codex-skills-spec-worktree`
- Active execution stop point: `approved`
- `publish-in-progress`, `pr-open`, and `merged` remain listed only for
  canonical contract compatibility; they are not exercised in this topic

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/codex-migration-copilot-specific/codex-migration-copilot-specific.plan.md` | Planning actor | Repo-visible execution contract for this branch topic |
| Requirements baseline | `analysis/codex-migration-copilot-specific/requirements.md` | Planning actor | Branch-local classification baseline |
| Migration report | `docs/migration/codex-migration-copilot-specific-report.md` | Implement Agent | Candidate verdicts, reusable references, and no-migrate decisions |
| Copilot-specific skill | `.github/skills/copilot-instructions-init/` | Implement Agent | Allowed Copilot-specific candidate path |

Artifact path notes:

- This topic does not require `VERSION` changes.
- This topic does not require `README.md` changes before the candidate set is frozen.

## Implementation Steps

1. Collect candidate skills that fit the Copilot-specific class.
2. Freeze `reference-only` versus `do-not-migrate` verdicts for each skill.
3. Produce the branch-local report with reusable-reference notes where relevant.
4. Implement only follow-up work that stays inside the frozen branch-local
   boundary.

## Validation / Acceptance Checks

- Every candidate has a Copilot-specific verdict.
- `reference-only` versus `do-not-migrate` is explicit for each skill.
- No forced migration implementation happens without reclassification.

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
