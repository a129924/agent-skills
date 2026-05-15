---
topic: python-implementation-workflow-drift-handling
status: READY FOR TECHNICAL TRANSLATION
created: 2026-05-15
updated: 2026-05-15
---

# Python Implementation Workflow Drift Handling — Business Requirements

> 這份基線只凍結 **custom agent 與 repo workflow 文件** 對 drift / correction handling
> 的需求，不直接設計最終 markdown 寫法或實作細節。

---

## 問題陳述

目前 `.github/agents/python-implementation-workflow.agent.md` 與
`plan/agent-handoff-workflow.md` 對一般 `needs-rework` 迴路已有定義，但對下列情境仍缺少
一致、可審查、可回溯的處置契約：

1. implementation 在執行中或 review 後，被發現已偏離 repo-visible source of truth
2. human 明確指出目前方向錯誤，但 workflow 尚未定義如何在不破壞 source-of-truth 規則下處理
3. medium / high severity drift 發生後，缺少 correction artifact、parent sync、與 closure
   authority 的明確規則

若這個缺口不補齊，將造成：

- workflow 在 medium / high drift 下可能繼續前進而沒有留下 correction trail
- human / planner / implementer 的責任邊界被模糊化
- correction sidecar 與 parent artifacts 長期分裂，current truth 與 historical truth 無法重建

---

## Actors

| Actor | 角色 | 權限 / 邊界 |
| --- | --- | --- |
| Human operator | 指出方向錯誤、補充意圖、決定是否繼續此 topic | 可提出 correction signal，但不得只靠聊天內容直接覆寫 repo-visible source of truth |
| Workflow agent | 執行 phase routing 與 gate | 可做 provisional severity classification；不得最終確認 severity；不得自行關閉 correction |
| Planner | 確認 correction severity，定義 correction direction，決定何時可關閉 correction | 必須確認 medium / high drift 的最終 severity；在必要 review 通過後才可關閉 correction |
| Implementer | 根據已凍結 direction 修補 implementation | 可處理 low severity defect；不得自行改 correctness criteria 或省略 required correction artifacts |
| Reviewer | 在 implementation review / code review 中發現 drift、scope 問題、品質問題 | 可觸發 correction signal；不得直接替 planner 完成 correction authoring |

---

## Measurable Requirements

### R1 — Medium / High drift 不得 silent advance

| Element | Requirement |
| --- | --- |
| Actor | Workflow agent + Planner |
| Condition | 在 implementation、implementation review、code review，或 human 明確指出方向錯誤時，若發現該問題影響 source-of-truth semantics、public contract meaning、architecture boundary、或 phase routing |
| Observable result | Workflow agent 產生 provisional severity classification，並阻止 topic 直接前進到下一個 later phase；Planner 必須確認最終 severity 後，workflow 才能進入 correction path |
| Metric / decision rule | 若問題屬 medium / high severity drift，則在 Planner 未確認 severity 前，不得從當前 discovery phase 前進到後續 phase |
| Failure meaning | 重大 drift 被當成普通 rework 放行，造成錯誤方向持續擴散 |

### R2 — Ordinary `needs-rework` 與 correction-triggering drift 必須可區分

| Element | Requirement |
| --- | --- |
| Actor | Workflow agent + Planner |
| Condition | 收到 `needs-rework` 類型輸出或 drift signal 時 |
| Observable result | Workflow 使用 impact-based rule 區分 ordinary rework 與 correction-triggering drift |
| Metric / decision rule | 只要問題改變 source-of-truth semantics、public contract meaning、architecture boundary、或 phase routing，即屬 correction-triggering drift；否則可保留為 ordinary `needs-rework` |
| Failure meaning | 所有 `needs-rework` 被混成同一類，導致 correction artifact 該出現時沒有出現，或普通修補被過度升級 |

### R3 — Correction artifact 必須依 severity 出現

| Element | Requirement |
| --- | --- |
| Actor | Planner + Implementer |
| Condition | Planner 已確認 medium / high severity drift |
| Observable result | 依 severity 產生對應 correction layer artifact，且檔名採 `*.correction-plan.md` / `*.correction-step.md` |
| Metric / decision rule | Low severity -> 不需要 correction artifact；Medium severity -> 至少要 `*.correction-plan.md`；若修補需要多步 implementer work，必須再加 `*.correction-step.md`；High severity -> 必須同時有兩者 |
| Failure meaning | correction 方向只有口頭說明，沒有 repo-visible artifact 可供 review、resume、或 audit |

### R4 — High severity drift 必須把現有 implementation 視為 suspect code

| Element | Requirement |
| --- | --- |
| Actor | Planner + Workflow agent |
| Condition | Planner 確認 drift 為 high severity |
| Observable result | 現有 implementation 不再被當成可直接 patch 的可信基線，而是進入 correction / replan path |
| Metric / decision rule | High severity drift 一律要求 `*.correction-plan.md` + `*.correction-step.md`，且 workflow 不得把現有 implementation 當作 ordinary patch baseline 直接前進 |
| Failure meaning | 高風險錯誤被當成局部 patch，導致越修越偏且測試/設計一起失真 |

### R5 — Parent artifacts 必須回補成 current truth

| Element | Requirement |
| --- | --- |
| Actor | Planner |
| Condition | correction direction 已確認為 final，且 implementer 修正完成、code review 通過、planner review 通過 |
| Observable result | parent plan / spec / step 被同步回補為最新有效執行狀態 |
| Metric / decision rule | correction 不能只停留在 sidecar；close correction 前，至少必須同步：updated task direction、updated steps、updated acceptance criteria、changed architecture rule（若有）、changed routing decision（若有） |
| Failure meaning | correction artifact 與 parent artifacts 長期分裂，使用者無法知道哪份才是 current truth |

### R6 — Correction artifact 必須保留作 historical truth

| Element | Requirement |
| --- | --- |
| Actor | Planner + Workflow agent |
| Condition | correction 已完成、resolved、或 superseded |
| Observable result | correction artifact 仍被保留作 decision audit trail，不因 parent sync 完成而刪除 |
| Metric / decision rule | correction artifact 可標記為 resolved / superseded，但不得直接刪除；內容至少保留：drift trigger、修正原因、原 plan 不足處、保留/移除/重寫範圍、最終修正方向 |
| Failure meaning | correction 的來龍去脈消失，之後無法 audit 或解釋為何改變 workflow 行為 |

### R7 — Role boundary 必須在 drift 情境下保持清楚

| Element | Requirement |
| --- | --- |
| Actor | Human operator + Workflow agent + Planner + Implementer |
| Condition | 任一 correction-triggering drift 發生時 |
| Observable result | Human 負責提出方向疑慮；Workflow agent 負責 provisional routing；Planner 負責 final severity / closure；Implementer 負責執行修補 |
| Metric / decision rule | Human 訊息本身不得直接覆寫 repo-visible source of truth；Workflow agent 不得最終確認 severity；Implementer 不得自行重新定義 correctness criteria；Planner review 與 code review 通過前不得關閉 correction |
| Failure meaning | correction 被聊天訊息或 implementer 臨場決策接管，source-of-truth 規則失效 |

### R8 — Correction artifact 必須帶 parent sync note

| Element | Requirement |
| --- | --- |
| Actor | Planner |
| Condition | Medium / High severity correction artifact 被建立時 |
| Observable result | correction artifact 內包含 parent sync note，說明 parent artifacts 未來要如何回補 |
| Metric / decision rule | sync note 至少要列出：parent plan 哪一段被補充或修正、acceptance criteria 是否改變、phase routing 是否改變、existing tasks 是否改變 |
| Failure meaning | correction artifact 雖存在，但後續 parent sync 沒有明確目標，容易留下永久分裂 |

---

## Explicit Assumptions

1. 本 topic 只處理 `.github/agents/python-implementation-workflow.agent.md` 與
   `plan/agent-handoff-workflow.md` 的 drift / correction policy，不直接擴張到其他 skill 的實作。
2. repo-visible source of truth 仍以 parent plan / spec / step 與 repo workflow doc 為主；correction artifact
   只是一層 correction layer，不是永久取代物。
3. Workflow agent 可做 provisional classification，是因為需要先阻止 silent advance；但最終權限仍屬 Planner。
4. 本 topic 的 analysis / spec / implementation work 應在 dedicated worktree 中進行；這是此 topic 的執行前提，不是要強行變成所有 workflow 的全域規則。

---

## Non-goals

- 不把 `*.correction-plan.md` / `*.correction-step.md` 變成所有 workflow 的 always-on artifact
- 不重新設計整個 python implementation workflow 的 phase 數量
- 不修改 git commit / push / PR / merge 的 repo-level STOP POINT 規則
- 不直接修改其他 python-* skill 的責任邊界
- 不在這個 baseline 中定義 markdown 段落的最終字句或 machine parser 實作方式

---

## Contradictions Log

| 矛盾 | 衝突內容 | 解決方式 |
| --- | --- | --- |
| C1 | 現有 agent 說 `needs-rework` 一律內部迴路；新需求要求 medium/high drift 升級為 correction layer | 以 impact-based rule 分流：ordinary rework 仍走內部迴路；影響 source-of-truth semantics / public contract meaning / architecture boundary / phase routing 的 drift 必須走 correction path |
| C2 | Human 需要能指出方向錯誤；repo 規則又禁止 hidden chat override repo-visible artifacts | Human 訊息只觸發 classification，不直接覆寫 source of truth；最終 correction 必須由 Planner 確認並落在 repo-visible artifact |
| C3 | correction artifact 是否應該全域強制 | 改為 conditional required artifact pattern：只在 medium/high severity drift 時強制 |

---

## Extreme Boundary Checks

| 邊界條件 | 需求仍成立？ | 說明 |
| --- | --- | --- |
| Human 提出方向錯誤，但 Planner 尚未確認 severity | ✅ | workflow 必須停在 provisional routing，不得 silent advance |
| `*.correction-plan.md` 已存在，但 parent sync 尚未完成 | ✅ | correction 不可關閉；parent artifacts 仍未達 current truth |
| Implementer 已修好 code，但 code review / planner review 未通過 | ✅ | correction 不可關閉，也不可先同步 parent truth 為最終狀態 |
| 第二個 medium/high drift 在第一個 correction 關閉前被發現 | ✅ | workflow 必須再次要求 Planner 決定是延伸現有 correction layer 或建立新的 correction layer；在決定前不得前進 |
| correction artifact 已 resolved，但之後需要追溯為何改動 routing | ✅ | correction artifact 必須被保留，作為 historical truth |
| Wrong-role actor 只有 view / comment 權限，卻試圖直接關閉 correction | ✅ | correction closure authority 仍屬 Planner；不得因 comment 出現而直接關閉 |

---

## Blockers

無阻礙項目。需求已足夠進入技術翻譯。
