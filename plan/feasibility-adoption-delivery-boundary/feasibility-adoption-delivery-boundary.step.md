# feasibility-adoption-delivery-boundary Steps

## Workflow Stages

- [x] 使用者核准對話範圍並授權 feature worktree、語意 commit、push 與 Draft PR。
- [x] Feature branch 建立並核對起始 SHA 與工作樹狀態。
- [x] 獨立 Plan-Reviewer 複審 approved，Planner readiness PASS。
- [ ] Main Agent 提交獲准的四份 planning baseline，紀錄 commit SHA，移至 `planned`。
- [ ] Implementer 完成 canonical skill、inventory 與工具證據。
- [ ] Tester 完成必要檢查與案例覆蓋紀錄。
- [ ] 獨立 skill verdict 通過，Planner 提供 boundedness evidence，Main Agent 完成 Phase 4.5 checkpoint 與路由。
- [ ] 語意 commit、push、Draft PR 及 human review 交接。

## Actionable Steps

| ID | owner | 行動與完成條件 |
| --- | --- | --- |
| P1 | Plan-Reviewer | 核對 scope、write-set、驗收與 Git 停點，記錄明示 verdict。 |
| P2 | Planner | 核對 P1 verdict、未解項與執行分支，登錄 readiness。 |
| P3 | Main Agent | 核對 P1 與 P2，提交獲准的四份 planning baseline，登錄 commit SHA 與 `planned`。 |
| I1 | Implementer | 於 `planned` 後修改三份 canonical skill 檔與 inventory，依 plan 取得本機工具證據，交針對實際差異的結果。 |
| T1 | Tester | 檢查範圍、規格、連結、案例與生成物，記錄實際命令、結果、限制。 |
| R1 | Reviewer | 使用 agent-skill-reviewer 評估實際 draft 與 T1 證據，記錄獨立 verdict。 |
| A1 | Planner | 提供 scope、實際差異、staged 候選及證據限制的 boundedness evidence。 |
| A2 | Main Agent | 執行 Phase 4.5 checkpoint，未通過退回 `creator-in-progress`，通過進 `publish-in-progress`。 |
| D1 | Main Agent | 檢查精確 staged set 與 Git 授權，commit、push、建立 Draft PR，登錄 head 及 human review 停點。 |

## Handoff / Gate Notes

Plan-Reviewer 複審 approved，Planner readiness PASS，下一步為 P3 提交規劃基線。P1 如有 required fixes 交 Plan-Creator 修訂。P3 已提交 planning baseline 才能開始 I1。R1 若需回修由 Implementer 處理，Tester 補驗受影響項，Reviewer 核定。A2 由 Main Agent 判斷與路由。完成 Draft PR 後停止於 human review。Summary 記錄交付與下一責任人。
