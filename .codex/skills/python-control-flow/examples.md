# Python control-flow examples

Use these examples after `SKILL.md` narrows the question to general Python branching.

## `if/elif` vs `match/case`

### Choose `match/case`
```py
from enum import Enum

class JobStatus(Enum):
    PENDING = "pending"
    RUNNING = "running"
    FAILED = "failed"

def label_for(status: JobStatus) -> str:
    match status:
        case JobStatus.PENDING:
            return "queued"
        case JobStatus.RUNNING:
            return "working"
        case JobStatus.FAILED:
            return "needs attention"
```

- Use it for closed dispatch on one subject.
- Under `pyright --strict`, this can also help narrowing or exhaustiveness when it is already the clearer form.
- Prefer explicit cases on closed subjects instead of routine `case _:`.

### Choose `if/elif`
```py
def retry_delay(status_code: int, retry_after: int | None) -> int:
    if retry_after is not None:
        return retry_after
    if 500 <= status_code < 600:
        return 30
    if status_code == 429:
        return 60
    return 0
```

- Use `if/elif` for range checks, composite predicates, or unrelated conditions.
- If many `case ... if ...` guards would be needed, the guard logic is probably doing the real branching work.

### Avoid stretching `match/case`
```py
def bucket(score: int, is_admin: bool) -> str:
    match score:
        case value if value >= 90 and is_admin:
            return "vip-a"
        case value if value >= 90:
            return "a"
        case value if value >= 70:
            return "b"
        case _:
            return "c"
```

- Here the guards and fallback branch do the real work.
- A plain `if/elif` chain would be clearer than forcing `match/case`.

### Edge notes
- Keep `if` / `else` for tiny closed splits such as `bool` flags or a direct `value is None` split.
- A package-specific skill may override the generic rule if it explicitly defines a custom subject as semantically closed.

## Guard clauses

### Use
```py
def normalize_name(name: str | None) -> str:
    if name is None:
        raise ValueError("name is required")
    if not name.strip():
        raise ValueError("name cannot be blank")
    return name.strip()
```

- Use guard clauses for failed preconditions, invalid input, and short early exits.
- They should flatten the happy path, not add ceremony.

### Edge notes
```py
def normalize_tags(tags: list[str] | None) -> list[str]:
    if tags is None:
        return []
    return [tag.strip() for tag in tags]
```

- Once a guard returns or raises, usually drop the `else`.
- If cleanup, resource lifetime, or enter/exit symmetry matters, do not force multiple early returns just to flatten the function.

## Truthiness vs explicit checks

### Use explicit checks
```py
def choose_timeout(timeout: int | None) -> int:
    if timeout is None:
        return 30
    return timeout
```

- Use explicit checks when `None`, `0`, `""`, `[]`, or `False` would mean different things.

### Use truthiness only when the difference does not matter
```py
def send_digest(emails: list[str]) -> None:
    if not emails:
        return
    for email in emails:
        deliver(email)
```

- Truthiness is fine when you genuinely only care about empty vs non-empty.

### Avoid
```py
def choose_timeout(timeout: int | None) -> int:
    if timeout:
        return timeout
    return 30
```

- This silently treats `0` the same as `None`.
- For custom objects that implement `__bool__` or `__len__`, default to explicit checks unless their semantics are already obvious.

## Split signals

Stop and hand off to another skill when the main question becomes:

- ternary expressions, `:=`, or comprehension branching
- framework-specific helpers or orchestration style
- type-hint syntax instead of control-flow readability

## Out of scope for now

- ternary expressions
- assignment expressions
- branch-heavy comprehensions
- DDD or application-flow conventions
