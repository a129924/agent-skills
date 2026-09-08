## 目的與範圍

依已批准計畫修正 17 項確認問題，檢視全部 59 個 canonical Skills。此 PR 已 Ready for review，交由人工審查；不包含 merge、release 或 VERSION 調整。

## 主要修改

- 修正投影引擎自我改寫及 step completion 的缺漏／格式錯誤誤判，保留 CLI 契約並加入回歸測試。
- 收斂 59 個 discovery descriptions，區分獨立 review 與正式 workflow、可查明事實與必要提問，以及 draft／merge／release 權限。
- 修正矛盾範例、Pyright／TOML／Git 指令、PII 日誌及 TDD 完成條件；release 詳細流程改為按需讀取。
- 使用原有產生器同步 Codex、59 筆 inventory／mapping／provenance；保留 canonical ownership、有用 companion 知識、安全規則和跨模型需求。

## 驗證

- 94 個 canonical tests、64 個 projected runtime tests 通過（分開執行，避免同名測試模組衝突）。
- 實際 projected CLI 重跑：287 noop，零更新、零衝突。
- 59 個 frontmatter、來源雜湊、文件參考與 approved artifact manifest 範圍已檢查。
- 三模型各 12 個固定案例、medium effort、before／after；保留全部 72 筆觀察及 6 筆受影響案例重測。

| 預設決策標籤相符數 | Before | Final after |
| --- | --- | --- |
| Astra | 8/12 | 12/12 |
| Sol | 8/12 | 12/12 |
| Luna | 7/12 | 12/12 |

已逐筆檢查理由；標籤相符不是完整任務成功率。完整預載參考文件、每案例單次觀察，未測按需檢索、速度、token 效率或一般模型可靠性。Before Luna 的 PII case 雖標籤相符，理由另有錯誤前置 gate，已記錄。

## 保留與待辦

- 未刪除、改名或合併任何 Skill；未更動 `.github/skills`、VERSION 0.79.0 或既有 Git 歷史。
- 修改前保留可恢復 archive，位置與 SHA-256 見 topic summary；580 個 baseline manifest 檔案核驗通過。
- README 歷史索引缺漏及 GitHub compatibility drift 保留為範圍外追蹤。
- CI 結果與人工 review 以 PR 實際狀態為準；不宣稱 merge/release ready。

## 審查證據

見 `plan/skills-audit-and-progressive-disclosure/` 的 plan、findings、skill-dispositions、validation、原始 model-results、review-log 和 summary。獨立 review 核准範圍及限制均保留。

請人工確認：規則與範例保留是否符合使用情境、完成 gate 是否足夠嚴格，以及 draft／release 權限區分是否符合團隊流程。
