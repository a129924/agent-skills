---
name: python-descriptors-attribute-access
description: Choose and design Python attribute access mechanisms using the least-powerful-sufficient ladder — from plain attributes through @property, @cached_property, custom descriptors, and attribute hook methods — with strict discouragement of __getattr__, __setattr__, and __getattribute__.
---

# Purpose

Guide Python developers to select the **weakest attribute access mechanism** that correctly expresses the intended attribute semantics, while preserving code readability, maintainability, and IDE static navigation.

The skill covers:
- `@property` / getter / setter / deleter discipline
- `@cached_property` for lazy computed attributes (Python 3.8+)
- Custom descriptor protocol (`__get__`, `__set__`, `__delete__`, `__set_name__`)
- Data vs non-data descriptor lookup priority
- `__getattr__`, `__setattr__`, `__delattr__` — discouraged; permitted only under strict escape-hatch conditions
- `__getattribute__` — highest-risk; near-absolute discouragement
- `__init__` initialization pitfall when hook methods are present

# Trigger / When to use

Use this skill when:
- Choosing between plain attributes, `@property`, `@cached_property`, or a custom descriptor for a new attribute
- Reviewing code that uses `__getattr__`, `__setattr__`, or `__getattribute__`
- Designing a descriptor class intended for reuse across multiple attribute names
- Implementing a proxy, adapter, or delegation layer that requires attribute hook methods
- A code review flags "data flow invisible" or "IDE cannot navigate this attribute"
- A `RecursionError` during `__init__` suggests an attribute hook pitfall

Do **not** use this skill when:
- Choosing between `__slots__` vs instance `__dict__` → use `python-class-design`
- Implementing cross-field or DTO-level validation logic → use `python-error-handling`
- Understanding how the `@property` decorator wraps functions at the language level → use `python-decorators`
- Designing `__init__` or object construction rules beyond the attribute-hook pitfall → use `python-data-model-methods`
- Configuring ORM-specific descriptor patterns (Django, SQLAlchemy)
- Implementing metaclass attribute handling

# Inputs

- The attribute's intended access semantics (read-only, read-write, lazy, shared validation)
- Whether the attribute logic must be reused across multiple class attributes
- Whether the class is a proxy, adapter, or delegation layer
- The Python version floor of the target codebase (example syntax requires Python 3.10+; `@cached_property` requires Python 3.8+; the core descriptor protocol itself is available from Python 3.6+)
- Any static analysis tools in use (pyright, mypy)

# Process

Apply the **R1 mechanism selection ladder** as the primary decision entry point. Always start at the weakest rung and move up only when the current rung is insufficient:

```
1. plain attribute       — value stored directly on the instance
2. @property             — controlled read/write with invariant enforcement
3. @cached_property      — lazy, computed-once, pure (Python 3.8+)
4. custom descriptor     — reusable __get__/__set__/__delete__ across attributes
5. __getattr__           — discouraged; fallback for missing attributes only
6. __setattr__ / __delattr__ — discouraged; intercept all attribute assignment and deletion
7. __getattribute__      — highest-risk; intercepts ALL attribute access including self._x
```

For each attribute under design or review:

1. **Start at rung 1.** Ask: is a plain attribute sufficient? If yes, stop.
2. **Move to rung 2 (`@property`)** only if computed access or single-attribute invariant enforcement is needed. The setter boundary is single-attribute only — cross-field validation belongs in `python-error-handling`.
3. **Move to rung 3 (`@cached_property`)** only if the value is expensive to compute, pure, and should be stored after first access. Requires Python 3.8+.
4. **Move to rung 4 (custom descriptor)** only if `@property` logic must be reused across three or more attributes, or if lookup priority must be explicitly controlled.
5. **Move to rungs 5–6 (`__getattr__` / `__setattr__` / `__delattr__`)** only if the class is a proxy, adapter, delegation layer, or compatibility shim **and** all five escape-hatch conditions are satisfied (see `references/attribute-hooks.md`).
6. **Move to rung 7 (`__getattribute__`)** only with explicit architectural justification documented in code. Near-absolute discouragement applies.

Any ladder skip must be justified in code comments or documentation.

# Examples
**Correct — `@property` for single-attribute invariant:**
```py
@property
def radius(self) -> float: return self._radius
@radius.setter
def radius(self, value: float) -> None:
    if value < 0:
        raise ValueError("radius must be non-negative")
    self._radius = value
```
Single-attribute invariant on `radius`; no custom descriptor needed.
**Incorrect — `__getattr__` for convenience:**
```py
def __getattr__(self, name: str) -> str:
    return self._data.get(name, "")  # convenience, not proxy
```
`__getattr__` for convenience hides data flow; IDE cannot navigate attributes. Use explicit attributes.

# Outputs

- An attribute access implementation using the weakest sufficient mechanism
- All attribute read/write paths statically navigable (`pyright --strict` reports no implicit `Any`)
- Any ladder skip justified in code comments or documentation
- Escape hatch conditions documented if `__getattr__` / `__setattr__` / `__getattribute__` are used

# Boundaries

- `@cached_property` requires **Python 3.8+**. For Python 3.6–3.7 codebases, use a manual backing attribute with `@property`. The example code in this skill uses Python 3.10+ type-annotation syntax (`dict[str, T]`, `X | Y` unions); for older version floors substitute `Dict[str, T]` and `Optional[T]` from `typing`.
- Setter validation scope: single-attribute invariant only. If the setter inspects more than `self` and the incoming value, the logic belongs in `python-error-handling`.
- `__slots__` decisions and memory optimization belong in `python-class-design`.
- `__new__` and object construction lifecycle belong in `python-class-design`.
- Cross-field and DTO-level validation belong in `python-error-handling`.
- `@property` decorator mechanics (how decorators wrap functions at the language level) belong in `python-decorators`.
- General `__init__` construction rules belong in `python-data-model-methods`; this skill covers only the attribute-hook-specific initialization pitfall (R10).
- Metaclass attribute handling is out of scope.
- ORM-specific descriptor patterns (Django models, SQLAlchemy Column) are out of scope.

**Cross-skill signposts:**
- `python-decorators` — for `@property` decorator-protocol mechanics
- `python-class-design` — for `__slots__`, `__new__`, immutability decisions
- `python-error-handling` — for cross-field validation and domain-layer contracts
- `python-data-model-methods` — for `__init__` construction rules and `__eq__`/`__hash__` design

# Local references

- `reference.md`: navigation index — short overview pointing to the four topic-specific reference files
- `references/mechanism-ladder.md`: R1 — 7-rung decision ladder with per-rung upgrade criteria and unjustified-skip signal
- `references/property-and-cached-property.md`: R2 — `@property` discipline (getter/setter/deleter, invariant boundary); R3 — `@cached_property` lazy attributes, comparison table, Python 3.8+ gate
- `references/custom-descriptors.md`: R4 — upgrade criteria from `@property` to custom descriptor; R5 — `__set_name__` before/after example; R6 — data vs non-data descriptor lookup priority table and gotcha example
- `references/attribute-hooks.md`: R7 — `__getattr__` 5-condition escape hatch checklist; R8 — `__setattr__`/`__delattr__` same constraints; R9 — `__getattribute__` near-absolute discouragement; R10 — `__init__` pitfall with `object.__getattribute__`/`object.__setattr__` solution
- `examples.md`: required — six branching-decision scenarios with correct/incorrect code pairs covering ladder selection, setter validation, custom descriptors, lookup priority, escape hatch, and `__init__` pitfall
