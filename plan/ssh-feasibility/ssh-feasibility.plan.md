# SSH 控制 socket 可行性驗證

分析層提醒：`analysis/ssh-feasibility/requirements.md` 與 `analysis/ssh-feasibility/technical-spec.md` 均不存在。這兩份分析文件是選用輸入，本題以使用者確認的實驗需求為依據。

## Goal / Outcome

確認本機 Codex 能否以現行權限，在兩個獨立對話回合重用同一條由使用者登入的 OpenSSH 連線。使用者手動關線後，用同一命令重試，確認呼叫失敗且未另建 SSH 連線。將遮蔽後的證據與適用限制交給使用者，作為 Topic 2 評估直接使用 OpenSSH 的依據。

## Scope

- **In-Scope**　單一已授權主機、帳號、既有設定入口及驗證方式。一次登入、兩個 Codex 回合各執行一次唯讀查詢、手動關閉後重試一次。保存八段實驗紀錄與流程交接文件。
- **Out-Of-Scope**　Topic 2 的 Skill 檔案、完整設定與驗證矩陣、權限調整、遠端資料變更、stable-library 更新、merge、release 及圖資上傳。
- **Non-Goal**　封裝 Skill 或 MCP、代管憑證、驗證自動重連或對其他環境做推論。

## Locked Decisions

- 沿用本機 OpenSSH、現行 Codex 權限和既有主機驗證。使用者在自己的終端機登入。每次指令使用同一組主機別名、設定來源與專用 socket。
- 設定 `ControlPersist=15m`。本題測試 `-O exit` 手動關線。透過 `ProxyCommand=/usr/bin/false` 中止無法重用時的新 SSH 傳輸。
- 執行分支為 `docs/andrew/ssh-feasibility`，基準為 `dev`。按本題最新授權先建立隔離 worktree，然後在其中落盤與審查規劃基準。進入實驗前須有已審查的基準與已授權測試主機。
- 本題為非 stable-library 文件及驗證工作。完成必要檢查且無重大阻擋時，使用者已授權 topic commit、push 及對 `dev` 的 Draft PR，交給 human review 後停止。

## Boundaries / Exclusions

- **ReadOnly**　既有 SSH 設定、OpenSSH 原始碼、repo 工作流程、實驗模板、相鄰專案的實驗範例及適用的既有圖或 diff。
- **Modify**　僅更新本題列定的新文件。既有追蹤檔案、根目錄 `README.md`、`VERSION`、`.github/copilot-instructions.md` 與平台投影均為唯讀。
- **Deleted**　無既有檔案刪除。master 關閉時由 OpenSSH 清理本次專用的 `/tmp/codex-ssh.*/control`。
- 權限拒絕、登入缺口及診斷不足按已確認的前置條件與證據分類。未有已授權主機時停在實驗前。

## Status / Allowed Transitions

進度以同目錄的 step 檔為準。獨立 Plan-Reviewer 查核 repo 內的計畫。通過後提交規劃基準並標記 `planned`。進入實驗後依 `creator-in-progress` → `review-ready` → `reviewer-in-progress` → `approved` 或 `needs-rework`。回修回到 `creator-in-progress`。獨立驗證審查及 Phase 4.5 範圍核對完成後，依已授權的發佈條件進入 `publish-in-progress` → `pr-open`，在 Draft PR 停下交付人工審閱。若有重大阻擋，記錄事實及下一個可驗證的步驟。

## Artifact Paths

| 檔案 | Owner | 用途 |
| --- | --- | --- |
| `plan/ssh-feasibility/ssh-feasibility.plan.md` | Plan-Creator | Phase 1 執行契約 |
| `plan/ssh-feasibility/ssh-feasibility.step.md` | Plan-Creator 建立，Main Agent 按證據更新 | 多次角色交接與現況 |
| `plan/ssh-feasibility/ssh-feasibility.review-log.md` | 獨立 Plan-Reviewer 或 Reviewer | 審查回饋控制路由、回修或複審時建立 |
| `plan/ssh-feasibility/ssh-feasibility.summary.md` | Main Agent | 驗證結果及人工交接前建立 |
| `experiments/E001/README.md` | Implementer 記錄，Tester 提供證據 | 八段實驗紀錄。落盤前重查編號，若占用先對齊 plan |

本地圖資位於 `/private/tmp/ssh-feasibility/`。Archify 的 `archify/workflow.json`、`archify/workflow.html` 與檢查證據以 showcase 驗證及人工檢視交付。Floorplan 在 `blueprint/` 建立本機草案與 HTML。Show-me 圖在對話中交付。Graphify 有可用且版本相符的圖才查詢，否則定向查來源。PR Lens 以實際 diff 為輸入，輸出留在 `pr-lens/`。

## Implementation Steps

1. 用 `skills/feasibility-validation/templates/experiment-readme.md` 建立實驗紀錄，固定判準並記錄測試環境與現行權限。
2. 使用者以已授權帳號在終端機登入。使用預設 SSH 設定時令 `ssh_cfg=()`，獨立入口則令 `ssh_cfg=(-F "/path/to/approved.sshconfig")`。建立僅本人可存取的專用 socket。

   ```bash
   ssh_dir=$(mktemp -d /tmp/codex-ssh.XXXXXXXX) &&
     sock="$ssh_dir/control" &&
     ssh "${ssh_cfg[@]}" -S "$sock" -M -N -f -o ControlPersist=15m "$host" &&
     ssh "${ssh_cfg[@]}" -S "$sock" -O check "$host"
   ```

3. 在兩個獨立 Codex 回合以同一參數執行下列命令，每輪查驗 master 身分。使用者以同一設定與 socket 執行 `-O exit`，確認 `-O check` 失敗後，Codex 重試同一命令一次。

   ```bash
   ssh "${ssh_cfg[@]}" -v -S "$sock" -T \
     -o ControlMaster=no -o BatchMode=yes \
     -o ProxyCommand=/usr/bin/false "$host" 'hostname && id -un'
   ```

4. 在實驗紀錄內保存版本、結束碼、身分比對及必要診斷。將主機、帳號、PID、socket 路徑換成一致代稱。密碼、金鑰和完整除錯輸出保留在 repo 之外。

## Validation / Acceptance Checks

**TestCase**

1. 兩輪執行皆返回 `0`、預期主機與帳號、相同 master PID，並各有 mux 重用診斷。
2. 手動關閉後 `-O check` 失敗。原命令重試應顯示 socket 不可用、嘗試執行本機 `/usr/bin/false`、SSH 非零結束且無遠端身分輸出。與 OpenSSH 10.2p1 的 [mux 路徑](https://github.com/openssh/openssh-portable/blob/V_10_2_P1/ssh.c#L1596-L1615) 及 [傳輸選擇](https://github.com/openssh/openssh-portable/blob/V_10_2_P1/sshconnect.c#L508-L533) 核對。
3. 變更路徑須符合契約，進度、摘要與 README 的遮蔽證據須一致。圖資及靜態查核不代替上述實測。

兩項 SSH 測試都符合才記為成功。前置條件成立且證據明確反例時記為失敗。已嘗試但證據不足時記為無法判定。尚未嘗試記為未執行，並分開記錄本輪驗證任務是否完成。

## Reviewer Handoff

獨立 Plan-Reviewer 使用下列固定回傳格式，在實際 verdict 中選擇其中一個值。實驗的獨立 Reviewer 另外核對實測及文件證據。

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

本題交付停點為 Draft PR 的 human review。無 post-merge 或 release 動作。Topic 2 只在本題驗證完成後另行規劃。

## Open Questions / Unresolved Items

實測需要已授權且可登入的主機、設定入口、預期身分及使用者建立的 master。未取得前，實驗維持未執行。
