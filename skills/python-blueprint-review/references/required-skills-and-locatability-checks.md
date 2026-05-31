# Capability and Locatability Checks

Use this reference when reviewing capability requirements and structure in an
authored greenfield `blueprint.md`.

## Capability requirement clarity

The blueprint must state required capabilities concretely enough that the
intended dependency and tooling surface can be understood without guessing.

Acceptable examples:
- `pytest for automated test execution`
- `ruff for linting and import sorting`
- `Typer-based CLI entrypoint`

Blocking examples:
- `standard testing`
- `normal developer tooling`
- `whatever linting is appropriate`

Review should return `needs-rework` when:
- capability requirements are present only as generic wishes
- implementation-critical tooling or dependency choices are left implicit
- the author expects a downstream implementer to infer the real requirement surface

The reviewer must not:
- require exact current-library skill-name matches
- normalize or repair capability names automatically
- substitute a guessed tool or skill on the author's behalf

## Structural locatability rule

Structure and invariants must be concrete enough that implementation does not
need reinterpretation.

At minimum, review should expect:
- real package names when package structure matters
- real filesystem paths
- real entrypoint file paths
- mutually consistent structure across all locators

## Locatable versus abstract

### Acceptable

```markdown
- package: weather_service
- path: src/weather_service
- path: tests
- entrypoint: src/weather_service/main.py
```

### Blocking

```markdown
- path: modern layout
- package: good defaults
- entrypoint: standard CLI
```

These blocking examples fail because downstream implementation would still need
to invent the real filesystem structure.

## Contradiction checks

Return `needs-rework` when locators disagree, for example:

```text
- package: weather_service
- path: src/service_core
```

```text
- entrypoint: src/weather_service/main.py
- path: app/
```

The review should not guess which locator is authoritative.

## Review response pattern

When these checks fail:

1. identify the exact ambiguous capability or non-locatable structural item
2. explain why downstream implementation is blocked
3. return `needs-rework`
4. describe the required contract repair without rewriting the blueprint inline
