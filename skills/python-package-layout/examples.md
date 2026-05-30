# Examples

- Positive: Recommend `src/weather_client/` for reusable code, keep `pyproject.toml` as the metadata and entry-point anchor, place CLI glue in a thin module, and keep tests in `tests/` importing the packaged module normally.
- Positive: For a CLI-enabled package, keep command-line parsing thin and delegate real behavior into package code under `src/<package_name>/`.
- Negative: Leave reusable modules at the repo root, let tests pass only because the current working directory is importable, or treat ad-hoc scripts as the primary home for package logic.
