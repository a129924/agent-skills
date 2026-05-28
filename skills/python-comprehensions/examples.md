# Comprehensions examples

Use these detailed scenarios after `SKILL.md` and `reference.md` to clarify readability boundaries and trade-offs.

## Scenario A: Simple single-level list comprehension

**Situation**: Transform a list of numbers by squaring them.

### Use comprehension (correct)
```python
numbers = [1, 2, 3, 4, 5]
squares = [x ** 2 for x in numbers]
# Result: [1, 4, 9, 16, 25]
```

**Why**: Single transformation, clear at first glance, idiomatic Python.

### Alternative (acceptable but verbose)
```python
squares = []
for x in numbers:
    squares.append(x ** 2)
```

**When to choose the loop**: When the team is unfamiliar with comprehensions or when the logic is so simple that the overhead of a loop is negligible in a teaching context.

---

## Scenario B: Nested comprehension (readable boundary)

**Situation**: Flatten a list of lists.

### Use comprehension (correct, at the boundary)
```python
matrix = [[1, 2], [3, 4], [5, 6]]
flattened = [x for row in matrix for x in row]
# Result: [1, 2, 3, 4, 5, 6]
```

**Why**: Two-level nesting is still readable; the outer loop is clear.

### Alternative (also acceptable)
```python
flattened = []
for row in matrix:
    for x in row:
        flattened.append(x)
```

**Decision**: Comprehension here is idiomatic and concise without sacrificing clarity. The explicit loop is equally valid for a team that finds nested comprehensions hard to parse.

---

## Scenario C: Nested comprehension (too complex → use explicit loop)

**Situation**: Filter and transform a 2D matrix, then compute a derived field.

### Avoid (too dense)
```python
# Bad: Too many operations in one comprehension
result = [
    {'row': i, 'col': j, 'value': matrix[i][j] * 2}
    for i in range(len(matrix))
    for j in range(len(matrix[i]))
    if matrix[i][j] > 5
]
```

**Why it's hard to read**: Multiple operations (indexing, filtering, transformation) nested together make cognitive load high.

### Use explicit loop (correct)
```python
result = []
for i, row in enumerate(matrix):
    for j, value in enumerate(row):
        if value > 5:
            result.append({
                'row': i,
                'col': j,
                'value': value * 2,
            })
```

**Why it's better**: Each step is clear; logic is easier to debug and extend.

---

## Scenario D: Generator expression vs list comprehension

**Situation**: Process a very large list but may not consume all results.

### Use generator expression (correct for large data)
```python
huge_numbers = range(10_000_000)
large_squares = (x ** 2 for x in huge_numbers if x % 2 == 0)

# Consume lazily
for square in large_squares:
    if square > 1_000_000_000:
        break
```

**Why**: Generator expressions are lazy; memory usage is constant regardless of input size. Useful when the caller stops early.

### Use list comprehension (correct for full consumption)
```python
numbers = [1, 2, 3, 4, 5]
squares = [x ** 2 for x in numbers]
# All squares are computed immediately; results are reusable.
```

**Decision**: Generator expressions are better for:
- Streaming or online processing
- Very large datasets
- When the caller may not consume the entire sequence

List comprehensions are better for:
- Small to medium data
- Results that are iterated multiple times
- When the full result is needed before proceeding

---

## Scenario E: Comprehension vs map/filter trade-off

**Situation**: Filter numbers and apply a transformation.

### Use comprehension (correct, most readable)
```python
numbers = [1, 2, 3, 4, 5, 6]
evens_doubled = [x * 2 for x in numbers if x % 2 == 0]
# Result: [4, 8, 12]
```

**Why**: Combines filter and transform in one readable structure.

### Use map/filter (acceptable if pre-existing functions)
```python
def is_even(x):
    return x % 2 == 0

def double(x):
    return x * 2

evens_doubled = list(map(double, filter(is_even, numbers)))
# Result: [4, 8, 12]
```

**When to use map/filter**: Only if those functions already exist and are reused elsewhere. Avoid lambda inside map/filter when a comprehension would be clearer.

### Avoid (bad)
```python
# Readability is worse, not better
evens_doubled = list(map(lambda x: x * 2, filter(lambda x: x % 2 == 0, numbers)))
```

**Why**: Lambdas inside map/filter reduce readability. Comprehension is clearer.

---

## Scenario F: Set and dict comprehensions

**Situation A**: Remove duplicates from a list while transforming.

### Use set comprehension (correct)
```python
numbers = [1, 2, 2, 3, 3, 4]
unique_squares = {x ** 2 for x in numbers}
# Result: {1, 4, 9, 16}
```

**Why**: Set comprehension is idiomatic and efficient for deduplication.

**Situation B**: Build a mapping (e.g., name to age).

### Use dict comprehension (correct)
```python
people = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
]
name_to_age = {p['name']: p['age'] for p in people}
# Result: {'Alice': 30, 'Bob': 25}
```

**Why**: Dict comprehension is the natural way to build a mapping from a sequence.

### Alternative (acceptable for complex logic)
```python
name_to_age = {}
for person in people:
    if person['age'] >= 18:
        name_to_age[person['name']] = person['age']
```

**When to choose the loop**: If the logic for key/value extraction is complex or requires intermediate variables, the explicit loop is often clearer.

---

## Scenario G: Anti-pattern — try/except inside comprehension

**Situation**: Parse a list of strings as integers, skipping invalid entries.

### Avoid (anti-pattern)
```python
# Bad: try/except inside comprehension is a design smell
# (This syntax is not even valid Python, but shows the intention)
numbers = [int(s) for s in strings if error_handling_here]
```

### Refactor with helper function (correct)
```python
def try_int(s):
    try:
        return int(s)
    except ValueError:
        return None

numbers = [x for x in (try_int(s) for s in strings) if x is not None]
```

**Why it's better**: Error handling is explicit and separate from the comprehension logic.

### Refactor with explicit loop (also correct)
```python
numbers = []
for s in strings:
    try:
        numbers.append(int(s))
    except ValueError:
        pass  # Skip invalid entries
```

**Why it's better**: Clear control flow; the try/except is visually prominent.

---

## Scenario H: Edge case — scoping and walrus operator

**Situation A**: Comprehension scoping in Python 3.

### Reference
```python
# Python 3: loop variable does NOT leak into outer scope
squares = [x ** 2 for x in range(5)]
# x is not defined here in Python 3
# (In Python 2, x would be 4)
```

**Why**: Python 3 isolates comprehension scope to prevent accidental variable pollution.

**Situation B**: Using walrus operator inside comprehension (Python 3.8+).

### Use when appropriate (Python 3.8+)
```python
# Avoid repeating an expensive calculation
def expensive(x):
    return x ** 2

results = [y for x in range(10) if (y := expensive(x)) > 50]
# Results only include values where y > 50
```

**When to use walrus**: Only when an expensive operation would otherwise be evaluated twice (once in filter, once in the result).

### Avoid (too clever)
```python
# Too many walrus operators reduce readability
results = [z for x in data if (y := f(x)) and (z := g(y)) > 0]
```

**Why it's hard to read**: Multiple assignments inside the comprehension obscure the data flow.

---

## Summary of readability signals

| Pattern | Use comprehension? | Reason |
|---------|-------------------|--------|
| Single loop, simple filter | ✓ Yes | Idiomatic and clear |
| Single loop, multiple chained filters | ~ Maybe | Consider explicit loop if filters are complex |
| Two-level nesting (flat) | ✓ Yes | Still readable at boundary |
| Two-level nesting + complex logic | ✗ No | Use explicit loop for clarity |
| Try/except inside | ✗ No | Extract to helper function or explicit loop |
| Side effects (printing, writing) | ✗ No | Use explicit loop, not a comprehension |
| Very large data, lazy evaluation needed | ~ Maybe | Use generator expression instead |
| Predefined functions (map/filter) | ✓ Yes | If function is already reused, map/filter OK; else comprehension |
| Set deduplication | ✓ Yes | Set comprehension is idiomatic |
| Mapping/dict building | ✓ Yes | Dict comprehension is idiomatic |
