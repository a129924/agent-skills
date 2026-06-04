# Phase 3 Inputs

Phase 3 goal: platform projection and runtime adaptation.

## Skills that need `.codex/skills/` projection

- `agent-skill-creator`
- `agent-skill-template`
- `plan-creator`
- `plan-reviewer`
- `plan-step-tracker`
- `python-blueprint-authoring`
- `python-blueprint-review`
- `python-plan-authoring`
- `python-pre-commit`
- `python-project-init-greenfield`
- `python-project-retrofit`
- `python-pyproject-toolconfig`
- `python-tdd-test-authoring`
- `sense-env-scaffold`

## Skills that need `.codex/agents/` custom agent projection

- none evidenced in Phase 1
- `human_review_required` for any future `.codex/agents/` projection involving `copilot-instructions-init`, `plan-step-tracker`, `python-project-init-greenfield`, `python-project-retrofit`, or `sense-env-scaffold`

## Skills requiring path rewrite

- `agent-skill-creator`
- `agent-skill-template`
- `plan-creator`
- `plan-reviewer`
- `plan-step-tracker`
- `python-blueprint-review`
- `python-project-init-greenfield`
- `python-project-retrofit`
- `copilot-instructions-init`

## Skills requiring script copy or script relocation

- `plan-step-tracker`
- `python-pre-commit`
- `python-pyproject-toolconfig`
- `sense-env-scaffold`

## Skills requiring runtime validation

- `plan-step-tracker`
- `sense-env-scaffold`
- `python-pre-commit`
- `python-pyproject-toolconfig`
- `python-project-init-greenfield`
- `python-project-retrofit`
- `copilot-instructions-init`

## Skills that should not be projected into Codex

- none conclusively in Phase 1, but `copilot-instructions-init` should not be projected as a generic portable skill without an adapter split

## Skills that need platform adapter design

- `copilot-instructions-init`
- `plan-step-tracker`
- `sense-env-scaffold`
- `python-project-init-greenfield`
- `python-project-retrofit`

## Recommended Future Structure

```text
skills/<skill-name>/
  SKILL.md
  scripts/
  templates/
  adapters/
    codex.md
    copilot.md

.codex/skills/<skill-name>/
.codex/agents/<agent-name>.md
.github/skills/<skill-name>/
.github/agents/<agent-name>.md
```
