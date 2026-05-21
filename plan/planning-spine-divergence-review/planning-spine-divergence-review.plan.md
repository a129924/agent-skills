# planning-spine-divergence-review

## Goal / Outcome

- Decompose `plan-creator` and `plan-reviewer` divergence into bounded
  remediation units.
- Record overwrite risk area by area.
- Produce a report that can be used directly to author the later
  `planning-spine-bounded-remediation` topic.

## Scope

- **In scope**:
  - `analysis/planning-spine-divergence-review/requirements.md`
  - `plan/planning-spine-divergence-review/planning-spine-divergence-review.plan.md`
  - `docs/migration/planning-spine-divergence-review.md`
  - read-only inspection of:
    - `skills/plan-creator/`
    - `.github/skills/plan-creator/`
    - `skills/plan-reviewer/`
    - `.github/skills/plan-reviewer/`
    - `docs/migration/same-name-divergence-review.md`
    - `.codex/skills/README.md`
    - `.codex/skills/provenance.md`

- **Out of scope**:
  - any skill content edit
  - any overwrite or merge action
  - any `.codex/skills` change
  - business-intent same-name candidates
  - README / VERSION / tag updates

## Locked Decisions

- This topic is evidence-only.
- `plan-creator` and `plan-reviewer` remain high-sensitivity planning-spine
  surfaces in this topic.
- The report must prefer `recommended_authority_now: unresolved` over a weak
  overwrite recommendation.
- No bounded remediation is executed here.

## Status / Allowed Transitions

- **Current**: `review-ready`
- **Execution model**: planning + divergence decomposition complete; awaiting
  reviewer/planner publish check
- **Allowed transitions**:
  - `review-ready` -> `reviewer-in-progress`
  - `reviewer-in-progress` -> `approved`
  - `reviewer-in-progress` -> `needs-rework`
  - `needs-rework` -> `creator-in-progress`
  - `creator-in-progress` -> `review-ready`
  - `approved` -> `publish-in-progress`
  - `publish-in-progress` -> `pr-open`
  - `publish-in-progress` -> `merged`
  - `pr-open` -> `needs-rework`
  - `pr-open` -> `merged`
  - `merged` -> terminal

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Requirements baseline | `analysis/planning-spine-divergence-review/requirements.md` | Planning actor | Locks candidate set, difference areas, and stop conditions |
| Topic plan | `plan/planning-spine-divergence-review/planning-spine-divergence-review.plan.md` | Planning actor | Repo-visible execution contract |
| Divergence decision report | `docs/migration/planning-spine-divergence-review.md` | Planning actor | Area-by-area decision and risk table for planning-spine drift |
| Upstream divergence evidence | `docs/migration/same-name-divergence-review.md` | Existing repo artifact | Read-only source of the prior major-diff routing |

Artifact path notes:

- No writable skill path exists in this plan.
- If execution would require editing any planning-spine skill path, stop and
  re-plan as remediation.

## Implementation Steps

1. Reconfirm the major-diff status for `plan-creator` and `plan-reviewer`.
2. For each fixed difference area, record:
   - current behavior in `skills/`
   - current behavior in `.github/skills/`
   - risk if one side is force-overwritten
   - the bounded remediation unit that would resolve it later
   - the current authority recommendation, if any
3. Keep any unresolved high-risk row explicitly unresolved.
4. End with a short routing summary for the later remediation topic.

## Validation / Acceptance Checks

- The report covers both locked candidates.
- Every fixed difference area appears in the report.
- Every row has overwrite risk plus follow-up routing.
- No skill content path is changed.

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
