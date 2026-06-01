# copilot-instructions-init-canonicalize

## Goal / Outcome

- Create `skills/copilot-instructions-init/` as the target-architecture
  canonical copy of the existing transition-era candidate.
- Preserve `.github/skills/copilot-instructions-init/` as the current
  compatibility and active skill surface during transition.
- Leave one repo-visible migration artifact that records the copied file set,
  preserved `.github/...` boundary, confirmed-blocker context, and deferred
  runtime/tooling lanes.

## Scope

- **In scope**:
  - `analysis/copilot-instructions-init-canonicalize/requirements.md`
  - `analysis/copilot-instructions-init-canonicalize/technical-spec.md`
  - `plan/copilot-instructions-init-canonicalize/copilot-instructions-init-canonicalize.plan.md`
  - `skills/copilot-instructions-init/`
  - `docs/migration/copilot-instructions-init-canonicalize.md`

- **Out of scope**:
  - `.github/skills/copilot-instructions-init/`
  - changing the target output destination away from target-project `.github/copilot-instructions.md`
  - changing stale-fact fingerprints or `.github/skills/` summary coupling
  - changing managed-block or overwrite / keep / manual-merge behavior
  - `AGENTS.md`
  - `docs/repo-positioning.md`
  - `README.md`
  - `VERSION`
  - `.codex/*`
  - repo-wide migration checklist updates

## Locked Decisions

- This topic implements only the bounded canonical copy for
  `copilot-instructions-init`.
- `skills/` receives a new target-architecture copy at
  `skills/copilot-instructions-init/`.
- `.github/skills/copilot-instructions-init/` remains the transition-era
  compatibility surface and the active skill contract in this topic.
- The current transition-era output expectations remain live in this topic:
  - the skill still targets target-project `.github/copilot-instructions.md`
  - stale-fact validation still uses Git `HEAD`, `pyproject.toml` / `uv.lock`,
    and `.github/skills/` summary
  - merge policy still stops at `full overwrite`, `keep current content`, or
    `manual merge by the human`
- The canonical copy must include the full candidate surface:
  - `SKILL.md`
  - `checklist.md`
  - `examples.md`
  - `references/input-sources-and-priority.md`
  - `references/instruction-layering.md`
  - `references/merge-and-conflict-policy.md`
- Runtime/tooling blocker repair remains deferred to a separate future topic.

## Boundaries / Exclusions

- Do not edit `.github/skills/copilot-instructions-init/` in this topic.
- Do not retarget the target-project output destination away from
  `.github/copilot-instructions.md`.
- Do not change stale-fingerprint rules, managed-block policy, or overwrite
  choice semantics.
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

- Branch target: `feat/andrew/copilot-instructions-init-canonicalize`
- Base branch: `dev`
- This topic must not be reclassified into runtime/tooling repair or active-path
  cutover without a new plan.

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/copilot-instructions-init-canonicalize/copilot-instructions-init-canonicalize.plan.md` | Planning actor | Repo-visible execution contract |
| Requirements baseline | `analysis/copilot-instructions-init-canonicalize/requirements.md` | Planning actor | Locked single-candidate scope, copy boundary, and stop conditions |
| Technical baseline | `analysis/copilot-instructions-init-canonicalize/technical-spec.md` | Planning actor | Execution-facing copy rules, deferred blocker inventory, and verification contract |
| Migration report | `docs/migration/copilot-instructions-init-canonicalize.md` | Creator | Repo-visible copy result and deferred-runtime evidence |
| Target skill folder | `skills/copilot-instructions-init/` | Creator | New target-architecture canonical copy |
| Compatibility source | `.github/skills/copilot-instructions-init/` | Existing repo artifact | Read-only transition-era source to copy from and preserve |

## Implementation Steps

1. Verify the source inventory at `.github/skills/copilot-instructions-init/`
   still matches the file set frozen in the technical spec:
   - `SKILL.md`
   - `checklist.md`
   - `examples.md`
   - `references/input-sources-and-priority.md`
   - `references/instruction-layering.md`
   - `references/merge-and-conflict-policy.md`
2. Copy the current transition-era source content from
   `.github/skills/copilot-instructions-init/` into a new
   `skills/copilot-instructions-init/` target-architecture folder,
   preserving relative structure exactly.
3. Preserve current `.github/skills/copilot-instructions-init/`
   compatibility content without edits.
4. Write `docs/migration/copilot-instructions-init-canonicalize.md` with:
   - candidate name
   - source root
   - target root
   - copied file set
   - compatibility layer preserved
   - active path changed: no
   - confirmed-blocker context preserved
   - deferred runtime/tooling blocker lanes
5. Stop and re-plan if implementation requires:
   - editing `.github/skills/copilot-instructions-init/`
   - changing target output destination, stale-fingerprint rules, or merge policy
   - touching shared migration, governance, projection, or release surfaces

## Validation / Acceptance Checks

- Only the locked candidate is copied into `skills/`.
- `skills/copilot-instructions-init/` contains the full required surface,
  not only `SKILL.md`.
- `.github/skills/copilot-instructions-init/` remains present and unchanged.
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

- verify that the full candidate surface was copied, including checklist and all references
- verify that `.github/skills/copilot-instructions-init/` was preserved unchanged
- verify that no artifact claims active cutover or target output-surface cutover
- verify that confirmed-blocker context and deferred runtime/tooling lanes remain explicit

## Post-merge / release actions

- No repository release action is part of this topic.
- `merged` is terminal for this topic.
- Runtime-path migration, target output transition, stale-gate redesign,
  merge-policy transition, projection switching, and repo-wide path governance
  changes require separate later topics.
