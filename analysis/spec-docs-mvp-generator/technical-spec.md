# Technical Specification: spec-docs-mvp-generator

**Status**: READY FOR EXECUTION PLANNING  
**Topic**: `spec-docs-mvp-generator`  
**Baseline Reference**: `analysis/spec-docs-mvp-generator/requirements.md`

---

## Source Baseline Summary

這個 topic 需要一個 canonical skill `skills/spec-docs-mvp-generator/`，用最小且可控
的方式支援單一 spec 文檔生成。凍結業務邊界如下：

- v1 每次只處理一個明確 `spec-name`
- 只觸及兩個 repo-visible 文檔：
  - `docs/01-specs/<spec-name>.md`
  - `docs/02-spec-relations/data-ownership-map.md`
- 兩份文檔都必須使用固定章節骨架，且不是空檔
- rerun 必須安全，不得覆寫既有 authored content
- 明確排除 `docs/00-overview/architecture-principles.md`、multi-spec maps、
  interfaces、flows、state machines、ADRs、implementation notes
- canonical authority 已凍結為 `skills/`；本 topic 不處理 projection、path migration、
  custom agent 或 runtime orchestration

## Translation Stance

本 spec 採悲觀實作者視角翻譯上述 baseline：

- 假設目標 docs 可能已存在真實作者內容，不能用整檔覆寫當成捷徑
- 假設使用者會 rerun skill 以補漏，而不是只在全新 repo 使用一次
- 假設 repo 治理不接受任何藉由此 topic 偷渡的 path / projection / runtime 變更
- 假設 v1 最小可行實作應優先使用 skill 文檔與模板資產，而不是新增自訂 agent 或執行框架

若後續 implementation 需要：

- 同 topic 修改 `.github/**`、`.codex/**`、`agents/**`
- 為了產生 spec docs 引入 runtime orchestration 或 workflow-to-agent binding
- 對既有 spec 文檔採破壞性整檔重寫
- 把 v1 擴張成 multi-spec、interfaces、flows、state machines、ADRs

則必須 rollback 到 alignment，而不是在 implementation 期間擴 scope。

## Exact Implementation Write Set

未來 implementation topic 只允許在 repo 內 create / modify 這些 canonical skill
artifact：

### Allowed to create

- `skills/spec-docs-mvp-generator/SKILL.md`
- `skills/spec-docs-mvp-generator/reference.md`
- `skills/spec-docs-mvp-generator/examples.md`
- `skills/spec-docs-mvp-generator/templates/spec-template.md`
- `skills/spec-docs-mvp-generator/templates/data-ownership-map-template.md`

### Allowed to modify

- `plan/spec-docs-mvp-generator/spec-docs-mvp-generator.step.md`

### Read-only during implementation

- `analysis/spec-docs-mvp-generator/requirements.md`
- `analysis/spec-docs-mvp-generator/technical-spec.md`
- `AGENTS.md`
- `docs/repo-positioning.md`
- `.github/**`
- `.codex/**`
- `agents/**`
- `README.md`
- `VERSION`

說明：

- 目標 repo 內的 `docs/01-specs/` 與 `docs/02-spec-relations/` 是 skill 執行時寫入面，
  不是此 repo 在 implementation topic 內要新增的固定 artifact。
- `README.md`、`VERSION`、projection surface、release surface 不在此 topic v1 scope。
- `plan/spec-docs-mvp-generator/spec-docs-mvp-generator.step.md` 是後續 planning /
  execution gating artifact，不是本輪 analysis 要產生的檔案。

## Requirement-to-Technical Mapping

| Requirement | Technical realization | Dependencies | Cost / burden | Status |
| --- | --- | --- | --- | --- |
| R1 canonical boundary only | 以 `skills/spec-docs-mvp-generator/` 為唯一實作面；SKILL.md 明寫不碰 projection/runtime/custom agent | repo governance | Low | feasible |
| R2 single-spec v1 output scope | 在 `SKILL.md` 與 `reference.md` 定義 required input `spec-name` 與固定 target write set | skill contract discipline | Low | feasible |
| R3 fixed spec doc skeleton | `templates/spec-template.md` 內凍結 9 個章節與非空 starter prompts | template asset + apply_patch write flow | Low | feasible |
| R4 fixed ownership map skeleton | `templates/data-ownership-map-template.md` 內凍結 5 個章節與固定 table header | template asset + apply_patch write flow | Low | feasible |
| R5 safe rerun / non-destructive update | `reference.md` 定義 merge 規則：缺節補齊、重跑不重複、保留既有內容、禁止整檔清空 | deterministic patch instructions | Medium | feasible |
| R6 local-only generation | skill 僅依賴本地模板與 repo 內容，不引入網路或外部安裝流程 | markdown-only implementation | Low | feasible |
| R7 explicit refusal for excluded outputs | `SKILL.md` + `examples.md` 明列 refusal / reroute patterns | scope guard wording | Low | feasible |
| R8 later `step.md` requirement | 後續 plan 必須建立 `plan/spec-docs-mvp-generator/spec-docs-mvp-generator.step.md`，並逐步列出工作項 | workflow contract | Low | feasible with prerequisite |

## Technical Design

### 1. Skill package structure

建立一個純 canonical skill package：

- `skills/spec-docs-mvp-generator/SKILL.md`
- `skills/spec-docs-mvp-generator/reference.md`
- `skills/spec-docs-mvp-generator/examples.md`
- `skills/spec-docs-mvp-generator/templates/spec-template.md`
- `skills/spec-docs-mvp-generator/templates/data-ownership-map-template.md`

設計理由：

- v1 需求是固定骨架與安全 patch 規則，模板資產足以承載
- 不需要自訂 agent、CLI、runtime orchestration 或 path migration
- 模板可讓 reviewer 直接檢查章節 contract，而不必從長篇 prose 逆向推定

### 2. Input contract

`SKILL.md` 必須要求至少這些輸入：

- `spec-name`：必填；決定 `docs/01-specs/<spec-name>.md`
- 可選背景內容：
  - 問題摘要
  - goals / non-goals
  - actors
  - 已知 data ownership facts
  - open questions

若可選背景不足，skill 仍必須產出非空骨架，但以 starter prompts / placeholder bullets
承載未補齊內容，而不是產出空章節。

若 `spec-name` 缺失，skill 必須 stop and ask，不得猜測檔名。

### 3. Template contracts

### `templates/spec-template.md`

必須固定含有以下章節，順序不可漂移：

1. `Summary`
2. `Problem`
3. `Goals`
4. `Non-goals`
5. `Actors`
6. `Requirements`
7. `Data Ownership Notes`
8. `Acceptance Signals`
9. `Open Questions`

每節至少要有一行 starter 內容，例如：

- 說明句
- `- TODO:` bullets
- seed checklist

禁止空節、禁止只留 heading。

### `templates/data-ownership-map-template.md`

必須固定含有以下章節：

1. `Purpose`
2. `Ownership Table`
3. `Shared or Derived Data`
4. `Boundary Notes`
5. `Open Questions`

`Ownership Table` 必須內含固定表頭：

`| Data Item | System of Record | Upstream Writers | Downstream Readers | Notes |`

且至少要有一行 seed row 或說明文字，避免只留下空表頭。

### 4. Write and merge semantics

future implementation 必須遵守以下 deterministic write 規則：

### First creation

- 若 `docs/01-specs/<spec-name>.md` 不存在，依 `spec-template.md` 建立完整檔案
- 若 `docs/02-spec-relations/data-ownership-map.md` 不存在，依 map template 建立完整檔案
- 必要時可建立 `docs/01-specs/` 與 `docs/02-spec-relations/` 目錄

### Existing file update

- 若目標檔已存在：
  - 保留既有非模板內容
  - 補上缺漏的固定章節
  - 補上缺漏的 ownership table header
  - 不插入重複的固定章節 heading
  - 不因 rerun 清空或覆寫整個檔案

### Partial completion recovery

- 若上一次只完成其中一份文檔，rerun 必須能補齊剩餘檔案
- rerun 後結果必須收斂到同一份固定骨架，不可越跑越多重複章節

這些規則應寫進 `reference.md`，讓 skill 執行者用 `apply_patch` 或等價安全編輯方式
完成，而不是直接整檔覆蓋。

### 5. Refusal and reroute behavior

`SKILL.md` 與 `examples.md` 必須明確處理超範圍請求。

至少要覆蓋以下 refusal / reroute 案例：

- 要求 `docs/00-overview/architecture-principles.md`
- 要求 multi-spec maps
- 要求 interfaces / flows / state machines
- 要求 ADRs
- 要求 implementation notes
- 要求順手做 projection / `.github/**` / `.codex/**` path 切換

技術要求不是「忽略這些需求」，而是要明確告知它們不屬於 v1。

### 6. Validation strategy

此 skill 屬於模板與文檔 contract 類型，v1 不要求額外 CLI 或 automated test harness，
但 implementation 必須提供可重複的人類可驗證檢查面：

- `reference.md` 內列出固定章節 contract
- `examples.md` 至少提供：
  - 全新 spec 生成案例
  - 既有 spec 補缺案例
  - 既有 ownership map 補表頭案例
  - 超範圍拒絕案例
- reviewer 可依模板直接核對輸出是否滿足固定章節與 non-destructive update 規則

若 implementation 想新增 script 或 CLI，會改變 topic 的 cost 與 surface，必須先回滾
到 alignment，而不是在本 topic 直接加碼。

### 7. Planning prerequisite for next role

analysis 完成後，Plan-Creator 必須把以下 artifact 納入後續 planning batch：

- `plan/spec-docs-mvp-generator/spec-docs-mvp-generator.plan.md`
- `plan/spec-docs-mvp-generator/spec-docs-mvp-generator.step.md`

其中 `spec-docs-mvp-generator.step.md` 必須逐步列出至少這些後續工作類別：

1. 建立 skill package 與模板檔
2. 定義 input contract 與 refusal rules
3. 定義 safe rerun / merge 規則
4. 補 examples 與 reviewer 驗證點

這是 workflow prerequisite，不是本輪 analysis 直接執行的內容。

## Architecture-Compliance Self-Check

| Dimension | Result | Note |
| --- | --- | --- |
| `skills/` canonical authority | fits existing architecture | 與 `AGENTS.md`、`docs/repo-positioning.md` 一致 |
| `.github/**` / `.codex/**` projection boundaries | fits existing architecture | topic 不修改 projection surface |
| Workflow-agent boundary | fits existing architecture | 不新增 custom agent 或 workflow-to-agent binding |
| Runtime orchestration boundary | fits existing architecture | v1 為 template-driven skill，無 runtime orchestration |
| Repo-visible doc generation | fits with prerequisites | 依賴後續實作正確使用 `apply_patch` 或等價安全 patch 行為 |
| Required `step.md` gating | fits with prerequisites | 需由 Plan-Creator 在後續 batch 補齊，analysis 本身不產生 |
| Release / README surface | out of scope by design | v1 不處理 release surface |

## Cost of Realization

| Workstream | Complexity | Sequencing | Burden |
| --- | --- | --- | --- |
| 凍結固定模板骨架 | 低 | 必須先完成 | 兩個模板檔即可承載 |
| 撰寫 `SKILL.md` | 低-中 | 依賴模板 contract | 需清楚寫出 input、scope guard、write semantics |
| 撰寫 `reference.md` merge 規則 | 中 | 依賴模板 contract | 需把 non-destructive rerun 規則說清楚 |
| 撰寫 `examples.md` | 中 | 依賴 `SKILL.md` / `reference.md` | 至少 4 類案例 |
| 後續 `step.md` 建立 | 低 | analysis 後進行 | workflow gating，非實作主體 |

總評估：低到中等複雜度。主要風險不在程式，而在於是否把固定骨架與安全 rerun
規則寫得足夠清楚，讓 implementer 與 reviewer 不需要靠聊天補完。

## Conflicts and Rollback Triggers

以下情況屬於 material conflict，應 rollback 到 alignment：

1. 後續 implementation 想把 v1 擴成 multi-spec batch 或新增第三份文檔
2. 後續 implementation 主張必須修改 `.github/**`、`.codex/**` 或 `agents/**`
3. 後續 implementation 無法承諾 non-destructive rerun，只能整檔覆寫
4. 後續 implementation 認為需要 CLI / runtime orchestration 才能完成 v1

對應的 rollback note：

- failing business assumption: v1 只需兩份固定骨架文檔與安全補齊即可成立
- contradictory technical claim: 需要額外 surface、runtime、或 destructive rewrite
- renegotiation needed: 是否接受 scope 擴張；若否，維持本 spec 的模板型實作路線

## Handoff

此 technical spec 已足以交給後續 `Plan-Creator`。

Plan-Creator 進下一階段時必須：

- 保持 scope 嚴格鎖在 canonical skill `skills/spec-docs-mvp-generator/`
- 建立 `plan/spec-docs-mvp-generator/spec-docs-mvp-generator.step.md`
- 讓 `step.md` 逐步列出每個 implementation / review step 的處理事項
- 不把本 topic 擴成 projection、runtime、workflow binding 或 broader design-doc suite
