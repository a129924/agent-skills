# Requirements: workflow-artifact-standardization

**Status**: FROZEN — planning baseline ready; shared-contract edits blocked pending explicit human permission
**Topic**: `workflow-artifact-standardization`
**Date**: 2026-05-27

---

## Problem Statement

The repository already has repo-visible plans, workflow specs, and review gates,
but it does not yet have one repo-level artifact contract that makes workflow
progression, topic close, and follow-up handoff consistently visible without
relying on chat memory.

The missing contract is:

- when `step.md` is required
- when a topic-close `summary artifact` is required
- what each artifact minimally contains
- which artifact blocks workflow progression versus topic close
- how `required follow-up` is declared without pretending a topic is fully done

## Actors

| Actor | Role |
| --- | --- |
| Planning actor | Freezes the workflow-artifact baseline in repo-visible artifacts |
| Creator / implementer | Applies later workflow-contract updates only after permission |
| Reviewer | Independently checks whether the later contract changes match the frozen baseline |
| Main Agent | Orchestrates worktree setup, planning artifacts, and later publish routing |
| Human operator | Grants the explicit permission required before shared workflow docs may be edited |

## Frozen Requirements

### R1 — Worktree-first planning materialization

When this topic starts, the repository root `dev` branch MUST remain clean, and
repo-visible artifact writes for this topic MUST occur only inside the dedicated
topic worktree.

- Actor: Main Agent
- Condition: topic bootstrap begins
- Observable: `analysis/workflow-artifact-standardization/requirements.md`,
  `plan/workflow-artifact-standardization/workflow-artifact-standardization.plan.md`,
  and `plan/workflow-artifact-standardization/workflow-artifact-standardization.step.md`
  are created in the topic worktree, not on repo-root `dev`
- Acceptance: repo-root `dev` stays clean while the worktree contains the topic artifacts
- Failure meaning: planning intent remains in chat or leaks onto the wrong branch

### R2 — `step.md` conditional requirement and gate role

`plan/<topic>/<topic>.step.md` MUST be treated as conditionally required at the
repo level whenever either of these is true:

1. the topic requires two or more workflow-role handoffs, or
2. the topic has `required follow-up`

If `step.md` is required and missing, workflow progression MUST stop until the
artifact is created.

- Actor: workflow participants using topic artifacts
- Condition: a topic meets either trigger above
- Observable: the topic contains a `step.md` artifact before it progresses
- Acceptance: missing required `step.md` blocks progression instead of being treated as optional
- Failure meaning: handoff state is invisible and later phases can advance without a repo-visible gate

### R3 — Repo-level `step.md` minimum contract

When a repo-level `step.md` exists, it MUST satisfy all of the following:

- `Workflow Stages` is present
- `Workflow Stages` is a workflow progression gate, not only a progress note
- `Workflow Stages` stays semantically aligned to the repo-level workflow in
  `plan/agent-handoff-workflow.md`
- the minimum stage set is:
  - `plan`
  - `branch-ready`
  - `creator`
  - `review`
  - `publish`
  - `pr-open`
  - `merged`
  - `released`
- `Actionable Steps` is present and grouped by workflow stage
- grouping is sufficient for the next role to find its own section without each
  line having an explicit owner tag
- `Handoff / Gate Notes` is present for stop-point, approval, resume, or gate-specific context

- Actor: planning actor / creator of the artifact
- Condition: producing repo-level `step.md`
- Observable: the file contains the three required sections and the minimum stage set
- Acceptance: another agent can determine both current phase readiness and stage-local next work without chat
- Failure meaning: the file becomes a generic checklist instead of a workflow progression artifact

### R4 — Topic-close `summary artifact` conditional requirement and gate role

A topic-close `summary artifact` MUST be treated as conditionally required
whenever either of these is true:

1. the topic has a topic-close handoff to another agent or human, or
2. the topic has `required follow-up`

If the `summary artifact` is required and missing, topic close MUST stop until
the artifact is created.

- Actor: topic owner at close time
- Condition: a topic meets either trigger above
- Observable: the topic has a close summary before being treated as closed
- Acceptance: missing required `summary artifact` blocks topic close
- Failure meaning: completion and handoff must be reconstructed from scattered notes or chat

### R5 — `summary artifact` minimum contract

When a repo-level `summary artifact` exists, it MUST contain these minimum sections:

- `current state`
- `completed`
- `not completed`
- `required follow-up`
- `next handoff`

The `next handoff` section MUST include:

- `next actor`
- `next step`

- Actor: topic owner at close time
- Condition: producing a required `summary artifact`
- Observable: the file contains the fixed sections and the handoff minimum
- Acceptance: the next human or agent can determine current topic outcome and immediate takeover action without reading chat
- Failure meaning: the summary becomes descriptive but not executable as a handoff artifact

### R6 — `required follow-up` close semantics

If a topic has `required follow-up`, the topic MAY still be closed, but only as
an explicit `close with follow-up`. It MUST NOT be represented as fully done.

The `summary artifact` is the source of truth for this close decision and for
the declared follow-up handoff. `step.md` may reflect later follow-up status,
but it does not define the close meaning.

- Actor: topic owner at close time
- Condition: topic completion leaves required follow-up
- Observable: close state is explicitly marked as close-with-follow-up in the summary
- Acceptance: the repository can distinguish fully closed work from work that is closed but still hands off required next work
- Failure meaning: follow-up work can be lost because the original topic looks fully complete

### R7 — Workflow and migration separation during planning phase

This topic's planning artifacts MUST support a two-worktree split:

- a workflow worktree that owns workflow spec and process doc updates
- a migration worktree that only performs inventory, candidate sequencing, and bounded planning until the workflow baseline is authorized

- Actor: Main Agent / planning actor
- Condition: both topics are bootstrapped in parallel
- Observable: workflow artifact decisions are frozen in this topic, while migration planning treats them as pending baseline rather than already implemented contract
- Acceptance: neither worktree silently redefines the other's authority
- Failure meaning: workflow and migration lines drift into one mixed topic and lose clear sequencing

## Non-goals

- Do not modify `plan/agent-handoff-workflow.md` in this planning-only phase
- Do not modify `docs/process/workflows/` in this planning-only phase
- Do not move or edit skill folders as part of this topic bootstrap
- Do not create a separate testcase artifact in the first planning batch
- Do not allow repo-root `dev` to become the working branch for this topic

## Resolved Contradictions

### C1 — `step.md` as checklist vs workflow progression artifact

- Conflict: a simple checklist is easier to write, but it cannot safely gate workflow progression
- Resolution: repo-level `step.md` is a workflow progression artifact with stage semantics, not only a checklist

### C2 — topic with `required follow-up` as done vs not done

- Conflict: required next work exists, but the repository still needs a usable close state
- Resolution: allow explicit close-with-follow-up; do not represent it as fully done

### C3 — `summary artifact` vs `step.md` as follow-up truth

- Conflict: both artifacts could describe unfinished downstream work
- Resolution: `summary artifact` owns close and handoff truth; `step.md` only reflects progression status

## Explicit Assumptions

- A1: human permission will later be given separately before shared workflow-contract files are edited
- A2: the workflow and migration topics will remain on separate worktrees and separate branches
- A3: repo-level artifact standardization can be planned before the exact shared-doc patch set is frozen

## Success Signals

This topic is ready to move past planning when:

1. the worktree contains the three planning artifacts for this topic
2. the baseline above is frozen in repo-visible form
3. later implementation work is clearly blocked pending explicit human permission
4. the migration topic can consume this baseline as an upstream dependency without assuming it is already implemented

