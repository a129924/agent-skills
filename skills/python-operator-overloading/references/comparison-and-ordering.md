# Comparison and Ordering Reference

Covers R5, R8.

---

## R5 — Ordering Consistency Rule

When a class defines any of `__lt__`, `__le__`, `__gt__`, or `__ge__`, the
ordering semantics must be consistent with the class's existing `__eq__`.

**Consistency invariant:**
```
not (a < b) and not (b < a)  →  must imply  a == b
```

Violation: `a == b` returns `True` but the ordering methods use different fields
or logic, causing `sorted()` to produce results that contradict equality checks.

### Cross-skill dependency

`__eq__` is owned by `python-data-model-methods`. This skill treats it as an
**external pre-condition**: the ordering methods defined under this skill must
align with whatever `__eq__` the class already has. Do not define `__eq__` here.

### Reviewer acceptance check

For any class that defines ordering operators, a reviewer can verify consistency
by checking three questions in one screen:

1. What fields (or derived values) does `__eq__` compare?
2. Do the ordering methods compare the same fields?
3. Is there any field used in `__lt__` but absent from `__eq__`, or vice versa?

If the answers to 1 and 2 are consistent and 3 is "no", the ordering contract
is satisfied.

---

## R8 — @functools.total_ordering Recommendation

If a class defines `__eq__` and exactly one ordering method (`__lt__`, `__le__`,
`__gt__`, or `__ge__`), Python cannot derive the remaining three comparison
methods automatically. Calling `>=` on such an object raises `TypeError` at
runtime even though `<` works.

**Failure scenario:**
```python
class Money:
    def __lt__(self, other: object) -> bool: ...
    # __le__, __gt__, __ge__ not defined

sorted([m1, m2, m3])  # works — sort uses __lt__ internally
m1 >= m2              # raises TypeError — __ge__ is not defined
```

**Recommendation:** decorate the class with `@functools.total_ordering` to
complete the ordering contract from a minimal `__eq__` + one ordering method:

```python
from functools import total_ordering

@total_ordering
class Money:
    # __eq__ is defined elsewhere (python-data-model-methods).
    # It must compare the same field used in __lt__ to satisfy the consistency rule.

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Money):
            return NotImplemented  # type: ignore[return-value]
        return self.amount < other.amount

    # @total_ordering fills in __le__, __gt__, __ge__ automatically.
```

**Boundary:** the mechanism of `@functools.total_ordering` — how it wraps
methods, its performance characteristics, and its interaction with `__eq__` at
the decorator level — is owned by `python-decorators`. This skill recommends
using it as a semantic completion tool; consult `python-decorators` for decorator
mechanics.
