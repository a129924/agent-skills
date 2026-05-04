# Attribute Hooks — R7, R8, R9, R10

All hook methods covered in this file are **discouraged by default**.
Higher placement on the mechanism ladder means higher risk, higher maintenance cost,
and greater harm to IDE navigation and static analysis.

Reach for these mechanisms only when a lower rung genuinely cannot express
the required behaviour.

---

## R7 — `__getattr__`: fallback for missing attributes (discouraged)

### Default position

`__getattr__` is **discouraged** for all code.

Python calls `__getattr__` only when normal attribute lookup fails — the attribute
is not in the instance `__dict__`, the class, or any base class. This makes
`__getattr__` a fallback, not an interception mechanism.

### Why it is harmful by default

- IDE tools cannot statically resolve attributes dispatched through `__getattr__`.
- `pyright --strict` and mypy flag attributes accessed via `__getattr__` as `Any`.
- Silent `AttributeError` suppression (returning a default instead of raising)
  hides bugs and makes debugging hard.
- Infinite recursion during `__init__` is a common and non-obvious failure mode (see R10).

### Escape hatch — `__getattr__` is permitted only when ALL conditions hold

**Checklist — every item must be true before using `__getattr__`:**

1. The class is explicitly a proxy, adapter, delegation layer, or compatibility shim.
2. The fallback target is explicit and documented (not a broad "try anything" search).
3. `AttributeError` is never silently swallowed — missing attributes must raise
   `AttributeError` with a clear, informative message.
4. Tests cover both the missing-attribute path (raises `AttributeError`) and the
   delegated-attribute path (returns the correct value from the target).
5. Public API documentation describes the delegation behaviour — callers must not
   discover it by accident.

**`__getattr__` is NOT permitted for:**
- Convenience — to avoid writing explicit attributes or properties
- Dynamic configuration dispatch that could be expressed as named methods
- Application code that does not implement a delegation or proxy pattern

### Minimal compliant example

```py
class Proxy:
    """Delegates attribute access to the wrapped object.

    Any attribute not defined on Proxy itself is forwarded to self._target.
    Raises AttributeError (with context) if _target does not have the attribute.
    """

    def __init__(self, target: object) -> None:
        object.__setattr__(self, "_target", target)   # bypass __setattr__ (R10)

    def __getattr__(self, name: str) -> object:
        # Condition 2: fallback target is explicit (_target)
        # Condition 3: AttributeError propagates naturally from getattr
        try:
            return getattr(object.__getattribute__(self, "_target"), name)
        except AttributeError:
            raise AttributeError(
                f"{type(self).__name__!r} proxy has no attribute {name!r}"
            ) from None
```

---

## R8 — `__setattr__` / `__delattr__`: intercepts all assignment (discouraged)

### Default position

`__setattr__` and `__delattr__` are **discouraged** for all code.

`__setattr__` intercepts **every** attribute assignment on the instance, including
assignments inside `__init__`. This makes it more invasive than `__getattr__` and
creates a higher risk of `__init__` pitfalls (see R10).

`__delattr__` intercepts every attribute deletion. The same constraints apply.

### Escape hatch — same 5-condition checklist as R7

**Checklist — every item must be true before using `__setattr__` or `__delattr__`:**

1. The class is explicitly a proxy, adapter, delegation layer, or compatibility shim.
2. The fallback target is explicit and documented.
3. `AttributeError` is never silently swallowed.
4. Tests cover both the missing-attribute path and the delegated-attribute path.
5. Public API documentation describes the delegation behaviour.

**`__setattr__` / `__delattr__` are NOT permitted for:**
- Logging or auditing attribute writes (use a custom descriptor on the specific attribute)
- Input coercion on all attributes (use a custom descriptor per attribute)
- Any pattern that `@property` or a custom descriptor on specific attributes can express

### Critical constraint — internal state in `__setattr__`

When `__setattr__` is defined, `self.name = value` inside `__init__` calls
`__setattr__`. If `__setattr__` tries to read `self._target` before `_target`
has been set, the result is `AttributeError` or infinite recursion.

**Always use `object.__setattr__` for internal state assignment.** See R10.

---

## R9 — `__getattribute__`: intercepts ALL attribute access (near-absolute discouragement)

### Default position

`__getattribute__` is the **highest-risk mechanism on the ladder**.

It is **near-absolutely discouraged**. It must not appear in application code
without explicit architectural justification documented in code.
Even framework internals should document the rationale.

### Why near-absolute discouragement applies

`__getattribute__` replaces the entire default attribute lookup mechanism.
Every attribute access — including `self._x`, `self.__class__`, `self.__dict__` —
goes through it.

Any implementation error that accesses `self` inside `__getattribute__` without
routing through `object.__getattribute__` causes **infinite recursion**:

```py
class Bad:
    def __getattribute__(self, name: str) -> object:
        print(f"access: {name}")          # OK
        return self.__dict__[name]        # INFINITE RECURSION: self.__dict__
                                          # calls __getattribute__ again
```

The correct form always routes internal reads through `object.__getattribute__`:

```py
class Instrumented:
    """Intercepts ALL attribute access. Requires architectural justification.

    Rationale: this class is the root instrumentation hook for the tracing
    framework; no lower rung can intercept reads of pre-existing attributes.
    See ADR-42.
    """

    def __getattribute__(self, name: str) -> object:
        value = object.__getattribute__(self, name)   # bypass recursion
        # … instrumentation logic …
        return value
```

### When `__getattribute__` might be justified

Only when the requirement is to intercept reads of attributes that **already exist**
in the instance `__dict__` or class hierarchy — which `__getattr__` cannot do.
Even then, seriously consider whether a custom data descriptor on specific
attributes is sufficient.

If you believe `__getattribute__` is necessary:
1. Document the architectural justification in the class docstring.
2. Reference a design decision record (ADR or equivalent) if available.
3. Route all internal state reads through `object.__getattribute__`.

---

## R10 — `__init__` initialization pitfall

### The problem

When `__getattr__` or `__setattr__` is defined, `__init__` runs in an environment
where attribute access and assignment are already intercepted. This creates a
non-obvious failure mode:

```py
# BROKEN: __setattr__ intercepts self._data = {} before _data exists
class Broken:
    def __init__(self) -> None:
        self._data: dict[str, object] = {}   # triggers __setattr__

    def __setattr__(self, name: str, value: object) -> None:
        self._data[name] = value              # reads self._data — not set yet!
                                             # → AttributeError or RecursionError
```

**Observable signal**: any `RecursionError` or `AttributeError` during `__init__`
in a class that defines `__getattr__` or `__setattr__` is almost certainly this pitfall.

### The fix — use `object.__setattr__` and `object.__getattribute__` for internal state

```py
# SAFE: internal state bypasses the overridden __setattr__
class Safe:
    def __init__(self) -> None:
        object.__setattr__(self, "_data", {})   # bypass __setattr__

    def __setattr__(self, name: str, value: object) -> None:
        data = object.__getattribute__(self, "_data")   # bypass __getattribute__
        data[name] = value

    def __getattr__(self, name: str) -> object:
        data = object.__getattribute__(self, "_data")   # bypass __getattribute__
        try:
            return data[name]
        except KeyError:
            raise AttributeError(
                f"{type(self).__name__!r} has no attribute {name!r}"
            ) from None
```

### Rules

- Inside `__getattr__`: use `object.__getattribute__(self, name)` to read
  internal state, never `self._name`.
- Inside `__setattr__`: use `object.__setattr__(self, name, value)` to write
  internal state, never `self._name = value`.
- In `__init__`: use `object.__setattr__(self, name, value)` for every internal
  state assignment when `__setattr__` is overridden.

> **Signpost**: this section covers the attribute-hook-specific initialization
> hazard only. For general `__init__` construction rules, parameter ordering,
> and super() discipline, see `python-data-model-methods`.
