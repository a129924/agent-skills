# Blueprint Contract

Use this reference when authoring a greenfield `blueprint.md`.

This contract intentionally mirrors the blueprint v1 shape already consumed by
`python-project-init-greenfield`. Authoring must reuse that shape exactly.

## Fixed section order

The blueprint must use this heading order exactly:

1. `## Project Overview`
2. `## Required Skills`
3. `## Toolchain Expectation`
4. `## Structural Invariants`
5. `## Quality Thresholds`
6. `## Acceptance Criteria`

Missing a required heading, reordering headings, or adding compatibility aliases
is a contract error.

## Acceptance block rules

- `## Acceptance Criteria` is mandatory.
- A fenced block tagged `yaml [sensing-assertions]` must appear immediately after
  that heading.
- If human-readable explanation is needed, it may appear only after the fenced
  block, not before it.
- Each assertion record must include:
  - `kind`
  - `target`
  - `expected`
- Unsupported assertion kinds must not be invented during authoring.

## Human-readable section syntax

Preferred bullet forms:

- `- Key: Value`
- `- Key @ Version: Purpose`

Interpretation rules:

- listed items are required unless they end with `(Optional)`
- trailing parenthetical notes should not change the parsed semantic key
- non-matching prose lines may exist as human-only explanation, but they should
  not carry machine-readable meaning that the executor must guess

## Section-specific meaning

### `## Project Overview`

- summarize the repository purpose and baseline-goal intent
- keep the prose concrete enough that later sections can stay aligned
- do not hide missing structural decisions behind high-level aspiration language

### `## Required Skills`

- use exact current-library skill directory names as keys
- describe the role or purpose of each skill after the colon
- if `(Optional)` is used, keep it after the exact skill name

Examples:

```markdown
- sense-env-scaffold: Acceptance verification runner
- python-testing-pytest: Test baseline
- python-docstrings (Optional): Optional docstring policy
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

These keys guide baseline configuration and acceptance expectations. They do not
authorize authoring to invent new governance rules.

## Normalization rules

These normalization rules apply to semantic keys such as Toolchain labels,
Structural Invariant prefixes, and Quality Threshold labels. They do **not**
rewrite `Required Skills` names.

- key parsing is case-insensitive for semantic labels
- underscores and hyphens normalize to the same semantic key
  - `type_checking` == `type-checking`
- keys outside the recommended sets are allowed when their purpose is clear
- unknown semantic keys should be translated from stated purpose, not treated as
  automatic errors

For `Required Skills` specifically:

- do not normalize case
- do not rewrite `_` and `-`
- only trim surrounding whitespace and ignore the trailing `(Optional)` marker
  for exact-name validation

## Contract-error conditions

Treat these as authoring stop-and-ask or stop-and-fix conditions:

- missing required heading
- headings out of the locked order
- missing `yaml [sensing-assertions]` block
- prose placed before the fenced sensing block under `## Acceptance Criteria`
- malformed machine-readable assertion block
- unsupported assertion kind
- abstract contract text that leaves required structure non-locatable
- attempts to widen the schema beyond blueprint v1
