# Behavior Visibility

Use this file when the main question is whether a decorator hides too much
behavior or belongs behind a clearer surface.

## When a decorator is a good fit

Decorators fit best when the added behavior is:
- repeated across many call sites
- call-driven rather than lifetime-driven
- small enough that the wrapped function still reads as the main behavior
- explicit from the decorator name and contract

Typical fit:
- logging or tracing
- narrow auth checks
- bounded retry behavior
- memoization or caching when the cache semantics are visible

## What must stay explicit

If a decorator adds non-obvious behavior, make it visible in the name,
docstring, and examples. This is especially important for:
- retries
- caching
- auth / permission checks
- timing / instrumentation
- exception translation or suppression
- rate limiting

Bad smell:
- "The decorator is only a convenience" used to justify hidden side effects.

## Lifetime boundary

Do not hide resource lifetime behind decoration when the behavior really depends
on setup/cleanup symmetry or ambient-state restoration.

Prefer an explicit function call or context manager when the behavior:
- opens and closes connections
- starts and ends transactions
- temporarily swaps cwd, env vars, locale, or other ambient state
- must guarantee cleanup on both success and error paths

That work belongs with `python-context-management`, not as normal decorator
guidance.

## Explicitness over magic

Prefer an explicit helper or context manager when:
- only one call site needs the behavior
- the behavior materially changes reviewability
- the behavior changes return shape or error semantics in a surprising way
- a reader would need to inspect the decorator implementation to understand the
  function contract

## Anti-patterns

### Hidden transaction scope

If `@with_transaction` opens, commits, rolls back, and closes a transaction
around a business function, the lifetime semantics are hidden. That is not a
good mainline decorator example for this skill.

### Hidden caching semantics

If `@cached` changes freshness, eviction, or error behavior, the decorator must
make those semantics explicit. If it cannot, prefer a named helper or explicit
cache API.
