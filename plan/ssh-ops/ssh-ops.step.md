# ssh-ops 進度

| 階段 | 狀態 | 證據 |
| --- | --- | --- |
| 正式 worktree | 已確認 | `feat/andrew/ssh-ops-download` 從 `4058339` 建立。 |
| 正式計畫 | `planned` | 已落盤版本通過獨立 Plan-Reviewer，規劃基準提交為 `ae0aaf5`。 |
| Skill 審查 | `approved` | 獨立 Reviewer 核對正式 Skill、範例與採用範圍，並以測試設定確認 OpenSSH 有效參數。Copilot CLI 在本環境未提供，無 Copilot 意見可供分類。 |
| 本機驗證 | 已確認 | [採用紀錄](../../docs/feasibility-adoption.md) 列出靜態檢查、沙箱權限、成功與失敗的受控結果。 |
| 交付 | `pr-open` | 正式 Skill 提交為 `e9513ed`。已 push 並確認 [Draft PR #133](https://github.com/a129924/agent-skills/pull/133) 開往 `dev`，移交使用者人工審閱。 |
| 實機驗收 | 待授權輸入 | 原生載入、同一 master 的真實下載與實機失效案例待指定資料與當次授權。 |

原 `c86f05e` 工作樹為候選來源。採用決策與驗證範圍見 [正式計畫](ssh-ops.plan.md) 及 [採用紀錄](../../docs/feasibility-adoption.md)。
