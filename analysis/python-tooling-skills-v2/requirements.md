# Requirements — python-tooling-skills-v2

**Status**: FROZEN
**Version target**: v0.43.0
**Baseline**: v0.41.0 遺留缺口補強

---

## R1 — apply_precommit.py script 化（T1）

**觀察點**：`python-pre-commit` skill 的 `templates/pre-commit-config.yaml` 含有 `RUFF_VERSION` placeholder，目前需 Agent 用 inline Python 手動替換。

**需求**：提供 `scripts/apply_precommit.py` script，支援以下行為：
- `--ruff-version`（預設 `v0.15.12`，純字串，不呼叫 subprocess）
- `--dry-run`（stdout 預覽，不落盤）
- `--force`（預設拒絕覆蓋；加 `--force` 才可覆蓋已存在的 `.pre-commit-config.yaml`）
- inline metadata `# requires-python = ">=3.11"`

**可觀察**：執行 `uv run scripts/apply_precommit.py` 在空目錄產生 `.pre-commit-config.yaml`，ruff 的 `rev` 值 = `v0.15.12`；執行相同指令第二次（無 `--force`）exit code ≠ 0 並輸出明確錯誤訊息。

---

## R2 — SKILL.md Process 更新（T1 附帶）

**需求**：`python-pre-commit/SKILL.md` Process Step 4 改為呼叫 `apply_precommit.py`（含 `--dry-run` 用法說明）；Local references 加 `scripts/apply_precommit.py` 條目。

**可觀察**：SKILL.md Process Step 4 不再有 inline Python snippet，改為 `uv run scripts/apply_precommit.py [options]` 指令範例。

---

## R3 — hooks-catalog.md 補充 ruff version 說明（T1 附帶）

**需求**：`references/hooks-catalog.md` 的 ruff-pre-commit 區段補充說明 rev 版本手動更新方式及來源 URL。

**可觀察**：hooks-catalog.md 中有 `https://github.com/astral-sh/ruff-pre-commit/releases` 連結，並說明版本與 uv ruff 版本脫鉤。

---

## R4 — --force 拒絕行為明確（T1 設計約束）

**需求**：預設不帶 `--force` 時，若 `.pre-commit-config.yaml` 已存在，script 必須 exit 1 並輸出明確提示。Phase 6 controlled flow 由 Agent 自動攜帶 `--force`。

**可觀察**：`test_no_force_fails_if_exists` 測試通過；`test_force_overwrites` 測試通過。

---

## R5 — Phase 6 debug 診斷表（T2）

**需求**：`python-project-init.agent.md` Phase 6 Step 4 在「exit code ≠ 0」分支加入 5-hook 失敗診斷表（ruff, ruff-format, pytest, trailing-whitespace, check-yaml）。

**可觀察**：agent.md Phase 6 Step 4 包含診斷表，每個 hook 對應「常見原因」和「建議修復」。

---

## R6 — python-pyproject-toolconfig Boundaries 補充（T3）

**需求**：`python-pyproject-toolconfig/SKILL.md` Boundaries 新增一行聲明：更新或修改現有 `[tool.*]` section 的內容超出本 skill 範圍，由 human 負責。

**可觀察**：SKILL.md Boundaries 區段中可找到該聲明。
