# Observer / Dispatcher Canonical Baseline Requirements

## Baseline

- Topic: `observer-dispatcher-canonical-baseline`
- Repository baseline: `VERSION` = `0.69.1`
- Status: `FROZEN`

## Goal

Define one bounded Observer / Dispatcher baseline so this repository can state,
without ambiguity, that:

- `skills/` remains the primary canonical skill source
- `agents/` is the canonical source for repo-defined workflow agent artifacts
- `.github/**`, `.codex/**`, and other `.<platform>/**` paths are repo-policy
  projection / compatibility surfaces rather than canonical sources
- the Observer role is limited to observe, slice, dispatch, handoff, route, and
  report

## Actors

- Human operator: chooses when the Observer mode is invoked and approves later
  workflow progression
- Planning actor: freezes the bounded contract and exact artifact paths
- Creator / implementer: edits only the exact Feature 1 implementation write set
- Reviewer: checks that the implementation matches the bounded contract
- Observer / Dispatcher agent: coordinates role routing without doing concrete
  implementation or review work itself

## In-scope implementation result

Feature 1 is complete only when the implementation topic produces exactly these
repo-visible changes:

- create `agents/observer-dispatcher.agent.md`
- create `skills/subagent-dispatch-policy/SKILL.md`
- create `skills/subagent-dispatch-policy/examples.md`
- create `skills/context-package-builder/SKILL.md`
- create `skills/context-package-builder/examples.md`
- create `skills/handoff-routing-policy/SKILL.md`
- create `skills/handoff-routing-policy/examples.md`
- update `AGENTS.md`
- update `docs/repo-positioning.md`
- update `.github/copilot-instructions.md`
- update `README.md`

## Requirements

### R1. Canonical source positioning

The resulting repo truth must explicitly state:

- `AGENTS.md` remains the governance canonical source
- `skills/` remains the primary canonical skill source and repository truth for
  reusable skill behavior
- `agents/` is added as the canonical source for repo-defined workflow agent
  artifacts
- `.github/**`, `.codex/**`, and other `.<platform>/**` paths are described in
  repo policy as projection / compatibility surfaces only

### R2. Observer scope must stay bounded

The Observer / Dispatcher baseline must define only one concrete agent artifact:

- `agents/observer-dispatcher.agent.md`

It must not broaden into a multi-agent taxonomy.

### R3. Observer responsibility boundary

The Observer artifact must clearly state that it:

- is not Planner, Implementer, Reviewer, or Correction Planner
- only manages task flow, context flow, dispatch, handoff, routing, and status
  reporting
- must not implement code changes
- must not review code or plans directly
- must not fix, rewrite, or approve artifacts
- must not collapse multiple roles into itself
- must not simulate missing subAgent output

### R4. Hard stop requirement

The Observer artifact must contain a hard stop rule:

- if real subAgent dispatch separation cannot be established, it must stop
- if the task needs concrete agents, registry/catalog behavior,
  workflow-to-agent binding, or runtime semantics, it must stop and report that
  the request is out of scope for Feature 1

### R5. Real dispatch definition

The baseline must define real subAgent dispatch as requiring all of:

- a separated role instruction surface
- a separated task context package
- an explicit handoff payload
- an explicit result payload
- no hidden role simulation by the Observer

### R6. Fixed allowed values

The Observer contract must freeze these exact allowed values:

- Observer state values:
  - `INTAKE`
  - `DISPATCHED`
  - `WAITING`
  - `ROUTING`
  - `BLOCKED`
  - `COMPLETE`
- SubAgent verdict values:
  - `PASS`
  - `PATCH_REQUIRED`
  - `REPLAN_REQUIRED`
  - `MISSING_EVIDENCE`
  - `BLOCKED`

### R7. Role-only dispatch target rule

Observer dispatch outputs may only target these roles:

- `Planner`
- `Implementer`
- `Reviewer`
- `Correction Planner`

The baseline must prohibit dispatch to concrete files, paths, registry keys,
catalog entries, or launcher-specific names.

### R8. Supporting-skill separation

The three supporting skills must have non-overlapping responsibilities:

- `subagent-dispatch-policy`: choose the next role or stop
- `context-package-builder`: produce the minimal task-specific handoff context
- `handoff-routing-policy`: choose the next route after a subAgent result

### R9. Minimal-context rule

The context-packaging skill must explicitly forbid:

- whole conversation history
- unrelated prior decisions
- speculative reasoning
- multiple independent tasks
- unresolved roadmap material
- unnecessary platform-specific assumptions
- role-to-file lookup hints
- registry identifiers

### R10. Existing workflow boundary

The baseline must not encode, migrate, normalize, or bind existing
human-operated workflows.

If workflow execution state is needed, the only allowed workflow-derived input
is a topic-local progression artifact such as:

- `plan/<plan-topic-name>/<plan-topic-name>.step.md`

The Observer baseline must not depend on memorizing or reconstructing the full
workflow from that artifact.

### R11. `.codex/**` wording boundary

Any mention of `.codex/**` must be written as repository policy about projection
or compatibility surfaces. It must not be written as:

- a canonical source claim
- an external platform fact
- an official external authority model

## Out of scope

Feature 1 must not:

- create concrete Planner / Implementer / Reviewer / Correction Planner agent
  files
- create any agent registry, catalog, or mapping table
- define workflow-to-agent binding rules
- define runtime orchestration semantics
- create compatibility mirrors such as `.github/agents/**` unless a later topic
  explicitly requires them
- migrate or normalize existing human-operated workflow definitions
- update `VERSION`, create a release artifact, or claim a release action

## Acceptance signals

Feature 1 is acceptable only if all of the following are true:

- the implementation stays inside the exact in-scope write set
- `skills/` remains the primary canonical source in repo truth documents
- `agents/observer-dispatcher.agent.md` defines a bounded Observer contract
- the Observer contains the hard stop rule and real-dispatch definition
- the three supporting skills are separated cleanly and include `examples.md`
- `.codex/**` is described only as a repo-policy projection / compatibility
  surface
- no concrete agents, registry, workflow binding, or runtime semantics are
  introduced

## Non-goals

- making the Observer executable in every external runtime
- formalizing all repository workflows into the Observer baseline
- designing a broader agent system
- publishing a compatibility-mirror strategy for every platform path

## Resolved contradictions

- Root `agents/` is allowed as a new canonical source for workflow agent
  artifacts without changing the repository's primary content focus away from
  `skills/`
- Observer mode is allowed as a bounded workflow artifact without becoming a
  repo-wide always-on execution model
- `.codex/**` may be mentioned in policy language without being promoted to
  canonical truth
