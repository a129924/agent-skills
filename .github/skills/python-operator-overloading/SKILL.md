---
name: python-operator-overloading
description: Defines Python operator overloading rules for binary arithmetic contracts, reflected operator pairing, in-place return semantics, unary operator purity, comparison ordering consistency, and the NotImplemented dispatch protocol.
---

# Purpose

Guide Python developers to implement operator overloading correctly: when to
overload versus using a named method, how to complete the two-sided dispatch
contract (`__add__` / `__radd__`, `return NotImplemented` vs `raise TypeError`),
and how to keep comparison and ordering semantically consistent.

# Trigger / When to use

Use this skill when:
- A class defines any of `__add__`, `__sub__`, `__mul__`, `__truediv__`,
  `__floordiv__`, `__mod__`, or `__pow__`
- A class defines `__iadd__`, `__imul__`, or other in-place operators
- A class defines `__neg__`, `__pos__`, or `__abs__`
- A class defines `__lt__`, `__le__`, `__gt__`, or `__ge__`
- Mixed-type arithmetic must interoperate with a foreign type (`Money * int`)
- A reviewer is checking whether an operator implementation handles unsupported
  types correctly

Do not use this skill when:
- The question is about `__eq__` or `__hash__` definition → use `python-data-model-methods`
- The question is about mutable vs immutable class design → use `python-class-design`
- The question is about `@functools.total_ordering` decorator mechanics → use `python-decorators`
- The operator is framework-specific (SQLAlchemy, NumPy broadcasting, etc.)

# Inputs

- The class definition and the operator methods under review or authorship
- The types the operator is expected to accept (same-type, mixed-type, or unknown)
- Whether the class is mutable or immutable (relevant for in-place return contract)
- Whether the class must support reflected arithmetic (e.g., `3 + obj`)
- Whether the class should be fully ordered (sort key, comparison operators)

# Process

1. **Decide whether to overload at all.** Overload when the operation has clear
   mathematical or domain semantics (`Vector + Vector`, `Money * int`). Use a
   named method (`.add()`, `.scaled_by()`) when the meaning is ambiguous.

2. **Return `NotImplemented` for unsupported types — never raise `TypeError` directly.**
   `TypeError` kills the dispatch chain; `NotImplemented` lets Python try the
   reflected operator on the other operand. See
   `references/binary-operators.md` § NotImplemented Dispatch.

3. **Check reflected operator pairing.** Every `__add__` that may receive a
   foreign left-hand operand must be accompanied by `__radd__`. Without `__radd__`,
   `3 + money_obj` raises `TypeError` even when the operation is valid.
   See `references/binary-operators.md` § Reflected Operator Pairing.

4. **Apply the `isinstance` guard for mixed-type arithmetic.** Guard with
   `isinstance`, handle the accepted type, and return `NotImplemented` for all
   others. Never rely on implicit coercion.
   See `references/binary-operators.md` § Mixed-Type Guard.

5. **Verify in-place operator return contract.** `__iadd__` and similar must
   return `self` (mutable) or a new object (immutable). Returning `None`
   (implicit fall-through) silently rebinds the caller's variable to `None`.
   Annotate with an explicit return type (e.g., `-> MyType`) so pyright enforces
   this. See `references/in-place-and-unary-operators.md`.

6. **Verify unary operator purity.** `__neg__`, `__pos__`, and `__abs__` must
   not mutate `self`; return a new object every time.
   See `references/in-place-and-unary-operators.md`.

7. **Check ordering consistency with `__eq__`.** Verify the invariant:
   `not (a < b) and not (b < a)` must imply `a == b`. `__eq__` is a
   pre-condition owned by `python-data-model-methods`.
   See `references/comparison-and-ordering.md`.

8. **Recommend `@functools.total_ordering` when appropriate.** If the class
   defines `__eq__` and exactly one ordering method, recommend
   `@functools.total_ordering` to complete the contract. For decorator
   mechanics, signpost to `python-decorators`.

# Examples

**Positive — correct `NotImplemented` return:**
```python
class Money:
    def __add__(self, other: object) -> "Money":
        if not isinstance(other, Money):
            return NotImplemented  # lets Python try other.__radd__(self)
        return Money(self.amount + other.amount, self.currency)
```

**Negative — premature `TypeError` kills reflected dispatch:**
```python
class Money:
    def __add__(self, other: object) -> "Money":
        if not isinstance(other, Money):
            raise TypeError(f"unsupported type: {type(other)}")  # BAD
        return Money(self.amount + other.amount, self.currency)
```

# Outputs

- Operator methods that return `NotImplemented` for unsupported types
- Reflected operator pairs (`__add__` / `__radd__`) where mixed-type left-hand
  arithmetic is intended
- In-place operator methods with explicit `return self` or `return new_obj`
- Unary operators that return new objects without mutating `self`
- Ordering operators semantically consistent with the class's `__eq__`

# Boundaries

- **`python-data-model-methods`** — owns `__eq__` and `__hash__`. This skill
  treats `__eq__` as an external pre-condition for ordering consistency. Do not
  define or redefine `__eq__` using this skill.
- **`python-class-design`** — owns mutable vs immutable class design. This skill
  owns only the in-place operator return syntax contract; consult
  `python-class-design` for whether a class should be mutable at all.
- **`python-decorators`** — owns `@functools.total_ordering` decorator mechanics.
  This skill recommends using it; for how it works, consult `python-decorators`.
- Framework-specific operators (SQLAlchemy `==` expressions, NumPy broadcasting)
  are out of scope.
- Complex cross-type coercion (currency conversion, unit normalization) is out
  of scope; delegate to an adapter or service layer.
- Inherited operator MRO resolution is out of scope; consult `python-class-design`.

# Local references

- `reference.md`: navigation overview listing all three split reference files
  and their topic coverage
- `references/binary-operators.md`: R1, R2, R6, R7 — arithmetic operator
  families, reflected operator pairing, `NotImplemented` dispatch rules, and
  mixed-type arithmetic type-guard
- `references/in-place-and-unary-operators.md`: R3, R4 — in-place return
  contract (`return self` vs `return new_obj` vs forbidden `return None`) and
  unary operator purity rule
- `references/comparison-and-ordering.md`: R5, R8 — ordering consistency rule,
  `__eq__` as pre-condition dependency, and `@functools.total_ordering`
  recommendation
- `examples.md`: 6 scenario sections covering all 8 requirements; required for
  this branching multi-path skill
