# Custom Descriptors — R4, R5, R6

---

## R4 — Upgrade criteria: from `@property` to a custom descriptor

Do not write a custom descriptor unless `@property` is provably insufficient.
A custom descriptor is justified only when **at least one** of these three conditions
is true:

1. **Cannot reuse**: the same `__get__`/`__set__`/`__delete__` logic must apply to
   three or more attributes in the same class, and duplicating it as separate
   `@property` definitions would create an obvious maintenance burden.

2. **Cannot centralize**: the shared validation or transformation cannot be expressed
   as a single `@property` in the owner class because it must be a first-class object
   that is assigned to multiple class-level names.

3. **Cannot express priority**: the lookup priority between the descriptor and the
   instance `__dict__` must be explicitly controlled (data vs non-data distinction
   governs this — see R6).

**Upgrade signal**: if three or more attributes in the same class share identical
`@property` setter logic, the duplication is the prompt to consider a descriptor.

**Do not** write a custom descriptor:
- for a single attribute that `@property` already handles cleanly
- because descriptors "feel more professional" than properties
- to add logging or instrumentation — use a decorator instead

---

## R5 — `__set_name__`: dynamic private attribute names

Any custom descriptor intended for reuse across multiple attribute names **must**
implement `__set_name__`. Without it, the descriptor must hardcode the private backing
attribute name, making it impossible to reuse across different attribute names.

### The problem — hardcoded private name

```py
# WRONG: descriptor hardcodes the backing attribute name
class PositiveFloat:
    def __get__(self, obj: object, objtype: type | None = None) -> float:
        if obj is None:
            return self  # type: ignore[return-value]
        return obj._value          # hardcoded: always "_value"

    def __set__(self, obj: object, value: float) -> None:
        if value <= 0:
            raise ValueError(f"Must be positive, got {value!r}")
        obj._value = value         # hardcoded: always "_value"


class Shape:
    width = PositiveFloat()
    height = PositiveFloat()     # BUG: both use "_value"; they share storage!
```

Both `width` and `height` write to the same `_value` key on the instance, so they
overwrite each other. The descriptor cannot be reused.

### The fix — `__set_name__` for dynamic private names

```py
# CORRECT: __set_name__ sets a per-attribute private name
class PositiveFloat:
    def __set_name__(self, owner: type, name: str) -> None:
        self.private_name = f"_{name}"    # e.g., "_width", "_height"

    def __get__(self, obj: object, objtype: type | None = None) -> float:
        if obj is None:
            return self  # type: ignore[return-value]
        return getattr(obj, self.private_name)

    def __set__(self, obj: object, value: float) -> None:
        if value <= 0:
            raise ValueError(f"Must be positive, got {value!r}")
        setattr(obj, self.private_name, float(value))


class Shape:
    width = PositiveFloat()     # private_name = "_width"
    height = PositiveFloat()    # private_name = "_height"
```

Python calls `__set_name__` automatically when the class body is executed, passing
the owner class and the attribute name as it appears in the class body.

### When `__set_name__` applies

| Situation | Use `__set_name__`? |
| --- | --- |
| Descriptor assigned to multiple attribute names | Yes — required |
| Descriptor assigned to exactly one attribute, name known | Optional — can hardcode, but `__set_name__` is still cleaner |
| Descriptor created at runtime (not at class definition) | `__set_name__` is not called automatically; call it manually if needed |

---

## R6 — Data vs non-data descriptors

### The distinction

| Type | Defines | Lookup priority |
| --- | --- | --- |
| Data descriptor | `__get__` **and** `__set__` (or `__delete__`) | Shadows instance `__dict__` |
| Non-data descriptor | Only `__get__` | Instance `__dict__` takes priority |

### Lookup priority order

Python resolves `instance.attr` in this order:

```
1. Data descriptor from the class (or MRO)
2. Instance __dict__
3. Non-data descriptor from the class (or MRO)
4. Class __dict__ (plain class attribute)
```

This priority order is a property of the Python data model, not configurable.

### Why the distinction matters

**Data descriptor** (defines `__set__`):
- Always wins over the instance `__dict__`.
- Assigning `instance.attr = value` always calls `__set__`; the value never
  lands in `instance.__dict__` under that name.
- Use when the descriptor must enforce invariants on every write.

**Non-data descriptor** (only `__get__`):
- Instance `__dict__` wins.
- Assigning `instance.attr = value` stores the value in `instance.__dict__` and
  shadows the descriptor.
- Use when instance-level override is an intentional design choice (e.g., `@cached_property`).

### Gotcha — non-data descriptor silently overridden

```py
class Logger:
    """Non-data descriptor: only defines __get__."""
    def __get__(self, obj: object, objtype: type | None = None) -> str:
        if obj is None:
            return self  # type: ignore[return-value]
        return f"[{obj.__class__.__name__}]"


class Service:
    log_prefix = Logger()


svc = Service()
print(svc.log_prefix)          # "[Service]" — descriptor runs

svc.log_prefix = "OVERRIDE"    # stores in svc.__dict__; shadows the descriptor
print(svc.log_prefix)          # "OVERRIDE" — descriptor is bypassed!
```

If the descriptor is unexpectedly overridden by instance assignment, the root cause
is almost always this: the descriptor is non-data (no `__set__`), so the instance
`__dict__` wins.

**Fix**: add a `__set__` that raises `AttributeError` to make the descriptor a data
descriptor and prevent instance-level override:

```py
class Logger:
    def __get__(self, obj: object, objtype: type | None = None) -> str:
        if obj is None:
            return self  # type: ignore[return-value]
        return f"[{obj.__class__.__name__}]"

    def __set__(self, obj: object, value: object) -> None:
        raise AttributeError("log_prefix is read-only")
```

### Signposts

- `python-decorators` — for how `@property` itself uses the descriptor protocol internally
- `python-class-design` — for `__slots__` and how slot descriptors interact with instance `__dict__`
