# Blueprint v1 Review Checks

Use this reference when reviewing an authored greenfield `blueprint.md`.

This file intentionally mirrors the locked blueprint v1 contract already consumed
by `python-project-init-greenfield`. Review must enforce that contract, not invent
a new schema.

## Locked heading order

The blueprint must use this exact order:

1. `## Project Overview`
2. `## Required Skills`
3. `## Toolchain Expectation`
4. `## Structural Invariants`
5. `## Quality Thresholds`
6. `## Acceptance Criteria`

Review should fail when:
- any required heading is missing
- headings are reordered
- a compatibility alias or extra schema heading is added

## Acceptance block rules

- `## Acceptance Criteria` is mandatory.
- A fenced `yaml [sensing-assertions]` block must appear immediately under that
  heading.
- Human-readable explanation may appear only after the fenced block, never before it.
- Each assertion record must include:
  - `kind`
  - `target`
  - `expected`
- Supported blueprint v1 assertion kinds are only:
  - `path_exists`
  - `path_type`
  - `command_available`
- Any other `kind` value is a blocking contract error and must return `needs-rework`.
- Malformed YAML-like structure is a blocking contract error.

## Human-readable section interpretation

Preferred bullet forms:

- `- Key: Value`
- `- Key @ Version: Purpose`

Review notes:
- listed items are required unless they end with `(Optional)`
- trailing parenthetical notes do not change the parsed semantic key
- non-matching prose may exist as explanation, but it must not replace required machine-readable structure

## Contract-breaking review outcomes

Return `needs-rework` when the blueprint:
- drifts from the locked blueprint v1 heading order
- lacks the required fenced sensing block
- places prose before the fenced sensing block
- omits `kind`, `target`, or `expected`
- uses an unsupported assertion kind outside `path_exists`, `path_type`, or `command_available`
- adds schema surface that the executor contract does not already consume
