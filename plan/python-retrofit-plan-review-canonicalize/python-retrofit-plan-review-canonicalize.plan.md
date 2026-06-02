# python-retrofit-plan-review-canonicalize

## Goal / Outcome

- Create `skills/python-retrofit-plan-review/` as the target-architecture
  canonical copy of the existing transition-era candidate.
- Preserve `.github/skills/python-retrofit-plan-review/` as the current
  compatibility surface during transition.
- Leave one repo-visible migration artifact that records the copied file set,
  preserved planning-spine review semantics, and deferred coupled-lane work.

## Scope

- **In scope**:
  - `analysis/python-retrofit-plan-review-canonicalize/requirements.md`
  - `analysis/python-retrofit-plan-review-canonicalize/technical-spec.md`
  - `plan/python-retrofit-plan-review-canonicalize/python-retrofit-plan-review-canonicalize.plan.md`
  - `skills/python-retrofit-plan-review/`
  - `docs/migration/python-retrofit-plan-review-canonicalize.md`

- **Out of scope**:
  - `.github/skills/python-retrofit-plan-review/`
  - `python-retrofit-plan-authoring`
  - `python-project-retrofit`
  - `sense-env-scaffold`
  - `AGENTS.md`
  - `docs/repo-positioning.md`
  - `README.md`
  - `VERSION`
  - `.codex/*`
  - repo-wide migration checklist updates

## Locked Decisions

- This topic implements only the bounded canonical copy for
  `python-retrofit-plan-review`.
- `skills/` receives a new target-architecture copy at
  `skills/python-retrofit-plan-review/`.
- `.github/skills/python-retrofit-plan-review/` remains the transition-era
  compatibility surface in this topic.
- Retrofit V2 review-verdict, risk-boundary, lane-fit, and sensing-assertion
  review semantics must remain unchanged in this topic.
- The canonical copy must include the full bounded candidate surface:
  - `SKILL.md`
  - `examples.md`
  - `checklist.md`
  - `references/`
- Coupled planning-spine synchronization remains deferred to separate future
  topics.
- Base branch is `dev` because that is the only verifiable local bootstrap base
  in the current repository snapshot.

## Boundaries / Exclusions

- Do not edit `.github/skills/python-retrofit-plan-review/` in this topic.
- Do not rewrite `python-retrofit-plan-authoring`,
  `python-project-retrofit`, or `sense-env-scaffold`.
- Do not modify review-verdict contract, Retrofit V2 review checks, or sensing
  assertion-kind rules in this topic.
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

- Branch target: `feat/andrew/python-retrofit-plan-review-canonicalize`
- Base branch: `dev`
- This topic must not be reclassified into planning-spine redesign or
  active-path cutover without a new plan.
- This topic is authored in strict alignment with:
  - `analysis/python-retrofit-plan-review-canonicalize/requirements.md`
  - `analysis/python-retrofit-plan-review-canonicalize/technical-spec.md`

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/python-retrofit-plan-review-canonicalize/python-retrofit-plan-review-canonicalize.plan.md` | Planning actor | Repo-visible execution contract |
| Requirements baseline | `analysis/python-retrofit-plan-review-canonicalize/requirements.md` | Planning actor | Locked single-candidate scope, copy boundary, and stop conditions |
| Technical baseline | `analysis/python-retrofit-plan-review-canonicalize/technical-spec.md` | Planning actor | Execution-facing copy rules, deferred coupling inventory, and verification contract |
| Migration report | `docs/migration/python-retrofit-plan-review-canonicalize.md` | Creator | Repo-visible copy result and deferred-coupling evidence |
| Target skill folder | `skills/python-retrofit-plan-review/` | Creator | New target-architecture canonical copy |
| Compatibility source | `.github/skills/python-retrofit-plan-review/` | Existing repo artifact | Read-only transition-era source to copy from and preserve |
| Planning-spine evidence | `plan/python-retrofit-plan-review/python-retrofit-plan-review.plan.md` | Existing repo artifact | Read-only evidence for current coupled semantics |
| Coupling evidence | `docs/migration/platform-coupling-inventory.md` | Existing repo artifact | Read-only evidence for downstream deferred coupling |

Artifact path notes:

- This topic does not modify `.github/skills/python-retrofit-plan-review/`.
- This topic does not modify downstream planning-spine skills or executor artifacts.
- This topic does not modify `.codex/*`, `README.md`, `VERSION`,
  `.github/copilot-instructions.md`, `AGENTS.md`, `docs/repo-positioning.md`, or
  checklist-wide migration trackers.
- If execution requires editing any other path, stop and repair this plan
  before continuing.

## Implementation Steps

1. Verify the source inventory at `.github/skills/python-retrofit-plan-review/`
   still matches the file set frozen in the technical spec:
   - `SKILL.md`
   - `examples.md`
   - `checklist.md`
   - `references/lane-fit-and-reroute.md`
   - `references/retrofit-v2-review-checks.md`
   - `references/review-verdict-contract.md`
   - `references/risk-boundary-and-locatability-checks.md`
2. Copy the current transition-era source content from
   `.github/skills/python-retrofit-plan-review/` into a new
   `skills/python-retrofit-plan-review/` target-architecture folder,
   preserving relative structure exactly.
3. Preserve current `.github/skills/python-retrofit-plan-review/`
   compatibility content without edits.
4. Write `docs/migration/python-retrofit-plan-review-canonicalize.md` with:
   - candidate name
   - source root
   - target root
   - copied file set
   - compatibility layer preserved
   - active authored/reviewed path changed: no
   - deferred coupled lanes
5. Stop and re-plan if implementation requires:
   - editing `.github/skills/python-retrofit-plan-review/`
   - changing review-verdict or Retrofit V2 review semantics
   - retargeting downstream planning-spine consumers
   - touching shared migration, governance, projection, or release surfaces

## Validation / Acceptance Checks

- Only the locked candidate is copied into `skills/`.
- `skills/python-retrofit-plan-review/` contains the full required bounded
  surface, not only `SKILL.md`.
- `.github/skills/python-retrofit-plan-review/` remains present and unchanged.
- No downstream planning-spine or executor artifact is changed in this topic.
- No contract redesign, shared governance change, projection update, or
  release-surface edit is performed.
- The migration report states what was copied, what remained the compatibility
  layer, and which coupled lanes stayed deferred.

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

- verify that the full bounded surface was copied, including checklist and all
  references
- verify that `.github/skills/python-retrofit-plan-review/` was preserved
  unchanged
- verify that no artifact claims review-contract redesign or active-path cutover
- verify that deferred downstream coupled lanes remain explicit rather than
  silently omitted

## Post-merge / release actions

- No repository release action is part of this topic.
- `merged` is terminal for this topic.
- Downstream planning-spine synchronization, projection switching, and repo-wide
  path governance changes require separate later topics.

## Open Questions / Unresolved Items

- None at topic-bootstrap time.
- If later implementation reveals that creating the canonical copy requires
  downstream planning-spine rewrites or shared-governance edits, stop and
  re-plan instead of widening this topic silently.
