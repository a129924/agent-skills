# Structural Invariants Locatability

Use this reference when authoring `## Structural Invariants` for a greenfield
`blueprint.md`.

## Core rule

`Structural Invariants` must be concrete enough for
`python-project-init-greenfield` to consume without reinterpretation.

At minimum, locatable structure should name real package names, real filesystem
paths, real entrypoint files, and any other structure-defining choices that the
executor must scaffold explicitly.

## Locatable versus abstract

### Locatable examples

```markdown
- package: weather_service
- path: src/weather_service
- path: tests
- entrypoint: src/weather_service/main.py
```

These items are locatable because the executor can create or verify them without
guessing intent.

### Non-locatable examples

```markdown
- path: modern layout
- package: good defaults
- entrypoint: standard CLI
```

These items are not locatable because they require interpretation before any file
can be created.

## Authoring requirements

- use concrete path strings instead of style labels
- use a real Python package name when a package namespace matters
- use a full entrypoint path, not only a module concept such as “main app”
- keep tool choices concrete when structure depends on them, such as `src/`
  package layout under `uv`-aligned expectations
- keep related structural items mutually consistent
  - example: `package: weather_service` should align with `path: src/weather_service`

## Stop-and-ask triggers

Stop before handoff when any of these is true:

- the request uses abstract phrases such as “modern layout”, “clean structure”,
  “sensible packages”, or “good defaults”
- the package name is missing and cannot be derived safely from explicit intent
- the entrypoint is described only conceptually, not as a file path
- different requested paths contradict each other
- the structure depends on a tool or layout choice that is still undecided

## Contradiction examples

These require clarification before drafting:

```text
- package: weather_service
- path: src/service_core
```

```text
- entrypoint: src/weather_service/main.py
- path: app/
```

The skill should not guess which locator is authoritative.

## Authoring response pattern

When locatability fails:

1. identify the exact abstract or contradictory item
2. explain why the executor cannot consume it safely
3. ask for a concrete package name, path, entrypoint, or tool choice
4. stop drafting until the missing locator is provided
