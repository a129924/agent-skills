# `@property` and `@cached_property` — R2, R3

---

## R2 — `@property` discipline

### What `@property` is for

`@property` is the canonical solution for two scenarios:

1. **Computed read**: the attribute value is derived from other state on every access.
2. **Single-attribute invariant**: an assignment must be validated before the value is stored.

Both scenarios are confined to **one attribute**. If the logic touches more than one
attribute or requires cross-object knowledge, `@property` is no longer sufficient.

> **Signpost**: `@property` is syntactically a decorator; the mechanics of how
> decorators wrap functions belong in `python-decorators`, not here.

---

### Getter, setter, deleter

```py
class BoundedValue:
    def __init__(self, initial: float) -> None:
        self._value = initial

    @property
    def value(self) -> float:
        """Return the current value."""
        return self._value

    @value.setter
    def value(self, new: float) -> None:
        if not 0.0 <= new <= 100.0:
            raise ValueError(f"value must be in [0, 100], got {new}")
        self._value = new

    @value.deleter
    def value(self) -> None:
        del self._value
```

Use a **deleter** only when attribute deletion is a meaningful operation in the
domain. Omit it when deletion would leave the object in an invalid state.

---

### Setter validation boundary — single-attribute invariant only

The setter is the right place to enforce an invariant **if and only if** the check
inspects no more than `self` and the incoming value.

**In scope for the setter** — single-attribute invariant:

```py
@temperature.setter
def temperature(self, value: float) -> None:
    if value < -273.15:
        raise ValueError("Temperature below absolute zero")
    self._temperature = value
```

**Out of scope for the setter** — cross-field validation:

```py
# WRONG — the setter checks another attribute (self.max_temp)
@temperature.setter
def temperature(self, value: float) -> None:
    if value > self.max_temp:          # cross-field: violates boundary
        raise ValueError("Exceeds max")
    self._temperature = value
```

> **Boundary rule**: if the setter inspects more than `self` and the incoming value,
> the validation has left `@property` jurisdiction.
>
> **Signpost**: cross-field validation, DTO-level contracts, and schema validation
> belong in `python-error-handling`.

---

### When to use vs when not to use

| Signal | Use `@property`? |
| --- | --- |
| Computed read with no side effects | Yes |
| Single-attribute invariant on write | Yes |
| Read-only attribute (no setter) | Yes |
| Logic shared across 3+ attributes | No — upgrade to custom descriptor (R4) |
| Cross-field validation | No — belongs in `python-error-handling` |
| Value computed once and stored | No — use `@cached_property` (R3) |

---

## R3 — `@cached_property`

### What `@cached_property` is for

`@cached_property` (from `functools`, Python 3.8+) is a **non-data descriptor** that:

1. Computes a value the first time the attribute is accessed.
2. Stores the result in the instance `__dict__` under the attribute name.
3. Returns the cached value on all subsequent accesses without recomputing.

Use it when the attribute is **expensive to compute**, **pure** (no side effects),
and **idempotent** (the answer does not change as long as the underlying state
does not change).

---

### Python 3.8+ version gate

`@cached_property` was introduced in Python 3.8.

| Python version | Recommendation |
| --- | --- |
| 3.8+ | Use `@cached_property` from `functools` |
| 3.6–3.7 | Use `@property` with a manual `_name` backing attribute |

For Python 3.6–3.7, the manual equivalent:

```py
class Document:
    def __init__(self, text: str) -> None:
        self._text = text
        self._word_count: int | None = None      # manual cache

    @property
    def word_count(self) -> int:
        if self._word_count is None:
            self._word_count = len(self._text.split())
        return self._word_count
```

---

### `@property` vs `@cached_property` comparison

| Criterion | `@property` | `@cached_property` |
| --- | --- | --- |
| Recomputed on every access | Yes | No — computed once, then stored |
| Stored in instance `__dict__` | No | Yes |
| Descriptor kind | Data descriptor (has `__set__` via `property`) | Non-data descriptor (no `__set__`) |
| Can be overridden by instance dict | No | Yes — instance dict takes priority |
| Supports setter | Yes | No |
| Thread-safe | Not applicable | No — race condition on first access in multi-threaded code |
| Python version | 3.0+ | 3.8+ |
| Suitable for side-effect-bearing computation | Yes | No — must be pure |

---

### Non-data descriptor behaviour of `@cached_property`

Because `@cached_property` does not define `__set__`, it is a **non-data descriptor**.
The instance `__dict__` takes priority over it.

This means:
- On first access, the descriptor's `__get__` runs and stores the result in
  `instance.__dict__[name]`.
- On subsequent accesses, Python finds the value in `instance.__dict__` and returns it
  directly, without calling the descriptor's `__get__` at all.

**Implication**: the cached value can be invalidated by deleting the key from
`instance.__dict__`:

```py
doc = Document(text="hello world")
_ = doc.word_count           # computed and stored in doc.__dict__
del doc.__dict__["word_count"]  # cache cleared; next access recomputes
```

Document this behaviour in public-API docstrings when cache invalidation is
a supported operation.

---

### When `@cached_property` is not appropriate

- The value must be recomputed on every access → use `@property`.
- The computation has side effects → use `@property`.
- The class uses `__slots__` without a `__dict__` slot → `@cached_property` will
  not work; use `@property` with a manual backing attribute. (See `python-class-design`
  for `__slots__` guidance.)
- Thread safety is required for the first-access race → add a lock or use a
  thread-safe caching approach instead.
