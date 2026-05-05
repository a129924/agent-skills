# Business Baseline — python-tooling-skills

**Topic**: 擴展 Python 專案初始化工具鏈，補足 pre-commit template 化與 pyproject.toml tool sections 自動化

**Frozen Date**: 2026-05-05

---

## 需求總覽

| ID | 需求陳述 | 可測量條件 | 優先級 |
|---|---|---|---|
| R-T2 | `python-project-init.agent.md` 補 Phase 6（永遠執行，不問 Q9） | Phase 6 section 存在、永遠執行、呼叫兩個 skill | P0 |
| R-T4 | `python-pre-commit` skill 加 `templates/pre-commit-config.yaml` | 完整 YAML template、cp + sed 流程、RUFF_VERSION 佔位符替換 | P0 |
| R-T5 | 新建 `python-pyproject-toolconfig` 獨立 skill | script 支援 CLI args、template 分塊結構、tomllib 偵測 section 存在、append 不覆寫 | P0 |

---

## 凍結的業務決策

### 1. Template 化策略

**背景**：用戶習慣的 pre-commit hooks 和 pyproject.toml 工具配置都是固定的，每次手動編寫浪費 token、容易出錯。

**決策**：
- ✅ `python-pre-commit` 新增 `templates/pre-commit-config.yaml`，包含全部 4 種 hooks（ruff, trailing-whitespace 等、pytest manual、pyright optional）
- ✅ `python-pyproject-toolconfig` 使用分塊 templates：`toolconfig-ruff.toml.tmpl`、`toolconfig-pyright.toml.tmpl`、`toolconfig-pytest.toml.tmpl`
- ✅ Script 偵測現有 sections → 只 append 缺少的 blocks，不覆寫

### 2. 固定值 vs 變數邊界

**R-T4（pre-commit）**：
- 固定：所有 hooks 組態、stages、args
- 變數：只有 `RUFF_VERSION`（由 `uv run ruff --version` 動態取得）

**R-T5（pyproject toolconfig）**：
- 固定：`line-length=100`、所有 select/ignore rules、`convention=google`、pytest patterns、pyright excludes
- 變數：`python_version`（target-version / pythonVersion）、`package_name`（include path）
- **不納入 template**：`exclude` patterns（用戶自行管理，過於客製化）

### 3. Phase 6 執行策略

**R-T2**：
- 永遠執行（不新增 Q9 詢問）
- 順序：Phase 5 通過 → 自動進 Phase 6
- 動作：呼叫 `/fleet @python-pre-commit/` 和 `/fleet @python-pyproject-toolconfig/`，然後 `uv run pre-commit install` 和驗證

---

## 極端邊界檢查（Extreme-Boundary Validation）

| 邊界情境 | 需求如何應對 |
|---|---|
| **Section 已存在** | Script 偵測 section（tomllib 讀取）→ 跳過 append，不重複 |
| **pyproject.toml 不存在** | Script 報錯（明確 error message），不自動建立 |
| **sed/awk 跨平台差異** | T4 改用 Python `str.replace()` 替代 sed，避免 macOS/Linux 差異 |
| **Python < 3.11** | T5 使用 inline metadata `requires-python = ">=3.11"`，uv 自動選合適版本，避免下載 |
| **參數缺失** | T5 script 採 always-ask-human（互動式 prompt），不默默失敗 |
| **Pre-commit 已安裝** | `pre-commit install` 本身冪等，重複執行無副作用 ✅ |

---

## 非需求（Out of Scope）

- ❌ `exclude` patterns 不進 template（用戶自行在 pyproject.toml 補充）
- ❌ pyproject 的其他 sections（如 `[project]` / `[build-system]`）不修改
- ❌ 針對個別專案的自訂 ruff rules（template 只提供標準 ruleset）
- ❌ 事後修改已生成的 template（script 輸出到 stdout，用戶自行 review）

---

## 衝突與阻礙（Resolved）

| 潛在衝突 | 解決方案 |
|---|---|
| tomllib 無法寫入 TOML | 改用 raw text append + section 存在偵測（tomllib 讀、Python append 寫） |
| `sed -i` macOS/Linux 不相容 | 改用 Python `str.replace()`（T4） |
| 參數輸入介面不清 | T5 script 用 CLI args + always-ask-human prompt（用戶確認後執行） |
| T5 output 到哪 | 輸出到 stdout（用戶 review 後自行 redirect 進 pyproject.toml） |

---

## 驗收信號

- [ ] T4 YAML template 語法正確（`uv run --with pyyaml` 驗證）
- [ ] T4 Process Step 4 成功執行 sed 替換（手動測試）
- [ ] T5 script CLI args 格式確定（`--python-version` / `--package-name`）
- [ ] T5 script 偵測 section 存在邏輯正確（單元測試覆蓋）
- [ ] T2 Phase 6 在 Phase 5 通過後自動進入（集成測試）
- [ ] `pre-commit run --all-files` exit code 0 = Phase 6 驗證通過 ✅

---

## 假設與後續

**假設**：
- 用戶的 pre-commit hooks 和 pyproject.toml 工具配置長期穩定（固定值不變）
- Python >= 3.10 環境已準備

**後續需求追蹤**：
- 若 ruff / pyright 規則更新，僅修改 template 區塊，不影響 skill 本身
- 若用戶需要更多工具配置（如 `[tool.mypy]`），用獨立 skill 擴展，不混入現有 skill
