# Binary Operators Reference

Covers R1, R2, R6, R7.

---

## R1 — Arithmetic Operator Families

Python maps binary arithmetic expressions to dunder methods:

| Expression | Left-hand method | Reflected method |
| ---------- | ---------------- | ---------------- |
| `a + b`    | `__add__`        | `__radd__`       |
| `a - b`    | `__sub__`        | `__rsub__`       |
| `a * b`    | `__mul__`        | `__rmul__`       |
| `a / b`    | `__truediv__`    | `__rtruediv__`   |
| `a // b`   | `__floordiv__`   | `__rfloordiv__`  |
| `a % b`    | `__mod__`        | `__rmod__`       |
| `a ** b`   | `__pow__`        | `__rpow__`       |

**When to overload vs use a named method:**
- Overload when the operation has clear mathematical or domain semantics
  (`Vector + Vector`, `Money * int`, `Duration - Duration`).
- Use a named method (`.add()`, `.scaled_by()`) when the operation requires
  additional context, has surprising semantics for the `+` symbol, or would
  confuse a reader unfamiliar with the domain.

**The `NotImplemented` obligation:** every binary arithmetic method must return
`NotImplemented` when the operand type is not supported. See R6 below.

---

## R2 — Reflected Operator Pairing

When `a + b` is evaluated and `a.__add__(b)` returns `NotImplemented`, Python
automatically tries `b.__radd__(a)`. This is the reflected operator dispatch.

**Symmetric pair rule:** any class that intends to support reflected arithmetic
must define the reflected counterpart alongside the forward method:

```python
class Money:
    def __add__(self, other: object) -> "Money":
        if not isinstance(other, Money):
            return NotImplemented
        return Money(self.amount + other.amount, self.currency)

    def __radd__(self, other: object) -> "Money":
        # Called when the left-hand type's __add__ returns NotImplemented.
        # self is the right-hand Money; other is the left-hand operand.
        if not isinstance(other, Money):
            return NotImplemented
        return Money(other.amount + self.amount, self.currency)
```

Without `__radd__`, any expression where a foreign type appears on the left
raises `TypeError` immediately, even when the operation is semantically valid.

---

## R6 — NotImplemented Dispatch vs TypeError

### Decision table

| What you return / raise      | Effect                                                          |
| ---------------------------- | --------------------------------------------------------------- |
| `return NotImplemented`      | Correct — Python tries reflected operator on right-hand operand |
| `raise TypeError(...)`       | Violation — kills dispatch chain; reflected operator never runs |
| `return None`                | Violation — Python treats `None` as the arithmetic result       |

**Rule:** when the operand is an unsupported type, always `return NotImplemented`.
Never raise or return anything else for an unsupported type.

```python
# Correct
def __add__(self, other: object) -> "Money":
    if not isinstance(other, Money):
        return NotImplemented  # Python continues: tries other.__radd__(self)
    return Money(self.amount + other.amount, self.currency)

# Violation — kills __radd__ dispatch
def __add__(self, other: object) -> "Money":
    if not isinstance(other, Money):
        raise TypeError(f"unsupported: {type(other)}")  # BAD
    return Money(self.amount + other.amount, self.currency)
```

### NotImplemented vs NotImplementedError — confusion trap

These are two completely different Python objects:

| Name                  | Kind                        | Use case                                                   |
| --------------------- | --------------------------- | ---------------------------------------------------------- |
| `NotImplemented`      | built-in singleton constant | Return from a binary/comparison dunder to signal "try the other side" |
| `NotImplementedError` | exception class             | Raise when a method is declared but its body is not yet written |

```python
# WRONG — NotImplementedError is an exception, not a dispatch signal
def __add__(self, other: object) -> "Money":
    if not isinstance(other, Money):
        raise NotImplementedError  # BAD: unhandled exception, not graceful fallback

# CORRECT
def __add__(self, other: object) -> "Money":
    if not isinstance(other, Money):
        return NotImplemented  # singleton constant — dispatch continues
    return Money(self.amount + other.amount, self.currency)
```

Returning `NotImplemented` allows Python to continue the dispatch protocol.
Raising `NotImplementedError` terminates execution with an unhandled exception.

---

## R7 — Mixed-Type Arithmetic Type-Guard

When a class legitimately accepts a foreign operand type, use an explicit
`isinstance` guard:

```python
class Money:
    def __mul__(self, other: object) -> "Money":
        if isinstance(other, int | float):
            return Money(self.amount * other, self.currency)
        return NotImplemented  # all other types fall through

    def __rmul__(self, other: object) -> "Money":
        # Handles: 3 * money_obj (int.__mul__ returns NotImplemented)
        return self.__mul__(other)
```

**Pattern:**
1. Guard accepted foreign types with `isinstance`
2. Return the computed result for accepted types
3. Return `NotImplemented` for everything else — do not raise, do not return `None`

**Boundary:** complex coercion logic (e.g., `Decimal` → `Money` conversion,
currency exchange rates) is out of scope for this skill. When coercion involves
business logic, delegate to an adapter or service layer and keep the operator
method a thin dispatch gate.
