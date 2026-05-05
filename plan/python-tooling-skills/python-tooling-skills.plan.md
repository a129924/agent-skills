# python-tooling-skills

## Goal / Outcome

v0.41.0 交付完成時，repo 包含：
1. **python-pre-commit** skill 升版：新增 `templates/pre-commit-config.yaml`（RUFF_VERSION 佔位符），SKILL.md Process Step 4 改為 cp + Python str.replace 替換 RUFF_VERSION，不再靠 Agent 逐行生成 YAML
2. **python-pyproject-toolconfig** 新 skill：分塊 templates + `apply_toolconfig.py` script（inline metadata `>=3.11`，CLI args，偵測 section 後直接 append，支援 `--dry-run` preview），搭配單元測試
3. **python-project-init.agent.md** 補 Phase 6（永遠執行，呼叫兩個新 skill）

## Scope

- **In scope**:
  - `.github/skills/python-pre-commit/SKILL.md` — Process Step 4 改版
  - `.github/skills/python-pre-commit/templates/pre-commit-config.yaml` — 新建
  - `.github/skills/python-pyproject-toolconfig/` — 全新 skill 目錄
    - `SKILL.md`
    - `examples.md`
    - `reference.md`
    - `scripts/apply_toolconfig.py`
    - `templates/toolconfig-ruff.toml.tmpl`
    - `templates/toolconfig-pyright.toml.tmpl`
    - `templates/toolconfig-pytest.toml.tmpl`
    - `tests/test_section_detection.py`
    - `tests/test_substitution.py`
    - `tests/test_idempotent.py`
    - `tests/test_existing_preserved.py`
  - `.github/agents/python-project-init.agent.md` — 角色邊界表 + Phase 6 新增
  - `README.md` — 新增 python-pyproject-toolconfig 條目
  - `VERSION` — 0.40.0 → 0.41.0

- **Out of scope**:
  - python-pre-commit 的 hooks 邏輯變更（只加 template，不改 hook 種類）
  - pyproject.toml 中的 `[project]` / `[build-system]` sections
  - exclude patterns template 化（用戶自行管理）
  - python-project-init Phase 0–5 任何改動

## Locked Decisions

- **Template 化策略**：RUFF_VERSION 用 Python `re.sub` 替換（不用 shell sed，跨平台相容）
- **T5 分塊 templates**：三個獨立 `.toml.tmpl`（ruff / pyright / pytest），各自偵測對應 section
- **T5 script 執行**：inline metadata `requires-python = ">=3.11"`，`uv run` 自動選已裝版本
- **T5 output**：直接寫入 pyproject.toml（append mode）；提供 `--dry-run` flag 輸出 stdout 供 preview，不修改檔案
- **T5 script 參數**：CLI args（`--python-version` / `--package-name`，always-ask-human）
- **Phase 6 執行**：永遠執行，不問 Q9，Phase 5 acceptance 通過後自動進入
- **冪等性保證**：section 存在時跳過 append；`pre-commit install` 本身冪等
- 本次為 stable-library-affecting topic：`README.md` + `VERSION` 在 `publish-in-progress` 階段更新

## Boundaries / Exclusions

- T2（agent.md Phase 6）依賴 T4/T5 均已在同一 PR 完成，主 agent 不得在 T4/T5 未完成前執行 T2
- Creator 不得自行扮演 reviewer；Reviewer 不得自行撰寫實作
- python-pre-commit 現有測試（`tests/`）若不存在，T4 不新建（T4 scope 限 template + SKILL.md 改版）

## Status / Allowed Transitions

- **Current**: `planned`
- **Execution model**: 三個子任務（T4 / T5 / T2）依序：T4+T5 平行 creator → 各自 reviewer → T2 creator → T2 reviewer → publish → merge
- **Allowed transitions**:
  - `planned` → `creator-in-progress`
  - `creator-in-progress` → `review-ready`
  - `review-ready` → `reviewer-in-progress`
  - `reviewer-in-progress` → `approved`
  - `reviewer-in-progress` → `needs-rework`
  - `needs-rework` → `creator-in-progress`
  - `approved` → `creator-in-progress`
  - `approved` → `publish-in-progress`
  - `publish-in-progress` → `pr-open`
  - `publish-in-progress` → `merged`
  - `pr-open` → `needs-rework`
  - `pr-open` → `merged`
  - `merged` → `released`

Routing notes:
- T4 + T5 可平行進入 `creator-in-progress`
- T2 在 T4 + T5 均 `approved` 後才進入 `creator-in-progress`
- 本 topic 宣告 `timing=publish-in-progress`（README + VERSION 在 publish 階段更新）

## Artifact Paths

| Artifact | Path | Owner | Role |
|---|---|---|---|
| Topic plan | `plan/python-tooling-skills/python-tooling-skills.plan.md` | Planning actor | Repo-visible execution contract |
| python-pre-commit SKILL.md | `.github/skills/python-pre-commit/SKILL.md` | Creator | Process Step 4 改版 |
| python-pre-commit template | `.github/skills/python-pre-commit/templates/pre-commit-config.yaml` | Creator | 完整 YAML template，含 RUFF_VERSION 佔位符 |
| python-pyproject-toolconfig SKILL.md | `.github/skills/python-pyproject-toolconfig/SKILL.md` | Creator | 新 skill 主文件 |
| python-pyproject-toolconfig examples.md | `.github/skills/python-pyproject-toolconfig/examples.md` | Creator | 詳細使用範例 |
| python-pyproject-toolconfig reference.md | `.github/skills/python-pyproject-toolconfig/reference.md` | Creator | 穩定技術參考 |
| apply_toolconfig.py | `.github/skills/python-pyproject-toolconfig/scripts/apply_toolconfig.py` | Creator | 主要執行腳本（inline metadata >=3.11） |
| ruff template | `.github/skills/python-pyproject-toolconfig/templates/toolconfig-ruff.toml.tmpl` | Creator | [tool.ruff] block template |
| pyright template | `.github/skills/python-pyproject-toolconfig/templates/toolconfig-pyright.toml.tmpl` | Creator | [tool.pyright] block template |
| pytest template | `.github/skills/python-pyproject-toolconfig/templates/toolconfig-pytest.toml.tmpl` | Creator | [tool.pytest.ini_options] block template |
| tests | `.github/skills/python-pyproject-toolconfig/tests/` | Creator | 4 個單元測試（section 偵測、替換、冪等、保留） |
| python-project-init agent | `.github/agents/python-project-init.agent.md` | Creator (T2) | Phase 6 新增 + 角色邊界表更新 |
| README.md | `README.md` | Main Agent | 新增 python-pyproject-toolconfig 條目（publish-in-progress） |
| VERSION | `VERSION` | Main Agent | 0.40.0 → 0.41.0（publish-in-progress） |

此 topic 修改 `README.md`（新增 skill 條目）、`VERSION`（0.40.0 → 0.41.0）、`.github/agents/python-project-init.agent.md`。
若後續工作出現不在上列路徑內的變更，視為計畫偏移，須先回報。

## Stable library metadata

- `README row`: 新增一行至 `## Current skills` 表格：`python-pyproject-toolconfig | Tool sections template + apply script`
- `VERSION bump`: MINOR，0.40.0 → 0.41.0
- `timing`: `publish-in-progress`
- `rationale`: python-pyproject-toolconfig 是新的 stable skill；python-pre-commit 升版補足 template 化後重新標記為 stable

## Implementation Steps

### T4：python-pre-commit 升版（creator-in-progress → review-ready）

1. 建立 `.github/skills/python-pre-commit/templates/pre-commit-config.yaml`
   - 包含 4 種 hooks（ruff + ruff-format、pre-commit-hooks 5 項、pytest local manual、pyright local manual）
   - `rev: RUFF_VERSION` 作為佔位符
2. 更新 `.github/skills/python-pre-commit/SKILL.md`
   - Process Step 4：cp template → Python str.replace 替換 RUFF_VERSION → install
   - Local references 補 `templates/` 條目
3. YAML 驗證：`uv run --with pyyaml -c "import yaml; yaml.safe_load(open('templates/pre-commit-config.yaml'))"`

### T5：python-pyproject-toolconfig 新 skill（creator-in-progress → review-ready）

1. 建立 `templates/toolconfig-ruff.toml.tmpl`（含 `${PYTHON_VERSION}` 佔位符）
2. 建立 `templates/toolconfig-pyright.toml.tmpl`（含 `${PYTHON_VERSION}` / `${PACKAGE_NAME}`）
3. 建立 `templates/toolconfig-pytest.toml.tmpl`（固定值，無佔位符）
4. 建立 `scripts/apply_toolconfig.py`（inline metadata `>=3.11`，tomllib section 偵測，raw text append，stdout 輸出）
5. 建立 4 個單元測試（section 偵測、substitution、idempotent、existing 保留）
6. 建立 `SKILL.md`、`examples.md`、`reference.md`

### T2：python-project-init.agent.md（T4+T5 approved 後）

1. 角色邊界表新增 2 行（python-pre-commit、python-pyproject-toolconfig）
2. 新增 Phase 6 section（永遠執行，Phase 5 通過後自動進入，呼叫兩個 skill，install + 驗證）
3. 禁止行為補充：❌ Phase 6 不得在 Phase 5 fail 前執行
4. 共存關係補充：兩個新 skill 的說明行

## Validation / Acceptance Checks

- T4 YAML template 通過 `pyyaml` 驗證（`uv run --with pyyaml`）
- T4 SKILL.md Process Step 4 明確包含 cp + Python str.replace + install 三步
- T4 Local references 包含 `templates/` 條目
- T5 script 可執行（`uv run scripts/apply_toolconfig.py --help` 顯示兩個必要參數）
- T5 script inline metadata 包含 `requires-python = ">=3.11"`
- T5 所有 4 個單元測試通過（`uv run --with pytest pytest .github/skills/python-pyproject-toolconfig/tests/ -v`）
- T5 `SKILL.md` Local references 列出 scripts/、templates/、tests/ 並說明各自用途
- T2 `python-project-init.agent.md` Phase 6 存在且明確「永遠執行」
- T2 角色邊界表包含 python-pre-commit 和 python-pyproject-toolconfig 兩行
- README.md 新增條目
- VERSION 為 `0.41.0`
- `plan/python-tooling-skills/python-tooling-skills.plan.md` 本身存在且路徑正確

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

1. 刪除 branch（remote + local）：`feat/andrew/python-tooling-skills`
2. `git pull --ff-only main`
3. `git tag v0.41.0 && git push origin v0.41.0`
4. 確認 `VERSION` = `0.41.0` 且 `README.md` 含新 skill 條目

## Open Questions / Unresolved Items

- 無。所有技術決策已在 `analysis/python-tooling-skills/` 凍結，無待解項目
