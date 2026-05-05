# Requirements: Python Implementation Workflow SDD/TDD Supplement

**Status**: frozen — ready for technical translation
**Topic**: `python-implementation-workflow-sdd-tdd`
**Depends on**: `python-implementation-workflow` (PR #48, v0.38.0)

---

## Problem Statement

PR #48 建立了可執行的 4-skill Python 實作流程，但仍缺乏以下三個防禦機制，
導致 Agent 出貨快但人腦跟不上：

1. **Codebase blindness**：`python-plan-authoring` 允許在未看過 codebase 的情況下撰寫 plan，造成「只改 spec 不看 code」。
2. **No RED before GREEN**：缺乏「先寫失敗測試，再實作」的正式 skill，讓 AI executor 可以「出貨但測試不存在或事後補」。
3. **Atomic commit 無規範**：commit 順序不明確，導致 review 無法追蹤 plan → test → impl 的時序。

---

## Actors

| Actor | 角色 | 權限 |
|-------|------|------|
| **Python developer** | 觸發整個 workflow 的主使用者 | 可觸發任何 skill |
| **Executor agent** | 根據 approved plan 實作，先執行 TDD skill | 只能執行 plan 明確授權的工作 |
| **TDD author** | 根據 plan 的 Requirements + Public Contract 撰寫 RED tests | 不得修改 production code |
| **Plan reviewer** | 擋下缺乏 codebase evidence 的非 trivial plan | 輸出 `approved` / `needs-rework` |
| **Implementation reviewer** | 驗證 TDD 流程是否被遵守（若 plan 要求） | 輸出 `approved` / `needs-rework` |

---

## Frozen Decisions

### D1 — Behavior Change Classifier（觸發 TDD 的量測規則）

```yaml
trivial:
  - comment change
  - formatting only
  - internal variable rename (no external reference)
  - docstring change only

non_trivial:
  - public API signature change
  - function/class rename (externally referenced)
  - change in return value or type
  - validation logic change
  - parsing or transformation logic change
  - error handling behavior change
  - side effect change (I/O, DB, network)

rule:
  if any non_trivial condition is true → TDD required
  else → TDD optional
```

### D2 — Codebase Evidence Levels（「足夠」的量測標準）

```yaml
insufficient:
  - no files listed
  - files listed but unrelated to task
  consequence: must return needs-rework

minimal:
  - at least 1 relevant file listed
  - no interface or behavior described
  acceptable_for: new feature only (no existing behavior change)

sufficient:
  - relevant files listed
  - existing interfaces identified OR explicitly stated "no existing interface found"
  - current behavior described
  consequence: pass

rule:
  if modifying existing behavior → require sufficient
  if new feature only → minimal acceptable
```

### D3 — Atomic Commit Enforcement Level

```yaml
default_mode: recommendation

strict_mode:
  enabled_by: explicit repo policy or plan flag
  implementation_review_behavior:
    - verify commit order: RED test → GREEN impl
    - violation → needs-rework

recommendation_mode:
  implementation_review_behavior:
    - check if test mapping exists
    - do not fail on commit order alone
```

### D4 — RED Test Unexpectedly Passes

```yaml
if test passes before implementation:
  classify_as: pass_existing
  require_explanation:
    - which existing behavior satisfies the test
    - why no new code is needed OR
    - why the test is still valuable as regression
  not_a_failure: true
```

### D5 — Rollout Strategy（分階段避免破壞 stable skills）

```yaml
phase_1:
  type: additive only
  artifacts:
    - python-tdd-test-authoring (new skill)
    - behavior change classifier (reference in skill)
    - evidence levels (reference in skill)
    - atomic commit order doc (reference in skill)
  version: 0.38.0 → 0.40.0

phase_2:
  type: modify stable skills
  artifacts:
    - python-plan-authoring (codebase evidence section + template v2)
    - python-plan-review (evidence gate)
  requires: phase_1 merged
  version: 0.40.0 → 0.41.0

phase_3:
  type: modify stable skill (depends on phase 2 adoption)
  artifacts:
    - python-implementation-review (TDD evidence check)
  requires: phase_2 merged
  version: 0.41.0 → 0.42.0
```

### D6 — Template Versioning（向後相容策略）

```yaml
template_v1: deprecated (no codebase evidence required)
template_v2: current (codebase evidence required for existing behavior changes)

plan_review_behavior:
  if template_version == v1 or unknown: warn (not fail)
  if template_version == v2: enforce strictly
```

### D7 — TDD Skill Complexity Level

```yaml
complexity: medium-high
required_artifacts:
  - SKILL.md
  - examples.md
  - checklist.md
reason:
  - 3 verdict paths (red-tests-ready / needs-rework / insufficient-context)
  - test_mapping YAML output
  - production_code_modified guard
  - strict scope boundary
```

### D8 — Out of Scope (All Phases)

```text
- sdd-state-machine.md → future topic (router skill upgrade)
- 強制 40–100 題逼問 → rejected (reduces usability)
- 巨大 python-sdd-workflow skill → rejected (single responsibility violated)
- 把 TDD、implementation、review 混在同一個 skill → rejected
```

---

## Measurable Requirements

### R1 — python-tdd-test-authoring（新 skill）

| Element | Requirement |
|---------|-------------|
| Actor | TDD author agent / developer |
| Trigger condition | Plan approved + D1 classifier returns `non_trivial` |
| Observable result | 輸出 `test_mapping` YAML，每個 Requirement / Public Contract 有對應 test case |
| Guard | `production_code_modified: false` 必須為 true |
| Metric | 缺少任何 5 種測試類別（happy/invalid/edge/regression/backward）→ needs-rework |
| Failure meaning | Executor 在無 RED tests 的情況下直接實作，測試成為事後補丁 |

### R2 — Codebase Evidence Gate（Phase 2：python-plan-review）

| Element | Requirement |
|---------|-------------|
| Actor | Plan reviewer |
| Trigger condition | plan modifies existing code + `sufficient` evidence not present |
| Observable result | `needs-rework` verdict |
| Metric | level == `insufficient` for any existing-behavior change → always block |
| Failure meaning | Executor 在未了解現有 codebase 的情況下按 plan 實作，造成 regression |

### R3 — TDD Evidence Check（Phase 3：python-implementation-review）

| Element | Requirement |
|---------|-------------|
| Actor | Implementation reviewer |
| Trigger condition | Plan required TDD (D1 classifier = non_trivial) |
| Observable result | 驗證 `test_mapping` 存在且測試對應 Requirements / Public Contract |
| Metric | `recommendation` mode → warn if missing; `strict` mode → needs-rework |
| Failure meaning | 聲稱符合 plan，但 RED tests 不存在或不對應 |

### R4 — 不破壞 PR #48 四個 skill 的責任邊界

```text
python-plan-review:    只新增 evidence gate（phase 2）；不改現有 verdict logic
python-plan-authoring: 只新增 codebase evidence section（phase 2）；不改 13 節結構
python-implementation-review: 只新增 TDD evidence check（phase 3）；不改 traceability logic
python-code-review:    不修改（code quality skill 不需 SDD/TDD 知識）
```

---

## Acceptance Criteria

```text
Phase 1 完成：
[ ] python-tdd-test-authoring skill 存在且通過 agent-skill-reviewer
[ ] TDD skill 明確禁止修改 production code
[ ] TDD skill 的 test_mapping 覆蓋全部 5 種測試類別
[ ] Behavior change classifier 記錄在 skill reference 中
[ ] Evidence levels 記錄在 skill reference 中
[ ] Atomic commit order 記錄在 skill reference 中
[ ] README +1 row, VERSION 0.38.0 → 0.40.0

Phase 2 完成（independent topic）：
[ ] python-plan-authoring 要求 non-trivial change 提供 sufficient codebase evidence
[ ] python-plan-review 能擋下 insufficient evidence 的 non-trivial plan
[ ] template v2 存在（包含 Codebase Evidence 子節）
[ ] v1 plan 在 review 時觸發 warn 而非 fail

Phase 3 完成（independent topic）：
[ ] python-implementation-review 在 strict mode 驗證 RED test commit 早於 GREEN
[ ] 在 recommendation mode 只警告不 block
```
