# Required Skills Validation

Use this reference when authoring `## Required Skills` in a greenfield
`blueprint.md`.

## Validation rule

Every named skill in `## Required Skills` must resolve to a real current-library
folder under:

```text
skills/<skill-name>/
```

with at least:

```text
skills/<skill-name>/SKILL.md
```

Validation is authoring-time blocking. Do not leave unresolved names for the
executor to discover later.

## Exact-name policy

Validate skill names exactly as authored.

Allowed preprocessing:
- trim surrounding whitespace
- ignore a trailing `(Optional)` marker for validation purposes only

Not allowed:
- changing case
- rewriting `_` to `-` or `-` to `_`
- substituting “close enough” skills
- inventing placeholders for not-yet-created skills
- assuming a future publish step will add the missing skill

## Optional-item handling

The `(Optional)` marker changes downstream installation weight, not library-name
validation.

Examples:

```markdown
- python-docstrings (Optional): Optional docstring guidance
- python-testing-pytest: Required testing baseline
```

Both lines still require exact-name validation against the current library.
If either named skill is absent, authoring must stop and ask.

## Validation examples

### Valid

```markdown
- sense-env-scaffold: Acceptance verification runner
- python-type-hints-strict: Strict typing baseline
- python-docstrings (Optional): Optional docstring guidance
```

### Invalid: guessed alias

```markdown
- python_type_hints_strict: Strict typing baseline
```

Reason: `_` versus `-` is not normalized for skill names.

### Invalid: case change

```markdown
- Python-Testing-Pytest: Testing baseline
```

Reason: case must match the current library exactly.

### Invalid: missing library folder

```markdown
- python-linting-baseline: Shared lint policy
```

Reason: if `skills/python-linting-baseline/` does not exist, authoring
must stop and ask.

## Blocking conditions

Stop and ask when any of these is true:

- a named skill folder is absent from the current library
- the folder exists but `SKILL.md` is missing
- the request uses an alias, shorthand, or future-planned skill name
- the human asks to “just keep the name for now” even though the library does not
  contain it
- the blueprint would otherwise be handed to `python-project-init-greenfield`
  with unresolved library dependencies

## Authoring response pattern

When validation fails:

1. identify the exact unresolved skill name
2. identify the missing expected path under `skills/`
3. stop authoring
4. ask the human to choose an existing exact skill name or add the missing skill
   to the library before blueprint handoff
