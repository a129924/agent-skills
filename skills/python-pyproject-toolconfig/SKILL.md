---
name: python-pyproject-toolconfig
description: Define append-only policy and reusable config snippets for adding missing `ruff`, `pyright`, and `pytest` sections to an existing `pyproject.toml` without overwriting existing tool settings.
complexity: medium
risk_profile:
  - ambiguity_sensitive
inputs:
  - explicit Python version
  - explicit import package name
  - existing `pyproject.toml`
  - whether `ruff`, `pyright`, and `pytest` sections already exist
outputs:
  - append-only guidance for missing `pyproject.toml` tool sections
  - reusable snippets for `ruff`, `pyright`, and `pytest`
  - an append / skip decision summary that preserves existing settings
use_when:
  - a Python project has `pyproject.toml` but is missing one or more standard tool sections
  - the task is to standardize lint, typing, and test config while preserving local customization
  - the user needs policy or snippet guidance rather than a script-centric patch flow
do_not_use_when:
  - the project uses `setup.cfg`, `tox.ini`, or separate tool config files instead of `pyproject.toml`
  - the task is to rewrite or merge existing `tool.*` sections deeply
  - the request is primarily about `coverage`, `mypy`, or other out-of-scope tools
---

# Purpose
Provide append-only policy and reusable snippets for adding missing `ruff`, `pyright`, and `pytest` sections to `pyproject.toml` while preserving existing settings.

# Trigger / When to use
Use this skill when:
- a Python project has `pyproject.toml` but is missing one or more standard tool sections
- the task is to standardize lint, typing, and test config while preserving local customization
- the user needs policy or snippet guidance rather than a script-centric patch flow

Do not use this skill when:
- the project uses `setup.cfg`, `tox.ini`, or separate tool config files instead of `pyproject.toml`
- the task is to rewrite or merge existing `tool.*` sections deeply
- the request is primarily about `coverage`, `mypy`, or other out-of-scope tools

# Inputs
- explicit Python version
- explicit import package name
- existing `pyproject.toml`
- whether `ruff`, `pyright`, and `pytest` sections already exist

# Process
1. Confirm `pyproject.toml` exists and the Python version plus package name are explicit; do not guess either value.
2. Inspect whether `ruff`, `pyright`, and `pytest` sections already exist.
3. For each missing section, propose an append-only snippet that does not overwrite existing settings.
4. Keep the contract at policy/snippet level: what to append, what to skip, and why.
5. If a section already exists but appears wrong, treat that as a separate maintenance task rather than silently rewriting it here.

# Recommended Scope
- `tool.ruff`
- `tool.pyright`
- `tool.pytest.ini_options`

# Validation
Before proceeding, confirm:
- `pyproject.toml` exists
- Python version and import package name are explicit
- no proposed action overwrites an existing `tool.*` section
- the guidance stays focused on `ruff`, `pyright`, and `pytest`

# Boundaries
- Do not overwrite or deeply merge existing `tool.*` sections.
- Do not infer Python version or package name without explicit input.
- Do not widen into unrelated tool configuration such as `coverage` or `mypy`.
- Do not make a script/template wrapper the main contract of this skill.

# Local references
- `examples.md`: append-only `pyproject.toml` examples showing missing-section adds, skip behavior, and out-of-scope update cases
