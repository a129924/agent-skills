---
name: handoff-routing-policy
description: Route the next allowed role after one explicit subAgent result, or stop, without encoding full workflows, registries, or runtime semantics.
complexity: medium
---

# Purpose

Choose the next route after one explicit subAgent result.

This skill works only after a real dispatch has already occurred and a result
payload has been returned.

# Trigger / When to use

Use this skill when:

- one explicit subAgent result has been returned
- the Observer is in `ROUTING`
- the result includes one frozen verdict value

Do not use this skill when:

- the task is still deciding whether to dispatch
- the task is to build the context package
- the task requires full workflow reconstruction or runtime orchestration logic

# Inputs

- `result_role`: one of `Planner`, `Implementer`, `Reviewer`, `Correction Planner`
- `verdict`: one of
  - `PASS`
  - `PATCH_REQUIRED`
  - `REPLAN_REQUIRED`
  - `MISSING_EVIDENCE`
  - `BLOCKED`
- bounded evidence summary
- explicit blocker list, if any
- optional evidence owner for `MISSING_EVIDENCE`

# Process

1. Confirm the result came from real dispatch rather than Observer simulation.
2. Confirm the verdict is one of the frozen allowed values.
3. If the result reveals runtime semantics, registry behavior, workflow binding,
   or another out-of-scope expansion, stop.
4. Route by verdict without inventing a broader workflow model:
   - `PASS`: choose the next role only if one more bounded role handoff is
     needed; otherwise stop
   - `PATCH_REQUIRED`: route to `Implementer`
   - `REPLAN_REQUIRED`: route to `Correction Planner`
   - `MISSING_EVIDENCE`: route only to the bounded role that can supply the
     missing evidence; if that owner is unknown, stop
   - `BLOCKED`: stop unless a bounded route to `Planner` is explicitly justified
5. Emit exactly one next role or `stop`, with a short factual reason.

# Examples

- **Positive**: An `Implementer` returns `PATCH_REQUIRED` with concrete bounded
  evidence, and the skill routes to `Implementer`.
- **Negative**: A result says "probably approved" with no explicit verdict, and
  the skill refuses to invent one.

# Outputs

- `next_role`: `Planner` | `Implementer` | `Reviewer` | `Correction Planner` |
  `stop`
- `reason`: short factual reason
- `stop_condition`: `none` or exact blocker

# Validation

## Required Checks

- `PASS`: the result came from real dispatch, the Observer is in `ROUTING`, the
  verdict is exactly one frozen allowed value, and the skill returns exactly
  one allowed `next_role` or `stop` consistent with the stated verdict.
- `BLOCKED`: stop when the verdict is unknown, unstructured, or unsupported;
  when the evidence owner for `MISSING_EVIDENCE` is unknown; or when proceeding
  would require invented workflow state, registry behavior, runtime semantics,
  or a broader routing model than this skill allows.

## Quality Checks (best effort)

- `SOFT FAIL`: mark status as `INCOMPLETE` when the allowed verdict is clear
  enough to route or stop, but the bounded evidence summary or blocker detail is
  incomplete.
- Under `SOFT FAIL`, keep the routing decision within the frozen verdict set,
  state the missing evidence explicitly, and avoid inventing additional workflow
  state.

# Failure Handling

## Missing Context

- If the verdict is valid but supporting evidence is partial, return the bounded
  best-effort route or `stop` with the limitation stated explicitly.
- If missing context could reasonably change the next allowed role, mark the
  result `BLOCKED` and stop.

## Ambiguous Requirement

- If the returned result does not contain one frozen verdict value, do not infer
  or normalize it into the allowed set.
- If `MISSING_EVIDENCE` lacks a known bounded owner, stop instead of inventing
  one.

## Execution Limitation

- If the request depends on hidden workflow state, file-path ownership, registry
  identifiers, launcher-specific targets, or runtime orchestration details,
  return `stop` or `BLOCKED` with the limitation stated explicitly.
- Do not fabricate broader workflow progression beyond the single returned
  subAgent result.

# Boundaries

- Do not choose the initial dispatch role.
- Do not build the context package.
- Do not reconstruct the full existing workflow from a step artifact.
- Do not invent verdict values outside the frozen set.
- Do not emit registry identifiers, file paths, or launcher-specific targets.

# Local references

- `examples.md`: verdict-driven routing examples, including stop conditions for
  missing evidence and out-of-scope expansion
