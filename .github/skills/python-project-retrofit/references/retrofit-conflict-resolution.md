# Retrofit Conflict Resolution

Use this reference when `python-project-retrofit` encounters layout conflicts or
implicit toolchain remnants during retrofit.

## Gate 1: Shadow File Detection

A shadow file conflict exists when the current repository already has a file or
folder whose semantic role overlaps the target structure, but the paths differ.

Common examples:

- root `app.py` versus `src/<package>/main.py`
- `tests.py` versus `tests/test_main.py`
- `service/` at root versus `src/service/`
- legacy CLI wrapper versus planned package entrypoint

### Required resolution menu

For every shadow conflict, offer exactly one of these four human-selected
outcomes:

1. `move` — relocate the current file into the target structure
2. `delete` — remove the current file and keep only the target path
3. `coexist` — keep both paths intentionally
4. `abort` — stop the retrofit without changing the workspace

Do not infer the choice from naming style, file age, or path modernity.

## Gate 2: Implicit Config Mining

Scan for toolchain remnants that imply existing packaging or environment policy:

- `poetry.lock`
- `pyproject.toml`
- `setup.py`
- `setup.cfg`
- `.venv`
- `conda.yml`
- `requirements.txt`
- `Pipfile`

When remnants are found, offer exactly one of these four human-selected
outcomes:

1. `migrate` — carry forward the existing configuration into the target toolchain
2. `delete` — remove the remnants for a clean target state
3. `preserve` — keep the remnants unchanged
4. `abort` — stop the retrofit without changing the workspace

## Conflict-handling rules

- stop and ask; do not auto-resolve
- keep the gate prompt concrete by naming the paths or files involved
- make destructive consequences explicit before the human answers
- if one answer changes the meaning of another gate, rerun the affected analysis
  rather than guessing

## Simultaneous triggers

If both gate families trigger at once, the locked priority order is:

1. Shadow File Detection
2. Implicit Config Mining
3. Git safety and pre-destructive check

Why this order matters:

- path conflicts determine the structural intent
- config remnants determine migration or cleanup scope after structure is clear
- Git safety protects the chosen destructive step immediately before execution

## No auto-merge policy

Conflicting config files must not be auto-merged.

Examples that require a stop-and-ask path:

- `setup.cfg` and `pyproject.toml` both define tool settings
- `requirements.txt` and `Pipfile` imply competing dependency workflows
- Poetry metadata and target uv-style config would require heuristic synthesis

Allowed behavior:

- describe the conflict plainly
- ask which file or toolchain should win
- migrate only the scope the human approved

Disallowed behavior:

- “best effort” line-by-line merges
- silent overwrite because one format is newer
- treating coexistence as implied consent to ignore divergence

## Suggested prompt shape

When you ask the human, keep the prompt direct:

```text
Detected shadow conflict:
- current: app.py
- target: src/weather_service/main.py
- shared intent: primary application entrypoint
Choose one: move | delete | coexist | abort
```

```text
Detected config remnants:
- poetry.lock
- pyproject.toml
Choose one: migrate | delete | preserve | abort
```

The skill should prefer a second explicit question over a combined ambiguous one.
