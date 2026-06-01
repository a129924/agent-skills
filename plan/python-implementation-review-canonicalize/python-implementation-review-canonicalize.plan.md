# python-implementation-review-canonicalize

## Goal / Outcome

- Create `skills/python-implementation-review/` as the target-architecture
  canonical copy of the existing transition-era candidate.
- Preserve `.github/skills/python-implementation-review/` as the current
  compatibility and active skill surface during transition.
- Leave one repo-visible migration artifact that records the copied file set,
  preserved `.github/...` boundary, confirmed-blocker context, and deferred
  runtime/tooling lanes.

## Scope

- **In scope**:
  - `analysis/python-implementation-review-canonicalize/requirements.md`
  - `analysis/python-implementation-review-canonicalize/technical-spec.md`
  - `plan/python-implementation-review-canonicalize/python-implementation-review-canonicalize.plan.md`
  - `skills/python-implementation-review/`
  - `docs/migration/python-implementation-review-canonicalize.md`

- **Out of scope**:
  - `.github/skills/python-implementation-review/`
  - changing approval proof requirements away from `python-plan-review`
  - changing `plan/<topic>/<topic>.step.md` gate semantics or pending-step detection
  - changing BLOCKED refusal behavior
  - changing sequencing between `python-implementation-review` and `python-code-review`
  - `AGENTS.md`
  - `docs/repo-positioning.md`
  - `README.md`
  - `VERSION`
  - `.codex/*`
  - repo-wide migration checklist updates

## Locked Decisions

- This topic implements only the bounded canonical copy for
  `python-implementation-review`.
- `skills/` receives a new target-architecture copy at
  `skills/python-implementation-review/`.
- `.github/skills/python-implementation-review/` remains the transition-era
  compatibility surface and the active skill contract in this topic.
- The current transition-era gate expectations remain live in this topic:
  - formal approval still comes from `python-plan-review`
  - optional step gating still resolves through `plan/<topic>/<topic>.step.md`
  - pending implementation steps still produce a BLOCKED plain-text refusal
  - `python-implementation-review` still runs before `python-code-review`
- The canonical copy must include the full candidate surface:
  - `SKILL.md`
  - `examples.md`
  - `reference.md`
  - `references/contract-deviation-rules.md`
  - `references/plan-section-structure.md`
  - `references/semantic-boundaries.md`
  - `references/traceability-status.md`
- Runtime/tooling blocker repair remains deferred to a separate future topic.

## Boundaries / Exclusions

- Do not edit `.github/skills/python-implementation-review/` in this topic.
- Do not change approval proof rules, step-gate rules, BLOCKED refusal behavior,
  or review sequencing.
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

- Branch target: `feat/andrew/python-implementation-review-canonicalize`
- Base branch: `dev`
- This topic must not be reclassified into runtime/tooling repair, approval-gate
  repair, or active-path cutover without a new plan.

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/python-implementation-review-canonicalize/python-implementation-review-canonicalize.plan.md` | Planning actor | Repo-visible execution contract |
| Requirements baseline | `analysis/python-implementation-review-canonicalize/requirements.md` | Planning actor | Locked single-candidate scope, copy boundary, and stop conditions |
| Technical baseline | `analysis/python-implementation-review-canonicalize/technical-spec.md` | Planning actor | Execution-facing copy rules, deferred blocker inventory, and verification contract |
| Migration report | `docs/migration/python-implementation-review-canonicalize.md` | Creator | Repo-visible copy result and deferred-runtime evidence |
| Target skill folder | `skills/python-implementation-review/` | Creator | New target-architecture canonical copy |
| Compatibility source | `.github/skills/python-implementation-review/` | Existing repo artifact | Read-only transition-era source to copy from and preserve |

## Implementation Steps

1. Verify the source inventory at `.github/skills/python-implementation-review/`
   still matches the file set frozen in the technical spec:
   - `SKILL.md`
   - `examples.md`
   - `reference.md`
   - `references/contract-deviation-rules.md`
   - `references/plan-section-structure.md`
   - `references/semantic-boundaries.md`
   - `references/traceability-status.md`
2. Copy the current transition-era source content from
   `.github/skills/python-implementation-review/` into a new
   `skills/python-implementation-review/` target-architecture folder,
   preserving relative structure exactly.
3. Preserve current `.github/skills/python-implementation-review/`
   compatibility content without edits.
4. Write `docs/migration/python-implementation-review-canonicalize.md` with:
   - candidate name
   - source root
   - target root
   - copied file set
   - compatibility layer preserved
   - active path changed: no
   - confirmed-blocker context preserved
   - deferred runtime/tooling blocker lanes
5. Stop and re-plan if implementation requires:
   - editing `.github/skills/python-implementation-review/`
   - changing approval proof, step-gate, refusal-output, or sequencing behavior
   - touching shared migration, governance, projection, or release surfaces

## Validation / Acceptance Checks

- Only the locked candidate is copied into `skills/`.
- `skills/python-implementation-review/` contains the full required surface,
  not only `SKILL.md`.
- `.github/skills/python-implementation-review/` remains present and unchanged.
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

- verify that the full candidate surface was copied, including `reference.md`
  and all four split references
- verify that `.github/skills/python-implementation-review/` was preserved unchanged
- verify that no artifact claims active cutover or gate-behavior cutover
- verify that confirmed-blocker context and deferred runtime/tooling lanes remain explicit

## Post-merge / release actions

- No repository release action is part of this topic.
- `merged` is terminal for this topic.
- Runtime-path migration, approval-gate redesign, step-gate redesign,
  review-sequencing transition, projection switching, and repo-wide path
  governance changes require separate later topics.
