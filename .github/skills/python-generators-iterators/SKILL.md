---
name: python-generators-iterators
description: Choose clear Python iteration patterns. Use this when deciding whether code should return a concrete collection versus a generator, or when designing generator functions, generator expressions, and custom iterator classes.
complexity: medium
risk_profile: [ambiguity_sensitive]
inputs:
  - the collection being iterated or the work being performed
  - whether the collection is large, infinite, or expensive to compute
  - whether the caller needs to iterate once or multiple times
  - whether the iteration has side effects or dependencies on internal state
  - whether readability benefits from lazy evaluation or eager collection
outputs:
  - a decision on whether a function should return a concrete collection or a generator
  - clear choice between generator function, generator expression, and custom iterator class
  - explicit documentation of exhaustion and side-effect expectations
  - a code review guide for iteration patterns
use_when:
  - deciding whether a function should return a concrete list or a generator
  - choosing between a generator function, a generator expression, and a custom iterator class
  - reviewing yield and yield from patterns for readability and correctness
  - designing iteration behavior for single-pass versus multi-pass expectations
  - deciding when to implement __iter__ and __next__ protocol
  - reviewing iterator exhaustion and side effects on repeated iteration
do_not_use_when:
  - the main task is async iteration, async generators, or async for; use python-async-await
  - the main task is control-flow branching; use python-control-flow
  - the main task is choosing between Enum, dataclass, ABC, or Protocol; use python-model-selection
  - the main task is package/module boundary design; use python-module-boundaries
  - the main task is deep test design for lazy evaluation; use python-testing-pytest
---

# Purpose

Choose when Python code should return a concrete collection versus a generator,
design generator functions and expressions clearly, and decide when a custom
iterator class is warranted instead of a generator function.

# Trigger / When to use

Use this skill when:
- deciding whether a function should return a concrete list or a generator
- choosing between a generator function, a generator expression, and a custom
  iterator class
- reviewing `yield` and `yield from` patterns for readability and correctness
- designing iteration behavior for single-pass versus multi-pass expectations
- deciding when to implement `__iter__` and `__next__` protocol
- reviewing iterator exhaustion and side effects on repeated iteration

Do not use this skill when:
- the main task is async iteration, async generators, or `async for`; use
  `python-async-await`
- the main task is control-flow branching; use `python-control-flow`
- the main task is choosing between `Enum`, `dataclass`, `ABC`, or `Protocol`;
  use `python-model-selection`
- the main task is package/module boundary design; use
  `python-module-boundaries`
- the main task is deep test design for lazy evaluation; use
  `python-testing-pytest`

# Inputs

- the collection being iterated or the work being performed
- whether the collection is large, infinite, or expensive to compute
- whether the caller needs to iterate once or multiple times
- whether the iteration has side effects or dependencies on internal state
- whether readability benefits from lazy evaluation or eager collection

# Process

1. **Decide concrete versus generator honestly** — Return a concrete collection
   unless the caller will iterate once, the collection is large, or computing
   the full result is expensive or infinite. Do not make code lazy just to look
   modern.
2. **Choose generator function versus expression** — Use a generator function
   when logic is complex, state is involved, or readability needs helper steps.
   Use a generator expression only for simple transformations where a
   comprehension would fit.
3. **Use `yield` and `yield from` clearly** — Use `yield` for simple production;
   use `yield from` to delegate to a sub-generator instead of writing a loop.
   Keep both patterns obvious in code review.
4. **Think about exhaustion and reuse** — A generator can only iterate once.
   Document or enforce single-pass expectations explicitly. If code needs
   multi-pass iteration, return a concrete collection or use a custom iterator
   that resets.
5. **Implement custom iterators sparingly** — Use a generator function unless
   you need `__iter__` and `__next__` protocol for state management, reset
   capability, or compatibility with code that inspects `__class__`. Do not
   implement the protocol just to avoid a function.
6. **Keep iteration side-effect-free or explicit** — Iterator side effects on
   internal state, external I/O, or network requests must be obvious at the
   call site. Lazy I/O surprises break trust.

# Examples

- Positive: Return a generator when computing a large result set. Use a
  generator expression for a simple transformation. Implement `__iter__` and
  `__next__` when iteration must reset or track complex state.
- Positive: Use `yield from` to flatten nested iterables cleanly instead of
  writing nested loops.
- Negative: Return a generator to avoid up-front work when the caller expects a
  small, bounded result. Implement `__iter__` and `__next__` for a simple
  producer; use a generator function instead.
- Negative: Hide I/O, database queries, or side effects inside a generator
  without documenting the lazy behavior. Consume the generator eagerly, then
  document the laziness or make it eager and explicit.

# Outputs

- a decision on whether a function should return a concrete collection or a
  generator
- clear choice between generator function, generator expression, and custom
  iterator class
- explicit documentation of exhaustion and side-effect expectations
- a code review guide for iteration patterns

# Validation

Before proceeding, confirm:
- **Caller iteration contract known**: does the caller iterate once, multiple times, or partially?
- **Side effects documented**: are any side effects in the iterator (I/O, database queries) visible or documented?
- **Collection size and cost understood**: is the dataset large, infinite, or expensive to compute, or small and bounded?

**SOFT FAIL** — ask and wait before continuing:
- Caller's iteration ownership is unclear (once vs multiple passes) → cannot safely recommend generator vs concrete collection; ask before proceeding
- Side effects exist but are undocumented → ask how to surface them before recommending a `yield`-based design
- Collection size is unknown → ask whether lazy evaluation or eager collection is appropriate for this context

**BLOCKED** — stop and redirect:
- The main task involves async iteration, `async for`, or async generators → redirect to `python-async-await`
- The main task is control-flow branching logic → redirect to `python-control-flow`

# Failure Handling

## Missing Context
- If caller iteration contract, side-effect documentation, or collection characteristics cannot be determined, mark output as INCOMPLETE and list the missing information.

## Ambiguous Requirement
- If blocking: stop and ask whether the caller needs single-pass or multi-pass iteration before recommending a generator.
- If non-blocking: proceed with the conservative default (concrete collection) and document the assumption.

## Execution Limitation
- State the limitation explicitly.
- Do not invent an iteration pattern that cannot be justified from available context.

# Red Flags

- generator returned for a small, bounded result where eager evaluation was
  simpler
- `yield` used to avoid a straightforward list comprehension
- generator hidden inside a function without documenting the lazy behavior to
  the caller
- custom iterator class implemented where a simple generator function or
  expression would work
- `yield` not paired with cleanup code; implicit generator cleanup surprises
- iterator side effects (I/O, database queries) not visible or documented

# Common Rationalizations

- "Making this lazy now will save time later if the data gets large."
- "Generator is more Pythonic than returning a list."
- "A generator expression is easier to read than itertools."
- "I implemented `__iter__` and `__next__` to be more explicit."
- "The caller probably only wants a few items, so lazy is better."

# Boundaries

- Do not define async iteration semantics; use `python-async-await`.
- Do not define general branching or control-flow rules; use
  `python-control-flow`.
- Do not define model-selection or construct-choice rules beyond iterator
  protocol; use `python-model-selection`.
- Do not define package boundaries or import policy; use
  `python-module-boundaries`.
- Do not define deep test design or lazy-evaluation test fixtures; use
  `python-testing-pytest`.

# Local references

- `reference.md`: sync-only iteration semantics, generator design baseline, and
  iterator protocol rules
- `examples.md`: concrete examples, anti-patterns, and split signals for
  generator function vs expression vs custom iterator choice
