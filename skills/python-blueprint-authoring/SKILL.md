---
name: python-blueprint-authoring
description: Author a greenfield Python baseline blueprint that freezes structure, tooling, quality signals, and fit boundaries without coupling the output to a locked executor schema.
complexity: high
risk_profile:
  - ambiguity_sensitive
inputs:
  - project or repository name
  - proof that the lane is greenfield or baseline-only
  - project purpose and baseline scope
  - required capabilities, skill dependencies, and toolchain choices
  - concrete structure expectations for packages, entrypoints, and support files
  - measurable quality targets and acceptance signals
outputs:
  - a bounded greenfield baseline blueprint
  - explicit fit / non-fit guidance for greenfield versus retrofit routing
  - stop-and-ask feedback when required structure, tooling, or acceptance signals are missing
use_when:
  - a new or baseline-only Python repository needs its first design baseline before implementation starts
  - the task is to author or repair a greenfield baseline, not to execute it
  - the task needs concrete structure, toolchain, and acceptance expectations without pretending the output is executor-ready
do_not_use_when:
  - the repository already has meaningful structure, migration pressure, or retrofit conflict surfaces
  - the task is to execute a valid blueprint
  - the task is to review or approve an existing blueprint
  - the request lacks tool choices, verifiable acceptance targets, or locatable structural details
---

# Purpose
Turn greenfield Python repository intent into a bounded blueprint that captures structure, tooling, and acceptance expectations without locking the result to a workflow-specific executor contract.

# Trigger / When to use
Use this skill when:
- a new or baseline-only Python repository needs its first design baseline before implementation starts
- the task is to author or repair a greenfield baseline, not to execute it
- the work needs concrete structure, toolchain, and acceptance expectations without pretending the output is already executor-ready

Do not use this skill when:
- the repository already has meaningful structure, migration pressure, or retrofit conflict surfaces
- the task is to execute a valid blueprint
- the task is to review or approve an existing blueprint
- the request lacks tool choices, verifiable acceptance targets, or locatable structural details

# Inputs
- project or repository name
- proof that the lane is greenfield or baseline-only
- project purpose and baseline scope
- required capabilities, skill dependencies, and toolchain choices
- concrete structure expectations for packages, entrypoints, and support files
- measurable quality targets and acceptance signals

# Process
1. Confirm the lane is truly greenfield. If the repository already carries meaningful structure or migration conflict, stop and reroute to a retrofit-oriented skill.
2. Freeze the baseline outcome: what the repository must support, what it must exclude, and how success will be observed.
3. Specify concrete structure expectations for package layout, entrypoints, tests, configuration anchors, and any initial skill dependencies.
4. Make toolchain choices explicit, including packaging, linting, type checking, testing, and execution conventions.
5. Record quality and acceptance signals in observable terms rather than workflow-specific commands alone.
6. Keep strong fit boundaries: the blueprint should help design a greenfield baseline, not authorize execution, copy operations, or destructive changes.

# Recommended Output Shape
- Project overview
- Greenfield fit confirmation
- Structural expectations
- Toolchain expectations
- Quality targets
- Acceptance signals
- Non-goals
- Open questions

# Validation
Before proceeding, confirm:
- the lane is greenfield rather than retrofit
- structure expectations are concrete enough to locate packages, tests, and entrypoints
- tool choices are explicit rather than implied
- acceptance signals are measurable

# Boundaries
- Do not couple the output to a locked executor schema or required provenance format.
- Do not execute the blueprint, copy skills, or create project files as part of this skill.
- Do not treat retrofit-shaped repositories as greenfield just to keep moving.

# Local references
- `examples.md`: greenfield-only blueprint examples covering fit checks, structure expectations, and non-fit reroutes
