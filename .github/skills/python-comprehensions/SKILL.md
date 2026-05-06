---
name: python-comprehensions
description: Choose clear Python comprehensions and know when explicit loops or map/filter are more readable. Use this when drafting or reviewing list, dict, set comprehensions, generator expressions, and readability boundaries.
complexity: low
risk_profile: []
inputs:
  - the data structure and transformation needed
  - the complexity of the filter or transformation logic
  - whether the result is used once or repeated
  - whether lazy evaluation matters
  - team familiarity with comprehensions vs imperative code
outputs:
  - a review-ready decision for comprehension vs loop vs functional tool
  - explicit readability criteria applied to the code
  - guidance on when lazy evaluation (generator) vs eager (list) is appropriate
  - awareness of variable scoping and Python 3+ semantics
use_when:
  - code review or design must choose between a comprehension and an explicit loop
  - a comprehension has become hard to read or debug
  - the task must decide between comprehension and map/filter/functools equivalents
  - the code must balance functional style with imperative clarity
do_not_use_when:
  - the task is mainly about generator functions or iterator design (use python-generators-iterators)
  - the task is mainly about functional composition, currying, or functional style patterns
  - the task is only about naming, type hints, or control flow branching
  - performance analysis is the primary goal (not readability)
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
- the task is mainly about functional composition, currying, or functional style patterns
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

**Correct** — simple single-level comprehension, readable at a glance:
```python
squares = [x ** 2 for x in numbers]
```

**Incorrect** — comprehension used for side effects; hides intent and order:
```python
[results.append(int(s)) for s in strings if s.isdigit()]
# Better: use an explicit loop
```

See `examples.md` for detailed scenarios covering nested, lazy, and filter/map trade-offs.

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
