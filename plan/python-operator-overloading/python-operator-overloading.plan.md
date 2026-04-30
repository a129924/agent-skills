# Python Operator Overloading Skill Plan

> **Strict Mode** — both analysis-layer artifacts exist and outrank chat-time
> instructions unless a human explicitly says `override`.
>
> Analysis inputs:
> - `analysis/python-operator-overloading/requirements.md` (FROZEN, 2026-04-30)
> - `analysis/python-operator-overloading/technical-spec.md` (READY FOR PLAN
>   CREATION, 2026-04-30)
>
> This plan maps 100% to `analysis/python-operator-overloading/technical-spec.md`.
> No self-healing, no gap-filling, no silent scope additions.

---

## Goal / Outcome

Create a repo-visible stable skill at
`.github/skills/python-operator-overloading/` that teaches Python developers:

- when to overload an operator versus keeping an explicit named method
- how to implement the two-sided dispatch protocol correctly
  (`__add__` / `__radd__`, `return NotImplemented` vs `raise TypeError`)
- how in-place operators must return `self` or a new object (never `None`)
- how unary operators must be pure and return a new object
- how comparison and ordering operators must align semantically with `__eq__`
- when `@functools.total_ordering` completes the ordering contract

The completed topic should produce a review-ready skill backed by 8 explicitly
traceable requirements (R1–R8 from the frozen baseline).

---

## Scope

- **In scope**:
  - create `.github/skills/python-operator-overloading/SKILL.md`
  - create `.github/skills/python-operator-overloading/reference.md` as the
    focused navigation overview
  - create `.github/skills/python-operator-overloading/references/binary-operators.md`
    covering R1, R2, R6, R7
  - create `.github/skills/python-operator-overloading/references/in-place-and-unary-operators.md`
    covering R3, R4
  - create `.github/skills/python-operator-overloading/references/comparison-and-ordering.md`
    covering R5, R8
  - create `.github/skills/python-operator-overloading/examples.md` with 6
    scenario sections for all requirement paths
  - update `README.md`: add the stable-library row for
    `python-operator-overloading`
  - update `VERSION`: bump `0.34.0` → `0.35.0`

- **Out of scope**:
  - `__eq__` / `__hash__` definition (owned by `python-data-model-methods`)
  - mutable vs immutable class design (owned by `python-class-design`)
  - `@functools.total_ordering` decorator mechanics (owned by
    `python-decorators`)
  - inherited operator MRO resolution (owned by `python-class-design`)
  - framework-specific operators (SQLAlchemy, NumPy broadcasting, etc.)
  - complex cross-type coercion logic (adapter/service layer concern)
  - descriptors, `__getattr__`, metaclass behavior
  - `__new__`, `__del__`, object lifecycle

---

## Locked Decisions

All decisions below are locked from the analysis layer and must not be
rediscovered or renegotiated during implementation.

- This topic is a **stable-library-affecting topic** with declared publish and
  release timing.
- The skill's primary scope is **Python operator overloading semantics** —
  binary arithmetic, reflected operators, in-place operators, unary operators,
  comparison/ordering, `NotImplemented` dispatch, and mixed-type arithmetic
  type-guard.
- **`references/` split is required** — 5 logical topic clusters exceed the
  3-topic policy threshold. The 3-file split under `references/` is mandatory:
  - `references/binary-operators.md`
  - `references/in-place-and-unary-operators.md`
  - `references/comparison-and-ordering.md`
- **`examples.md` is required** — branching skill with multi-path decisions;
  6 scenario sections are required.
- **`NotImplemented` vs `TypeError` rule is a first-class requirement (R6)**,
  not a parenthetical note. Creator must dedicate a full scenario in `examples.md`
  to this distinction, including the `NotImplemented` vs `NotImplementedError`
  confusion trap.
- **`__eq__` must not appear as implementation guidance** inside this skill. It
  is a cross-skill pre-condition dependency. Any creator drift into `__eq__`
  definition is a rollback trigger.
- **`@functools.total_ordering` mechanics must not be authored here.** The skill
  recommends it as a semantic completion tool; detailed decorator mechanics
  belong in `python-decorators`.
- **Stable-library timing is locked to `stable-library-affecting-now`**:
  - `README.md` and `VERSION` are updated at `publish-in-progress`
  - tag action `v0.35.0` at `release`
- **Python 3.10+ baseline** — matches the repo's existing typing standard;
  built-in generics and PEP 604 unions are allowed in examples.

### Cross-skill dependency contracts (read-only)

| Skill | How this skill references it |
| --- | --- |
| `python-data-model-methods` | `__eq__` is an external pre-condition for ordering consistency (R5); must not be redefined here |
| `python-class-design` | Mutable vs immutable design for `__iadd__` return semantics (R3 boundary); signpost only |
| `python-decorators` | `@functools.total_ordering` mechanism (R8 boundary); signpost only |

---

## Boundaries / Exclusions

- **`python-data-model-methods`** — owns foundational dunders (`__init__`,
  `__repr__`, `__str__`, `__eq__`, `__hash__`, `__bool__`). This skill must
  not redefine `__eq__` even in examples. Cross-skill semantic alignment rule
  is allowed; ownership is not transferred.
- **`python-class-design`** — owns mutability design philosophy and class public
  surface shape. This skill owns only the in-place operator return syntax
  contract.
- **`python-decorators`** — owns `@functools.total_ordering` implementation and
  decorator mechanism details. This skill references the recommendation intent
  only.
- **`python-async-await`** — owns async data-model protocols. This skill is
  synchronous-only.
- If later work requires operator MRO inheritance, descriptor-based operator
  dispatch, or framework-specific operator semantics, stop and split into a
  separate topic.

---

## Status / Allowed Transitions

- **Current**: `planned`
- **Execution model**: follow the canonical creator → reviewer → publish →
  merge → release path; this topic reaches `released` because it declares a
  post-merge tag action.
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
  - `released` → terminal

Routing notes:

- Use the standard Phase 4.5 planner-alignment checkpoint from
  `plan/agent-handoff-workflow.md`.
- If creator drifts into `__eq__` implementation, `total_ordering` mechanics,
  MRO inheritance, or framework operators, route back to `creator-in-progress`
  and repair scope before publish.
- If `NotImplemented` dispatch rule is compressed to a footnote in
  `examples.md`, route back to `creator-in-progress`.

---

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/python-operator-overloading/python-operator-overloading.plan.md` | Planning actor | Repo-visible execution contract for this topic |
| Skill contract | `.github/skills/python-operator-overloading/SKILL.md` | Creator | Executable skill instructions; ~110–130 lines; all required sections |
| Reference overview | `.github/skills/python-operator-overloading/reference.md` | Creator | Focused navigation file; lists 3 split reference files and their roles |
| Binary operators reference | `.github/skills/python-operator-overloading/references/binary-operators.md` | Creator | Covers R1, R2, R6, R7: arithmetic, reflected, `NotImplemented` dispatch, mixed-type guard |
| In-place and unary reference | `.github/skills/python-operator-overloading/references/in-place-and-unary-operators.md` | Creator | Covers R3, R4: in-place return contract and unary purity rule |
| Comparison and ordering reference | `.github/skills/python-operator-overloading/references/comparison-and-ordering.md` | Creator | Covers R5, R8: ordering consistency with `__eq__`, `total_ordering` recommendation |
| Detailed examples | `.github/skills/python-operator-overloading/examples.md` | Creator | 6 scenario sections; required for this branching multi-path skill |
| Stable-library summary | `README.md` | Main Agent | Add stable-library row for `python-operator-overloading` |
| Repo version baseline | `VERSION` | Main Agent | Bump `0.34.0` → `0.35.0` |

Artifact path notes:

- This topic **modifies `README.md`** and **`VERSION`** at `publish-in-progress`.
- This topic does **not** modify `.github/copilot-instructions.md`,
  `plan/agent-handoff-workflow.md`, or any existing `python-*` skill folder.
- These paths are an executable contract. If later work tries to add async
  protocol examples, MRO inheritance sections, or framework-specific operator
  subfolders, stop and repair the plan or split the work into a separate topic.

---

## Stable library metadata

### README row

- Table: `## Current skills`
- Exact row:

  `| \`python-operator-overloading\` | defines Python operator overloading rules for binary arithmetic contracts, reflected operator pairing, in-place return semantics, unary operator purity, comparison ordering consistency, and the NotImplemented dispatch protocol |`

- Position:
  - after `python-data-model-methods`
  - before `python-api-signature`

### VERSION bump

- Current: `0.34.0`
- Direction: `MINOR`
- New: `0.35.0`
- Reason: new stable skill, non-breaking capability addition

### Timing

- README / VERSION timing: `publish-in-progress`
- Reason: the PR should show both the new stable skill and the stable-library
  surfaces it promotes

### Additional release metadata

- Tag action: create and push annotated tag `v0.35.0` at `release`
- Release notes artifact: none in this topic
- GitHub Release object: none in this topic unless a later release-specific
  topic adds one

---

## Implementation Steps

### Creator Phase (after plan approval)

1. Create `.github/skills/python-operator-overloading/`.
2. Draft `SKILL.md` with the required repository shape:
   - YAML frontmatter (`name`, `description`)
   - Purpose
   - Trigger / When to use
   - Inputs
   - Process (6 decision steps; include a reflected-operator check step and a
     `NotImplemented` vs named-method step)
   - Examples (at minimum one concise positive and one concise negative in SKILL.md)
   - Outputs
   - Boundaries (must name all 3 cross-skill signposts)
   - Local references (must list all 5 local files with roles)
3. Author `reference.md` as a navigation overview (< 40 lines); list the 3
   split reference files and their topic coverage.
4. Author `references/binary-operators.md` first (highest complexity):
   - R1: arithmetic operator families and `NotImplemented` obligation
   - R2: reflected operator symmetric pair rule
   - R6: `NotImplemented` vs `TypeError` dispatch decision — dedicate a
     subsection; include `NotImplemented` vs `NotImplementedError` trap
   - R7: `isinstance` guard pattern for mixed-type arithmetic
5. Author `references/in-place-and-unary-operators.md`:
   - R3: `__iadd__` / `__imul__` return contract — `return self` (mutable),
     `return new_obj` (immutable), `return None` is a hard violation; include a
     note recommending explicit `-> MyType` return-type annotation on in-place
     methods as the pyright-enforceable form of the contract
   - R4: unary purity rule — `__neg__`, `__pos__`, `__abs__` must not mutate
     `self`
6. Author `references/comparison-and-ordering.md`:
   - R5: semantic consistency rule — `not (a < b) and not (b < a)` implies
     `a == b`; `__eq__` is a pre-condition dependency (do not redefine here)
   - R8: `@functools.total_ordering` as semantic completion recommendation;
     signpost mechanics to `python-decorators`
7. Draft `examples.md` with 6 scenario sections:
   - Section 1: binary arithmetic — `Money.__add__` positive + negative
     (direct `TypeError` raise)
   - Section 2: reflected operator — `3 + money_obj` scenario
   - Section 3: in-place operator — `__iadd__` with/without `return`
   - Section 4: comparison / ordering — `__lt__` + `total_ordering`
   - Section 5: `NotImplemented` dispatch — dedicated anti-pattern scenario
     distinguishing `NotImplemented` vs `NotImplementedError`
   - Section 6: mixed-type arithmetic — `isinstance` guard pattern
8. Verify no `__eq__` implementation guidance appears anywhere in the skill.
9. Verify `total_ordering` mechanics are not authored here; only a signpost.
10. Verify all examples run on Python 3.10+.
11. Stage `README.md` and `VERSION` updates at `publish-in-progress`.

### Creator deliverable summary

- review-ready `.github/skills/python-operator-overloading/` folder with:
  - `SKILL.md` (required)
  - `reference.md` (required)
  - `references/` with 3 topic files (required — policy mandates split)
  - `examples.md` (required — branching skill policy)
- all files contain explicit examples and clear boundaries
- all code examples run on Python 3.10+ or are clearly version-gated

---

## Validation / Acceptance Checks

Reviewer and Main Agent must verify:

1. `SKILL.md` contains all required sections including `Local references`.
2. `Local references` in `SKILL.md` names all 5 local files with their roles.
3. `reference.md` is a navigation overview only; it does not duplicate content
   from split reference files.
4. `references/binary-operators.md` includes a dedicated subsection for the
   `NotImplemented` vs `TypeError` vs `NotImplementedError` trap.
5. `references/in-place-and-unary-operators.md` explicitly states that returning
   `None` from `__iadd__` is a hard violation.
6. `references/comparison-and-ordering.md` does not define `__eq__`; it only
   references it as a pre-condition.
7. `examples.md` has all 6 scenario sections; `NotImplemented` dispatch is a
   first-class scenario, not a footnote.
8. No `__eq__` implementation code appears in any file.
9. No `@functools.total_ordering` mechanics are authored in any file (signpost
   only).
10. `README.md` row is positioned after `python-data-model-methods` and before
    `python-api-signature`.
11. `VERSION` reads `0.35.0` at publish time.

---

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

---

## Post-merge / release actions

1. Confirm merge commit is on `dev`.
2. Verify `VERSION` reads `0.35.0` and `README.md` contains the
   `python-operator-overloading` row in the correct position.
3. Update this topic plan: `merged` → `released`.
4. Create and push annotated tag `v0.35.0`:
   ```bash
   git tag -a v0.35.0 -m "release: python-operator-overloading stable skill"
   git push origin v0.35.0
   ```
5. Release gate: workspace must be clean before tagging. If worktree is dirty,
   resolve before proceeding.

---

## Open Questions / Unresolved Items

None. Both analysis-layer artifacts are frozen and all decisions are locked.
This plan is ready for `plan-reviewer` handoff.
