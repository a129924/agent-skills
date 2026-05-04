# Technical Specification: Python Implementation Workflow

**Status**: frozen — ready for plan authoring
**Topic**: `python-implementation-workflow`
**Source baseline**: `analysis/python-implementation-workflow/requirements.md`

---

## Baseline Summary

4 個可攜式 Agent Skills，建立 Python 代碼實作的完整工作流程：

```
python-plan-authoring → python-plan-review → [executor] →
python-implementation-review → python-code-review
```

技術核心：每個 skill 是靜態的 repo 內文件資產（`.github/skills/<name>/`），
不是執行程式。驗收標準由 SKILL.md 的 Process 節定義。

---

## Requirement-to-Technical Mapping

| Requirement | Technical Realization | Dependencies | Cost / Burden | Status |
|-------------|----------------------|--------------|---------------|--------|
| R1 Plan Authoring（13 節契約） | `python-plan-authoring/SKILL.md` 定義 13 節模板、stop-and-ask 條件、各節必要內容規範 | agent-skill-creator（草稿）、agent-skill-reviewer（審查） | SKILL.md（高複雜度）+ examples.md（必要）+ templates/ | feasible |
| R2 Plan Review（可執行性） | `python-plan-review/SKILL.md` 定義 13 節完整性檢查清單 + 逐節驗收標準 | python-plan-authoring（定義被驗的格式） | SKILL.md（中複雜度）+ checklist.md（必要）+ examples.md | feasible |
| R3 Implementation Review（對齊性） | `python-implementation-review/SKILL.md` 定義 plan traceability 矩陣、scope creep 偵測、API contract 驗證 | plan 格式由 R1 定義 | SKILL.md（中-高複雜度）+ examples.md（必要，分支多） | feasible |
| R4 Code Review（品質，自動偵測工具） | `python-code-review/SKILL.md` 定義工具偵測優先順序 + 各品質維度評判標準 | 專案配置（pyproject.toml / Makefile / README） | SKILL.md（高複雜度）+ examples.md（必要，工具分支多）+ reference.md | feasible |

---

## Technical Tasks and Artifacts

### Skill 1：`python-plan-authoring`

**複雜度**：高（多分支、stop-and-ask 條件多、輸出格式需精確）
**必要文件**：
- `SKILL.md` — Trigger、Process（含 13 節模板）、stop-and-ask 條件清單、Inputs/Outputs/Boundaries
- `examples.md` — 必要（分支多：完整 plan 範例 vs 缺節觸發 needs-rework 範例）
- `templates/python-plan-template.md` — 可選，但高度建議（executor 直接複用）

**Key design decisions**：
- 13 節模板定義在 SKILL.md Process 節，或 templates/ 下的 `python-plan-template.md`
- stop-and-ask 條件：當 Decisions、Non-goals、Validation Commands 缺失時必須停止詢問
- 不預設 plan 儲存路徑（可攜式，由 caller 決定）

### Skill 2：`python-plan-review`

**複雜度**：中（線性驗收，但需精確映射 13 節標準）
**必要文件**：
- `SKILL.md` — Process（逐節驗收邏輯）、Inputs（plan 文件路徑）、Outputs（JSON verdict）
- `checklist.md` — 必要（可複用的 13 節驗收清單 + 各節合格標準）
- `examples.md` — 必要（至少一個 approved 範例、一個 needs-rework + blocking issues 範例）

**Key design decisions**：
- 輸出格式：JSON `{ "verdict": "approved|needs-rework", "blocking_issues": [] }`
- 驗收粒度：逐節（非整體判斷），缺任一節 → 直接 needs-rework
- 不驗證實作細節，只驗計劃文件本身

### Skill 3：`python-implementation-review`

**複雜度**：中-高（需 traceability 矩陣、scope creep 偵測邏輯）
**必要文件**：
- `SKILL.md` — Process（逐 Step traceability、Non-goals 邊界檢查、API contract 比對）
- `examples.md` — 必要（happy path + scope creep 案例 + API 破壞案例 + 漏實作案例）

**Key design decisions**：
- 語意邊界：只驗「是否忠實達成 plan」，不驗 code quality
- 責任範圍：Implementation Steps（完成否）、Non-goals（有無越界）、Public Contract（有無未授權改動）、Test Plan（對應否）
- 不負責：code style、architecture quality、Python idiomatic correctness

### Skill 4：`python-code-review`

**複雜度**：高（多工具分支、多品質維度、輸出結構化）
**必要文件**：
- `SKILL.md` — Process（工具偵測流程、各品質維度定義）、Inputs/Outputs/Boundaries
- `examples.md` — 必要（工具偵測分支、各維度問題範例）
- `reference.md` — 必要（工具偵測規則、anti-pattern 清單、各維度評判標準）

**Key design decisions**：
- 工具偵測優先順序：`pyproject.toml` → `Makefile` → `README` → generic best-practice fallback
- 不執行工具（靜態 skill），而是提供判斷框架讓 agent 依工具輸出做出判斷
- 語意邊界：不驗計劃對齊（已由 implementation-review 保證）
- Anti-pattern 清單：`__getattr__`/`__setattr__` 濫用、bare except、mutable default arg 等

---

## Architecture Compliance Self-Check

| Dimension | Result | Notes |
|-----------|--------|-------|
| Skill folder shape | **fits existing architecture** | 遵循 `.github/copilot-instructions.md` 的 skill 資料夾規範 |
| Naming convention | **fits existing architecture** | lowercase kebab-case |
| SKILL.md required sections | **fits existing architecture** | frontmatter + Purpose + Trigger + Inputs + Process + Examples + Outputs + Boundaries + Local references |
| companion file rule | **fits with prerequisites** | python-plan-authoring、python-code-review 需 examples.md（高複雜度必要）|
| examples.md necessity | **fits with prerequisites** | 3/4 skills 因分支多而需要 examples.md（見規範）|
| portable / self-contained | **fits existing architecture** | Skills 不依賴本 repo workflow（與 plan-creator 無重疊）|
| stable-library surface | **fits with prerequisites** | 4 new skills → README 新增 4 行 + MINOR VERSION bump（0.37.0 → 0.38.0）|

---

## Cost-of-Realization Assessment

| Workstream | Complexity | Sequencing | Notes |
|-----------|-----------|-----------|-------|
| python-plan-authoring | 高 | 第 1 個（定義下游驗收格式） | SKILL.md 較長；需 examples.md；需 template |
| python-plan-review | 中 | 第 2 個（依賴 authoring 定義的格式） | checklist.md 是核心產出 |
| python-implementation-review | 中-高 | 第 3 個（獨立於 authoring/review） | 新概念，無直接參考 skill；需設計 traceability 框架 |
| python-code-review | 高 | 第 4 個（獨立於前三個） | reference.md 工作量大；anti-pattern 清單需詳細 |
| agent-skill-reviewer 驗證 | 中 | 所有 skills 完成後 | 4 個 skill 各跑一次 reviewer 流程 |
| README + VERSION bump | 低 | 最後 | 4 行新增 + 版本 0.37.0 → 0.38.0 |

**預估總文件量**：
- 4 × SKILL.md（各約 80-150 行）
- 3 × examples.md（各約 60-100 行）
- 1 × checklist.md（約 30-50 行）
- 1 × reference.md（約 80-120 行）
- 1 × templates/python-plan-template.md（約 60 行）

---

## Conflicts and Blockers

無實質衝突。以下注意事項：

| Issue | Type | Handling |
|-------|------|---------|
| python-plan-authoring 的 template 路徑 | 設計決策 | 建議放 `templates/python-plan-template.md`（與 plan-creator 的 templates/ 模式一致） |
| python-code-review 的 anti-pattern 清單範圍 | 設計邊界 | 應引用現有 python-* skills 的規則而非重複定義（e.g., 引用 python-descriptors-attribute-access 的 escape-hatch 規則） |
| python-implementation-review 無直接參考 | 新概念風險 | 需在 examples.md 中提供足夠的 traceability 矩陣範例 |

---

## Rollback Triggers

以下條件應回滾至業務對齊：
- 若 `*.plan.md` 格式與本 repo `plan-creator` 格式產生混淆 → 在 SKILL.md Boundaries 節明確區隔
- 若 `python-code-review` 的 anti-pattern 清單與現有 `python-descriptors-attribute-access` 產生重複定義 → 改為引用而非重複
