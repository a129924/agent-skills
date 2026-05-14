# Repository Positioning

`agent-skills` is the repository for defining, collecting, and governing Agent
Skills plus the installable layouts that external tooling or platform adapters
consume.

It owns repository positioning, governance rules, and skill-source boundaries.
It does not own fetch, install, sync, or deploy orchestration.

## Current Operating State

Current repository state is:

- `AGENTS.md` is the governance canonical source.
- `.github/skills/` remains the current Copilot active authored and reviewed
  workflow path during transition.
- `skills/` is not the current active workflow path in this topic.
- `skills/` belongs to the intended canonical skill-source direction and target
  architecture only.
- external installer tooling or repositories may consume platform-facing layouts,
  but install orchestration stays outside this repository.

Current operating state and target architecture are intentionally distinct in
this runway. This topic freezes both statements without cutting over the active
workflow path.

## Target Architecture

Target architecture after a separate migration is:

- `skills/` is the intended canonical skill source.
- `skills/` is the long-term authoring, review, and promotion source of truth.
- `.<platform>/skills/...` is a platform projection, adapter layout, or
  compatibility mirror created to satisfy platform-specific directory rules and
  runtime behavior.
- platform projections are not canonical sources.

In target architecture:

- author in `skills/`
- review canonical source in `skills/`
- project into `.<platform>/skills/...` only to satisfy platform/runtime needs

## Migration Boundary

This topic is a positioning freeze only.

This topic does:

- define current state clearly
- define target architecture clearly
- define future migration boundaries clearly
- freeze wording without performing active-path cutover

This topic does not:

- migrate `.github/skills/` into `skills/`
- delete `.github/skills/`
- add `.codex/` or `.claude/`
- change creator output paths
- change reviewer target paths
- change template scaffold paths
- add generator, renderer, or installer scripts
- add `blueprints/`, `internalized/`, or `agent-runtime/`
- declare `skills/` as already active today

Transition wording for this topic is:

- `skills/` is the intended canonical skill source in target architecture only.
- `.github/skills/` remains the current Copilot active authored/reviewed
  workflow path during transition.
- `.github/skills/` should become a platform projection / compatibility mirror
  after a separate migration updates creator, reviewer, template,
  runtime/tooling, and installer assumptions.

## External Installer Boundary

This repository owns:

- governance rules
- repository positioning
- canonical skill-source direction
- projection boundary definitions

External installer repositories or tools own:

- fetch
- install
- sync
- deploy

## Future Migration Blockers

Future migration should audit, align, and then transition:

- `agent-skill-creator`
- `agent-skill-reviewer`
- `agent-skill-template`
- runtime/tooling path checks
- external installer assumptions
