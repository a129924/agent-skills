---
name: python-pre-commit
description: Configures pre-commit hooks for uv-based Python projects by producing a valid `.pre-commit-config.yaml` with the canonical hook set. Use this when a uv Python project needs pre-commit setup or an existing config needs hooks merged in.
---

# Purpose
Produce a valid `.pre-commit-config.yaml` for a uv-based Python project with the canonical hook set (ruff, ruff-format, pre-commit-hooks). Keep slow hooks (pytest, pyright) on `manual` stage so they never block ordinary commits.

# Trigger / When to use
Use this skill when:
- A uv-based Python project has no `.pre-commit-config.yaml` and needs one created from scratch.
- An existing `.pre-commit-config.yaml` in a uv project is missing canonical hooks and needs them merged in.
- The user asks to "set up pre-commit", "add pre-commit hooks", or "configure commit hooks" for a uv Python project.

Do not use this skill when:
- The project does not use uv (pip, poetry, conda, or bare virtualenv).
- The request is about CI/CD pipeline configuration (GitHub Actions, pre-commit.ci cloud service).
- The request is about secrets scanning hooks (detect-secrets, gitleaks, etc.).
- The request asks for `.git/hooks/` file creation rather than `.pre-commit-config.yaml`.

# Inputs
- The target project directory path.
- Whether a `.pre-commit-config.yaml` already exists.
- Whether pyright strict mode is used in the project (determines whether to include the optional pyright hook).
- The ruff version in `pyproject.toml` (to align `rev` in ruff-pre-commit).

# Process
1. **Check for existing config** — look for `.pre-commit-config.yaml` in the project root.
   - **New config (file does not exist)**: create a fresh file with the full canonical hook set from `references/hooks-catalog.md`.
   - **Update existing config (file exists)**: read the current file, identify which canonical hooks are missing, and merge them in without overwriting hooks the user has already configured.

2. **Determine ruff rev** — run `uv run ruff --version` to get the actual resolved version and use that as the `vX.Y.Z` tag for `ruff-pre-commit`. If ruff is not yet installed or the command fails, keep the existing `rev` unchanged and inform the user to verify version alignment manually before committing.

3. **Decide on optional hooks**:
   - Include the `pytest` hook using `stages: [manual]`. It must never be on the default stage.
   - Include the `pyright` hook with `stages: [manual]` only if the project uses pyright strict mode.

4. **Write the config** — produce `.pre-commit-config.yaml` following the hook structure in `references/hooks-catalog.md`. Use `entry: uv run <cmd>` for all local hooks.

5. **Provide install command** — after writing the file, output the commands the user must run manually:
   ```
   uv run pre-commit install
   uv run pre-commit run --all-files
   ```
   Do not run these commands automatically; report them for the user to execute.

# Examples
- **Positive**: A new uv project has no `.pre-commit-config.yaml`. The skill creates one with ruff, ruff-format, and pre-commit-hooks at default stage, and a pytest hook at `manual` stage. Running `uv run pre-commit run --all-files` exits 0.
- **Negative**: Adding pytest as a default-stage hook so every `git commit` runs the full test suite. This blocks ordinary commits and defeats the purpose of fast pre-commit checks. pytest must always use `stages: [manual]`.

# Outputs
- `.pre-commit-config.yaml` in the project root.
- Install instructions for the user:
  ```
  uv run pre-commit install
  uv run pre-commit run --all-files
  ```

# Boundaries
- Does not cover CI/CD pipeline configuration (GitHub Actions, pre-commit.ci).
- Does not support non-uv toolchains (pip, poetry, conda).
- Does not manage secrets scanning hooks (detect-secrets, gitleaks, etc.).
- Does not write `.git/hooks/` files directly; only produces `.pre-commit-config.yaml`.
- Does not run `uv run pre-commit install` or `uv run pre-commit run --all-files` autonomously; those commands are the user's responsibility.

# Local references
- `reference.md`: index overview pointing to split topic files in `references/`.
- `references/hooks-catalog.md`: canonical YAML blocks for ruff, pre-commit-hooks, pytest, and pyright hooks.
- `references/stage-matrix.md`: stage decision table (`commit` / `manual` / `push`) and manual-run commands.
- `references/uv-run-format.md`: `uv run` + `language: system` entry rationale with correct and incorrect patterns.
- `references/version-pinning.md`: ruff rev alignment strategy, upgrade steps, and pre-commit-hooks rev guidance.
- `examples.md`: detailed scenarios for new setup, config merging, pyright strict projects, and anti-patterns.
