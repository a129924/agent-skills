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
- If the topic affects `README.md`, `VERSION`, release notes, or deferred release timing, the topic plan must include a `## Stable library metadata` section.
- `## Stable library metadata` must declare the workflow fields needed to execute the promotion, including at minimum:
  - `README row`: whether `README.md` changes and what row or entry is expected
  - `VERSION bump`: whether `VERSION` changes and the intended bump, or an explicit no-bump decision
  - `timing`: whether promotion happens at `publish-in-progress`, is deferred, or is tied to `release`
- If release notes or deferred release timing are part of the topic, declare them inside `## Stable library metadata`, not only as narrative notes elsewhere.
- Do not treat `Locked Decisions` as a substitute for stable-library metadata; executable metadata must still appear in its own section.
- If `timing=release`, the topic plan must also declare the release action under `Post-merge / release actions` as required by the workflow.
- If no release action exists, `Post-merge / release actions` should say that explicitly rather than leaving release handling implied.
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
