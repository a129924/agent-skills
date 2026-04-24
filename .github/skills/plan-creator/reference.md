# Plan Creator Reference

Use this file to keep topic-plan authoring aligned with the repository workflow.

## Required section meaning

- `Goal / Outcome`: the concrete repository-visible result of the topic
- `Scope`: what the topic will and will not change
- `Locked Decisions`: choices that downstream roles should not re-decide
- `Boundaries / Exclusions`: nearby work that must stay out of the topic
- `Status / Allowed Transitions`: the topic's current workflow status and the only legal transitions
- `Artifact Paths`: exact repo-visible outputs, not broad labels
- `Implementation Steps`: what creator work will produce
- `Validation / Acceptance Checks`: the signals reviewer and main agent should verify
- `Reviewer Handoff`: fixed machine-consumable JSON contract
- `Post-merge / release actions`: what happens after merge, including when no release action exists
- `Open Questions / Unresolved Items`: only what truly remains open

## Stable-library rule

- If the topic does **not** affect stable-library surfaces, say so explicitly.
- If the topic affects `README.md`, `VERSION`, release notes, or deferred release timing, the plan must declare that intent explicitly.
- Do not mix review-ready-only work with undeclared stable-library promotion.

## Artifact path rule

- Treat `Artifact Paths` as an executable contract.
- Name concrete paths such as `.github/skills/<skill-name>/SKILL.md`, not vague phrases such as "docs" or "skill files".
- If later work appears outside the listed paths, that is a plan-alignment problem, not a harmless detail.

## Role boundary rule

- Planning actor writes the topic plan.
- Creator implements inside the plan's locked boundaries.
- Reviewer evaluates the draft independently.
- Main Agent owns execution routing, branch preparation, planner alignment, PR flow, and post-merge orchestration.
- Do not collapse these roles into one blended author.

## Stop-and-ask triggers

Stop and ask when:
- the real topic outcome is unclear
- artifact paths cannot be stated exactly
- stable-library timing is unclear
- release intent is implied but not declared
- the topic tries to mix multiple jobs that should be separate topics

## Template usage rule

- Start from `templates/topic-plan-template.md`.
- Replace prompts with explicit repository-specific answers.
- Delete irrelevant prompt text; do not leave template scaffolding in the final topic plan.
