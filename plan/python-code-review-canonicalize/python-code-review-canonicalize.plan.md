# python-code-review-canonicalize

## Goal / Outcome

- Create `skills/python-code-review/` as the target-architecture canonical copy
  of the existing transition-era candidate.
- Preserve `.github/skills/python-code-review/` as the current compatibility
  and active skill surface during transition.
- Leave one repo-visible migration artifact that records the copied file set,
  preserved `.github/...` boundary, confirmed-blocker context, and deferred
  runtime/tooling lanes.

## Scope

- **In scope**:
  - `analysis/python-code-review-canonicalize/requirements.md`
  - `analysis/python-code-review-canonicalize/technical-spec.md`
  - `plan/python-code-review-canonicalize/python-code-review-canonicalize.plan.md`
  - `skills/python-code-review/`
  - `docs/migration/python-code-review-canonicalize.md`

- **Out of scope**:
  - `.github/skills/python-code-review/`
  - changing the sequencing gate away from `python-implementation-review`
  - changing tooling detection order or strict-mode escalation behavior
  - changing verdict mapping from `blocking` findings to `needs-rework`
  - changing cross-skill routing or quality-dimension ownership rules
  - `AGENTS.md`
  - `docs/repo-positioning.md`
  - `README.md`
  - `VERSION`
  - `.codex/*`
  - repo-wide migration checklist updates

## Locked Decisions

- This topic implements only the bounded canonical copy for
  `python-code-review`.
- `skills/` receives a new target-architecture copy at
  `skills/python-code-review/`.
- `.github/skills/python-code-review/` remains the transition-era compatibility
  surface and the active skill contract in this topic.
- The current transition-era review expectations remain live in this topic:
  - `python-code-review` still requires prior
    `python-implementation-review` approval
  - tooling detection still stops at the first positive match across
    `pyproject.toml`, `Makefile`, `README.md` / `CONTRIBUTING.md`, then fallback
  - strict-mode projects still escalate `Any`, missing annotations, and
    unjustified ignores per the current source contract
  - one or more `blocking` findings still produces `needs-rework`
- The canonical copy must include the full candidate surface:
  - `SKILL.md`
  - `examples.md`
  - `reference.md`
  - `references/anti-patterns.md`
  - `references/cross-skill-signposts.md`
  - `references/observability.md`
  - `references/test-quality.md`
  - `references/tooling-detection.md`
- Runtime/tooling blocker repair remains deferred to a separate future topic.

## Boundaries / Exclusions

- Do not edit `.github/skills/python-code-review/` in this topic.
- Do not change sequencing-gate behavior, tooling detection order, strict-mode
  severity calibration, or verdict behavior.
- Do not change `AGENTS.md`, `docs/repo-positioning.md`, `README.md`,
  `VERSION`, or `.codex/*`.
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

- Branch target: `feat/andrew/python-code-review-canonicalize`
- Base branch: `dev`
- This topic must not be reclassified into runtime/tooling repair or active-path
  cutover without a new plan.

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/python-code-review-canonicalize/python-code-review-canonicalize.plan.md` | Planning actor | Repo-visible execution contract |
| Requirements baseline | `analysis/python-code-review-canonicalize/requirements.md` | Planning actor | Locked single-candidate scope, copy boundary, and stop conditions |
| Technical baseline | `analysis/python-code-review-canonicalize/technical-spec.md` | Planning actor | Execution-facing copy rules, deferred blocker inventory, and verification contract |
| Migration report | `docs/migration/python-code-review-canonicalize.md` | Creator | Repo-visible copy result and deferred-runtime evidence |
| Target skill folder | `skills/python-code-review/` | Creator | New target-architecture canonical copy |
| Compatibility source | `.github/skills/python-code-review/` | Existing repo artifact | Read-only transition-era source to copy from and preserve |

## Implementation Steps

1. Verify the source inventory at `.github/skills/python-code-review/` still
   matches the file set frozen in the technical spec:
   - `SKILL.md`
   - `examples.md`
   - `reference.md`
   - `references/anti-patterns.md`
   - `references/cross-skill-signposts.md`
   - `references/observability.md`
   - `references/test-quality.md`
   - `references/tooling-detection.md`
2. Copy the current transition-era source content from
   `.github/skills/python-code-review/` into a new
   `skills/python-code-review/` target-architecture folder, preserving relative
   structure exactly.
3. Preserve current `.github/skills/python-code-review/` compatibility content
   without edits.
4. Write `docs/migration/python-code-review-canonicalize.md` with:
   - candidate name
   - source root
   - target root
   - copied file set
   - compatibility layer preserved
   - active path changed: no
   - confirmed-blocker context preserved
   - deferred runtime/tooling blocker lanes
5. Stop and re-plan if implementation requires:
   - editing `.github/skills/python-code-review/`
   - changing sequencing-gate, tooling, or verdict behavior
   - touching shared migration, governance, projection, or release surfaces

## Validation / Acceptance Checks

- Only the locked candidate is copied into `skills/`.
- `skills/python-code-review/` contains the full required surface, not only
  `SKILL.md`.
- `.github/skills/python-code-review/` remains present and unchanged.
- No artifact claims active cutover away from transition-era `.github/...`
  behavior.
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

- verify that the full candidate surface was copied, including `reference.md`
  and all five split references
- verify that `.github/skills/python-code-review/` was preserved unchanged
- verify that no artifact claims active cutover or sequencing / tooling /
  verdict cutover
- verify that confirmed-blocker context and deferred runtime/tooling lanes
  remain explicit

## Post-merge / release actions

- No repository release action is part of this topic.
- `merged` is terminal for this topic.
- Runtime-path migration, sequencing-gate redesign, tooling-detection redesign,
  verdict-policy transition, projection switching, and repo-wide path
  governance changes require separate later topics.
