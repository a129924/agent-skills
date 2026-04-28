# Python Generators and Iterators Reference

This reference layer covers the mainline rules for choosing and designing Python iteration patterns.

## Reference Files

- `reference.md` (this file): focused overview and navigation entry
- Additional split reference files only if breadth exceeds three major topics

## Navigation

- **Mainline iteration semantics**: concrete versus generator choice, generator function versus expression, and `yield` / `yield from` discipline
- **Iterator protocol**: when to implement `__iter__` and `__next__` versus using a generator function
- **Exhaustion and state**: single-pass versus multi-pass expectations, reset capability, and side-effect documentation
- See `examples.md` for layered examples and anti-patterns

## Mainline iteration semantics

### Concrete collection versus generator choice

**Mainline rule**: Return a concrete collection (list, tuple, set) as the default. Use a generator only when:

1. The caller will iterate once
2. The collection is large, infinite, or expensive to compute
3. Eager evaluation would consume significant memory or CPU

**Why this rule**: Concrete collections are simpler, re-usable, and debuggable. Generators are a performance and design tool, not a style choice.

**Anti-pattern**: `return (x * 2 for x in data)` when `data` is small and the caller will iterate multiple times.

### Generator function versus generator expression choice

**Mainline rule**:

- Use a **generator function** when:
  - Logic requires helper steps, state tracking, or conditionals
  - Readability benefits from multiple lines and clear function intent
  - Setup or cleanup is needed before production starts

- Use a **generator expression** only when:
  - Transformation is simple (like a list comprehension, but lazy)
  - Logic fits in one readable line
  - No state or helper functions are involved

**Why this rule**: Generator functions are explicit, debuggable, and support complex logic. Generator expressions are light and Pythonic only for simple cases.

**Anti-pattern**: Complex multi-line logic hidden inside a generator expression.

### `yield` and `yield from` discipline

**Mainline rule**:

- Use `yield` to produce one value at a time
- Use `yield from` to delegate to a sub-generator, avoiding manual loops
- Do not use `yield` in a loop when `yield from` would be clearer

**Why this rule**: `yield from` makes delegation explicit and avoids off-by-one errors in manual iteration.

**Anti-pattern**:
```python
# bad
def flatten(nested):
    for item in nested:
        for subitem in item:
            yield subitem

# good
def flatten(nested):
    for item in nested:
        yield from item
```

## Iterator protocol

### When to implement `__iter__` and `__next__`

**Mainline rule**: Use a generator function or expression unless you need custom iterator behavior such as:

1. **Reset capability**: The caller wants to iterate the same data multiple times
2. **Complex state**: Iterator maintains internal state that does not fit a simple generator
3. **Compatibility**: Code expects `isinstance(obj, Iterator)` checks or protocol inspection

**Why this rule**: Generator functions are simpler and handle most use cases. Custom iterators add code without benefit unless one of the above applies.

**Anti-pattern**:
```python
# bad - unnecessary custom iterator for simple production
class CountUp:
    def __init__(self, max):
        self.max = max
        self.current = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current >= self.max:
            raise StopIteration
        self.current += 1
        return self.current

# good - generator function
def count_up(max):
    for i in range(1, max + 1):
        yield i
```

### Stateful iteration and reset

**Mainline rule**: If code needs to iterate the same data multiple times, either:

1. Return a concrete collection
2. Accept a callable that returns a fresh generator each time
3. Implement `__iter__` to return a new iterator object (not `self`)

**Why this rule**: A generator is single-pass by design. Forcing multi-pass behavior requires explicit reset capability to avoid surprises.

## Exhaustion and side effects

### Single-pass expectations

**Mainline rule**: Document or enforce that a returned generator can only be iterated once. If code iterates multiple times, explicitly convert to a list or use a callable factory.

**Why this rule**: Generator exhaustion is a common source of silent bugs.

### Side effects and lazy I/O

**Mainline rule**: Any iteration with side effects (database queries, file I/O, network calls, external state mutations) must be:

1. Documented explicitly in the function docstring
2. Obvious at the call site (not buried in a helper)
3. Ideally made eager and explicit instead of lazy

**Why this rule**: Lazy side effects surprise callers and make debugging hard.

**Anti-pattern**:
```python
# bad - hidden lazy I/O
def load_users():
    for user_id in user_ids:
        yield database.query(f"SELECT * FROM users WHERE id = {user_id}")

# good - explicit eagerness
def load_users():
    return [database.query(f"SELECT * FROM users WHERE id = {user_id}") for user_id in user_ids]
```

## Anti-patterns

1. **Generator for tiny results**: Returning a generator when the result is small and re-usable
2. **Hidden lazy I/O**: Side effects inside generators without caller awareness
3. **Over-engineered custom iterator**: Custom `__iter__` / `__next__` for what a generator function would handle
4. **Exhaustion surprise**: Generator consumed without documenting single-pass behavior
5. **Unnecessary nesting**: Generator expression inside a generator function when flattening with `yield from` would be clearer
