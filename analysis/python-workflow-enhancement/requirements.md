---
topic: python-workflow-enhancement
status: READY FOR TECHNICAL TRANSLATION — C1/C2/C3 已解決，D1 獨立化已決策
created: 2026-05-09
updated: 2026-05-09
---

# Python Workflow Enhancement — Business Requirements

> **Socratic review 結果（已解決）**：C1/C2/C3 三個矛盾已取得人類決策。
> D1 classifier 獨立化已決策。以下為凍結基線。

---

## 問題陳述

**原始主張：**
> 「SubAgent 之間現在有了共享的可見狀態。Executor 沒完成就無法通過 review gate。」

**Socratic 追問：**
- 「shared visible state」對誰可見？只對編排 agent？還是對人類使用者也可見？
- 現在「沒有共享狀態」造成什麼可觀察的損失？是 review 被錯誤放行？還是流程重工？
- 「Executor 沒完成就無法通過 review gate」——在現有系統中，這個「無法」指的是
  系統拒絕，還是只是人工慣例可跳過？

---

## 已識別 Actors

| Actor | 角色 | 未解決問題 |
|-------|------|-----------|
| Plan Author | 撰寫 plan.md，選擇性撰寫 spec.md | **誰負責撰寫 spec.md？** plan-authoring skill 產出？還是人類手動？兩者的品質期望是否相同？ |
| Executor | 執行 Implementation Steps，標記 [X] | **人類或 AI agent？** 這個判斷改變整個 STOP POINT 語義 |
| Orchestrator Agent | 觀察並路由 workflow | **觀察者還是執行者？**（見矛盾 C1） |
| Reviewer Agent | 對各 phase 進行獨立審查 | 明確，無爭議 |
| Human | 確認 STOP POINT 並 resume | 明確，無爭議 |

---

## 需求（已轉換為可觀察形式）

### Feature 1：spec.md 行為規格檔

**R1-1（規格存在性）**
- Actor：Plan Author（人類）+ python-plan-authoring skill（產出觸發）
- Condition：D1 classifier 返回 non-trivial（由 workflow agent 先行執行 D1）
- Observable result：`plan/<topic>/<topic>.spec.md` 存在且包含至少 1 個 Acceptance
  Criteria 條目、至少 1 個 Behavioral Scenario（Given/When/Then）
- Metric：spec.md 不存在時 workflow agent **BLOCKED**，並明確指示回到 plan-authoring 補產
- 決策紀錄（C2）：spec.md = 輕量 SDD（Specification Design Document）；在 D1 non-trivial
  時為強制產出，非選用；沒有 spec.md 的 TDD 不可接受

**R1-2（向下相容）**
- Condition：spec.md 不存在
- Observable result：python-tdd-test-authoring 仍可正常執行，產出 RED tests
- Metric：現有 plan.md Requirements 段落作為 fallback，行為與 v0.50.0 一致

**R1-3（衝突解決優先序）← 已解決**
- Condition：spec.md 的 Acceptance Criteria 與 plan.md Requirements 段落描述不一致
- Observable result：spec.md 優先（spec.md = SDD，是更完整的行為合約）；plan.md Requirements
  與 spec.md 衝突時，tdd-test-authoring 以 spec.md 為準，並在輸出 issues 中記錄衝突

---

**R-NEW：D1 Classifier（新增需求）**
- Actor：Workflow Agent
- Condition：plan-review 返回 approved 後，進入 TDD 階段前
- Observable result：`python-d1-classifier` 作為獨立 skill 執行，返回
  `trivial`（skip TDD）或 `non-trivial`（continue，含分類原因）
- Metric：workflow agent 先執行 D1，再決定是否叫用 tdd-test-authoring
- 決策紀錄（B6）：D1 從 tdd-test-authoring 內部邏輯獨立出來，成為可被複數 skill/agent 使用的
  standalone skill（`.github/skills/python-d1-classifier/`）

---

### Feature 2：python-implementation-workflow Agent

**R2-1（入口條件）**
- Actor：Human（啟動 workflow）
- Condition：`plan/<topic>/<topic>.plan.md` 已存在
- Observable result：Agent 成功定位 plan.md 並進入 Phase 1
- Metric：若 plan.md 不存在，agent 明確拒絕並說明原因（不猜測 topic）

**R2-2（STOP POINT 不可繞過）**
- Actor：Orchestrator Agent
- Condition：各 Phase 完成時
- Observable result：未收到人類明確 resume 訊息前，agent 停止所有後續動作
- Metric：與 repo 現有 STOP POINT 合約（plan/agent-handoff-workflow.md）行為一致

**R2-3（needs-rework 迴路行為）← 已解決**
- Condition：plan-review 或 implementation-review 或 code-review 返回 needs-rework
- Observable result：**內部迴路**，workflow agent 重新叫用對應的 authoring/authoring skill，
  無需人類介入
  - plan-review needs-rework → /fleet @python-plan-authoring/ 補修 → 重新 plan-review
  - implementation-review needs-rework → 通知 executor 回到 Phase 4 → 重新 impl-review
  - code-review needs-rework → 通知 executor 回到 Phase 4 → 重新 impl-review → 重新 code-review
- Metric：迴路不設上限（由人類決定是否中止）；每次迴路都記錄 needs-rework 原因
- 決策紀錄（C1）：agent 在 Phase 4（step.md gate）採用**主動阻擋型**；
  needs-rework 迴路不需要 STOP POINT（全部內部處理）

---

## 矛盾紀錄（Contradiction Log）← 全部已解決

**C1 — 主動阻擋 vs 被動觀察（已解決）**
- 決策：**主動阻擋**（Active Gate）
- Phase 4（implementation gate）使用 plan-step-tracker check_all_succeeded；未完成 → BLOCKED
- needs-rework 使用**內部迴路**，agent 自行重新叫用對應 skill，不設 STOP POINT
- 唯一等待人類的點是 Phase 4 executor 完成實作
- commit/push/PR 相關的 STOP POINT 不在本 workflow agent 範圍內

**C2 — spec.md 強制 vs 選用（已解決）**
- 決策：**D1 non-trivial 時強制（mandatory）**；D1 trivial 時跳過
- spec.md = 輕量 SDD；由 python-plan-authoring 產出；無 spec.md 時 workflow BLOCKED
- TDD + SDD 是本 workflow 的設計哲學；spec.md IS the SDD

**C3 — VERSION bump 時機（已解決）**
- 決策：**agent-skill-reviewer approved 後才 bump**；與 repo 版本治理一致

---

## 邊界條件處置（B1–B6）

| # | 邊界條件 | 決策 |
|---|----------|------|
| B1 | plan-review 連續 needs-rework | 內部迴路，不設上限；由人類中止 |
| B2 | spec.md 不完整 | tdd-test-authoring 標記 INCOMPLETE；不 block，但產出 issues |
| B3 | 多個 agent 同一 topic | 不支援（非目標）；A4 確認：每次一個 agent/topic |
| B4 | Session 重置後恢復 | 從 step.md Workflow Stages 重建 phase（B7 OK）|
| B5 | spec.md 與 plan.md 矛盾 | spec.md 優先（SDD 是更完整的行為合約）；記錄衝突 |
| B6 | D1 responsibility 邊界 | D1 提取為 standalone skill（`.github/skills/python-d1-classifier/`）|

---

## 非目標（已確認範圍外）

1. spec.md **不取代** plan.md Requirements 段落（互補，不替換）
2. spec.md **不需要**獨立審查流程（直接作為 tdd-test-authoring 輸入）
3. workflow agent **不處理** git 操作（commit、PR）— scope ends at code-review
4. workflow agent **不支援**多 topic 並行（A4 確認）
5. workflow agent **可**從 step.md 恢復狀態（B7 OK）

---

## 凍結評估

| 檢查項目 | 狀態 |
|----------|------|
| 每個需求是否有 actor + condition + observable result + metric？ | ✅ |
| 矛盾是否已解決？ | ✅ C1/C2/C3 全部已解決 |
| 邊界條件是否已處理？ | ✅ B1–B6 已處置 |
| 非目標是否明確？ | ✅ 5 個範圍問題已聲明 |
| 新需求（D1 classifier）是否已納入？ | ✅ R-NEW 已定義 |

**結論：基線已凍結。可進行 technical translation。**
