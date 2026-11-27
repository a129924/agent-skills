# ssh-ops 按需唯讀下載

可選的 `analysis/ssh-ops/requirements.md` 與 `analysis/ssh-ops/technical-spec.md` 均不存在。規劃依使用者確認的對話版計畫、Topic 1 的 E001 及後續授權，未使用分析層契約。

## Goal / Outcome

**Goal**　交付 macOS Codex 的 canonical `ssh-ops` Skill 與對應範例。在已開啟的對話明確呼叫原生 `$ssh-ops` 並驗明受審版本後，可重用使用者建立的 OpenSSH master，取得一個雜湊一致、模式為 `0600` 且未覆寫既有檔案的本機副本。

**Non-Goal**　使用者管理 SSH 登入與 master 生命週期。伺服器管理遠端帳號與檔案權限。

## Scope

- **In-Scope**　新增兩份 Skill 檔案，逐項審查及採用候選內容，保存採用與驗收證據。本機受控驗證與獨立審查通過後，按 topic 提交、push 並開往 `dev` 的 Draft PR，由使用者人工審閱。取得另行指定的實測輸入和當次授權後進行正式實機驗收。
- **Out-Of-Scope**　上傳、批次、任意遠端命令、SFTP-only、憑證管理、SSH 設定或伺服器權限變更、自動重連、永久權限、Skill 安裝與平台投影、stable-library 更新、merge、tag 及 release。

## Locked Decisions

- 正式起點是合併 Topic 1 PR #131 的 `4058339167baaf316692fb2ec2e50110824d9827`。正式分支為 `feat/andrew/ssh-ops-download`，獨立 worktree 為 `../agent-skills.worktrees/agent-20261127-ssh-ops-download`。以 `c86f05e` 作候選來源，逐項對照本 plan，記錄保留、調整及排除的理由。
- 使用者確認目標、帳號、可信預設設定或 `-F`、master 和專用 socket 的對應、單一絕對來源路徑及私有本機目錄和新檔名。每次從唯讀基線取得一次性權限，只允許指定 socket 及已解析的目的目錄寫入，直接網路停用並遵守受管理限制。
- 維持非互動及同一 master。來源須是已授權可讀的一般檔案。傳輸先寫同目錄獨占的 `0600` 暫存檔，核對 master 及兩端 SHA-256 後原子交付到新檔名。失敗回報階段，只清除本次暫存。
- E001 原權限拒絕與後續一次性下載分別追溯。實機須證明同一個已開啟的對話以原生入口載入正式審查版本，記錄提交、檔案指紋及實測組合。首輪取一組，其餘格保留未驗證。
- 交付限 Draft PR 與人工審閱，無 stable-library 推廣。工具圖放在 repo 外，不作為實機驗收或審查通過證據。

## Boundaries / Exclusions

- **ReadOnly**　本機 `dev`、候選分支與 worktree、候選提交及歷史、Topic 1 與 E001、既有 SSH 設定、共用治理與 stable-library 檔案。
- **Written**　正式 worktree 內僅建立 Artifact Paths 所列追蹤檔。repo 外的寫入包括已核准的下載成品、測試資料、當次暫存及列定的工具產物。
- **Modify**　只有下列正式 topic 檔案可按實際證據與角色更新。變更鎖定契約或新增路徑前，先走正式計畫修訂與審查。
- **Deleted**　既有追蹤檔案零刪除。傳輸失敗只清除當次暫存，保留既有內容及成功成品。

## Status / Allowed Transitions

實際狀態由 `ssh-ops.step.md` 記錄。正式規劃基準提交後進入 `planned`，接續 `creator-in-progress` → `review-ready` → `reviewer-in-progress` → `approved` 或 `needs-rework`。回修或契約不符回到 `creator-in-progress`。審查與 Phase 4.5 對齊通過後進入 `publish-in-progress`。以實際 Draft PR 驗證 `pr-open`，移交人工審閱。當前授權涵蓋同一 topic 的本機提交、push 和 Draft PR。

## Artifact Paths

| 路徑 | Owner | 角色 |
| --- | --- | --- |
| `plan/ssh-ops/ssh-ops.plan.md` | Plan-Creator | 執行契約 |
| `plan/ssh-ops/ssh-ops.step.md` | Plan-Creator 及各階段角色 | 記錄進度、證據與派遣 |
| `plan/ssh-ops/ssh-ops.review-log.md` | Plan-Reviewer 或 Reviewer | 回饋影響派遣或有多輪回修時記錄審查及結果 |
| `skills/ssh-ops/SKILL.md` | Skill Creator | canonical 入口 |
| `skills/ssh-ops/examples.md` | Skill Creator | 設定、操作與失敗範例 |
| `docs/feasibility-adoption.md` | Implementer | 來源、採用與驗收證據 |
| `plan/ssh-ops/ssh-ops.summary.md` | Main Agent | 人工交接 |

`README.md`、`VERSION`、`.github/copilot-instructions.md` 及平台投影維持唯讀。PR Lens 的本機限定 diff、來源、JSON 與渲染在 `/private/tmp/ssh-ops/pr-lens/`。Archify 的 workflow 與收據在 `/private/tmp/ssh-ops/archify/`。Floorplan 藍圖在 `/private/tmp/ssh-ops/floorplan-workspace/floorplan/`，開本機 HTML，Ask 服務關閉。Graphify 只查可追溯既有圖，無適用圖時定向讀來源。Show-me 使用對話內 Mermaid。

## Implementation Steps

1. 逐項核對候選，寫入 canonical `SKILL.md` 和 `examples.md`。落實授權輸入、一次性沙箱、既有 master、固定唯讀遠端操作、暫存、完整性及不可覆寫交付。
2. 建立採用紀錄，區分原權限 E001、側對話證據、所採用內容及正式版本的實測狀態。保留預設／`-F` × 密碼／金鑰矩陣。
3. 核對 frontmatter、相對連結、Bash 範例及 OpenSSH 設定解析。用隔離的受控案例確認失敗階段與清理，回報未驗證項目。工具檢查依各自技能契約執行，產物限 repo 外。

## Validation / Acceptance Checks

**TestCase**

| 方式 | 情境 | 通過條件 |
| --- | --- | --- |
| 實機 | 在既有對話原生載入已審正式版本，使用一組授權的 SSH 設定與登入方式下載 | 留存版本、當次權限與同一 master 的證據。路徑、位元組數、兩端 SHA-256 及 `0600` 有據。 |
| 實機 | 成功後，由使用者關閉測試 master 或等它失效。沿用原目標、設定、來源與 socket，改用另行授權、確認不存在的檔名和當次權限 | 在 master 檢查階段停止。沒有替代連線、新成品或當次暫存。 |
| 受控 | socket 遭拒、目錄不可寫或同名檔已存在 | 到達各自預期階段。沒有新成品或當次暫存。已知內容的同名檔維持原樣。 |
| 受控 | 部分傳輸後逾時，或傳輸完成但 SHA-256 不符 | 到達傳輸或完整性階段，清除當次暫存，最終名稱未建立。 |

各受控案例使用獨立目的地，提前停止記為受阻。缺少原生載入、當次授權或有效沙箱時停在對應階段。Draft PR 可供審閱靜態與受控證據，清楚列出尚未執行的實機項目。遮蔽證據中的敏感路徑、省略檔案內容與憑證。

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

交付停在 Draft PR 人工審閱。此輪沒有 merge、post-merge sync、stable-library 變更、tag 或 release。

## Open Questions / Unresolved Items

實測前需要使用者提供授權的目標、來源、既有 master、目的地和當次權限。受審正式版本能否在原生對話識別、實機下載及矩陣覆蓋均按實際證據記錄。
