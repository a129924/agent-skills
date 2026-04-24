# Signature Integrity

Use this file when the main question is whether a decorator preserves the
wrapped callable contract.

## Mainline rule

- Transparent decorators keep the same caller-visible parameters and return
  type.
- For those decorators, preserve metadata with `functools.wraps`.
- Preserve typing with `ParamSpec` (`P`) and `TypeVar` (`R`) so the wrapper
  stays a `Callable[P, R]`.
- If a decorator changes the return shape or caller-visible contract, do not
  present it as the normal transparent pattern.

## Transparent wrapper pattern

```python
from collections.abc import Callable
from functools import wraps
from typing import ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def log_calls(func: Callable[P, R]) -> Callable[P, R]:
    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        print(f"calling {func.__name__}")
        return func(*args, **kwargs)

    return wrapper
```

Why this is the mainline:
- preserves metadata
- preserves caller-visible parameters
- preserves the return type
- keeps the decorator transparent to static type checking

## Decorator factory pattern

```python
from collections.abc import Callable
from functools import wraps
from typing import ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def require_role(role: str) -> Callable[[Callable[P, R]], Callable[P, R]]:
    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            check_role(role)
            return func(*args, **kwargs)

        return wrapper

    return decorator
```

The factory may take configuration, but the inner decorator still preserves the
wrapped callable contract.

## Method decorators

- Method decorators follow the same transparency rule as ordinary function
  decorators.
- Do not drop to `Callable[..., Any]` just because the wrapped callable is later
  bound as a method.
- If the method decorator needs instance state, keep the receiver typed in the
  decorator contract instead of recovering it from `args[0]`.
- Use a receiver type variable plus `Concatenate` when the wrapper must inspect
  `self` or another leading bound object.

```python
from collections.abc import Callable
from functools import wraps
from typing import Concatenate, ParamSpec, Protocol, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


class ActiveSession(Protocol):
    def is_active(self) -> bool:
        ...


class HasSession(Protocol):
    session: ActiveSession


S = TypeVar("S", bound=HasSession)


def require_session(
    func: Callable[Concatenate[S, P], R],
) -> Callable[Concatenate[S, P], R]:
    @wraps(func)
    def wrapper(self: S, *args: P.args, **kwargs: P.kwargs) -> R:
        return func(self, *args, **kwargs)

    return wrapper
```

## Anti-patterns

### Anti-pattern: lossy typing

```python
from collections.abc import Callable
from typing import Any


def audit(func: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print("audited")
        return func(*args, **kwargs)

    return wrapper
```

Why this is wrong for transparent decorators:
- erases caller-visible parameters
- erases return typing
- makes the wrapper harder to reason about during review

### Anti-pattern: silent contract change

If a decorator turns `Callable[P, R]` into "same parameters, but now the return
value is a tuple / response object / sentinel-wrapped value", it is no longer a
transparent wrapper. Treat that as a boundary case and prefer a more explicit
surface.
