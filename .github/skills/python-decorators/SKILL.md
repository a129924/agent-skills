---
name: python-decorators
description: Choose and design ordinary Python decorators that preserve signature transparency, keep behavior explicit, and avoid hiding lifetime-driven work.
---

# Purpose
Choose when a decorator is the right tool and design ordinary Python decorators
so transparent wrappers stay explicit, readable, and type-safe.

# Trigger / When to use
Use this skill when:
- deciding whether repeated call-time behavior belongs in a decorator instead of
  an explicit helper call
- writing or reviewing function decorators, method decorators, or decorator
  factories
- preserving wrapped-callable metadata and caller-visible typing
- deciding whether retries, caching, auth checks, logging, or error translation
  are explicit enough to live in a decorator
- adding a custom decorator in framework code and wanting to keep it aligned
  with ordinary Python rules

Do not use this skill when:
- the main task is general strict-typing policy or checker configuration
- the behavior is really resource lifetime, setup/cleanup, or ambient-state
  restoration; use `python-context-management`
- the task is mainly about class decorators, descriptors, metaclasses, or
  framework-private decorator internals
- the decorator intentionally changes the caller-visible contract and that
  contract change is the main design goal

# Inputs
- the callable being wrapped and whether it is public or internal
- whether the added behavior is call-driven or lifetime-driven
- whether the decorator is meant to stay transparent to callers
- whether the decorator has side effects such as retries, caching, auth, or
  error translation
- whether a decorator factory is needed
- whether the code sits in a framework that depends on inspectable signatures or
  naming

# Process
1. **Choose the right tool** — Use a decorator for repeated call-time behavior
   that should wrap many call sites the same way. If the behavior is one-off,
   workflow-shaped, or clearer as an explicit function call, do not force a
   decorator.
2. **Keep lifetime explicit** — If the behavior acquires resources, restores
   state, manages transactions, or depends on setup/cleanup symmetry, hand it to
   `python-context-management` or an explicit helper instead of hiding it behind
   decoration.
3. **Default to transparent wrappers** — The first-draft mainline is a
   transparent decorator: same callable contract, same caller-visible typing,
   same return shape. Treat contract-changing decorators as boundary or
   anti-pattern material unless the design has a stronger explicit surface.
4. **Preserve signature integrity** — Use `functools.wraps`. For transparent
   wrappers, thread `ParamSpec` and `TypeVar` through `Callable[P, R]`. Do not
   erase the signature with `Callable[..., Any]` when the decorator claims to be
   transparent.
5. **Make behavior visible** — Name the decorator for the behavior it adds and
   document non-obvious effects such as retries, caching, auth checks, timing,
   or error translation. If the behavior would surprise a caller or reviewer,
   prefer an explicit function or API surface.
6. **Handle factories and methods carefully** — A decorator factory may take its
   own configuration, but the inner decorator should still preserve the wrapped
   callable contract when it is meant to be transparent. Method decorators
   follow the same rule; do not special-case them by dropping type information.
7. **Use framework notes as supplements only** — In FastAPI, pytest, Click, and
   similar ecosystems, custom decorators should still preserve explicit meaning,
   inspectable signatures, and visible boundaries. Framework notes do not
   override the core Python rules.

# Examples
- Positive: Wrap a function with `functools.wraps` plus `ParamSpec` / `TypeVar`
  so logging or retry behavior stays transparent to callers.
- Positive: Use a decorator factory for a repeated auth check when the wrapped
  callable keeps the same parameters and return type.
- Negative: Hide a database transaction or open/close lifecycle inside a
  `Callable[..., Any]` wrapper and still present it as a normal transparent
  decorator.

# Outputs
- a decision on whether a decorator is clearer than an explicit helper call or
  context manager
- a transparent decorator pattern for functions, methods, or decorator factories
- boundary guidance for hidden side effects, lifetime-driven work, and
  contract-changing wrappers
- light framework notes for developer-authored decorators when relevant

# Verification
- `functools.wraps` is used when metadata should be preserved
- transparent wrappers keep caller-visible typing with `ParamSpec` / `TypeVar`
  instead of `Callable[..., Any]`
- the decorator does not hide resource lifetime or setup/cleanup behavior
- non-obvious side effects and error semantics are named and documented
- framework notes, if any, stay custom-decorator-only and do not become
  framework policy

# Red Flags
- `Callable[..., Any]` in a wrapper that claims to preserve the original
  callable contract
- a decorator that opens connections, starts transactions, changes cwd, or
  restores ambient state
- a decorator that changes return shape or swallowed exceptions while still
  being described as transparent
- a framework note that starts depending on private framework internals
- a class-decorator, descriptor, or metaclass discussion drifting into the main
  decision path

# Common Rationalizations
- "It's internal, so erasing the signature with `Any` is fine."
- "A decorator is cleaner than an explicit `with` even if it hides setup and
  cleanup."
- "The framework already does magic, so one more hidden layer is harmless."
- "Using `functools.wraps` alone is enough even if the static type checker loses
  the callable contract."
- "Changing the return object is acceptable as long as the decorator name sounds
  nice."

# Boundaries
- Do not define general strict-typing policy, checker configuration, or typing
  escape hatches; use `python-type-hints-strict`.
- Do not define public API parameter ordering, keyword-only policy, or broad
  signature refactors; use `python-api-signature`.
- Do not define ordinary method/property/factory placement; use
  `python-class-design`.
- Do not define package/module layout or import-surface policy; use
  `python-module-boundaries`.
- Do not normalize hidden setup/cleanup or resource-lifetime decorators; use
  `python-context-management`.
- Do not make class decorators, descriptors, metaclasses, or framework-private
  decorator internals first-draft in-scope.

# Local references
- `reference.md`: overview for the local reference layer and navigation to split
  topics
- `references/signature-integrity.md`: transparent-wrapper typing, `wraps`,
  `ParamSpec`, `TypeVar`, and signature-preservation anti-patterns
- `references/behavior-visibility.md`: explicitness rules for side effects,
  caching, retries, auth, error translation, and lifetime boundaries
- `references/framework-notes.md`: light framework notes for developer-authored
  decorators in common ecosystems
- `examples.md`: detailed positive and negative examples for transparent
  wrappers, decorator factories, framework notes, and anti-patterns
