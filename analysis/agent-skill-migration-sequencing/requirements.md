# Requirements: agent-skill-migration-sequencing

**Status**: FROZEN — planning baseline ready; migration execution blocked pending explicit human permission
**Topic**: `agent-skill-migration-sequencing`
**Date**: 2026-05-27

---

## Problem Statement

The repository has a large set of migration candidates, but the next safe move
sequence is unclear because candidate readiness is mixed with workflow-contract
uncertainty.

The missing contract is not the migration implementation itself. The missing
contract is a repo-visible sequencing baseline that:

- classifies candidates at `topic / candidate` granularity
- prioritizes artifact gaps first
- separates work that can start now from work that depends on the workflow baseline
- prevents the migration worktree from silently editing shared workflow governance

## Actors

| Actor | Role |
| --- | --- |
| Migration planning actor | Builds the candidate sequencing baseline |
| Workflow baseline topic | Upstream dependency that freezes workflow artifact rules |
| Main Agent | Orchestrates the migration worktree and later sequencing execution |
| Human operator | Grants explicit permission before migration planning deepens or skill moves begin |

## Frozen Requirements

### R1 — Worktree-first planning materialization

When this topic starts, repo-visible writes for this topic MUST occur only in
the dedicated migration worktree, not on repo-root `dev`.

- Actor: Main Agent
- Condition: topic bootstrap begins
- Observable: `analysis/agent-skill-migration-sequencing/requirements.md`,
  `plan/agent-skill-migration-sequencing/agent-skill-migration-sequencing.plan.md`,
  and `plan/agent-skill-migration-sequencing/agent-skill-migration-sequencing.step.md`
  are created in the topic worktree
- Acceptance: repo-root `dev` remains clean while the migration planning artifacts live in the worktree
- Failure meaning: migration sequencing intent remains chat-only or contaminates the wrong branch

### R2 — Candidate inventory must use topic / candidate granularity

The first executable migration sequencing view MUST treat each row as one topic
or candidate, not as a generic skill family or an abstract gap class.

- Actor: migration planning actor
- Condition: candidate sequencing begins
- Observable: each row can be scheduled, deferred, or blocked independently
- Acceptance: the inventory can directly support worktree assignment and topic ordering
- Failure meaning: candidate readiness remains too broad to use operationally

### R3 — Main sequencing view is `can_start_now`

The migration baseline MUST classify candidates first by whether they can start now.

The primary states are:

- `can_start_now`
- `after-workflow-baseline`
- `shared-governance-blocked`

- Actor: migration planning actor
- Condition: first-pass sequencing view is produced
- Observable: another agent can sort work by startability before reading gap details
- Acceptance: the sequencing view supports direct scheduling rather than descriptive inventory only
- Failure meaning: migration work still needs hidden reasoning before sequencing decisions can be made

### R4 — Artifact gaps are first-pass migration blockers

The migration baseline MUST treat these artifact-related gaps as first-pass
classification signals:

- `bootstrap-artifact-gap`
- `step-gap`
- `summary-gap`
- `close-semantics-gap`
- `shared-governance-gap`
- `sequencing-gap`

Artifact gaps are the first priority, ahead of deeper design debates, because
they determine whether a candidate has enough repo-visible contract to be routed safely.

- Actor: migration planning actor
- Condition: first-pass gap classification runs
- Observable: candidates can be grouped by artifact readiness before move implementation starts
- Acceptance: missing planning spine and missing handoff artifacts are visible and actionable
- Failure meaning: move sequencing starts on candidates whose execution contract is still invisible

### R5 — Workflow baseline dependency must stay explicit

Candidates whose reasonable execution depends on the not-yet-authorized workflow
artifact baseline MUST be classified as `after-workflow-baseline`, not silently
treated as ready.

- Actor: migration planning actor
- Condition: a candidate needs the finalized repo-level `step.md`, `summary artifact`, or close semantics rules
- Observable: the candidate is deferred explicitly because of workflow baseline dependency
- Acceptance: migration planning does not assume workflow baseline implementation that does not yet exist
- Failure meaning: migration work begins on false assumptions and later needs resequencing

### R6 — Shared workflow governance surfaces remain out of scope

The migration worktree MUST NOT modify shared workflow governance surfaces in
its planning-first phase.

Protected surfaces include:

- `plan/agent-handoff-workflow.md`
- `docs/process/workflows/topic-bootstrap.workflow.md`
- `docs/process/workflows/migration-implementation.workflow.md`
- `docs/process/workflows/migration-publish-handoff.workflow.md`
- `docs/process/workflows/release-cleanup.workflow.md`

- Actor: Main Agent / migration planning actor
- Condition: sequencing work is underway
- Observable: migration planning may refer to these files as read-only evidence, but does not edit them
- Acceptance: workflow and migration authority remain separated
- Failure meaning: the migration topic expands into workflow governance repair

## Non-goals

- Do not move or rewrite any skill folder in this phase.
- Do not modify shared workflow governance files in this phase.
- Do not assume the workflow artifact baseline is already implemented.
- Do not create a separate testcase artifact in this first planning batch.

## Resolved Contradictions

### C1 — sequencing by skill family vs sequencing by topic

- Conflict: skill-family grouping is simpler, but it is not operational for worktree routing
- Resolution: use topic / candidate granularity

### C2 — gap inventory vs actionable schedule

- Conflict: pure gap-class inventory is easier to compile, but it does not answer what can start now
- Resolution: use `can_start_now` as the primary view and keep gap classes as supporting detail

### C3 — migration planning vs workflow governance edits

- Conflict: some candidates clearly depend on workflow contract changes
- Resolution: keep those candidates visible but classify them as `after-workflow-baseline` or `shared-governance-blocked`

## Explicit Assumptions

- A1: the workflow baseline topic will be maintained as a separate worktree and separate branch
- A2: human permission for migration deepening or skill moves will be granted later, not in this planning batch
- A3: existing candidate lists and prior inventory discussions can be used as read-only evidence when sequencing resumes

## Success Signals

This topic is ready to move past planning when:

1. the worktree contains the three planning artifacts for this topic
2. the sequencing baseline is frozen at topic / candidate granularity
3. `can_start_now` is the primary scheduling view
4. workflow-baseline dependency is explicit rather than implicit
5. no shared workflow governance file is modified in this phase
