---
name: subagent-dispatch-policy
description: Choose the next allowed role for one bounded task slice, or stop, without encoding workflow bindings, registry behavior, or runtime semantics.
complexity: medium
---

# Purpose

Choose the next role for one bounded task slice, or stop.

This skill decides only whether the Observer should dispatch and which allowed
role name should receive the handoff.

# Trigger / When to use

Use this skill when:

- one bounded task slice is in `INTAKE` or `ROUTING`
- the Observer needs to choose the next role
- the available evidence is already narrowed to one task slice

Do not use this skill when:

- the work is to build the context package itself
- the work is to route after a returned subAgent verdict
- the task requires workflow-to-agent binding, registry lookup, or runtime
  dispatch semantics

# Inputs

- one bounded task slice
- bounded evidence for that task slice
- current Observer state
- allowed target roles:
  - `Planner`
  - `Implementer`
  - `Reviewer`
  - `Correction Planner`

# Process

1. Confirm the task is a single bounded slice.
2. Confirm the Observer is not being asked to self-perform Planner,
   Implementer, Reviewer, or Correction Planner work.
3. Check whether real dispatch can be established:
   - separated role instruction surface
   - separated task context package
   - explicit handoff payload
   - explicit result payload contract
   - no hidden role simulation
4. If any real-dispatch condition is missing, stop.
5. If the task requires registry behavior, workflow binding, runtime semantics,
   or concrete role-agent files, stop.
6. Choose exactly one next role name or return `stop`.
7. Emit the decision without file paths, registry keys, catalog identifiers, or
   launcher-specific names.

# Examples

- **Positive**: A frozen implementation task slice needs concrete edits within
  an allowed write set, real dispatch is available, and the skill returns
  `Implementer`.
- **Negative**: The request asks for "whoever owns `.github/agents/...`" or
  depends on runtime launcher wiring, and the skill returns `stop` instead of a
  path-based target.

# Outputs

- `next_role`: `Planner` | `Implementer` | `Reviewer` | `Correction Planner` |
  `stop`
- `reason`: short factual reason
- `stop_condition`: `none` or exact blocker

# Boundaries

- Do not build the context package.
- Do not route based on a returned subAgent verdict.
- Do not encode full existing workflows.
- Do not output concrete file paths as targets.
- Do not infer agent registry, catalog, or runtime capabilities.

# Local references

- `examples.md`: positive and negative dispatch-selection scenarios, including
  hard-stop cases
