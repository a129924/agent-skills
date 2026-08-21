# WSL 原生 pre-commit 驗證

Windows Git 建立的 linked worktree 會在 `.git` 檔案內存放 Windows 路徑，
例如 `gitdir: D:/code/...`。WSL Git 不會可靠地將這種路徑解讀為 Windows
絕對路徑，因此不要在這種 worktree 中執行 `pre-commit`，也不要改寫其
`.git` 指標。

請改用 `scripts/verify-wsl-precommit.sh`。腳本不會讀取或修改 feature
worktree 的 Git metadata；它會在 WSL Linux 檔案系統中建立 bare cache 與
暫存 detached worktree，並在與 Windows worktree 相同的 commit SHA 執行
所有 hooks。

## 前置條件

- 欲驗證的 commit 已推送到 `origin`。
- WSL 可使用 `git`、`uv`、`flock`、`realpath`、`sha256sum` 與 `mktemp`。
- WSL 的 Git 認證可存取該 `origin`；第一次執行也需要下載
  `pre-commit==4.6.1`。

## 從 Windows worktree 取得不可變輸入

在 PowerShell 中，以 Windows Git 對 feature worktree 取得 SHA 與 remote：

```powershell
$worktree = 'D:\code\python\agent-skills.worktrees\agent-20260730-windows-wsl-dev'
$sha = git -C $worktree rev-parse HEAD
$origin = git -C $worktree remote get-url origin
```

這兩個值是唯一需要由 Windows worktree 讀取的資訊。請勿在 WSL 中對該
worktree 執行 Git 命令。

## 在 WSL 執行

將上述值帶入下列命令：

```bash
bash /mnt/d/code/python/agent-skills/scripts/verify-wsl-precommit.sh \
  --repo-url 'https://github.com/a129924/agent-skills.git' \
  --sha 'FULL_40_CHARACTER_COMMIT_SHA'
```

預設 cache 位於 `$XDG_CACHE_HOME/agent-skills-precommit`，或
`$HOME/.cache/agent-skills-precommit`。可用 `--cache-root` 指定另一個
WSL Linux 檔案系統路徑；腳本會拒絕 `/mnt/...`，避免再次將 Git metadata
放入 Windows 掛載點。

成功時，暫存 worktree 會被移除，bare cache 與 pre-commit 環境會保留以
加速下一次驗證。失敗時，暫存 worktree 會保留，腳本會印出其位置，方便
檢查 hook 的輸出或 formatter 造成的變更。

## 常見失敗

- `commit is not available from origin`：確認該 SHA 已推送，並確認
  `--repo-url` 是 feature branch 所在的 remote。
- 認證或 fetch 失敗：先在 WSL 確認可對相同 URL 執行 `git fetch`。
- hook 失敗：使用輸出的 temporary worktree 路徑檢查變更；原始 Windows
  worktree 不受影響。
