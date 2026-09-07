# Version Pinning Strategy

## ruff-pre-commit rev

**Goal**: keep the pre-commit hook version aligned with the intended ruff version to avoid split-brain lint results between the hook and CI.

| Approach | When to use | Trade-off |
|----------|------------|-----------|
| Keep the existing pin | Merge missing hooks | Preserves current behavior; upgrading is a separate choice |
| Use the generator's documented default | New config with no requested override | Reproducible pin; does not claim latest release |
| Check ruff-pre-commit releases | Explicit upgrade or version selection | Authoritative source; requires lookup |

**Source of truth**: https://github.com/astral-sh/ruff-pre-commit/releases<br>
The `rev` for `ruff-pre-commit` is independent of the ruff version resolved by `uv`. When choosing a new pin, verify it against the releases page rather than inventing a tag from the locally installed version. An ordinary merge preserves the existing pin; a new config may use the documented generator default without claiming it is current.

**Updating** (when upgrading ruff):
1. Update the ruff version constraint in `pyproject.toml`.
2. Run `uv sync` to resolve the new version.
3. Check https://github.com/astral-sh/ruff-pre-commit/releases to find the matching rev tag.
4. Update `rev` in `.pre-commit-config.yaml` to the new tag (e.g., `v0.12.0`).
5. Run `uv run pre-commit run --all-files` to validate.

## pre-commit-hooks rev

`pre-commit-hooks` is stable and infrequently breaking. Pin to `v4.6.0` unless a specific newer hook is needed. Update lazily when the project upgrades its Python or pre-commit version.
