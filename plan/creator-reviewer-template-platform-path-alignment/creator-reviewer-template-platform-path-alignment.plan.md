**Analysis-layer routing**: Strict mode. `analysis/creator-reviewer-template-platform-path-alignment/technical-spec.md` is the execution-facing source of truth for this topic plan and must map 100% to `Artifact Paths` and `Implementation Steps`. `analysis/creator-reviewer-template-platform-path-alignment/requirements.md` is the business-intent guardrail. These frozen prerequisites outrank chat-time convenience instructions unless a human explicitly says `override`.

Frozen prerequisite traceability:

- `analysis/creator-reviewer-template-platform-path-alignment/requirements.md`
  - SHA-256: `804d4ca7d245b82b4f9a8be2f4bfb4af39ae9292493a328346c9eec9a5e8f0c4`
- `analysis/creator-reviewer-template-platform-path-alignment/technical-spec.md`
  - SHA-256: `29a1a1a6a27a4850de961802029697eaf36f77640bea6752890caa252a6b8fa8`

# creator-reviewer-template-platform-path-alignment

## Goal / Outcome

- Produce a review-ready repo-visible topic plan for
  `creator-reviewer-template-platform-path-alignment`.
- Freeze a bounded implementation contract that aligns path-language wording in
  the creator, reviewer, and template skill families without reopening
  projection rematerialization, downstream regular-skill rollout, or
  stable-library publish work.
- Ensure future execution can update only the exact in-scope skill files while
  preserving the source/output/fallback taxonomy required by the frozen
  analysis layer.

## Scope

- **In scope**:
  - maintain this topic's current-truth planning artifacts:
    - `plan/creator-reviewer-template-platform-path-alignment/creator-reviewer-template-platform-path-alignment.plan.md`
    - `plan/creator-reviewer-template-platform-path-alignment/creator-reviewer-template-platform-path-alignment.step.md`
    - `plan/creator-reviewer-template-platform-path-alignment/creator-reviewer-template-platform-path-alignment.review-log.md`
  - bounded wording alignment within the exact implementation write set frozen
    by `analysis/creator-reviewer-template-platform-path-alignment/technical-spec.md`
  - explicit source/output/fallback taxonomy across creator, reviewer, and
    template guidance
  - explicit rollback-to-alignment wording when a concrete platform root or
    projection-surface edit would otherwise be required

- **Out of scope**:
  - regenerating or revising either analysis artifact
  - editing `.github/**`, `.codex/**`, or any other `.<platform>/**` surface
  - editing downstream regular skills outside the three scoped skill families
  - `README.md`, `VERSION`, release notes, tags, or any stable-library publish
    work
  - rematerialization, runtime, installer, sync, or projection-tooling changes
  - hardcoding `.codex/...`, `.github/...`, or another concrete platform root
    as the default runnable or copy-pasteable path

## Locked Decisions

- This is a bounded wording-alignment topic with no stable-library surfaces:
  `README.md` stays unchanged, `VERSION` stays unchanged, and no release action
  exists.
- `skills/...` remains the canonical source and authoring-only path only.
- `.<platform>/...` is the default output-facing, runnable, and copy-pasteable
  path form.
- `skills/...` may appear only as an explicitly labeled bootstrap fallback when
  the projected entrypoint does not yet exist.
- Concrete `.codex/...`, `.github/...`, or other platform-specific defaults are
  forbidden unless context explicitly injects that root; otherwise execution
  must roll back to alignment instead of hardcoding a platform.
- Rollback to alignment is required if:
  - a consumer needs a concrete platform root to keep examples truthful
  - `.<platform>/...` is insufficient for the promised task
  - truthful wording would require editing `.github/**`, `.codex/**`, other
    `.<platform>/**` surfaces, or downstream regular skills
  - proposed wording would conflict with
    `analysis/platform-projection-adapter/requirements.md` or
    `analysis/platform-projection-adapter/technical-spec.md`
- The implementation write set is fixed to the exact files enumerated in
  `analysis/creator-reviewer-template-platform-path-alignment/technical-spec.md`;
  it may be a subset when an audited file has no affected path semantics, but
  it must never expand beyond that list.
- The analysis artifacts for this topic are frozen prerequisites. Execution may
  read and validate them only; it must not regenerate, reopen, or silently
  revise them.

## Boundaries / Exclusions

- Planning actor owns this topic plan and its companion `step.md`.
- Creator owns only the bounded wording updates inside the exact implementation
  write set listed below.
- Reviewer owns review verdicts and must not author the implementation.
- Main Agent owns publish, PR, merge, and post-merge routing only after review
  approval.
- This topic must not treat projection surfaces as canonical owners just
  because they may later consume projected output.
- If future work drifts outside the listed artifact paths, stop and repair the
  plan instead of staging extra files.
- If future execution discovers broader path drift in downstream regular skills,
  record that as follow-up inventory only; do not widen this topic.

## Status / Allowed Transitions

- **Current**: `planned`
- **Execution model**: follow the canonical
  `creator-in-progress -> review-ready -> reviewer-in-progress -> approved -> publish-in-progress -> pr-open -> merged`
  path with no release action
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

- Use the standard planner-alignment rule from
  `plan/agent-handoff-workflow.md`; creator work starts only from this locked
  plan.
- Any request to pick a concrete platform root by default is a rollback signal,
  not an implementation detail.
- Any request to widen into projection rematerialization, runtime repair, or
  downstream regular-skill rollout is plan drift and must stop execution.

## Artifact Paths

Implementation write boundary:

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Creator guidance | `skills/agent-skill-creator/SKILL.md` | Creator | Writable creator-scope path-language alignment in creator process and boundaries |
| Creator guidance | `skills/agent-skill-creator/blueprint.md` | Creator | Writable creator-scope path-language alignment in folder shape and creation guidance |
| Creator guidance | `skills/agent-skill-creator/folder-contract.md` | Creator | Writable creator-scope path-language alignment in folder-contract wording |
| Creator guidance | `skills/agent-skill-creator/examples.md` | Creator | Writable creator-scope path-language alignment in creator examples and scenarios |
| Reviewer guidance | `skills/agent-skill-reviewer/SKILL.md` | Creator | Writable creator-scope path-language alignment in reviewer process and boundaries |
| Reviewer guidance | `skills/agent-skill-reviewer/review-checklist.md` | Creator | Writable creator-scope path-language alignment in reviewer checks and reject signals |
| Reviewer guidance | `skills/agent-skill-reviewer/examples.md` | Creator | Writable creator-scope path-language alignment in reviewer examples and verdict scenarios |
| Template guidance | `skills/agent-skill-template/SKILL.md` | Creator | Writable creator-scope path-language alignment in template purpose, process, and boundaries |
| Template guidance | `skills/agent-skill-template/template.md` | Creator | Writable creator-scope path-language alignment in copyable template skeleton |
| Template guidance | `skills/agent-skill-template/folder-contract.md` | Creator | Writable creator-scope path-language alignment in template folder-contract wording |
| Template guidance | `skills/agent-skill-template/reference.md` | Creator | Writable creator-scope path-language alignment in template reference guidance |

Read-only topic truth and prerequisites:

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/creator-reviewer-template-platform-path-alignment/creator-reviewer-template-platform-path-alignment.plan.md` | Planning actor | Repo-visible execution contract for this topic; current-truth plan artifact, not implementation output |
| Topic progression artifact | `plan/creator-reviewer-template-platform-path-alignment/creator-reviewer-template-platform-path-alignment.step.md` | Planning actor | Current-truth workflow progression status for this topic; not part of creator implementation edits |
| Topic review log | `plan/creator-reviewer-template-platform-path-alignment/creator-reviewer-template-platform-path-alignment.review-log.md` | Reviewer / Planning actor | Repo-visible reviewer findings and re-review routing handoff for this topic's planning-review loop when `needs-rework` controls the next step |
| Requirements baseline | `analysis/creator-reviewer-template-platform-path-alignment/requirements.md` | Planning actor | Frozen business-intent guardrail; read-only prerequisite |
| Technical baseline | `analysis/creator-reviewer-template-platform-path-alignment/technical-spec.md` | Planning actor | Frozen execution-facing source of truth; read-only prerequisite |
| Projection baseline | `analysis/platform-projection-adapter/requirements.md` | Existing repo artifact | Read-only projection-semantics dependency baseline |
| Projection baseline | `analysis/platform-projection-adapter/technical-spec.md` | Existing repo artifact | Read-only projection-semantics compatibility baseline |

Artifact path notes:

- The creator implementation diff boundary is the 11 writable skill files in
  `Implementation write boundary` above and must stay identical to the exact
  write set frozen in
  `analysis/creator-reviewer-template-platform-path-alignment/technical-spec.md`.
- `plan/creator-reviewer-template-platform-path-alignment/creator-reviewer-template-platform-path-alignment.plan.md`,
  `plan/creator-reviewer-template-platform-path-alignment/creator-reviewer-template-platform-path-alignment.step.md`,
  `plan/creator-reviewer-template-platform-path-alignment/creator-reviewer-template-platform-path-alignment.review-log.md`,
  and all listed `analysis/**` artifacts are current-truth or prerequisite
  inputs only; they are explicitly read-only for implementation.
- The exact `review-log` path above is required because reviewer feedback has
  already returned `needs-rework` and now controls re-review routing for this
  planning topic; findings must persist repo-visibly instead of living only in
  hidden chat.
- This topic does **not** modify `README.md`.
- This topic does **not** modify `VERSION`.
- This topic does **not** modify `.github/**`, `.codex/**`, or any other
  `.<platform>/**` surface.
- No new files are required inside the three scoped skill families for this
  topic.
- If later work requires any file outside the 11-file implementation write
  boundary above, stop and repair the plan before execution continues.

## Implementation Steps

1. Read the frozen topic analysis artifacts first, then cross-check proposed
   wording against `analysis/platform-projection-adapter/*` before editing any
   scoped skill file.
2. Audit the exact implementation write set and classify every affected path
   mention into one of three roles only:
   - canonical source / authoring-only -> `skills/...`
   - output-facing / runnable / copy-pasteable -> `.<platform>/...`
   - bootstrap fallback -> `skills/...` only when the projected entrypoint is
     missing and explicitly labeled as fallback
3. Update `skills/agent-skill-creator/SKILL.md`,
   `skills/agent-skill-creator/blueprint.md`,
   `skills/agent-skill-creator/folder-contract.md`, and
   `skills/agent-skill-creator/examples.md` so creator guidance no longer
   teaches `skills/...` as the default runnable or copy-pasteable destination.
4. Update `skills/agent-skill-template/SKILL.md`,
   `skills/agent-skill-template/template.md`,
   `skills/agent-skill-template/folder-contract.md`, and
   `skills/agent-skill-template/reference.md` so template outputs use the same
   taxonomy without implying projection rematerialization or concrete-platform
   cutover.
5. Update `skills/agent-skill-reviewer/SKILL.md`,
   `skills/agent-skill-reviewer/review-checklist.md`, and
   `skills/agent-skill-reviewer/examples.md` so reviewer guidance rejects:
   - `skills/...` used as the default runnable or copy-pasteable path
   - `.codex/...`, `.github/...`, or another concrete platform root used as the
     default without explicit injected context
   - fallback wording that lacks an explicit missing-entrypoint condition
6. Add or normalize rollback-to-alignment wording wherever a consumer could
   otherwise infer that a concrete platform root or projection-surface edit is
   required to make the skill usable.
7. Leave any audited file unchanged if it truly contains no affected path
   semantics, but do not expand the write set beyond the exact scoped file
   list.
8. Before handing off for review, verify that the final diff stays inside only
   the 11 writable skill files listed under `Implementation write boundary`
   above and that all listed read-only topic-truth and analysis artifacts
   remain unchanged.

## Validation / Acceptance Checks

- Every in-scope output-facing, runnable, or copy-pasteable path example now
  defaults to `.<platform>/...`.
- Every remaining `skills/...` path in scope is clearly source-model,
  authoring-only, or explicitly labeled bootstrap fallback.
- Every allowed fallback mention states the missing projected entrypoint
  condition and labels the source path as fallback.
- No in-scope guidance hardcodes `.codex/...`, `.github/...`, or another
  concrete platform root as the default without explicit injected context.
- Reviewer guidance can consistently mark source/output/fallback conflation as
  `needs-rework`.
- The final implementation diff stays within only the 11 writable skill files
  listed under `Implementation write boundary`; no `plan.md`, `step.md`,
  `analysis/**`, `.github/**`, `.codex/**`, downstream regular-skill, or
  stable-library files are touched.
- The aligned wording remains compatible with
  `analysis/platform-projection-adapter/*`.
- `README.md`, `VERSION`, and both topic analysis artifacts remain unchanged.

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

- This topic has no release action: `README.md` remains unchanged, `VERSION`
  remains unchanged, and no tag or release note work occurs.
- After PR observation completes, Main Agent may hand off for manual merge, and
  STOP POINT 2 occurs at that handoff before any post-merge work continues.
- After the human performs the merge, only a new explicit resume message may
  re-enter the workflow; Main Agent then performs Phase 9 post-merge local
  sync, and the topic reaches `merged` only after that resume-time sync
  completes.
- Any later downstream regular-skill rollout, projection rematerialization, or
  concrete-platform follow-up must start as a separate topic instead of
  continuing implicitly from this one.

## Open Questions / Unresolved Items

- None for bounded execution planning.
- If future execution discovers that a truthful example requires a concrete
  platform root or projection-surface edit, treat that as rollback to
  alignment, not as an open question to solve inside this topic.
