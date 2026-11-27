# ssh-ops 進度

| 階段 | 狀態 | 證據 |
| --- | --- | --- |
| 正式 worktree | 已確認 | `feat/andrew/ssh-ops-download` 從 `4058339` 建立。 |
| 正式計畫 | `planned` | 已落盤版本通過獨立 Plan-Reviewer，規劃基準提交為 `ae0aaf5`。 |
| Skill 審查 | `approved` | 獨立 Reviewer 核對正式 Skill、範例與採用範圍，並以測試設定確認 OpenSSH 有效參數。Copilot CLI 在本環境未提供，無 Copilot 意見可供分類。 |
| 本機驗證 | 已確認 | [採用紀錄](../../docs/feasibility-adoption.md) 列出靜態檢查、沙箱權限、成功與失敗的受控結果。 |
| 交付 | `publish-in-progress` | 已核對檔案界線與鎖定決策。依使用者授權提交、push 並開往 `dev` 的 Draft PR。 |
| 實機驗收 | 待授權輸入 | 原生載入、同一 master 的真實下載與實機失效案例待指定資料與當次授權。 |

原 `c86f05e` 工作樹為候選來源。採用決策與驗證範圍見 [正式計畫](ssh-ops.plan.md) 及 [採用紀錄](../../docs/feasibility-adoption.md)。
