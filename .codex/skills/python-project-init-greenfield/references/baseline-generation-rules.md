# Baseline Generation Rules

Use this reference when `python-project-init-greenfield` turns a valid
`blueprint.md` into a repository baseline.

## Default layout

The default greenfield layout is:

```text
.
├── .codex/
│   ├── skills-provenance.json
│   └── skills/
├── .github/
│   └── copilot-instructions.md
├── .gitignore
├── .env.example
├── .pre-commit-config.yaml
├── README.md
├── blueprint.md
├── pyproject.toml
├── scripts/
├── src/
└── tests/
```

Preserve `blueprint.md` as the persistent design contract.

## Required baseline files

Create these baseline surfaces unless the blueprint explicitly narrows them:

- `pyproject.toml`
- `README.md`
- `.gitignore`
- `.env.example`
- `.pre-commit-config.yaml`
- `.github/copilot-instructions.md`
- `src/__init__.py`
- `tests/__init__.py`
- any required invariant paths
- typed boilerplate for each `entrypoint:` invariant

Do not generate business-domain modules, service layers, or concrete secrets.

## Package naming

- prefer an explicit `package:` invariant
- otherwise derive the package name from the repository or directory name using `snake_case`
- normalize `-` to `_`
- keep the derived name Python-friendly; do not invent branding-driven package names

## Entrypoint boilerplate

Every generated `entrypoint:` file should contain typed minimal starter code, not
an empty file.

Expected traits:

- `main() -> None`
- at least one explicit import such as `logging` or `sys`
- a short comment that the baseline is governed by installed `.codex/skills`
- no speculative domain logic

## `pyproject.toml` expectations

Generate a usable uv-aligned baseline, not an over-opinionated application config.

Minimum expectations:

- project metadata
- Python requirement aligned to the blueprint
- pytest configuration
- ruff configuration
- pyright configuration
- room for quality-threshold translation when the blueprint gives explicit targets

Prefer a baseline suitable for:

- `uv sync`
- `uv run pytest`
- `uv run ruff check .`
- `uv run pyright`

## README minimum content

`README.md` should not be title-only.

Include at least:

- project title and short summary
- `## Governance` section listing installed skills and versions
- uv quick-start notes
- acceptance note pointing to the canonical `sense-env-scaffold` CLI projection path

## Placeholder-only surfaces

Keep these intentionally safe:

- `.env.example`
- placeholder `.github/copilot-instructions.md`

Use placeholders, comments, and guidance-only text. Do not write real credentials or
repo-specific policy that is not supported by the installed skills.

The placeholder `.github/copilot-instructions.md` should explicitly:

- tell Copilot to consult installed skills under `.codex/skills/`
- prefer the canonical `sense-env-scaffold` acceptance command before deeper repo-specific assumptions
- avoid inventing business-domain policy that the repository has not declared yet

## Required-skills deployment

When copying `Required Skills`:

- use the active source library as the source of truth
- validate that each skill folder contains at least `SKILL.md`
- copy the full folder, including companion files and local assets such as `references/`, `scripts/`, or `templates/`
- stop for human guidance if the target already has materially different same-named skill content

Do not create fake placeholder skill folders just to satisfy the blueprint.

## Provenance recording

Record installed-skill provenance in `.codex/skills-provenance.json`.

Capture at least:

- `skill_name`
- `source_version`
- `source_hash`

If the source library exposes a canonical version file, use it. In this repository,
the root `VERSION` file is the expected source-version baseline.

## Safe merge versus human gate

Safe additive merges may include:

- appending missing ignore patterns
- adding absent placeholder sections
- creating files that do not yet exist

Human approval is required for:

- replacing materially different config
- replacing or merging divergent skill folders
- overwriting a README with meaningful existing content
- any ambiguous path where "safe" is not obvious

## Acceptance handoff

Greenfield init is not complete until it closes the loop with acceptance.

Expected handoff:

1. ensure `python3 .codex/skills/sense-env-scaffold/scripts/sense_env.py` is locally available
2. run acceptance against `blueprint.md`
3. read the resulting success or gap output
4. stop on acceptance gaps instead of inventing unapproved fixes

If that canonical CLI path is unavailable, the skill must stop and explain that the
acceptance handoff cannot be completed yet.

## Non-goals

This skill does not own:

- retrofit / repair of established repositories
- CI/CD pipeline generation
- infrastructure scaffolding
- changing the blueprint schema
- modifying `sense_env.py`
