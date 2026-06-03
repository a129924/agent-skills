# Observer / Dispatcher Canonical Baseline Technical Spec

## Baseline

- Topic: `observer-dispatcher-canonical-baseline`
- Input baseline: `analysis/observer-dispatcher-canonical-baseline/requirements.md`
- Repository baseline: `VERSION` = `0.69.1`
- Status: `FROZEN`

## Translation stance

This spec translates the frozen Feature 1 business baseline into an exact,
bounded repository change set. It assumes no runtime, launcher, installer, or
platform capability beyond storing repo-visible artifacts.

If implementation requires concrete agents, registry behavior, workflow binding,
runtime semantics, or paths outside the frozen write set, the correct behavior
is to stop and re-route the topic as out of scope rather than force a broader
design.

## Exact implementation write set

Feature 1 implementation may only create or modify these paths:

### Allowed to create

- `agents/observer-dispatcher.agent.md`
- `skills/subagent-dispatch-policy/SKILL.md`
- `skills/subagent-dispatch-policy/examples.md`
- `skills/context-package-builder/SKILL.md`
- `skills/context-package-builder/examples.md`
- `skills/handoff-routing-policy/SKILL.md`
- `skills/handoff-routing-policy/examples.md`

### Allowed to modify

- `AGENTS.md`
- `docs/repo-positioning.md`
- `.github/copilot-instructions.md`
- `README.md`

All other repository paths are out of scope for Feature 1 implementation.

## Requirement-to-artifact mapping

| Requirement | Required artifact(s) | Technical realization |
| --- | --- | --- |
| R1 Canonical source positioning | `AGENTS.md`, `docs/repo-positioning.md`, `.github/copilot-instructions.md`, `README.md` | Update authority-model wording so `skills/` remains primary while root `agents/` is introduced as canonical for workflow agent artifacts |
| R2 Observer scope stays bounded | `agents/observer-dispatcher.agent.md` | Create exactly one concrete workflow agent artifact and avoid broader taxonomy |
| R3 Observer responsibility boundary | `agents/observer-dispatcher.agent.md` | Define role identity, forbidden behavior, and routing-only responsibility |
| R4 Hard stop requirement | `agents/observer-dispatcher.agent.md`, `skills/subagent-dispatch-policy/SKILL.md`, `skills/handoff-routing-policy/SKILL.md` | Encode explicit stop conditions for no-real-dispatch and out-of-scope expansion |
| R5 Real dispatch definition | `agents/observer-dispatcher.agent.md` | Define minimum dispatch-separation conditions in contract language |
| R6 Fixed allowed values | `agents/observer-dispatcher.agent.md`, `skills/handoff-routing-policy/SKILL.md` | Freeze observer states and subAgent verdict enums in the written contract |
| R7 Role-only dispatch target rule | `agents/observer-dispatcher.agent.md`, `skills/subagent-dispatch-policy/SKILL.md` | Restrict all dispatch outputs to role names only |
| R8 Supporting-skill separation | `skills/subagent-dispatch-policy/SKILL.md`, `skills/context-package-builder/SKILL.md`, `skills/handoff-routing-policy/SKILL.md` | Give each skill one sharply bounded responsibility |
| R9 Minimal-context rule | `skills/context-package-builder/SKILL.md`, `skills/context-package-builder/examples.md` | Define the required context package shape plus forbidden context categories |
| R10 Existing workflow boundary | `agents/observer-dispatcher.agent.md`, `docs/repo-positioning.md`, `.github/copilot-instructions.md` | State that existing workflows are not encoded, and only topic-local step artifacts may be used as workflow-derived input |
| R11 `.codex/**` wording boundary | `AGENTS.md`, `docs/repo-positioning.md`, `.github/copilot-instructions.md`, `README.md` | Describe `.codex/**` only as repo-policy projection / compatibility surface wording |

## Artifact-level implementation contract

### 1. Repo truth documents

`AGENTS.md`, `docs/repo-positioning.md`, `.github/copilot-instructions.md`, and
`README.md` must be updated together so they do not drift.

They must align on these points:

- `skills/` remains the primary canonical skill source
- `agents/` is the canonical source for repo-defined workflow agent artifacts
- `.github/**`, `.codex/**`, and other `.<platform>/**` paths are projection /
  compatibility surfaces in repo policy
- the repository does not own runtime orchestration, agent loading / execution
  capability, install, sync, or deploy
- Observer mode is opt-in and bounded

### 2. Observer agent artifact

`agents/observer-dispatcher.agent.md` must define:

- role identity
- allowed responsibilities
- forbidden behavior
- hard stop rule
- real dispatch definition
- fixed observer state values
- fixed subAgent verdict values
- role-only dispatch rule
- concrete output templates for intake, status, handoff, result summary, and
  final report

It must not:

- create or imply a registry
- reference concrete role-agent files
- define launcher-specific behavior
- claim runtime dispatch support exists

### 3. Supporting skills

Each skill folder must contain:

- `SKILL.md`
- `examples.md`

The skills must remain separate:

- `subagent-dispatch-policy`
  - input: task state and evidence
  - output: next role or stop
- `context-package-builder`
  - input: one task slice and bounded evidence
  - output: one minimal context package
- `handoff-routing-policy`
  - input: one subAgent result
  - output: next role or stop

### 4. Examples as validation surfaces

`examples.md` files must include:

- at least one positive example that stays inside the contract
- at least one negative example that shows forbidden behavior
- explicit cases where missing real dispatch or out-of-scope runtime needs force
  a stop

## Feasibility and architecture compliance

### Feasibility

This topic is feasible within the repository because it only requires:

- documentation updates in existing truth surfaces
- one new root `agents/` artifact
- three new root `skills/` folders

No external runtime integration is required for Feature 1.

### Architecture compliance

The design is compliant only if:

- root `agents/` is introduced as a bounded canonical source for workflow-agent
  artifacts
- `skills/` remains the primary repository truth for reusable skill behavior
- platform-facing paths remain projection / compatibility surfaces in repo
  policy wording
- existing human-operated workflows are not encoded into the new baseline

## Rollback / stop triggers

Stop implementation and route back to planning if any of the following becomes
necessary:

- editing any file outside the frozen Feature 1 write set
- adding concrete Planner / Implementer / Reviewer / Correction Planner agent
  files
- adding an agent registry, catalog, or mapping table
- defining workflow-to-agent binding
- defining runtime semantics or launch behavior
- creating `.github/agents/**` or other compatibility mirrors not already
  listed in the write set
- using anything other than a topic-local step artifact as workflow-derived
  state

## Acceptance checks

Implementation passes this spec only if:

- every changed path is in the exact write set above
- repo truth documents agree on the same authority model
- the Observer contract includes fixed state and verdict sets
- dispatch outputs target roles only
- supporting skills do not overlap and do not encode registry behavior
- `.codex/**` appears only in repo-policy projection / compatibility wording
- no broader agent-system behavior appears anywhere in the write set
