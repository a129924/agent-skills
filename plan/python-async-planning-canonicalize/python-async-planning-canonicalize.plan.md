# python-async-planning-canonicalize

## Goal / Outcome

- Create `skills/python-async-planning/` as the target-architecture canonical
  copy of the existing transition-era candidate.
- Preserve `.github/skills/python-async-planning/` as the current compatibility
  and active skill surface during transition.
- Leave one repo-visible migration artifact that records the copied file set,
  preserved `.github/...` boundary, and deferred broader workflow repair.

## Scope

- **In scope**:
  - `analysis/python-async-planning-canonicalize/requirements.md`
  - `analysis/python-async-planning-canonicalize/technical-spec.md`
  - `plan/python-async-planning-canonicalize/python-async-planning-canonicalize.plan.md`
  - `skills/python-async-planning/`
  - `docs/migration/python-async-planning-canonicalize.md`

- **Out of scope**:
  - `.github/skills/python-async-planning/`
  - `AGENTS.md`
  - `docs/repo-positioning.md`
  - `README.md`
  - `VERSION`
  - `.codex/*`
  - repo-wide migration checklist updates

## Locked Decisions

- This topic implements only the bounded canonical copy for
  `python-async-planning`.
- `skills/` receives a new target-architecture copy at
  `skills/python-async-planning/`.
- `.github/skills/python-async-planning/` remains the transition-era
  compatibility surface and the active skill contract in this topic.
- The canonical copy must include the full skill surface:
  - `SKILL.md`
  - `reference.md`
  - `examples.md`
- Broader workflow and path-governance repair remains deferred to a separate future topic.

## Boundaries / Exclusions

- Do not edit `.github/skills/python-async-planning/` in this topic.
- Do not change async trigger / exemption semantics, subsection names, or
  contradiction-log handling.
- Do not change `AGENTS.md`, `docs/repo-positioning.md`, `README.md`,
  `VERSION`, or `.codex/*`.
- If execution requires editing any other path, stop and re-plan instead of improvising.

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

- Branch target: `feat/andrew/python-async-planning-canonicalize`
- Base branch: `dev`
- This topic must not be reclassified into workflow repair or active-path cutover without a new plan.

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/python-async-planning-canonicalize/python-async-planning-canonicalize.plan.md` | Planning actor | Repo-visible execution contract |
| Requirements baseline | `analysis/python-async-planning-canonicalize/requirements.md` | Planning actor | Locked single-candidate scope, copy boundary, and stop conditions |
| Technical baseline | `analysis/python-async-planning-canonicalize/technical-spec.md` | Planning actor | Execution-facing copy rules, deferred blocker inventory, and verification contract |
| Migration report | `docs/migration/python-async-planning-canonicalize.md` | Creator | Repo-visible copy result and deferred evidence |
| Target skill folder | `skills/python-async-planning/` | Creator | New target-architecture canonical copy |
| Compatibility source | `.github/skills/python-async-planning/` | Existing repo artifact | Read-only transition-era source to copy from and preserve |

## Implementation Steps

1. Verify the source inventory at `.github/skills/python-async-planning/`
   still matches the file set frozen in the technical spec:
   - `SKILL.md`
   - `reference.md`
   - `examples.md`
2. Copy the current transition-era source content from
   `.github/skills/python-async-planning/` into a new
   `skills/python-async-planning/` target-architecture folder, preserving
   relative structure exactly.
3. Preserve current `.github/skills/python-async-planning/` compatibility
   content without edits.
4. Write `docs/migration/python-async-planning-canonicalize.md` with:
   - candidate name
   - source root
   - target root
   - copied file set
   - compatibility layer preserved
   - active path changed: no
   - deferred workflow lanes
5. Stop and re-plan if implementation requires editing `.github/skills/python-async-planning/`
   or touching shared governance, projection, or release surfaces.

## Validation / Acceptance Checks

- Only the locked candidate is copied into `skills/`.
- `skills/python-async-planning/` contains the full required surface, not only `SKILL.md`.
- `.github/skills/python-async-planning/` remains present and unchanged.
- No artifact claims active cutover away from transition-era `.github/...` behavior.
- No workflow repair, shared governance change, projection update, or release-surface edit is performed.
- The migration report states what was copied and what remained the compatibility layer.

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

- verify that the full candidate surface was copied, including `reference.md`
  and `examples.md`
- verify that `.github/skills/python-async-planning/` was preserved unchanged
- verify that no artifact claims active cutover or async-rule redesign
- verify that deferred workflow lanes remain explicit

## Post-merge / release actions

- No repository release action is part of this topic.
- `merged` is terminal for this topic.
- Active-path migration, workflow-integration changes, and repo-wide path
  governance changes require separate later topics.
