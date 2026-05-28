# python-helper-skill-promotion-wave-2 requirements baseline

Status: LOCKED
Topic: `python-helper-skill-promotion-wave-2`
Topic type: `selective promotion topic`
Base branch: `dev`
Target branch: `feat/andrew/python-helper-skill-promotion-wave-2`
Risk level: `medium`
Migration primitive: `folder-level direct copy`

## Problem statement

The repository already treats `skills/` as the intended canonical skill-source
direction and target architecture, but this topic does not authorize a repo-wide
path cutover.

What is missing is one bounded selective-promotion topic that creates
target-architecture copies for a locked wave of Python helper skills while
preserving `.github/skills/` as the current active authored/reviewed workflow
path during transition.

This topic must not widen into:

- repo-wide active-path cutover
- creator / reviewer / template contract-surface migration
- runtime/tooling blocker repair
- stable-library metadata or release actions
- governance or positioning rewrites

## Goal

Produce one bounded selective-promotion topic that:

- creates `skills/` target-architecture copies for exactly 18 locked Python
  helper skills
- preserves `.github/skills/` as the current active authored/reviewed workflow
  path during transition
- records the promotion result separately from any later active-path cutover,
  projection switch, or release work
- leaves a repo-visible promotion report that states what moved and what stayed
  deferred

## Frozen promotion set

Only these 18 skills are in scope:

- `python-api-signature`
- `python-async-await`
- `python-class-design`
- `python-comprehensions`
- `python-context-management`
- `python-control-flow`
- `python-data-model-methods`
- `python-decorators`
- `python-descriptors-attribute-access`
- `python-docstrings`
- `python-error-handling`
- `python-generators-iterators`
- `python-model-selection`
- `python-module-boundaries`
- `python-naming`
- `python-operator-overloading`
- `python-testing-pytest`
- `python-type-hints-strict`

No additional skill may be absorbed into this topic.

## Actors

- Human decision-maker
- Planning actor
- Creator / implementer
- Independent topic-plan reviewer
- Main Agent for later publish routing only

## Measurable requirements

| ID | Requirement | Observable result | Pass rule |
| --- | --- | --- | --- |
| R1 | The topic stays inside the locked 18-skill wave | Only the 18 listed `skills/<skill-name>/` folders are created as new target-architecture promotion results | No unlisted skill path is added or edited |
| R2 | Promotion remains separate from active-path cutover | The plan and final promotion report state that `skills/` gains target-architecture copies while `.github/skills/` remains the current active authored/reviewed workflow path | No artifact claims repo-wide cutover, retirement of `.github/skills/`, or dual canonical-source status |
| R3 | Promotion uses folder-level direct copy only | The promotion result for each in-scope skill is created from the corresponding `.github/skills/<skill-name>/` folder | No migration primitive other than folder-level direct copy is introduced |
| R4 | Shared governance and stable-library surfaces remain untouched | Bootstrap and implementation artifacts stay topic-local | No edit lands in `AGENTS.md`, `docs/repo-positioning.md`, `.github/copilot-instructions.md`, `README.md`, `VERSION`, or checklist-wide/shared governance files |
| R5 | Contract-surface and blocker lanes remain deferred | Creator / reviewer / template surfaces and runtime/tooling blocker surfaces stay out of scope | No edit lands in `agent-skill-creator`, `agent-skill-reviewer`, `agent-skill-template`, runtime/tooling blocker surfaces, or any unlisted skill |
| R6 | The topic leaves repo-visible promotion evidence | A migration report exists and states the locked promotion set, preserved active-path boundary, promotion result, and deferred follow-up lanes | Another agent can tell exactly what was promoted and what remains deferred |

## Locked decisions

- This is an implementation topic for selective promotion, not an inventory-only
  topic and not a repo-wide migration topic.
- The topic type is `selective promotion topic`.
- The migration primitive is `folder-level direct copy`.
- Only the locked 18-skill wave may be promoted in this branch.
- `.github/skills/` remains the current active authored/reviewed workflow path
  during transition in this topic.
- `skills/` is the target-architecture promotion result for the 18 in-scope
  skills only; this topic must not write `.github/skills/` and `skills/` as
  dual canonical sources.
- `skills/` may receive new target-architecture copies for the locked wave only.
- README / VERSION / release-tag handling is deferred to later work.
- Bootstrap worktree creation was already completed before this drafting round.
- This drafting round stops before commit and must not declare the workflow
  finished.

## Non-goals

- editing `AGENTS.md`
- editing `docs/repo-positioning.md`
- editing `.github/copilot-instructions.md`
- editing `README.md`
- editing `VERSION`
- moving `agent-skill-creator`, `agent-skill-reviewer`, or
  `agent-skill-template`
- repairing runtime/tooling blocker surfaces
- promoting any skill outside the locked 18-skill wave
- changing the current active path away from `.github/skills/`
- implementing projection switching, installer changes, or release work

## Assumptions and blockers

- `docs/repo-positioning.md` remains the authority for current-state vs
  target-architecture wording.
- `AGENTS.md` remains the governance canonical source.
- The current repository snapshot contains the 18 in-scope source folders only
  under `.github/skills/`; no matching `skills/<skill-name>/` target folders
  exist yet in this worktree.
- If promotion of any listed skill requires changes outside the exact artifact
  paths in the topic plan, the topic must stop and be re-planned instead of
  widening scope.
- The transition overlay path referenced by the workflow doc is not present in
  this worktree snapshot, so planning relies on the readable policy, workflow,
  repo-positioning, and handoff contracts already in-repo.
