# codex-migration-copilot-specific

## Goal / Outcome

- Freeze the Copilot-specific candidate set.
- Produce a branch-local report that separates `reference-only` from
  `do-not-migrate` skills.
- Record confirmed-blocker status where repo-visible evidence requires it.
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
- Confirmed-blocker status must be preserved explicitly in the report when the
  evidence set marks a candidate as runtime/tooling-blocked.
- Confirmed-blocker status is report context only; it must not replace the
  final branch-local verdict vocabulary.
- The branch must not force implementation migration for Copilot-specific-only
  skills.
- The branch must not perform runtime/tooling blocker repair.
- This topic is review-ready-only with no stable-library release action.

## Boundaries / Exclusions

- Do not absorb portable migration work that belongs in another branch.
- Do not perform repo-wide cutover or blocker repair from this branch.
- Do not hide `do-not-migrate` conclusions behind vague future-work wording.
- Do not hide confirmed-blocker status behind a generic Copilot-specific label.
- Do not treat conceptual reuse or reusable references as migration approval.

## Status / Allowed Transitions

- **Current**: `pr-open`
- **Execution model**: follow the canonical creator -> reviewer -> publish ->
  merge path through branch-local report production and PR handling, without
  widening into blocker repair or migration implementation
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
- Current repo-visible state includes an open PR for this branch, so
  `publish-in-progress` and `pr-open` are exercised states for this topic

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/codex-migration-copilot-specific/codex-migration-copilot-specific.plan.md` | Planning actor | Repo-visible execution contract for this branch topic |
| Requirements baseline | `analysis/codex-migration-copilot-specific/requirements.md` | Planning actor | Branch-local classification baseline |
| Migration report | `docs/migration/codex-migration-copilot-specific-report.md` | Implement Agent | Candidate verdicts, blocker visibility, reusable references, and no-migrate decisions |
| Copilot-specific skill | `.github/skills/copilot-instructions-init/` | Implement Agent | Allowed read/verify candidate path for Copilot-specific and blocker-aware classification |

Artifact path notes:

- This topic does not require `VERSION` changes.
- This topic does not require `README.md` changes before the candidate set is frozen.

## Implementation Steps

1. Collect candidate skills that fit the Copilot-specific class.
2. Verify whether repo-visible migration evidence also marks the candidate as a
   confirmed blocker and record that result.
3. Freeze `reference-only` versus `do-not-migrate` verdicts for each skill.
4. Produce the branch-local report with blocker notes and reusable-reference
   notes where relevant.
5. Carry the report through branch-local publish / PR handling as needed, but
   do not execute blocker repair or migration implementation from this branch.

## Validation / Acceptance Checks

- Every candidate has a Copilot-specific verdict.
- `reference-only` versus `do-not-migrate` is explicit for each skill.
- Confirmed-blocker status is explicit when supported by repo-visible evidence.
- Confirmed-blocker status appears as report context, not as a third verdict.
- No forced migration implementation happens without reclassification.
- No blocker repair is executed from this branch.

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
- If this branch merges, only normal branch-local cleanup or handoff is in
  scope; blocker repair and migration implementation remain out of scope.

## Open Questions / Unresolved Items

- No open candidate-list question remains; later changes require explicit
  reclassification.
