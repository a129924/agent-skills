# python-implementation-workflow-sdd-tdd

## Goal / Outcome

在 PR #48 的 4-skill Python 實作流程上補強 SDD/TDD 機制，Phase 1 僅新增一個 skill：

```
python-tdd-test-authoring
```

使完整 workflow 升級為：

```
python-plan-authoring
→ python-plan-review
→ python-tdd-test-authoring  ← NEW（non_trivial changes only）
→ implementation executor
→ python-implementation-review
→ python-code-review
```

完成時，`.github/skills/` 下新增 1 個符合 repo 規範的 stable skill 資料夾，
`README.md` 新增 1 行，`VERSION` 從 `0.38.0` bump 至 `0.40.0`。

---

## Scope

**In scope（Phase 1）**:
- `.github/skills/python-tdd-test-authoring/` — 新增
  - `SKILL.md`
  - `examples.md`（medium-high complexity skill，必要）
  - `checklist.md`（gatekeeping skill，必要）
  - `references/behavior-change-classifier.md`
  - `references/codebase-evidence-levels.md`
  - `references/atomic-commit-order.md`
- `README.md` — Current skills 表格新增 1 行
- `VERSION` — `0.38.0` → `0.40.0`

**Out of scope（Phase 1，屬於後續獨立 topic）**:
- `python-plan-authoring` 的修改 → Phase 2 topic: `python-plan-sdd-evidence`
- `python-plan-review` 的修改 → Phase 2 topic: `python-plan-sdd-evidence`
- `python-implementation-review` 的修改 → Phase 3 topic: `python-implementation-tdd-check`
- `sdd-state-machine.md` → future topic
- 任何現有 skill（PR #48 產出）的修改

---

## Locked Decisions

參見 `analysis/python-implementation-workflow-sdd-tdd/requirements.md`（D1–D8）

關鍵決策摘要：

| 決策 | 結論 |
|------|------|
| TDD 觸發量測 | D1 Behavior Change Classifier（trivial/non_trivial 明確規則） |
| Codebase evidence「足夠」標準 | D2 三級制（insufficient/minimal/sufficient） |
| Atomic commit enforcement | D3 recommendation by default（strict 為 opt-in） |
| RED test 意外通過 | D4 classify as `pass_existing`，必須附解釋 |
| Rollout 策略 | D5 Phase 1 additive only；Phase 2-3 分開 topic |
| Template versioning | D6 v1（warn）→ v2（enforce）向後相容 |
| TDD skill artifact set | D7 SKILL.md + examples.md + checklist.md（medium-high） |
| 排除項目 | D8 sdd-state-machine / 巨大 SDD skill / 混合 skill |

---

## Boundaries / Exclusions

- Phase 1 不修改任何 PR #48 已 merge 的 stable skill
- `python-tdd-test-authoring` 只負責「approved plan → RED tests」，不實作 production code，不審查 code quality
- skill 的 verdict logic 只輸出三種結果：`red-tests-ready` / `needs-rework` / `insufficient-context`
- D1 classifier 和 D2 evidence levels 記錄在 skill 的 `references/`，不重複寫入 SKILL.md 正文

---

## Status / Allowed Transitions

- **Current**: `planned`
- **Execution model**：canonical creator → reviewer → publish → merge path
- **Allowed transitions**:
  - `planned` → `creator-in-progress`
  - `creator-in-progress` → `review-ready`
  - `review-ready` → `reviewer-in-progress`
  - `reviewer-in-progress` → `approved`
  - `reviewer-in-progress` → `needs-rework`
  - `needs-rework` → `creator-in-progress`
  - `approved` → `publish-in-progress`
  - `publish-in-progress` → `merged`

---

## Artifact Paths

```text
.github/skills/python-tdd-test-authoring/SKILL.md
.github/skills/python-tdd-test-authoring/examples.md
.github/skills/python-tdd-test-authoring/checklist.md
.github/skills/python-tdd-test-authoring/references/behavior-change-classifier.md
.github/skills/python-tdd-test-authoring/references/codebase-evidence-levels.md
.github/skills/python-tdd-test-authoring/references/atomic-commit-order.md
README.md (line ~189: +1 row)
VERSION (0.38.0 → 0.40.0)
```

---

## Creator Input Contract

```text
Skill name:     python-tdd-test-authoring
Complexity:     medium-high
Responsibility: Create RED tests from an approved Python implementation plan before implementation begins.

Trigger:
  - python-plan-review returned `approved`
  - D1 classifier detects non_trivial change in plan

Skip when:
  - plan covers D1 trivial changes only
  - plan is docs / VERSION / formatting / Agent Skill 文件小修

Required outputs:
  - SKILL.md with 3-verdict output (red-tests-ready / needs-rework / insufficient-context)
  - examples.md with 5 scenarios (see T1.2 in technical-spec.md)
  - checklist.md with 9-item gate (see T1.3 in technical-spec.md)
  - references/ with 3 split files (behavior-change-classifier / codebase-evidence-levels / atomic-commit-order)

Hard boundaries:
  - never modify production code
  - never loosen assertions to make tests pass
  - never invent public API beyond approved plan
  - refuse if plan is not approved

Output YAML schema: see technical-spec.md T1.1
```

---

## Reviewer Gate

After creator completes, route to `/fleet @.github/skills/agent-skill-reviewer/` with:

```text
Review .github/skills/python-tdd-test-authoring/ for:
- SKILL.md has all required sections (Purpose / Trigger / Inputs / Process / Examples / Outputs / Boundaries / Local references)
- examples.md covers 5 required scenarios
- checklist.md covers 9 required checks
- references/ has all 3 split files with declared roles in SKILL.md Local references
- production_code_modified guard is explicit
- D1 trigger rule is unambiguous
- Boundaries section explicitly covers all 4 hard constraints
```

---

## Publish Checklist

```text
[ ] python-tdd-test-authoring/ passes agent-skill-reviewer
[ ] README.md +1 row (python-tdd-test-authoring | Create RED tests from approved plan before implementation)
[ ] VERSION 0.38.0 → 0.40.0
[ ] git commit with topic scope
[ ] branch feat/andrew/python-implementation-workflow-sdd-tdd
[ ] PR targets dev
[ ] STOP POINT 1: human approval before commit
[ ] STOP POINT 2: hard stop after PR creation, wait for human merge confirmation
```

---

## Dependent Future Topics

```text
Phase 2 → python-plan-sdd-evidence
  - python-plan-authoring: add codebase evidence section + template v2
  - python-plan-review: add evidence gate (D2 levels)

Phase 3 → python-implementation-tdd-check
  - python-implementation-review: add TDD evidence check (D3 enforcement modes)

Future → sdd-state-machine (out of current roadmap)
  - router skill upgrade: requirements-ready → plan-approved → tdd-required → implementation-ready
```

---

## Analysis Layer Reference

```text
analysis/python-implementation-workflow-sdd-tdd/requirements.md  — frozen business baseline (D1–D8 + R1–R4)
analysis/python-implementation-workflow-sdd-tdd/technical-spec.md — technical mapping + feasibility + PR strategy
```

Plan-creator must operate in **strict mode**: all scope, artifact paths, and implementation steps
must map 100% to technical-spec.md. No self-healing or gap-filling allowed.
