# python-project-retrofit-canonicalize

## Goal / Outcome

- Create `skills/python-project-retrofit/` as the target-architecture canonical
  copy of the existing transition-era candidate.
- Preserve `.github/skills/python-project-retrofit/` as the current
  compatibility and active runtime surface during transition.
- Leave one repo-visible migration artifact that records the copied file set,
  preserved runtime-path boundary, confirmed-blocker context, and deferred
  runtime/tooling blocker work.

## Scope

- **In scope**:
  - `analysis/python-project-retrofit-canonicalize/requirements.md`
  - `analysis/python-project-retrofit-canonicalize/technical-spec.md`
  - `plan/python-project-retrofit-canonicalize/python-project-retrofit-canonicalize.plan.md`
  - `skills/python-project-retrofit/`
  - `docs/migration/python-project-retrofit-canonicalize.md`

- **Out of scope**:
  - `.github/skills/python-project-retrofit/`
  - `sense-env-scaffold`
  - `python-project-init-greenfield`
  - acceptance-path replacement or aliasing
  - `AGENTS.md`
  - `docs/repo-positioning.md`
  - `README.md`
  - `VERSION`
  - `.codex/*`
  - repo-wide migration checklist updates

## Locked Decisions

- This topic implements only the bounded canonical copy for
  `python-project-retrofit`.
- `skills/` receives a new target-architecture copy at
  `skills/python-project-retrofit/`.
- `.github/skills/python-project-retrofit/` remains the transition-era
  compatibility surface and the active runtime command surface in this topic.
- The existing acceptance handoff through
  `python3 .github/skills/sense-env-scaffold/scripts/sense_env.py --mode acceptance --contract-file retrofit-plan.md`
  must remain the live runtime contract during this topic.
- The canonical copy must include the full executor candidate surface:
  - `SKILL.md`
  - `examples.md`
  - `references/retrofit-conflict-resolution.md`
  - `references/retrofit-plan-v2-contract.md`
  - `references/retrofit-safety-guidelines.md`
  - `references/sensing-delta-contract.md`
- Runtime/tooling blocker repair remains deferred to a separate future topic.
- Confirmed-blocker status is evidence context only; it does not widen this topic
  into blocker repair.
- Base branch is `dev` because that is the only verifiable local bootstrap base
  in the current repository snapshot.

## Boundaries / Exclusions

- Do not edit `.github/skills/python-project-retrofit/` in this topic.
- Do not retarget the acceptance handoff away from
  `.github/skills/sense-env-scaffold/scripts/sense_env.py`.
- Do not modify executor behavior, gate semantics, delta-report contract, or
  provenance semantics in this topic.
- Do not change `AGENTS.md`, `docs/repo-positioning.md`,
  `docs/migration/migration-runway-checklist.md`,
  `docs/migration/platform-coupling-inventory.md`, `.codex/skills/README.md`, or
  `.codex/skills/provenance.md`.
- If execution requires editing any path outside `Artifact Paths`, stop and
  re-plan instead of improvising.

## Status / Allowed Transitions

- **Current**: `planned`
- **Execution model**: follow the canonical creator -> reviewer -> publish ->
  merge path; this topic implements branch-local bounded copy work first and
  does not execute repository release or active-path cutover actions
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

- Branch target: `feat/andrew/python-project-retrofit-canonicalize`
- Base branch: `dev`
- This topic must not be reclassified into runtime/tooling repair or active-path
  cutover without a new plan.
- This topic is authored in strict alignment with:
  - `analysis/python-project-retrofit-canonicalize/requirements.md`
  - `analysis/python-project-retrofit-canonicalize/technical-spec.md`

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/python-project-retrofit-canonicalize/python-project-retrofit-canonicalize.plan.md` | Planning actor | Repo-visible execution contract |
| Requirements baseline | `analysis/python-project-retrofit-canonicalize/requirements.md` | Planning actor | Locked single-candidate scope, copy boundary, and stop conditions |
| Technical baseline | `analysis/python-project-retrofit-canonicalize/technical-spec.md` | Planning actor | Execution-facing copy rules, deferred blocker inventory, and verification contract |
| Migration report | `docs/migration/python-project-retrofit-canonicalize.md` | Creator | Repo-visible copy result and deferred-runtime evidence |
| Target skill folder | `skills/python-project-retrofit/` | Creator | New target-architecture canonical copy |
| Compatibility source | `.github/skills/python-project-retrofit/` | Existing repo artifact | Read-only transition-era source to copy from and preserve |
| Runtime blocker evidence | `docs/migration/platform-coupling-inventory.md` | Existing repo artifact | Read-only evidence for why runtime-path transition stays deferred |
| Runway checklist | `docs/migration/migration-runway-checklist.md` | Existing repo artifact | Read-only runway blocker classification source |

Artifact path notes:

- This topic does not modify `.github/skills/python-project-retrofit/`.
- This topic does not modify runtime/tooling callers or shared governance artifacts.
- This topic does not modify `.codex/*`, `README.md`, `VERSION`,
  `.github/copilot-instructions.md`, `AGENTS.md`, `docs/repo-positioning.md`, or
  checklist-wide migration trackers.
- If execution requires editing any other path, stop and repair this plan
  before continuing.

## Implementation Steps

1. Verify the source inventory at `.github/skills/python-project-retrofit/`
   still matches the file set frozen in the technical spec:
   - `SKILL.md`
   - `examples.md`
   - `references/retrofit-conflict-resolution.md`
   - `references/retrofit-plan-v2-contract.md`
   - `references/retrofit-safety-guidelines.md`
   - `references/sensing-delta-contract.md`
2. Copy the current transition-era source content from
   `.github/skills/python-project-retrofit/` into a new
   `skills/python-project-retrofit/` target-architecture folder, preserving
   relative structure exactly.
3. Preserve current `.github/skills/python-project-retrofit/` compatibility
   content without edits.
4. Write `docs/migration/python-project-retrofit-canonicalize.md` with:
   - candidate name
   - source root
   - target root
   - copied file set
   - compatibility layer preserved
   - active runtime path changed: no
   - confirmed-blocker context preserved
   - deferred runtime/tooling blocker lanes
5. Stop and re-plan if implementation requires:
   - editing `.github/skills/python-project-retrofit/`
   - changing acceptance handoff or executor behavior
   - retargeting runtime/tooling callers
   - touching shared migration, governance, projection, or release surfaces

## Validation / Acceptance Checks

- Only the locked candidate is copied into `skills/`.
- `skills/python-project-retrofit/` contains the full required executor surface,
  not only documentation files.
- `.github/skills/python-project-retrofit/` remains present and unchanged.
- No acceptance handoff path is changed away from
  `.github/skills/sense-env-scaffold/scripts/sense_env.py`.
- No runtime/tooling blocker repair, shared governance change, projection
  update, or release-surface edit is performed.
- The migration report states what was copied, what remained the compatibility
  layer, that confirmed-blocker context was preserved, and which blocker lanes
  stayed deferred.

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

Reviewer focus:

- verify that the full executor surface was copied, including all four
  references
- verify that `.github/skills/python-project-retrofit/` was preserved unchanged
- verify that no artifact claims active runtime-path cutover
- verify that confirmed-blocker context and deferred runtime/tooling blocker
  lanes remain explicit rather than silently omitted

## Post-merge / release actions

- No repository release action is part of this topic.
- `merged` is terminal for this topic.
- Runtime-path migration, acceptance-handoff rewrites, projection switching, and
  repo-wide path governance changes require separate later topics.

## Open Questions / Unresolved Items

- None at topic-bootstrap time.
- If later implementation reveals that creating the canonical copy requires
  runtime-path, downstream-caller, or shared-governance edits, stop and re-plan
  instead of widening this topic silently.
