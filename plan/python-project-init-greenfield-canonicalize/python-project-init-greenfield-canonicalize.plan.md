# python-project-init-greenfield-canonicalize

## Goal / Outcome

- Create `skills/python-project-init-greenfield/` as the target-architecture
  canonical copy of the existing transition-era candidate.
- Preserve `.github/skills/python-project-init-greenfield/` as the current
  compatibility and active skill surface during transition.
- Leave one repo-visible migration artifact that records the copied file set,
  preserved `.github/...` boundary, confirmed-blocker context, and deferred
  runtime/tooling lanes.

## Scope

- **In scope**:
  - `analysis/python-project-init-greenfield-canonicalize/requirements.md`
  - `analysis/python-project-init-greenfield-canonicalize/technical-spec.md`
  - `plan/python-project-init-greenfield-canonicalize/python-project-init-greenfield-canonicalize.plan.md`
  - `skills/python-project-init-greenfield/`
  - `docs/migration/python-project-init-greenfield-canonicalize.md`

- **Out of scope**:
  - `.github/skills/python-project-init-greenfield/`
  - changing required-skill deployment away from `.github/skills/`
  - changing `.github/skills-provenance.json` or `.github/copilot-instructions.md` output behavior
  - changing the canonical acceptance handoff path
  - `AGENTS.md`
  - `docs/repo-positioning.md`
  - `README.md`
  - `VERSION`
  - `.codex/*`
  - repo-wide migration checklist updates

## Locked Decisions

- This topic implements only the bounded canonical copy for
  `python-project-init-greenfield`.
- `skills/` receives a new target-architecture copy at
  `skills/python-project-init-greenfield/`.
- `.github/skills/python-project-init-greenfield/` remains the transition-era
  compatibility surface and the active skill contract in this topic.
- The current transition-era output expectations remain live in this topic:
  - required skills are still described as copied under `.github/skills/`
  - governance provenance is still described at `.github/skills-provenance.json`
  - placeholder guidance is still described for `.github/copilot-instructions.md`
  - acceptance still points to
    `python3 .github/skills/sense-env-scaffold/scripts/sense_env.py --mode acceptance --contract-file blueprint.md`
- The canonical copy must include the full candidate surface:
  - `SKILL.md`
  - `examples.md`
  - `references/baseline-generation-rules.md`
  - `references/blueprint-parsing-contract.md`
- Runtime/tooling blocker repair remains deferred to a separate future topic.

## Boundaries / Exclusions

- Do not edit `.github/skills/python-project-init-greenfield/` in this topic.
- Do not retarget required-skill deployment away from `.github/skills/`.
- Do not change provenance destination or placeholder Copilot-instructions destination.
- Do not retarget the acceptance handoff away from
  `.github/skills/sense-env-scaffold/scripts/sense_env.py`.
- Do not change `AGENTS.md`, `docs/repo-positioning.md`,
  `README.md`, `VERSION`, or `.codex/*`.
- If execution requires editing any path outside `Artifact Paths`, stop and
  re-plan instead of improvising.

## Status / Allowed Transitions

- **Current**: `planned`
- **Execution model**: branch-local bounded copy work first; no repository
  release or active-path cutover actions in this topic
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

- Branch target: `feat/andrew/python-project-init-greenfield-canonicalize`
- Base branch: `dev`
- This topic must not be reclassified into runtime/tooling repair or active-path
  cutover without a new plan.

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/python-project-init-greenfield-canonicalize/python-project-init-greenfield-canonicalize.plan.md` | Planning actor | Repo-visible execution contract |
| Requirements baseline | `analysis/python-project-init-greenfield-canonicalize/requirements.md` | Planning actor | Locked single-candidate scope, copy boundary, and stop conditions |
| Technical baseline | `analysis/python-project-init-greenfield-canonicalize/technical-spec.md` | Planning actor | Execution-facing copy rules, deferred blocker inventory, and verification contract |
| Migration report | `docs/migration/python-project-init-greenfield-canonicalize.md` | Creator | Repo-visible copy result and deferred-runtime evidence |
| Target skill folder | `skills/python-project-init-greenfield/` | Creator | New target-architecture canonical copy |
| Compatibility source | `.github/skills/python-project-init-greenfield/` | Existing repo artifact | Read-only transition-era source to copy from and preserve |

## Implementation Steps

1. Verify the source inventory at `.github/skills/python-project-init-greenfield/`
   still matches the file set frozen in the technical spec:
   - `SKILL.md`
   - `examples.md`
   - `references/baseline-generation-rules.md`
   - `references/blueprint-parsing-contract.md`
2. Copy the current transition-era source content from
   `.github/skills/python-project-init-greenfield/` into a new
   `skills/python-project-init-greenfield/` target-architecture folder,
   preserving relative structure exactly.
3. Preserve current `.github/skills/python-project-init-greenfield/`
   compatibility content without edits.
4. Write `docs/migration/python-project-init-greenfield-canonicalize.md` with:
   - candidate name
   - source root
   - target root
   - copied file set
   - compatibility layer preserved
   - active path changed: no
   - confirmed-blocker context preserved
   - deferred runtime/tooling blocker lanes
5. Stop and re-plan if implementation requires:
   - editing `.github/skills/python-project-init-greenfield/`
   - changing `.github/skills/` deployment, provenance destination, or
     Copilot placeholder destination
   - changing the acceptance handoff path
   - touching shared migration, governance, projection, or release surfaces

## Validation / Acceptance Checks

- Only the locked candidate is copied into `skills/`.
- `skills/python-project-init-greenfield/` contains the full required surface,
  not only `SKILL.md`.
- `.github/skills/python-project-init-greenfield/` remains present and unchanged.
- No artifact claims active cutover away from transition-era `.github/...` behavior.
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

- verify that the full candidate surface was copied, including both references
- verify that `.github/skills/python-project-init-greenfield/` was preserved unchanged
- verify that no artifact claims active cutover or downstream output-surface cutover
- verify that confirmed-blocker context and deferred runtime/tooling lanes remain explicit

## Post-merge / release actions

- No repository release action is part of this topic.
- `merged` is terminal for this topic.
- Runtime-path migration, `.github/...` output transition, projection switching,
  and repo-wide path governance changes require separate later topics.
