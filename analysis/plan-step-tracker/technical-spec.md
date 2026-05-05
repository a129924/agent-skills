# Technical Specification — plan-step-tracker

**Source baseline**: `analysis/plan-step-tracker/requirements.md` (FROZEN)  
**Output path**: `analysis/plan-step-tracker/technical-spec.md`  
**Status**: FROZEN v2 — 新增 R8/R9 技術翻譯，Python CLI + pytest，無 rollback 需要

---

## Source Baseline Summary

| Actor | Core need | Success signal |
| --- | --- | --- |
| Main Agent | 執行計畫時以低 token 成本查詢步驟狀態 | 1 次 CLI 呼叫取得全部步驟狀態，不逐一讀全文 |
| User | 詢問「哪些還沒做」時得到即時清單 | 輸出僅列 pending 步驟，且格式無歧義 |
| Developer / CI | 修改 step_tracker.py 後確認行為不回歸 | `pytest tests/` 全綠；exit code 1 供 CI blocking |

---

## Requirement-to-Technical Mapping

| Req | Technical Realization | Dependencies | Cost / Burden | Status |
| --- | --- | --- | --- | --- |
| R1 (file discovery) | `Path("plan") / topic / f"{topic}.step.md"` — 存在性檢查 | 目錄慣例 | 極低 | feasible |
| R2 (read_all) | `parse_steps(topic)` 傳回所有 Step 物件；CLI `read_all` subcommand | C1 ✅ | 極低 | feasible |
| R3 (read_not_run) | filter status == "pending"；CLI `read_not_run` subcommand | C1 ✅ | 極低 | feasible |
| R4 (read_success) | filter status == "done"；CLI `read_success` subcommand | C1 ✅ | 極低 | feasible |
| R5 (check_all_succeeded) | count pending → 0 = SUCCESS + exit 0；> 0 = BLOCKED + list + exit 1 | SKILL.md 指令 | 極低 | feasible |
| R6 (token efficiency) | Python 逐行讀一個檔案；不需讀多檔案 | Python ≥ 3.11 | 無額外 infra | feasible |
| R7 (scope) | 單一 `plan/<T>/<T>.step.md` | 慣例 | 低 | feasible |
| R8 (Python CLI) | `.github/skills/plan-step-tracker/scripts/step_tracker.py` — argparse，4 subcommand，uv script header | Python ≥ 3.11 | 低（1 個模組） | feasible |
| R9 (Tests) | `.github/skills/plan-step-tracker/tests/test_step_tracker.py` — pytest，6 覆蓋範疇，`tmp_path` fixture | pytest | 低–中 | feasible |

---

## Technical Artifacts Required

1. **`plan/<topic>/<topic>.step.md` 格式規範**（慣例文件，不是程式碼）
   - 定義於 `reference.md`；YAML frontmatter（meta only）+ 內容行 `- [ ]`/`- [X]`

2. **`.github/skills/plan-step-tracker/scripts/step_tracker.py`**（Python CLI，R8）

   ```python
   # /// script
   # requires-python = ">=3.11"
   # ///
   """Step status tracker for plan/<topic>/<topic>.step.md files.
   
   Usage:
     python step_tracker.py read_all <topic>
     python step_tracker.py read_not_run <topic>
     python step_tracker.py read_success <topic>
     python step_tracker.py check_all_succeeded <topic>  # exit 1 if pending
   """
   ```

   內部結構：
   - `Step` dataclass: `text: str`, `status: Literal["done", "pending"]`
   - `parse_steps(topic, plan_dir)` → `list[Step]`（逐行讀取，跳過非 `^\- \[.\]` 行）
   - `check_all_succeeded` 有 pending → print BLOCKED + list → `sys.exit(1)`
   - `[x]` 小寫視為 pending 並輸出 warning（不靜默接受）

3. **`.github/skills/plan-step-tracker/tests/test_step_tracker.py`**（pytest，R9）

   覆蓋範疇：
   | Test class | Cases |
   | --- | --- |
   | `TestParseStatus` | `[X]` → done；`[ ]` → pending；標題行/frontmatter 不被解析；`[x]` 小寫 → pending + warning |
   | `TestReadNotRun` | 混合狀態 → 只返 pending；全 done → 空清單 |
   | `TestReadSuccess` | 混合狀態 → 只返 done；全 pending → 空清單 |
   | `TestReadAll` | N checkbox 行 → N Step 物件 |
   | `TestCheckAllSucceeded` | 全 done → exit 0；有 pending → exit 1 + 清單 |
   | `TestEdgeCases` | 空檔案、`.step.md` 不存在 → FileNotFoundError、無 checkbox 行 |

4. **Agent Skill 資料夾**：`.github/skills/plan-step-tracker/`
   - `SKILL.md`：觸發條件、4 種操作（優先呼叫 `step_tracker.py`，grep 為 fallback）
   - `reference.md`：`.step.md` 格式規範 + grep 模式速查 + 分組規則 + CLI 用法
   - `examples.md`：4 種操作範例、blocking 範例、edge case 範例

---

## Architecture-Compliance Self-Check

| Dimension | Result | Note |
| --- | --- | --- |
| Repo 現有目錄慣例 | **fits with prerequisites** | 需建立 `plan/<topic>/*.step.md` 新慣例；現有 `plan/*.plan.md` 不受影響 |
| Skill 資料夾結構 | **fits existing architecture** | 遵循現有 `SKILL.md + reference.md + examples.md` 結構 |
| Python uv script | **fits existing architecture** | 符合 `python-pyproject-toolconfig` 的 `# /// script` 慣例 |
| pytest tests | **fits existing architecture** | `.github/skills/<name>/tests/` 同 `python-pyproject-toolconfig` pattern |
| grep/glob 工具 | **fits existing architecture** | Agent 已有 grep/glob 工具；作為 fallback 用 |
| 與 SQL todos 整合 | **no conflict** | `.step.md` 是獨立機制，不取代 SQL todos；兩者並存 |
| VERSION bump | **fits with prerequisites** | 新增 stable skill → MINOR bump（0.41.0 → 0.42.0） |
| `examples.md` 必要性 | **required** | 有分支邏輯（4 種操作 + blocking 判斷）→ 需 `examples.md` |
| `[x]` 小寫處理 | **needs explicit rule** | 只接受 `[X]`，`[x]` → pending + warning；必須寫進 reference.md |
| C3 conflict | **resolved** | Python CLI 為主執行層，grep 為 fallback；SKILL.md 需明確指示順序 |

---

## Cost of Realization

| Workstream | Complexity | Sequencing | Burden |
| --- | --- | --- | --- |
| 定義 `.step.md` 格式 | 低 | 必須先於 SKILL.md 完成 | 一次性，之後沿用 |
| 撰寫 `.github/skills/plan-step-tracker/scripts/step_tracker.py` | 低-中 | 依賴格式決定 | 1 個 Python 模組，argparse + dataclass |
| 撰寫 `.github/skills/plan-step-tracker/tests/test_step_tracker.py` | 中 | 依賴 CLI 完成 | 6 test class，tmp_path fixture |
| 撰寫 `SKILL.md` | 低-中 | 依賴 CLI + 格式 | CLI 用法 + grep fallback 指引 |
| 撰寫 `reference.md` | 低 | 依賴格式決定 | 格式規範 + grep 模式速查 + `[x]` warning 規則 |
| 撰寫 `examples.md` | 中 | 依賴 SKILL.md | 需涵蓋 4 種操作 + blocking + edge case |
| agent-skill-creator 子代理 | — | 依賴分析完成 | Creator/Reviewer 角色分離 |
| agent-skill-reviewer 子代理 | — | 依賴 creator 完成 | 獨立審查 |
| README + VERSION bump | 低 | 最後 | 1 行 + 1 版號 |

**總評估**：低至中等複雜度。Python CLI + tests 是主要工作量，Skill 文件為輔。無 infra 依賴，無外部 API 呼叫。

---

## Open Items / Blockers

~~**BLOCKER (soft) — C1：`.step.md` 狀態格式尚未最終確定**~~

**✅ C1 已解決**：格式確認為內容行 `- [ ]`/`- [X]`，單一 `<topic>.step.md` 檔案，YAML frontmatter 僅含 meta（topic/phase/created）。

~~**C2：multi-topic 彙總**~~ — 已移入 Non-Goals，不阻斷。

**✅ C3 已解決（Python vs grep）**：Python CLI 為主執行層（testable、cross-platform）；grep 為 fallback，僅在 CLI 不可用時使用。SKILL.md 需明確記載此優先順序。

**無遺留 blocker。**

---

## Conflicts Detected

**無 rollback-to-alignment 需要的衝突。**

所有需求（R1-R9）均可在現有 repo 架構下實現。C3 衝突（Python CLI vs grep）已決定：以 Python CLI 為主層，SKILL.md 記載 fallback 行為即可解決，無需更改需求或架構。

---

## Rollback Note

無需觸發 rollback-to-alignment。基線需求均可如實翻譯。

---

## Handoff

此 technical-spec 已凍結（v2），可作為 `plan-creator` 的嚴格模式（strict-mode）輸入。  
建議 plan 採用 strict-mode（兩份 analysis 文件均存在，C1/C2/C3 均已解決）。

**R8/R9 已加入**：Creator 需同時生成 `.github/skills/plan-step-tracker/scripts/step_tracker.py` 與 `.github/skills/plan-step-tracker/tests/test_step_tracker.py`。
