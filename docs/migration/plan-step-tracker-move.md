# plan-step-tracker-move

## Candidate verdict

| Candidate | Verdict | Source path | Target path | Notes |
| --- | --- | --- | --- | --- |
| `plan-step-tracker` | `copied` | `.github/skills/plan-step-tracker/` | `skills/plan-step-tracker/` | Canonical copy added under `skills/`; source skill content remains unchanged during the transition |

## Move result

- Added `skills/plan-step-tracker/` with a canonical copy of:
  - `SKILL.md`
  - `reference.md`
  - `examples.md`
  - `scripts/step_tracker.py`
  - `tests/test_step_tracker.py`
- Treated `step_tracker.py` as a normal skill-local script asset and moved it with the rest of the skill content.
- Kept `.github/skills/plan-step-tracker/` unchanged as the source-side transition artifact for this topic.

## Platform-bound cleanup

- Kept the copied skill content semantically aligned with the source folder.
- Updated only the `skills/` copy where `.github/skills/plan-step-tracker/...` path text was platform-bound:
  - `python skills/plan-step-tracker/scripts/step_tracker.py <operation> <topic>`
- Did not redesign the CLI behavior, supported operations, warning behavior, or tests.

## Explicit non-goals for this topic

- No shim, forwarder, wrapper, alias, adapter, or bridge was introduced.
- No `importlib`-based dynamic loading was introduced.
- No `.codex/skills` work was added.
- No publish, commit, push, or PR handling is part of this topic.

## Workflow contract alignment

- Updated `docs/process/workflows/migration-implementation.workflow.md` in its later execution-contract sections only.
- The workflow now stops at `MIGRATION_STATUS_CONFIRMED` and hands off later commit, push, and PR work to publish workflow handling.
- This keeps the generic implementation workflow aligned with the topic rule that implementation work must not silently perform publish actions.

## Deferred follow-up lanes

- Any future active-path cutover from `.github/skills/` to `skills/`
- Any downstream tooling or documentation retargeting outside this skill folder move
- Any separate topic that explicitly owns `.codex/skills` or other projection surfaces

## Workflow progress summaries

### Step Group 1

- `目前進度`：已將 `dev` 上的錯誤 topic 產物清除，並確認正式 topic work 只保留在 managed worktree。
- `下一步`：在 worktree 內重建 `skills/plan-step-tracker/` canonical copy，移除前一輪錯誤 shim 方向。
- `human check / blocking`：不需要人工確認；重點是避免延續錯誤 worktree 的 shim 設計。

### Step Group 2

- `目前進度`：已重建 canonical copy，且 `.github/skills/plan-step-tracker/` 保持原樣；`step_tracker.py` 已作為 skill 內容直接搬移。
- `下一步`：驗證 source 與 canonical copy 的測試與 CLI 行為一致，並確認 `skills/` 版本只存在去平台綁定差異。
- `human check / blocking`：不需要人工確認；若驗證失敗，需檢查是否誤改功能而非僅改路徑文字。

### Step Group 3

- `目前進度`：已完成 migration report、topic plan、canonical copy 與驗證，topic 未擴及 publish 或其他共享 surface。
- `下一步`：等待 reviewer 依 topic contract 做審閱。
- `human check / blocking`：需要 reviewer/human 做最終審閱；目前沒有已知 blocking defect。
