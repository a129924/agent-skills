# python-workflow-enhancement

## Analysis-Layer Routing

**模式：Strict Mode**（兩份 analysis 文件均存在）

| 文件 | 路徑 | 狀態 |
|------|------|------|
| 需求基準 | `analysis/python-workflow-enhancement/requirements.md` | ✅ FROZEN |
| 技術規格 | `analysis/python-workflow-enhancement/technical-spec.md` | ✅ COMPLETE |

**Authority rule**：technical-spec.md 為 execution-facing source of truth；requirements.md 為業務意圖護欄。

**B6 / R-NEW override**：technical-spec.md 的 B6（D1 standalone skill）和 R-NEW 條目被人類顯式覆蓋（「Option C：D1 保留在 tdd-test-authoring 內部，對外輸出結構化 verdict」）。本計畫以 Option C 決策為準。所有其他 technical-spec.md 內容以 strict mode 100% 對應。

---

## Goal / Outcome

在現有 Python 實作 workflow（v0.50.1）基礎上，增加三項可觀察的增強：

1. **spec.md artifact**：在 `python-plan-authoring` 建立 spec-template.md，並聲明 D1 non-trivial 時 spec.md 為強制產出（輕量 SDD）
2. **tdd-test-authoring 介面升級**：D1 分類邏輯保留在 skill 內部，但對外輸出結構化 verdict（trivial / non-trivial + reason）；spec.md 存在時優先於 plan.md Requirements
3. **workflow orchestrator agent**：新增 `python-implementation-workflow.agent.md`，以 active gate 模式串連 plan-review → TDD assessment → implementation gate → impl-review → code-review

完成後，`.github/agents/` 新增 1 個 agent 檔案，`.github/skills/` 下 2 個現有 skill 更新，`README.md` 新增 1 行，`VERSION` 從 `0.50.1` bump 至 `0.51.0`。

---

## Scope

**In scope**：
- `.github/skills/python-plan-authoring/templates/spec-template.md` — 新增
- `.github/skills/python-plan-authoring/SKILL.md` — 更新（spec.md 強制產出聲明）
- `.github/skills/python-tdd-test-authoring/SKILL.md` — 更新（structured verdict 輸出；spec.md 優先序；non-trivial + spec.md 缺失 → BLOCKED 路由）
- `.github/agents/python-implementation-workflow.agent.md` — 新增
- `README.md` — Current skills 表格新增 1 行（python-implementation-workflow agent）
- `VERSION` — `0.50.1` → `0.51.0`（MINOR bump）

**Out of scope**：
- 建立 `python-d1-classifier` standalone skill（已由 Option C 決策排除）
- 修改 `python-implementation-review` SKILL.md（step gate Step 1.5 已存在，無需更動）
- 修改 `python-plan-review`、`python-code-review`（無需更動）
- git 操作（commit、push、PR）——不在 agent scope 內
- 多 topic 並行支援
- spec.md 的獨立 review 流程

---

## Locked Decisions

（technical-spec.md 嚴格模式；以下為 downstream roles 不得重新發現的決策）

| 決策 | 結論 | 來源 |
|------|------|------|
| spec.md 強制條件 | D1 non-trivial 時強制；D1 trivial 時跳過 | requirements.md C2；technical-spec.md A3 |
| spec.md 格式 | Acceptance Criteria + Behavioral Scenarios（Given/When/Then）+ Error/Edge Cases | technical-spec.md A1 |
| spec.md 與 plan.md 衝突優先序 | spec.md 優先（SDD = 更完整的行為合約） | requirements.md R1-3 |
| D1 classifier 歸屬 | **Option C**：保留在 tdd-test-authoring 內部；對外輸出 structured verdict | 人類顯式 override（B6 / R-NEW） |
| tdd-skill D1 verdict 格式 | trivial / non-trivial + reason（structured output） | technical-spec.md A2 |
| workflow agent 模式 | Active Gate（主動阻擋）；Phase gate 使用 plan-step-tracker | technical-spec.md B4 |
| needs-rework 處理 | 內部迴路；agent 自行重新叫用對應 skill；不設上限 | requirements.md R2-3；technical-spec.md B5 |
| agent scope 邊界 | plan-review → code-review；git 操作在外 | requirements.md Non-goals |
| session 恢復 | 從 step.md Workflow Stages 推斷 current phase | technical-spec.md B7 |
| VERSION bump 時機 | agent-skill-reviewer approved 後才 bump | requirements.md C3 |
| 本 topic 影響 stable-library surfaces | ✅ 是（README.md + VERSION 均受影響） | — |

---

## Boundaries / Exclusions

- **角色邊界**：creator 建立 / 修改檔案；reviewer 提供 needs-rework 或 approved；main agent 不自行 approve
- **spec.md 不取代** plan.md Requirements 段落（兩份文件並存，互補）
- **spec.md 不需要**獨立 review 流程（直接作為 tdd-test-authoring 輸入）
- **D1 邏輯不外移**：D1 classification 保留在 tdd-test-authoring 內部邏輯中，不建立新 skill
- **agent 不執行** git 操作（commit / push / PR）
- 如有任何實作工作超出 Artifact Paths 所列路徑，視為計畫偏離，需先更新本計畫

---

## Accepted Deviations

- **deviation 項目**：`templates/step-template.md` 納入本 topic 的已接受計畫偏離。
- **理由**：workflow 落地時需要一致的 step 文件模板來承接 phase gate 與 resume 行為，屬於既有 scope 的實作支撐，不改變既定決策。
- **影響面**：僅影響 step 文件產生與執行一致性；不改變 6-phase 流程、D1 歸屬、verdict gate、或 git out-of-scope 邊界。
- **接受條件/邊界（不擴散 scope）**：僅允許新增/調整 `templates/step-template.md` 以支援本計畫既有 artifact；不得擴張至新 skill、新流程 phase、或額外治理機制。

---

## Status / Allowed Transitions

- **Current**: `planned`
- **Execution model**：creator → reviewer → publish → merge；本 topic 有 stable-library surfaces（README.md + VERSION），publishing 時一併更新
- **Allowed transitions**:
  - `planned` → `creator-in-progress`
  - `creator-in-progress` → `review-ready`
  - `review-ready` → `reviewer-in-progress`
  - `reviewer-in-progress` → `approved`
  - `reviewer-in-progress` → `needs-rework`
  - `needs-rework` → `creator-in-progress`
  - `approved` → `publish-in-progress`
  - `publish-in-progress` → `pr-open`
  - `pr-open` → `needs-rework`
  - `pr-open` → `merged`
  - `merged` → terminal

**Routing notes**：
- VERSION bump 和 README.md 更新在 `publish-in-progress` 階段執行（timing = publish-in-progress）
- agent-skill-reviewer 對 `.github/agents/python-implementation-workflow.agent.md` 的審查必須在 `publish-in-progress` 前完成
- Phase 4.5 標準規則適用：STOP POINT 1 在 commit/push/PR 前需人類明確授權

---

## Artifact Paths

| Artifact | Path | Owner | Role |
|----------|------|-------|------|
| Topic plan | `plan/python-workflow-enhancement/python-workflow-enhancement.plan.md` | Planning actor | 本 topic 的 repo-visible execution contract |
| spec 模板 | `.github/skills/python-plan-authoring/templates/spec-template.md` | Creator | 供 plan-authoring skill 使用的 spec.md 格式模板 |
| plan-authoring SKILL.md | `.github/skills/python-plan-authoring/SKILL.md` | Creator | 更新 Outputs 節：D1 non-trivial 時 spec.md 為強制產出 |
| tdd-test-authoring SKILL.md | `.github/skills/python-tdd-test-authoring/SKILL.md` | Creator | 更新 Inputs / Process / Outputs：structured verdict；spec.md 優先序；BLOCKED 路由 |
| Workflow agent | `.github/agents/python-implementation-workflow.agent.md` | Creator | 新 orchestrator agent（Phase 0–5，active gate）|
| README.md | `README.md` | Creator（publish-in-progress） | Current skills 表格新增 workflow agent 行 |
| VERSION | `VERSION` | Creator（publish-in-progress） | `0.50.1` → `0.51.0`（MINOR bump）|

**Artifact path notes**：
- `README.md` 和 `VERSION` 修改在 `publish-in-progress` 執行，不在 creator draft 階段
- 若工作超出上列路徑，必須先 amend 本計畫的 Artifact Paths 節

---

## Stable library metadata

- **README row**：`README.md` Current skills 表格新增 1 行：`python-implementation-workflow` 的 agent 說明
- **VERSION bump**：`0.50.1` → `0.51.0`（MINOR；新增 stable agent）
- **timing**：`publish-in-progress`（README 和 VERSION 在 PR 建立前一併提交）
- **rationale**：新增 stable workflow agent 符合 MINOR bump 政策；VERSION bump 在 agent-skill-reviewer approved 後執行

---

## Implementation Steps

**Step 1 — spec-template.md（Workstream A1）**
- 建立 `.github/skills/python-plan-authoring/templates/spec-template.md`
- 格式：3 段（Acceptance Criteria、Behavioral Scenarios（Given/When/Then）、Error/Edge Cases）
- 包含填寫說明（prompt text）讓 plan-authoring skill 知道如何填充

**Step 2 — python-plan-authoring SKILL.md 更新（Workstream A3）**
- 在 `Outputs` 節新增條件：「When D1 non-trivial: `plan/<topic>/<topic>.spec.md` is a required co-artifact」
- 格式說明：Acceptance Criteria + Behavioral Scenarios + Error/Edge Cases
- 命名規則：與 plan.md、step.md 同層，`<topic>.spec.md`

**Step 3 — python-tdd-test-authoring SKILL.md 更新（Workstream A2 + B2）**
- 更新 `Inputs` 節：
  - `plan/<topic>/<topic>.spec.md`（優先輸入，存在時優先於 plan.md Requirements；D1 non-trivial + spec.md 缺失 → BLOCKED）
  - D1 classification 保留內部，但 `Outputs` 節新增 structured verdict 欄位
- 更新 `Process` 節：Step 1 = D1 判斷（trivial → 輸出 verdict: trivial，早期返回；non-trivial → 繼續）
- 更新 `Outputs` 節：`verdict: trivial | non-trivial` + `reason: <string>`
- spec.md 優先序：明確聲明衝突時以 spec.md 為準，並在 issues 記錄衝突

**Step 4 — python-implementation-workflow.agent.md（Workstream B1–B5 + B7）**
- 建立 `.github/agents/python-implementation-workflow.agent.md`
- 遵循現有 `.github/agents/python-project-init.agent.md` 的檔案格式
- 包含以下 Phase 設計：
  - Phase 0：Pre-flight（確認 plan.md / spec.md / step.md 存在性；從 step.md Workflow Stages 重建 current phase）
  - Phase 1：Plan Review（/fleet @python-plan-review/；needs-rework → 內部迴路 /fleet @python-plan-authoring/）
  - Phase 2：TDD Assessment（/fleet @python-tdd-test-authoring/；讀 verdict；trivial → skip Phase 2 remainder；non-trivial + spec.md 缺失 → BLOCKED）
  - Phase 3：Implementation Gate（引導 executor；plan-step-tracker check_all_succeeded；exit 1 → BLOCKED）
  - Phase 4：Implementation Review（/fleet @python-implementation-review/；needs-rework → 通知 executor 回到 Phase 3）
  - Phase 5：Code Review（/fleet @python-code-review/；needs-rework → 通知 executor 回到 Phase 3；approved → DONE）
- 聲明 tools：`agent`（/fleet 呼叫）、`shell`（plan-step-tracker）

---

## Validation / Acceptance Checks

**Workstream A（spec.md artifact）**
- [ ] `spec-template.md` 存在於 `.github/skills/python-plan-authoring/templates/`
- [ ] spec-template.md 包含 Acceptance Criteria、Behavioral Scenarios、Error/Edge Cases 三節
- [ ] python-plan-authoring SKILL.md Outputs 節明確列出 D1 non-trivial 時 spec.md 為必要產出

**Workstream B（tdd-test-authoring 更新）**
- [ ] tdd-test-authoring SKILL.md Inputs 節包含 spec.md（優先輸入，可選）
- [ ] tdd-test-authoring SKILL.md Process 節 Step 1 為 D1 判斷，含 trivial 早期返回路徑
- [ ] tdd-test-authoring SKILL.md Outputs 節包含 `verdict` 欄位（trivial / non-trivial + reason）
- [ ] spec.md 優先序規則明確（衝突時以 spec.md 為準）
- [ ] non-trivial + spec.md 缺失 → BLOCKED 路由明確

**Workstream C（workflow agent）**
- [ ] `.github/agents/python-implementation-workflow.agent.md` 存在
- [ ] Phase 0–5 流程完整（含 pre-flight 與 session 恢復邏輯）
- [ ] Phase 3 gate 使用 plan-step-tracker（active gate，exit 1 → BLOCKED）
- [ ] needs-rework 路由全部為內部迴路（無需人類介入）
- [ ] 格式與現有 agent 檔案一致（python-project-init.agent.md）

**Stable-library**
- [ ] README.md Current skills 表格新增 python-implementation-workflow agent 行
- [ ] VERSION 從 0.50.1 → 0.51.0
- [ ] 上述兩項在 `publish-in-progress` 階段執行（非 creator draft）

---

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

---

## Post-merge / release actions

本 topic 有 stable-library 變更（README.md + VERSION）。

- **timing**：`publish-in-progress`（PR 建立前提交）
- **Release action**：無獨立 release；stable-library 更新在 merge 時生效
- **Merge 後**：無進一步動作；topic 進入 terminal 狀態

---

## Open Questions / Unresolved Items

無。所有決策已凍結（requirements.md FROZEN；technical-spec.md COMPLETE；B6 override 已記錄）。
