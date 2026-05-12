# platform-coupling-inventory

Analysis-layer routing: **strict mode**.
This phase consumes the frozen runway baseline and the frozen
`positioning-freeze` boundary. It authorizes inventory only. It does not
authorize migration, active-path cutover, contract transition, or
runtime/tooling repair.

## Goal / Outcome

- Produce a review-ready phase plan for `platform-coupling-inventory`.
- Inventory current repo-visible path, workflow, artifact, contract, and
  runtime/tooling coupling that would matter to a later migration.
- Preserve the runway separation between:
  - inventory
  - contract transition
  - runtime/tooling transition
  - promotion / release work
- Prepare a bounded implement handoff that records coupling evidence without
  widening into migration.

## Source-of-Truth Order

Use these repo-visible artifacts in this order:

1. `plan/platform-coupling-inventory/platform-coupling-inventory.plan.md`
2. `analysis/codex-migration-runway/technical-spec.md`
3. `analysis/codex-migration-runway/requirements.md`
4. `plan/positioning-freeze/positioning-freeze.plan.md`
5. `AGENTS.md`
6. `docs/repo-positioning.md`
7. `.github/copilot-instructions.md`

Authority notes:

- `docs/migration/platform-coupling-inventory.md` is the expected bounded-phase
  output evidence for this topic, not an input that outranks this plan.
- Hidden chat context does not outrank repo-visible artifacts.
- If the inventory cannot be completed without changing files outside the
  allowed writable scope, execution must stop and return to Setup Agent.

## Goal Boundary

- This topic is a **runway phase**, not full migration.
- This topic is **inventory-only**.
- This topic does **not** perform migration.
- This topic does **not** cut over the active path from `.github/skills/` to
  `skills/`.
- This topic does **not** transition creator / reviewer / template contracts.
- This topic does **not** repair runtime/tooling blockers.
- This topic does **not** rewrite governance or positioning authority.

## Scope

- **In scope**:
  - `plan/platform-coupling-inventory/platform-coupling-inventory.plan.md` as
    the planning-owned authoritative execution contract for this phase
  - `docs/migration/platform-coupling-inventory.md`

- **Out of scope**:
  - `.github/skills/*`
  - `skills/*`
  - `analysis/*`
  - `plan/positioning-freeze/positioning-freeze.plan.md`
  - `plan/skill-authoring-path-transition/skill-authoring-path-transition.plan.md`
  - `plan/high-frequency-skill-promotion/high-frequency-skill-promotion.plan.md`
  - `AGENTS.md`
  - `docs/repo-positioning.md`
  - `.github/copilot-instructions.md`
  - `README.md`
  - `VERSION`
  - `.codex/*`
  - `.claude/*`
  - any migration, promotion, release, installer, generator, renderer, or
    runtime/tooling transition work

## Locked Decisions

- `.github/skills/` remains the current active authored/reviewed workflow path
  during this runway.
- `skills/` remains target architecture only during this runway.
- This phase is limited to inventory only.
- This phase must not silently perform migration or active-path cutover.
- This phase must not change creator / reviewer / template contract content.
- This phase must not change runtime/tooling surfaces to compensate for missing
  path compatibility.
- This phase must not modify planning spine skill folders directly.
- `.github/skills/business-intent-alignment` and
  `.github/skills/business-to-technical-translation` must be classified as:
  - primary:
    - `workflow dependency`
    - `artifact dependency`
  - secondary:
    - `contract dependency`
    - `source/path dependency`
- The two planning spine skills must not be classified as primary
  `runtime/tooling blocker` in this phase.
- Inventory findings must separate evidence from remediation.
- `plan/platform-coupling-inventory/platform-coupling-inventory.plan.md`
  remains planning-owned, authoritative, and read-only for Bounded Implement
  Agent during execution.

## Dependency Interpretation

### Planning spine skills

- `.github/skills/business-intent-alignment`
- `.github/skills/business-to-technical-translation`

Interpretation rules:

- treat them as planning-spine dependencies
- track them as downstream workflow / artifact dependencies
- record their contract/path coupling when repo-visible evidence supports it
- do not classify them as primary runtime/tooling blockers in this phase
- do not modify those skill folders in this phase

### Contract surfaces

Creator / reviewer / template surfaces may be identified as path-coupled
workflow or contract dependencies, but this phase does not edit them:

- `.github/skills/agent-skill-creator/`
- `.github/skills/agent-skill-reviewer/`
- `.github/skills/agent-skill-template/`

### Runtime / tooling surfaces

Executable or generated-path dependencies may be identified and classified as
runtime/tooling blockers when explicit evidence exists, but this phase does not
repair them.

## Boundaries / Exclusions

- Setup Agent owns the runway baseline, this phase plan, and the implementer
  handoff contract.
- Bounded Implement Agent owns only the inventory execution inside the allowed
  writable path.
- Reviewer owns review verdict only.
- This phase must not create adjacent phase plans.
- This phase must not repair broader migration blockers by editing nearby
  contracts.
- If the required outcome cannot be achieved inside the allowed writable path,
  execution stops and returns to Setup Agent.

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

- Active phase-local execution for `platform-coupling-inventory` is expected to
  stop at reviewer approval / rework routing.
- The bounded implement worktree for this phase should be prepared by Main
  Agent before execution starts.
- The resulting phase branch merges back into
  `feat/andrew/copilot-to-codex-migration` first.
- Direct merge from a phase branch to `dev` is not authorized.

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/platform-coupling-inventory/platform-coupling-inventory.plan.md` | Setup Agent / Planning actor | Repo-visible authoritative execution contract for this phase; read-only for Bounded Implement Agent |
| Inventory evidence | `docs/migration/platform-coupling-inventory.md` | Bounded Implement Agent | Repo-visible inventory output for dependency, blocker, and coupling classification |
| Runway technical baseline | `analysis/codex-migration-runway/technical-spec.md` | Setup Agent / Planning actor | Execution-facing runway baseline |
| Runway requirements baseline | `analysis/codex-migration-runway/requirements.md` | Setup Agent / Planning actor | Business-intent boundary baseline |
| Positioning boundary plan | `plan/positioning-freeze/positioning-freeze.plan.md` | Setup Agent / Planning actor | Frozen upstream boundary for current-vs-target wording and non-migration constraints |

Artifact path notes:

- This phase does **not** modify `VERSION`.
- This phase does **not** modify `README.md`.
- This phase does **not** modify any planning artifact during bounded
  implementation.
- This phase may read any relevant repo-visible artifact needed to classify
  coupling, but may only write the inventory evidence path.

## Allowed / Forbidden Paths

### Allowed writable paths for Bounded Implement Agent

- `docs/migration/platform-coupling-inventory.md`

### Forbidden paths for Bounded Implement Agent

- `plan/platform-coupling-inventory/platform-coupling-inventory.plan.md`
- `analysis/codex-migration-runway/technical-spec.md`
- `analysis/codex-migration-runway/requirements.md`
- `plan/positioning-freeze/positioning-freeze.plan.md`
- `AGENTS.md`
- `docs/repo-positioning.md`
- `.github/copilot-instructions.md`
- `.github/skills/*`
- `skills/*`
- `README.md`
- `VERSION`
- `.codex/*`
- `.claude/*`

## Implementation Steps

1. Start from the source-of-truth order listed in this plan.
2. Treat this topic plan as the authoritative read-only contract during bounded
   implementation.
3. Inspect repo-visible governance, positioning, planning, and skill-contract
   artifacts for path, workflow, artifact, contract, and runtime/tooling
   coupling.
4. Record findings only in `docs/migration/platform-coupling-inventory.md`.
5. Explicitly distinguish:
   - current operating state
   - target architecture
   - migration boundary
   - dependency classification
   - blocker classification
6. Classify `.github/skills/business-intent-alignment` and
   `.github/skills/business-to-technical-translation` as:
   - primary:
     - `workflow dependency`
     - `artifact dependency`
   - secondary:
     - `contract dependency`
     - `source/path dependency`
7. Do not classify those planning spine skills as primary
   `runtime/tooling blocker`.
8. Do not modify any skill folder, contract surface, governance artifact, or
   runtime/tooling surface.
9. Do not perform promotion, release, installer, or path-cutover work.
10. Hand the resulting inventory evidence to independent review before any
    post-approval branch routing.

## Validation / Acceptance Checks

- The phase still reads as runway inventory work, not migration execution.
- Only `docs/migration/platform-coupling-inventory.md` is modified during
  bounded implementation.
- No `.github/skills/*` or `skills/*` content is modified.
- No creator / reviewer / template contract surface is modified.
- No runtime/tooling blocker surface is modified.
- No wording declares `skills/` already active today.
- No wording declares `.github/skills/` already demoted from current active
  path today.
- `.github/skills/business-intent-alignment` and
  `.github/skills/business-to-technical-translation` are classified with the
  required primary and secondary dependency classes.
- Those two planning spine skills are not misclassified as primary
  `runtime/tooling blocker`.
- The resulting phase branch is intended to merge back into
  `feat/andrew/copilot-to-codex-migration`, not directly into `dev`.

## Implementer Handoff Prompt

```md
你現在在 worktree
`<phase worktree path prepared by Main Agent for platform-coupling-inventory>`
中工作。

你的 branch 是：
`feat/andrew/platform-coupling-inventory`

你的 base / PR target branch 是：
`feat/andrew/copilot-to-codex-migration`

你的角色是：
- Bounded Implement Agent
- 只執行 `platform-coupling-inventory` 這一個 phase
- 不可自行擴 scope
- 不可修改 planning artifact

請先讀以下 source-of-truth artifacts，依此優先順序執行：
1. `plan/platform-coupling-inventory/platform-coupling-inventory.plan.md`
2. `analysis/codex-migration-runway/technical-spec.md`
3. `analysis/codex-migration-runway/requirements.md`
4. `plan/positioning-freeze/positioning-freeze.plan.md`
5. `AGENTS.md`
6. `docs/repo-positioning.md`
7. `.github/copilot-instructions.md`

你的 allowed writable path 只有：
- `docs/migration/platform-coupling-inventory.md`

以下都只能讀，不能改：
- `plan/platform-coupling-inventory/platform-coupling-inventory.plan.md`
- `analysis/codex-migration-runway/technical-spec.md`
- `analysis/codex-migration-runway/requirements.md`
- `plan/positioning-freeze/positioning-freeze.plan.md`
- `AGENTS.md`
- `docs/repo-positioning.md`
- `.github/copilot-instructions.md`
- `.github/skills/*`
- `skills/*`
- `README.md`
- `VERSION`
- `.codex/*`
- `.claude/*`

這個 phase 的目標：
- 只做 inventory
- 不做 migration
- 不做 active-path cutover
- 不做 creator / reviewer / template contract transition
- 不做 runtime/tooling transition

你必須：
- 對 `.github/skills/business-intent-alignment` 與
  `.github/skills/business-to-technical-translation` 使用固定分類：
  - primary:
    - `workflow dependency`
    - `artifact dependency`
  - secondary:
    - `contract dependency`
    - `source/path dependency`
- 不可把這兩個 planning spine skills 誤標為 primary
  `runtime/tooling blocker`

stop conditions：
- 你需要修改 allowed path 以外的任何檔案
- 你需要修改 `.github/skills/*` 或 `skills/*` 才能完成這個 phase
- 你需要修改 creator / reviewer / template contract surfaces 才能完成這個 phase
- 你需要修改 runtime/tooling surfaces 才能完成這個 phase
- 你需要宣告 `.github/skills/` 不再是 current active path
- 你需要宣告 `skills/` 已是 repo-wide current active path
```

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
- Any later release decision beyond the Big Feature Branch requires a separate
  human-directed topic.
