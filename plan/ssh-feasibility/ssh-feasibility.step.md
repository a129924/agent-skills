# SSH 控制 socket 可行性驗證進度

## Workflow Stages

| 階段 | 狀態 | 證據與下一步 |
| --- | --- | --- |
| 建立隔離 worktree | 已完成 | 分支 `docs/andrew/ssh-feasibility`，起點 `c391870430a155480bb3b66238e9bcd7d36a323b`。 |
| Phase 1 規劃與審查 | 已完成 | 獨立 Plan-Reviewer 回傳 `approved`，無阻擋問題。規劃基準已提交為 `fc218ce`，狀態為 `planned`。 |
| 實驗與獨立證據審查 | 未執行 | 待已授權測試主機和使用者登入。靜態依據已核對本機 OpenSSH 10.2p1、`ssh -G` 與上游實作。 |
| 交接 | 尚未開始 | 已列出執行阻擋與可用證據。完成實機驗證及獨立審查後，再依授權 push 並開 Draft PR。 |

## Actionable Steps

1. 審查並固化本 worktree 的 topic plan 及進度基準。
2. 在已授權主機執行兩輪 socket 重用及手動關線後的重試。把遮蔽結果放在 `experiments/E001/README.md`。
3. 核對實驗結果及檔案邊界，記錄本題驗證是否完成。

## Handoff / Gate Notes

- 使用者已授權從 feature worktree 執行本題，完成查核且無重大阻擋時提交、push 並開 Draft PR 給人審閱。
- 實驗狀態與 review 結果分開登錄。Topic 2 待 Topic 1 驗證完成後另行處理。
