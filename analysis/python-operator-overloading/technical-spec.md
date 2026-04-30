# Technical Specification: python-operator-overloading

> Translated from: `analysis/python-operator-overloading/requirements.md`
> Status: **READY FOR PLAN CREATION**
> Posture: pessimistic implementer — all costs, coupling risks, and rollback
> triggers are named explicitly.

---

## Baseline Gating Check

- `requirements.md` exists and is marked FROZEN: ✅
- All 8 requirements have named actors, conditions, observable results, and
  failure meanings: ✅
- No contradictions are outstanding: ✅
- Cross-skill boundaries are resolved (3 explicit dependencies): ✅
- No ambiguous scope remains that would require routing back to
  `business-intent-alignment`: ✅

Translation proceeds.

---

## Requirement-to-Technical Mapping

### R1 — Binary arithmetic operator contract

**Technical tasks:**
- SKILL.md: define the binary operator decision path — when to overload vs when
  a named method is clearer
- reference file (binary operators): enumerate supported arithmetic families
  (`__add__`, `__sub__`, `__mul__`, `__truediv__`, `__floordiv__`, `__mod__`,
  `__pow__`) with the `NotImplemented` return obligation
- examples.md: positive pattern — `Money.__add__` that returns `NotImplemented`
  for unsupported types; negative pattern — `Money.__add__` that raises
  `TypeError` directly, breaking third-party integration

**Artifacts:** `SKILL.md` (Process section), `references/binary-operators.md`,
`examples.md` (Section 1)

**Dependency note:** `references/binary-operators.md` must reference R6
(`NotImplemented` dispatch rule) as the governing rule for the "unsupported
type" path.

---

### R2 — Reflected operator contract

**Technical tasks:**
- reference file (binary operators): define the symmetric pair rule — `__add__`
  always paired with `__radd__` when reflected arithmetic is intended
- SKILL.md Process: add an explicit step for reflected operator check
- examples.md: `3 + money_obj` scenario where `int.__add__` returns
  `NotImplemented` and `Money.__radd__` handles the fallback

**Artifacts:** `references/binary-operators.md`, `SKILL.md`, `examples.md`
(Section 2)

**Feasibility note:** The reflected operator pairing rule is one of the most
missed Python behaviors. The examples.md scenario for `3 + obj` is technically
non-obvious and must be explicitly illustrated — no implicit assumption that
readers know this.

---

### R3 — In-place operator return contract

**Technical tasks:**
- reference file (in-place operators): define the two valid return forms:
  - mutable: `return self`
  - immutable: `return new_obj`
  - forbidden: implicit `return None`
- examples.md: anti-pattern — `__iadd__` without `return` statement; show the
  resulting `a = None` rebind bug explicitly
- SKILL.md Boundaries: signpost to `python-class-design` for mutable vs
  immutable design decision

**Artifacts:** `references/in-place-and-unary-operators.md`, `SKILL.md`,
`examples.md` (Section 3)

**Risk flag:** Static type checkers (`pyright --strict`) will catch missing
`return` in `__iadd__` if the method is annotated with the correct return type
(`-> MyType`). The skill should recommend explicit return type annotation as the
machine-enforceable form of this rule — this aligns with the repo's
`python-type-hints-strict` baseline without making that skill a dependency.

---

### R4 — Unary operator contract

**Technical tasks:**
- reference file (in-place and unary): define purity rule — unary operators
  (`__neg__`, `__pos__`, `__abs__`) must not mutate `self`; they return new
  objects
- examples.md: anti-pattern — `__neg__` that mutates `self.value` in place

**Artifacts:** `references/in-place-and-unary-operators.md`, `examples.md`
(Section 3, combined with in-place)

**Cost note:** R4 is low complexity to author (fewer edge cases than binary/
reflected). Combining it with R3 into one reference file is efficient and keeps
file count manageable.

---

### R5 — Comparison and ordering contract

**Technical tasks:**
- reference file (comparison and ordering): define the semantic consistency
  rule: `not (a < b) and not (b < a)` implies `a == b`; write this as an
  explicit acceptance check
- reference file: cross-skill dependency note that `__eq__` is a pre-condition
  owned by `python-data-model-methods` — do not redefine it here
- examples.md: anti-pattern — class implements `__lt__` but `__eq__` uses
  different fields, causing inconsistent sort ordering

**Artifacts:** `references/comparison-and-ordering.md`, `examples.md`
(Section 4)

**Cross-skill coupling risk:** The semantic alignment rule between `__lt__` and
`__eq__` is a dependency on behavior defined in `python-data-model-methods`.
Creator must not author a `__eq__` example inside this skill's examples. If
creator drifts into `__eq__` implementation guidance, reviewer should flag
`needs-rework`.

---

### R6 — `NotImplemented` vs `TypeError` dispatch rule

**Technical tasks:**
- reference file (binary operators): distinguish three cases precisely:
  1. `return NotImplemented` — correct (allows Python to try reflected operator)
  2. `raise TypeError(...)` — violation (kills dispatch chain prematurely)
  3. `return None` or returning a sentinel — violation (Python treats `None` as the arithmetic result, causing silent data loss)
- Add explicit note: `NotImplemented` (singleton) vs `NotImplementedError`
  (exception) — these are two different Python objects; confusing them is a
  well-known trap
- examples.md: dedicate a focused scenario to this distinction

**Artifacts:** `references/binary-operators.md` (merged with R1/R2), `examples.md`
(Section 5 — dedicated `NotImplemented` scenario)

**Priority flag:** R6 is the highest information-density requirement in this
baseline. The `NotImplemented` vs `NotImplementedError` confusion is a
documented Python footgun. The examples.md section for this must be explicit and
cannot be compressed into a parenthetical note.

---

### R7 — Mixed-type arithmetic type-dispatch rule

**Technical tasks:**
- reference file (binary operators): document the `isinstance` guard pattern as
  the canonical dispatch mechanism for mixed-type arithmetic
- define the boundary: class-specific coercion logic (e.g., `Decimal` → `Money`
  conversion) is out of scope; skill covers only the dispatch decision
- examples.md: `Money * int` scenario — `isinstance(other, int)` check, handle,
  then `return NotImplemented` for all other types

**Artifacts:** `references/binary-operators.md`, `examples.md` (Section 6)

---

### R8 — `@functools.total_ordering` usage intent

**Technical tasks:**
- reference file (comparison and ordering): document `@functools.total_ordering`
  as the recommended semantic completion tool when only `__eq__` + one ordering
  method is defined
- add failure scenario: class has `__lt__` but not `__ge__`; `sorted()` works
  but direct `>=` raises `TypeError`
- SKILL.md Boundaries: explicit signpost to `python-decorators` for decorator
  mechanism details

**Artifacts:** `references/comparison-and-ordering.md`, `SKILL.md` (Boundaries),
`examples.md` (Section 4, combined with R5)

---

## Artifact Plan

| Artifact | Path | Authoring notes |
| --- | --- | --- |
| Skill contract | `.github/skills/python-operator-overloading/SKILL.md` | ~110–130 lines; required sections: frontmatter, Purpose, Trigger, Inputs, Process (decision steps), Examples, Outputs, Boundaries, Local references |
| Reference overview | `.github/skills/python-operator-overloading/reference.md` | Short navigation file (< 40 lines); lists split files and roles; matches `python-data-model-methods` pattern |
| Binary operator reference | `.github/skills/python-operator-overloading/references/binary-operators.md` | Covers R1, R2, R6, R7 — arithmetic, reflected, `NotImplemented` dispatch, mixed-type guard |
| In-place + unary reference | `.github/skills/python-operator-overloading/references/in-place-and-unary-operators.md` | Covers R3, R4 — return contract and purity rule |
| Comparison + ordering reference | `.github/skills/python-operator-overloading/references/comparison-and-ordering.md` | Covers R5, R8 — ordering consistency with `__eq__`, `total_ordering` recommendation |
| Examples | `.github/skills/python-operator-overloading/examples.md` | Required (branching topic, multi-path decisions); ~200–270 lines; 6 scenario sections |
| README stable row | `README.md` | Add after `python-data-model-methods` row, before `python-api-signature` |
| Version bump | `VERSION` | MINOR bump from `0.34.0` → `0.35.0` |

**Reference split justification:** 8 requirements span 5 logical topic clusters
(binary arithmetic, reflected operators, in-place/unary, comparison/ordering,
`NotImplemented` dispatch + mixed-type guard). A single `reference.md` would
exceed the ~1000-token policy threshold. The 3-file split under `references/`
follows the established `python-data-model-methods` pattern.

---

## Architecture Compliance Self-Check

| Check | Result | Notes |
| --- | --- | --- |
| Required files present | ✅ FIT | `SKILL.md` + `reference.md` + `references/` + `examples.md` satisfy the skill folder contract |
| Single responsibility | ✅ FIT | Scope is operator overloading only; class design, decorator mechanics, and `__eq__` are explicitly excluded |
| Portable | ✅ FIT | No repo-specific or framework-specific content; Python 3.10+ baseline matches existing repo standard |
| Independent | ✅ FIT | Outbound signposts only; no inbound coupling from other skills |
| `examples.md` required? | ✅ YES | Branching topic with multi-path decisions; meets the repo policy threshold |
| `references/` split required? | ✅ YES | 5 logical topic clusters exceed the 3-topic threshold |
| Frontmatter, Local references section | ✅ FIT | Must list all 3 split reference files with roles |
| Positive + negative examples in SKILL.md | ✅ FIT | Required by repo policy; covered in Process/Examples section |
| Cross-skill boundaries declared | ✅ FIT | 3 boundaries named: `python-data-model-methods`, `python-class-design`, `python-decorators` |
| No overlap with existing stable skills | ✅ FIT | `python-operator-overloading` folder does not exist; no README row present |
| README row position | ✅ FIT | After `python-data-model-methods`, before `python-api-signature` |
| VERSION: current `0.34.0` → `0.35.0` | ✅ FIT | MINOR bump, new stable skill |

No architecture waivers required.

---

## Feasibility Assessment

### Cost-of-realization

| Workstream | Complexity | Notes |
| --- | --- | --- |
| `SKILL.md` authoring | Medium | Decision-path logic requires careful wording; 6 boundary signposts needed |
| `reference.md` overview | Low | Navigation file; mirrors existing skill pattern |
| `references/binary-operators.md` | Medium-High | Most information-dense file; covers R1, R2, R6, R7 including `NotImplemented` trap |
| `references/in-place-and-unary-operators.md` | Low-Medium | Straightforward return contract; combined R3+R4 |
| `references/comparison-and-ordering.md` | Medium | Cross-skill dependency note requires careful wording to avoid `__eq__` drift |
| `examples.md` | High | 6 scenario categories; must not let `3 + obj` scenario be skipped; `NotImplemented` vs `NotImplementedError` must be explicit |
| README + VERSION | Low | Mechanical updates; slot position known |

**Total effort estimate:** Comparable to `python-data-model-methods` (3 reference
files, 272-line examples.md). Expect similar scope.

### Sequencing constraint

- Creator must not author `__eq__` examples — this is the most likely drift
  surface. Reviewer must check for `__eq__` definition in examples.
- `NotImplemented` vs `NotImplementedError` confusion must be a first-class
  anti-pattern in examples.md, not a footnote. If creator buries it, reviewer
  should return `needs-rework`.
- `references/binary-operators.md` is the most complex file; creator should
  author it first to establish the `NotImplemented` dispatch rules before
  writing the other files.

---

## Conflict Detection

No conflicts between technical reality and business intent detected.

| Check | Status |
| --- | --- |
| Python 3.10+ baseline — all operator methods in scope exist on this version | ✅ No conflict |
| `references/` split is supported by repo policy | ✅ No conflict |
| `examples.md` required threshold is met | ✅ No conflict |
| Cross-skill boundaries map to stable existing skills | ✅ No conflict |
| VERSION bump `0.34.0` → `0.35.0` — no tag conflict | ✅ No conflict |

---

## Rollback Triggers

The following conditions would require rollback to an earlier phase:

| Trigger | Rollback target |
| --- | --- |
| Creator adds `__eq__` implementation guidance inside this skill | Rollback to `creator-in-progress`; repair scope |
| Creator merges `total_ordering` decorator mechanics into this skill | Rollback to `creator-in-progress`; move mechanics to signpost |
| `NotImplemented` dispatch rule is reduced to a parenthetical note | Rollback to `creator-in-progress`; restore as first-class section |
| `references/` split is collapsed to single `reference.md` without justification | Reviewer should flag as potential policy violation; check token count |
| VERSION at publish time is not `0.35.0` | Release gate blocks tag creation |

No rollback to `business-intent-alignment` is triggered; all requirements are
technically feasible without renegotiation.

---

## Handoff to Plan Creation

This technical spec is ready for `plan-creator` to produce:
`plan/python-operator-overloading/python-operator-overloading.plan.md`

**Strict mode is in effect**: both `requirements.md` and `technical-spec.md`
are present in `analysis/python-operator-overloading/`. The plan must map 100%
to this spec with no self-healing or gap-filling.

### Plan contract anchors for `plan-creator`

- Artifact paths: 7 files (SKILL.md, reference.md, 3 split reference files,
  examples.md, topic plan itself) + README row + VERSION
- Stable-library metadata: README row after `python-data-model-methods`, before
  `python-api-signature`; VERSION `0.34.0` → `0.35.0`
- Execution model: creator → reviewer → publish → merge → release (standard
  stable-library-affecting path)
- Scope boundary hardening: must name `__eq__` drift and `total_ordering`
  mechanics drift as explicit rollback conditions in the plan
- Tag action: `v0.35.0` at release
