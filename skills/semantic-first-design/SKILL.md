---
name: semantic-first-design
description: Guide Python design and review toward explicit contracts, states, policies, boundaries, composition, and failure semantics when material ambiguity prevents local reasoning.
complexity: medium
risk_profile:
  - ambiguity_sensitive
inputs:
  - the Python design or review question and the code or contract under discussion
  - the meanings callers must be able to distinguish
  - existing repository contracts and the relevant specialised Python skill, when known
outputs:
  - a prioritized semantic-ambiguity assessment
  - the smallest explicit distinction that removes the material ambiguity
  - a bounded handoff to a specialised Python skill when its contract owns the decision
use_when:
  - a Python design or review question has a material contract, state, policy, boundary, composition, abstraction, or failure ambiguity
  - a caller cannot determine an important behavior from local names, types, signatures, or visible composition
do_not_use_when:
  - the question is already owned by a specialised Python skill without cross-cutting semantic ambiguity
  - the proposed change only adds patterns, wrappers, interfaces, or enums for stylistic uniformity
---

# Purpose

Identify material semantic ambiguity in Python design or review work, then
recommend the smallest explicit distinction that lets a caller reason about the
important behavior locally. This is a cross-cutting guardrail, not a replacement
for specialised Python design skills.

# Trigger / When to use

Use this skill when:

- a Python API, type, workflow, or component can reasonably be interpreted in
  more than one material way;
- a result, state transition, flag, dependency, or failure is hidden behind a
  generic value, fallback, convention, or implementation detail; or
- a review needs to decide whether a proposed abstraction removes ambiguity or
  merely adds structure.

Do not use this skill when:

- the question is solely about public signature shape, naming, model choice,
  strict typing, error policy, or library architecture; route directly to its
  specialised skill instead;
- the uncertainty is cosmetic and cannot affect behavior, safety, or a
  caller's reasonable interpretation; or
- the suggested solution is a blanket rule such as wrapping every primitive or
  adding an interface for every function.

# Inputs

- The concrete Python design or review target, including the locally visible
  name, signature, type, control flow, and composition where available.
- The distinct meanings that a caller, maintainer, or boundary consumer must
  tell apart.
- Existing repository contracts and constraints; do not reopen locked contract,
  architecture, or path decisions.
- The external system or dependency involved, if the ambiguity crosses a
  boundary.

# Process

1. State the observed ambiguity in one sentence: identify the same-looking
   value, path, or behavior that currently carries multiple meanings.
2. Classify it as contract/type/state, absence, boolean/policy, boundary,
   composition, abstraction, or failure semantics. Use the decision prompts in
   `reference.md`; classify only what is material to the question.
3. Identify the minimum distinction that makes the relevant meaning visible in
   a name, type, signature, return path, component boundary, or orchestration
   step. Keep a simple representation when it already has one unambiguous
   meaning.
4. Check local reasoning: a reader with the call site and directly referenced
   contract should be able to tell what happens on success, normal absence, and
   failure without tracing unrelated implementation details.
5. Route the concrete decision to the specialised owner instead of redefining
   its rules: `python-api-signature`, `python-naming`,
   `python-model-selection`, `python-error-handling`,
   `python-type-hints-strict`, or `python-library-architecture`.
6. Return a bounded recommendation: ambiguity, explicit distinction, expected
   caller guarantee, and specialised handoff. Do not prescribe extra patterns
   without a specific ambiguity they remove.

# Examples

- Positive: A lookup returns `None` for both "record does not exist" and
  "backend call failed." Separate normal absence from explicit failure, then
  hand the failure contract to `python-error-handling`.
- Incorrect: Replace every `str` with a wrapper class because semantic-first
  design always requires value objects, even though the values cannot be
  confused and have no distinct guarantees.

# Outputs

- A concise statement of the material ambiguity and why it prevents local
  reasoning.
- The smallest explicit semantic distinction and the guarantee it introduces.
- A direct, bounded routing recommendation when a specialised Python skill owns
  the concrete signature, naming, model, type, error, or architecture choice.
- `INCOMPLETE` or `BLOCKED` status when the available context cannot support a
  safe distinction.

# Validation

## Required Checks

- Confirm the ambiguity changes a caller-visible guarantee, valid state,
  behavior choice, boundary meaning, or failure interpretation.
- Confirm the recommendation gives each normal result and failure path one
  distinguishable meaning.
- Confirm the proposed abstraction, type, policy, or component removes a named
  ambiguity rather than merely standardizing style.
- Confirm no specialised skill's concrete rules are restated, weakened, or
  overridden.

## Quality Checks (best effort)

- Prefer an explicit name, return distinction, or visible composition over a
  new abstraction when that is sufficient.
- Keep orchestration readable: reveal what happens next, but do not invent
  no-op steps for structural symmetry.
- Check the worked patterns in `examples.md` when a similar ambiguity recurs.

## On Soft Fail

- **SOFT FAIL**: Mark the output `INCOMPLETE` when enough context is missing to rank an
  otherwise non-blocking ambiguity.
- State the missing contract or caller expectation, make no invented policy,
  and provide only the safe observations and routes available.

## On Blocked

- **BLOCKED**: Mark the output `BLOCKED` and stop when plausible interpretations would
  select different public contracts, valid states, failure behavior, or
  architecture boundaries.
- State the exact unresolved meaning and the decision owner required before a
  recommendation can be made.

# Failure Handling

## Missing Context

- If success, absence, failure, caller expectation, or boundary ownership is
  unknown, mark the assessment `INCOMPLETE` and list the missing information.

## Ambiguous Requirement

- If alternative interpretations materially change the recommended contract or
  design boundary, mark it `BLOCKED`; do not choose one by inference.
- Otherwise state the conservative assumption and why it does not change the
  recommendation.

## Execution Limitation

- State when code, call sites, or an external contract cannot be inspected.
- Do not manufacture a type, policy, error, or abstraction to conceal the
  limitation.

# Red Flags

- `None`, `False`, an empty collection, or an unchanged value can each mean
  success, absence, invalid input, and failure.
- A boolean names an implementation switch rather than a natural binary domain
  fact, or a credible third behavior already exists.
- A public type promises a guarantee that the implementation has not established.
- A third-party identifier, flag, exception, or weak result leaks unchanged
  into the application contract.
- Important dependencies are selected by registry, discovery, or hidden
  defaults such that visible composition cannot explain the behavior.

# Boundaries

- Do not mandate value objects, `Enum`, `dataclass`, `ABC`, `Protocol`,
  factories, builders, registries, or dependency containers as universal
  solutions.
- Do not design public signature mechanics; route them to
  `python-api-signature`.
- Do not set identifier names or visibility conventions; route them to
  `python-naming`.
- Do not choose concrete Python model constructs; route them to
  `python-model-selection`.
- Do not define exception hierarchy, translation, retry, or logging policy;
  route failure-policy work to `python-error-handling`.
- Do not define strict annotation syntax or typing escape hatches; route them
  to `python-type-hints-strict`.
- Do not define reusable-library package architecture; route that work to
  `python-library-architecture`.
- Do not change existing specialised skills, platform projections, or runtime
  code as part of this guardrail.

# Local references

- `reference.md`: semantic decision prompts and the routing boundary for each
  ambiguity category.
- `examples.md`: worked Python patterns and anti-patterns for resolving common
  semantic ambiguity without overengineering.
