# Blueprint Parsing Contract

Use this reference when `python-project-init-greenfield` reads `blueprint.md`.

## Fixed section order

The blueprint must use this logical order exactly:

1. `## Project Overview`
2. `## Required Skills`
3. `## Toolchain Expectation`
4. `## Structural Invariants`
5. `## Quality Thresholds`
6. `## Acceptance Criteria`

Missing any required section is a contract error for greenfield init.

## Acceptance block rules

- `## Acceptance Criteria` is mandatory.
- A fenced block tagged ````yaml [sensing-assertions]```` must appear immediately after that heading.
- Each v1 assertion record must contain:
  - `kind`
  - `target`
  - `expected`
- Natural-language explanation may exist under the heading, but not inside the machine-readable block.
- Unsupported assertion kinds are forbidden in blueprint v1 and should stop init.

## Human-readable section syntax

Preferred bullet forms:

- `- Key: Value`
- `- Key @ Version: Purpose`

Interpretation rules:

- listed items are required unless they end with `(Optional)`
- trailing parenthetical notes should not change the parsed key
- non-matching prose lines are human-only explanation and should be skipped without error

## Section-specific meaning

### `## Required Skills`

- use exact skill directory names as keys
- interpret the value as the role or purpose
- examples:

```markdown
- sense-env-scaffold: Acceptance verification runner
- python-testing-pytest: Test baseline
```

### `## Toolchain Expectation`

Recommended core keys:

- `python`
- `package_manager`
- `linter`
- `formatter`
- `tester`
- `type_checker`

Version markers are optional:

```markdown
- python @ 3.12: Runtime baseline
- package_manager @ uv: Dependency and lock workflow
```

### `## Structural Invariants`

Recommended semantic prefixes:

- `path:`
- `entrypoint:`
- `package:`

Examples:

```markdown
- package: weather_service
- path: src/weather_service
- entrypoint: src/weather_service/main.py
```

### `## Quality Thresholds`

Recommended core keys:

- `coverage`
- `type_checking`
- `complexity`
- `line_length`
- `test_pass`
- `lint_pass`

These keys guide baseline configuration and later acceptance expectations; they
do not authorize the initializer to invent extra governance rules.

## Normalization rules

- key parsing is case-insensitive
- underscores and hyphens normalize to the same semantic key
  - `type_checking` == `type-checking`
- keys outside the recommended sets are allowed when their purpose is clear
- unknown keys should be translated from stated purpose, not treated as automatic errors

## Optional-item semantics

- `(Optional)` changes init behavior, not contract parsing
- optional items should prefer placeholders, comments, or illustrative stubs
- optional items should not trigger mandatory installation or heavy scaffolding by default

## Contract-error conditions

Treat these as blocking contract errors:

- missing required heading
- headings out of the locked order
- missing `[sensing-assertions]` block
- malformed YAML-like assertion block
- unsupported assertion kind
- unreadable `blueprint.md`

Do not continue into file creation after a contract error.
