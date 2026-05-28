# Python Generators and Iterators Examples

This file covers concrete examples, anti-patterns, and split signals for choosing and using generators and iterators in Python.

## Scenario A: Concrete collection versus lazy generator

**Situation**: A function returns user data.

**Good**: Concrete list for small, bounded data
```python
def get_active_users():
    """Return a list of active users. The result is small and may be iterated multiple times."""
    return [u for u in users if u.is_active]
```

**Good**: Generator for large or expensive computation
```python
def get_large_dataset():
    """Yield rows from a large dataset without loading all rows into memory."""
    for row in database.scan_table("users"):
        yield row
```

**Anti-pattern**: Generator for small data that caller will iterate multiple times
```python
def get_active_users():
    return (u for u in users if u.is_active)  # Bad: exhausts after first iteration

# Caller gets surprised
users_gen = get_active_users()
first_pass = list(users_gen)  # OK
second_pass = list(users_gen)  # Empty! Generator is exhausted
```

## Scenario B: Generator function versus generator expression

**Good**: Simple generator expression
```python
def transform_data(items):
    """Return doubled values lazily."""
    return (x * 2 for x in items)
```

**Good**: Generator function for complex logic
```python
def transform_data(items):
    """Yield doubled values, skipping invalid items."""
    for x in items:
        if isinstance(x, (int, float)) and x > 0:
            yield x * 2
```

**Anti-pattern**: Complex logic hidden in generator expression
```python
def transform_data(items):
    return (x * 2 for x in items if isinstance(x, (int, float)) and x > 0 and x != some_sentinel)
    # Reads poorly; logic should be in a function
```

## Scenario C: `yield` and `yield from`

**Good**: Using `yield from` to flatten nested lists
```python
def flatten(nested):
    """Flatten a nested list structure."""
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item

# Usage
result = list(flatten([1, [2, [3, 4]], 5]))  # [1, 2, 3, 4, 5]
```

**Anti-pattern**: Manual loop when `yield from` would be clearer
```python
def flatten(nested):
    for item in nested:
        if isinstance(item, list):
            for subitem in flatten(item):
                yield subitem
        else:
            yield item
```

## Scenario D: Generator function state tracking

**Good**: Generator function managing state
```python
def fibonacci(limit):
    """Yield Fibonacci numbers up to limit."""
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b
```

**Anti-pattern**: Custom iterator class for simple state
```python
class Fibonacci:
    def __init__(self, limit):
        self.limit = limit
        self.a, self.b = 0, 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.a >= self.limit:
            raise StopIteration
        value = self.a
        self.a, self.b = self.b, self.a + self.b
        return value

# The generator function is simpler
```

## Scenario E: Custom iterator with reset capability

**Good**: Custom iterator when reset is needed
```python
class RepeatingIterator:
    """Iterator that can be reused multiple times."""
    def __init__(self, items):
        self.items = items
        self.index = 0
    
    def __iter__(self):
        self.index = 0  # Reset on each iteration
        return self
    
    def __next__(self):
        if self.index >= len(self.items):
            raise StopIteration
        value = self.items[self.index]
        self.index += 1
        return value

# Usage
iter_obj = RepeatingIterator([1, 2, 3])
print(list(iter_obj))  # [1, 2, 3]
print(list(iter_obj))  # [1, 2, 3] - Works because __iter__ resets
```

**Good**: Concrete list when multi-pass is needed
```python
def get_items():
    """Return items as a concrete list for multi-pass iteration."""
    return [1, 2, 3]

# Usage
items = get_items()
first_pass = [x * 2 for x in items]   # Works
second_pass = [x + 1 for x in items]  # Works - items not exhausted
```

## Scenario F: Hidden lazy I/O anti-pattern

**Anti-pattern**: Side effects buried in a generator
```python
def load_users():
    """Load users from database lazily. BAD: Side effects are hidden."""
    for user_id in user_ids:
        yield database.query(f"SELECT * FROM users WHERE id = {user_id}")

# Caller gets surprised by slow iteration
for user in load_users():  # Each iteration hits the database
    print(user)
```

**Good**: Explicit eagerness with side effects documented
```python
def load_users():
    """Load and return all users from database.
    
    Note: This function executes database queries eagerly.
    """
    return [database.query(f"SELECT * FROM users WHERE id = {user_id}") for user_id in user_ids]
```

**Good**: Lazy generator with side effects documented clearly
```python
def load_users():
    """Yield users from database lazily.
    
    Warning: Each iteration executes a database query.
    Use list(load_users()) to materialize all results at once.
    """
    for user_id in user_ids:
        yield database.query(f"SELECT * FROM users WHERE id = {user_id}")
```

## Scenario G: Generator exhaustion

**Anti-pattern**: Exhausted generator without awareness
```python
gen = (x for x in range(5))
first = list(gen)   # [0, 1, 2, 3, 4]
second = list(gen)  # [] - Generator exhausted!
```

**Good**: Fresh generator each iteration
```python
def generate():
    return (x for x in range(5))

first = list(generate())   # [0, 1, 2, 3, 4]
second = list(generate())  # [0, 1, 2, 3, 4] - Fresh generator each call
```

**Good**: Convert to list if multi-pass is needed
```python
gen = (x for x in range(5))
data = list(gen)  # Materialize once
first = [y * 2 for y in data]   # Use data multiple times
second = [y + 1 for y in data]  # Works - data is a list
```

## Scenario H: Choosing concrete versus custom iterator

**Good**: Concrete list for simple re-usable data
```python
class DataRange:
    def __init__(self, start, end):
        self.data = list(range(start, end))

obj = DataRange(1, 5)
first = list(obj.data)   # [1, 2, 3, 4]
second = list(obj.data)  # [1, 2, 3, 4] - Works, data is reusable
```

**Good**: Custom iterable (with `__iter__` returning a new iterator) for complex state
```python
class DataRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def __iter__(self):
        return iter(range(self.start, self.end))

obj = DataRange(1, 5)
first = list(obj)   # [1, 2, 3, 4]
second = list(obj)  # [1, 2, 3, 4] - Works, __iter__ returns fresh iterator
```

## Scenario I: Generator expression simplicity limits

**Good**: Generator expression for simple transformation
```python
squares = (x**2 for x in range(10) if x % 2 == 0)
```

**Better**: Named generator function for clarity if logic grows
```python
def even_squares(limit):
    """Yield squares of even numbers up to limit."""
    for x in range(limit):
        if x % 2 == 0:
            yield x ** 2

squares = even_squares(10)
```

## Anti-patterns summary

| Anti-pattern | Problem | Fix |
| --- | --- | --- |
| Generator for small, reusable data | Exhaustion surprise | Return a concrete list |
| Hidden lazy I/O | Caller unaware of side effects | Make it eager or document clearly |
| Over-engineered custom iterator | Complexity without need | Use a generator function |
| Generator exhaustion | Silent bugs from reuse | Materialize to list or create fresh generators |
| Complex logic in generator expression | Hard to read and debug | Use a generator function |
