# sense-env-scaffold-canonicalize

## Goal / Outcome

- Create `skills/sense-env-scaffold/` as the target-architecture canonical copy
  of the existing transition-era candidate.
- Preserve `.github/skills/sense-env-scaffold/` as the current compatibility
  and active runtime surface during transition.
- Leave one repo-visible migration artifact that records the copied file set,
  preserved runtime-path boundary, and deferred runtime/tooling blocker work.

## Scope

- **In scope**:
  - `analysis/sense-env-scaffold-canonicalize/requirements.md`
  - `analysis/sense-env-scaffold-canonicalize/technical-spec.md`
  - `plan/sense-env-scaffold-canonicalize/sense-env-scaffold-canonicalize.plan.md`
  - `skills/sense-env-scaffold/`
  - `docs/migration/sense-env-scaffold-canonicalize.md`

- **Out of scope**:
  - `.github/skills/sense-env-scaffold/`
  - downstream caller rewrites in `python-project-init-greenfield`,
    `python-retrofit-plan-authoring`, `python-retrofit-plan-review`, or
    `python-project-retrofit`
  - runtime-path aliasing or cutover work
  - `AGENTS.md`
  - `docs/repo-positioning.md`
  - `README.md`
  - `VERSION`
  - `.codex/*`
  - repo-wide migration checklist updates

## Locked Decisions

- This topic implements only the bounded canonical copy for
  `sense-env-scaffold`.
- `skills/` receives a new target-architecture copy at
  `skills/sense-env-scaffold/`.
- `.github/skills/sense-env-scaffold/` remains the transition-era
  compatibility surface and the active runtime command surface in this topic.
- The existing executable path
  `.github/skills/sense-env-scaffold/scripts/sense_env.py` must remain the live
  runtime contract during this topic.
- The canonical copy must include the full executable candidate surface:
  - `SKILL.md`
  - `examples.md`
  - `references/`
  - `scripts/sense_env.py`
  - `scripts/sense_env_runtime/`
- Runtime/tooling blocker repair remains deferred to a separate future topic.
- Base branch is `dev` because that is the only verifiable local bootstrap base
  in the current repository snapshot.

## Boundaries / Exclusions

- Do not edit `.github/skills/sense-env-scaffold/` in this topic.
- Do not retarget any downstream caller away from
  `.github/skills/sense-env-scaffold/scripts/sense_env.py`.
- Do not modify `sense_env.py` behavior, assertion-kind support, manifest schema,
  or CLI semantics in this topic.
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

- Branch target: `feat/andrew/sense-env-scaffold-canonicalize`
- Base branch: `dev`
- This topic must not be reclassified into runtime/tooling repair or active-path
  cutover without a new plan.
- This topic is authored in strict alignment with:
  - `analysis/sense-env-scaffold-canonicalize/requirements.md`
  - `analysis/sense-env-scaffold-canonicalize/technical-spec.md`

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/sense-env-scaffold-canonicalize/sense-env-scaffold-canonicalize.plan.md` | Planning actor | Repo-visible execution contract |
| Requirements baseline | `analysis/sense-env-scaffold-canonicalize/requirements.md` | Planning actor | Locked single-candidate scope, copy boundary, and stop conditions |
| Technical baseline | `analysis/sense-env-scaffold-canonicalize/technical-spec.md` | Planning actor | Execution-facing copy rules, deferred blocker inventory, and verification contract |
| Migration report | `docs/migration/sense-env-scaffold-canonicalize.md` | Creator | Repo-visible copy result and deferred-runtime evidence |
| Target skill folder | `skills/sense-env-scaffold/` | Creator | New target-architecture canonical copy |
| Compatibility source | `.github/skills/sense-env-scaffold/` | Existing repo artifact | Read-only transition-era source to copy from and preserve |
| Runtime blocker evidence | `docs/migration/platform-coupling-inventory.md` | Existing repo artifact | Read-only evidence for why runtime-path transition stays deferred |
| Runway checklist | `docs/migration/migration-runway-checklist.md` | Existing repo artifact | Read-only runway blocker classification source |

Artifact path notes:

- This topic does not modify `.github/skills/sense-env-scaffold/`.
- This topic does not modify downstream caller plans or skills.
- This topic does not modify `.codex/*`, `README.md`, `VERSION`,
  `.github/copilot-instructions.md`, `AGENTS.md`, `docs/repo-positioning.md`, or
  checklist-wide migration trackers.
- If execution requires editing any other path, stop and repair this plan
  before continuing.

## Implementation Steps

1. Verify the source inventory at `.github/skills/sense-env-scaffold/` still
   matches the file set frozen in the technical spec:
   - `SKILL.md`
   - `examples.md`
   - `references/env-manifest-schema.md`
   - `references/sense-env-cli-contract.md`
   - `scripts/sense_env.py`
   - `scripts/sense_env_runtime/__init__.py`
   - `scripts/sense_env_runtime/contract.py`
   - `scripts/sense_env_runtime/models.py`
   - `scripts/sense_env_runtime/runtime.py`
2. Copy the current transition-era source content from
   `.github/skills/sense-env-scaffold/` into a new
   `skills/sense-env-scaffold/` target-architecture folder, preserving relative
   structure exactly.
3. Preserve current `.github/skills/sense-env-scaffold/` compatibility content
   without edits.
4. Write `docs/migration/sense-env-scaffold-canonicalize.md` with:
   - candidate name
   - source root
   - target root
   - copied file set
   - compatibility layer preserved
   - active runtime path changed: no
   - deferred runtime/tooling blocker lanes
5. Stop and re-plan if implementation requires:
   - editing `.github/skills/sense-env-scaffold/`
   - changing `sense_env.py` behavior
   - retargeting downstream callers
   - touching shared migration, governance, projection, or release surfaces

## Validation / Acceptance Checks

- Only the locked candidate is copied into `skills/`.
- `skills/sense-env-scaffold/` contains the full required executable surface,
  not only documentation files.
- `.github/skills/sense-env-scaffold/` remains present and unchanged.
- No downstream caller path is changed away from
  `.github/skills/sense-env-scaffold/scripts/sense_env.py`.
- No runtime/tooling blocker repair, shared governance change, projection
  update, or release-surface edit is performed.
- The migration report states what was copied, what remained the compatibility
  layer, and which blocker lanes stayed deferred.

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

- verify that the full executable surface was copied, including the runtime
  package
- verify that `.github/skills/sense-env-scaffold/` was preserved unchanged
- verify that no artifact claims active runtime-path cutover
- verify that deferred runtime/tooling blocker lanes remain explicit rather than
  silently omitted

## Post-merge / release actions

- No repository release action is part of this topic.
- `merged` is terminal for this topic.
- Runtime-path migration, downstream caller rewrites, projection switching, and
  repo-wide path governance changes require separate later topics.

## Open Questions / Unresolved Items

- None at topic-bootstrap time.
- If later implementation reveals that creating the canonical copy requires
  runtime-path, downstream-caller, or shared-governance edits, stop and re-plan
  instead of widening this topic silently.
