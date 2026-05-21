# same-name-direct-canonicalize

## Goal / Outcome

- Record that `business-intent-alignment` and
  `business-to-technical-translation` are already equivalent across both
  surfaces.
- Freeze `skills/` as the canonical authority for those two candidates.
- Freeze `.github/skills/` as the transition-era compatibility mirror for
  those two candidates.

## Scope

- **In scope**:
  - `analysis/same-name-direct-canonicalize/requirements.md`
  - `plan/same-name-direct-canonicalize/same-name-direct-canonicalize.plan.md`
  - `docs/migration/same-name-direct-canonicalize.md`
  - read-only evidence from:
    - `docs/migration/same-name-divergence-review.md`
    - `docs/migration/codex-readability-baseline.md`
    - `.codex/skills/README.md`
    - `.codex/skills/provenance.md`

- **Out of scope**:
  - all skill content edits
  - all `.codex/skills` mutations
  - `plan-creator`
  - `plan-reviewer`
  - README / VERSION / tag updates

## Locked Decisions

- This topic is documentation-only.
- Both locked candidates are treated as already equivalent unless hidden diffs
  are discovered during validation.
- `skills/` is the canonical authority for both locked candidates.
- `.github/skills/` remains the transition-era compatibility mirror.
- This topic does not declare repo-wide active-path cutover complete.

## Status / Allowed Transitions

- **Current**: `planned`
- **Execution model**: planning + decision capture only
- **Allowed transitions**:
  - `planned` -> `creator-in-progress`
  - `creator-in-progress` -> `review-ready`
  - `review-ready` -> `reviewer-in-progress`
  - `reviewer-in-progress` -> `approved`
  - `reviewer-in-progress` -> `needs-rework`
  - `needs-rework` -> `creator-in-progress`
  - `approved` -> `publish-in-progress`
  - `publish-in-progress` -> `pr-open`
  - `publish-in-progress` -> `merged`
  - `pr-open` -> `needs-rework`
  - `pr-open` -> `merged`
  - `merged` -> terminal

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Requirements baseline | `analysis/same-name-direct-canonicalize/requirements.md` | Planning actor | Locks candidate set and stop conditions |
| Topic plan | `plan/same-name-direct-canonicalize/same-name-direct-canonicalize.plan.md` | Planning actor | Repo-visible execution contract |
| Decision report | `docs/migration/same-name-direct-canonicalize.md` | Planning actor | Final canonical-authority decision for the equivalent pair |
| Upstream divergence evidence | `docs/migration/same-name-divergence-review.md` | Existing repo artifact | Read-only proof that both candidates are equivalent and routed to direct canonicalization |

Artifact path notes:

- No writable skill path exists in this plan.
- If execution would require editing any candidate path, stop and re-plan.

## Implementation Steps

1. Reconfirm that the two locked candidates have no content diffs.
2. Reconfirm that `.codex/skills` currently reads both candidates from
   `skills/`.
3. Write a decision report that states:
   - the pair is already equivalent
   - no merge/overwrite is required
   - canonical authority is `skills/`
   - `.github/skills/` remains compatibility-only
   - active-path cutover is still not declared complete
4. Keep all existing skill and projection files unchanged.

## Validation / Acceptance Checks

- The report covers exactly the two locked candidates.
- Both rows state equivalence and canonical authority = `skills/`.
- The report explicitly preserves `.github/skills/` as compatibility-only.
- No file outside the three topic artifacts is changed.

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
