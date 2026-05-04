# Mechanism Ladder — R1

The mechanism ladder is the primary decision tool for this skill.
Always start at the weakest rung. Move up only when the current rung is
demonstrably insufficient for the expressed attribute semantic.

Any rung that is skipped **must be justified in code comments or documentation**.
Unjustified skips are a signal for code review.

---

## The 7-rung ladder

```
1. plain attribute
2. @property
3. @cached_property       (Python 3.8+)
4. custom descriptor
5. __getattr__
6. __setattr__ / __delattr__
7. __getattribute__
```

---

## Rung 1 — plain attribute

**What it is**: A value assigned directly on the instance in `__init__` (or at the class level).

```py
class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y
```

**When it is sufficient**:
- No computation on read.
- No invariant to enforce on write.
- The value is mutable and its type is enforced elsewhere (e.g., by a static analysis tool).

**What forces an upgrade to rung 2**:
- The attribute must be computed from other state on every read.
- A write must be validated (e.g., must be non-negative, must match a pattern).
- The attribute should be read-only.

---

## Rung 2 — `@property`

**What it is**: A descriptor created by the `@property` built-in that intercepts attribute
get, set, and delete at the class level.

```py
class Temperature:
    def __init__(self, celsius: float) -> None:
        self._celsius = celsius

    @property
    def celsius(self) -> float:
        return self._celsius

    @celsius.setter
    def celsius(self, value: float) -> None:
        if value < -273.15:
            raise ValueError(f"Temperature below absolute zero: {value}")
        self._celsius = value
```

**When it is sufficient**:
- Single-attribute computed value (getter) or single-attribute invariant (setter).
- Logic does not need to be shared across multiple attributes in the same class.
- Python version is 3.6+.

**What forces an upgrade to rung 3**:
- The computed value is expensive and the same answer is valid across multiple calls
  (pure, no side effects on set). Caching it manually with a backing attribute is the signal.

**What forces an upgrade to rung 4**:
- Three or more attributes in the same class share identical `@property` setter logic
  that would have to be duplicated.

---

## Rung 3 — `@cached_property`

**What it is**: A non-data descriptor (Python 3.8+) that computes a value once on first
access and stores it in the instance `__dict__`, returning the cached value on subsequent
accesses.

```py
from functools import cached_property

class Document:
    def __init__(self, text: str) -> None:
        self._text = text

    @cached_property
    def word_count(self) -> int:
        return len(self._text.split())
```

**When it is sufficient**:
- The attribute is expensive to compute.
- The result is pure and idempotent (same answer as long as the input state does not change).
- The value should be stored after first access without manual backing attribute boilerplate.
- Python 3.8+ is available.

**What forces an upgrade (back to rung 2)**:
- The value must be recomputed on every access → use `@property` instead.
- The codebase targets Python 3.6 or 3.7 → use manual backing attribute with `@property`.

**What forces an upgrade to rung 4**:
- The same cached-property logic must be shared across multiple attribute names.

---

## Rung 4 — custom descriptor

**What it is**: A class that implements one or more of `__get__`, `__set__`, `__delete__`.
Instances of the descriptor class are assigned as class attributes and intercept
attribute access on all instances of the owner class.

```py
class Validated:
    def __set_name__(self, owner: type, name: str) -> None:
        self.private_name = f"_{name}"

    def __get__(self, obj: object, objtype: type | None = None) -> float:
        if obj is None:
            return self  # type: ignore[return-value]
        return getattr(obj, self.private_name)

    def __set__(self, obj: object, value: float) -> None:
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError(f"Expected non-negative number, got {value!r}")
        setattr(obj, self.private_name, float(value))
```

**When it is sufficient**:
- Reuse is the primary driver — the same `__get__`/`__set__` logic applies to
  multiple attributes in one or more classes.
- Lookup priority must be explicitly controlled (data vs non-data).

**What forces an upgrade to rung 5**:
- The attribute name is not known at class definition time — the class dynamically
  delegates attribute resolution to a wrapped object. This is a proxy/delegation
  pattern and `__getattr__` is the appropriate tool.

---

## Rung 5 — `__getattr__`

**What it is**: A special method called by Python only when normal attribute lookup
fails (the attribute is not found in the instance `__dict__` or the class hierarchy).

**When it is permitted** (escape hatch — all 5 conditions must hold):
1. The class is explicitly a proxy, adapter, delegation layer, or compatibility shim.
2. The fallback target is explicit and documented.
3. `AttributeError` is never silently swallowed.
4. Tests cover both the missing-attribute path and the delegated-attribute path.
5. Public API documentation describes the delegation behaviour.

**What forces an upgrade to rung 6**:
- The class must intercept attribute **assignment** in addition to lookup.

---

## Rung 6 — `__setattr__` / `__delattr__`

**What it is**: Special methods that intercept every attribute **assignment** or
**deletion** on an instance, including assignments inside `__init__`.

**When it is permitted** (same 5-condition escape hatch as rung 5):
- Class is a proxy, adapter, delegation layer, or compatibility shim.
- All 5 conditions from rung 5 satisfied.

**Critical hazard**: `__setattr__` intercepts `self.x = value` inside `__init__`.
Use `object.__setattr__(self, name, value)` for internal state to avoid recursion.
See `references/attribute-hooks.md` R10 for the `__init__` pitfall.

**What forces an upgrade to rung 7**:
- The class must intercept **every** attribute read, including reads of attributes
  that exist in the instance `__dict__`. This is almost never the correct solution.

---

## Rung 7 — `__getattribute__`

**What it is**: A special method that intercepts **every** attribute access, including
`self._x` and `self.__class__`. It replaces the default attribute lookup mechanism
entirely.

**When it is permitted**: Only with explicit architectural justification documented
in code. Near-absolute discouragement applies. Any implementation error that reads
`self` inside `__getattribute__` without routing through `object.__getattribute__`
causes infinite recursion.

**No "what forces an upgrade"** — `__getattribute__` is the top of the ladder.
If this rung is insufficient, the design must be reconsidered at the architectural level.

---

## Unjustified skip signal

If a rung is skipped without explanation, add one of the following to the code:

```py
# Descriptor chosen over @property: 4 attributes share identical validation logic.
# @cached_property not used: Python 3.7 target; manual _cache backing attribute used.
# __getattr__ used: this class is a compatibility shim over legacy API (see ProxyBase).
```

A code reviewer who sees a higher-rung mechanism without such a comment should
treat it as a potential design smell and ask for justification.
