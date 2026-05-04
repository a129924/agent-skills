# python-implementation-workflow

## Goal / Outcome

新增 4 個可攜式 Agent Skills，為任何 Python 專案建立可預測、可審查的代碼實作工作流程：

```
python-plan-authoring → python-plan-review → [executor] →
python-implementation-review → python-code-review
```

完成時，`.github/skills/` 下新增 4 個符合 repo 規範的 stable skill 資料夾，
`README.md` 新增 4 行，`VERSION` 從 `0.37.0` bump 至 `0.38.0`。

## Scope

- **In scope**:
  - `.github/skills/python-plan-authoring/` — 新增
  - `.github/skills/python-plan-review/` — 新增
  - `.github/skills/python-implementation-review/` — 新增
  - `.github/skills/python-code-review/` — 新增
  - `README.md` — Current skills 表格新增 4 行
  - `VERSION` — `0.37.0` → `0.38.0`（MINOR bump，新增 4 個 stable skills）

- **Out of scope**:
  - `python-descriptors-attribute-access` 的更新（獨立 topic）
  - 本 repo 的 `plan-creator` 格式（不修改）
  - CLI 工具或自動化腳本（只定義 skill 文件）
  - 任何現有 skill 的修改

## Locked Decisions

- **Skills 適用範圍**：可攜式，用於任何 Python 專案；與本 repo 的 `plan-creator` 不重疊
- **`*.plan.md` 標準模板**：13 節（Goal / Non-goals / Current Context / Requirements / Decisions / Public Contract & API Changes / Affected Files & Modules / Implementation Steps / Test Plan / Validation Commands / Risks / Rollback Plan / Open Questions）
- **三種 review 語意邊界**（不得混淆）：
  - `python-plan-review`：Can this be executed without guessing?
  - `python-implementation-review`：Does the implementation satisfy the approved plan?
  - `python-code-review`：Is this good Python code?
- **工具偵測策略**：`python-code-review` 依專案配置自動偵測（`pyproject.toml` → `Makefile` → `README` → fallback）
- **Reviewer handoff 格式**：YAML（格式見各 review skill 的 Outputs 節）
- **examples.md 必要性**：python-plan-authoring、python-implementation-review、python-code-review 因分支多而必須有 `examples.md`；python-plan-review 因 gatekeeping 性質需 `checklist.md` + `examples.md`
- **此 topic 影響 stable-library surfaces**：README + VERSION，timing = `publish-in-progress`

## Boundaries / Exclusions

- `python-plan-authoring` 的 `*.plan.md` 輸出格式與 `plan-creator` 的 `plan/<topic>/<topic>.plan.md` 格式不同，不得混用
- `python-code-review` 的 anti-pattern 規則應引用現有 `python-descriptors-attribute-access`，不得重複定義
- `python-implementation-review` 只驗對齊性，不得對 code quality 發表意見（交由 `python-code-review`）
- 此 topic 的 4 個 skills 各自獨立，creator 和 reviewer 角色分離（遵循 repo workflow）

## Status / Allowed Transitions

- **Current**: `publish-in-progress`
- **Execution model**：canonical creator → reviewer → publish → merge path；此 topic 包含 stable-library 更新，因此執行至 `merged`（VERSION bump 在 `publish-in-progress` 完成）
- **Allowed transitions**:
  - `planned` → `creator-in-progress`
  - `creator-in-progress` → `review-ready`
  - `review-ready` → `reviewer-in-progress`
  - `reviewer-in-progress` → `approved`
  - `reviewer-in-progress` → `needs-rework`
  - `needs-rework` → `creator-in-progress`
  - `approved` → `creator-in-progress` (Phase 4.5 rework routing only)
  - `approved` → `publish-in-progress`
  - `publish-in-progress` → `pr-open`
  - `pr-open` → `needs-rework`
  - `pr-open` → `merged`
  - `merged` → terminal

**Routing notes**：
- 每個 skill 應分別通過 `agent-skill-reviewer` 的 `approved`，再一次性進入 `publish-in-progress`
- Phase 4.5 standard rule 適用：`approved` 後直接進入 `publish-in-progress`（不需額外路由）

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/python-implementation-workflow/python-implementation-workflow.plan.md` | Planning actor | Repo-visible execution contract |
| Business requirements | `analysis/python-implementation-workflow/requirements.md` | Planning actor | 凍結的業務需求基準 |
| Technical spec | `analysis/python-implementation-workflow/technical-spec.md` | Planning actor | 技術實現規格 |
| `python-plan-authoring` SKILL.md | `.github/skills/python-plan-authoring/SKILL.md` | Creator | 主合約，含 13 節模板定義與 stop-and-ask 條件 |
| `python-plan-authoring` examples.md | `.github/skills/python-plan-authoring/examples.md` | Creator | 完整 plan 範例 + 缺節觸發 needs-rework 範例 |
| `python-plan-authoring` template | `.github/skills/python-plan-authoring/templates/python-plan-template.md` | Creator | 13 節空白模板供 executor 複用 |
| `python-plan-review` SKILL.md | `.github/skills/python-plan-review/SKILL.md` | Creator | 逐節驗收邏輯、YAML verdict 格式 |
| `python-plan-review` checklist.md | `.github/skills/python-plan-review/checklist.md` | Creator | 13 節驗收清單 + 各節合格標準 |
| `python-plan-review` examples.md | `.github/skills/python-plan-review/examples.md` | Creator | approved 範例 + needs-rework 範例 |
| `python-implementation-review` SKILL.md | `.github/skills/python-implementation-review/SKILL.md` | Creator | traceability 矩陣、scope creep 偵測、API contract 驗證 |
| `python-implementation-review` examples.md | `.github/skills/python-implementation-review/examples.md` | Creator | happy path + scope creep + API 破壞 + 漏實作案例 |
| `python-code-review` SKILL.md | `.github/skills/python-code-review/SKILL.md` | Creator | 工具偵測流程、各品質維度定義 |
| `python-code-review` examples.md | `.github/skills/python-code-review/examples.md` | Creator | 工具偵測分支 + 各維度問題範例 |
| `python-code-review` reference.md | `.github/skills/python-code-review/reference.md` | Creator | 工具偵測規則、anti-pattern 清單、評判標準 |
| Stable library summary | `README.md` | Main Agent | Current skills 表格新增 4 行 |
| Version baseline | `VERSION` | Main Agent | `0.37.0` → `0.38.0` |

Artifact path notes:
- 此 topic 修改 `README.md` 和 `VERSION`，timing = `publish-in-progress`
- 若實作過程中路徑偏離此表，停止並修正路徑後再繼續
- Analysis 層檔案（`analysis/`）已存在，不需再建立

## Stable Library Metadata

- **README row**：在 Current skills 表格新增 4 行（python-plan-authoring / python-plan-review / python-implementation-review / python-code-review），各附一行描述
- **VERSION bump**：`0.37.0` → `0.38.0`（MINOR，新增 4 個 stable skills）
- **timing**：`publish-in-progress`（與 PR 一起提交）
- **rationale**：4 個新 stable skills 都影響 README 的 Current skills 表格；VERSION 按 SemVer MINOR 規則 bump

## Implementation Steps

依照 `analysis/python-implementation-workflow/technical-spec.md` 的順序建立 4 個 skills：

1. **使用 `agent-skill-creator` 建立 `python-plan-authoring`**
   - 建立 `.github/skills/python-plan-authoring/SKILL.md`（含 13 節模板定義、stop-and-ask 條件）
   - 建立 `.github/skills/python-plan-authoring/examples.md`（完整 plan 範例 + 缺節觸發 needs-rework 範例）
   - 建立 `.github/skills/python-plan-authoring/templates/python-plan-template.md`（13 節空白模板）
   - 移交 `agent-skill-reviewer` 審查，取得 `approved`

2. **使用 `agent-skill-creator` 建立 `python-plan-review`**
   - 建立 `.github/skills/python-plan-review/SKILL.md`（逐節驗收邏輯、YAML verdict 格式）
   - 建立 `.github/skills/python-plan-review/checklist.md`（13 節驗收清單 + 各節合格標準）
   - 建立 `.github/skills/python-plan-review/examples.md`（approved 範例 + needs-rework 範例）
   - 移交 `agent-skill-reviewer` 審查，取得 `approved`

3. **使用 `agent-skill-creator` 建立 `python-implementation-review`**
   - 建立 `.github/skills/python-implementation-review/SKILL.md`（traceability 矩陣、scope creep 偵測、API contract 驗證）
   - 建立 `.github/skills/python-implementation-review/examples.md`（happy path + scope creep + API 破壞 + 漏實作案例）
   - 移交 `agent-skill-reviewer` 審查，取得 `approved`

4. **使用 `agent-skill-creator` 建立 `python-code-review`**
   - 建立 `.github/skills/python-code-review/SKILL.md`（工具偵測流程、各品質維度定義）
   - 建立 `.github/skills/python-code-review/examples.md`（工具偵測分支 + 各維度問題範例）
   - 建立 `.github/skills/python-code-review/reference.md`（工具偵測規則、anti-pattern 清單、評判標準）
   - 移交 `agent-skill-reviewer` 審查，取得 `approved`

5. **更新 stable library（publish-in-progress）**
   - 更新 `README.md`：Current skills 表格新增 4 行
   - 更新 `VERSION`：`0.37.0` → `0.38.0`

## Validation / Acceptance Checks

- [ ] 4 個 skill 資料夾均存在於 `.github/skills/`
- [ ] 每個 SKILL.md 包含完整 frontmatter（name + description）及所有必要節
- [ ] 每個 skill 的 `examples.md` 或 `checklist.md` 存在（依各 skill 需求）
- [ ] 每個 SKILL.md 的 `Trigger / When to use` 明確，包含至少一個正例和一個反例
- [ ] 每個 skill 通過 `agent-skill-reviewer` 的 `approved` verdict
- [ ] `README.md` Current skills 表格新增 4 行（路徑正確、描述清晰）
- [ ] `VERSION` 為 `0.38.0`
- [ ] 4 個 skill 的語意邊界不重疊（plan-review / implementation-review / code-review 各自獨立）

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

## Post-merge / Release Actions

- 無額外 release action（VERSION bump 已在 `publish-in-progress` 完成）
- 合併後無需建立 git tag（MINOR bump 不強制 tag）
- `merged` 為此 topic 的 terminal state

## Open Questions / Unresolved Items

- `python-plan-authoring` 的 `templates/python-plan-template.md` 是否應與 `plan-creator` 的 templates 路徑保持一致？（建議：各自獨立，因用途不同）
- `python-code-review` 引用 `python-descriptors-attribute-access` 的方式：直接連結還是複製規則？（建議：在 Boundaries 節說明「anti-pattern 完整規則見 python-descriptors-attribute-access」，不複製）
