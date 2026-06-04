# Skill Inventory

| Skill Name | skills/ | .github/skills/ | .codex/skills/ | Category | Runtime Mode | Has SKILL.md | Has Scripts | Has Templates | Has Hooks | Has Agents | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| agent-skill-creator | yes | yes | yes | workflow, project-bootstrap | projection_required | yes | no | no | no | no | skills/ and .github/ differ on authoring target path; codex projection materialized in this worktree |
| agent-skill-reviewer | yes | yes | yes | workflow, reviewer | portable | yes | no | no | no | no | codex projection materialized in this worktree |
| agent-skill-template | yes | yes | yes | workflow, project-bootstrap | projection_required | yes | no | no | no | no | template and folder-contract differ on active authoring path; codex projection materialized in this worktree |
| business-intent-alignment | yes | yes | yes | planner, generic | portable | yes | no | no | no | no | codex projection materialized in this worktree |
| business-to-technical-translation | yes | yes | yes | planner, generic | portable | yes | no | no | no | no | codex projection materialized in this worktree |
| copilot-instructions-init | yes | yes | no | project-bootstrap, copilot-only, platform-native | platform_native | yes | no | no | no | no | writes .github/copilot-instructions.md and consumes .github skill inventory |
| git-branch-naming | yes | yes | yes | git, workflow | portable | yes | no | no | no | no | codex projection materialized in this worktree |
| git-commit-convention | yes | yes | yes | git, workflow | portable | yes | no | no | no | no | codex projection materialized in this worktree |
| git-post-merge-workflow | yes | yes | yes | git, workflow | portable | yes | no | no | no | no | codex projection materialized in this worktree |
| git-release-management | yes | yes | no | git, release | portable | yes | no | no | no | no | - |
| plan-creator | yes | yes | yes | planner, workflow | projection_required | yes | no | yes | no | no | fallback contract source differs between surfaces; codex projection materialized in this worktree |
| plan-reviewer | yes | yes | yes | planner, reviewer | projection_required | yes | no | no | no | no | review basis path and blocked behavior differ between surfaces; codex projection materialized in this worktree |
| plan-step-tracker | yes | yes | no | workflow, planner | projection_required | yes | yes | no | no | no | CLI path and supported operation set differ between surfaces |
| python-api-signature | yes | yes | no | python, generic | portable | yes | no | no | no | no | - |
| python-async-await | yes | yes | no | python, generic | portable | yes | no | no | no | no | - |
| python-async-planning | yes | yes | no | python, planner | portable | yes | no | no | no | no | - |
| python-blueprint-authoring | yes | yes | no | python, planner, project-bootstrap | projection_required | yes | no | no | no | no | github surface adds checklist and reference set |
| python-blueprint-review | no | yes | no | python, reviewer, project-bootstrap | projection_required | yes | no | no | no | no | missing canonical counterpart under skills/; validates exact current library root via .github/skills path |
| python-class-design | yes | yes | no | python, generic | portable | yes | no | no | no | no | - |
| python-code-review | yes | yes | no | python, reviewer | portable | yes | no | no | no | no | - |
| python-comprehensions | yes | yes | no | python, generic | portable | yes | no | no | no | no | - |
| python-context-management | yes | yes | no | python, generic | portable | yes | no | no | no | no | - |
| python-control-flow | yes | yes | no | python, generic | portable | yes | no | no | no | no | - |
| python-data-model-methods | yes | yes | no | python, generic | portable | yes | no | no | no | no | - |
| python-decorators | yes | yes | no | python, generic | portable | yes | no | no | no | no | - |
| python-descriptors-attribute-access | yes | yes | no | python, generic | portable | yes | no | no | no | no | - |
| python-docstrings | yes | yes | no | python, generic | portable | yes | no | no | no | no | - |
| python-error-handling | yes | yes | no | python, generic | portable | yes | no | no | no | no | - |
| python-generators-iterators | yes | yes | no | python, generic | portable | yes | no | no | no | no | - |
| python-implementation-review | yes | yes | no | python, reviewer | portable | yes | no | no | no | no | - |
| python-library-architecture | yes | yes | no | python, generic | portable | yes | no | no | no | no | github surface adds reference.md and broader validation wording |
| python-model-selection | yes | yes | no | python, generic | portable | yes | no | no | no | no | - |
| python-module-boundaries | yes | yes | no | python, generic | portable | yes | no | no | no | no | - |
| python-naming | yes | yes | no | python, generic | portable | yes | no | no | no | no | - |
| python-operator-overloading | yes | yes | no | python, generic | portable | yes | no | no | no | no | - |
| python-package-layout | yes | yes | no | python, generic | portable | yes | no | no | no | no | github surface adds reference.md and broader routing wording |
| python-plan-authoring | yes | yes | no | python, planner | projection_required | yes | no | yes | no | no | github surface adds templates and expanded plan contract |
| python-plan-review | yes | yes | no | python, reviewer | portable | yes | no | no | no | no | - |
| python-pre-commit | yes | yes | no | python, workflow | projection_required | yes | yes | yes | no | no | github surface adds script, templates, references, and tests |
| python-project-init-greenfield | yes | yes | no | python, project-bootstrap | projection_required | yes | no | no | no | no | - |
| python-project-retrofit | yes | yes | no | python, migration | projection_required | yes | no | no | no | no | - |
| python-pyproject-toolconfig | yes | yes | no | python, workflow | projection_required | yes | yes | yes | no | no | github surface adds script, templates, references, and tests |
| python-retrofit-plan-authoring | yes | yes | no | python, planner, migration | portable | yes | no | no | no | no | - |
| python-retrofit-plan-review | yes | yes | no | python, reviewer, migration | portable | yes | no | no | no | no | - |
| python-serialization-boundaries | yes | yes | no | python, reviewer | portable | yes | no | no | no | no | only REVIEW.md differs |
| python-tdd-test-authoring | yes | yes | no | python, workflow | projection_required | yes | no | no | no | no | github surface adds checklist and verdict-oriented references |
| python-testing-pytest | yes | yes | no | python, generic | portable | yes | no | no | no | no | - |
| python-type-hints-strict | yes | yes | no | python, generic | portable | yes | no | no | no | no | - |
| sense-env-scaffold | yes | yes | no | python, workflow, project-bootstrap | projection_required | yes | yes | no | no | no | runtime assertion handling differs in script implementation |
| worktree-manager | yes | yes | yes | workflow, git | portable | yes | no | no | no | no | codex projection materialized in this worktree |

## Non-standard Structures

- `.codex/skills/` is a materialized first-wave projection surface in this worktree, not a full third canonical tree.
- `python-blueprint-review` exists only under `.github/skills/`; no `skills/python-blueprint-review/` counterpart was found.
- `python-pre-commit`, `python-pyproject-toolconfig`, `plan-step-tracker`, and `sense-env-scaffold` ship scripts and/or tests, so their runtime behavior is not pure-instruction only.
- `agent-skill-creator`, `agent-skill-template`, `plan-creator`, and `plan-reviewer` contain path-sensitive authoring/review contract drift between `skills/` and `.github/skills/`.
