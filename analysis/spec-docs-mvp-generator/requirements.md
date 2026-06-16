# Requirements: spec-docs-mvp-generator

**Status**: FROZEN  
**Topic**: `spec-docs-mvp-generator`  
**Date**: 2026-06-16

---

## Problem Statement

本 repo 已有明確的 canonical source 邊界與 workflow 治理，但目前沒有一個
canonical skill 能穩定產出 v1 所需的最小 spec 文檔集合。缺少這個能力時，
每次起草 spec 都容易發生以下問題：

- 產出路徑不一致，repo-visible 文檔落在錯誤位置
- 檔案只有空標題或空白骨架，後續作者仍需重新發明章節結構
- scope 擴張到 architecture principles、multi-spec maps、interfaces、
  flows、state machines、ADRs、implementation notes
- topic 一邊做技能設計，一邊重開 canonical / projection / path 決策

此 topic 的需求基線只凍結 analysis layer，為後續建立
`skills/spec-docs-mvp-generator/` 提供可執行的邊界，不進入 plan 或實作。

## Actors

| Actor | Role |
| --- | --- |
| Repo author / operator | 需要為單一 spec 建立 repo-visible 起始文檔 |
| Main Agent | 依 skill 合約在正確路徑建立或補齊文檔 |
| Creator / implementer | 後續只在 `skills/spec-docs-mvp-generator/` 內實作 canonical skill |
| Reviewer | 驗證 skill 產出是否守住固定骨架、範圍邊界與非破壞性更新規則 |
| Plan-Creator | 在 analysis 完成後建立後續 plan 與必需的 `*.step.md` |

## Frozen Requirements

### R1 — Canonical skill boundary only

後續 implementation topic MUST 只以 canonical skill
`skills/spec-docs-mvp-generator/` 為實作目標，不得把此 topic 擴成 custom
agent、runtime orchestration、workflow-to-agent binding、projection /
cutover / path migration，亦不得重開 `skills/` vs `.github/**` /
`.codex/**` 的 authority 決策。

- Actor: Creator / implementer
- Condition: 後續 plan 或 implementation 開始
- Observable: topic 的新增實作主要落在 `skills/spec-docs-mvp-generator/`
  及其直接支援資產；沒有把 scope 擴到 `agents/`、`.github/**`、`.codex/**`
  或 workflow runtime surface
- Acceptance: implementation 可被 reviewer 判定為「canonical skill topic」
  而非 path/projection/runtime topic
- Failure meaning: topic 失去邊界，後續 plan 不再可審核

### R2 — Single-spec v1 output scope

v1 每次執行 MUST 只支援一個明確 `spec-name`，並且只以這兩個 repo-visible
輸出為目標：

1. `docs/01-specs/<spec-name>.md`
2. `docs/02-spec-relations/data-ownership-map.md`

v1 MUST NOT 同時產出或更新任何其他 spec 文檔類型。

- Actor: Repo author / operator, Main Agent
- Condition: skill 以單一 `spec-name` 被呼叫
- Observable: 目標 write set 只包含上述兩個路徑
- Acceptance: 不產生 `docs/00-overview/architecture-principles.md`、multi-spec
  maps、interfaces、flows、state machines、ADRs、implementation notes
- Failure meaning: spec 產生器不再是 MVP，並且會擴大 review 與維護範圍

### R3 — Fixed `docs/01-specs/<spec-name>.md` skeleton with non-empty starter content

`docs/01-specs/<spec-name>.md` MUST 使用固定章節骨架，且每個章節都必須帶有
非空的起始文字、提示句或 starter bullets，不可只留空標題。固定章節集凍結為：

1. `Summary`
2. `Problem`
3. `Goals`
4. `Non-goals`
5. `Actors`
6. `Requirements`
7. `Data Ownership Notes`
8. `Acceptance Signals`
9. `Open Questions`

- Actor: Repo author / operator
- Condition: 目標 spec 文檔首次建立，或既有檔案缺少必要章節時
- Observable: 檔案存在、章節順序固定、每節至少有一行 starter 內容
- Acceptance: reviewer 可直接看見完整骨架，不需再補發明章節名稱；檔案不是
  空白模板
- Failure meaning: 後續作者仍要自行設計骨架，skill 無法提供穩定起點

### R4 — Fixed `data-ownership-map.md` skeleton with non-empty starter content

`docs/02-spec-relations/data-ownership-map.md` MUST 使用固定章節骨架，且每個章節
都必須帶有非空 starter 內容。固定章節集凍結為：

1. `Purpose`
2. `Ownership Table`
3. `Shared or Derived Data`
4. `Boundary Notes`
5. `Open Questions`

其中 `Ownership Table` MUST 至少包含一個固定欄位表頭：

`Data Item | System of Record | Upstream Writers | Downstream Readers | Notes`

- Actor: Repo author / operator
- Condition: map 文檔首次建立，或既有檔案缺少必要章節 / 表頭時
- Observable: 檔案存在、章節順序固定、table header 存在、各節非空
- Acceptance: reviewer 可以據此直接開始填 ownership facts，不需要再補定義欄位
- Failure meaning: data ownership 關聯仍停留在口頭描述，無統一承載面

### R5 — Safe rerun and non-destructive update rule

若目標檔已存在，v1 MUST 採安全 rerun 規則：保留既有使用者內容，補齊缺漏的
固定章節或表頭，不得因 rerun 而清空既有內容，也不得重複插入同名章節。

- Actor: Main Agent
- Condition: 目標 spec 文檔或 map 文檔已存在，或上一次執行中途被中斷
- Observable: rerun 後既有內容仍存在；缺漏骨架被補齊；同名固定章節不重複
- Acceptance: 第二次執行是 idempotent；中斷後可繼續收斂到固定骨架
- Failure meaning: skill 會破壞已寫內容，無法安全用於真實 repo

### R6 — Local-only generation with no external dependency

v1 MUST 只依賴 repo 內現有上下文與本地模板能力，不能要求網路抓取、外部服務、
runtime orchestration 或額外平台安裝流程才能產生上述兩份文檔。

- Actor: Repo author / operator
- Condition: 在一般 worktree 或本地 repo 內離線執行
- Observable: 兩份目標文檔可在無網路條件下被建立或補齊
- Acceptance: external dependency unavailable 不會改變文檔骨架或 scope
- Failure meaning: skill 無法作為 canonical repo skill 穩定重用

### R7 — Out-of-scope requests must be refused, not approximated

當輸入要求超出 v1 邊界時，skill MUST 明確拒絕或導回後續 topic，而不是以
「接近的章節」或「順手多做一點」方式偷偷擴張輸出。明確排除項包括：

- `docs/00-overview/architecture-principles.md`
- multi-spec maps
- interfaces
- flows
- state machines
- ADRs
- implementation notes

- Actor: Main Agent, Reviewer
- Condition: 使用者要求任何超出 v1 的文檔或章節
- Observable: skill 說明與 examples 對超範圍請求有拒絕或 reroute 規則
- Acceptance: 實際輸出仍只限 R2 規定的兩個檔案與其固定章節
- Failure meaning: v1 邊界被軟化，topic 失去 MVP 可控性

### R8 — Follow-up workflow artifact requirement for later planning

本 topic 在 analysis 後交給 Plan-Creator 時，後續 planning batch MUST 視
`plan/spec-docs-mvp-generator/spec-docs-mvp-generator.step.md` 為必備 artifact，
且該檔必須逐步列出每個 step 要處理的事項；analysis round 本身則 MUST NOT
產生任何 `plan/` 或 `*.step.md` artifact。

- Actor: Plan-Creator
- Condition: analysis 完成後進入後續 planning workflow
- Observable: analysis layer 只產出 `requirements.md` 與 `technical-spec.md`；
  後續 plan 階段另行建立 `*.step.md`
- Acceptance: implementation workflow 開始前存在 repo-visible `step.md`，且其內容
  具備逐步工作項
- Failure meaning: workflow progression 失去 repo-visible gate，或 analysis topic
  越界進入 planning artifact 產生

## Non-goals

- 不在此 topic 設計 `docs/00-overview/architecture-principles.md`
- 不在 v1 支援 multi-spec maps 或跨多 spec 的 inventory
- 不在 v1 產出 interfaces、flows、state machines、ADRs、implementation notes
- 不在此 analysis round 產生 `plan/spec-docs-mvp-generator/*.plan.md`
  或 `*.step.md`
- 不在此 topic 重寫 canonical/path/projection 治理
- 不把此 skill topic 擴成 custom agent、runtime orchestration 或 workflow binding

## Extreme-Boundary Checks

### No network / degraded external dependency

- v1 需求不依賴網路、外部 API、遠端模板倉庫或安裝器。
- 在完全離線環境下，固定章節骨架與 starter 內容仍必須可產生。

### Wrong user role / missing approval

- 若輸入要求超出 v1 scope，skill 不得自行升級權限或多寫其他檔案。
- 缺少必要 `spec-name` 時不得猜測目標檔名並寫入錯誤路徑。

### Interrupted / partial completion

- 若第一次只建立了其中一份文檔，rerun 必須能補齊另一份並保留已存在內容。
- 不得因部分完成而把後續 rerun 視為 destructive rewrite。

### Low-volume / peak-volume

- v1 不支援單次 multi-spec 批次處理；高量情境只能以多次單 spec 執行處理。
- 單次執行的行為模型不因 spec 規模大小而改變固定骨架或輸出路徑。

## Resolved Contradictions

### C1 — Fixed skeleton vs author freedom

- Conflict: 固定骨架能降低 drift，但過度剛性可能限制後續作者補充內容
- Resolution: 凍結固定章節名稱與順序，但章節內文允許後續自由編修；rerun 只補缺漏，
  不重寫既有內容

### C2 — Shared ownership map vs per-spec isolation

- Conflict: spec 文檔是 per-spec 檔案，但 data ownership map 是共用關聯面
- Resolution: v1 凍結為單一共享 `docs/02-spec-relations/data-ownership-map.md`，
  不額外建立 per-spec ownership map

### C3 — MVP usefulness vs scope explosion

- Conflict: 使用者可能會順勢要求更多 architecture 或 design artifacts
- Resolution: v1 只保證兩份文檔與固定骨架；其他 artifact 全數明確排除

### C4 — Canonical implementation vs projection pressure

- Conflict: skill 可能被要求同時處理 `.github/**`、`.codex/**` 或其他 surface
- Resolution: 此 topic 只定義 canonical `skills/` skill；projection 與 path migration
  屬於後續獨立 topic

## Explicit Assumptions

- A1: `spec-name` 會由呼叫端明確提供，並作為 `docs/01-specs/<spec-name>.md`
  的目標檔名基準
- A2: 目標 repo 允許建立 `docs/01-specs/` 與 `docs/02-spec-relations/` 路徑，若不存在，
  後續實作可建立目錄
- A3: fixed skeleton 的 starter 內容可以是提示句、待填 bullet 或 seed table，
  不要求 analysis 階段先凍結真實 spec 內容
- A4: 後續 Plan-Creator 會依 repo workflow 要求補上 `*.step.md`，而不是要求 analysis
  直接越界產生

## Success Signals

此 topic 的需求基線可交給 technical translation，當且僅當：

1. v1 支援路徑被明確凍結為兩個 docs 輸出
2. 兩份文檔的固定章節骨架已被明確命名，且要求非空 starter 內容
3. scope exclusions 與 canonical boundary 已被明確凍結
4. rerun / partial completion / offline 邊界已被明確定義
5. 後續 `step.md` requirement 已被記錄為 planning 前置條件，但 analysis 自身未越界產生 plan artifact
