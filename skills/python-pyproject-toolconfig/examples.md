# Examples

- Positive: Add missing `tool.ruff`, `tool.pyright`, and `tool.pytest.ini_options` snippets to an existing `pyproject.toml` while skipping sections that already exist.
- Positive: Stop and ask when the Python version or import package name is not explicit enough to write correct append-only guidance.
- Negative: Rewrite an existing `tool.pyright` section in place, guess the package name, or widen the skill into `coverage`/`mypy` maintenance.
