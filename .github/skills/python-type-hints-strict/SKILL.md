---
name: python-type-hints-strict
description: Define or enforce Python type-hint rules for projects that run pyright in strict mode. Use this when drafting typing guidance or reviewing code against a strict typing baseline.
---

# Purpose
Define one strict typing contract for Python code that must pass `pyright --strict`.

# Trigger / When to use
Use this skill when:
- a project mandates `pyright --strict`
- code review must decide whether a typing pattern is acceptable
- a coding standard needs a strict type-hint section

Do not use this skill when:
- the task is only about naming conventions
- the task mainly chooses runtime models or control-flow style

# Inputs
- the Python version and typing baseline
- any allowed escape hatches
- repository policy or examples that already constrain typing

# Process
1. Start from `pyright --strict` as the default baseline.
2. Require explicit parameter and return annotations on public functions and methods.
3. Prefer PEP 604 unions and built-in generics over legacy `typing` spellings.
4. Limit `Any`, `cast`, and ignore comments to explicit, justified edge cases.
5. Put reusable details and exceptions in `reference.md`.

# Examples
- Positive: Require `User | None`, `list[str]`, and a named `TypeAlias` for complex repeated types.
- Negative: Allow implicit `Any`, untyped public APIs, or routine ignore comments with no justification.

# Outputs
- a review-ready strict typing rule set or skill draft
- explicit allowed and disallowed typing patterns
- a local reference file for edge cases and escape hatches

# Boundaries
- Do not choose between `Enum`, `dataclass`, `ABC`, or `Protocol`.
- Do not define naming policy or branch-selection rules.
- Do not relax strict typing without an explicit repository-level exception.

# Local references
- `reference.md`: strict typing defaults, allowed exceptions, and short examples
