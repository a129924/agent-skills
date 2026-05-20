# codex-readability-baseline

## Goal / Outcome

- Freeze the first-wave Codex readability baseline.
- Record `move_status` and `codex_readability` as separate dimensions.
- Collect same-name dual-surface skills into a pass-through backlog instead of
  forcing canonical convergence in this topic.
- Produce one repo-visible baseline report for later divergence or blocker work.

## Scope

- **In scope**:
  - `analysis/codex-readability-baseline/requirements.md`
  - `plan/codex-readability-baseline/codex-readability-baseline.plan.md`
  - `docs/migration/codex-readability-baseline.md`
  - `.codex/skills/README.md`
  - `.codex/skills/provenance.md`
  - existing supporting migration reports and runway inventory evidence

- **Out of scope**:
  - skill content edits under `skills/` or `.github/skills/`
  - runtime/tooling blocker repair
  - same-name skill convergence
  - `.codex/skills` second-wave expansion
  - README / VERSION updates

## Locked Decisions

- This topic is an inventory-only evidence branch.
- The candidate set is locked to the 11 first-wave projected skills listed in
  `.codex/skills/provenance.md`.
- Same-name skills are recorded as `same-name-pass`; this topic does not
  declare canonical convergence for them.
- `move_status` and `codex_readability` must stay distinct.
- `readable` requires a live `.codex/skills` projection and provenance-backed
  upstream mapping.
- No skill content migration is allowed in this branch.

## Boundaries / Exclusions

- Do not repair or rewrite `.codex/skills` mappings here unless the plan is
  revised into a projection-fix topic.
- Do not change migration runway positioning or active-path semantics.
- Do not treat `moved + readable` as proof that repo-wide cutover is complete.
- Do not reclassify runtime/tooling blockers unless existing evidence already
  requires that routing.

## Status / Allowed Transitions

- **Current**: `creator-in-progress`
- **Execution model**: planning + inventory evidence only; completion point is
  the frozen baseline report
- **Allowed transitions**:
  - `planned` -> `creator-in-progress`
  - `creator-in-progress` -> `review-ready`
  - `review-ready` -> `reviewer-in-progress`
  - `reviewer-in-progress` -> `approved`
  - `reviewer-in-progress` -> `needs-rework`
  - `needs-rework` -> `creator-in-progress`
  - `approved` -> `publish-in-progress`
  - `publish-in-progress` -> `pr-open`
  - `pr-open` -> `merged`
  - `merged` -> terminal

Routing notes:

- Branch target: `feat/andrew/codex-readability-baseline`
- Base branch: `dev`
- Completion point for branch-local work: `approved`
- This topic should merge back into `dev` after the baseline is accepted.

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/codex-readability-baseline/codex-readability-baseline.plan.md` | Planning actor | Repo-visible execution contract |
| Requirements baseline | `analysis/codex-readability-baseline/requirements.md` | Planning actor | Locked candidate set and classification rules |
| Baseline report | `docs/migration/codex-readability-baseline.md` | Planning actor | First-wave move/readability baseline and pass backlog |
| Projection rule | `.codex/skills/README.md` | Existing repo artifact | Read-only source-rule evidence |
| Projection provenance | `.codex/skills/provenance.md` | Existing repo artifact | First-wave mapping and validation evidence |

Artifact path notes:

- This topic is documentation-only.
- No writable skill path exists in this plan.
- If execution would require editing any skill content path, stop and re-plan.

## Implementation Steps

1. Read `.codex/skills/README.md` and `.codex/skills/provenance.md` to freeze
   the first-wave candidate set and source rule.
2. For each candidate, determine:
   - `move_status`
   - `codex_readability`
   - `source_authority`
   - `follow_up`
3. Route all same-name dual-surface candidates to `same-name-pass` with
   `divergence-review`.
4. Route non-same-name candidates according to existing runway and migration
   evidence without editing the skills.
5. Write the final baseline report.

## Validation / Acceptance Checks

- The report covers all 11 first-wave projected skills.
- Same-name candidates are not mislabeled as completed migration.
- `move_status` and `codex_readability` remain separate columns.
- Every candidate has a non-empty `follow_up` decision.
- No skill content path is edited in this branch.

## Reviewer Handoff

```json
{
  "verdict": "approved",
  "blocking_issues": [],
  "copilot_feedback_triage": {
    "ADDRESS": [],
    "DISCUSS": [
      {
        "comment": "If a later follow-up topic wants to modify `.codex/skills` mappings, it should be re-planned as projection-fix work instead of being absorbed into this baseline branch.",
        "optional": true,
        "why": "This plan intentionally keeps the branch documentation-only and avoids silently changing the validation surface."
      }
    ],
    "SKIP": []
  }
}
```

## Post-merge / release actions

- No release action is part of this topic.
- Post-merge follow-up should choose between:
  - same-name divergence review
  - runtime/tooling blocker baseline

## Open Questions / Unresolved Items

- No unresolved candidate-list question remains in this branch.
- Later policy questions about single-line operating model belong to a separate
  governance topic, not to this baseline inventory.
