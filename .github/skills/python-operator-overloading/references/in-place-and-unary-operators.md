# In-Place and Unary Operators Reference

Covers R3, R4.

---

## R3 — In-Place Operator Return Contract

In-place operators (`__iadd__`, `__isub__`, `__imul__`, `__itruediv__`, etc.)
are invoked when Python evaluates `a += b`. After the call, Python **rebinds `a`
to the return value** of `a.__iadd__(b)`.

### Valid return forms

| Object kind | Correct return  | Reason                                              |
| ----------- | --------------- | --------------------------------------------------- |
| Mutable     | `return self`   | Mutation happened in-place; the same object remains valid |
| Immutable   | `return new_obj`| Cannot mutate; must produce and return the new value |
| Any         | implicit `None` | **Hard violation** — caller's variable is rebound to `None` |

### Hard violation: implicit return None

```python
# BROKEN — missing return self
class Counter:
    def __iadd__(self, other: int) -> "Counter":
        self.value += other
        # No return statement — Python implicitly returns None

counter = Counter(0)
counter += 1
# counter is now None — silent data loss
print(counter.value)  # AttributeError: 'NoneType' object has no attribute 'value'
```

```python
# CORRECT
class Counter:
    def __iadd__(self, other: int) -> "Counter":
        self.value += other
        return self  # rebinds caller to the same Counter object
```

### Immutable in-place contract

```python
# Correct for an immutable value type
class FrozenCounter:
    def __init__(self, value: int) -> None:
        self._value = value

    def __iadd__(self, other: int) -> "FrozenCounter":
        return FrozenCounter(self._value + other)  # new object; self is unchanged
```

### Pyright-enforceable form

Annotate in-place methods with an explicit return type. `pyright` in strict mode
flags a missing `return` when the declared return type is not `None`:

```python
class Counter:
    def __iadd__(self, other: int) -> "Counter":  # explicit return type
        self.value += other
        return self  # pyright enforces this; omitting it is a type error
```

**Note:** whether your class *should* be mutable is a design question owned by
`python-class-design`. This skill owns only the return-syntax contract.

---

## R4 — Unary Operator Purity Rule

Unary operators (`__neg__`, `__pos__`, `__abs__`) must be **pure**:
- They must **not** mutate `self`
- They must **return a new object**

```python
# Correct — pure unary operators
class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __neg__(self) -> "Vector":
        return Vector(-self.x, -self.y)  # new object; self is unchanged

    def __abs__(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5  # scalar result; self is unchanged
```

```python
# BROKEN — mutates self (violates purity rule)
class Vector:
    def __neg__(self) -> "Vector":
        self.x = -self.x  # BAD: mutates self
        self.y = -self.y
        return self
```

**Why purity matters:** a caller writing `-v` does not expect `v` itself to
change. Mutation inside a unary operator breaks composition, makes tests
non-reproducible, and violates the principle of least surprise.
