# Required Skills and Locatability Checks

Use this reference when reviewing `## Required Skills` and
`## Structural Invariants` in an authored greenfield `blueprint.md`.

## Exact-name `Required Skills` validation

Every named skill in `## Required Skills` must resolve to a real current-library
folder under:

```text
skills/<skill-name>/
```

with at least:

```text
skills/<skill-name>/SKILL.md
```

Allowed preprocessing:
- trim surrounding whitespace
- ignore a trailing `(Optional)` marker for validation only

Not allowed:
- changing case
- rewriting `_` to `-` or `-` to `_`
- guessing a “close enough” skill
- accepting a future-planned skill that is not in the active library

Review should return `needs-rework` when:
- the named skill folder is absent
- the folder exists but `SKILL.md` is missing
- the authored skill name differs only by case, `_`, or `-`
- the blueprint expects the executor to discover the missing skill later

## Structural locatability rule

`Structural Invariants` must be concrete enough for
`python-project-init-greenfield` to consume without reinterpretation.

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

These blocking examples fail because the executor would have to guess the actual
filesystem structure.

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

1. identify the exact unresolved skill name or non-locatable structural item
2. explain why safe executor handoff is blocked
3. return `needs-rework`
4. describe the required contract repair without rewriting the blueprint inline
