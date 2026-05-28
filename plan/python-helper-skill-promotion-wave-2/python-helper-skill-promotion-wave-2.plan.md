# python-helper-skill-promotion-wave-2

Analysis-layer routing: **incomplete layer with explicit warning**.
`analysis/python-helper-skill-promotion-wave-2/requirements.md` exists and is
the frozen business-intent guardrail for this topic. The companion
`analysis/python-helper-skill-promotion-wave-2/technical-spec.md` does not
exist in this worktree, so this plan is authored from the locked requirements
baseline plus repo-visible governance and workflow contracts. No chat-time
instruction overrides that requirements baseline.

## Goal / Outcome

- Produce a review-ready selective-promotion plan for
  `python-helper-skill-promotion-wave-2`.
- Promote exactly 18 locked Python helper skills into `skills/` as
  target-architecture copies.
- Preserve `.github/skills/` as the current active authored/reviewed workflow
  path during transition.
- Leave a repo-visible promotion evidence artifact that records what was
  promoted, what stayed deferred, and the one-way source-authority rule for this
  wave.

## Scope

- **In scope**:
  - `analysis/python-helper-skill-promotion-wave-2/requirements.md`
  - `plan/python-helper-skill-promotion-wave-2/python-helper-skill-promotion-wave-2.plan.md`
  - `plan/python-helper-skill-promotion-wave-2/python-helper-skill-promotion-wave-2.step.md`
  - `docs/migration/python-helper-skill-promotion-wave-2.md`
  - `skills/python-api-signature/`
  - `skills/python-async-await/`
  - `skills/python-class-design/`
  - `skills/python-comprehensions/`
  - `skills/python-context-management/`
  - `skills/python-control-flow/`
  - `skills/python-data-model-methods/`
  - `skills/python-decorators/`
  - `skills/python-descriptors-attribute-access/`
  - `skills/python-docstrings/`
  - `skills/python-error-handling/`
  - `skills/python-generators-iterators/`
  - `skills/python-model-selection/`
  - `skills/python-module-boundaries/`
  - `skills/python-naming/`
  - `skills/python-operator-overloading/`
  - `skills/python-testing-pytest/`
  - `skills/python-type-hints-strict/`

- **Out of scope**:
  - `AGENTS.md`
  - `docs/repo-positioning.md`
  - `.github/copilot-instructions.md`
  - `README.md`
  - `VERSION`
  - `.github/skills/agent-skill-creator/`
  - `.github/skills/agent-skill-reviewer/`
  - `.github/skills/agent-skill-template/`
  - runtime/tooling blocker surfaces
  - any skill not listed in the 18-skill promotion set
  - repo-wide active-path cutover
  - release or tag work

## Locked Decisions

- This topic is a **selective promotion topic**, not a repo-wide migration.
- This topic is **not** a stable-library publish topic.
- The migration primitive is `folder-level direct copy`.
- The target branch for workflow input is
  `feat/andrew/python-helper-skill-promotion-wave-2`.
- The worktree path is `/private/tmp/python-helper-skill-promotion-wave-2`.
- Bootstrap worktree creation was already completed before this drafting round.
- Only these 18 skills may be promoted in this branch:
  - `python-api-signature`
  - `python-async-await`
  - `python-class-design`
  - `python-comprehensions`
  - `python-context-management`
  - `python-control-flow`
  - `python-data-model-methods`
  - `python-decorators`
  - `python-descriptors-attribute-access`
  - `python-docstrings`
  - `python-error-handling`
  - `python-generators-iterators`
  - `python-model-selection`
  - `python-module-boundaries`
  - `python-naming`
  - `python-operator-overloading`
  - `python-testing-pytest`
  - `python-type-hints-strict`
- `.github/skills/` remains the current active authored/reviewed workflow path
  during transition.
- `skills/` is the target-architecture promotion result for the selected wave
  only; this topic must not describe `.github/skills/` and `skills/` as dual
  canonical sources.
- README / VERSION / release-tag handling is deferred to later work.
- This bootstrap round stops before commit and must not declare review passed,
  planner final review passed, `COMMITTED`, or `FINISHED`.

## Boundaries / Exclusions

- Planning actor owns the topic boundaries, locked decisions, and repo-visible
  planning artifacts only.
- Creator owns only the bounded selective-promotion execution inside the listed
  artifact paths and must not modify planning artifacts.
- Reviewer owns verdict only and must not implement the promotion.
- Main Agent owns later publish routing only after independent review and
  planner final review complete.
- Do not edit `.github/skills/<skill-name>/` for the in-scope wave in this
  topic; those folders are promotion inputs and must remain preserved as the
  current active path.
- Do not widen into creator / reviewer / template contract-surface migration.
- Do not widen into runtime/tooling blocker repair, projection switching,
  installer changes, governance rewrites, or stable-library updates.
- If later work needs any path outside `Artifact Paths`, stop and re-plan
  instead of improvising.

## Status / Allowed Transitions

- **Current**: `planned`
- **Execution model**: follow the canonical `creator -> reviewer -> publish ->
  merge` workflow path for this topic; no repository release action is declared
  here
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

- Base branch: `dev`
- Target branch: `feat/andrew/python-helper-skill-promotion-wave-2`
- Standard Phase 4.5 rule applies: reviewer acceptance alone does not authorize
  publish progression if planner alignment finds scope drift.
- This topic must not be reclassified into repo-wide cutover, runtime/tooling
  repair, or stable-library metadata work without a new plan.
- This drafting round ends before commit; later commit progression remains
  blocked until independent plan review and planner final review are both
  complete.

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/python-helper-skill-promotion-wave-2/python-helper-skill-promotion-wave-2.plan.md` | Planning actor | Repo-visible execution contract for this topic |
| Requirements baseline | `analysis/python-helper-skill-promotion-wave-2/requirements.md` | Planning actor | Locked promotion set, source-authority boundary, and stop conditions |
| Topic progression artifact | `plan/python-helper-skill-promotion-wave-2/python-helper-skill-promotion-wave-2.step.md` | Planning actor, then Main Agent | Workflow progression truth for later creator/reviewer/publish handoff |
| Promotion report | `docs/migration/python-helper-skill-promotion-wave-2.md` | Creator | Repo-visible promotion result and deferred-boundary evidence |
| Target skill folder | `skills/python-api-signature/` | Creator | Target-architecture promotion copy for the selected helper skill |
| Target skill folder | `skills/python-async-await/` | Creator | Target-architecture promotion copy for the selected helper skill |
| Target skill folder | `skills/python-class-design/` | Creator | Target-architecture promotion copy for the selected helper skill |
| Target skill folder | `skills/python-comprehensions/` | Creator | Target-architecture promotion copy for the selected helper skill |
| Target skill folder | `skills/python-context-management/` | Creator | Target-architecture promotion copy for the selected helper skill |
| Target skill folder | `skills/python-control-flow/` | Creator | Target-architecture promotion copy for the selected helper skill |
| Target skill folder | `skills/python-data-model-methods/` | Creator | Target-architecture promotion copy for the selected helper skill |
| Target skill folder | `skills/python-decorators/` | Creator | Target-architecture promotion copy for the selected helper skill |
| Target skill folder | `skills/python-descriptors-attribute-access/` | Creator | Target-architecture promotion copy for the selected helper skill |
| Target skill folder | `skills/python-docstrings/` | Creator | Target-architecture promotion copy for the selected helper skill |
| Target skill folder | `skills/python-error-handling/` | Creator | Target-architecture promotion copy for the selected helper skill |
| Target skill folder | `skills/python-generators-iterators/` | Creator | Target-architecture promotion copy for the selected helper skill |
| Target skill folder | `skills/python-model-selection/` | Creator | Target-architecture promotion copy for the selected helper skill |
| Target skill folder | `skills/python-module-boundaries/` | Creator | Target-architecture promotion copy for the selected helper skill |
| Target skill folder | `skills/python-naming/` | Creator | Target-architecture promotion copy for the selected helper skill |
| Target skill folder | `skills/python-operator-overloading/` | Creator | Target-architecture promotion copy for the selected helper skill |
| Target skill folder | `skills/python-testing-pytest/` | Creator | Target-architecture promotion copy for the selected helper skill |
| Target skill folder | `skills/python-type-hints-strict/` | Creator | Target-architecture promotion copy for the selected helper skill |
| Current active source | `.github/skills/python-api-signature/` | Existing repo artifact | Current active transition-era source used as promotion input |
| Current active source | `.github/skills/python-async-await/` | Existing repo artifact | Current active transition-era source used as promotion input |
| Current active source | `.github/skills/python-class-design/` | Existing repo artifact | Current active transition-era source used as promotion input |
| Current active source | `.github/skills/python-comprehensions/` | Existing repo artifact | Current active transition-era source used as promotion input |
| Current active source | `.github/skills/python-context-management/` | Existing repo artifact | Current active transition-era source used as promotion input |
| Current active source | `.github/skills/python-control-flow/` | Existing repo artifact | Current active transition-era source used as promotion input |
| Current active source | `.github/skills/python-data-model-methods/` | Existing repo artifact | Current active transition-era source used as promotion input |
| Current active source | `.github/skills/python-decorators/` | Existing repo artifact | Current active transition-era source used as promotion input |
| Current active source | `.github/skills/python-descriptors-attribute-access/` | Existing repo artifact | Current active transition-era source used as promotion input |
| Current active source | `.github/skills/python-docstrings/` | Existing repo artifact | Current active transition-era source used as promotion input |
| Current active source | `.github/skills/python-error-handling/` | Existing repo artifact | Current active transition-era source used as promotion input |
| Current active source | `.github/skills/python-generators-iterators/` | Existing repo artifact | Current active transition-era source used as promotion input |
| Current active source | `.github/skills/python-model-selection/` | Existing repo artifact | Current active transition-era source used as promotion input |
| Current active source | `.github/skills/python-module-boundaries/` | Existing repo artifact | Current active transition-era source used as promotion input |
| Current active source | `.github/skills/python-naming/` | Existing repo artifact | Current active transition-era source used as promotion input |
| Current active source | `.github/skills/python-operator-overloading/` | Existing repo artifact | Current active transition-era source used as promotion input |
| Current active source | `.github/skills/python-testing-pytest/` | Existing repo artifact | Current active transition-era source used as promotion input |
| Current active source | `.github/skills/python-type-hints-strict/` | Existing repo artifact | Current active transition-era source used as promotion input |

Artifact path notes:

- This topic does **not** modify `README.md`.
- This topic does **not** modify `VERSION`.
- This topic does **not** modify `.github/copilot-instructions.md`.
- This topic does **not** modify `AGENTS.md` or `docs/repo-positioning.md`.
- This topic does **not** modify `agent-skill-creator`, `agent-skill-reviewer`,
  `agent-skill-template`, runtime/tooling blocker surfaces, or any unlisted
  skill path.
- If execution drifts outside the listed paths, stop and repair the plan before
  continuing.

## Implementation Steps

1. Read this topic plan, the locked requirements baseline, and the repo-level
   handoff workflow before changing files.
2. Reconfirm that the promotion set is limited to the 18 locked helper skills.
3. For each in-scope skill, copy the entire corresponding
   `.github/skills/<skill-name>/` folder into `skills/<skill-name>/` using the
   locked `folder-level direct copy` primitive.
4. Preserve the `.github/skills/<skill-name>/` source folders without edits and
   without re-declaring them as canonical sources.
5. Write `docs/migration/python-helper-skill-promotion-wave-2.md` with:
   - the locked 18-skill promotion set
   - the one-way source-authority rule for the wave
   - the fact that `.github/skills/` remains the current active path during
     transition
   - the promotion result for each in-scope skill
   - the deferred follow-up lanes that remain out of scope here
6. Stop and re-plan if any in-scope skill needs shared-governance,
   contract-surface, runtime/tooling, README, VERSION, or repo-positioning
   edits.
7. Hand the resulting diff to independent review before any publish routing.

## Validation / Acceptance Checks

- Only the 18 locked helper skills are promoted in this topic.
- No unlisted `.github/skills/*` folder is materialized under `skills/`.
- No in-scope `.github/skills/<skill-name>/` folder is edited.
- `skills/` and `.github/skills/` are not described as dual canonical sources.
- The promotion report explicitly states that `.github/skills/` remains the
  current active path during transition.
- No edit lands in `AGENTS.md`, `docs/repo-positioning.md`,
  `.github/copilot-instructions.md`, `README.md`, `VERSION`, agent-skill
  contract surfaces, runtime/tooling blocker surfaces, or any unlisted skill.
- The topic progression artifact stays usable as workflow truth for later
  creator, reviewer, and publish handoff.

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

- No repository release action is part of this topic.
- `merged` is terminal for this topic.
- README / VERSION updates, active-path cutover, projection switching, contract
  surface migration, and runtime/tooling repair remain separate later topics.

## Open Questions / Unresolved Items

- None at topic-bootstrap drafting time.
- If later execution reveals that any in-scope skill cannot be promoted by
  folder-level direct copy inside the listed paths, stop and re-plan instead of
  widening scope silently.
