---
name: python-control-flow
description: Choose clear general-purpose Python branching patterns. Use this when drafting or reviewing `if/elif`, `match/case`, guard clauses, and truthiness rules.
---

# Purpose
Choose readable Python control flow without turning every branch into the same style.

# Trigger / When to use
Use this skill when:
- code review or design work must choose between `if/elif` and `match/case`
- a function may benefit from guard clauses or flatter early exits
- a condition may need explicit checks instead of plain truthiness

Do not use this skill when:
- the task is mainly about naming, type-hint syntax, or model selection
- the task is mainly about ternary expressions, walrus, or comprehension style
- the task is mainly about framework or DDD-specific workflow policy

# Inputs
- the branch subject or predicate
- whether the subject is closed and owned
- whether `None`, empty values, and `False` mean different things
- whether cleanup, resource lifetime, or symmetry matters
- any package-specific skill that defines its own exhaustive branching subject

# Process
1. Choose `match/case` for clear closed dispatch on one subject; keep `if/elif` for composite, range-based, unrelated, or guard-heavy branching.
2. Keep tiny closed splits as `if` / `else` or explicit checks instead of forcing `match/case`.
3. Prefer explicit checks when `None`, empty values, and `False` differ; default custom truthy/falsy objects to explicit checks.
4. Prefer guard clauses for failed preconditions and early exits, but let cleanup symmetry and readability override that preference.
5. Put edge notes, anti-patterns, `case _:` guidance, and package-specific override examples in `examples.md`.

# Examples
- Positive: Use `match/case` for an `Enum` status dispatch, use guard clauses for invalid input, and use `is None` when `0` is still a valid value.
- Negative: Force `match/case` for a simple `bool`, rely on `if timeout:` when `0` is meaningful, or keep the main path under `else` after a guard already returns.

# Outputs
- a review-ready control-flow rule set or skill draft
- a branch-selection matrix with explicit default choices and exceptions
- local examples for common cases and ambiguous edges

# Boundaries
- Do not define naming, strict typing syntax, or model-selection policy.
- Do not make pyright the only reason to choose `match/case`.
- Do not define ternary, walrus, branch-heavy comprehension, or DDD flow rules.

# Local references
- `examples.md`: branch examples, edge notes, anti-patterns, and split signals
