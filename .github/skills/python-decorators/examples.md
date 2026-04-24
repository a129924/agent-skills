# Examples: Python Decorators

This file provides detailed positive and negative examples for choosing and
designing ordinary Python decorators. The examples assume the first-draft
mainline: transparent decorators are normal; contract-changing or
lifetime-hiding decorators are boundary or anti-pattern material.

## Positive Scenarios

### Scenario A: Transparent Function Decorator

```python
from collections.abc import Callable
from functools import wraps
from time import perf_counter
from typing import ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def trace_runtime(func: Callable[P, R]) -> Callable[P, R]:
    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        started = perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            duration = perf_counter() - started
            print(f"{func.__name__} took {duration:.3f}s")

    return wrapper
```

Why this is correct:
- preserves metadata with `wraps`
- preserves caller-visible typing with `ParamSpec` / `TypeVar`
- adds call-time tracing without changing parameters or return shape
- does not hide resource lifetime

---

### Scenario B: Transparent Method Decorator

```python
from collections.abc import Callable
from functools import wraps
from typing import ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def require_active_session(func: Callable[P, R]) -> Callable[P, R]:
    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        self = args[0]
        if not self.session.is_active():
            raise RuntimeError("session is not active")
        return func(*args, **kwargs)

    return wrapper


class ExportService:
    @require_active_session
    def export(self, vendor_id: str) -> str:
        return f"exported:{vendor_id}"
```

Why this is correct:
- method decoration still preserves the callable contract
- the decorator adds a narrow call-time guard
- the rule is explicit from the decorator name

---

### Scenario C: Decorator Factory with Transparent Typing

```python
from collections.abc import Callable
from functools import wraps
from typing import ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def retry_on(exception_type: type[Exception], attempts: int) -> Callable[[Callable[P, R]], Callable[P, R]]:
    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            remaining = attempts
            while True:
                try:
                    return func(*args, **kwargs)
                except exception_type:
                    remaining -= 1
                    if remaining <= 0:
                        raise

        return wrapper

    return decorator
```

Why this is correct:
- the outer factory handles configuration
- the inner decorator keeps the original callable contract
- retry semantics are explicit in the decorator name and arguments

---

### Scenario D: Boundary Case Where an Explicit Helper Is Clearer

```python
def send_with_retry(send: Callable[[], str], attempts: int) -> str:
    remaining = attempts
    while True:
        try:
            return send()
        except TimeoutError:
            remaining -= 1
            if remaining <= 0:
                raise


result = send_with_retry(lambda: client.send(payload), attempts=3)
```

Why this is correct:
- only one call site needs the behavior
- the retry policy stays explicit at the call site
- no decorator is needed just to avoid a small helper function

---

### Scenario E: Light Framework Note for a Custom FastAPI Decorator

```python
from collections.abc import Callable
from functools import wraps
from typing import ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def audit_endpoint(event_name: str) -> Callable[[Callable[P, R]], Callable[P, R]]:
    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            audit_log(event_name)
            return func(*args, **kwargs)

        return wrapper

    return decorator
```

Why this is correct:
- the note is about a developer-authored custom decorator, not FastAPI internals
- it preserves inspectable callable metadata
- it adds explicit call-time behavior without hiding dependency/resource lifetime

## Negative Scenarios

### Anti-pattern F: Signature-Erasing Transparent Wrapper

```python
from collections.abc import Callable
from typing import Any


def trace_calls(func: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print("called")
        return func(*args, **kwargs)

    return wrapper
```

Why this is wrong:
- erases caller-visible parameter and return information
- cannot honestly claim to preserve a transparent callable contract
- encourages hidden typing drift

---

### Anti-pattern G: Hidden Lifetime Management in a Decorator

```python
from collections.abc import Callable
from functools import wraps


def with_db_transaction(func: Callable[..., object]) -> Callable[..., object]:
    @wraps(func)
    def wrapper(*args, **kwargs):
        connection = open_connection()
        transaction = connection.begin()
        try:
            result = func(*args, **kwargs)
            transaction.commit()
            return result
        except Exception:
            transaction.rollback()
            raise
        finally:
            connection.close()

    return wrapper
```

Why this is wrong for the mainline:
- hides acquisition and cleanup behind decoration
- mixes call wrapping with resource lifetime management
- belongs closer to explicit helpers or `python-context-management`

---

### Anti-pattern H: Contract-Changing Wrapper Presented as Transparent

```python
from collections.abc import Callable
from functools import wraps
from typing import ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def as_response(func: Callable[P, R]) -> Callable[P, dict[str, object]]:
    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> dict[str, object]:
        return {"ok": True, "data": func(*args, **kwargs)}

    return wrapper
```

Why this is not a mainline pattern:
- changes the caller-visible return contract
- should not be presented as a normal transparent decorator
- needs a more explicit API decision or at least a strong boundary note
