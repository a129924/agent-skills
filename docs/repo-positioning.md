# Repository Positioning

`agent-skills` is the repository for defining, collecting, and governing Agent
Skills plus bounded repo-defined workflow agent artifacts and the installable
layouts that external tooling or platform adapters consume.

It owns repository positioning, governance rules, and skill-source boundaries.
It does not own agent loading or execution capability, runtime orchestration,
fetch, install, sync, or deploy orchestration.

## Current Authority Model

The repository's current authority model is:

- `AGENTS.md` is the governance canonical source.
- `skills/` is the primary canonical skill source and repository truth for
  reusable skill behavior.
- `agents/` is the canonical source for repo-defined workflow agent artifacts.
- `docs/repo-positioning.md` defines repository positioning and boundary
  language.
- `.github/copilot-instructions.md` is GitHub/Copilot compatibility guidance
  and defers authority to `AGENTS.md` and this document.
- `.github/**`, `.codex/**`, and other `.<platform>/**` layouts are
  compatibility or projection surfaces, not source of truth.
- external installer tooling or repositories may consume platform-facing
  layouts, but install orchestration stays outside this repository.

Historical migration artifacts may describe older transition states or
platform-specific constraints. Those artifacts remain historical context only
and do not override the current authority model above.

## Compatibility and Projection Surfaces

Platform-facing layouts may exist because a specific tool or workflow expects a
particular path shape.

Those surfaces are bounded as follows:

- they provide compatibility, projection, or platform-specific entrypoints
- they do not own repository truth
- their presence does not declare current authoring or review authority
- any change to how they are generated, synchronized, or consumed is separate
  work from this positioning topic

This includes `.github/skills/**`, `.github/agents/**`, `.codex/skills/**`,
and other `.<platform>/**` projections.

## Workflow Agent Boundary

The repository now allows one bounded workflow-agent truth surface under
`agents/`.

That boundary means:

- `agents/` may store repo-defined workflow agent artifacts
- `agents/` does not imply runtime dispatch, agent registry, catalog ownership,
  launcher wiring, or execution support
- the Observer / Dispatcher baseline is routing-only and opt-in
- existing human-operated workflows are not encoded into this baseline
- if workflow-derived state is needed, the only allowed input is a topic-local
  progression artifact such as `plan/<topic>/<topic>.step.md`
- a topic-local progression artifact is evidence only, not a full workflow
  reconstruction source

## Target Architecture Direction

The current authority model already treats `skills/` as canonical truth for
reusable skill behavior and `agents/` as canonical truth for repo-defined
workflow agent artifacts. Separate follow-up work may still align older
contract surfaces, workflow assumptions, or projection mechanisms around that
current truth.

That future alignment may include:

- creator, reviewer, and template contract updates
- workflow agent contract updates under `agents/` when separately scoped
- runtime or tooling path-check alignment
- installer or projection automation alignment
- reduction or simplification of compatibility-only surfaces once consumers no
  longer depend on them

This document does not declare that broader alignment complete.

## Migration Boundary

This topic is a positioning correction only.

This topic does:

- restate one current authority model
- add `agents/` as a bounded canonical source for repo-defined workflow agent
  artifacts
- define compatibility and projection surfaces as non-canonical
- keep historical migration context subordinate to current truth
- preserve a clear boundary around later contract, workflow, and tooling work

This topic does not:

- rewrite `.github/skills/**`, `.codex/skills/**`, or `skills/**`
- define workflow-to-agent binding or runtime dispatch semantics
- delete compatibility surfaces
- change creator output paths
- change reviewer target paths
- change template scaffold paths
- change runtime/tooling/install/sync/projection automation
- declare broader skill-path migration complete

## External Installer Boundary

This repository owns:

- governance rules
- repository positioning
- canonical skill-source definition
- canonical workflow-agent definition for repo-defined artifacts under `agents/`
- projection boundary definitions

External installer repositories or tools own:

- runtime loading or execution
- fetch
- install
- sync
- deploy

## Future Alignment Dependencies

Future alignment should audit, align, and then transition:

- `agent-skill-creator`
- `agent-skill-reviewer`
- `agent-skill-template`
- runtime/tooling path checks
- external installer assumptions
- any platform-specific projection automation
