# E001 · Codex 重用 OpenSSH 控制 socket

## 驗證什麼

- 實驗編號為 E001。
- 以現行本機 Codex 權限，檢查兩個獨立回合能否重用同一條已驗證的 SSH 連線，並在手動關閉後停止。

## 為什麼

結果決定 Topic 2 是否以直接呼叫 OpenSSH 為候選方案。OpenSSH 原始碼可解釋連線選擇與中止路徑。實機仍需查明目前 Codex 權限是否可使用由使用者建立的 socket。

## 成功與失敗判準

- 成功需要兩輪均有 mux 重用診斷、相同 master、正確遠端身分及結束碼 `0`。手動關閉後，原命令需以非零結束，診斷顯示 socket 不可用、本機 `/usr/bin/false` 中止備援，且沒有遠端身分輸出。
- 前置條件成立且明確違反判準時為失敗。已嘗試但診斷不足以判斷時為無法判定。
- 只測一台主機、一個帳號、一種設定與驗證方式。上限為一次登入、兩輪唯讀查詢、一次關線後重試。

## 環境與前置條件

- 已核對本機 OpenSSH 10.2p1。驗證期間沿用 Codex 現行權限。
- 需要已授權測試主機、所選 SSH 設定入口、預期遠端身分，以及使用者在本機終端登入後建立的專用 socket。
- 使用者授權實際測試主機，使用預設 SSH 設定。終端顯示密碼提示及控制 socket 已存在，隨後 `-O check` 回報既有 master 正在運行。紀錄以代稱標示目標與 master。

## 重現步驟

1. 使用者依 [Topic 1 計畫](../../plan/ssh-feasibility/ssh-feasibility.plan.md#implementation-steps) 在終端登入，並用 `-O check` 驗證 master。
2. 在兩個 Codex 回合用相同別名、設定及 socket 執行 `hostname && id -un`，核對身分、master 與 mux 證據。
3. 使用者執行 `-O exit` 後確認 master 已關閉。Codex 以完全相同的唯讀呼叫重試一次。

## 是否成功

- 實驗狀態：**失敗**。首輪已觀察到現行 Codex 權限拒絕控制 socket 存取，跨回合重用的必要條件不成立。
- 本輪驗證任務完成：**是**。已取得足以判定現行權限下不可重用的負向證據。第二輪與手動關線後重試未執行。

## 結果與證據

| 已做的查核 | 觀察 |
| --- | --- |
| 本機版本與 `ssh -G` | 確認 OpenSSH 10.2p1 與 `ControlMaster=no`、`BatchMode=yes`、指定 socket、`ProxyCommand=/usr/bin/false` 的解析。 |
| 離線對照 | 使用空 SSH 設定、未建立的 socket 與 `.invalid` 示意別名。診斷顯示呼叫本機 `/usr/bin/false`、結束碼 `255`、標準輸出為空。 |
| 終端基準 | 使用者的 `-O check` 回報 master A 正在運行。Codex 可確認指定路徑是 socket。 |
| Codex 首輪 | 現行權限拒絕存取控制 socket。`-O check` 及唯讀 SSH 呼叫各以 `255` 結束。沒有 mux 成功、遠端身分輸出或另建 SSH 連線。診斷顯示備援路徑選用本機 `/usr/bin/false`。 |

## 結論與限制

現行 Codex 權限下，無法重用使用者終端建立的實際 SSH master。觀察範圍是此環境及權限設定。首輪沒有執行遠端查詢，因此未獨立核實遠端身分，也沒有手動關線後的實機證據。離線對照與首輪觀察均顯示本機備援路徑中止，支持既定的失敗即停止行為。

Topic 2 不應把此路徑視為現行權限下可用。若要評估不同連線方式或權限設定，另行規劃。這次沒有調整權限。終端 master 的清理已交回使用者。
