# Phase 2 Inputs

Phase 2 goal: canonical convergence around `skills/`.

## Skills that can safely use `skills/` as canonical

- `agent-skill-reviewer`
- `business-intent-alignment`
- `business-to-technical-translation`
- `git-branch-naming`
- `git-commit-convention`
- `git-post-merge-workflow`
- `python-project-init-greenfield`
- `python-project-retrofit`
- `worktree-manager`

## Skills where `.github/skills/` has newer or better content to merge

- `agent-skill-creator`
- `agent-skill-template`
- `python-blueprint-authoring`
- `python-library-architecture`
- `python-package-layout`
- `python-plan-authoring`
- `python-pre-commit`
- `python-pyproject-toolconfig`
- `python-tdd-test-authoring`
- `python-blueprint-review`

## Skills where `.codex/skills/` has newer or better content to merge

- none; the 11 materialized `.codex/skills/` entries match either `skills/` or `.github/skills/` projections in this worktree

## Skills that should remain Copilot-only

- `copilot-instructions-init`

## Skills that should be marked deprecated

- none in Phase 1

## Skills requiring human decision before convergence

- `plan-creator`
- `plan-reviewer`
- any alias or authority dispute that would change runtime behavior

## Warning

Do not overwrite `.codex/skills/` blindly for `projection_required` skills.
