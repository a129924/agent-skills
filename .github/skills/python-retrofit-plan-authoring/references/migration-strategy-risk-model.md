# Migration Strategy Risk Model

Use this reference when filling `yaml [migration-strategy]` in a Retrofit V2
contract.

## Required YAML shape

```yaml [migration-strategy]
risk_level: LOW
destructive_actions: []
backup_required: false
```

## Field semantics

### `risk_level`

Current allowed values:

- `LOW`
- `HIGH`

`MEDIUM` is reserved for future extension only and must not be authored or
required by the executor in this topic.

### `destructive_actions`

- use a YAML sequence of concrete human-readable action strings
- list each move, delete, overwrite, relocation, or core-toolchain replacement that could destroy or obscure the current state
- use `[]` only when the retrofit is truly additive or otherwise non-destructive

Examples:

```yaml
destructive_actions:
  - move app.py -> src/weather_service/main.py
  - replace requirements.txt with pyproject.toml
```

### `backup_required`

- `false` for current `LOW` contracts
- `true` for current `HIGH` contracts
- treat this as a recovery-path requirement, not as permission to skip runtime gates

## Risk classification rules

Classify risk from observable physical traits, not comfort level.

Use `LOW` when the plan is limited to:
- pure additions
- non-destructive configuration changes
- explicitly retaining current structure while adding governed surfaces

Use `HIGH` when the plan includes any of these:
- existing directory reshaping
- existing code relocation
- deleting legacy files or directories
- overwriting important config files
- replacing multiple core-toolchain surfaces

## Alignment rules

- if a draft lists destructive actions, it must not use `LOW`
- if the requested transformation is too abstract to classify confidently, stop and ask instead of guessing
- if `risk_level` and `destructive_actions` disagree, fix the contract before handoff
- the executor will rerun a Risk Alignment Check and hard-block a `LOW` plan when destructive actions are discovered during scanning

## Migration Direction note

`Migration Direction` may describe the intended strategic direction, such as:

- additive baseline reinforcement
- staged package relocation
- single-toolchain consolidation

It does not replace `risk_level`, does not replace `destructive_actions`, and
does not authorize runtime conflict-resolution choices.

## Recommended current pairing

For the current V2 contract, prefer this simple alignment:

- `LOW` -> `destructive_actions: []` and `backup_required: false`
- `HIGH` -> non-empty `destructive_actions` and `backup_required: true`
