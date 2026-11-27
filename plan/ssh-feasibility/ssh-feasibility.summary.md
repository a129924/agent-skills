# SSH 控制 socket 可行性驗證交接

## current state

規劃基準已於隔離 worktree 的 `docs/andrew/ssh-feasibility` 提交。Topic 1 實機驗證等待已授權測試主機，實驗狀態仍為未執行。

## completed

- 獨立 Plan-Reviewer 對 topic plan 回傳 `approved`，無阻擋。
- 已核對 OpenSSH 10.2p1、參數解析與未建立 socket 的離線行為。遮蔽證據見 [E001](../../experiments/E001/README.md)。

## not completed

- 跨兩輪重用及手動關線後重試的實機驗證。
- 實機證據獨立審查、push 與 Draft PR。Topic 2 尚未開始。

## required follow-up

取得已授權的測試別名、設定入口及預期遠端身分。由使用者在本機終端登入並確認 master。完成實測後按證據更新 E001 及本摘要。

## next handoff

- **next actor**　使用者，接續由 Tester 執行計畫。
- **next step**　確認測試目標與設定入口，在自己的終端機完成登入。密碼及金鑰解鎖資訊留在終端。
