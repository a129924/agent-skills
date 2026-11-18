# feasibility-adoption-delivery-boundary Plan

分析層說明（非阻擋）　此 topic 無對應的 `analysis/feasibility-adoption-delivery-boundary/requirements.md` 和 `technical-spec.md`。以使用者已核准的對話範圍作為需求基線。

## Goal / Outcome

**Goal**　讓 UI、Pipeline、Facade 等能力依本輪契約交付正式實作，以實際消費和對應證據驗收。缺少完整產品入口時，仍能完成符合範圍的能力採用，並單獨記錄產品整合情況。交付為 canonical skill、案例、紀錄模板、對應 inventory 更新與獨立審查後的 Draft PR。

## Scope

**In-Scope**

- 在 `feasibility-adoption` 既有步驟內說明交付層次、正式能力與驗收支援、來源寫入授權及採用完成判斷。
- 補充既有紀錄模板及通用案例。用既有生成器更新 canonical inventory 的對應 hash。
- 使用既有 repo 實作與審查流程。以 Graphify、PR Lens、Archify 和 show-me 支援查核與交付。

**Out-Of-Scope**　參考專案、舊 topic、其他 skills、安裝副本、平台投影、治理與工具設定、歷史紀錄回填、stable-library promotion、外部圖資發布、merge、tag 及 release。

## Locked Decisions

1. 明列交付是契約、單一能力、元件、協調行為或完整產品整合。完成範圍內必要組合。承諾可執行行為時，實際執行正式實作。純契約以具體消費端的相容性或遵循證據驗收。空方法、未執行的測試或 Preview 宣告留下證據缺口。
2. 分別判斷構件的正式交付用途、驗收用途和來源寫入權。測試、Preview、runner 或受控 host 可直接消費正式能力，按需要提供範圍外依賴的替身。保留宿主、診斷及模擬支援的用途邊界。受測能力本身須是真實正式實作。
3. 依目標專案規則辨識既有入口是凍結驗證、持續維護工具或本輪新增組裝。凍結來源需要改接時，使用已獲准的驗收位置。維護工具的必要調整依既有授權執行。若明確限制或重大衝突仍待解，提出最小差異並保留可獨立完成的工作。Git 歷史提供追溯，寫權依現行規則和授權。Plan 結案本身不凍結曾涉及的正式來源。
4. 採用判定依本輪契約、正式實作、可確認的實際消費與對應證據。驗收接入與產品接入分開記錄。範圍外的產品組裝無須列成部分採用缺口。若本輪承諾產品整合，受控驗收只支持實際查驗的範圍，另須取得產品整合證據。必要驗收缺證時依原定義保留部分採用或不確定及其理由。
5. 沿用現有採用分類、驗證狀態及工作流程。既有採用紀錄按原內容讀取。新欄位記錄本輪證據及限制，避免將缺歷史欄位本身當作未採用證據。本輪按需要選工具，沒有固定驗收工具組合。

## Boundaries / Exclusions

**Non-Goal**　實作下游產品、回修參考專案，或為 skill 使用新增 phase、approval、runtime orchestration 或狀態系統。既有獨立 skill 審查與 Git 授權流程照常適用。本文案例均為示意。

實作與產生器限指定 feature worktree。若必要寫入超出 Artifact Paths，先交 Planner 對齊 scope。README、VERSION 與 Copilot instructions 屬唯讀範圍。本題無 stable-library promotion 或 release 排程。

## Status / Allowed Transitions

- **Current**　使用者已核准對話範圍與 Draft PR 交付。規劃檔就緒後，待獨立 Plan-Reviewer verdict、Planner readiness 與 Main Agent 提交獲准的 planning baseline。階段完成由角色依實際證據更新。
- **Branch**　`fix/andrew/feasibility-adoption-delivery-boundary`，base `dev`，起始 SHA `0a0501a6f3c05c32b4abea093d1f4ac20d591cdf`。隔離工作樹 `agent-skills.worktrees/agent-20261118-feasibility-adoption-delivery-boundary`。
- **Transitions**　獨立 Plan-Reviewer 核對 → Planner readiness → Main Agent 提交已獲授權的四份 planning baseline → `planned` → `creator-in-progress` → `review-ready` → `reviewer-in-progress` → `approved` 或 `needs-rework`。回修回到 `creator-in-progress`，在同一 write-set 驗證和複審。`approved` 後 Planner 提供 boundedness evidence，Main Agent 執行 Phase 4.5 checkpoint，未通過退回 `creator-in-progress`，通過進 `publish-in-progress` → `pr-open`。
- 使用者已授權本 topic 的 planning baseline commit、完成審查與必要檢查後的實作語意 commit、push 及對 `dev` 的 Draft PR。交 human review 後停止，維持 Draft。

## Artifact Paths

**ReadOnly**　`AGENTS.md`、`docs/repo-positioning.md`、`plan/agent-handoff-workflow.md`、`plan/topic-plan-contract.md`、舊 topic 與歷史、其他 skills、`scripts/build_skills_inventory.py`、既有 tests、`README.md`、`VERSION`、`.github/copilot-instructions.md`、平台投影、repo 設定及相符既有關聯圖。

**Written**

| 路徑 | Owner | 用途 |
| --- | --- | --- |
| `plan/feasibility-adoption-delivery-boundary/feasibility-adoption-delivery-boundary.plan.md` | Plan-Creator | 執行契約 |
| `plan/feasibility-adoption-delivery-boundary/feasibility-adoption-delivery-boundary.step.md` | Planner | 階段證據與交接 |
| `plan/feasibility-adoption-delivery-boundary/feasibility-adoption-delivery-boundary.review-log.md` | 各獨立 Reviewer | Verdict、受審版本及回修依據 |
| `plan/feasibility-adoption-delivery-boundary/feasibility-adoption-delivery-boundary.summary.md` | Planner、Main Agent | 交付事實與 human review 停點 |

工具圖稿、patch 快照、provenance、receipts 及檢視紀錄置於 repo 外的 `/private/tmp/feasibility-adoption-delivery-boundary/`，按 `archify/`、`pr-lens/` 子目錄與 `tool-status.md` 管理。Graphify 只讀既有圖。

**Modify**

| 路徑 | Owner | 用途 |
| --- | --- | --- |
| `skills/feasibility-adoption/SKILL.md` | Implementer | 採用契約、權限、完成判斷及必要檢查 |
| `skills/feasibility-adoption/templates/adoption-record.md` | Implementer | 驗收、來源權限及產品接入的追溯資訊 |
| `skills/feasibility-adoption/examples.md` | Implementer | 通用案例及負向判定 |
| `artifacts/skills-inventory.jsonl` | Implementer | 既有生成器重算 skill tree hash |

**Deleted**　無 tracked 檔案刪除。

## Implementation Steps

1. 補強 `SKILL.md` 既有流程、必須檢查和完成判斷。維持獨立使用，並以「實際接入」涵蓋由具體消費端直接使用正式能力的情境。
2. 調整紀錄模板，納入交付範圍、驗收入口與版本、受測正式版本、來源狀態及授權、替身角色、產品整合要求與證據、結果限制。必要產品整合與受控驗收各自有事實和缺口。
3. 保留舊示例中的適用規則，補上通用案例。若舊例因缺必要接入而屬部分採用，明示缺的是本輪承諾的接入。
4. 執行 `python3 -B scripts/build_skills_inventory.py` 重生 inventory。確認 canonical path 與列數維持，本 skill hash 隨內容改變。
5. Graphify 0.9.73 的每次 CLI 呼叫設 `GRAPHIFY_NO_AUTO_REFRESH=1`。僅查有效且來源相符的既有圖，並以原始碼核對關鍵關係。圖缺失或不適用時使用定向原始碼查核，記錄原因。
6. PR Lens 0.11.0 用實際本機 bounded diff 產生變更圖並 validate、render。完整 topic 快照納入計畫範圍內未追蹤檔案。記錄實際 base、檔案範圍、來源及未提交狀態，核對 render manifest。需要發布前的最終版本證據時，以已驗證的實際差異為準。
7. Archify 依工具契約產出判斷流程的 workflow showcase，依序 validate、deliver、visual-check 並保存精確交付版本、receipts、四 viewport 截圖與人工檢視證據。自動校驗連續兩輪未改善最佳錯誤數即停止，視覺修正最多兩輪。實際驗證缺口照實記錄。
8. show-me 的對話版沿用 Mermaid 判斷流程。實際交付時連結已驗證的圖與 receipts，準確標明來源範圍。

## Validation / Acceptance Checks

**TestCase**

| 情境 | 驗收結果 |
| --- | --- |
| 正式 UI library 尚無完整 App | 由受控消費端直接使用正式元件，取得對應行為證據後可完成本輪元件採用。 |
| 已凍結的驗證入口需要改接 | 選擇獲准的替代位置，舊驗證版本和重現證據可追溯。 |
| Pipeline 使用獲准維護的驗收工具 | 可完成必要改接並執行真實正式步驟，紀錄版本與行為結果。 |
| Facade 須用替身供應外部依賴 | 真 Facade 可驗收其協調。替換 Facade 本身、空方法或未執行宣告均留下缺口。 |
| 本輪範圍包含產品整合 | 受控驗收只證明其查驗能力，完整採用另須產品端實際整合證據。 |
| fixture 或 harness 僅供驗收 | 追溯其用途、來源與授權、入口版本、受測正式版本、替身與證據限制。 |

- 核對 frontmatter、必要章節、站內相對連結、示例及模板互相一致，且 `git diff --check` 通過。
- 執行 `python3 -m pytest -q tests/test_build_skills_inventory.py`。以既有腳本兩次重建到 repo 外並 `cmp`，比對 tracked inventory，確認只有 `feasibility-adoption` 這筆的 hash 變動。
- Tester 列實際命令、結果與覆蓋。示意案例走讀、工具證據與未執行項分別記錄。獨立 `agent-skill-reviewer` 核對能力契約及證據，Planner 提供鎖定範圍、實際差異與驗證結果的 boundedness evidence。Main Agent 依 Phase 4.5 判斷契約對齊及路由，通過後核對實際 staged set 與語意 commit，再執行獲准的 Draft PR 交付。

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

授權終點是 Draft PR 與 human review。後續 merge、清理、同步及 release 另依原流程與明示授權處理。本題沒有排定 post-merge 動作。

## Open Questions / Unresolved Items

無待確認的需求。Reviewer verdict、Planner readiness、planning baseline commit、實作驗證、工具證據與 Draft PR 均依後續事實登錄。
