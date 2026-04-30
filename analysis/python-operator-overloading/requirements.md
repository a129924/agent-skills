# Requirements Baseline: python-operator-overloading

> Status: **FROZEN** — ready for `business-to-technical-translation`.
> Frozen by: business-intent-alignment session (2026-04-30).
> All ⚠️ boundary items have been resolved. No contradictions survived review.

---

## Problem Statement (Business Terms)

Python developers routinely overload operators without understanding the
two-sided dispatch protocol, the obligation to return `NotImplemented` instead
of raising `TypeError` prematurely, or the semantic consistency requirement
between equality and ordering. The result is operator behavior that surprises
both the caller and the maintainer.

A focused skill is needed to teach **when** to overload an operator, **how** to
implement the two-sided contract correctly, and **where** to draw the line
between operator syntax and explicit named methods.

---

## Actors and Permission Boundaries

| Actor | Role |
| --- | --- |
| Python developer | Authors the class that overloads operators |
| Reviewer / maintainer | Validates semantic consistency and contract completeness at review time |
| Agent (Copilot) | Drafts or reviews operator overloading decisions against this skill |

---

## In-Scope Requirements

### R1 — Binary arithmetic operator contract

- **Actor**: Python developer authoring a class with numeric or value semantics
- **Condition**: The class defines `__add__`, `__sub__`, `__mul__`, `__truediv__`,
  `__floordiv__`, `__mod__`, `__pow__`, or similar binary arithmetic methods
- **Observable result**: The method either produces a valid result object or
  returns `NotImplemented` when the operand type is unsupported
- **Metric / decision rule**: No binary arithmetic method raises `TypeError`
  directly for an unsupported type without first returning `NotImplemented` to
  allow Python to try the reflected operator on the right-hand operand
- **Failure meaning**: Mixed-type arithmetic breaks silently or prevents third-party
  types from integrating with the class through their own `__radd__`/`__rsub__`

### R2 — Reflected operator contract

- **Actor**: Python developer whose class must interoperate with foreign types
- **Condition**: `obj + foreign_value` is tried but the left-hand `__add__` returns
  `NotImplemented`
- **Observable result**: Python automatically tries `foreign_value.__radd__(obj)`,
  giving the right-hand type a chance to handle the dispatch
- **Metric / decision rule**: The symmetric pair rule is explicitly defined: every
  `__add__` that returns `NotImplemented` must be accompanied by a corresponding
  `__radd__` when the class intends to support reflected arithmetic
- **Failure meaning**: Mixed-type arithmetic silently fails or produces
  `TypeError: unsupported operand type(s)` even when the operation is valid in
  both directions

### R3 — In-place operator return contract

- **Actor**: Python developer defining `__iadd__`, `__imul__`, or similar in-place
  operators
- **Condition**: A caller writes `a += b`, which calls `a.__iadd__(b)` and
  rebinds `a` to the return value
- **Observable result**: The method returns `self` for mutable objects or a new
  object for immutable objects; it never returns `None`
- **Metric / decision rule**: Any `__iadd__` or similar that falls through without
  an explicit `return` is a defect; returning `None` (implicit) is a hard
  violation
- **Failure meaning**: `a += b` rebinds `a` to `None`, silently destroying the
  reference; this is a class of bug that static type checkers often miss without
  explicit annotation
- **Boundary**: This skill owns the **syntax contract** (what to return and why).
  The question of whether an object *should* be mutable at all is owned by
  `python-class-design`.

### R4 — Unary operator contract

- **Actor**: Python developer defining `__neg__`, `__pos__`, or `__abs__`
- **Condition**: A caller applies `-obj`, `+obj`, or `abs(obj)` to a class with
  numeric or vector semantics
- **Observable result**: The method returns a new object with the correct semantic
  state transformation; it does not mutate `self`
- **Metric / decision rule**: Reviewer can verify in one read that the unary
  operator is pure (no `self` mutation) and returns the correct type
- **Failure meaning**: `abs(obj)` returns the wrong type or mutates `obj` in place,
  breaking composition and test reproducibility

### R5 — Comparison and ordering contract (excluding `__eq__`)

- **Actor**: Python developer whose class should be sortable or orderable
- **Condition**: The class defines any of `__lt__`, `__le__`, `__gt__`, `__ge__`
- **Observable result**: The ordering operators are semantically consistent with
  the existing `__eq__` — that is, `not (a < b) and not (b < a)` must imply
  `a == b`
- **Metric / decision rule**: The skill defines this cross-skill semantic alignment
  rule as an explicit acceptance check; reviewer can verify consistency without
  inspecting a second file
- **Failure meaning**: `a == b` is `True` but `sorted([a, b])` produces unstable
  or counter-intuitive order, or comparisons raise `TypeError` unexpectedly
- **Boundary**: `__eq__` itself is owned by `python-data-model-methods`. This
  skill treats it as a pre-condition and cross-skill contract dependency, not
  something it redefines.

### R6 — `NotImplemented` vs `TypeError` dispatch rule

- **Actor**: Python developer implementing any binary operator
- **Condition**: The right-hand operand is not a supported type
- **Observable result**: The method returns `NotImplemented` (not
  `NotImplementedError`, not `TypeError`) to signal that Python should attempt
  the reflected operator
- **Metric / decision rule**:
  - `return NotImplemented` → correct; Python continues dispatch
  - `raise TypeError(...)` directly → violation; kills dispatch prematurely
  - returning a sentinel or `None` → violation; Python treats it as the arithmetic result (not a dispatch signal), causing silent data loss
- **Failure meaning**: Third-party types that implement the reflected operator
  cannot interoperate with the class even when a valid operation exists

### R7 — Mixed-type arithmetic type-dispatch rule

- **Actor**: Python developer whose class must accept operands of a compatible
  foreign type (e.g., `Money * int`, `Vector + tuple`)
- **Condition**: The binary operator receives a foreign type that can be
  legitimately supported
- **Observable result**: The method performs an `isinstance` check first, handles
  the accepted foreign type explicitly, and returns `NotImplemented` for all
  other types
- **Metric / decision rule**: The dispatch logic fits in one `isinstance` guard
  without implicit type coercion or silent numeric conversion
- **Failure meaning**: The method silently converts operands or crashes on
  borderline types, obscuring errors that should surface as `TypeError`
- **Boundary**: Complex cross-type coercion logic (e.g., currency conversion,
  dimensional unit normalization) is out of scope. The skill will note that
  such cases should delegate to an adapter or service layer.

### R8 — `@functools.total_ordering` usage intent

- **Actor**: Python developer who wants a fully ordered type with minimal
  boilerplate
- **Condition**: The class defines `__eq__` and exactly one ordering method
  (`__lt__`, `__le__`, `__gt__`, or `__ge__`)
- **Observable result**: The skill recommends `@functools.total_ordering` as the
  canonical way to complete the ordering contract from a minimal implementation
- **Metric / decision rule**: Developer can verify in one screen that the ordering
  semantic is complete and consistent without manually implementing all four
  comparison methods
- **Failure meaning**: Developer implements only `__lt__` and assumes Python will
  infer the rest; `>=` and `<=` then raise `TypeError` at runtime
- **Boundary**: The mechanism of `@functools.total_ordering` (how it wraps
  functions, its performance implications) is owned by `python-decorators`.
  This skill treats it as a semantic recommendation only.

---

## Explicit Non-Goals

| Item | Reason excluded |
| --- | --- |
| `__eq__` / `__hash__` definition | Owned by `python-data-model-methods` |
| Mutable vs immutable class design | Owned by `python-class-design` |
| `@functools.total_ordering` decorator mechanics | Owned by `python-decorators` |
| Inherited operator MRO resolution | Owned by `python-class-design` |
| Framework-specific operators (e.g., SQLAlchemy `==`, NumPy broadcasting) | Out of scope entirely |
| Complex cross-type coercion (unit conversion, currency) | Adapter/service layer concern |
| `__getattr__`, descriptors, metaclass behavior | Out of scope entirely |
| `__new__`, `__del__`, object lifecycle | Out of scope entirely |

---

## Acceptance Criteria (Success Signals)

Three layered acceptance criteria derived from Q5 decision D:

**AC-1 (Transparency)** — A reviewer reading only the operator methods can tell
without opening callsite code whether `3 + obj` and `obj + 3` are both
supported.

**AC-2 (Minimum Surprise — primary criterion)** — No maintainer encounters the
situation where `obj1 == obj2` is `True` but `obj1 < obj2` raises an unexpected
error, or where `a += b` silently sets `a = None`.

**AC-3 (Decision clarity)** — A developer following this skill can decide, for
any candidate operator, whether overloading it improves clarity or whether a
named method (e.g., `add(other)`) is semantically cleaner.

---

## Explicit Assumptions

- Target Python version is **3.10+**, matching the repository's existing typing
  baseline.
- Examples may use built-in generics (`list[int]`) and PEP 604 unions
  (`int | None`).
- The skill covers **synchronous** operator methods only. Async data-model
  protocols are owned by `python-async-await`.
- This skill treats `__eq__` from `python-data-model-methods` as an external
  pre-condition dependency, not a re-definition.

---

## Cross-Skill Contract Dependencies

| Dependency | How this skill references it |
| --- | --- |
| `python-data-model-methods` | `__eq__` is the external pre-condition for ordering consistency (R5); not redefined here |
| `python-class-design` | Mutable vs immutable decision for `__iadd__` return semantics (R3 boundary) |
| `python-decorators` | `@functools.total_ordering` mechanism (R8 boundary) |

---

## Contradiction Log

No contradictions survived the interview round. The following potential
contradictions were explicitly resolved:

| Potential conflict | Resolution |
| --- | --- |
| `__eq__` ownership overlap | Resolved as cross-skill semantic alignment dependency, not ownership transfer |
| `@total_ordering` ownership overlap | Resolved as intent-vs-mechanism split: intent here, mechanics in `python-decorators` |
| `__iadd__` mutability overlap with `python-class-design` | Resolved as syntax-contract-vs-design-philosophy split |

---

## Remaining Blockers

None. This baseline is ready for `business-to-technical-translation`.

---

## Handoff Boundary

Next step: `business-to-technical-translation` →
`analysis/python-operator-overloading/technical-spec.md`
