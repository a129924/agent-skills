# Operator Overloading — Reference Overview

This is a navigation file. Consult `SKILL.md` for the decision process, then
follow the links below for detailed rules on each topic.

---

## Split reference files

### `references/binary-operators.md`

Covers R1, R2, R6, R7:
- Arithmetic operator families (`__add__`, `__sub__`, `__mul__`, `__truediv__`,
  `__floordiv__`, `__mod__`, `__pow__`) — when to overload vs use a named method
- Reflected operator pairing — symmetric `__radd__` / `__rsub__` rule
- `NotImplemented` dispatch vs `TypeError` — decision table and the
  `NotImplemented` vs `NotImplementedError` confusion trap
- Mixed-type arithmetic type-guard — `isinstance` check pattern

### `references/in-place-and-unary-operators.md`

Covers R3, R4:
- In-place return contract — `return self` (mutable), `return new_obj`
  (immutable), `return None` as a hard violation, pyright-enforceable annotation
- Unary purity rule — `__neg__`, `__pos__`, `__abs__` must not mutate `self`

### `references/comparison-and-ordering.md`

Covers R5, R8:
- Ordering consistency rule — semantic alignment with `__eq__` as pre-condition
  dependency owned by `python-data-model-methods`
- `@functools.total_ordering` recommendation; decorator mechanics signposted to
  `python-decorators`

---

Detailed examples for all 6 requirement paths: `examples.md`.
