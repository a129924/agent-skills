# feasibility-validation：可行性驗證 Skill 計畫

Analysis-layer routing: `INCOMPLETE`（nonblocking semantic warning）。Optional `analysis/feasibility-validation/requirements.md` 與 `analysis/feasibility-validation/technical-spec.md` 均不存在；不建立 analysis。需求基線為使用者原草案、五項能力澄清及 2026-10-07 已核准 formal plan。最新授權只更新 Git 交付終點為 topic commit → push → Draft PR（base `dev`）→ human review。

## Goal / Outcome

建立協助 agent 主動收斂問題、設計最小實驗及判讀證據的 `feasibility-validation` skill，回答影響後續實作選擇的技術未知。交付精簡行為指令、README 模板與正反例。

## Scope

涵蓋五項判斷：

1. **需要實驗嗎？** 官方文件或原始碼優先；只有必須執行才能確認、且答案影響實作選擇時，才進入實驗。
2. **到底驗證什麼？** 收斂為一個主要問題與明確假設，指出不同結果影響哪些實作選擇。
3. **最小實驗怎麼做？** 選擇足以區分假設成立與不成立的操作、輸入及觀察方式。
4. **怎樣算成立？** 執行前設定成功、失敗與無法判定的可觀察條件。
5. **證據支持到哪裡？** 區分觀察與推論，主動指出適用環境、輸入、條件及限制。

保留原草案的實驗目錄、編號、六步流程、README 八段與證據要求。Repo 寫入只涵蓋列定七個路徑。

## Locked Decisions

- Skill 主動協助設計與判讀；目錄與模板負責保存過程及證據。
- 一個實驗對應一個主要問題；獨立依賴假設須標示，必要時拆案。
- 建置成功或測試通過，不自行證明主要假設成立。
- 驗證完成與假設成立分開判定；否定假設也可完成驗證。
- 按需啟用，結果回原決策位置，不新增必經 phase、gate 或 workflow binding。
- 語言與工具不限定；選擇足以回答問題且容易重現的方式。
- Complexity 採 `medium`；三份 skill 檔案為本題完整交付面。
- 本題不涉及 stable-library promotion；允許經審查後 commit、push、Draft PR，停 human review。

## Boundaries / Exclusions

本題交付 skill，不執行個別實驗、不建立實驗 CLI 或另一套完整開發流程。

證據涉及已鎖定決策時，提出證據與影響，交回既有變更流程。實驗程式正式採用仍遵循原實作與審查流程；實驗完成不自動核准後續實作。

所有寫入限指定 feature worktree；禁止在 `/Users/andrew/code/python/agent-skills` dev worktree 實作。不得修改既有 skills、repo workflow、平台相容面、根目錄 `README.md`、`VERSION` 或 Copilot instructions。不含 stable promotion、projection、tag、release、merge 或延後發布。

Plan-Creator 落檔契約；獨立 Plan-Reviewer 核對落檔內容。Implementer 負責六項實作，Reviewer 獨立審查，Main Agent 負責 routing、Git 交付及進度同步；不得自我核准或模擬角色分離。

## Status / Allowed Transitions

目前為 `creator-in-progress`（ordinary `needs-rework` 回修）。Planning baseline 為 `85262e3`；獨立 Reviewer 發現 B1：未提供判準時須由 agent 主動設計，不能要求使用者先填答案。Implementer 正在同範圍回修；implementation approval 尚未取得。

- 2026-10-07 已建立 worktree `/Users/andrew/code/python/agent-skills.worktrees/agent-20261007-feasibility-validation`，branch `feat/andrew/feasibility-validation`，initial HEAD `60b3b5b77515c354ed355c1adb28a8ed349dda67`。
- 使用者已核准 formal plan 與 bounded commit／push／Draft PR 授權；無須重問同一授權，但仍須完成獨立審查、scope preview 與必要 gates。
- 先由獨立 Plan-Reviewer 核對 repo 四份 artifacts，解決 blocker，再由獲授權的 Main Agent commit planning artifacts；只有實際 commit 且 ready for execution 後才記 `planned`。
- 允許轉換：`planned → creator-in-progress → review-ready → reviewer-in-progress → approved|needs-rework`；`needs-rework → creator-in-progress`；`approved → creator-in-progress|publish-in-progress`；`publish-in-progress → pr-open`。
- 採標準 Phase 4.5 contract alignment；Main Agent 確認 Reviewer approval、plan alignment 與 pre-commit checks 後進 Git 交付。Stable-library handling 明確 skip。
- Draft PR base `dev`；到 human review 即停止本次執行，不輪詢 merge。本授權不包含 `pr-open → merged`；merge 及後續須另有明確授權。

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/feasibility-validation/feasibility-validation.plan.md` | Plan-Creator | 執行契約 |
| Progression | `plan/feasibility-validation/feasibility-validation.step.md` | Planner；Main Agent 同步實際 phase | 交接進度 |
| Review log | `plan/feasibility-validation/feasibility-validation.review-log.md` | Plan-Reviewer、Reviewer 各自記錄 | 審查與回修證據；Plan-Creator 僅初始化對話來源 |
| Summary | `plan/feasibility-validation/feasibility-validation.summary.md` | Planner；Main Agent 同步交付事實 | 結案及下一交接 |
| Skill | `skills/feasibility-validation/SKILL.md` | Implementer | 行為契約 |
| Template | `skills/feasibility-validation/templates/experiment-readme.md` | Implementer | 紀錄模板 |
| Examples | `skills/feasibility-validation/examples.md` | Implementer | 正例與證據不足反例 |

列定路徑為 executable contract，超出範圍先修正計畫。`README.md`、`VERSION`、`.github/copilot-instructions.md` 均不改。

PR Lens 以真實 base/head diff 製作 local artifacts，置於 repo 外 `/private/tmp/feasibility-validation`，不屬 repo artifact set、不修改 repo config、不上傳資產。Graphify 若無 usable existing graph 則 targeted source fallback，不自動 build；Main Agent 記錄實際結果。

## Implementation Steps

1. **建立 skill 入口。** 採 `medium` complexity，metadata 與正文一致，明列觸發、五項判斷、完成條件、權限邊界及 local references。
2. **明定資訊不足的處理。** 問題、決策影響或判準缺失時，列出缺口，不依猜測執行。可恢復缺口採 `SOFT FAIL／INCOMPLETE`；繼續會造成誤導時採 `BLOCKED`。這些 skill 處理結果與實驗四狀態分開。
3. **保留六步流程。** 定義問題 → 設定判準 → 設計最小實驗 → 執行並保存證據 → 判讀結果 → 寫回紀錄。補明決策影響、依賴假設、投入上限與停止條件。
4. **保留 README 八段。** 驗證什麼、為什麼、成功與失敗判準、環境與前置條件、重現步驟、是否成功、結果與證據、結論與限制。
5. **明定完成語意。** 「是否成功」保留未執行／成功／失敗／無法判定，同段記錄驗證任務是否完成及原因。取得足以支持決策的證據，或清楚交代無法判定原因、缺少證據與決策限制，皆可完成本次驗證。
6. **保留重現規範。** 使用 `experiments/E001/README.md`，編號採 E001、E002，建立前確認未占用。集中必要程式、設定與可公開資料；排除建置產物、秘密及非公開資料。記錄環境版本、輸入、指令、日期與證據位置，標示模擬證據，分開觀察、推論及限制。

## Validation / Acceptance Checks

採 skill 行為情境審查，不新增 production tests 或實驗 CLI。Independent Plan-Reviewer 核對 canonical 11 sections、exact paths、角色邊界及四 planning artifacts 一致性；Reviewer 評估實際 skill 輸出。Main Agent 做 scope preview 與必要 Git 交付 checks，不自行宣告獨立 review 通過。

| 情境 | 預期行為 |
| --- | --- |
| 官方文件或原始碼足以回答 | 留下依據，不建立實驗。 |
| UTF-8 跨區塊解析 | 刻意在多位元組字元內切分區塊，分批送入並核對完整輸出；整檔讀取成功不足以支持假設。 |
| 假設被否定 | 有效證據足以支持排除實作選擇，驗證仍可完成。 |
| 環境或前置條件不足 | 記錄無法判定、缺少條件及決策限制，不誤判為假設失敗。 |
| 有限或模擬證據 | 結論限定於實際測試條件，不宣稱普遍保證。 |
| 問題、決策影響或判準缺失 | 指出缺口，不猜測執行。 |
| 文件一致性 | 指令、模板與例子一致，驗證結果與 skill 處理狀態不混用。 |

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

## Post-merge / release actions

Git endpoint 為 topic commit → push → Draft PR（base `dev`）→ human review，由 Main Agent 在審查及 alignment 通過後執行。無 stable promotion、merge、post-merge sync、release、tag 或 projection 授權；不安排延後發布。本次到 human review handoff 即停止。

## Open Questions / Unresolved Items

無待選實作問題。Optional analysis layer `INCOMPLETE` 為 nonblocking warning，不新增 analysis。Planning baseline、Creator 實作、獨立 skill review round 2、contract alignment 與本機 checks 已完成。Git 交付與 human review handoff 待實際執行；Copilot 與外部 CI 未驗證，不宣告 merge readiness。
