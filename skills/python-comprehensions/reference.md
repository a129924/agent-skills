# Comprehensions reference

## Readability heuristics

### Rule 1: Single-level comprehensions are standard
- One loop, one optional filter: always a comprehension.
- Example: `[x * 2 for x in items if x > 0]` is clear and idiomatic.
- Scope: list, dict, and set comprehensions all follow this rule.

### Rule 2: Nested comprehensions have a limit
- Nested comprehensions are readable only up to 2 levels of indentation.
- More than one nested loop, especially with chained filters, signals an explicit loop is clearer.
- Example (readable): `[(x, y) for x in xs for y in ys]` is still clear.
- Example (borderline): `[x for sublist in data for x in sublist if x > 0]` — consider unpacking this.
- Cognitive test: "Can a maintainer unroll this mentally in one pass?" If no, refactor.

### Rule 3: Chained filters reduce readability
- Multiple `if` clauses inside a comprehension compound readability cost.
- Prefer separate filter steps or explicit loops when `if` conditions repeat or are complex.
- Example: `[x for x in data if x > 10 if x < 100]` → consider an explicit loop with named conditions.

### Rule 4: Transformation clarity trumps terseness
- Prefer a readable 3-line loop over a 1-line comprehension no one understands.
- Do not optimize for keystroke count.
- Use comprehensions when the transformation fits in one clear mental model.

## Scoping rules

### Python 3: Comprehensions have their own scope
- **In Python 3.x**, comprehension variables (loop variables, intermediate results) do **not** leak into the enclosing scope; referencing them after the comprehension raises `NameError`.
- **Key difference from Python 2**: Python 2 leaks the loop variable; Python 3 does not.
- Example (Python 3):
  ```python
  [x * 2 for x in range(10)]
  print(x)  # NameError: name 'x' is not defined (in Python 3)
  ```
- Example (Python 2 — do not rely on this):
  ```python
  [x * 2 for x in range(10)]
  print(x)  # prints 9 (last value, leaked from comprehension)
  ```

### Walrus operator (`:=`) in comprehensions
- Available only in Python 3.8+.
- The walrus operator assigns a value and returns it, useful for filtering with expensive operations.
- Example:
  ```python
  # Python 3.8+
  results = [y for x in data if (y := expensive_calc(x)) is not None]
  ```
- Keep walrus usage light; excessive use of `:=` inside comprehensions harms readability.
- Reference this only when the baseline is 3.8+ and the alternative would be less readable.

## Performance notes

### Comprehension vs explicit loop
- **Memory**: List comprehensions are eager; they build the entire list in memory. Generator expressions are lazy; they yield one item at a time.
- **Speed**: List comprehensions are slightly faster than explicit loops due to internal optimization; not a decisive factor for ordinary code.
- **When to care**: Use generator expressions for very large datasets or when the caller may not consume the entire result.

### Map/filter vs comprehension
- Functionally equivalent; readability and team familiarity should drive the choice.
- Comprehensions are usually more readable for mixed transformation and filtering.
- `map()` and `filter()` are useful when combining operations from `functools` or when the function is already defined and reused.
- Example (comprehension):
  ```python
  evens = [x for x in range(100) if x % 2 == 0]
  ```
- Example (map/filter):
  ```python
  evens = list(filter(lambda x: x % 2 == 0, range(100)))
  ```
- Comprehension is usually clearer; choose `map/filter` only if the functional flow is already dominant.

## Anti-patterns to flag

### Try/except inside comprehension
- **Smell**: Indicates error handling should happen at a different layer.
- **Refactor**: Use an explicit loop or a helper function that handles the exception.
- Example (bad, pseudo-code only — not valid Python syntax):
  ```python
  # pseudo-code: "trying" to put try/except logic inside a comprehension
  values = [int(s) for s in strings if <try: int(s) except ValueError: skip>]
  ```
- Example (better):
  ```python
  def to_int_or_none(s):
      try:
          return int(s)
      except ValueError:
          return None
  converted = (to_int_or_none(s) for s in strings)
  values = [value for value in converted if value is not None]
  ```

### Comprehension as a side-effect function
- **Smell**: A comprehension that exists only for its side effects (e.g., printing, writing to a file) is not a comprehension at all.
- **Refactor**: Use an explicit loop or `for ... in ...` statement.
- Example (bad):
  ```python
  [print(x) for x in items]  # returns a list of None
  ```
- Example (better):
  ```python
  for x in items:
      print(x)
  ```

## Navigation
- See `examples.md` for detailed scenarios: simple, nested, generator, filter/map trade-offs, set/dict comprehensions, and edge cases.
- See `SKILL.md` for the decision process and boundaries vs related skills.
