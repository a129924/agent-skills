# Technical Spec: Python Implementation Workflow SDD/TDD Supplement

**Status**: frozen — ready for plan authoring
**Topic**: `python-implementation-workflow-sdd-tdd`
**Source requirements**: `analysis/python-implementation-workflow-sdd-tdd/requirements.md`

---

## Architecture Compliance Check

### Existing skill surfaces (must not break)

| Skill | Stable since | Phase 1 touch | Phase 2 touch | Phase 3 touch |
|-------|-------------|---------------|---------------|---------------|
| `python-plan-authoring` | v0.38.0 | ❌ no touch | ✅ add evidence section | ❌ no touch |
| `python-plan-review` | v0.38.0 | ❌ no touch | ✅ add evidence gate | ❌ no touch |
| `python-implementation-review` | v0.38.0 | ❌ no touch | ❌ no touch | ✅ add TDD check |
| `python-code-review` | v0.38.0 | ❌ no touch | ❌ no touch | ❌ no touch |

### Repo policy compliance

- Each phase is a separate topic → separate creator → reviewer → publish → PR cycle
- Phase 1 is purely additive: no existing skill modified → low risk
- Phase 2 modifies 2 stable skills → must re-run agent-skill-reviewer for both
- Phase 3 modifies 1 stable skill → must re-run agent-skill-reviewer

---

## Phase 1 Technical Tasks

### T1.1 — Create `python-tdd-test-authoring/SKILL.md`

**Complexity**: medium-high  
**Required sections**: Purpose / Trigger / Inputs / Process / Examples / Outputs / Boundaries / Local references

**Trigger logic** (must reference D1 classifier):
```text
Use when:
- python-plan-review has returned `approved`
- plan contains any D1 non_trivial change indicator

Skip when:
- plan covers only D1 trivial changes
- plan is docs / VERSION / formatting only
```

**Process steps** (must enforce):
1. Confirm plan is approved (refuse if not)
2. Run D1 classifier against plan content
3. If trivial → output `skip_with_reason` verdict, not an error
4. Read Requirements, Public Contract, Non-goals, Test Plan sections
5. Inspect existing test structure and project test conventions
6. Create tests covering all 5 categories (happy / invalid / edge / regression / backward_compat)
7. For each test: set `expected_initial_status` (fail / pass_existing / skip_with_reason)
8. If `pass_existing`: add explanation of which existing behavior satisfies it
9. Verify `production_code_modified: false`
10. Output `test_mapping` YAML + validation command

**Output YAML schema**:
```yaml
verdict: red-tests-ready | needs-rework | insufficient-context

test_mapping:
  - requirement: "<requirement text>"
    test_file: "tests/..."
    test_case: "test_..."
    expected_initial_status: fail | pass_existing | skip_with_reason
    pass_existing_reason: "<if pass_existing: explain>"

production_code_modified: false

validation_command: "pytest ..."
```

**Boundaries** (hard):
- Never modify production code
- Never loosen assertions to make tests pass
- Never invent public API beyond the approved plan
- Never skip regression tests when behavior is changed
- Refuse if plan is not `approved`

### T1.2 — Create `python-tdd-test-authoring/examples.md`

Required scenarios:
1. `non_trivial` → full `red-tests-ready` output with complete `test_mapping`
2. `trivial` → `skip_with_reason` output (valid, not a failure)
3. `pass_existing` case → how to document pre-passing test
4. `needs-rework` case → incomplete plan (missing Public Contract)
5. `insufficient-context` → plan not approved yet, skill refuses

### T1.3 — Create `python-tdd-test-authoring/checklist.md`

Required checks:
```text
[ ] D1 classifier ran: is this trivial or non_trivial?
[ ] All Requirements mapped to tests
[ ] Public Contract fully covered
[ ] Non-goals respected (no tests for out-of-scope behavior)
[ ] 5 test categories present: happy / invalid / edge / regression / backward_compat
[ ] expected_initial_status set for every test
[ ] pass_existing tests have explanation
[ ] production_code_modified: false confirmed
[ ] validation_command provided
```

### T1.4 — Create `python-tdd-test-authoring/references/`

Split reference files (3 topics → use references/ instead of single reference.md):

| File | Purpose |
|------|---------|
| `behavior-change-classifier.md` | D1 trivial vs non_trivial classification rules and examples |
| `codebase-evidence-levels.md` | D2 insufficient / minimal / sufficient definitions |
| `atomic-commit-order.md` | Recommended commit order, enforcement level (recommendation vs strict) |

### T1.5 — README + VERSION

```text
README: +1 row → python-tdd-test-authoring | Create RED tests from approved plan before implementation
VERSION: 0.38.0 → 0.39.0
```

---

## Phase 2 Technical Tasks (Separate Topic Plan)

> **Note**: Phase 2 requires its own topic plan after Phase 1 is merged.
> Listed here for completeness only — not part of current execution.

### T2.1 — Modify `python-plan-authoring/SKILL.md`

Add to Process:
```markdown
## Codebase Exploration Requirement

Before drafting a plan that modifies existing behavior:
1. Identify relevant files/modules using D1 classifier
2. Inspect existing public interfaces
3. Document in `Current Context > Codebase Evidence` subsection
4. If relevant files cannot be identified → stop and ask

Required evidence for non_trivial changes:
- Inspected files listed
- Existing interfaces identified (or "no existing interface found")
- Current behavior described
- Conventions to preserve noted
```

### T2.2 — Update `python-plan-authoring/templates/python-plan-template.md` → v2

Add `Codebase Evidence` subsection under `Current Context`:
```markdown
### Codebase Evidence
- Inspected files:
  - src/...
  - tests/...
- Existing interfaces:
  - ...
- Current behavior:
  - ...
- Conventions to preserve:
  - ...
```

### T2.3 — Modify `python-plan-review/SKILL.md` + `checklist.md`

Add evidence gate to Process:
```markdown
## Codebase Evidence Gate

Return `needs-rework` when:
- plan contains D1 non_trivial change AND
- `Current Context` has no inspected files listed, OR
- `Current Context` lists files unrelated to the task, OR
- existing interfaces are not identified (without explicit "no existing interface")

Evidence level required:
- modifying existing behavior → sufficient
- new feature only → minimal acceptable
```

---

## Phase 3 Technical Tasks (Separate Topic Plan)

> **Note**: Phase 3 requires its own topic plan after Phase 2 is merged.

### T3.1 — Modify `python-implementation-review/SKILL.md`

Add TDD evidence check:
```markdown
## TDD Evidence Check

If the plan required TDD (D1 classifier = non_trivial):

In recommendation mode (default):
- Check if test_mapping exists
- If missing → warn but do not fail

In strict mode (repo policy opt-in):
- Verify test_mapping exists and covers Requirements + Public Contract
- If commit history available: verify RED test commit precedes GREEN impl
- Violation → needs-rework
```

---

## Feasibility Assessment

### Risk: Phase 2 has breaking change potential

**Concern**: Adding codebase evidence as a required section may break
users who have existing `*.plan.md` files authored with template v1.

**Mitigation**: Template v2 is additive (new subsection under Current Context,
not a new required top-level section). Plan review in transition period: treat
absent evidence in v1 plans as `warn`, not `fail`.

### Risk: Behavior Change Classifier is subjective at edges

**Concern**: "very small rename" — is renaming a public function trivial?

**Decision**: D1 classifier rule is explicit: any function/class rename that
is externally referenced = non_trivial. The key test is "external reference",
not "size of rename". This resolves the ambiguity.

### Cost of rework for Phase 2

Both `python-plan-authoring` and `python-plan-review` were just approved in
v0.38.0. Re-opening them for Phase 2 means:
- Each needs a separate creator cycle + reviewer approval
- Reviewer must treat them as first-class reviews (not "small patches")
- Estimated: 2 creator runs + 2 reviewer runs per skill = 4 fleet agents for Phase 2

### Rollback trigger

If Phase 2 codebase evidence gate generates excessive `needs-rework` for
valid plans (false positive rate > 20%), roll back to `warn` enforcement
for all evidence levels until the classifier is refined.

---

## PR Strategy

| PR | Topic Plan | Content | VERSION |
|----|-----------|---------|---------|
| Phase 1 PR | `python-implementation-workflow-sdd-tdd` | New `python-tdd-test-authoring` + refs | `0.38.0 → 0.40.0` |
| Phase 2 PR | `python-plan-sdd-evidence` (new topic) | Modify plan-authoring + plan-review | `0.40.0 → 0.41.0` |
| Phase 3 PR | `python-implementation-tdd-check` (new topic) | Modify implementation-review | `0.41.0 → 0.42.0` |

---

## What Is Intentionally Excluded

```text
sdd-state-machine.md        → future topic: converts router skill to state machine
python-sdd-workflow skill   → rejected: single responsibility violated
forced 40-100 question loop → rejected: reduces usability
mixing TDD + review in one  → rejected: semantic boundary violation
```
