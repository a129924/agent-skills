# Platform Projection Adapter Requirements

## Baseline

- Topic: `platform-projection-adapter`
- Status: `FROZEN`
- Scope type: planning-only baseline for a later implementation topic

## Problem Statement

本 repo 已凍結 `skills/` 為 canonical source，但多個 canonical skill 內容仍以
`.<platform>/...` 描述平台投影位置。需要一個可重複執行、預設安全、可摘要回報的
轉換能力，把整個 canonical `skills/` library 投影到呼叫者指定的平台 root
（例如 `.codex`），同時禁止任何對 canonical `skills/` 的回寫。

## Actors

- Human operator: 指定 `--platform-root`，決定只看 dry-run 還是允許 `--apply`
- Planning actor: 凍結需求、技術規格與 topic plan
- Creator / implementer: 實作 CLI 與薄 Agent Skill，但不得擴大範圍
- Reviewer: 驗證 CLI、測試、技能包裝與 write-set 邊界
- Main Agent: 依 workflow 處理後續 review / publish / merge 路由

## Goal

交付一個 `CLI + 薄 Agent Skill` 能力，使呼叫者可以：

1. 從 canonical `skills/` 讀取整個 library。
2. 以顯式 `--platform-root` 指定投影目的地。
3. 先用預設 dry-run 取得完整投影摘要。
4. 僅在顯式 `--apply` 下寫入目標平台 root。
5. 在既有目標內容衝突時，只有顯式 `--force` 才允許覆寫。

## Non-Goals

- 不回寫、重排、或規範化 canonical `skills/`
- 不在 v1 支援部分 skill 投影；v1 一律投影整個 `skills/` library
- 不在 v1 變更 `.github/**`、`.codex/**`、或其他 `.<platform>/**` 既有內容
- 不把 Agent Skill 變成第二套轉換核心；轉換核心只能在 CLI
- 不為 skill 本體建立獨立測試面；自動化測試只落在 CLI
- 不在 v1 刪除 target root 內多餘但非本次投影覆蓋到的檔案

## Requirements

| ID | Requirement | Acceptance signal |
| --- | --- | --- |
| R1 | Canonical source 保護：任何執行模式都只能讀取 `skills/`，不得改寫 canonical library | 執行前後 `skills/` 無新增、刪除、覆寫；topic plan 與 CLI 契約都把 canonical source 視為 read-only |
| R2 | Whole-library projection：v1 必須涵蓋執行當下 `skills/` 底下的全部 regular files，並保留相對路徑 | dry-run 或 apply 摘要能逐一對應每個 source file 到一個 target path；不得只投影單一 skill 子集 |
| R3 | 顯式平台 root：CLI 必須要求 `--platform-root`，不得猜測 `.codex` 或其他具體平台 | 未提供 `--platform-root` 時命令失敗並指出缺少必要參數；提供 `.codex` 時 target path 落在 `.codex/skills/...` |
| R4 | 預設 dry-run：未帶 `--apply` 時只輸出計畫摘要，不寫任何 target file | dry-run 執行後 target root 沒有檔案變更，且摘要至少列出 create / update / noop / conflict 類型 |
| R5 | Apply gating：只有顯式 `--apply` 才允許寫入；若 target 中存在內容衝突，未帶 `--force` 必須整體阻擋寫入 | `--apply` 且無衝突時完成寫入；有衝突且無 `--force` 時 exit 為阻擋狀態，並列出衝突檔案 |
| R6 | Force semantics：顯式 `--force` 只解除受管 target file 的覆寫阻擋，不授權擴大 source 範圍或刪除額外檔案 | 同一組輸入在 `--apply --force` 下可覆寫衝突檔案；未列入本次 projection 的額外 target file 仍保留 |
| R7 | Placeholder projection：canonical 內容中的 `.<platform>/...` 佔位敘述，在 target 內容中必須一致投影為指定 platform root 前綴 | 來源含 `.<platform>/skills/...`、`.<platform>/skills-provenance.json` 等字串時，target 內容改寫為 `<platform-root>/skills/...`、`<platform-root>/skills-provenance.json`；非 placeholder 的 `skills/...` canonical 描述保持不變 |
| R8 | Thin Agent Skill：skill 只負責收參數、預設 dry-run、apply/force gating、以及摘要回報；不得複製或分叉轉換邏輯 | SKILL.md 的流程以呼叫本地 CLI 為主；沒有第二套獨立轉換規則藏在 skill 文案 |
| R9 | CLI-only testing：自動化測試只驗證 CLI 行為，固定命令為 `uv run --with pytest pytest skills/platform-projection-adapter/tests/ -v` | 測試目錄只位於 `skills/platform-projection-adapter/tests/`；topic 驗證與 reviewer 檢查不要求 skill-level 測試 |
| R10 | Summary clarity：每次執行都必須輸出足以讓人判斷是否可安全進入 apply 的摘要 | dry-run / apply 皆輸出 source count、target action counts、衝突數、target root 與模式資訊 |
| R11 | Interrupted / rerun clarity：若 apply 因中斷、權限或衝突失敗，CLI 不得宣稱成功，且下一次 dry-run 必須能重新反映尚未完成的 target state | 失敗 run 回傳非成功狀態並指出原因；重新 dry-run 時仍可看到剩餘 create / update / conflict |

## Boundary Checks

### No network / degraded dependency

- 需求不依賴網路或外部服務。
- 只要本地 `skills/` 可讀、target root 可存取，dry-run 與 apply 就必須可執行。

### Wrong role / missing approval

- 未帶 `--apply` 視為沒有寫入授權。
- 未帶 `--force` 視為沒有覆寫既有衝突 target 的授權。

### Interrupted / partial completion

- apply 中斷後不得輸出成功摘要。
- 部分寫入若已發生，下一次 dry-run 仍必須據實呈現目前 target state，而不是假設全量完成。

### Low-volume / peak-volume

- 無論 `skills/` 當下檔案數量高低，行為模型不變：仍是 whole-library discovery、dry-run summary、apply gating。
- 需求不允許以「量太大」為理由降級成部分投影。

## Assumptions

- 目前 canonical `skills/` library 為可解碼的文字檔為主；若未來出現不支援的檔案型別，CLI 應明確失敗而非靜默跳過
- `--platform-root` 可由呼叫者顯式提供為 repo-relative 或其他可存取路徑；v1 不替呼叫者推測平台名稱
- topic 的當前工作僅凍結 planning / analysis artifact，不執行 implementation

## Resolved Contradictions

- `CLI 是唯一轉換核心` 與 `需要 Agent Skill 入口` 並不衝突；已凍結為「skill 只做包裝與 gating，邏輯全部留在 CLI」
- `v1 採 whole-library projection` 與 `風險控制` 並不衝突；已凍結為「靠 dry-run / apply / force gating 控制風險，而不是縮小投影範圍」
- `canonical source 不可回寫` 與 `平台投影需要改寫 placeholder 文案` 並不衝突；已凍結為「只改寫 target 內容，不改 source」

## Blocker Status

無 blocker。現有凍結背景足以安全產出技術規格與 topic plan。
