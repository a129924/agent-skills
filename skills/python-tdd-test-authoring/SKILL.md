---
name: python-tdd-test-authoring
description: Design RED tests from Python requirements or plan context before implementation starts, using test-first mapping, D1 trivial-versus-non-trivial reasoning, and explicit fit boundaries without workflow-gated verdict artifacts.
complexity: high
risk_profile:
  - ambiguity_sensitive
inputs:
  - the requirements, plan, or behavior description being tested
  - any existing test structure, naming conventions, and helper utilities
  - the expected public contract, error cases, boundary cases, state effects, and integration points
  - evidence about whether production code has already changed
outputs:
  - a test-first design with requirement-to-test mapping
  - RED-test recommendations or skeletons for determinable cases
  - explicit fit / not-fit guidance when the request arrives too late or lacks behavior clarity
use_when:
  - implementation has not started or production code is still untouched
  - the task is to design tests first from requirements, plan context, or behavior description
  - the work needs explicit mapping from behavior to test cases before coding
do_not_use_when:
  - production code has already been modified and the task is no longer test-first
  - the behavior or requirements are too vague to produce testable assertions honestly
  - the task is to emit workflow-specific verdict files or gate another workflow step
---

# Purpose
Design RED tests before implementation by mapping behavior to test cases, forcing clear assertions, and keeping test-first boundaries explicit.

# Trigger / When to use
Use this skill when:
- implementation has not started or production code is still untouched
- the task is to design tests first from requirements, plan context, or behavior description
- the work needs explicit mapping from behavior to test cases before coding

Do not use this skill when:
- production code has already been modified and the task is no longer test-first
- the behavior or requirements are too vague to produce testable assertions honestly
- the task is to emit workflow-specific verdict files or gate another workflow step

# Inputs
- the requirements, plan, or behavior description being tested
- any existing test structure, naming conventions, and helper utilities
- expected public contract, error cases, boundary cases, state effects, and integration points
- evidence about whether production code has already changed

# Process
1. Confirm the request is still test-first. If production code has already moved, stop and say the fit boundary is violated.
2. Run a D1 reasoning pass:
   - `trivial`: the change is too small to justify a full test-authoring workflow
   - `non-trivial`: explicit test mapping is warranted
3. For non-trivial work, map each requirement or behavior claim to one or more tests.
4. Cover at least these categories when they are relevant: happy path, error handling, boundary or edge behavior, state or side effects, and integration points.
5. Prefer RED-test recommendations or skeletons that another engineer can implement without inventing the assertion intent.
6. If a requirement is too vague, name the ambiguity and leave the affected mapping unresolved rather than fabricating test logic.

# Outputs
- requirement-to-test mapping
- RED-test recommendations or skeletons for determinable cases
- explicit notes about ambiguous requirements, skipped areas, and fit-boundary violations

# Validation
Before proceeding, confirm:
- the work is still test-first
- each determinable requirement maps to at least one test
- assertions are explicit rather than implied
- the mapping covers the relevant error, boundary, state, and integration behavior

# Boundaries
- Do not modify production code.
- Do not require YAML verdict files, fixed next-step routing, or workflow-gated artifacts.
- Do not pretend vague requirements are test-ready.
- Do not treat a trivial D1 outcome as a failure; it is a valid narrow-fit result.

# Local references
- `examples.md`: test-first mapping examples for trivial and non-trivial D1 outcomes, red-test coverage, and late-arrival reroutes
