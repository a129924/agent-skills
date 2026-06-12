# Technical Specification: platform-projection-adapter

**Status**: `READY FOR EXECUTION PLANNING`  
**Topic**: `platform-projection-adapter`  
**Baseline Reference**: `analysis/platform-projection-adapter/requirements.md`

---

## Source Baseline Summary

這個 topic 需要一個以 CLI 為核心的 whole-library projection adapter：

- source of truth 固定為 read-only 的 `skills/`
- caller 以顯式 `--platform-root` 指定 target root
- 預設 dry-run；只有 `--apply` 可寫入；既有衝突僅 `--force` 可覆寫
- Agent Skill 只是薄包裝層，不得分叉轉換邏輯
- 自動化測試只驗證 CLI，固定命令為
  `uv run --with pytest pytest skills/platform-projection-adapter/tests/ -v`

## Translation Stance

本 spec 以悲觀實作者視角翻譯 frozen baseline：

- 假設 target root 可能已存在既有內容，不能靜默覆寫
- 假設 future caller 會反覆 dry-run / apply，需要穩定且可重跑的摘要
- 假設 repo 目前不接受對 `.github/**`、`.codex/**` 或 `skills/` 進行同 topic 混合改寫
- 假設 runtime target path 屬於執行時輸入，不是 repo-visible implementation artifact

若 implementation 需要：

- 改寫 canonical `skills/`
- 把 projection scope 縮成單一 skill 子集
- 在 skill 包裝層新增第二套轉換邏輯
- 對 target root 做刪除式同步

則應回滾到 alignment，而不是擴大此 topic。

## Exact Implementation Write Set

未來 implementation topic 只允許在 repo 內 create / modify 這些路徑：

### Allowed to create

- `skills/platform-projection-adapter/SKILL.md`
- `skills/platform-projection-adapter/examples.md`
- `skills/platform-projection-adapter/reference.md`
- `skills/platform-projection-adapter/scripts/platform_projection_adapter.py`
- `skills/platform-projection-adapter/tests/test_platform_projection_adapter.py`

### Allowed to modify

- `plan/platform-projection-adapter/platform-projection-adapter.step.md`

### Read-only during implementation

- `skills/` 既有 canonical library（除新建 `skills/platform-projection-adapter/` 之外）
- `analysis/platform-projection-adapter/requirements.md`
- `analysis/platform-projection-adapter/technical-spec.md`
- `plan/platform-projection-adapter/platform-projection-adapter.plan.md`
- `.github/**`
- `.codex/**`
- `README.md`
- `VERSION`

說明：

- 執行時 target root 及其投影結果不是 repo-visible implementation artifact；它們由 CLI 在 runtime 依 `--platform-root` 產生與驗證。
- `README.md`、`VERSION` 與 release surfaces 在本 topic 明確不納入。

## Requirement-to-Technical Mapping

| Requirement | Technical realization | Dependencies | Cost / burden | Status |
| --- | --- | --- | --- | --- |
| R1 Canonical source protection | CLI 將 `skills/` 視為唯讀輸入；任何 apply 都只寫 target root | repo governance + path discipline | Low | feasible |
| R2 Whole-library projection | 遞迴枚舉 `skills/` 下全部 regular files，保留相對路徑投影到 `<platform-root>/skills/` | `pathlib`, deterministic traversal | Medium | feasible |
| R3 Explicit platform root | argparse / CLI 參數要求 `--platform-root` | Python CLI contract | Low | feasible |
| R4 Default dry-run | 先建 projection plan；未帶 `--apply` 只輸出摘要，不執行 write phase | planning/execution split | Low | feasible |
| R5 Apply gating | `--apply` 啟動 write phase；如有 differing target files 先收集 conflicts 並整體阻擋 | pre-write comparison pass | Medium | feasible |
| R6 Force semantics | `--force` 只解除 managed-target overwrite block；不做 target pruning | overwrite policy | Low | feasible |
| R7 Placeholder projection | 對文字內容做 token rewrite：`.<platform>/` -> normalized `<platform-root>/`；保留非 placeholder canonical `skills/...` 敘述 | text decode + replacement rule | Medium | feasible |
| R8 Thin Agent Skill | SKILL.md 只呼叫本地 CLI，包裝 dry-run / apply / force 與摘要判讀 | skill contract discipline | Low | feasible |
| R9 CLI-only testing | pytest 只針對 `platform_projection_adapter.py`；skill 不另建測試 | fixed test command | Low | feasible |
| R10 Summary clarity | CLI 輸出 mode、platform root、source count、action counts、conflicts | reporting layer | Low | feasible |
| R11 Interrupted / rerun clarity | write phase 不得在失敗時輸出成功；重新 dry-run 以實際 target state 重算 | deterministic reconciliation | Medium | feasible |

## Technical Design

### 1. CLI artifact

建立：

- `skills/platform-projection-adapter/scripts/platform_projection_adapter.py`

建議執行介面：

```bash
uv run skills/platform-projection-adapter/scripts/platform_projection_adapter.py \
  --platform-root .codex
```

```bash
uv run skills/platform-projection-adapter/scripts/platform_projection_adapter.py \
  --platform-root .codex --apply
```

```bash
uv run skills/platform-projection-adapter/scripts/platform_projection_adapter.py \
  --platform-root .codex --apply --force
```

最小參數面：

- `--platform-root <path>`: required
- `--apply`: optional; absent means dry-run
- `--force`: optional; only meaningful with `--apply`

建議輸出結構：

- mode: `dry-run` or `apply`
- platform root
- source file count
- action counts: `create`, `update`, `noop`, `conflict`
- path list for create/update/conflict entries
- final result line: `SAFE_TO_APPLY`, `APPLIED`, or `BLOCKED`

### 2. Discovery and path mapping

Projection source:

- repo-root `skills/`

Projection target base:

- `<platform-root>/skills/`

Path rule:

1. 枚舉 `skills/` 下全部 regular files。
2. 對每個 source file 保留 `skills/` 之下的相對路徑。
3. 對應 target path 為 `<platform-root>/skills/<relative-path>`.

範例：

- `skills/python-project-init-greenfield/SKILL.md`
  -> `<platform-root>/skills/python-project-init-greenfield/SKILL.md`
- `skills/python-project-init-greenfield/references/baseline-generation-rules.md`
  -> `<platform-root>/skills/python-project-init-greenfield/references/baseline-generation-rules.md`

### 3. Content rewrite rule

v1 rewrite contract 僅處理 canonical 內容中的平台 placeholder：

- literal token `.<platform>/`
- replacement prefix: normalized `<platform-root>/`

Examples:

- `.<platform>/skills/sense-env-scaffold/scripts/sense_env.py`
  -> `.codex/skills/sense-env-scaffold/scripts/sense_env.py`
- `.<platform>/skills-provenance.json`
  -> `.codex/skills-provenance.json`

Non-rewrite examples:

- `skills/` canonical-source 聲明維持原樣
- 非 placeholder 的一般文字不做額外 normalization

v1 假設 current library 為 UTF-8 text-first surface。若 source file 無法以預期文字模式解碼，CLI 應 fail fast 並將該 file 視為 blocker，而不是靜默略過或輸出損壞內容。

### 4. Planning phase before writes

CLI 先建立一份 in-memory projection plan，對每個 source file 產出其中一種動作：

- `create`: target file 不存在
- `update`: target file 存在但內容不同
- `noop`: target file 已存在且內容相同
- `conflict`: target file 存在且內容不同，且當前模式不允許覆寫

Policy:

- dry-run：`update` 與 `conflict` 都可在摘要中出現，但不寫入
- `--apply` without `--force`：若存在任何 differing target file，整體回傳 `BLOCKED`
- `--apply --force`：允許將 differing managed target files 轉為 overwrite 寫入

### 5. Write semantics

Apply phase 順序：

1. 完整跑完 discovery + content render + diff classification
2. 若模式為 dry-run，直接輸出摘要結束
3. 若模式為 `--apply` 且存在 blocked conflicts，先輸出衝突摘要再失敗結束
4. 若模式允許寫入，建立必要 parent directories
5. 只寫入本次 source inventory 對應到的 managed target files

v1 明確不做：

- delete / prune target extras
- partial-scope projection
- in-place mutation of source files

### 6. Thin Agent Skill contract

建立：

- `skills/platform-projection-adapter/SKILL.md`
- `skills/platform-projection-adapter/examples.md`
- `skills/platform-projection-adapter/reference.md`

Skill contract:

- 預設示範 dry-run
- 只有在 human 明確要求 apply 時才帶 `--apply`
- 只有在 human 明確允許覆寫時才帶 `--force`
- 讀取 CLI 摘要後回報 create/update/noop/conflict 統計
- 不在 SKILL.md 內重新定義 projection algorithm

### 7. Test strategy

建立：

- `skills/platform-projection-adapter/tests/test_platform_projection_adapter.py`

固定命令：

```bash
uv run --with pytest pytest skills/platform-projection-adapter/tests/ -v
```

測試焦點僅限 CLI：

- required arg validation (`--platform-root`)
- dry-run 不寫入但輸出摘要
- apply create path
- apply blocked on differing target without `--force`
- apply overwrite with `--force`
- whole-library traversal preserves relative paths
- placeholder rewrite correctness
- rerun/noop behavior after successful apply
- failure surface for unreadable or undecodable source input

建議使用 `tmp_path` 建立臨時 source/target fixture，避免依賴真實 `.codex/` 或其他 repo 內 projection surface。

## Cost-of-Realization Assessment

| Workstream | Complexity | Main burden | Ongoing operational cost |
| --- | --- | --- | --- |
| CLI discovery + render plan | Medium | whole-library traversal and deterministic summary | low |
| overwrite / conflict gating | Medium | fail-safe behavior without silent partial success | low |
| placeholder rewrite contract | Medium | preserving canonical wording while rewriting only platform placeholders | low |
| thin skill wrapper | Low | keeping wrapper thin and non-duplicative | low |
| pytest coverage | Low | temp-dir based end-to-end CLI cases | low |

## Architecture / Governance Compliance Check

| Dimension | Result | Notes |
| --- | --- | --- |
| canonical-source governance | fits existing governance | `skills/` stays primary truth and remains read-only |
| platform-surface model | fits existing governance | target root is a projection/compatibility surface, not a new canonical owner |
| bounded implementation write set | fits with prerequisites | implementation only creates one new root skill and updates topic-local step truth |
| `.github/**` / `.codex/**` boundary | fits existing governance | no repo-visible edits under compatibility surfaces are required |
| skill/CLI role separation | fits existing governance | CLI owns transformation; skill only wraps invocation and reporting |
| test placement | fits existing architecture | tests live under the new skill folder and target the CLI only |

## Rollback-to-Alignment Triggers

回到 alignment 而不是直接實作，若出現以下任一情況：

1. stakeholder 要求 v1 支援單一 skill 子集投影，而非 whole-library
2. stakeholder 要求 apply 同步刪除 target extras
3. implementation 發現需要改寫 canonical `skills/` 才能完成 projection
4. implementation 需要在 SKILL.md 之外維護第二套轉換規則或 target-specific branching
5. target root 路徑語義被要求依不同平台做隱式推測，而不是顯式 `--platform-root`

## Ready-for-Next-Step Decision

此 technical spec 已足以驅動嚴格模式的 topic plan 與後續 implementation：

- future creator 只需在 `skills/platform-projection-adapter/` 建立薄 skill、CLI、tests
- projection target content 由 runtime `--platform-root` 決定，不需在 repo 內新增 `.codex/**` 或其他 projection outputs
- README / VERSION / release work 明確不屬於本 topic
