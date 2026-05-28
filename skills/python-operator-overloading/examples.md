# Operator Overloading — Examples

Six scenario sections covering all 8 requirements (R1–R8).

---

## Section 1: Binary Arithmetic — `__add__` with NotImplemented (R1, R6)

### Scenario

`Money` supports same-currency addition: `money_a + money_b`.

### Positive — correct dispatch protocol

```python
from dataclasses import dataclass


@dataclass
class Money:
    amount: float
    currency: str

    def __add__(self, other: object) -> "Money":
        if not isinstance(other, Money):
            return NotImplemented  # lets Python try other.__radd__(self)
        if self.currency != other.currency:
            raise ValueError(
                f"Currency mismatch: {self.currency} vs {other.currency}"
            )
        return Money(self.amount + other.amount, self.currency)
```

Outcome: `Money(10, "USD") + Money(5, "USD")` → `Money(15.0, "USD")`.
If `other` is not `Money`, Python receives `NotImplemented` and can still try
`other.__radd__(self)` — giving third-party types a chance to handle it.

### Negative — direct `TypeError` kills dispatch

```python
@dataclass
class Money:
    amount: float
    currency: str

    def __add__(self, other: object) -> "Money":
        if not isinstance(other, Money):
            raise TypeError(f"unsupported operand type: {type(other)}")  # WRONG
        return Money(self.amount + other.amount, self.currency)
```

Problem: any third-party type that implements `__radd__(money_obj)` can never
run. The `raise TypeError` terminates the dispatch chain immediately.

---

## Section 2: Reflected Operator — `3 + money_obj` (R2)

### Scenario

`Money` supports numeric scaling so `scalar + money_obj` and `money_obj + scalar`
are both valid. Without `__radd__`, the former always fails.

### How dispatch works for `3 + money_obj`

1. Python evaluates `3 + money_obj`.
2. `int.__add__(3, money_obj)` — `int` does not know about `Money`, returns
   `NotImplemented`.
3. Python then tries `money_obj.__radd__(3)`.
4. If `__radd__` handles `int`, the expression succeeds.

### Positive — full symmetric pair

```python
class Money:
    def __init__(self, amount: float, currency: str) -> None:
        self.amount = amount
        self.currency = currency

    def __add__(self, other: object) -> "Money":
        if isinstance(other, int | float):
            return Money(self.amount + other, self.currency)
        if isinstance(other, Money) and other.currency == self.currency:
            return Money(self.amount + other.amount, self.currency)
        return NotImplemented

    def __radd__(self, other: object) -> "Money":
        # Handles: other + self when other.__add__ returns NotImplemented.
        # Example: 3 + money_obj → int.__add__ fails → money_obj.__radd__(3)
        return self.__add__(other)

    def __repr__(self) -> str:
        return f"Money({self.amount}, {self.currency!r})"


print(Money(10.0, "USD") + 5)       # Money(15.0, 'USD')
print(3 + Money(10.0, "USD"))       # Money(13.0, 'USD') — via __radd__
```

### Negative — missing `__radd__`

```python
class Money:
    def __add__(self, other: object) -> "Money":
        if isinstance(other, int | float):
            return Money(self.amount + other, self.currency)
        if isinstance(other, Money) and other.currency == self.currency:
            return Money(self.amount + other.amount, self.currency)
        return NotImplemented

    # No __radd__ defined.


# 3 + Money(10.0, "USD")
# → int.__add__(3, money) returns NotImplemented
# → no Money.__radd__ to try
# → TypeError: unsupported operand type(s) for +: 'int' and 'Money'
```

---

## Section 3: In-Place Operator — `__iadd__` return contract (R3, R4)

### Scenario

A mutable `Counter` accumulates values via `+=`. The in-place method must
return `self`; omitting the return silently destroys the reference.

### Positive — correct `return self`

```python
class Counter:
    def __init__(self, value: int = 0) -> None:
        self.value = value

    def __iadd__(self, other: int) -> "Counter":
        if not isinstance(other, int):
            return NotImplemented  # type: ignore[return-value]
        self.value += other
        return self  # rebinds caller to the same object

    def __repr__(self) -> str:
        return f"Counter({self.value})"


c = Counter(0)
c += 5
assert c is not None       # c is still a Counter, not None
assert c.value == 5
```

### Negative — missing `return` (returns `None`)

```python
class Counter:
    def __iadd__(self, other: int) -> "Counter":
        if not isinstance(other, int):
            return NotImplemented  # type: ignore[return-value]
        self.value += other
        # Missing: return self

c = Counter(0)
c += 5
print(c)        # None — Python rebound c to the return value of __iadd__
print(c.value)  # AttributeError: 'NoneType' object has no attribute 'value'
```

### Unary purity rule (R4)

```python
class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __neg__(self) -> "Vector":
        return Vector(-self.x, -self.y)  # new object — self is unchanged

    # WRONG — mutates self:
    # def __neg__(self) -> "Vector":
    #     self.x = -self.x  # BAD: caller's v is unexpectedly changed
    #     self.y = -self.y
    #     return self
```

---

## Section 4: Comparison / Ordering — `__lt__` and `total_ordering` (R5, R8)

### Scenario

`Money` should be sortable and support all six comparison operators without
manually implementing `__le__`, `__gt__`, and `__ge__`.

### Positive — `__lt__` with `@total_ordering`

```python
from functools import total_ordering


@total_ordering
class Money:
    def __init__(self, amount: float, currency: str) -> None:
        self.amount = amount
        self.currency = currency

    # __eq__ is owned by python-data-model-methods; it must compare self.amount
    # (the same field used in __lt__) to satisfy the ordering consistency rule.

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Money):
            return NotImplemented  # type: ignore[return-value]
        return self.amount < other.amount

    # @total_ordering derives __le__, __gt__, __ge__ from __eq__ + __lt__.


m1 = Money(5.0, "USD")
m2 = Money(10.0, "USD")
print(m1 < m2)   # True
print(m1 <= m2)  # True  — derived by total_ordering
print(m1 > m2)   # False — derived by total_ordering
```

### Negative — ordering inconsistency

```python
class Item:
    def __init__(self, name: str, price: float, rank: int) -> None:
        self.name = name
        self.price = price
        self.rank = rank

    # Assume __eq__ (owned by python-data-model-methods) compares self.price.

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Item):
            return NotImplemented  # type: ignore[return-value]
        return self.rank < other.rank  # INCONSISTENT: __eq__ uses price, __lt__ uses rank
```

Problem: two items with the same price but different ranks satisfy `a == b`
(because `__eq__` compares price) but neither `a < b` nor `b < a` is `True`
(because `__lt__` compares rank). The invariant
`not (a < b) and not (b < a)  →  a == b` is violated. `sorted()` produces
results that contradict equality comparisons.

---

## Section 5: NotImplemented Dispatch — Anti-Pattern Scenarios (R6)

This section is dedicated to three distinct dispatch errors. Read carefully —
the differences are subtle but critical.

### Anti-pattern A — `raise TypeError` directly

```python
class Celsius:
    def __init__(self, degrees: float) -> None:
        self.degrees = degrees

    def __add__(self, other: object) -> "Celsius":
        if not isinstance(other, Celsius):
            raise TypeError("can only add Celsius to Celsius")  # WRONG
        return Celsius(self.degrees + other.degrees)
```

Consequence: any type that implements `__radd__` to handle `Celsius` (e.g., a
`Fahrenheit` class that knows how to convert) never gets the chance to run.

### Anti-pattern B — `raise NotImplementedError` (wrong object entirely)

```python
class Celsius:
    def __add__(self, other: object) -> "Celsius":
        if not isinstance(other, Celsius):
            raise NotImplementedError  # WRONG — this is an exception, not a signal
        return Celsius(self.degrees + other.degrees)
```

`NotImplementedError` is an exception subclassing `RuntimeError`. It signals
"this method has no implementation yet". Raising it here causes an unhandled
exception — it does not trigger the reflected operator fallback.

### Anti-pattern C — `return None`

```python
class Celsius:
    def __add__(self, other: object) -> "Celsius | None":
        if not isinstance(other, Celsius):
            return None  # WRONG — Python treats None as the arithmetic result
        return Celsius(self.degrees + other.degrees)


result = Celsius(20.0) + 5
print(result)  # None — silent data loss; no error raised
```

Python does not treat `None` as a dispatch signal. The expression evaluates to
`None`, silently destroying the result.

### Correct pattern

```python
class Celsius:
    def __add__(self, other: object) -> "Celsius":
        if not isinstance(other, Celsius):
            return NotImplemented  # singleton constant — signals "try reflected"
        return Celsius(self.degrees + other.degrees)
```

### NotImplemented quick reference

| Object                | Kind                        | Use for                                                    |
| --------------------- | --------------------------- | ---------------------------------------------------------- |
| `NotImplemented`      | built-in singleton constant | Return from dunder to allow Python's dispatch fallback     |
| `NotImplementedError` | exception class             | Raise when a method body is not yet written                |
| `TypeError`           | exception class             | Raise when the operation is definitively invalid (post-dispatch, after all fallbacks exhausted) |

---

## Section 6: Mixed-Type Arithmetic — `isinstance` Guard Pattern (R7)

### Scenario

`Money` supports multiplication by an integer or float scalar:
`Money(10, "USD") * 2` → `Money(20.0, "USD")`.

### Positive — explicit `isinstance` guard

```python
class Money:
    def __init__(self, amount: float, currency: str) -> None:
        self.amount = amount
        self.currency = currency

    def __mul__(self, other: object) -> "Money":
        if isinstance(other, int | float):
            return Money(self.amount * other, self.currency)
        return NotImplemented  # all other types fall through

    def __rmul__(self, other: object) -> "Money":
        # Handles: 3 * money_obj (int.__mul__ returns NotImplemented)
        return self.__mul__(other)

    def __repr__(self) -> str:
        return f"Money({self.amount}, {self.currency!r})"


print(Money(10.0, "USD") * 2)    # Money(20.0, 'USD')
print(3 * Money(10.0, "USD"))    # Money(30.0, 'USD') — via __rmul__
```

**Pattern:**
1. Guard accepted foreign types with `isinstance`
2. Return the computed result for accepted types
3. Return `NotImplemented` for everything else

### Negative — silent type coercion

```python
class Money:
    def __mul__(self, other: object) -> "Money":
        try:
            return Money(self.amount * float(other), self.currency)  # WRONG
        except (TypeError, ValueError):
            return NotImplemented
```

Problem: `float(other)` silently accepts strings like `"2.5"`, objects with
`__float__`, or other unexpected types. The accepted operand surface is
invisible from the method signature and hard to review.

### Boundary note

Complex coercion (e.g., `Decimal` → `float` conversions, currency exchange
rates for `Money * Money`) is out of scope for this skill. When coercion
requires business logic, delegate to an adapter or service layer and keep the
operator method a thin, readable dispatch gate.
