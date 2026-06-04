# Summary

Phase 1 did not modify skill contents or perform convergence.

## Counts

- Skills found under `skills/`: 49
- Skills found under `.github/skills/`: 50
- Skills found under `.codex/skills/`: 11 materialized projections
- Unique skill identities: 50
- Skills common to all three surfaces: 11
- Skills only in `skills/`: 0
- Skills only in `.github/skills/`: 1 (`python-blueprint-review`)
- Skills only in `.codex/skills/`: 0
- Copilot-only skills: 1 (`copilot-instructions-init`)
- Portable skills: 35
- Projection-required skills: 14
- Platform-native skills: 1

## Highest-Risk Drift Findings

- `agent-skill-creator` and `agent-skill-template` disagree on whether new authoring output targets `skills/` or `.github/skills/`.
- `plan-creator` and `plan-reviewer` disagree on fallback/review basis paths and blocking behavior, so planning-spine overwrite is unsafe.
- `plan-step-tracker`, `sense-env-scaffold`, `python-pre-commit`, and `python-pyproject-toolconfig` carry script-level runtime contracts, so later projection cannot be a blind file copy.
- `copilot-instructions-init` remains platform-native because it generates `.github/copilot-instructions.md` from GitHub-surface assumptions.

## Recommended Next Steps

- Phase 2: converge same-name generic skills toward `skills/` only where content is already identical or where drift is low-risk and evidence-backed.
- Phase 3: design projection/adaptor treatment for script-bearing or path-sensitive skills before touching `.codex/skills/` or runtime callers.

## Scope Reminder

- Report output is `1` summary plus `8` analysis reports = `9 Phase 1 files`.
- `.github/skills/` and `.codex/skills/` were evaluated here as compatibility/projection surfaces, not auto-promoted to canonical truth.
