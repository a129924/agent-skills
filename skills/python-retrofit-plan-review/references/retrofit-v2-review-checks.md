# Retrofit V2 Review Checks

Use this reference when reviewing an authored Retrofit V2 `retrofit-plan.md`.

This file intentionally mirrors the locked Retrofit V2 contract already consumed
by `python-project-retrofit`. Review must enforce that contract, not invent a
new schema.

## Locked heading order

The plan must use this exact order:

1. `## Survey Summary`
2. `## Gap Analysis`
3. `## Target Transformation`
4. `## Migration Strategy`
5. `## Acceptance Criteria`

Review should fail when:
- any required heading is missing
- headings are reordered
- old headings such as `## Project Overview` or `## Target Structure` appear
- old and new heading families are mixed together

## `yaml [migration-strategy]` rules

`## Migration Strategy` must contain a parseable fenced block tagged
`yaml [migration-strategy]` with at least:

```yaml [migration-strategy]
risk_level: LOW
destructive_actions: []
backup_required: false
```

Review rules:
- `risk_level` must be `LOW` or `HIGH`
- `MEDIUM` is unsupported for current execution and must fail review
- `destructive_actions` must be a YAML sequence, even when empty
- `backup_required` must be the YAML boolean `true` or `false`
- prose may explain strategy after the block, but the block is the execution-facing source of truth
- prose must not contradict the machine-readable fields

## `yaml [sensing-assertions]` rules

`## Acceptance Criteria` must contain a parseable fenced block tagged
`yaml [sensing-assertions]`.

Each assertion record must include:
- `kind`
- `target`
- `expected`

Supported assertion kinds are only:
- `path_exists`
- `path_type`
- `command_available`

Review should fail when:
- the block is missing or malformed
- an assertion record omits `kind`, `target`, or `expected`
- an assertion kind falls outside the supported subset
- review attempts to widen the assertion contract instead of rejecting the plan

## Narrow machine-readable contract expectation

Review should assume the same narrow, execution-facing intent already used by the
current tooling:
- the `migration-strategy` block must stay machine-readable and unambiguous
- the `sensing-assertions` block must stay machine-readable and unambiguous
- human-readable prose is allowed as explanation, but not as a substitute for required fields

## Contract-breaking review outcomes

Return `needs-rework` when the plan:
- drifts from the locked Retrofit V2 heading order
- lacks a valid `yaml [migration-strategy]` block
- lacks a valid `yaml [sensing-assertions]` block
- uses unsupported `risk_level` values
- uses unsupported sensing assertion kinds
- omits required assertion fields
- introduces schema surface the executor does not already consume
