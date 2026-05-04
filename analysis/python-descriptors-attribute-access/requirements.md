# Requirements Baseline — `python-descriptors-attribute-access`

**Status**: FROZEN  
**Frozen at**: 2026-05-04  
**Scope verdict**: Full descriptor protocol + discouraged hierarchy (expanded from original @property-restricted intent — explicitly confirmed by stakeholder)

---

## Business Intent

Help Python developers choose the **least powerful attribute access mechanism** that correctly expresses the intended attribute semantics, while preserving code readability, maintainability, and IDE static navigation.

Core positioning:

> Teach Python developers how to control attribute access semantics using `@property`, `@cached_property`, descriptors, and attribute hook methods, while avoiding unnecessary magic that harms readability, IDE navigation, and maintainability.

---

## Target Audience

- **Primary**: Python package and library authors
- **Secondary**: Application developers implementing proxy, adapter, or delegation patterns

Python version floor: **3.6+** (required for `__set_name__`); `@cached_property` requires **3.8+**.

---

## Requirements

### R1 — Mechanism Selection Ladder (Core)

When choosing how to expose or control attribute access, a developer MUST prefer the weakest mechanism sufficient for the expressed semantic.

**The canonical ladder** (weakest to most powerful):

```
plain attribute
→ @property
→ @cached_property
→ custom descriptor
→ __getattr__
→ __setattr__
→ __getattribute__
```

**Observable signal**: Any choice that skips a ladder rung must be justified in code comments or documentation.

---

### R2 — `@property` Discipline

`@property` is the canonical solution for:
- single-attribute computed read-only values
- single-attribute invariants enforced at write time

Setter validation belongs here **if and only if** the invariant is scoped to the single attribute value (e.g., `temperature >= -273.15`, `age >= 0`).

**Out of `@property` scope**: cross-field validation, DTO-level contracts, schema validation — those belong in `python-error-handling` or domain-layer skills.

**Measurable boundary**: If the setter needs to inspect more than `self` and the incoming value, it has left the `@property` jurisdiction.

---

### R3 — `@cached_property` Usage

For lazy computed attributes that are expensive and pure (no side effects on set), `@cached_property` is preferred over manual caching with a private backing attribute.

**Decision rule**:
- attribute must be recomputed on every access → `@property`
- attribute is computed once and stored (pure, idempotent) → `@cached_property`

`@cached_property` produces a non-data descriptor; it is overridable by instance `__dict__`. This must be documented when it matters.

---

### R4 — Custom Descriptor Discipline

Custom descriptors (`__get__`, `__set__`, `__delete__`) are justified ONLY when:
- `@property` cannot be reused across multiple attributes without duplicating logic
- shared validation or transformation cannot be centralized in a single `@property`
- descriptor lookup priority behaviour must be explicitly controlled

**Upgrade signal**: if three or more attributes in the same class share identical `@property` setter logic, consider a custom descriptor.

---

### R5 — `__set_name__` Requirement

Any custom descriptor class designed for reuse across multiple attribute names MUST implement `__set_name__` to avoid hardcoded private attribute names.

**Observable failure**: a descriptor that hardcodes `self.private_name = "_value"` in `__init__` is not reusable and cannot be validated without knowing the owner class structure.

**Correct pattern**: `__set_name__(self, owner, name)` sets `self.private_name = f"_{name}"`.

---

### R6 — Data vs Non-data Descriptor Awareness

Developers MUST understand the distinction:
- **Data descriptor**: defines both `__get__` and `__set__` (or `__delete__`) → shadows instance `__dict__`
- **Non-data descriptor**: defines only `__get__` → instance `__dict__` takes priority

Lookup priority order: data descriptor > instance `__dict__` > non-data descriptor > class `__dict__`.

**Observable check**: if a descriptor is unexpectedly overridden by an instance attribute, the root cause is almost always the data/non-data distinction.

---

### R7 — `__getattr__` Escape Hatch (Discouraged, Strict Constraints)

`__getattr__` is **discouraged by default** for all code.

Escape hatch is permitted ONLY when ALL of the following hold:

1. The class is explicitly a proxy, adapter, delegation layer, or compatibility shim
2. The fallback target is explicit and documented
3. `AttributeError` is never silently swallowed — missing attributes raise `AttributeError` with a clear message
4. Tests cover both the missing-attribute path and the delegated-attribute path
5. Public API documentation describes the delegation behaviour

For the `__init__` initialization hazard this pattern creates when using `__getattr__`, see R10.

**Escape hatch is NOT permitted** for:
- convenience (avoiding boilerplate)
- dynamic configuration dispatch that could be expressed as named methods
- application code that does not implement a delegation pattern

---

### R8 — `__setattr__` / `__delattr__` Escape Hatch (Discouraged, Same Constraints)

Same escape hatch constraints as R7.

Default: discouraged.  
Justification required: proxy / adapter / delegation pattern with all 5 constraints from R7 satisfied.

---

### R9 — `__getattribute__` as Highest-Risk Tool

`__getattribute__` MUST NOT appear in application code without explicit architectural justification documented in code.

Even framework internals SHOULD document the rationale.

`__getattribute__` is the highest-risk mechanism on the ladder because it intercepts **all** attribute access including `self._x`, and any implementation error that accesses `self` inside `__getattribute__` will cause infinite recursion.

---

### R10 — `__init__` Initialization Pitfall (Anti-pattern, In Scope)

Any code using `__getattr__` or `__setattr__` MUST handle the `__init__` initialization order pitfall.

**Problem**: `__getattr__` is called when an attribute is not found. If `__init__` tries to set `self._data = {}` and `__setattr__` is overridden, the implementation can trigger infinite recursion before the object is initialized.

**Rule**: Inside `__getattr__` and `__setattr__`, always use `object.__getattribute__` and `object.__setattr__` for internal state access.

**Observable signal**: any `RecursionError` during `__init__` in a class that defines `__getattr__` or `__setattr__` is this pitfall.

---

## Success Measurement

A developer has applied this skill correctly when **all three signals hold**:

| Signal | Verification method |
| --- | --- |
| Weakest sufficient mechanism chosen | Verifiable in code review against the R1 ladder |
| All attribute read/write paths are statically navigable | `pyright --strict` reports no implicit `Any` on attribute access |
| No reviewer comment about "data flow invisible" after the change | Code review record |

Primary signal: **R1 mechanism selection**. Secondary signals: B and C reinforce the primary.

---

## Non-Goals (Out of Scope)

- Metaclass attribute handling
- `__new__` / object lifecycle policy (belongs to `python-class-design`)
- ORM-specific descriptor patterns (Django models, SQLAlchemy, etc.)
- Framework-grade instrumentation
- `__slots__` memory optimization (belongs to `python-class-design`)
- Schema validation frameworks
- Cross-field domain validation (belongs to domain-layer or error-handling skills)
- `functools` beyond `@cached_property` (belongs to a future `python-functools` skill)

---

## Resolved Contradictions

| Contradiction | Resolution |
| --- | --- |
| Original intent: "禁止 `__getattr__`/`__setattr__`" vs final position: discouraged with escape hatch | Stakeholder refined position during Socratic interview. Escape hatch is permitted under strict constraints (R7). Not a conflict — a precision update. |
| Original scope: "restricted `@property`-only" vs final scope: full descriptor protocol | Stakeholder explicitly confirmed scope expansion is intentional and not runaway. Both levels are now part of the skill under the R1 ladder. |

---

## Explicit Assumptions

- The skill targets Python 3.6+ environments; `@cached_property` sections require 3.8+
- Developers are assumed to use a static analysis tool (pyright or mypy) as part of their workflow
- The skill serves both package authors and application developers, with escape hatch applicability determined by pattern (proxy/delegation), not code location (library vs app)

---

## Remaining Blockers

None. All scope, success metrics, non-goals, contradictions, and extreme-boundary edge cases are resolved.

**Ready for technical translation.**
