# Technical Specification — python-tooling-skills-v2

**Status**: FROZEN
**Derived from**: `requirements.md` R1–R6
**Version target**: v0.43.0

---

## R→T Mapping

| Requirement | Technical Task | Artifact Path |
|-------------|---------------|---------------|
| R1 | T1a: 新增 `apply_precommit.py` | `.github/skills/python-pre-commit/scripts/apply_precommit.py` |
| R1 | T1b: 新增 `test_apply_precommit.py` | `.github/skills/python-pre-commit/tests/test_apply_precommit.py` |
| R2 | T1c: 更新 SKILL.md Process Step 4 + Local references | `.github/skills/python-pre-commit/SKILL.md` |
| R3 | T1d: 更新 hooks-catalog.md ruff-pre-commit 區段 | `.github/skills/python-pre-commit/references/hooks-catalog.md` |
| R4 | T1b: 測試 `test_no_force_fails_if_exists` + `test_force_overwrites` | 同 T1b |
| R5 | T2: 更新 Phase 6 Step 4 加診斷表 | `.github/agents/python-project-init.agent.md` |
| R6 | T3: 更新 Boundaries 加一行聲明 | `.github/skills/python-pyproject-toolconfig/SKILL.md` |

---

## T1 — apply_precommit.py 實作規格

**CLI interface**：
```
uv run scripts/apply_precommit.py [--ruff-version VERSION] [--dry-run] [--force]
```

| Arg | 預設 | 說明 |
|-----|------|------|
| `--ruff-version` | `v0.15.12` | ruff-pre-commit rev（純字串，不呼叫 subprocess） |
| `--dry-run` | False | 輸出 stdout，不落盤 |
| `--force` | False | 允許覆蓋已存在的 `.pre-commit-config.yaml` |

**5 個測試**：

| 測試名稱 | 驗證目標 |
|---------|---------|
| `test_version_substitution` | RUFF_VERSION 被替換為預設 `v0.15.12` |
| `test_custom_ruff_version` | `--ruff-version v0.12.0` 正確寫入 |
| `test_dry_run_no_write` | `--dry-run` 不修改磁碟 |
| `test_force_overwrites` | 已存在 + `--force` → 成功覆蓋 |
| `test_no_force_fails_if_exists` | 已存在 + 無 `--force` → exit code 1 |

---

## T2 — Phase 6 Step 4 診斷表（5 hooks）

`ruff`, `ruff-format`, `pytest`, `trailing-whitespace`/`end-of-file-fixer`, `check-yaml`

---

## T3 — Boundaries 補充

`不負責更新現有 [tool.*] section 的內容；修改現有設定的維護責任由 human 承擔`

---

## 架構合規自查

| 檢查項目 | 狀態 |
|---------|------|
| T1 script 無 external deps（pure stdlib）| ✅ |
| T1 tests 用 `tmp_path` 隔離 | ✅ |
| T1 inline metadata `>=3.11` | ✅ |
| T2 只改 agent.md，不動 Phase 0–5 | ✅ |
| T3 只加一行，不改現有 Boundaries 項目 | ✅ |
| VERSION MINOR bump | ✅ 0.42.1 → 0.43.0 |
