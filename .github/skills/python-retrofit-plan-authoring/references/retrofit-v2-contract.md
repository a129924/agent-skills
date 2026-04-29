# Retrofit V2 Contract

Use this reference when authoring a Retrofit V2 `retrofit-plan.md`.

## Fixed section order

The contract must use this heading order exactly:

1. `## Survey Summary`
2. `## Gap Analysis`
3. `## Target Transformation`
4. `## Migration Strategy`
5. `## Acceptance Criteria`

Missing a required heading, reordering headings, or using old Retrofit V1
headings is a contract error.

## Section meaning

### `## Survey Summary`

- summarize observable current-state facts only
- name the current entrypoints, packages, config surfaces, and notable layout constraints
- do not describe the desired future state here

### `## Gap Analysis`

- compare current-state facts to the intended target state
- name concrete mismatches, likely shadow conflicts, config-remnant conflicts, and other retrofit blockers
- prefer exact paths or filenames over generalized phrases such as “legacy structure”

### `## Target Transformation`

- declare the desired end state with concrete paths, entrypoints, config outcomes, and toolchain outcomes
- `Migration Direction` may appear here or directly below as a strategy declaration
- `Migration Direction` must not replace runtime gate choices such as `move`, `delete`, `coexist`, `migrate`, `preserve`, or `abort`

### `## Migration Strategy`

- include a fenced block tagged `yaml [migration-strategy]`
- treat that fenced block as the machine-readable source of truth for risk metadata
- prose may explain the strategy after the block, but prose must not contradict the YAML fields

Minimum required fields:

```yaml [migration-strategy]
risk_level: LOW
destructive_actions: []
backup_required: false
```

### `## Acceptance Criteria`

- include a fenced block tagged `yaml [sensing-assertions]`
- each assertion record must include:
  - `kind`
  - `target`
  - `expected`
- explanatory prose may follow the block, but the machine-readable block must stay explicit and complete

## Contract-authoring rules

- use concrete paths, filenames, and tool names when the retrofit intent depends on them
- keep human-readable explanation outside the machine-readable blocks
- do not rely on the executor to translate old headings into V2 headings
- do not leave destructive implications hidden only in prose
- do not continue when the contract is too abstract to locate affected surfaces

## Contract-error conditions

Treat these as stop-and-ask or stop-and-fix conditions:

- missing required heading
- headings out of the locked order
- old headings such as `## Project Overview` or `## Target Structure`
- missing or malformed `yaml [migration-strategy]`
- missing or malformed `yaml [sensing-assertions]`
- `risk_level` outside `LOW` or `HIGH`
- target transformation that lacks concrete locators such as paths, files, tool names, or verifiable targets
- prose that tries to pre-authorize runtime gate outcomes
