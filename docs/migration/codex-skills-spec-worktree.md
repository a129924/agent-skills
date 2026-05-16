# Codex Skills Spec Worktree

## Purpose

This document defines a bounded `.codex/skills` validation surface for a
dedicated spec worktree topic.

It is intentionally separate from the current `copilot-to-codex-migration`
runway. It does not change the repository's frozen positioning statements, and
it does not declare an active-path cutover.

## Positioning

- This is a spec-worktree validation topic only.
- `.codex/skills/` is a projection / prototype surface for Codex validation.
- `.codex/skills/` is not the canonical source of truth.
- `skills/` remains the intended canonical skill source / target architecture.
- `.github/skills/` remains the current Copilot active authored/reviewed
  workflow path during transition.

## Source Selection Rule

When the same skill exists in both `skills/` and `.github/skills/`, the
`.codex/skills` validation surface must prefer `skills/`.

Fallback rule:

- use `skills/<skill-name>/` first when it exists
- otherwise use `.github/skills/<skill-name>/`

This rule exists to avoid validating an outdated transition-era copy when a
target-architecture promotion result already exists.

## First-Wave Skill Set

### Promote-from-`skills/`

- `business-intent-alignment`
- `business-to-technical-translation`
- `plan-creator`
- `plan-reviewer`

### Fallback-to-`.github/skills/`

- `agent-skill-creator`
- `agent-skill-reviewer`
- `agent-skill-template`
- `git-commit-convention`
- `git-branch-naming`
- `git-post-merge-workflow`
- `worktree-manager`

## Runtime Boundary

This first wave does not validate the runtime/tooling blocker set.

Explicitly excluded from this topic:

- `sense-env-scaffold`
- `plan-step-tracker`
- `python-project-init-greenfield`
- `python-project-retrofit`
- `copilot-instructions-init`

If validation reveals that these blockers must be included, stop and open a
separate runtime/tooling transition topic instead of widening this one.

## Projection Shape

`.codex/skills/` should mirror only the selected first-wave skills and should
preserve source traceability.

Required rules:

- each projected skill must resolve to exactly one upstream source path
- the projection must not silently merge content from both source trees
- the projection must be safe to delete without affecting canonical sources
- validation artifacts in `.codex/skills/` must not be mistaken for active-path
  cutover evidence

## Validation Goals

The first-wave validation is successful only if all of the following are true:

- Codex can discover and read the projected first-wave skills from
  `.codex/skills/`
- the four planning skills promoted into `skills/` still work when projected
  from `skills/`
- creator/reviewer/template and git/worktree skills can be projected from
  `.github/skills/` without source confusion
- the validation surface makes source provenance obvious
- no repository document is changed to claim that `.codex/skills/` is canonical
  or active today

## Removal / Lifecycle

- `.codex/skills/` in this topic is disposable validation scaffolding
- its presence does not change repo governance
- follow-up decisions about a formal Codex projection belong to a later topic
