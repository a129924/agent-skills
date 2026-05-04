# Requirements: Python Implementation Workflow

**Status**: frozen — ready for technical translation
**Topic**: `python-implementation-workflow`

---

## Problem Statement

Python 專案開發中缺乏從需求到高品質程式碼的可預測、可審查、可自動化流程，
導致：計劃無法實作（spec 不完整）、實作偏離需求（scope drift）、程式碼品質不可控
（hidden technical debt）。

目前 Agent Skill 生態系中已有 Agent Skill 本身的 creator/reviewer，但缺少針對
**任何 Python 專案** 的開發工作流程支援。

---

## Actors

| Actor | 角色 | 權限 |
|-------|------|------|
| **Python developer** | 主要使用者，撰寫計劃並使用 review skills | 可觸發任何 skill |
| **Executor agent** | 根據 plan 實作代碼，不得自行決定未列的事項 | 只能執行 plan 明確授權的工作 |
| **Plan reviewer** | 獨立審查計劃可執行性 | 只能輸出 `approved` / `needs-rework` |
| **Code reviewer** | 獨立審查程式碼品質 | 只能輸出 `approved` / `needs-rework` |
| **CI/CD pipeline** | 可自動調用 review skills | 依專案配置，無額外權限 |

---

## Measurable Requirements

### R1 — Plan Authoring（可執行契約）

| Element | Requirement |
|---------|-------------|
| Actor | Python developer / planning agent |
| Condition | 當需要為任何 Python 功能建立實作計劃時 |
| Observable result | 輸出 `*.plan.md`，包含 13 個標準節，每節非空且內容可執行 |
| Metric | 缺少任何必要節 → skill 必須停止並要求補齊（不得輸出不完整的 plan） |
| Failure meaning | Executor 無法在不猜測的情況下執行，導致 scope drift 或未授權決策 |

**13 節標準**（全部必要）：
Goal / Non-goals / Current Context / Requirements / Decisions /
Public Contract & API Changes / Affected Files & Modules / Implementation Steps /
Test Plan / Validation Commands / Risks / Rollback Plan / Open Questions

**Decisions 節必須明確回答**（最易自行發揮的 7 項）：
- 新功能放哪個 module / package
- 是否新增 public API
- 是否改動既有 interface
- 是否允許 breaking change
- 是否新增 dependency
- 錯誤處理策略
- typing 策略

### R2 — Plan Review（可執行性驗證）

| Element | Requirement |
|---------|-------------|
| Actor | Plan reviewer agent |
| Condition | 收到一份 `*.plan.md` 草稿 |
| Observable result | 輸出 `approved` 或 `needs-rework`，附帶具體 blocking issues |
| Metric | 若任一必要節缺失或 Implementation Steps 為高階願望而非可執行步驟 → 必須輸出 `needs-rework` |
| Failure meaning | 不合格的 plan 進入實作 → executor 自行猜測 → scope drift |

**「Can this be executed without guessing?」** 是驗收標準。

### R3 — Implementation Review（對齊性驗證）

| Element | Requirement |
|---------|-------------|
| Actor | Implementation reviewer agent |
| Condition | 收到一份已實作的 code change + 對應的已核准 `*.plan.md` |
| Observable result | 逐一比對 Implementation Steps、Non-goals、Public Contract |
| Metric | 任一 Step 未完成 → `needs-rework`；任何 Non-goals 邊界被跨越 → `needs-rework` |
| Failure meaning | 對「錯的實作」做後續優化，資源浪費且掩蓋偏差 |

**「Does the implementation satisfy the approved plan?」** 是驗收標準。

### R4 — Code Review（品質驗證）

| Element | Requirement |
|---------|-------------|
| Actor | Code reviewer agent |
| Condition | 收到一份已通過 implementation review 的 code change |
| Observable result | 依專案配置偵測工具，輸出 `approved` / `needs-rework` + 分類問題清單 |
| Metric | typing / lint / readability / error handling / test quality 各維度有明確判斷 |
| Failure meaning | Hidden technical debt 進入 codebase，未來維護成本上升 |

**工具偵測順序**：`pyproject.toml` → `Makefile` → `README` → 通用 fallback。
**「Is this good Python code?」** 是驗收標準。

---

## Explicit Assumptions

1. Skills 為可攜式，適用於任何 Python 專案（非本 repo 專用）
2. `python-plan-authoring` 輸出格式與 `plan-creator`（本 repo 格式）無關；兩者不重疊
3. Skills 本身遵循 `.github/copilot-instructions.md` 的 skill folder 規範
4. Skills 將透過 `agent-skill-creator` 草稿 → `agent-skill-reviewer` 審查
5. Executor agent 被假定為「不會主動詢問未明確決策」，因此 plan 必須覆蓋所有關鍵決策

---

## Non-goals

- 不更新 `python-descriptors-attribute-access`（獨立 topic）
- 不建立 CI/CD 整合管線
- 不替換本 repo 的 `plan-creator`（格式不同，用途不同）
- 不建立新的 Python runtime 執行環境
- 不提供 `*.plan.md` 格式的自動驗證腳本（只定義 skill，不提供 CLI 工具）

---

## Contradictions Log

無衝突。以下潛在矛盾已於討論中解決：

| 潛在矛盾 | 解決方式 |
|---------|---------|
| `implementation-review` 與 `code-review` 的責任邊界 | 明確分離：前者驗對齊性，後者驗品質；順序不可顛倒 |
| `python-plan-authoring` vs `plan-creator` 的用途 | 前者為任何 Python 專案通用；後者為本 repo 工作流程專用 |
| Validation Commands 是否綁定特定工具 | 決策：依專案配置自動偵測，不強制指定工具 |

---

## Extreme Boundary Checks

| 邊界條件 | 需求仍然成立？ | 說明 |
|---------|-------------|------|
| Plan 缺少 Decisions 節 | ✅ | plan-review 必須捕捉，輸出 `needs-rework` |
| Plan 的 Validation Commands 為空 | ✅ | plan-review 必須要求至少提供 fallback 指引 |
| Implementation 新增了 plan 未列的功能 | ✅ | implementation-review 必須標記 scope creep |
| 專案沒有任何 tooling 配置（無 pyproject.toml / Makefile） | ✅ | code-review 必須以通用 best practice fallback 運作，不得崩潰 |
| Plan 有 Open Questions 未解 | ✅ | 若 Open Questions 影響實作，plan-review 必須阻擋（非警告） |
| 極小型 Python 腳本（無 package 結構） | ✅ | Affected Files 節可簡化，但仍必須存在 |
| Executor 在實作時發現 plan 的決策有誤 | ✅ | Executor 應回報並觸發 plan 修訂，不得自行修改決策 |

---

## Blockers

無阻礙項目。需求已足夠進入技術翻譯。
