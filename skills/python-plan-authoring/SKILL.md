---
name: python-plan-authoring
description: Turn Python implementation intent into a bounded execution plan that freezes scope, decisions, affected areas, tests, and validation before coding begins, without requiring repo-specific workflow artifacts.
complexity: high
risk_profile:
  - ambiguity_sensitive
inputs:
  - feature, refactor, or bug-fix intent with scope
  - relevant current codebase context such as modules, packages, and public APIs
  - measurable requirements for the change
  - explicit decision inputs for module placement, API shape, breaking changes, dependencies, error handling, and typing
  - at least 3 non-goals
  - test strategy signals and validation commands
  - async-capable evidence when the topic changes async boundary, lifecycle, concurrency, failure, or cancellation behavior
  - open questions the author cannot resolve alone
outputs:
  - a bounded implementation plan with scope, decisions, affected areas, test plan, validation, and open questions
  - explicit non-goals and unresolved assumptions
  - stop-and-ask questions when required information is missing
use_when:
  - a Python feature, refactor, or bug fix needs a frozen contract before coding starts
  - multiple files, interfaces, or decisions will be affected
  - a reviewer or future implementer must be able to follow the plan without guessing
do_not_use_when:
  - the change is trivial and isolated
  - the task is to execute or review an existing plan
  - no Python code is involved
  - the request is for a generic project-management or release plan unrelated to Python implementation
---

# Purpose
Turn Python implementation intent into a reviewable plan that freezes scope, decisions, affected areas, tests, and validation before coding starts. The plan is an execution contract, not a todo list.

# Trigger / When to use
Use this skill when:
- a Python feature, refactor, or bug fix needs a frozen contract before coding starts
- the task touches more than one file or module and scope clarity is needed before coding
- multiple interfaces will be modified and the dependency order must be declared
- a reviewer or future implementer must be able to verify work against a written plan

Do not use this skill when:
- the change is trivial and isolated
- the task is to execute or review an existing plan
- no Python code is involved
- the request is for a generic project-management or release plan unrelated to Python implementation

# Inputs
- the feature, change, or bug fix being planned
- relevant current codebase context such as modules, packages, and public APIs
- measurable requirements for the change
- explicit decision inputs for module placement, API shape, breaking changes, dependencies, error handling, and typing
- at least 3 non-goals
- test strategy signals and validation commands
- async-capable evidence when the topic changes async behavior materially
- open questions the author cannot resolve alone

# Process
1. Confirm the task is implementation planning, not execution, code review, or release workflow.
2. Freeze the goal, scope, and non-goals first. If missing facts would change scope materially, stop and ask instead of drafting around guesswork.
3. Record the core decisions explicitly: module placement, public API shape, dependency order, breaking-change stance, error-handling stance, and typing stance.
4. Map the change into bounded affected areas rather than mandatory repo-visible artifact names. Name the files, modules, or packages likely to change only when they can be grounded honestly.
5. Add Thin SDD and Thin TDD fields:
   - design intent: what behavior or contract changes
   - test intent: what must be verified before considering the work done
6. When async risk is present, add an explicit async-planning status line with the trigger evidence or exemption reasoning.
7. End with validation commands, open questions, assumptions, and clear stop-and-ask blockers.

# Recommended Output Shape
- Goal / outcome
- Scope
- Non-goals
- Locked decisions
- Affected areas
- Thin SDD fields
- Thin TDD fields
- Validation
- Open questions / assumptions

# Validation
Before proceeding, confirm:
- the plan is specific enough that an implementer can act without guessing
- non-goals are explicit and actually exclude neighboring work
- decisions cover module placement, API shape, dependencies, error handling, and typing
- tests and validation commands are concrete enough to verify completion
- async status is explicit when async risk exists

# Boundaries
- Do not require `.plan.md`, `.step.md`, or `.spec.md` as part of this skill's core contract.
- Do not turn the plan into a reviewer-verdict protocol or executor workflow gate.
- Do not promise file-level certainty when the current codebase evidence does not support it.
- Do not start coding, scaffolding, or reviewing implementation quality.

