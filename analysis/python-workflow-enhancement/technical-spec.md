---
topic: python-workflow-enhancement
status: COMPLETE — C1/C2/C3 已解決；D1 classifier 已決策為 standalone skill
baseline: analysis/python-workflow-enhancement/requirements.md
created: 2026-05-09
updated: 2026-05-09
---

# Python Workflow Enhancement — Technical Spec

> **Baseline gate 結果**：`requirements.md` 狀態已更新為 READY FOR TECHNICAL TRANSLATION。
> C1/C2/C3 全部已解決；B6（D1 classifier）已決策為 standalone skill。
> 本文件為完整技術規格。

---

## 需求→技術翻譯矩陣

| 需求 ID | 業務需求 | 技術實現 | 依賴 | 成本/負擔 | 狀態 |
|--------|----------|----------|------|-----------|------|
| R1-2 | spec.md 不存在時現有 workflow 不受影響 | `python-tdd-test-authoring` 加入 `spec.md` 存在性檢查；不存在時 fallback 至 `plan.md` Requirements | 現有 `python-tdd-test-authoring` SKILL.md 修改 | 低：條件邏輯 + 文件更新 | **feasible** |
| R2-1 | plan.md 存在時 agent 能定位並進入 Phase 1 | Agent pre-flight：讀取 `plan/<topic>/<topic>.plan.md`；缺失時拒絕並回報 topic 名稱 | `plan-step-tracker` 腳本（讀 step.md 驗證） | 低：file-existence check + 錯誤輸出 | **feasible** |
| R2-2 | STOP POINT 不可繞過 | STOP POINT 定義對齊 `plan/agent-handoff-workflow.md`；無明確 resume 訊息前 agent 靜止 | 現有 repo STOP POINT 合約 | 低：策略宣告 + 路由規則 | **feasible** |
| R1-1 | D1 non-trivial 時 spec.md 強制存在 | plan-authoring 需將 spec.md 列為必要產出（D1 non-trivial path）；workflow agent Phase 2 驗證存在性；缺失 → BLOCKED | python-plan-authoring SKILL.md 更新；python-d1-classifier skill（B6） | 低-中：plan-authoring 輸出合約更新 + agent 路由邏輯 | **feasible（C2 已解決）** |
| R1-3 | spec.md vs. plan.md 衝突優先序 | spec.md 優先（SDD = 更完整的行為合約）；tdd-test-authoring 以 spec.md 為準；衝突記錄至輸出 issues | python-tdd-test-authoring SKILL.md 更新（明確優先序） | 低：文件宣告 + 條件邏輯 | **feasible（C2 已解決）** |
| R2-3 | needs-rework 迴路行為 | 內部迴路：agent 重新叫用對應 skill；不設上限；每次記錄原因 | /fleet 呼叫能力 | 低：路由邏輯；無 phase state machine 需求 | **feasible（C1 已解決）** |
| R-NEW | D1 Classifier standalone skill | `.github/skills/python-d1-classifier/` 新增 skill；輸入：plan.md；輸出：trivial/non-trivial + reason | python-tdd-test-authoring 移除內嵌 D1；workflow agent Phase 2 叫用 D1 | 中：新 skill 需完整 creator/reviewer 流程 | **feasible（B6 已決策）** |

---

## Workstream A：spec.md artifact（部分可行）

### 可立即規劃的部分

**A1 — spec-template.md（無爭議）**
- 任務：在 `python-plan-authoring/templates/` 新增 `spec-template.md`
- 格式：3 段結構（Acceptance Criteria、Behavioral Scenarios、Error/Edge Cases）
- 依賴：無
- 成本：低（純文件，無邏輯）
- 架構合規：`fits existing architecture`（template 已有 precedent：`python-plan-template.md`）

**A2 — python-tdd-test-authoring SKILL.md（向下相容 fallback）**
- 任務：加入 `inputs` 段落：「`plan/<topic>/<topic>.spec.md`（優先輸入，可選）；不存在時使用 `plan.md` Requirements 段落」
- 成本：低（文件更新，不改 skill 邏輯）
- 架構合規：`fits existing architecture`

**A3 — python-plan-authoring SKILL.md（必要性聲明）← C2 已解決**
- 任務：將 `spec.md` 列為條件強制輸出：「When D1 non-trivial: `plan/<topic>/<topic>.spec.md` is a required co-artifact」
- 格式聲明：Acceptance Criteria + Behavioral Scenarios（Given/When/Then） + Error/Edge Cases
- 成本：低（文件更新，輸出合約變更）
- 架構合規：`fits existing architecture`（spec.md 與 plan.md 同層，命名模式一致）

---

## Workstream B：python-implementation-workflow Agent（全部可行）

### 可立即規劃的部分

**B1 — Pre-flight 邏輯（Phase 0）**
- 任務：agent 確認 `plan/<topic>/<topic>.plan.md` 存在；偵測 spec.md 和 step.md 是否存在
- 技術實現：讀取檔案路徑；缺失時輸出明確錯誤，停止並等待人類提供路徑
- 成本：低
- 架構合規：`fits existing architecture`

**B2 — /fleet 路由（Phase 1、4、5）**
- 任務：plan-review、implementation-review、code-review 均使用 `/fleet` 指令路由到對應 skill
- 技術實現：`/fleet @python-plan-review/`、`/fleet @python-implementation-review/`、`/fleet @python-code-review/`
- 依賴：agent tools 宣告需包含 `agent`
- 成本：低（現有 python-project-init 有 precedent）
- 架構合規：`fits existing architecture`

**B3 — step.md Phase 3 gate**
- 任務：在 Phase 4 前執行 `plan-step-tracker check_all_succeeded <topic>`
- 技術實現：`python .github/skills/plan-step-tracker/scripts/step_tracker.py check_all_succeeded <topic>`；exit code 1 → 阻擋
- 依賴：plan-step-tracker 腳本（已存在）
- 成本：低（呼叫現有腳本）
- 架構合規：`fits existing architecture`

### 受 C1 已解決：全部可規劃

**B4 — Phase State Machine（active gate 路徑）← C1 已解決**
- 決策：**Active Gate**（主動阻擋）
- 技術實現：
  - Phase 4 gate：`plan-step-tracker check_all_succeeded <topic>`（exit code 1 → BLOCKED）
  - needs-rework：agent 重新叫用對應 skill（/fleet 路由），不需 STOP POINT
  - Phase 0：從 step.md `## Workflow Stages` 推斷 current phase（session 恢復）
- 成本：中（phase detection 邏輯 + 路由決策表）
- 架構合規：`fits existing architecture`（step.md 格式穩定，plan-step-tracker 已支援）

**B5 — needs-rework 迴路← C1 已解決**
- 決策：**內部迴路**（agent 自行重新叫用 authoring skill）
- 路由表：
  - plan-review needs-rework → `/fleet @python-plan-authoring/` → 重新 plan-review
  - impl-review needs-rework → 通知 executor 回到 Phase 4 → 重新 impl-review
  - code-review needs-rework → 通知 executor 回到 Phase 4 → 重新 impl-review → 重新 code-review
- 成本：低（條件路由，無 state machine 需求）
- 注意：迴路不設上限；人類可在任意 turn 中止

**B6 — D1 classifier 責任歸屬 ← 已決策為 standalone skill**
- 決策：提取為 `.github/skills/python-d1-classifier/`
- 技術實現：workflow agent Phase 2 呼叫 `/fleet @python-d1-classifier/`；獲取 trivial/non-trivial verdict 後決定是否繼續 Phase 3
- tdd-test-authoring：移除內嵌 D1 步驟，改為接受外部 D1 verdict 作為輸入
- 成本：中（新 skill 需完整 creator/reviewer 流程）
- 架構合規：`fits existing architecture`（新 standalone skill，符合 skills/ 結構）

**B7 — Session 重置後 Phase 恢復 ← 已決策**
- 決策：從 step.md `## Workflow Stages` 推斷 current phase
- 技術實現：pre-flight 讀取 step.md；Workflow Stages 區段的 [X]/[ ] 狀態決定恢復點；step.md 不存在 → 從 Phase 0 重開
- 成本：低（純文件讀取邏輯）
- 架構合規：`fits existing architecture`

---

## Workstream C：python-d1-classifier（新增 standalone skill）

**C1 — 從 python-tdd-test-authoring 提取 D1 邏輯**
- 任務：建立 `.github/skills/python-d1-classifier/` 完整 skill folder（SKILL.md + reference.md + examples.md）
- 輸入：approved plan.md（Public Contract、Requirements、Affected Files 三段落）
- 輸出：`trivial` / `non-trivial` + reason（JSON 或 structured markdown）
- 成本：中（skill 需通過 agent-skill-creator + agent-skill-reviewer 流程）
- 依賴：python-tdd-test-authoring SKILL.md 需同步更新（移除內嵌 D1）
- 架構合規：`fits existing architecture`（`.github/skills/` 路徑，與其他 skills 一致）

**C2 — python-tdd-test-authoring 更新**
- 任務：SKILL.md inputs 更新：移除「D1 判斷」步驟；加入「D1 classifier output（verdict + reason）作為外部輸入」
- spec.md 優先序：明確聲明 spec.md 存在時為主要輸入（優先於 plan.md Requirements）
- 成本：低（文件更新）

---

## 架構合規自檢

| 面向 | 評估結果 | 備注 |
|------|----------|------|
| artifact 路徑（spec.md 在 plan/<topic>/） | `fits existing architecture` | 與 plan.md、step.md 同層，一致 |
| agent 檔案路徑（.github/agents/） | `fits existing architecture` | 已有 python-project-init、workflow-gate precedent |
| SKILL.md 更新（python-plan-authoring、python-tdd-test-authoring） | `fits existing architecture` | 屬於正常 skill maintenance |
| /fleet 呼叫模式 | `fits existing architecture` | python-project-init 已有 precedent |
| step.md gate 使用 plan-step-tracker 腳本 | `fits existing architecture` | 腳本已存在且有測試 |
| STOP POINT 語義（active gate） | `fits existing architecture` | C1 已解決為 active gate；與 handoff-workflow.md 對齊 |
| VERSION bump 時機 | `fits existing architecture` | C3 已解決：agent-skill-reviewer approved 後才 bump |
| python-d1-classifier 新 skill | `fits existing architecture` | `.github/skills/` 路徑；需 creator/reviewer 流程 |

---

## 成本總覽（悲觀估計）

| Workstream | 複雜度 | 主要風險 |
|-----------|--------|---------|
| A1 spec-template.md | 低 | 無 |
| A2 tdd-skill fallback 更新 | 低 | 無 |
| A3 plan-authoring 必要性聲明 | 低 | 無（C2 已解決） |
| B1 pre-flight | 低 | Phase 恢復邏輯從 step.md 讀取（B7 OK）|
| B2 /fleet 路由 | 低 | — |
| B3 step.md gate | 低 | — |
| B4 STOP POINT（active gate） | 中 | phase detection 需正確讀 step.md Workflow Stages；session 恢復邏輯 |
| B5 needs-rework 迴路 | 低 | 無上限迴路；人類可中止（可接受）|
| B6 D1 classifier（standalone skill） | 中 | 需完整 creator/reviewer 流程；是 workflow agent 的前置依賴 |
| B7 session 恢復 | 低 | step.md Workflow Stages 格式需穩定 |
| C1 python-d1-classifier skill 建立 | 中 | 新 skill；需 creator + reviewer；是 B4/B6 的前置依賴 |
| C2 tdd-test-authoring 更新（D1 移除） | 低 | 需確認 tdd-skill 現有 D1 邏輯可乾淨提取 |

---

## Rollback-to-Alignment 觸發器（已全部解除）

| ROLLBACK | 原因 | 解除狀態 |
|----------|------|---------|
| ROLLBACK-1（C1） | agent 觀察者 vs. active gate | ✅ 已解除：active gate 已確認 |
| ROLLBACK-2（C2） | spec.md 選用 vs. TDD 品質 | ✅ 已解除：D1 non-trivial 時強制 |
| ROLLBACK-3（C3） | VERSION bump 時機 | ✅ 已解除：reviewer approved 後 bump |

---

## 已確認非目標（技術層面無爭議）

- spec.md **不**取代 plan.md 的 Requirements 段落（兩份文件並存）
- workflow agent **不**執行 git 操作（commit、push、PR）
- workflow agent **不**管理多個並行 topic（單一 topic per session）
- spec.md **不**需要獨立 review（直接作為 tdd-test-authoring 輸入）

---

## 技術翻譯完整性評估

| 檢查項目 | 狀態 |
|----------|------|
| 每個需求是否映射至技術實現或明確 blocker？ | ✅ 全部已映射 |
| 成本/負擔是否明確？ | ✅ 各 workstream 均已標注 |
| 架構合規自檢是否完整？ | ✅ 全部 `fits existing architecture` |
| 矛盾是否有 rollback trigger？ | ✅ 全部 ROLLBACK 已解除 |
| 隱性耦合是否揭露？ | ✅ B6/B7 已決策；C1/C2 workstream 已納入 |
| 新需求（D1 classifier）是否已技術化？ | ✅ Workstream C 已定義 |

**結論：技術規格完整。可進行 plan 更新並開始執行。**

執行順序（依前置依賴）：
1. `python-d1-classifier` skill（C1）← workflow agent 的前置依賴
2. `spec-template.md`（A1）+ `plan-authoring` 更新（A3）← spec.md 合約
3. `tdd-test-authoring` 更新（A2 + C2）← D1 外部化
4. `python-implementation-workflow.agent.md`（B 系列）← 依賴 C1 完成
5. `README.md` 更新 + `VERSION` bump（reviewer approved 後）
