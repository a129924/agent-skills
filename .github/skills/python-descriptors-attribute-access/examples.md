# Examples — `python-descriptors-attribute-access`

Six branching-decision scenarios. Each section shows a correct and an incorrect
pattern with explanatory notes. Code blocks are tagged `py`.

---

## S1 — Ladder selection walkthrough

**Scenario**: a `Rectangle` class needs three attributes — `width` (validated),
`area` (computed, no storage), and `diagonal` (expensive, computed once).

**Choosing the right rung for each attribute:**

```py
from functools import cached_property
import math


class Rectangle:
    # width: needs a single-attribute invariant on write → rung 2 (@property)
    # area: computed on every read, no storage → rung 2 (@property)
    # diagonal: expensive, pure, computed once → rung 3 (@cached_property)

    def __init__(self, width: float, height: float) -> None:
        self._width = width          # backing attribute for @property
        self._height = height

    @property
    def width(self) -> float:
        return self._width

    @width.setter
    def width(self, value: float) -> None:
        if value <= 0:
            raise ValueError(f"width must be positive, got {value!r}")
        self._width = value

    @property
    def area(self) -> float:
        return self._width * self._height

    @cached_property
    def diagonal(self) -> float:
        # Expensive (simulated): computed once, stored in instance __dict__
        return math.sqrt(self._width ** 2 + self._height ** 2)
```

**Why this is correct**: each attribute uses the weakest rung sufficient for its
semantic. Plain attributes are used for `_height` (no invariant needed). No custom
descriptor is needed because no logic is shared across three or more attributes.

---

**Incorrect — skipping rungs without justification:**

```py
class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        self._store: dict[str, float] = {}
        self._store["width"] = width
        self._store["height"] = height

    def __getattr__(self, name: str) -> float:
        # convenience: avoids writing explicit @property definitions
        return self._store[name]
```

**Why this is wrong**: `__getattr__` (rung 5) is used for convenience, not because
the class is a proxy or delegation layer. None of the five escape-hatch conditions
are satisfied. IDE cannot navigate `rect.width` or `rect.area`. Use `@property`
(rung 2) instead.

---

## S2 — `@property` setter validation — in-scope vs out-of-scope

**Scenario**: a `Thermostat` class stores a `temperature` and a `max_temperature`.
Should the `temperature` setter validate against `max_temperature`?

**Correct — single-attribute invariant (absolute lower bound only):**

```py
class Thermostat:
    def __init__(self, temperature: float, max_temperature: float) -> None:
        self._temperature = temperature
        self.max_temperature = max_temperature

    @property
    def temperature(self) -> float:
        return self._temperature

    @temperature.setter
    def temperature(self, value: float) -> None:
        # Single-attribute invariant: absolute physical lower bound only.
        # The check inspects only `value` — not any other attribute.
        if value < -273.15:
            raise ValueError(f"Temperature below absolute zero: {value}")
        self._temperature = value
```

**Why this is correct**: the setter checks only the incoming `value` against an
absolute constant. It does not inspect any other attribute of `self`.

---

**Incorrect — cross-field validation in the setter:**

```py
class Thermostat:
    def __init__(self, temperature: float, max_temperature: float) -> None:
        self._temperature = temperature
        self.max_temperature = max_temperature

    @property
    def temperature(self) -> float:
        return self._temperature

    @temperature.setter
    def temperature(self, value: float) -> None:
        # WRONG: inspects self.max_temperature — a cross-field invariant
        if value > self.max_temperature:
            raise ValueError(f"Exceeds max temperature {self.max_temperature}")
        self._temperature = value
```

**Why this is wrong**: the setter inspects `self.max_temperature`, which is a
cross-field invariant. This logic belongs in a domain method or in `python-error-handling`,
not in the `@property` setter. The setter's scope is single-attribute only.

---

## S3 — Custom descriptor with `__set_name__` (before/after)

**Scenario**: a `Shape` class needs `width` and `height`, both requiring positive-float
validation. Duplicating `@property` logic twice is the upgrade signal.

**Before — duplicated `@property` without `__set_name__` (wrong approach):**

```py
class Shape:
    def __init__(self, width: float, height: float) -> None:
        self._width = width
        self._height = height

    @property
    def width(self) -> float:
        return self._width

    @width.setter
    def width(self, value: float) -> None:
        if value <= 0:
            raise ValueError(f"Must be positive: {value!r}")
        self._width = float(value)

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, value: float) -> None:
        if value <= 0:
            raise ValueError(f"Must be positive: {value!r}")   # duplicated
        self._height = float(value)
```

Identical setter logic repeated twice. Adding a third attribute (`depth`) would
require a third copy.

---

**After — custom descriptor with `__set_name__` (correct approach):**

```py
class PositiveFloat:
    """Descriptor: enforces a positive float value for a named attribute."""

    def __set_name__(self, owner: type, name: str) -> None:
        self.private_name = f"_{name}"   # "_width", "_height", etc.

    def __get__(self, obj: object, objtype: type | None = None) -> float:
        if obj is None:
            return self  # type: ignore[return-value]
        return getattr(obj, self.private_name)

    def __set__(self, obj: object, value: float) -> None:
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError(f"Must be a positive number, got {value!r}")
        setattr(obj, self.private_name, float(value))


class Shape:
    width = PositiveFloat()     # __set_name__ called: private_name = "_width"
    height = PositiveFloat()    # __set_name__ called: private_name = "_height"

    def __init__(self, width: float, height: float) -> None:
        self.width = width      # calls PositiveFloat.__set__
        self.height = height    # calls PositiveFloat.__set__
```

**Why this is correct**: `__set_name__` gives each descriptor instance a unique
private name (`_width`, `_height`). Validation logic lives in one place.
Adding `depth = PositiveFloat()` requires zero additional code.

---

## S4 — Data vs non-data descriptor lookup priority gotcha

**Scenario**: a `LoggedField` descriptor is intended to intercept all reads of
an attribute. An instance accidentally overrides it.

**The gotcha — non-data descriptor silently bypassed:**

```py
class LoggedField:
    """Intended to intercept all reads. Only defines __get__ → non-data descriptor."""

    def __set_name__(self, owner: type, name: str) -> None:
        self.name = name

    def __get__(self, obj: object, objtype: type | None = None) -> object:
        if obj is None:
            return self
        value = obj.__dict__.get(self.name)
        print(f"Reading {self.name}: {value!r}")
        return value


class Config:
    timeout = LoggedField()


cfg = Config()
cfg.__dict__["timeout"] = 30    # or: cfg.timeout = 30
print(cfg.timeout)              # prints 30, NO "Reading timeout:" log
                                # descriptor is bypassed by instance __dict__
```

**Why this happens**: `LoggedField` defines only `__get__` (non-data descriptor).
The instance `__dict__` takes priority over non-data descriptors. Once `timeout`
is in `cfg.__dict__`, the descriptor's `__get__` is never called.

---

**The fix — make it a data descriptor by adding `__set__`:**

```py
class LoggedField:
    """Data descriptor: intercepts all reads AND writes."""

    def __set_name__(self, owner: type, name: str) -> None:
        self.private_name = f"_{name}"   # store under a different key

    def __get__(self, obj: object, objtype: type | None = None) -> object:
        if obj is None:
            return self
        value = getattr(obj, self.private_name, None)
        print(f"Reading {self.private_name}: {value!r}")
        return value

    def __set__(self, obj: object, value: object) -> None:
        print(f"Writing {self.private_name}: {value!r}")
        setattr(obj, self.private_name, value)


class Config:
    timeout = LoggedField()


cfg = Config()
cfg.timeout = 30       # calls LoggedField.__set__ — "Writing _timeout: 30"
print(cfg.timeout)     # calls LoggedField.__get__ — "Reading _timeout: 30"
```

**Why this is correct**: `LoggedField` now defines both `__get__` and `__set__`
(data descriptor). Data descriptors have priority over the instance `__dict__`,
so `cfg.timeout = 30` always calls `__set__`, and subsequent reads always call
`__get__`. The backing value is stored under `_timeout`, not `timeout`.

---

## S5 — `__getattr__` escape hatch — compliant proxy vs non-compliant convenience

### Compliant — class is an explicit delegation proxy (all 5 conditions met)

```py
class ReadOnlyProxy:
    """Read-only proxy. Delegates all attribute reads to the wrapped object.

    Delegation: any attribute not defined on ReadOnlyProxy is forwarded to
    the wrapped object. Raises AttributeError with context if not found.

    Public API: callers may read any attribute available on the wrapped object.
    They may not write attributes through this proxy.
    """

    def __init__(self, target: object) -> None:
        # Use object.__setattr__ to bypass potential __setattr__ override (R10)
        object.__setattr__(self, "_target", target)

    def __setattr__(self, name: str, value: object) -> None:
        raise AttributeError(f"{type(self).__name__} is read-only")

    def __getattr__(self, name: str) -> object:
        # Condition 1: explicit proxy class
        # Condition 2: fallback target is self._target, documented above
        # Condition 3: AttributeError raised with clear message if missing
        target = object.__getattribute__(self, "_target")
        try:
            return getattr(target, name)
        except AttributeError:
            raise AttributeError(
                f"{type(self).__name__!r} proxy has no attribute {name!r} "
                f"(not found on wrapped {type(target).__name__!r})"
            ) from None
```

**Why this is compliant**:
1. ✅ Explicit proxy class with documented delegation behaviour.
2. ✅ Fallback target (`_target`) is explicit and documented in the docstring.
3. ✅ `AttributeError` propagates with a clear, informative message.
4. ✅ (Test responsibility) Tests must cover `proxy.missing_attr` → `AttributeError`
   and `proxy.real_attr` → correct value.
5. ✅ Public API documentation describes delegation (class docstring).

---

### Non-compliant — `__getattr__` for convenience

```py
class AppConfig:
    def __init__(self) -> None:
        self._settings: dict[str, object] = {
            "timeout": 30,
            "retries": 3,
        }

    def __getattr__(self, name: str) -> object:
        # Convenience: avoid writing explicit properties for each setting
        return self._settings.get(name)   # WRONG: swallows AttributeError for unknown keys
```

**Why this is non-compliant**:
- The class is not a proxy, adapter, or delegation layer.
- `.get(name)` returns `None` for unknown keys — `AttributeError` is silently swallowed.
- `cfg.timeot` (typo) returns `None` instead of raising `AttributeError` — bugs hide.
- IDE cannot resolve `cfg.timeout` statically.
- Use explicit `@property` definitions or a typed `dataclass` instead.

---

## S6 — `__init__` pitfall — `Broken` class vs `Safe` class

**Scenario**: a `Store` class intercepts all attribute writes via `__setattr__`
to log them. `__init__` tries to set up the internal `_data` dictionary.

### Broken — `__setattr__` intercepts `__init__` setup before `_data` exists

```py
class Broken:
    def __init__(self) -> None:
        self._data: dict[str, object] = {}   # calls __setattr__!

    def __setattr__(self, name: str, value: object) -> None:
        # self._data is not yet set when __init__ first runs this
        self._data[name] = value             # AttributeError: '_data' not set
                                             # or RecursionError if __getattr__
                                             # is also defined
```

**Failure mode**: `self._data[name] = value` inside `__setattr__` tries to read
`self._data`, which itself triggers `__setattr__` (or `__getattr__` if defined)
before `_data` exists → `AttributeError` or `RecursionError`.

---

### Safe — use `object.__setattr__` for internal state

```py
class Safe:
    def __init__(self) -> None:
        # Bypass __setattr__ for the internal _data dict
        object.__setattr__(self, "_data", {})

    def __setattr__(self, name: str, value: object) -> None:
        # Use object.__getattribute__ to read _data; never self._data
        data = object.__getattribute__(self, "_data")
        print(f"Setting {name!r} = {value!r}")
        data[name] = value

    def __getattr__(self, name: str) -> object:
        data = object.__getattribute__(self, "_data")
        try:
            return data[name]
        except KeyError:
            raise AttributeError(
                f"{type(self).__name__!r} has no attribute {name!r}"
            ) from None


store = Safe()
store.x = 10       # Setting 'x' = 10
print(store.x)     # 10
```

**Why this is correct**:
- `object.__setattr__(self, "_data", {})` bypasses `__setattr__` and writes
  directly to the instance `__dict__` — `_data` is available before any custom
  logic runs.
- `object.__getattribute__(self, "_data")` inside `__setattr__` reads the internal
  state without going through any overridden lookup — no recursion possible.

**Rule summary**:
- In `__init__`: use `object.__setattr__` for internal state when `__setattr__` is overridden.
- In `__setattr__` / `__getattr__`: use `object.__getattribute__` to read internal state.
- Never use `self._name` inside these methods — it re-enters the hook and risks recursion.

> This pattern is also shown in `references/attribute-hooks.md` R10 (Safe class).
