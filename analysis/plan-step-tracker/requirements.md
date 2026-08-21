# Requirements — plan-step-tracker

**Status**: FROZEN v2 — C1/C2/C3 已解決  
**Topic path**: `analysis/plan-step-tracker/requirements.md`

---

## Problem Statement

當 Main Agent 或使用者執行多步驟計畫時，需要反覆查詢「哪些步驟完成了、哪些還沒」。
目前每次都讓 Agent 讀取整個計畫文件或一一讀取多個檔案，浪費大量 token。
核心需求是：**以最少 token 成本讀取特定 topic 的步驟狀態**，並在所有步驟未完成時能阻斷（blocking）繼續執行。

---

## Named Actors

| Actor | Description |
| --- | --- |
| Main Agent | 執行 `plan/<topic>/` 計畫的 AI Agent，執行過程中需查詢步驟狀態 |
| User | 直接詢問「目前哪些步驟還沒做完」的人類使用者 |
| Developer / CI | 修改 `step_tracker.py` 後需確保 pytest 通過的開發者或 CI pipeline |

---

## File Structure Convention（已確認）

**Single file per topic（Plan 沒切 → Step 沒切）：**

```
plan/<topic>/
  <topic>.step.md      ← 唯一步驟追蹤檔，鏡像 plan 結構
```

**`.step.md` 內部格式**（由使用者確認）：

```yaml
---
topic: <topic>
phase: implementation
created: YYYY-MM-DD
---

# <topic> — Step Tracking

## Workflow Stages
- [X] plan-authoring
- [ ] implementation

## Implementation Steps

### Group A: <名稱>
- [X] 1. 已完成的步驟
- [ ] 2. 未完成的步驟
```

**分組規則**：Groups 直接從 `plan.md` 的 Implementation Steps 區塊結構複製，不自行創造新分組。

**多檔案情境**：僅當 plan 本身切成多個 `.plan.md` 時，才對應切多個 `.step.md`。

**狀態標記**：`[ ]` = pending，`[X]` = done，位於內容行（非 YAML frontmatter 欄位）。

---

## Measurable Requirements

### R1 — 步驟發現（File Discovery）

- **Actor**: Main Agent / User
- **Condition**: 給定 topic 名稱 `<T>`，`plan/<T>/` 下有至少 0 個 `.step.md` 檔案
- **Observable result**: 輸出所有 `.step.md` 檔案清單（含 step 標題與狀態），**不需讀取每個檔案全文**
- **Metric**: 使用 1 次 grep/glob 呼叫完成發現，不需逐一打開檔案
- **Failure meaning**: 若無法發現步驟，明確回報「topic `<T>` 下無 .step.md 檔案」，不得靜默失敗

### R2 — 讀取全部步驟（read_all）

- **Actor**: Main Agent / User
- **Condition**: topic 下有 N 個 `.step.md` 檔案（N ≥ 0）
- **Observable result**: 輸出所有步驟的標題 + 狀態（done/pending），無需完整文件內容
- **Metric**: 不得因 N > 20 而讀取超過必要 token

### R3 — 只讀未完成步驟（read_not_run）

- **Actor**: Main Agent / User
- **Condition**: topic 下有混合狀態步驟
- **Observable result**: 僅輸出 pending 步驟；已完成步驟不出現在輸出
- **Metric**: 輸出不含任何 done 步驟
- **Failure meaning**: 若全部完成，回報「所有步驟已完成」

### R4 — 只讀已完成步驟（read_success）

- **Actor**: Main Agent / User
- **Condition**: topic 下有混合狀態步驟
- **Observable result**: 僅輸出 done 步驟；pending 步驟不出現在輸出
- **Metric**: 輸出不含任何 pending 步驟

### R5 — 全完成驗證（check_all_succeeded）

- **Actor**: Main Agent（通常為計畫執行到結尾時自動觸發）/ User
- **Condition**: 需在進入下一個主要階段前確認所有步驟完成
- **Observable result**: 若所有步驟為 done → 回傳「SUCCESS：所有 N 個步驟已完成」；若有任意 pending → **阻斷執行並列出所有未完成步驟**（blocking）
- **Metric**: 輸出清楚標示 SUCCESS 或 BLOCKED，不得模糊化結果
- **Failure meaning**: pending 步驟存在 = 不可繼續；必須列出待辦清單

### R8 — Python CLI 工具（step_tracker.py）

- **Actor**: Main Agent / User / CI
- **Condition**: 需在終端機環境中執行步驟狀態查詢（不依賴 grep 直接命令）
- **Observable result**: 可用 `python scripts/step_tracker.py <operation> <topic>` 執行 4 種操作，輸出與 grep 等效但更結構化
- **Metric**: CLI 正常執行時 exit code 0；`check_all_succeeded` 有 pending 時 exit code 1（供 CI blocking 使用）
- **Failure meaning**: 若找不到 `.step.md` 檔案，明確輸出錯誤訊息並 exit code 1（不靜默失敗）

### R9 — pytest 測試覆蓋

- **Actor**: Developer / CI
- **Condition**: `step_tracker.py` 任何邏輯修改後，CI 必須能驗證正確性
- **Observable result**: `pytest .github/skills/plan-step-tracker/tests/` 全部通過
- **Metric**: 測試必須覆蓋以下 6 個範疇（缺任一視為測試不完整）：
  1. `parse_status`：`- [X]` 解析為 done，`- [ ]` 解析為 pending，其他行不誤判
  2. `read_not_run`：只回傳 pending 行，不含任何 done
  3. `read_success`：只回傳 done 行，不含任何 pending
  4. `read_all`：回傳全部狀態行，數量與 `.step.md` 中的 checkbox 行一致
  5. `check_all_succeeded`：全完成 → SUCCESS + exit 0；有 pending → BLOCKED + 清單 + exit 1
  6. **Edge cases**：空檔案、`.step.md` 不存在（FileNotFoundError）、內容無任何 checkbox 行
- **Failure meaning**: 任何測試失敗 = 程式碼回歸，不可 ship



- **Actor**: Main Agent
- **Condition**: topic 有 1～100+ 個 `.step.md` 檔案
- **Observable result**: 所有 R1～R5 操作不需讀取每個 `.step.md` 的完整內文來判斷狀態
- **Metric**: 狀態判斷基於輕量讀取（frontmatter 或首行），完整內文只在明確要求時讀取
- **Decision rule**: 任何操作若需讀取 N 個完整檔案才能回答「這步驟是 done 還是 pending」，則設計不合格

---

## Status Format Decision（C1 已解決）

**決定**：使用內容行的 `[ ]`/`[X]` 標記（非 YAML frontmatter status 欄位）。

格式為每個步驟行以 `- [ ]` 或 `- [X]` 開頭。False positive 風險已排除：
- YAML frontmatter 行（`---`、`topic:`）不符合 `^\- \[ \]` 模式
- 標題行（`#`、`##`、`###`）不符合
- 僅 `- [ ]` 或 `- [X]` 開頭的內容行才被 grep 捕捉

對應 grep 模式：
- pending: `grep -n '^\- \[ \]' plan/<topic>/<topic>.step.md`
- done: `grep -n '^\- \[X\]' plan/<topic>/<topic>.step.md`
- all: `grep -n '^\- \[.\]' plan/<topic>/<topic>.step.md`
- count pending: `grep -c '^\- \[ \]' plan/<topic>/<topic>.step.md` → 0 = all done

**C1 矛盾已解決，無遺留 blocker。**

---

## Explicit Assumptions

1. Steps 僅存在於 `plan/<topic>/` 目錄下，不跨 topic 查詢
2. 每個 topic 的 steps 數量上限為合理範圍（< 200），不需分頁
3. 狀態是二元的：done 或 pending（不支援 in_progress、blocked 等中間狀態）
4. `.step.md` 副檔名本身就是識別依據，不需額外 metadata
5. 此 Skill 為**唯讀**——不負責修改步驟狀態
6. Python 3.11+（與現有 `apply_toolconfig.py` 一致的 `# /// script` uv 格式）
7. 測試用 `tmp_path` fixture 建立暫存 `.step.md`，不讀真實的 `plan/` 目錄

---

## Non-Goals

- 跨 topic 的彙總查詢（如「所有 plan 中未完成的步驟」）
- 即時監控（file watching）
- 修改或更新步驟狀態
- 與 SQL todos 表整合（獨立機制）
- 支援非 `.step.md` 檔案
- 提供 integration test（只做 unit test，不需啟動真實 Agent）

---

## Contradiction Log

| ID | Statement A | Statement B | Conflict | Decision |
| --- | --- | --- | --- | --- |
| C1 | ~~使用者偏好 `[ ]`/`[X]` 內容標記~~ | ~~內文可能有 false positive~~ | ~~無法保證唯一性~~ | **✅ 已解決**：內容行 `^\- \[.\]` 開頭，frontmatter/標題不符合此模式，無 false positive |
| C2 | check_all_succeeded 應阻斷執行（blocking） | Skill 本身無法實際阻止 agent 繼續 | Skill 只能輸出訊號，agent 必須遵守 | **由 SKILL.md 的指令強制 agent 行為；Python CLI 以 exit code 1 支援 CI blocking** |
| C3 | Python CLI（R8）與 grep-based Agent Skill（R2-R5）語意重疊 | 兩者都實作 4 種操作 | 是否重複？誰是主？ | **決定**：Python CLI 為主要執行層（可測試、可跨平台）；SKILL.md 指引 Agent 優先呼叫 CLI，grep 為 fallback |

---

## Extreme Boundary Checks

- **0 個步驟**：topic 存在但 `.step.md` 無 checkbox 行 — 回報空清單，不報錯
- **`.step.md` 不存在**：明確 FileNotFoundError，exit code 1，不靜默失敗
- **空檔案**：只有 frontmatter，無 checkbox 行 → 視為 0 pending、0 done
- **全部 done**：read_not_run 回報空清單，check_all_succeeded 回報 SUCCESS
- **全部 pending**：check_all_succeeded 阻斷並列出全部，exit code 1
- **100+ checkbox 行**：Python 逐行解析仍在 < 1 秒內完成（無迴圈複雜度問題）
- **`[x]` 小寫**：`- [x]` 是否視為 done？**需決定**：建議只接受 `[X]` 大寫，`[x]` 視為非法 → 視為 pending，並在輸出警告
- **格式行混入非 checkbox 內容**：`- some text without brackets` 不符合 `^\- \[.\]`，直接忽略

---

## Handoff to Technical Translation

此文件已凍結（v2）。所有需求有明確 actor、條件、可觀察結果與 metric。  
**C1、C2 已解決；C3 已決定（Python CLI 為主執行層）。**  
新增需求 R8（Python CLI）與 R9（Tests）可進入技術翻譯。
