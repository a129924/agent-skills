# python-tooling-skills-v2

## Goal / Outcome

v0.43.0 交付完成時，repo 包含：
1. **python-pre-commit** skill 補強：新增 `scripts/apply_precommit.py`（`--ruff-version` / `--dry-run` / `--force`）與對應 5 個單元測試；SKILL.md Process Step 4 改為呼叫 script；hooks-catalog.md 補充 ruff version 手動更新說明
2. **python-project-init.agent.md** Phase 6 Step 4 加入 5-hook 失敗診斷表（ruff / ruff-format / pytest / trailing-whitespace / check-yaml）
3. **python-pyproject-toolconfig** SKILL.md Boundaries 新增「更新現有 section 超出本 skill 範圍」聲明

## Scope

### In scope
- `.github/skills/python-pre-commit/scripts/apply_precommit.py` — 新建
- `.github/skills/python-pre-commit/tests/test_apply_precommit.py` — 新建（5 tests）
- `.github/skills/python-pre-commit/SKILL.md` — Process Step 4 改版 + Local references 補充
- `.github/skills/python-pre-commit/examples.md` — Scenario 1 加 script 呼叫 + rev 更新至 v0.15.12
- `.github/skills/python-pre-commit/references/hooks-catalog.md` — rev 更新至 v0.15.12 + version note
- `.github/agents/python-project-init.agent.md` — Phase 6 Step 4 加診斷表
- `.github/skills/python-pyproject-toolconfig/SKILL.md` — Boundaries 加一行
- `README.md` — 更新 python-pre-commit 條目說明
- `VERSION` — 0.42.1 → 0.43.0

### Out of scope
- python-pre-commit 現有 hooks 邏輯、hook 種類、現有測試
- python-pyproject-toolconfig 的其他 sections 或 scripts
- python-project-init.agent.md Phase 0–5 任何改動

## Locked Decisions

| 決策點 | 決定 |
|--------|------|
| RUFF_VERSION 來源 | 寫死 `DEFAULT_RUFF_VERSION = "v0.15.12"`；不呼叫 subprocess |
| --force 行為 | 預設拒絕（exit 1）；Phase 6 Agent 自動攜帶 `--force` |
| 測試策略 | 真實 uv 呼叫 + `tmp_path` 隔離 |
| inline metadata | `# requires-python = ">=3.11"` |

## Stable Library Metadata

- **Topic**: `python-tooling-skills-v2`
- **Version**: 0.43.0
- **Affected skills**: `python-pre-commit`（主要）、`python-pyproject-toolconfig`（minor）
- **README.md update required**: yes
- **VERSION bump**: MINOR

## Tasks

| ID | Description | Primary Artifact | Status |
|----|-------------|-----------------|--------|
| T3 | python-pyproject-toolconfig SKILL.md Boundaries 補一行 | `python-pyproject-toolconfig/SKILL.md` | done |
| T2 | python-project-init.agent.md Phase 6 診斷表 | `python-project-init.agent.md` | done |
| T1 | apply_precommit.py + tests + SKILL.md + hooks-catalog + examples | multiple | done |

## Status Transitions

- `planned` → `creator-in-progress` → `review-ready` → `reviewer-in-progress` → `approved` → `publish-in-progress` → `pr-open` → `merged`

**Current Status**: `publish-in-progress`

## Analysis Layer

- `analysis/python-tooling-skills-v2/requirements.md` — FROZEN（R1–R6）
- `analysis/python-tooling-skills-v2/technical-spec.md` — FROZEN

## Post-merge / Release Actions

1. Delete remote + local branch `feat/andrew/python-tooling-skills-v2`
2. `git pull --ff-only origin dev`
3. Push tag `v0.43.0`
4. Verify `VERSION` = `0.43.0` in main
