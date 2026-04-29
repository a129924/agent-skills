# Retrofit Plan V2 Contract

Use this reference when `python-project-retrofit` parses `retrofit-plan.md`.

## Fixed heading order

The executor accepts this exact heading order only:

1. `## Survey Summary`
2. `## Gap Analysis`
3. `## Target Transformation`
4. `## Migration Strategy`
5. `## Acceptance Criteria`

There is no compatibility layer from old headings such as `## Project Overview`
or `## Target Structure`.

## Required machine-readable blocks

### `## Migration Strategy`

The section must contain a fenced block tagged `yaml [migration-strategy]`
with at least:

```yaml [migration-strategy]
risk_level: LOW
destructive_actions: []
backup_required: false
```

Parsing rules:

- `risk_level` must be `LOW` or `HIGH`
- `MEDIUM` is reserved and should be treated as unsupported for current execution
- `destructive_actions` must be a YAML sequence, even when empty
- `backup_required` must be the explicit YAML boolean `true` or `false`
- any other `backup_required` value or type is a contract parsing error
- prose may explain the strategy, but the YAML block is the execution source of truth

### `## Acceptance Criteria`

The section must contain a fenced block tagged `yaml [sensing-assertions]`.
Each assertion record must contain:

- `kind`
- `target`
- `expected`

Unsupported or malformed assertions remain contract errors.

## Section interpretation

- `## Survey Summary`: human-readable current-state context
- `## Gap Analysis`: concrete mismatches and likely blockers
- `## Target Transformation`: desired end-state paths and configuration surfaces
- `## Migration Strategy`: machine-readable risk metadata plus explanatory prose
- `## Acceptance Criteria`: machine-readable post-retrofit verification contract

`Migration Direction`, if present, is strategy-only context. It cannot choose
runtime gate answers.

## Runtime implications

- a `LOW` plan that still implies destructive execution must fail the Risk Alignment Check
- a `HIGH` plan must support destructive preview generation from `destructive_actions`
- missing destructive detail is a blocking contract problem, not a reason to improvise

## Contract errors

Treat these as blocking parse errors:

- missing required heading
- headings out of order
- old or mixed heading sets
- missing or malformed `yaml [migration-strategy]`
- missing or malformed `yaml [sensing-assertions]`
- unsupported `risk_level`
- `backup_required` set to any value other than the YAML boolean `true` or `false`
- destructive execution implied by the plan while `destructive_actions` is empty or incomplete
