---
name: python-comprehensions
description: Choose clear Python comprehensions and know when explicit loops or map/filter are more readable. Use this when drafting or reviewing list, dict, set comprehensions, generator expressions, and readability boundaries.
---

# Purpose
Use list, dict, and set comprehensions for single-level transformations; know when nested or complex comprehensions should become explicit loops; decide between comprehensions and functional tools like `map/filter`.

# Trigger / When to use
Use this skill when:
- code review or design must choose between a comprehension and an explicit loop
- a comprehension has become hard to read or debug
- the task must decide between comprehension and `map`/`filter`/`functools` equivalents
- the code must balance functional style with imperative clarity

Do not use this skill when:
- the task is mainly about generator functions or iterator design (use `python-generators-iterators`)
- the task is mainly about functional composition, currying, or functional style patterns (use `python-functional-style`)
- the task is only about naming, type hints, or control flow branching
- the performance analysis is the primary goal (not readability)

# Inputs
- the data structure and transformation needed
- the complexity of the filter or transformation logic
- whether the result is used once or repeated
- whether lazy evaluation matters
- team familiarity with comprehensions vs imperative code

# Process
1. Prefer single-level list/dict/set comprehensions for simple transformations (one loop, one optional filter).
2. When a comprehension would have 2+ nested loops or multiple chained filters, consider an explicit loop for clarity.
3. Judge readability by "can a maintainer understand this without mentally unrolling it?" — not by token count.
4. When the transformation is a pure `map` or `filter`, compare comprehension vs functional tool; prefer whichever reads clearest in context.
5. Use generator expressions for lazy evaluation or when memory matters; document the lazy choice if non-obvious.
6. Flag try/except blocks inside comprehensions as a design smell; refactor to explicit loops.
7. Refer to `reference.md` for readability heuristics, scoping rules, and version-specific behavior.

# Examples

**Positive (use comprehension)**:
```python
# Simple list comprehension: clear transformation
squares = [x ** 2 for x in numbers]

# Dict comprehension with filter: readable at a glance
name_to_age = {person['name']: person['age'] for person in people if person['age'] >= 18}

# Generator expression: lazy, memory-efficient
large_squares = (x ** 2 for x in huge_list)
```

**Negative (use explicit loop or reconsider)**:
```python
# Too nested (3 levels) with complex conditions; hard to parse
flattened = [
    value
    for row_group in matrix_groups
    for row in row_group
    for value in row
    if value is not None and value > 0
]
# Better: use explicit nested loops with named steps

# Side-effect comprehension: legal Python, but hides validation and intent
[results.append(int(s)) for s in strings if s.isdigit()]
# Better: explicit loop

# Chained filters that would be clearer as separate steps
filtered = [x for x in data if x > 10 if x < 100 if x % 2 == 0]
# Better: explicit loop with named intermediate filters or functools.reduce
```

# Outputs
- a review-ready decision for comprehension vs loop vs functional tool
- explicit readability criteria applied to the code
- guidance on when lazy evaluation (generator) vs eager (list) is appropriate
- awareness of variable scoping and Python 3+ semantics

# Boundaries
- Do not design or critique iterator protocols, generator functions, or lazy evaluation frameworks.
- Do not define naming policy, type-hint syntax, or strict typing rules.
- Do not define functional composition, currying, or pure-functional style patterns.
- Do not replace explicit control-flow guidance (`if/elif` choices, guard clauses).

# Local references
- `reference.md`: readability heuristics, scoping rules, performance notes, and Python 3 variable semantics
- `examples.md`: 5–8 detailed scenarios covering simple, nested, lazy, filter/map trade-offs, and anti-patterns
