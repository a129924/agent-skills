# skill-authoring-path-transition

Analysis-layer routing: **strict mode**.
This phase consumes the existing runway baseline plus the repo-visible
inventory evidence. It prepares a bounded contract-transition phase only. It
does not authorize full migration, promotion, or runtime/tooling repair.

## Goal / Outcome

- Produce a review-ready phase plan for `skill-authoring-path-transition`.
- Limit the phase to creator / reviewer / template contract transition only.
- Preserve the runway separation between:
  - inventory
  - contract transition
  - runtime/tooling transition
  - promotion / release work
- Prepare a bounded implement handoff that keeps planning spine skills tracked
  as downstream dependencies instead of default blockers.

## Source-of-Truth Order

Use these repo-visible artifacts in this order:

1. `plan/skill-authoring-path-transition/skill-authoring-path-transition.plan.md`
2. `plan/platform-coupling-inventory/platform-coupling-inventory.plan.md`
3. `docs/migration/platform-coupling-inventory.md`
4. `analysis/codex-migration-runway/technical-spec.md`
5. `analysis/codex-migration-runway/requirements.md`
6. `plan/positioning-freeze/positioning-freeze.plan.md`
7. `AGENTS.md`
8. `docs/repo-positioning.md`

Upstream authority chain:

- `plan/platform-coupling-inventory/platform-coupling-inventory.plan.md` is
  present and readable in this worktree.
- `docs/migration/platform-coupling-inventory.md` remains the paired upstream
  evidence artifact and does not replace the plan contract.
- Inherited stop conditions and role boundaries must be interpreted from the
  upstream plan contract first, then its evidence artifact, before falling
  through to the runway baseline and frozen positioning sources.

## Goal Boundary

- This topic is a **runway phase**, not full migration.
- This topic transitions contract surfaces only.
- This topic does **not** perform promotion.
- This topic does **not** cut over the active path from `.github/skills/` to
  `skills/`.
- This topic does **not** repair runtime/tooling blockers.
- This topic does **not** rewrite governance or positioning authority.

## Scope

- **In scope**:
  - `plan/skill-authoring-path-transition/skill-authoring-path-transition.plan.md`
    as the planning-owned authoritative execution contract for this phase
  - `.github/skills/agent-skill-creator/`
  - `.github/skills/agent-skill-reviewer/`
  - `.github/skills/agent-skill-template/`

- **Out of scope**:
  - `.github/skills/business-intent-alignment/`
  - `.github/skills/business-to-technical-translation/`
  - `.github/skills/sense-env-scaffold/`
  - `.github/skills/plan-step-tracker/`
  - `.github/skills/python-project-init-greenfield/`
  - `.github/skills/python-project-retrofit/`
  - `.github/skills/copilot-instructions-init/`
  - `skills/*`
  - `analysis/*`
  - `docs/repo-positioning.md`
  - `AGENTS.md`
  - `.github/copilot-instructions.md`
  - `README.md`
  - `VERSION`
  - `.codex/*`
  - `.claude/*`
  - any promotion, release, installer, generator, or runtime/tooling transition
    work

## Locked Decisions

- `.github/skills/` remains the current active authored/reviewed workflow path
  during this runway.
- `skills/` remains target architecture only during this runway.
- This phase is limited to creator / reviewer / template contract transition.
- This phase must not silently perform full promotion.
- This phase must not change runtime/tooling surfaces to compensate for missing
  path compatibility.
- This phase must not modify planning spine skill folders directly.
- `.github/skills/business-intent-alignment` and
  `.github/skills/business-to-technical-translation` must be tracked as:
  - downstream consumer / producer dependencies
  - planning spine dependencies
  - not default blockers
- Planning spine skills may be elevated to blocker status only if bounded
  implementation encounters explicit repo-visible evidence that the transition
  cannot proceed without changing them.
- Inventory classifications remain in force unless new repo-visible evidence
  contradicts them.
- `plan/skill-authoring-path-transition/skill-authoring-path-transition.plan.md`
  remains planning-owned, authoritative, and read-only for Bounded Implement
  Agent during execution.

## Dependency Interpretation

### Planning spine skills

- `.github/skills/business-intent-alignment`
- `.github/skills/business-to-technical-translation`

Interpretation rules:

- treat them as downstream dependencies of canonical authoring-target
  transition
- check whether creator / reviewer / template contract wording would later
  require those skills to consume updated canonical authoring-target semantics
- record downstream implications if found
- do not directly modify those skill folders in this phase
- do not escalate them to phase blockers without explicit evidence

### Creator / reviewer / template surfaces

The inventory evidence already identifies these three as path-coupled contract
surfaces:

- `.github/skills/agent-skill-creator/`
- `.github/skills/agent-skill-reviewer/`
- `.github/skills/agent-skill-template/`

This phase exists to transition those surfaces only.

### Runtime / tooling surfaces

The inventory evidence identifies these as runtime/tooling blockers:

- `.github/skills/sense-env-scaffold/`
- `.github/skills/plan-step-tracker/`
- `.github/skills/python-project-init-greenfield/`
- `.github/skills/python-project-retrofit/`
- `.github/skills/copilot-instructions-init/`

They remain tracked blockers, but are not writable in this phase.

## Boundaries / Exclusions

- Setup Agent owns the runway baseline, this phase plan, and the implementer
  handoff contract.
- Bounded Implement Agent owns only the contract-transition execution inside
  the allowed writable paths.
- Reviewer owns review verdict only.
- This phase must not create adjacent phase plans.
- This phase must not repair upstream planning gaps by inventing missing
  contracts.
- This phase must not work around runtime/tooling blockers by broadening into
  executable-surface changes.
- If the required outcome cannot be achieved inside the allowed writable paths,
  execution stops and returns to Setup Agent.

## Status / Allowed Transitions

- **Current**: `planned`
- **Allowed phase statuses**:
  - `planned`
  - `in-progress`
  - `review-ready`
  - `approved`
  - `needs-rework`

- **Allowed transitions**:
  - `planned` -> `in-progress`
  - `in-progress` -> `review-ready`
  - `review-ready` -> `approved`
  - `review-ready` -> `needs-rework`
  - `needs-rework` -> `in-progress`

Routing notes:

- Merge routing belongs to branch policy, not phase status vocabulary.
- If approved, the resulting phase branch merges back into
  `feat/andrew/copilot-to-codex-migration` first.
- Direct merge from a phase branch to `dev` is not authorized.

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/skill-authoring-path-transition/skill-authoring-path-transition.plan.md` | Setup Agent / Planning actor | Repo-visible authoritative execution contract for this phase; read-only for Bounded Implement Agent |
| Upstream inventory plan contract | `plan/platform-coupling-inventory/platform-coupling-inventory.plan.md` | Upstream bounded phase output | Repo-visible upstream execution contract for inherited role boundaries, stop conditions, and inventory-only phase semantics |
| Inventory evidence | `docs/migration/platform-coupling-inventory.md` | Upstream bounded phase output | Repo-visible evidence for dependency and blocker classification, read after the upstream inventory plan contract in the source-of-truth chain |
| Runway technical baseline | `analysis/codex-migration-runway/technical-spec.md` | Setup Agent / Planning actor | Execution-facing runway baseline |
| Runway requirements baseline | `analysis/codex-migration-runway/requirements.md` | Setup Agent / Planning actor | Business-intent boundary baseline |
| Positioning boundary plan | `plan/positioning-freeze/positioning-freeze.plan.md` | Setup Agent / Planning actor | Frozen upstream boundary for current-vs-target wording and non-migration constraints |

Artifact path notes:

- This phase does **not** modify `VERSION`.
- This phase does **not** modify `README.md`.
- This phase does **not** modify any planning artifact during bounded
  implementation.
- This phase may read planning spine skills for downstream impact checking, but
  may not modify them.

## Allowed / Forbidden Paths

### Allowed writable paths for Bounded Implement Agent

- `.github/skills/agent-skill-creator/`
- `.github/skills/agent-skill-reviewer/`
- `.github/skills/agent-skill-template/`

### Forbidden paths for Bounded Implement Agent

- `plan/skill-authoring-path-transition/skill-authoring-path-transition.plan.md`
- `docs/migration/platform-coupling-inventory.md`
- `analysis/codex-migration-runway/technical-spec.md`
- `analysis/codex-migration-runway/requirements.md`
- `plan/positioning-freeze/positioning-freeze.plan.md`
- `plan/platform-coupling-inventory/platform-coupling-inventory.plan.md`
- `.github/skills/business-intent-alignment/`
- `.github/skills/business-to-technical-translation/`
- `.github/skills/sense-env-scaffold/`
- `.github/skills/plan-step-tracker/`
- `.github/skills/python-project-init-greenfield/`
- `.github/skills/python-project-retrofit/`
- `.github/skills/copilot-instructions-init/`
- `skills/*`
- `.github/copilot-instructions.md`
- `AGENTS.md`
- `docs/repo-positioning.md`
- `README.md`
- `VERSION`
- `.codex/*`
- `.claude/*`

## Implementation Steps

1. Start from the source-of-truth order listed in this plan.
2. Treat this topic plan as the authoritative read-only contract during bounded
   implementation.
3. Use `docs/migration/platform-coupling-inventory.md` as the upstream evidence
   source for dependency and blocker interpretation.
4. Transition creator / reviewer / template contracts only within the allowed
   writable paths.
5. Update those contracts so they align to canonical authoring-target
   transition semantics without claiming that the repo has already completed
   active-path cutover.
6. Check whether the new creator / reviewer / template wording introduces
   downstream implications for:
   - `.github/skills/business-intent-alignment`
   - `.github/skills/business-to-technical-translation`
7. If downstream implications exist, record them inside the modified
   creator/reviewer/template contract surfaces or review notes without editing
   the planning spine skill folders themselves.
8. Do not modify runtime/tooling blocker surfaces.
9. Do not perform promotion, release, installer, or path-cutover work.
10. Hand the resulting diff to independent review before post-approval branch
    routing.

## Validation / Acceptance Checks

- The phase still reads as runway contract transition work, not full migration.
- Only creator / reviewer / template contract surfaces are modified.
- No planning artifact is modified during bounded implementation.
- No planning spine skill folder is modified.
- No runtime/tooling blocker surface is modified.
- No wording declares `skills/` already active today.
- No wording declares `.github/skills/` already demoted to projection today.
- Creator / reviewer / template surfaces stay mutually consistent about the
  canonical authoring-target transition.
- Planning spine skills remain classified as tracked downstream dependencies
  unless explicit evidence forces escalation.
- If escalation is required, the implementing agent stops and reports exact
  evidence instead of widening scope.
- The resulting phase branch is intended to merge back into
  `feat/andrew/copilot-to-codex-migration`, not directly into `dev`.

## Implementer Handoff Prompt

```md
你現在在 worktree
`/Users/andrew/code/python/agent-skills.worktrees/feat-andrew-copilot-to-codex-migration`
中工作。

你的 branch 是：
`feat/andrew/copilot-to-codex-migration`

你的 phase branch 應從這條 branch 切出，並回 merge 到：
`feat/andrew/copilot-to-codex-migration`

你的角色是：
- Bounded Implement Agent
- 只執行 `skill-authoring-path-transition` 這一個 phase
- 不可自行擴 scope
- 不可修改 planning artifact

請先讀以下 source-of-truth artifacts，依此優先順序執行：
1. `plan/skill-authoring-path-transition/skill-authoring-path-transition.plan.md`
2. `plan/platform-coupling-inventory/platform-coupling-inventory.plan.md`
3. `docs/migration/platform-coupling-inventory.md`
4. `analysis/codex-migration-runway/technical-spec.md`
5. `analysis/codex-migration-runway/requirements.md`
6. `plan/positioning-freeze/positioning-freeze.plan.md`
7. `AGENTS.md`
8. `docs/repo-positioning.md`

upstream authority chain：
- `plan/platform-coupling-inventory/platform-coupling-inventory.plan.md`
  現在已存在且可讀。
- 你必須先讀 upstream plan contract，再讀
  `docs/migration/platform-coupling-inventory.md` 這份 paired evidence。
- 不可把 evidence 當作 plan contract 的替代品；兩者要一起納入同一條
  source-of-truth 順序。

你的 allowed writable paths 只有：
- `.github/skills/agent-skill-creator/`
- `.github/skills/agent-skill-reviewer/`
- `.github/skills/agent-skill-template/`

以下都只能讀，不能改：
- `plan/skill-authoring-path-transition/skill-authoring-path-transition.plan.md`
- `docs/migration/platform-coupling-inventory.md`
- `analysis/codex-migration-runway/technical-spec.md`
- `analysis/codex-migration-runway/requirements.md`
- `plan/positioning-freeze/positioning-freeze.plan.md`
- `plan/platform-coupling-inventory/platform-coupling-inventory.plan.md`
- `.github/skills/business-intent-alignment/`
- `.github/skills/business-to-technical-translation/`
- `.github/skills/sense-env-scaffold/`
- `.github/skills/plan-step-tracker/`
- `.github/skills/python-project-init-greenfield/`
- `.github/skills/python-project-retrofit/`
- `.github/skills/copilot-instructions-init/`
- `skills/*`
- `.github/copilot-instructions.md`
- `AGENTS.md`
- `docs/repo-positioning.md`
- `README.md`
- `VERSION`
- `.codex/*`
- `.claude/*`

這個 phase 的目標：
- 只做 creator / reviewer / template contract transition
- 不做 full promotion
- 不做 runtime/tooling transition
- 不做 active-path cutover
- 不做 planning spine skill folder 修改

對 planning spine skills 的處理方式：
- `.github/skills/business-intent-alignment`
- `.github/skills/business-to-technical-translation`

你必須：
- 只把它們視為 downstream consumer / producer dependencies
- 檢查 creator / reviewer / template contract transition 是否會對它們造成
  downstream implication
- 若有 implication，記錄 follow-up impact
- 不可直接修改它們
- 不可把它們抬升成 phase blocker，除非有明確 repo-visible evidence

stop conditions：
- 你需要修改 allowed paths 以外的任何檔案
- 你需要直接修改 planning spine skills
- 你需要修改 runtime/tooling blocker surfaces 才能完成這個 phase
- 你需要把 `docs/migration/platform-coupling-inventory.md` 當作 upstream plan
  contract 的替代品
- 你需要宣告 `.github/skills/` 已不再是 current active path
- 你需要宣告 `skills/` 已經是 current active path
- 你需要混入 promotion / release / installer work
- 你打算把 planning spine skills 重新分類成 blocker，但沒有明確
  repo-visible evidence

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
  "dependency_escalations": [],
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
- Any later integration beyond the Big Feature Branch remains a separate
  human-directed step.

## Open Questions / Unresolved Items

- This phase assumes the now-readable upstream inventory plan contract plus its
  paired evidence artifact are sufficient to preserve the inventory-only
  boundary without broadening into promotion, runtime/tooling transition, or
  governance rewrite.
- If execution encounters a dependency that would require changing forbidden
  paths despite that readable upstream chain, the phase must still stop and
  return to Setup Agent rather than broadening scope.
