# Technical Specification — python-tooling-skills

**Version**: v0.41.0  
**Baseline Reference**: `analysis/python-tooling-skills/requirements.md`  
**Status**: Review-Ready

---

## 需求對應表

| 業務需求 | 技術實現 | 依賴 | 可行性 | 成本 |
|---|---|---|---|---|
| R-T4 | `templates/pre-commit-config.yaml` + RUFF_VERSION 佔位符 + Process 步驟 4 改版 | uv、ruff、sed / Python str.replace | 低風險 | 0.5 days |
| R-T5 | `python-pyproject-toolconfig` skill（新建） + script + 3 templates + 測試 | Python 3.11+、tomllib、tomllib-fallback handling | 中風險 | 1.5 days |
| R-T2 | `python-project-init.agent.md` Phase 6 + 角色邊界表更新 | 依賴 T4/T5 merged | 低風險 | 0.5 days |

---

## 技術任務分解

### T4：python-pre-commit 升版

**Artifact 路徑**：
```
.github/skills/python-pre-commit/
├── SKILL.md（Process Step 4 改版）
├── Local references 補 templates/ 條目
└── templates/
    └── pre-commit-config.yaml
```

**技術設計**：

1. **templates/pre-commit-config.yaml**（完整）
   ```yaml
   repos:
     # ruff
     - repo: https://github.com/astral-sh/ruff-pre-commit
       rev: RUFF_VERSION
       hooks:
         - id: ruff
           args: ["--fix"]
         - id: ruff-format
   
     # trailing-whitespace, check-yaml etc
     - repo: https://github.com/pre-commit/pre-commit-hooks
       rev: v4.5.0
       hooks:
         - id: trailing-whitespace
         - id: end-of-file-fixer
         - id: check-yaml
         - id: check-merge-conflict
         - id: check-added-large-files
           args: ["--maxkb=500"]
   
     # pytest (local, manual stage)
     - repo: local
       hooks:
         - id: pytest
           name: pytest
           entry: uv run pytest
           language: system
           types: [python]
           stages: [manual]
           pass_filenames: false
           always_run: true
   
     # pyright (local, manual stage, optional)
     - repo: local
       hooks:
         - id: pyright
           name: pyright
           entry: uv run --with pyright pyright
           language: system
           types: [python]
           stages: [manual]
           pass_filenames: false
           always_run: true
   ```

2. **SKILL.md Process Step 4 改版**（原 Step 3）
   ```
   Step 4. 產生 pre-commit config：
   - 若 templates/pre-commit-config.yaml 存在（skill 提供），執行：
     cp templates/pre-commit-config.yaml .pre-commit-config.yaml
   - 替換 RUFF_VERSION 佔位符：
     python -c "
     import re
     with open('.pre-commit-config.yaml') as f:
       content = f.read()
     ruff_version = __import__('subprocess').check_output(
       ['uv', 'run', 'ruff', '--version']
     ).decode().split()[1]
     content = re.sub(r'RUFF_VERSION', ruff_version, content)
     with open('.pre-commit-config.yaml', 'w') as f:
       f.write(content)
     "
   - 執行 install：uv run pre-commit install
   ```

3. **驗證測試**：
   ```bash
   uv run --with pyyaml -c "import yaml; yaml.safe_load(open('templates/pre-commit-config.yaml'))"
   ```

**可行性評估**：
- ✅ Template 靜態，修改低風險
- ✅ 跨平台（使用 Python re + subprocess 替代 sed）
- ⚠️ 需確保 ruff 版本解析正確（`ruff --version` 格式固定）

---

### T5：python-pyproject-toolconfig（新 Skill）

**Artifact 路徑**：
```
.github/skills/python-pyproject-toolconfig/
├── SKILL.md
├── examples.md
├── reference.md
├── scripts/
│   └── apply_toolconfig.py
├── templates/
│   ├── toolconfig-ruff.toml.tmpl
│   ├── toolconfig-pyright.toml.tmpl
│   └── toolconfig-pytest.toml.tmpl
└── tests/
    ├── test_section_detection.py
    ├── test_substitution.py
    ├── test_idempotent.py
    └── test_existing_preserved.py
```

**技術設計**：

1. **分塊 Templates**

   **toolconfig-ruff.toml.tmpl**
   ```toml
   [tool.ruff]
   line-length = 100
   target-version = "py${PYTHON_VERSION}"
   fix = true
   
   [tool.ruff.lint]
   select = ["E","W","F","N","D","UP","B","A","C4","ARG","RUF"]
   ignore = ["D100","D101","D102","D103","D104","D105"]
   
   [tool.ruff.lint.pydocstyle]
   convention = "google"
   
   [tool.ruff.lint.per-file-ignores]
   "__init__.py" = ["F401"]
   "tests/**/*.py" = ["D","ARG"]
   ```

   **toolconfig-pyright.toml.tmpl**
   ```toml
   [tool.pyright]
   typeCheckingMode = "strict"
   pythonVersion = "${PYTHON_VERSION}"
   include = ["src/${PACKAGE_NAME}"]
   exclude = ["**/tests/**","**/__pycache__","**/node_modules","**/.*",".venv","**/dist","**/build","**/.eggs"]
   ```

   **toolconfig-pytest.toml.tmpl**
   ```toml
   [tool.pytest.ini_options]
   minversion = "7.0"
   testpaths = ["tests"]
   python_files = ["test_*.py"]
   python_classes = ["Test*"]
   python_functions = ["test_*"]
   ```

2. **scripts/apply_toolconfig.py**（Inline Script Metadata）
   ```python
   # /// script
   # requires-python = ">=3.11"
   # ///
   import argparse
   import tomllib
   from pathlib import Path
   
   def main():
       parser = argparse.ArgumentParser()
       parser.add_argument("--python-version", required=True, help="e.g., 3.10")
       parser.add_argument("--package-name", required=True, help="e.g., mylib")
       args = parser.parse_args()
       
       pyproject_path = Path("pyproject.toml")
       if not pyproject_path.exists():
           raise FileNotFoundError("pyproject.toml not found")
       
       # 讀 pyproject 偵測 sections
       with open(pyproject_path, 'rb') as f:
           data = tomllib.load(f)
       
       existing_tools = set(data.get("tool", {}).keys())
       
       # 逐個 template append
       output_lines = []
       skill_dir = Path(__file__).parent.parent
       
       for tmpl_name, section_name in [
           ("toolconfig-ruff.toml.tmpl", "ruff"),
           ("toolconfig-pyright.toml.tmpl", "pyright"),
           ("toolconfig-pytest.toml.tmpl", "pytest")
       ]:
           if section_name not in existing_tools:
               tmpl_path = skill_dir / "templates" / tmpl_name
               with open(tmpl_path) as f:
                   content = f.read()
               content = content.replace("${PYTHON_VERSION}", args.python_version)
               content = content.replace("${PACKAGE_NAME}", args.package_name)
               output_lines.append(content)
       
       if output_lines:
           with open(pyproject_path, 'a') as f:
               f.write("\n" + "\n\n".join(output_lines))
           print(f"✅ Appended tool sections to {pyproject_path}")
       else:
           print("ℹ️  All tool sections already exist")
   
   if __name__ == "__main__":
       main()
   ```

   **執行方式**：
   ```bash
   uv run scripts/apply_toolconfig.py --python-version 3.10 --package-name mlops_async
   ```

3. **測試（pytest）**
   ```python
   # test_section_detection.py
   def test_existing_ruff_section_skipped(tmp_path):
       pyproject = tmp_path / "pyproject.toml"
       pyproject.write_text("[tool.ruff]\nline-length = 80\n")
       # 執行 script → 驗證 [tool.pyright] 被 append，但 [tool.ruff] 保留原值
   
   # test_idempotent.py
   def test_idempotent_append(tmp_path):
       # 執行兩次 script → 驗證 sections 不重複
   ```

**可行性評估**：
- ✅ tomllib inline metadata 保證版本相容
- ⚠️ raw text append 需謹慎（換行符號、結尾 EOF）
- ⚠️ section 偵測邏輯需單元測試覆蓋

---

### T2：python-project-init.agent.md Phase 6

**變更範圍**：
1. 角色邊界表新增 2 行（python-pre-commit、python-pyproject-toolconfig）
2. Phase 6 section（新增）：
   ```
   ### Phase 6 — Pre-commit & Tooling Setup
   
   **執行條件**：Phase 5 acceptance 通過
   **永遠執行**（無 Q9 分支）
   
   1. 執行 `/fleet @.github/skills/python-pre-commit/`
   2. 執行 `/fleet @.github/skills/python-pyproject-toolconfig/`
      - python-version 參數：來自 Q3
      - package-name 參數：來自 uv init 專案名稱
   3. 通知 install：`uv run pre-commit install`
   4. 驗證：`uv run pre-commit run --all-files`
      - Exit code 0 = Phase 6 成功 ✅
   ```

3. 禁止行為補充：❌ Phase 6 不得在 Phase 5 acceptance fail 前執行

---

## 架構合規性檢查

| 維度 | 檢查項 | 結果 |
|---|---|---|
| **Repository 邊界** | Skills 獨立、不污染 repo 本身 | ✅ 符合（skills 內部隔離） |
| **整合模式** | Phase 6 呼叫兩個 skills via `/fleet` | ✅ 符合（標準 agent orchestration） |
| **配置可攜性** | Template 固定值可跨專案複用 | ✅ 符合（變數化邊界清晰） |
| **安全邊界** | 無秘密資訊、無破壞性預設值 | ✅ 符合 |
| **冪等性** | 重複執行無副作用 | ✅ 符合（section 存在偵測、install 冪等） |

---

## 成本評估

| 工作項 | 複雜度 | 工期 | 備註 |
|---|---|---|---|
| T4 template + step 改版 | 低 | 0.5d | 外科手術式修改 |
| T5 script + templates | 中 | 1.5d | tomllib 讀寫、section 偵測、測試 |
| T5 測試覆蓋 | 中 | 0.5d | 單元 + 集成測試 |
| T2 agent.md Phase 6 | 低 | 0.5d | 依賴 T4/T5 merged |
| **總計** | | **2.5-3d** | 單一開發者 |

---

## 衝突與回退觸發

| 衝突 | 應對 | 回退觸發 |
|---|---|---|
| tomllib 無法序列化（不支援 write） | 改用 raw text append + section 偵測 | ❌ 不觸發回退（已解決） |
| pyproject.toml 格式破壞 | Script 先 backup、test round-trip | 📌 若 append 後 tomllib 解析失敗，回退需求評估 |
| Phase 6 interop 失敗 | 各 skill 獨立測試；Phase 5 acceptance 必須 pass | ✅ 若 Phase 5 fail → Phase 6 不執行（內嵌防護） |

---

## 驗收清單

- [ ] T4 template YAML 有效（`pyyaml` 驗證）
- [ ] T4 RUFF_VERSION 替換成功（手動測試）
- [ ] T5 script CLI args 可執行（`--help` 清晰）
- [ ] T5 section 偵測邏輯單元測試 ≥ 80% 覆蓋
- [ ] T5 idempotent 驗證通過
- [ ] T2 Phase 6 在 Phase 5 pass 後自動觸發
- [ ] `pre-commit run --all-files` exit code 0 確認
- [ ] README.md 更新新 skill 清單（after merge）
- [ ] VERSION bump 0.40.0 → 0.41.0 + tag

---

## 已解決的可行性風險

✅ **tomllib write 無法** → raw text append + tomllib 讀取偵測  
✅ **sed 跨平台差異** → Python str.replace() / re  
✅ **参數輸入界面** → CLI args + always-ask-human prompt  
✅ **T5 output 目標** → 直接寫入 pyproject.toml（append mode）；`--dry-run` flag 輸出 stdout 供 preview，不落盤  
✅ **Python 版本相容** → inline metadata `>=3.11`，uv 自動選版本  
✅ **pre-commit 冪等性** → 內建支援，重複 install 安全

---

## 後續維護

- 若 ruff / pyright rules 更新 → 僅修改 templates 檔案
- 若支援新工具配置 → 新增獨立 skill，遵循相同分塊 template 模式
- 若 Python 版本升級需求 → 調整 inline metadata、更新 Phase 6 文檔

**維護成本**：每個工具配置變更 ≈ 1-2 hours（template 更新 + 測試）
