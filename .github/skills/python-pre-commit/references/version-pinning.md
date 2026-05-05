# Version Pinning Strategy

## ruff-pre-commit rev

**Goal**: keep the pre-commit hook version aligned with the ruff version in `pyproject.toml` to avoid split-brain lint results.

| Approach | When to use | Trade-off |
|----------|------------|-----------|
| Match `pyproject.toml` ruff version | Project pins ruff in dev deps (e.g., `ruff>=0.11.0,<0.12`) | Best consistency; requires updating both places when upgrading ruff |
| Pin to current latest stable | Greenfield project with no ruff version constraint | Easy to set up; may drift from CI ruff version over time |

**Recommendation**: always check `pyproject.toml` first. If ruff is pinned (even loosely), derive the `rev` from that version. Use `uv run ruff --version` to confirm the resolved version in the project environment.

**Updating both together** (when upgrading ruff):
1. Update the ruff version constraint in `pyproject.toml`.
2. Run `uv sync` to resolve the new version.
3. Run `uv run ruff --version` to confirm the resolved version.
4. Update `rev` in `.pre-commit-config.yaml` to match (e.g., `v0.12.0`).
5. Run `uv run pre-commit run --all-files` to validate.

## pre-commit-hooks rev

`pre-commit-hooks` is stable and infrequently breaking. Pin to `v4.6.0` unless a specific newer hook is needed. Update lazily when the project upgrades its Python or pre-commit version.
