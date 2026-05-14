# positioning-freeze

Analysis-layer routing: **strict mode**.
`analysis/codex-migration-runway/technical-spec.md` is the execution-facing
source of truth for this topic, and
`analysis/codex-migration-runway/requirements.md` remains the business-intent
guardrail. This plan is limited to the first bounded phase of the runway and
does not authorize migration work.

Human override:

- The analysis topic is intentionally `codex-migration-runway`.
- The first bounded implementation topic is intentionally `positioning-freeze`.
- This plan consumes the runway analysis artifacts by explicit human instruction
  rather than by the repository's usual same-topic analysis/plan pairing.

## Goal / Outcome

- Produce a review-ready phase plan for `positioning-freeze` that freezes
  repository positioning only.
- Prepare the first bounded implement phase so it can clarify current operating
  state, target architecture, and migration boundary without performing skill
  migration.
- Preserve the runway's role separation: Setup Agent defines the global
  baseline; the later Bounded Implement Agent executes only this phase.

## Scope

- **In scope**:
  - `plan/positioning-freeze/positioning-freeze.plan.md` as the planning-owned,
    authoritative execution contract for this phase
  - `AGENTS.md`
  - `docs/repo-positioning.md`
  - `.github/copilot-instructions.md`

- **Out of scope**:
  - `analysis/codex-migration-runway/requirements.md`
  - `analysis/codex-migration-runway/technical-spec.md`
  - `README.md`
  - `.github/skills/*`
  - `skills/*`
  - `.codex/*`
  - `.claude/*`
  - `plan/platform-coupling-inventory/`
  - any inventory, promotion, installer, generator, renderer, or migration
    script work

## Locked Decisions

- This topic is **review-ready-only with no stable-library surfaces**.
- This phase freezes repository positioning only; it does not perform migration.
- Current operating state must keep stating that `.github/skills/` remains the
  current Copilot active authored/reviewed workflow path during transition.
- Target architecture may state that `skills/` is the intended canonical skill
  source, but this phase must not declare it active today.
- Migration boundary must explicitly say this phase does not perform skill-path
  migration, platform directory changes, or creator / reviewer / template path
  transition.
- `.github/skills/business-intent-alignment` and
  `.github/skills/business-to-technical-translation` are part of the planning
  spine and must not be treated as optional side references.
- The bounded implement handoff for this phase must use:
  - worktree path:
    `../agent-skills.worktrees/feat-andrew-positioning-freeze`
  - current branch: `feat/andrew/copilot-to-codex-migration`
  - target phase branch: `feat/andrew/positioning-freeze`
  - PR target branch: `feat/andrew/copilot-to-codex-migration`
- `plan/positioning-freeze/positioning-freeze.plan.md` remains planning-owned,
  authoritative, and read-only for Bounded Implement Agent during phase
  execution.
- Bounded Implement Agent may modify only the writable implementation paths
  listed in this plan and must not edit the topic plan.
- Bounded Implement Agent must stop instead of widening into inventory,
  promotion, or path-transition work.
- `.github/skills/*` skill contract content must not be edited in this phase.
- creator / reviewer / template contract content must not be edited in this
  phase.
- No wording may imply that `skills/` is already the current active workflow
  path.

## Boundaries / Exclusions

- Setup Agent owns the runway baseline and this phase plan only.
- Bounded Implement Agent owns phase execution within the writable
  implementation paths only and must treat the topic plan as read-only.
- Reviewer owns review verdict only and must not author the final
  implementation directly.
- This phase must not create adjacent phase plans.
- This phase must not repair broader migration blockers by editing nearby
  contracts.
- If the required outcome cannot be achieved without touching forbidden paths,
  stop and return to planning instead of silently widening the phase.

## Status / Allowed Transitions

- **Current**: `planned`
- **Execution model**: retain the repository's canonical status vocabulary for
  contract compatibility, but treat only the pre-publish subset as active
  execution owned by this bounded phase. Downstream publish / PR / merge states
  remain canonical routing context and are not writable-scope authorization for
  Bounded Implement Agent.
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

- Active phase-local execution for `positioning-freeze` is expected to stop at
  reviewer approval / rework routing. The canonical downstream statuses remain
  listed only for repo-contract compatibility and later branch-routing clarity.
- The bounded implement worktree for this phase is
  `../agent-skills.worktrees/feat-andrew-positioning-freeze`.
- Main Agent prepares the bounded phase worktree and branch before bounded
  implementation starts:
  - create worktree `../agent-skills.worktrees/feat-andrew-positioning-freeze`
  - cut `feat/andrew/positioning-freeze` from
    `feat/andrew/copilot-to-codex-migration`
- The phase branch merges back into
  `feat/andrew/copilot-to-codex-migration` first.
- Direct merge from a phase branch to `dev` is not authorized.
- Merge routing is post-approval context, not an active phase status in this
  topic plan.
- If plan or artifact drift appears, route back to planning before continuing.

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/positioning-freeze/positioning-freeze.plan.md` | Setup Agent / Planning actor | Repo-visible authoritative execution contract for the positioning-freeze phase; read-only for Bounded Implement Agent |
| Governance summary | `AGENTS.md` | Bounded Implement Agent | Canonical governance summary that must remain aligned with the frozen positioning language |
| Positioning authority | `docs/repo-positioning.md` | Bounded Implement Agent | Primary current-state / target-architecture / migration-boundary document |
| Copilot mirror | `.github/copilot-instructions.md` | Bounded Implement Agent | GitHub/Copilot always-on mirror of the same frozen positioning stance when wording repair is required |

Artifact path notes:

- This phase does **not** modify `VERSION`.
- This phase does **not** modify `README.md`.
- This phase does **not** modify any file under `.github/skills/` or `skills/`.
- The topic plan remains in scope as the authoritative contract artifact, but it
  is not part of the writable implementation scope for Bounded Implement Agent.
- Treat the listed paths as an executable contract.
- If later work drifts outside these paths, stop and repair the plan before
  continuing.

## Implementation Steps

1. Start from the runway source-of-truth artifacts in this order:
   - `plan/positioning-freeze/positioning-freeze.plan.md`
   - `analysis/codex-migration-runway/technical-spec.md`
   - `analysis/codex-migration-runway/requirements.md`
2. Treat `plan/positioning-freeze/positioning-freeze.plan.md` as the
   authoritative read-only contract during implementation.
3. Execute only within the writable implementation paths:
   - `AGENTS.md`
   - `docs/repo-positioning.md`
   - `.github/copilot-instructions.md`
4. Freeze current operating state wording so it remains true that:
   - `AGENTS.md` is the governance canonical source
   - `.github/skills/` remains the current Copilot active authored/reviewed
     workflow path during transition
   - `skills/` is the intended canonical skill source / target architecture,
     not the currently active path
5. Freeze target architecture wording so it remains explicit that:
   - `skills/` is the intended canonical skill source
   - `.<platform>/skills/...` is a future projection / adapter / compatibility
     layout, not source of truth
6. Freeze migration boundary wording so it remains explicit that this phase does
   not:
   - perform skill-path migration
   - add `.codex/` or `.claude/`
   - change creator output paths
   - change reviewer target paths
   - change template scaffold paths
   - add generator / renderer / installer scripts
7. Keep creator / reviewer / template contract content unchanged.
8. Keep `.github/skills/*` skill contract content unchanged.
9. If wording conflicts are found between the writable implementation paths,
    resolve them only by
   clarifying positioning language within the allowed paths. Do not widen into
   migration execution.
10. Hand the resulting diff to an independent reviewer and require a verdict
    against this plan before any post-approval routing.

## Validation / Acceptance Checks

- `positioning-freeze` still reads as a runway phase, not a migration phase.
- `AGENTS.md`, `docs/repo-positioning.md`, and
  `.github/copilot-instructions.md` stay semantically aligned.
- The current operating state is explicit and still names `.github/skills/` as
  the current active authored/reviewed path during transition.
- The target architecture is explicit and still names `skills/` as intended
  canonical source / target architecture only.
- The migration boundary is explicit and still says this phase does not perform
  migration.
- No wording declares `skills/` already active today.
- The topic plan remains unchanged during bounded implementation.
- No files outside the listed writable implementation paths are modified.
- `README.md` remains unchanged in this phase.
- No `.github/skills/*` contract content is modified.
- No creator / reviewer / template contract content is modified.
- No `.codex/` or `.claude/` paths are added.
- No generator / renderer / installer script work is added.
- No adjacent phase plan such as `platform-coupling-inventory` is authored.
- The resulting phase branch is intended to merge back into
  `feat/andrew/copilot-to-codex-migration`, not directly into `dev`.

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

- No repository release action is part of this phase.
- If the phase is approved and later merged, it merges back into
  `feat/andrew/copilot-to-codex-migration` first.
- Any later merge or release decision beyond the Big Feature Branch requires a
  separate human-directed topic.

## Open Questions / Unresolved Items

- The exact wording delta across `AGENTS.md`, `docs/repo-positioning.md`, and
  `.github/copilot-instructions.md` is intentionally left for the bounded
  implement phase to resolve within the frozen path constraints.
- If those documents cannot be aligned without touching forbidden paths, stop
  and return to planning with the contradiction written explicitly.
