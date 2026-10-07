# feasibility-validation：可行性驗證 Skill 計畫

Analysis-layer routing: `INCOMPLETE`（nonblocking semantic warning）。Optional `analysis/feasibility-validation/requirements.md` 與 `analysis/feasibility-validation/technical-spec.md` 均不存在；不建立 analysis。需求基線為使用者原草案、五項能力澄清及 2026-10-07 已核准 formal plan。原 Git 交付終點為 topic commit → push → Draft PR（base `dev`）→ human review；human review 已完成，使用者已明確授權 comment fixes → commit → push → reply/resolve，無 merge 授權。

## Goal / Outcome

建立協助 agent 主動收斂問題、設計最小實驗及判讀證據的 `feasibility-validation` skill，回答影響後續實作選擇的技術未知。交付精簡行為指令、README 模板與正反例。

## Scope

涵蓋五項判斷：

1. **需要實驗嗎？** 官方文件或原始碼優先；只有必須執行才能確認、且答案影響實作選擇時，才進入實驗。
2. **到底驗證什麼？** 收斂為一個主要問題與明確假設，指出不同結果影響哪些實作選擇。
3. **最小實驗怎麼做？** 選擇足以區分假設成立與不成立的操作、輸入及觀察方式。
4. **怎樣算成立？** 執行前設定成功、失敗與無法判定的可觀察條件。
5. **證據支持到哪裡？** 區分觀察與推論，主動指出適用環境、輸入、條件及限制。

保留原草案的實驗目錄、編號、六步流程、README 八段與證據要求。Repo 當前完整契約為列定八個 exact paths：3 skill + 4 planning + 1 generated inventory。既有七路徑 review 事實僅屬歷史。

## Locked Decisions

- Skill 主動協助設計與判讀；目錄與模板負責保存過程及證據。
- 一個實驗對應一個主要問題；獨立依賴假設須標示，必要時拆案。
- 建置成功或測試通過，不自行證明主要假設成立。
- 驗證完成與假設成立分開判定；否定假設也可完成驗證。
- 按需啟用，結果回原決策位置，不新增必經 phase、gate 或 workflow binding。
- 語言與工具不限定；選擇足以回答問題且容易重現的方式。
- Complexity 採 `medium`；三份 skill 檔案為 skill 行為交付面；另同步既有 generator 的 inventory 衍生產物，不改變 skill 行為。
- 本題不涉及 stable-library promotion；原授權允許經審查後 commit、push、Draft PR 並停 human review；該交接及 human review 已完成，現授權 bounded comment fixes → commit → push → reply/resolve。

## Boundaries / Exclusions

本題交付 skill，不執行個別實驗、不建立實驗 CLI 或另一套完整開發流程。

證據涉及已鎖定決策時，提出證據與影響，交回既有變更流程。實驗程式正式採用仍遵循原實作與審查流程；實驗完成不自動核准後續實作。

所有寫入限指定 feature worktree；禁止在 `/Users/andrew/code/python/agent-skills` dev worktree 實作。不得修改既有 skills、repo workflow、平台相容面、根目錄 `README.md`、`VERSION` 或 Copilot instructions。不含 stable promotion、projection、tag、release、merge 或延後發布。

Plan-Creator 落檔契約；獨立 Plan-Reviewer 核對落檔內容。Implementer 負責原六項 skill 實作與第七項 inventory regeneration，Reviewer 獨立審查，Main Agent 負責 routing、Git 交付及進度同步；不得自我核准或模擬角色分離。

## Status / Allowed Transitions

目前為 `needs-rework`（open PR 的 bounded inventory repair，planning 修訂待獨立 Plan-Reviewer approval）。2026-10-07T03:55:09.168860Z、HEAD `c0552e8b764eff64ffbd713a582695ed928ca847` 的外部快照確認 PR #127 OPEN／Ready；舊 11 threads resolved 為歷史，新 inventory thread `PRRT_kwDOSC_kWs6pv07c`（db `4202836714`）仍 unresolved，當前 unresolved = 1。使用者 renewed comment fixes → commit → push → reply/resolve 授權；無 merge 授權。

依使用者交接的獨立 Planner 判定，此留言為 `REQUIRED_CORRECTION / ADDRESS`，採普通 `needs-rework / IMPLEMENT_CONTINUE`，屬同一 authorized topic 的 derivative inventory sync，不新增 correction layer。此記錄為 Plan-Creator 引述 Planner provenance，非本輪獨立核准。

以下為歷史交付／審查事實：Planning baseline 為 `85262e3`，實作 commit 為 `e48255a`；B1 已修正並獲獨立 Reviewer round 2 `approved`。Phase 4.5 alignment、reviewed hashes、YAML／links／模板 checks 與七檔 pre-commit 均通過。分支已 push，PR [#127](https://github.com/a129924/agent-skills/pull/127) 原以 Draft 建立，base `dev`。2026-10-07T03:32:37.524174Z、HEAD `77d27dabab7c64b364cef0ea4461786f1935874e` 快照確認 OPEN、Ready（`isDraft=false`）；使用者已完成 human review 並明確授權 comment fixes → commit → push → reply/resolve。上一輪 bounded comment fixes 已獲獨立 Plan-Reviewer 與 Reviewer approved；Main Agent 已核對契約 alignment、靜態檢查、pre-commit 及七檔範圍。上一輪修正提交 `a1817327343e568c9d0c95858438bfaf699970d4` 已 push；7 ADDRESS、4 SKIP 均已附理由回覆並 resolve。2026-10-07T03:39:06.872446Z 的 PR 快照確認 OPEN／Ready、11 threads 全部 resolved、unresolved = 0。該快照只描述該時間及 head，未宣告 merge readiness。

- 2026-10-07 已建立 worktree `/Users/andrew/code/python/agent-skills.worktrees/agent-20261007-feasibility-validation`，branch `feat/andrew/feasibility-validation`，initial HEAD `60b3b5b77515c354ed355c1adb28a8ed349dda67`。
- 使用者已核准 formal plan 與 bounded commit／push／Draft PR 授權；無須重問同一授權，但仍須完成獨立審查、scope preview 與必要 gates。
- 先由獨立 Plan-Reviewer 核對 repo 四份 artifacts，解決 blocker，再由獲授權的 Main Agent commit planning artifacts；只有實際 commit 且 ready for execution 後才記 `planned`。
- 允許轉換：`planned → creator-in-progress → review-ready → reviewer-in-progress → approved|needs-rework`；`needs-rework → creator-in-progress`；`approved → creator-in-progress|publish-in-progress`；`publish-in-progress → pr-open`；`pr-open → needs-rework`。
- 採標準 Phase 4.5 contract alignment；Main Agent 確認 Reviewer approval、plan alignment 與 pre-commit checks 後進 Git 交付。Stable-library handling 明確 skip。
- PR base `dev`；歷史 Draft 交付已停於 human review，現依明確授權進行 bounded comment repair，不輪詢 merge。本授權不包含 `pr-open → merged`；merge 及後續須另有明確授權。

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/feasibility-validation/feasibility-validation.plan.md` | Plan-Creator | 執行契約 |
| Progression | `plan/feasibility-validation/feasibility-validation.step.md` | Planner；Main Agent 同步實際 phase | 交接進度 |
| Review log | `plan/feasibility-validation/feasibility-validation.review-log.md` | Plan-Reviewer、Reviewer 各自記錄 | 審查與回修證據；Plan-Creator 僅初始化或依明確授權 append creator-supplied Planner provenance，不寫 approval |
| Summary | `plan/feasibility-validation/feasibility-validation.summary.md` | Planner；Main Agent 同步交付事實 | 結案及下一交接 |
| Skill | `skills/feasibility-validation/SKILL.md` | Implementer | 行為契約 |
| Template | `skills/feasibility-validation/templates/experiment-readme.md` | Implementer | 紀錄模板 |
| Examples | `skills/feasibility-validation/examples.md` | Implementer | 正例與證據不足反例 |
| Canonical inventory | `artifacts/skills-inventory.jsonl` | Implementer | 既有 `scripts/build_skills_inventory.py` 的 generated output，完整覆蓋 canonical skill roots |

八個 exact paths（3 skill + 4 planning + 1 inventory）為 executable contract，超出範圍先修正計畫。`README.md`、`VERSION`、`.github/copilot-instructions.md` 均不改。

PR Lens 以真實 base/head diff 製作 local artifacts，置於 repo 外 `/private/tmp/feasibility-validation`，不屬 repo artifact set、不修改 repo config、不上傳資產。Graphify 若無 usable existing graph 則 targeted source fallback，不自動 build；Main Agent 記錄實際結果。

## Implementation Steps

1. **建立 skill 入口。** 採 `medium` complexity，metadata 與正文一致，明列觸發、五項判斷、完成條件、權限邊界及 local references。
2. **明定資訊不足的處理。** 先檢查來源與上下文；意圖及決策影響已知時，agent 主動設計缺少的假設、足以區分假設的最小輸入／操作／觀察方式，並在執行前固定成功、失敗與無法判定的可觀察判準，不因缺少現成技術判準而停止。只對仍未解決且會實質影響實驗的意圖、決策、權限或資源歧義阻擋執行並列出缺口；可恢復缺口採 `SOFT FAIL／INCOMPLETE`，繼續會造成誤導時採 `BLOCKED`。這些 skill 處理結果與實驗四狀態分開。
3. **保留六步流程。** 定義問題 → 設定判準 → 設計最小實驗 → 執行並保存證據 → 判讀結果 → 寫回紀錄。補明決策影響、依賴假設、投入上限與停止條件。
4. **保留 README 八段。** 驗證什麼、為什麼、成功與失敗判準、環境與前置條件、重現步驟、是否成功、結果與證據、結論與限制。
5. **明定完成語意。** 「是否成功」保留未執行／成功／失敗／無法判定，同段記錄驗證任務是否完成及原因。取得足以支持決策的證據，或清楚交代無法判定原因、缺少證據與決策限制，皆可完成本次驗證。
6. **保留重現規範。** 使用 `experiments/E001/README.md`，編號採 E001、E002，建立前確認未占用。集中必要程式、設定與可公開資料；排除建置產物、秘密及非公開資料。記錄環境版本、輸入、指令、日期與證據位置，標示模擬證據，分開觀察、推論及限制。

7. **同步 canonical inventory。** 僅在本輪獨立 Plan-Reviewer approval 後，由 Implementer 在指定 feature worktree 執行 `python scripts/build_skills_inventory.py` 再生 `artifacts/skills-inventory.jsonl`。現存 inventory 59 筆缺新 skill；既有外部 preview 60 筆僅新增該 skill，既有 59 筆 bytes 未變。不得修改 generator、tests 或三份 skill 檔案；不手寫 hash。

## Validation / Acceptance Checks

採 skill 行為情境審查，不新增 production tests 或實驗 CLI。Independent Plan-Reviewer 核對 canonical 11 sections、exact paths、角色邊界及四 planning artifacts 一致性；Reviewer 評估實際 skill 輸出。Main Agent 做 scope preview 與必要 Git 交付 checks，不自行宣告獨立 review 通過。

| 情境 | 預期行為 |
| --- | --- |
| 官方文件或原始碼足以回答 | 留下依據，不建立實驗。 |
| UTF-8 跨區塊解析 | 刻意在多位元組字元內切分區塊，分批送入並核對完整輸出；整檔讀取成功不足以支持假設。 |
| 假設被否定 | 有效證據足以支持排除實作選擇，驗證仍可完成。 |
| 環境或前置條件不足 | 記錄無法判定、缺少條件及決策限制，不誤判為假設失敗。 |
| 有限或模擬證據 | 結論限定於實際測試條件，不宣稱普遍保證。 |
| 意圖及決策已知，但缺少技術假設或判準 | 先查來源與上下文，主動設計假設及能區分結果的最小輸入／操作／觀察方式，執行前固定成功／失敗／無法判定判準。 |
| 仍有實質意圖、決策、權限或資源歧義 | 指出未解缺口，阻擋受影響的執行，不猜測意圖或越過邊界。 |
| 文件一致性 | 指令、模板與例子一致，驗證結果與 skill 處理狀態不混用。 |

Inventory 驗收：輸出可解析為 60 筆 JSONL，60 個唯一 canonical roots 完整對應既有 generator 探索的 top-level `skills/`；每筆僅含 `canonical_path`、`tree_hash`，排序、UTF-8 與尾端換行遵循現有序列化契約。Hash 依 skill-root-relative 路徑穩定排序，以 UTF-8 relative path + NUL + file bytes + NUL 的 SHA-256 stream 計算，保留 generator 的 symlink／junk 排除規則。新 `skills/feasibility-validation` 的 `tree_hash` 必須為 `9f4ed20178d4bde9e8c12721a2393737d4d4ad7a9b11e3fc2b3190b5fb4a7100`；其餘既有 59 筆各行 bytes 與原 inventory 完全一致。相同 skill tree 重跑 generator，輸出 bytes 必須完全相同（idempotent）；差異只能新增該一筆。

本輪順序：planning repair → independent Plan-Reviewer approval → Implementer regenerate → independent Reviewer verification → Main alignment／適用 checks → 已授權 commit／push／reply-resolve。Approval 前不得寫入 inventory；Plan-Creator 本輪只改三份 topic docs 並 append review-log，不執行 generator、tests、API、dispatch 或 Git mutations。

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

原 Git endpoint 為 topic commit → push → Draft PR（base `dev`）→ human review，已完成該交付及 human review；現由 Main Agent 在適用審查及 alignment 通過後完成已授權 comment fixes → commit → push → reply/resolve。無 stable promotion、merge、post-merge sync、release、tag 或 projection 授權；不安排延後發布。原 human review handoff 停點已完成；本輪修正交付後停止，不推論 merge 授權。

## Open Questions / Unresolved Items

無待選實作問題；optional analysis layer `INCOMPLETE` 仍為 nonblocking warning。當前八路徑契約修訂待獨立 Plan-Reviewer approval；inventory 尚未再生，當輪 Reviewer verification、alignment、commit／push／reply-resolve 未完成。舊 approvals、hashes、七檔 checks、Draft 交付與 11 threads resolved 快照均保留為歷史，不核准本輪修訂。最新外部觀察未回報 check runs；Codex 在先前 HEAD 的 Completed（2026-10-07T03:43:07.787356Z）僅為歷史 automation 狀態，不等於本輪 gate 通過。
