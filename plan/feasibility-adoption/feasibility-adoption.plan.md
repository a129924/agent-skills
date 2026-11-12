# feasibility-adoption：選擇性正式採用與盤點計畫

Analysis-layer routing: INCOMPLETE（nonblocking semantic warning）。Optional analysis/feasibility-adoption/requirements.md 與 analysis/feasibility-adoption/technical-spec.md 均不存在；本題不建立 analysis。需求基線為使用者已確認的能力／決策採用需求、經獨立對話審查修正的完整計畫及 2026-11-12 執行授權。對話審查 PASS 不等於本次落盤 artifacts 已通過 repository plan gate。

## Goal / Outcome

**Goal：**新增兩個可獨立使用、單一職責的 skills，處理可行性驗證成果選擇性正式採用，以及尋找尚未採用的能力／決策。交付六份 canonical skill 檔案、generated inventory、四份 planning artifacts 及 repo 外輔助圖／證據。經獨立審查與必要檢查後完成 topic commit → push → Draft PR（base dev）→ human review。

| Skill | 單一職責 | Complexity |
| --- | --- | --- |
| feasibility-adoption | 辨識必要能力、比較採用方案，在原任務已有授權時沿原流程完成 bounded implementation 與驗證 | high |
| feasibility-adoption-audit | 唯讀比對驗證成果、採用紀錄及正式程式，提出有證據的採用盤點 | medium |

兩個 skills 的必要身分、責任及授權限制留在 entrypoint；案例、模板作為本地 companion，支援獨立安裝，不依賴另一個 skill 的隱藏上下文。

## Scope

### In-Scope

- 新增兩個 skills，包含觸發／排除情境、必要輸入、處理步驟、正反例、完成條件、Validation、Failure Handling 與 local references。
- 獨立採用紀錄及盤點模板，涵蓋部分採用、直接重用、抽取調整、重寫、排除、不確定及舊資料辨識。
- 以既有 scripts/build_skills_inventory.py 再生唯一列定的 generated artifact。
- 使用 Archify、PR Lens、Graphify 作本 topic 理解及交付輔助，產物限 repo 外。
- 四份 planning artifacts 與使用者明確授權的 feature-worktree 實現、topic commit、push、Draft PR 及 human-review handoff。

### Out-Of-Scope

不修改 repo 通用 agent-skill-implementation skill／契約，不實際採用其他專案的實驗成果；不修改 feasibility-validation、治理、共用 workflow、creator／reviewer／template 契約、工具設定或平台相容面。不新增 runtime orchestration、必經 phase、approval、runtime/tool 依賴或 tracked 圖資。不包含 stable promotion、merge、post-merge sync、tag、release、上傳圖資或其他發布。

## Locked Decisions

1. **驗證與採用分離。**feasibility-validation 只記錄驗證什麼、證據、是否成功及本輪驗證任務完成否；其四狀態與完成判斷均不能證明已採用。不新增 feasibility 的必填採用責任，不修改其 skill、八段 README 模板或 examples。
2. **定位正式來源。**src-implementation 是正式程式泛稱，依目標專案規範、實際用途與接入點定位，不硬編碼目錄；不能僅看路徑名稱。
3. **按能力／決策選擇。**先辨識必要部分及採用方案，再確認依賴閉包。必要依賴須對應既有正式能力、此次必要實作或明確缺口；依賴某實驗不代表必須搬入整個實驗。
4. **允許有依據的重用。**不得因實驗成功而整套搬入正式來源；按所選能力及必要依賴採用。必要程式與有價值的測試可重用、抽取調整或重寫；僅供實驗的 harness、模擬依賴與示範入口，無正式用途時排除。按正式契約確認所需介面、錯誤處理、生命週期及驗證；重寫仍追溯原能力／決策。
5. **沿用既有授權。**原任務已授權實作時，沿原實作與審查流程完成 bounded implementation 及驗證，不重問相同授權。只有驗證授權時，交付具體方案及受限範圍，不修改正式程式。實驗成功不產生實作授權；影響鎖定決策則回原變更流程。
6. **紀錄落點。**優先沿用專案既有採用紀錄落點；沒有既有落點時，預設 docs/feasibility-adoption.md。依當前模式與既有寫入授權建立／更新；不能寫入時交付相同結構的具體內容與限制。紀錄不放入實驗 README。此為未來 skill 使用契約，不授權本 topic 建立該專案紀錄。
7. **最小追溯紀錄。**每個能力／決策記錄識別、來源及版本／快照、選定與排除範圍、必要依賴、採用方式、判定及理由、正式程式與接入位置、驗證證據、剩餘缺口及觀察日期。採用方式與採用程度分開；計畫採用不能冒充完成，部分採用須明列完成及剩餘部分。保留歷次依據，不改寫原實驗結果。
8. **舊資料。**由既有問題、結論、程式及決策辨識能力／決策，本次補建識別須明標，不冒充歷史紀錄。相同行為或等效能力，不能無證據宣稱源自某實驗。
9. **唯讀盤點。**先宣告來源集合、正式來源／接入範圍、版本及排除範圍，再逐項列證據分類：已採用、部分採用、未採用、已排除、不確定。重寫須比對行為、決策與接入證據，不僅比檔名或程式相似度。缺 tracker、名稱相似、檔案存在、實驗成功都不足以判已採用或未採用；未採用須有明確待辦／未落地證據，或可界定且足夠的正式範圍查核。範圍不足、對應不明或證據衝突標不確定。盤點不自動補實作或改 tracker。
10. **本題交付意圖。**Skills 先達 review-ready 再由獨立 Reviewer 審查；不涉及 stable-library promotion，不修改 README.md、VERSION、release notes，也不安排延後 release。使用者已授權審查通過後 topic commit → push → Draft PR → human review。
11. **Path roles。**skills/ 是 canonical authoring source；對使用者展示執行入口時採 .<platform>/skills/<skill-name>/，不硬選 .codex 或 .github。Bootstrap fallback 必須依 creator/template 契約標明；本題不進行平台 projection。

## Boundaries / Exclusions

**Non-Goal：**不以本 topic 改寫其他 skill／共用契約，不設立新的採用必經流程，也不把工具圖解當作 correctness approval。

所有 repository 寫入僅限 /Users/andrew/code/python/agent-skills.worktrees/agent-20261112-feasibility-adoption；不得在 /Users/andrew/code/python/agent-skills 的 dev worktree 實作。超出 Artifact Paths 先修正計畫，不以順手整理擴張 write-set。

Plan-Creator 落盤及修訂 planning contract；Implementer 僅負責列定實作與工具產物；獨立 Plan-Reviewer／Reviewer 各自審查並記錄自己的 verdict；Planner 處理 readiness／最終 boundedness；Main Agent 管理 branch、routing、Phase 4.5 alignment 及已授權 Git 交付。不得自我核准或模擬獨立角色。普通回修使用既有 needs-rework loop，本題不預設 correction artifacts 或新增 gate。

## Status / Allowed Transitions

**Current（2026-11-12，Draft PR 交付後）：**狀態為 pr-open。Planning baseline 94c161f310ee0a6bf63f34808f07dc6c9451cdda；實作 commit a5abd634b61133e4f108d75dffd8d626ebe13799 已 push。Main Agent 透過 GitHub connector 建立 [Draft PR #129](https://github.com/a129924/agent-skills/pull/129)，base dev（4c7e6af）、head a5abd63、isDraft=true。獨立 Plan-Reviewer／implementation Reviewer approved，Planner boundedness PASS；Archify passed、Graphify 合規 source fallback、PR Lens validate／render passed。Human review pending；本題不宣稱 merge、release 或 topic merge completion。PR Lens 固定映射 base 4c7e6af…head a5abd63 的真實 11-file diff；後續只同步 planning 交付紀錄，不冒稱圖已涵蓋後續文件 commit。

**歷史 planning 落盤時點：**當時 Phase 1 四份 artifacts 已落盤，等待 repository Plan-Reviewer，尚無 planning commit；此段只保存當時狀態，不描述目前進度。對話 PASS 與 human approval 未代替後續已完成的獨立檔案審查。

- 2026-11-12 使用者核准完整計畫並授權 feature-worktree 實現 → topic commit → push → Draft PR（base dev）→ human review。此 bounded authorization 已涵蓋 STOP POINT 1，不重問同一授權，仍須完成審查、alignment、scope 與必要 checks。
- 指定 worktree 已由 Main Agent 建立，branch 為 feat/andrew/feasibility-adoption；本輪唯讀確認 initial HEAD 4c7e6afc2697c019ba12e6c74890c01923db6810，落盤前 clean。
- 分支符合 git-branch-naming 的 <type>/<username>/<short-description>；feat、andrew 與 feasibility-adoption 對應本題新增能力及既有 namespace。建立命令 git switch -c feat/andrew/feasibility-adoption 僅為歷史計畫，現有 branch 已建，不重跑。
- 本地及已知 remote-tracking 的無衝突結論僅為既有觀察；未 fetch，不宣稱實際遠端名稱已查證。Push 前 Main Agent 檢查目標與必要衝突。
- 獨立 repository plan review／Planner readiness 完成並由 Main Agent 提交 planning baseline 後，才記 planned 並進 creator-in-progress。實作前確認 semantic branch、worktree 及無無關變更。
- 本題適用 canonical creator → reviewer → publish 路徑，但授權終點為 pr-open 的 Draft PR／human-review handoff，不延伸 merge。

允許本題使用的 canonical transitions：
planned → creator-in-progress → review-ready → reviewer-in-progress；
reviewer-in-progress → approved 或 needs-rework；
needs-rework → creator-in-progress；
approved → creator-in-progress 或 publish-in-progress；
publish-in-progress → pr-open；
pr-open → needs-rework（已有授權內的 bounded repair）。
pr-open → merged 為 repo canonical transition，但本次無 merge 授權；不執行 merged／released 或其後動作。

採標準 Phase 4.5 contract alignment；Reviewer approved 不免除 Planner／Main alignment。無 workflow review round cap；Archify 的兩種停止規則僅屬工具契約。Draft PR 交 human review 後停止，不背景輪詢 merge。Summary 是交付／close handoff truth；step 只是進度，不以勾選宣稱 topic 已完成。

## Artifact Paths

下列分類僅描述本 topic；不代表未來 skill 使用者專案的 write-set。所有 tracked paths 均相對指定 feature worktree。

### Written：新增 tracked 檔案

| Artifact | Exact path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | plan/feasibility-adoption/feasibility-adoption.plan.md | Plan-Creator | 執行契約 |
| Progression | plan/feasibility-adoption/feasibility-adoption.step.md | Planner；Main Agent 同步實際 phase | 多角色交接進度 |
| Review log | plan/feasibility-adoption/feasibility-adoption.review-log.md | 獨立 Plan-Reviewer／Reviewer；Plan-Creator 僅初始化 | Verdict／回修證據 |
| Summary | plan/feasibility-adoption/feasibility-adoption.summary.md | Planner；Main Agent 同步交付事實 | 結果及 human handoff truth |
| Adoption skill | skills/feasibility-adoption/SKILL.md | Implementer | 採用行為與授權契約 |
| Adoption examples | skills/feasibility-adoption/examples.md | Implementer | 分支／誤用案例 |
| Adoption template | skills/feasibility-adoption/templates/adoption-record.md | Implementer | 獨立採用紀錄 |
| Audit skill | skills/feasibility-adoption-audit/SKILL.md | Implementer | 唯讀盤點契約 |
| Audit examples | skills/feasibility-adoption-audit/examples.md | Implementer | 分類及舊資料案例 |
| Audit template | skills/feasibility-adoption-audit/templates/adoption-audit.md | Implementer | 範圍、證據、分類及缺口報告 |

### Modify：唯一既有 tracked 檔案

| Artifact | Exact path | Owner | Role |
| --- | --- | --- | --- |
| Canonical inventory | artifacts/skills-inventory.jsonl | Implementer | 以既有 generator 再生；不手寫 hash |

共 11 個 exact tracked paths。Written 檔案建立後回修仍限同一清單。README.md、VERSION、.github/copilot-instructions.md 均不改；無 stable-library metadata 或 release timing 待決。

### ReadOnly

AGENTS.md、docs/repo-positioning.md、plan/agent-handoff-workflow.md、plan/topic-plan-contract.md；本題適用的 creator、reviewer、template、planning、branch skills 及必要 local references；skills/feasibility-validation/SKILL.md、skills/feasibility-validation/examples.md、skills/feasibility-validation/templates/experiment-readme.md；scripts/build_skills_inventory.py、相關既有測試與驗證設定；Git 狀態及 bounded diff；外部 Archify、PR Lens、Graphify skill 套件與 runtime。不修改 generator、tests、工具套件、repo config、hooks 或 projection。

### Written：repo 外輔助產物

由 Implementer 建立，Main Agent 在交付摘要引用實際輸出：
- /private/tmp/feasibility-adoption/archify/workflow.json：workflow candidate。
- /private/tmp/feasibility-adoption/archify/workflow.html：deliver 的受信 HTML。
- 同 archify/ 目錄內保存 validate／deliver JSON receipts，以及 visual-check 實際命名的四張 PNG、contact sheet 與 JSON receipt；輸出名稱由實際 receipt 確認，不捏造檔案。
- /private/tmp/feasibility-adoption/pr-lens/graph.json：真實變更的概念圖。
- /private/tmp/feasibility-adoption/pr-lens/diff.patch、/private/tmp/feasibility-adoption/pr-lens/provenance.json：bounded diff、真實 base/head 或工作樹快照及檔案範圍。
- /private/tmp/feasibility-adoption/pr-lens/rendered/：CLI manifest 及實際產生的 SVG。
- /private/tmp/feasibility-adoption/tool-status.md：命令、版本、來源、退出狀態、人工視覺觀察、錯誤、fallback 及未完成項目。

以上外部產物不加入 Git；工具可在自己的同目錄建立必要 private snapshots。Graphify 本題不建立 graph、cache 或 metadata。

### Deleted

無 repository tracked 檔案刪除；工具僅管理上述 scratch 範圍內自己的暫存或過期 sidecars。

## Implementation Steps

1. **建立兩個 skill entrypoints。**依 agent-skill-creator／template／folder contract 撰寫六份新 skill 檔案，採 high／medium complexity 並選擇符合實際行為的 risk_profile。保留觸發、必要授權與完成語意於 entrypoint，列明 companion／template 的角色。不得靠 YAML 宣稱 runtime routing。
2. **完成 adoption 行為。**先讀原任務、鎖定決策、可得證據與正式程式，辨識必要能力／決策，提出有依據的重用／調整／重寫／排除方案及依賴閉包。把成功條件、實際接入及驗證證據與待辦分開；依現有授權沿原實作流程完成，不藉實驗成功擴張權限。
3. **完成獨立紀錄。**模板包含最小追溯欄位、部分採用及剩餘項目；支援既有落點及明確預設，不能寫入則交付相同結構內容。保留歷史，不複製整份實驗紀錄、不把採用狀態塞回 feasibility。
4. **完成 audit 行為。**先界定範圍、來源及版本，以能力／決策逐項比對 adoption records、正式來源及接入證據。舊資料補建識別有標示；推論與事實分開，缺證據標不確定。僅唯讀盤點並輸出報告，不自動更新 tracker 或實作。
5. **撰寫 worked examples。**覆蓋 TestCase 的部分採用、依賴閉包、有價值測試重用、重寫、等效能力、排除、不確定、舊資料、權限不足及實驗四狀態分離；案例明標示意，不捏造實際執行成果。
6. **同步 canonical inventory。**使用既有 python scripts/build_skills_inventory.py 再生 artifacts/skills-inventory.jsonl，確認僅新增兩個 roots、既有 roots 記錄不變及重跑 byte-idempotence；不修改 generator 或 tests。
7. **Graphify bounded navigation。**依使用者指定的 /Users/andrew/.agents/skills/graphify/SKILL.md，僅 existing usable graph，先查來源版本與位置。每次 CLI 包含 GRAPHIFY_NO_AUTO_REFRESH=1，包括 version/help。適用時用 /Users/andrew/.local/bin/graphify bounded query，budget 1500，重大關係回原始來源確認。初始探索未找到 graph.json，不能宣稱已有 usable graph；不存在／不適用或 runtime 失敗，記具體限制並用 targeted source fallback。本題不是明確 build 請求，不 extract、refresh、安裝或整合。
8. **PR Lens change map。**依 /Users/andrew/.agents/skills/pr-lens/SKILL.md，僅用 /Users/andrew/.local/share/pr-lens-runtime/bin/pr-lens 0.11.0。先取得真實 base/head diff 或包含新增檔案的 bounded diff，保存實際 provenance；工作樹 diff 不冒稱 committed head，未追蹤新檔須納入明確 snapshot。讀 references/example.graph.json 及 references/graph-document.md 後製作外部 graph，保留必要 unchanged neighbors、file refs，validate 再 render 並讀 manifest。當前未找到 pr-lens.yml；scratch render 用 --no-config。若實際 PR 已有既存 overlay，先唯讀查證再按 skill 使用，不能新建／改 config。不執行 uploads、provider/API、canvas、auth、server、PR 發布或自動 integration；無可用版本則記實際錯誤，不 install／upgrade。
9. **Archify workflow showcase。**依 /Users/andrew/.codex/skills/archify/SKILL.md 及 references/delivery-contract.md，執行時先讀 schemas/workflow.schema.json、schemas/common.schema.json 及 examples/agent-tool-call.workflow.json，下一工具動作直接寫第一版 candidate；不先讀 renderer internals。使用新 IDs／本題內容，meta.quality_profile="showcase"，主線最多 12 個 primary nodes，呈現驗證／採用／盤點責任及既有授權分支，不畫成新增必經流程。正文繁中，省略 meta.locale 並明示固定 Viewer UI 與 html lang 回退英文；預設 static／classic、無動畫，不開 preview server、不 --open。每次改 candidate 後 validate；最終要求 9 checks、0 errors、0 warnings，使用 deliver 凍結及交付 HTML／SHA-256 receipt。隨後對精確交付 HTML 執行 visual-check，不帶 --repo-root，取得四種 viewport containment 及實際截圖；閱讀 images／contact sheet，單獨記 visual-review 結果，不能把 visualReview:pending 當人工通過。
10. **遵守工具修正與限制。**Archify 自動驗證依 SKILL：客觀錯誤數持續創新低可繼續，連續兩輪未改善最佳錯誤數才停止並回報 diagnostics。視覺審查依 delivery-contract 最多兩輪，correction_rounds=0|1|2；若改 candidate，重新 validate／deliver，對新 HTML 重新蒐集及檢視證據。工具非零 exit、skipped、runtime 不可用或 fallback 均實報，不增依賴、不修改 tool/config。工具未完成交付保留為未完成，不能冒稱整個 topic 完成；Graphify 在無 usable graph 時記錄合規 source fallback 可滿足本題導航分支。

## Validation / Acceptance Checks

### TestCase

| 情境 | 預期行為 |
| --- | --- |
| 實驗成功但正式來源無接入 | 不標已採用，按範圍證據判未採用或不確定 |
| 同一實驗只採部分能力 | 按能力／決策拆分，追溯完成、剩餘及排除部分 |
| 選定能力依賴其他實驗 | 確認必要依賴閉包，不整套搬入 |
| 有價值的測試可重用 | 允許重用／調整／重寫，排除無正式用途的實驗構件 |
| 正式版本完全重寫 | 追溯原能力／決策、行為與接入，不要求程式相似 |
| 正式程式已有等效能力 | 可滿足依賴，但無證據不宣稱源自特定實驗 |
| 只有 harness、示範或未接入檔案 | 不認定已正式採用 |
| 舊資料無 tracker、名稱相似或證據衝突 | 明標補建識別、缺口與不確定，不猜歷史 |
| 原任務已授權實作／只有驗證授權 | 前者完成 bounded implementation，後者交具體方案及限制 |
| 假設失敗／無法判定，但驗證任務完成 | 保留原實驗結果，不推導採用進度 |
| 無寫入權限或模式不允許 | 不寫採用紀錄，交相同結構內容及限制 |
| Inventory 再生 | 完整覆蓋 canonical roots，只新增兩 roots，既有記錄不變、序列化及 hash 契約不變、重跑 bytes 一致 |
| Graphify 無 usable graph | 記錄 targeted-source fallback，不 build／refresh |
| PR Lens 缺真實 diff 或 runtime 失敗 | 不偽造 map／provenance，記未完成工具交付 |
| Archify 自動通過但未檢視實際畫面 | 不宣稱 visual_review:passed |
| Archify 交付／視覺修正 | 分別遵守兩種修正規則，candidate 改動使舊 receipt／視覺證據失效 |
| 任一必要工具交付失敗 | 留下具體錯誤／限制與未完成事項，不冒稱整題完成 |

採文件結構／metadata、local links、模板與正文一致性、範圍 diff、行為情境審查、inventory contract 及適用 pre-commit checks；不新增 production tests 或測試框架。Supported Astra、Sol、Luna 所需的明確語意與案例不能僅為縮短文字刪除，不宣稱 model/speed 改善或未執行的 runtime model evaluation。

Archify 自動驗收須 9/9 showcase、0 errors、0 warnings，不能拿四項 basic checks 代替。Visual-check 量測 1440×900、1600×1000、1920×1080、2048×1320，均須 scrollWidth <= innerWidth、scrollHeight <= innerHeight，並檢視最小及最大 viewport 的 light/dark 截圖，確認文字、路徑、節點與整體平衡。不藏 overflow、不裁切、不縮小字型偽造通過。Receipt 的 pending 與人工 visual_review 分開回報；無 image reader 則 skipped，不能稱完成視覺交付。

Independent Plan-Reviewer 檢查 canonical 11 sections、exact paths、九欄位、狀態真實性、角色與四檔一致性；Reviewer 依 agent-skill-reviewer 審實際 skill folders，並核對必要工具證據及 inventory。工具圖解不是 correctness approval。Main Agent 確認 reviewed snapshot、Phase 4.5 alignment、scope 和必要 checks 後才交付已授權 Draft PR。

## Reviewer Handoff

~~~json
{
  "verdict": "approved|needs-rework",
  "blocking_issues": [],
  "copilot_feedback_triage": {
    "ADDRESS": [],
    "DISCUSS": [],
    "SKIP": []
  }
}
~~~

## Post-merge / release actions

本次授權終點為 topic commit → push → Draft PR（base dev）→ human review。既有授權滿足相同 bounded Git 交付的 STOP POINT 1；不要重複要求批准，但不得略過必要審查與 checks。Draft PR 與當前交付證據記入 summary 後停止交 human，不背景輪詢 merge。

無 stable-library promotion、README／VERSION／release-note 更新、延後 release、merge、post-merge sync、tag 或 release 授權；不執行 Phase 9／10。將來若明確授權 merge 後續，另按當時狀態與原契約處理，本計畫不預先核准。

## Open Questions / Unresolved Items

無待使用者選擇的需求／偏好。Optional analysis layer INCOMPLETE 是 nonblocking warning，不建立 analysis。

**歷史 planning 落盤時點：**repository plan review、Planner readiness、planning commit、skills／inventory、implementation review 及 Git 交付當時均未完成；不是目前未完成清單。

**目前未完成（2026-11-12）：**本次三份 planning 交付紀錄的 commit／push 由 Main Agent 接續處理，human review 尚待使用者進行。技能、inventory、獨立 reviews、Phase 4.5 boundedness、實作 commit／push、Draft PR 及三項輔助工具分支已有實證。PR Lens graph／provenance／diff.patch／manifest 與 SVG 位於 /private/tmp/feasibility-adoption/pr-lens/，固定 head a5abd63，不包含其後 planning-only delivery 記錄更新；工具詳見 tool-status.md。Graphify 無 usable graph 的 source fallback 是計畫允許分支，不冒稱建立 graph。交 human review 後停止，不輪詢 merge，不擴張 locked scope。
