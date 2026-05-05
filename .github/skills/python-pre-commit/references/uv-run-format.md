# uv run Entry Format

All local hooks in a uv project must use:
```yaml
entry: uv run <command>
language: system
```

## Why `language: system`

pre-commit normally creates an isolated virtualenv for each hook repo. For `repo: local` hooks in a uv project, this would create a separate environment that does not have the project's dependencies installed. Using `language: system` tells pre-commit to use the system Python (which resolves to the uv-managed `.venv` when `uv run` is used as the entry point).

## Why `uv run` instead of direct binary path

- `uv run <cmd>` activates the uv virtual environment automatically, ensuring the correct Python and all project dependencies are available.
- Direct binary paths (`.venv/bin/pytest`) are fragile and break when the venv is recreated.
- `python -m pytest` without `uv run` does not guarantee the uv venv is active.

## Correct

```yaml
entry: uv run pytest
language: system
```

## Incorrect

```yaml
entry: python -m pytest
language: python         # creates a separate pre-commit venv
```

```yaml
entry: .venv/bin/pytest  # fragile absolute path
language: system
```
