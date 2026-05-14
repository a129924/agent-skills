# high-frequency-skill-promotion

Analysis-layer routing: **incomplete layer with explicit warning**.
There are no topic-local `analysis/high-frequency-skill-promotion/` artifacts in
this worktree. This plan is authored from the frozen runway baseline, the
runway checklist, the repo-visible inventory evidence, and the already-merged
`skill-authoring-path-transition` phase contract.

Upstream authority chain:

- `plan/platform-coupling-inventory/platform-coupling-inventory.plan.md` is
  present and readable in this worktree.
- `docs/migration/platform-coupling-inventory.md` remains the paired upstream
  evidence artifact and does not replace the plan contract.
- Source-of-truth interpretation for inherited boundaries must read the
  upstream inventory plan contract before its evidence artifact, then follow
  the remaining runway and positioning sources.

## Goal / Outcome

- Produce a review-ready phase plan for `high-frequency-skill-promotion`.
- Promote only a bounded first wave of high-frequency skills into the
  target-architecture `skills/` tree.
- Keep `.github/skills/` as the current active authored/reviewed workflow path
  during this runway while avoiding dual canonical-source claims.
- Prepare an implementer handoff that limits this phase to selected skills only
  and forbids full-library migration.

## Scope

- **In scope**:
  - `plan/high-frequency-skill-promotion/high-frequency-skill-promotion.plan.md`
    as the planning-owned authoritative execution contract for this phase
  - create `skills/` as needed for the first-wave promotion target
  - create or update:
    - `skills/business-intent-alignment/`
    - `skills/business-to-technical-translation/`
    - `skills/plan-creator/`
    - `skills/plan-reviewer/`
  - create a repo-visible promotion evidence artifact:
    - `docs/migration/high-frequency-skill-promotion.md`

- **Out of scope**:
  - promotion of any skill outside the first-wave list
  - full `.github/skills/` to `skills/` migration
  - changing repo-wide current-state authority in `AGENTS.md` or
    `docs/repo-positioning.md`
  - changing `.github/copilot-instructions.md`
  - changing creator / reviewer / template contracts
  - changing runtime/tooling blocker surfaces
  - changing installer or external deployment assumptions
  - changing `README.md`
  - changing `VERSION`
  - release or tag work
  - deleting `.github/skills/` folders

## Locked Decisions

- This topic is a **runway phase**, not full migration.
- This topic is **not** a stable-library publish topic.
- `.github/skills/` remains the current active authored/reviewed workflow path
  during this runway.
- `skills/` remains the target-architecture tree; promoting selected skills
  here does **not** mean the whole repository has cut over.
- This phase must not let `.github/skills/` and `skills/` become dual canonical
  sources.
- During this phase, the canonical-source claim for promoted skills must be
  one-way and explicit:
  - `skills/<skill-name>/` is the target-architecture promotion source for the
    selected wave
  - `.github/skills/<skill-name>/` remains the current active consumer-facing
    path during transition
  - `.github/skills/<skill-name>/` must not be re-declared as a second
    canonical source for the same promoted skill
- The first wave must explicitly re-evaluate at least these four skills:
  - `.github/skills/business-intent-alignment`
  - `.github/skills/business-to-technical-translation`
  - `.github/skills/plan-creator`
  - `.github/skills/plan-reviewer`
- Planning spine skills remain tracked planning dependencies, not default
  blockers.
- This phase must not silently widen into runtime/tooling repair, creator path
  repair, or governance rewrite.
- `plan/high-frequency-skill-promotion/high-frequency-skill-promotion.plan.md`
  remains planning-owned, authoritative, and read-only for Bounded Implement
  Agent during execution.

## First-Wave Skill List and Selection Rationale

### Selected first-wave promotion set

1. `business-intent-alignment`
2. `business-to-technical-translation`
3. `plan-creator`
4. `plan-reviewer`

### Why these four are selected

| Skill | Why it qualifies as first-wave high-frequency promotion |
| --- | --- |
| `business-intent-alignment` | Mandatory planning-spine input in the runway baseline; referenced across runway analysis, checklist, inventory, and planning topics; promotes the top-of-funnel requirements artifact used by later phases |
| `business-to-technical-translation` | Mandatory planning-spine input in the runway baseline; directly produces technical specs consumed by later planning and implementation handoffs; high cross-topic dependency with no default runtime/tooling-blocker classification |
| `plan-creator` | Highest repo-visible reference frequency among the four candidates; central to `plan/<topic>/<topic>.plan.md` creation, strict-mode routing, artifact-path contracts, and workflow transitions |
| `plan-reviewer` | High repo-visible reference frequency and direct gatekeeper role before creator execution; forms a closed planning loop with `plan-creator` and the planning spine inputs |

### Why adjacent skills are not in this first wave

- `agent-skill-creator`, `agent-skill-reviewer`, and `agent-skill-template` are
  contract-transition surfaces, not the first-wave promotion target for this
  topic.
- `sense-env-scaffold`, `plan-step-tracker`, `python-project-init-greenfield`,
  `python-project-retrofit`, and `copilot-instructions-init` remain
  runtime/tooling blockers per inventory evidence and are excluded from this
  promotion wave.
- This phase is intentionally biased toward a bounded planning loop rather than
  breadth across the whole library.

## Boundaries / Exclusions

- Setup Agent owns the runway baseline, this phase plan, and the implementer
  handoff contract.
- Bounded Implement Agent owns only the first-wave promotion execution inside
  the allowed writable paths.
- Reviewer owns review verdict only.
- This phase must not author adjacent phase plans.
- This phase must not repair missing upstream plan contracts by inventing them.
- This phase must not broaden into global current-state rewrite just because the
  selected promotion set is important.
- If the selected-wave promotion cannot be expressed without changing
  forbidden-path governance artifacts, execution must stop and route back to
  Setup Agent.

## Status / Allowed Transitions

- **Current**: `planned`
- **Execution model**: follow the canonical
  `creator -> reviewer -> publish -> merge` workflow path for this topic; no
  repository release action is declared here
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

- Merge routing belongs to branch policy, not phase status vocabulary.
- Active bounded implementation for this topic is limited to the creator /
  reviewer portion of the canonical workflow plus Main Agent publish / merge
  routing.
- If approved, the resulting phase branch merges back into
  `feat/andrew/copilot-to-codex-migration` first.
- Direct merge from a phase branch to `dev` is not authorized.
- No repository release action is part of this phase.

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/high-frequency-skill-promotion/high-frequency-skill-promotion.plan.md` | Setup Agent / Planning actor | Repo-visible authoritative execution contract for this phase; read-only for Bounded Implement Agent |
| Promotion evidence | `docs/migration/high-frequency-skill-promotion.md` | Bounded Implement Agent | Repo-visible record of first-wave selected skills, source-authority statement, and promotion result |
| Target tree root | `skills/` | Bounded Implement Agent | Target-architecture root to be materialized for the selected wave if absent |
| First-wave target folder | `skills/business-intent-alignment/` | Bounded Implement Agent | Target-architecture promotion copy for the selected planning-spine skill |
| First-wave target folder | `skills/business-to-technical-translation/` | Bounded Implement Agent | Target-architecture promotion copy for the selected planning-spine skill |
| First-wave target folder | `skills/plan-creator/` | Bounded Implement Agent | Target-architecture promotion copy for the selected high-frequency planning skill |
| First-wave target folder | `skills/plan-reviewer/` | Bounded Implement Agent | Target-architecture promotion copy for the selected high-frequency planning skill |
| Current active source | `.github/skills/business-intent-alignment/` | Bounded Implement Agent | Current active transition-era source used as the promotion input for this selected skill |
| Current active source | `.github/skills/business-to-technical-translation/` | Bounded Implement Agent | Current active transition-era source used as the promotion input for this selected skill |
| Current active source | `.github/skills/plan-creator/` | Bounded Implement Agent | Current active transition-era source used as the promotion input for this selected skill |
| Current active source | `.github/skills/plan-reviewer/` | Bounded Implement Agent | Current active transition-era source used as the promotion input for this selected skill |

Artifact path notes:

- This phase does **not** modify `README.md`.
- This phase does **not** modify `VERSION`.
- This phase does **not** modify `AGENTS.md`, `docs/repo-positioning.md`, or
  `.github/copilot-instructions.md`.
- This phase does **not** modify creator / reviewer / template contract
  surfaces.
- If later work drifts outside the listed paths, stop and return to planning.

## Implementation Steps

1. Start from the source-of-truth order listed in the implementer handoff.
2. Treat this topic plan as the authoritative read-only contract during bounded
   implementation.
3. Reconfirm the first-wave selection against repo-visible evidence before
   changing files:
   - `business-intent-alignment`
   - `business-to-technical-translation`
   - `plan-creator`
   - `plan-reviewer`
4. Materialize `skills/` if it does not yet exist.
5. Create or update the four selected target folders under `skills/`.
6. Populate those target folders from the current active `.github/skills/`
   source folders without promoting any additional skill.
7. In `docs/migration/high-frequency-skill-promotion.md`, record:
   - the first-wave skill set
   - the source-authority rule for the wave
   - the fact that `.github/skills/` remains the current active path during the
     runway
   - the fact that this phase does not authorize full-library cutover
8. Do not modify runtime/tooling blocker surfaces.
9. Do not declare `skills/` the new repo-wide current active path.
10. Hand the resulting diff to independent review before post-approval branch
    routing.

## Validation / Acceptance Checks

- Only the first-wave selected skills are promoted in this phase.
- No unselected `.github/skills/*` folder is materialized under `skills/`.
- `skills/` and `.github/skills/` are not described as dual canonical sources.
- The promotion evidence artifact explicitly states the one-way authority rule
  for the selected wave.
- `.github/skills/` remains described as the current active path during the
  runway.
- No creator / reviewer / template contract surface is modified.
- No runtime/tooling blocker surface is modified.
- No repo-wide governance artifact (`AGENTS.md`, `docs/repo-positioning.md`,
  `.github/copilot-instructions.md`) is modified.
- No `README.md` or `VERSION` change is introduced.
- The resulting phase branch is intended to merge back into
  `feat/andrew/copilot-to-codex-migration`, not directly into `dev`.

## Implementer Handoff Prompt

```md
你現在在 worktree
`<phase worktree path prepared by Main Agent for high-frequency-skill-promotion>`
中工作。

你的 branch 是：
`feat/andrew/high-frequency-skill-promotion`

你的 base / PR target branch 是：
`feat/andrew/copilot-to-codex-migration`

你的角色是：
- Bounded Implement Agent
- 只執行 `high-frequency-skill-promotion` 這一個 phase
- 不可自行擴 scope
- 不可修改 planning artifact

請先讀以下 source-of-truth artifacts，依此優先順序執行：
1. `plan/high-frequency-skill-promotion/high-frequency-skill-promotion.plan.md`
2. `docs/migration/migration-runway-checklist.md`
3. `plan/platform-coupling-inventory/platform-coupling-inventory.plan.md`
4. `docs/migration/platform-coupling-inventory.md`
5. `plan/skill-authoring-path-transition/skill-authoring-path-transition.plan.md`
6. `analysis/codex-migration-runway/technical-spec.md`
7. `analysis/codex-migration-runway/requirements.md`
8. `plan/positioning-freeze/positioning-freeze.plan.md`
9. `AGENTS.md`
10. `docs/repo-positioning.md`

upstream authority chain：
- `plan/platform-coupling-inventory/platform-coupling-inventory.plan.md`
  現在已存在且可讀。
- 你必須先讀 upstream inventory plan contract，再讀
  `docs/migration/platform-coupling-inventory.md` 這份 paired evidence。
- 不可把 evidence 當作 plan contract 的替代品；兩者要一起納入同一條
  source-of-truth 順序。

你的 allowed writable paths 只有：
- `docs/migration/high-frequency-skill-promotion.md`
- `skills/business-intent-alignment/`
- `skills/business-to-technical-translation/`
- `skills/plan-creator/`
- `skills/plan-reviewer/`

以下都只能讀，不能改：
- `plan/high-frequency-skill-promotion/high-frequency-skill-promotion.plan.md`
- `docs/migration/migration-runway-checklist.md`
- `docs/migration/platform-coupling-inventory.md`
- `plan/skill-authoring-path-transition/skill-authoring-path-transition.plan.md`
- `analysis/codex-migration-runway/technical-spec.md`
- `analysis/codex-migration-runway/requirements.md`
- `plan/positioning-freeze/positioning-freeze.plan.md`
- `plan/platform-coupling-inventory/platform-coupling-inventory.plan.md`
- `AGENTS.md`
- `docs/repo-positioning.md`
- `.github/copilot-instructions.md`
- `README.md`
- `VERSION`
- `.github/skills/*`
- `.codex/*`
- `.claude/*`

這個 phase 的目標：
- 只 promote 首波高頻 skills 到 `skills/`
- 不做全量搬遷
- 不做 repo-wide active-path cutover
- 不讓 `.github/skills/` 和 `skills/` 變成雙 canonical source

首波 skill 名單固定為：
- `business-intent-alignment`
- `business-to-technical-translation`
- `plan-creator`
- `plan-reviewer`

你必須：
- 只處理這四個 skill
- 在 repo-visible evidence 中寫清楚首波 source-authority 規則
- 保留 `.github/skills/` 為 runway 期間 current active path 的語義
- 不可宣告全庫已切到 `skills/`

stop conditions：
- 你需要修改 allowed paths 以外的任何檔案
- 你需要修改 `.github/skills/*` 才能完成這個 phase
- 你需要修改 runtime/tooling blocker surfaces 才能完成這個 phase
- 你需要修改 creator / reviewer / template contract surfaces 才能完成這個 phase
- 你需要修改 `AGENTS.md`、`docs/repo-positioning.md` 或
  `.github/copilot-instructions.md`
- 你需要把 `docs/migration/platform-coupling-inventory.md` 當作 upstream
  plan contract 的替代品
- 你需要宣告 `.github/skills/` 已不再是 current active path
- 你需要宣告 `skills/` 已經是 repo-wide current active path
- 你打算擴大首波 skill 名單，但沒有新的 repo-visible evidence 與 human
  approval

若觸發 stop condition，請只回報：
- exact file/path
- 為何它是 blocker
- 為何它超出本 phase scope
- 需要哪個補齊的 upstream contract 或後續 phase 才能處理
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
- If approved and later merged, the phase branch merges back into
  `feat/andrew/copilot-to-codex-migration` first.
- Any later repo-wide cutover, release, or installer action remains a separate
  human-directed step.

## Open Questions / Unresolved Items

- This phase assumes the now-readable upstream inventory plan contract plus its
  paired evidence artifact are sufficient to preserve the inventory-only and
  runway-only boundaries while promoting only the selected first wave.
- This phase assumes first-wave promotion can be expressed without modifying
  repo-wide governance artifacts. If execution disproves that assumption, stop
  and route back to Setup Agent instead of broadening scope.
