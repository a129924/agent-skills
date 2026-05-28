# Agent Skill Migration Sequencing Plan

## Goal / Outcome

Freeze a repo-visible execution contract for the `agent-skill-migration-sequencing`
topic so later migration planning can classify and order candidates without
depending on chat memory or prematurely editing shared workflow governance.

## Scope

- In scope for this phase:
  - use the committed planning baseline as the only writable topic spine
  - inventory migration candidates at `topic / candidate` granularity
  - freeze the migration sequencing view and gap classes
  - freeze the dependency boundary on the workflow baseline topic
  - verify the actual execution flow before the second topic commit
  - revise the topic contract so topic-local publish handoff becomes in scope
  - materialize topic-local publish handoff artifacts through `STOP POINT 1`
- Out of scope for this phase:
  - skill folder migration or copying
  - workflow governance edits
  - implementation of any candidate move topic
  - commit, push, or PR progression for this topic

## Locked Decisions

- Topic name is `agent-skill-migration-sequencing`.
- Repo-root `dev` remains clean; repo-visible writes occur only in the topic worktree.
- The first batch in this worktree must materialize:
  - `analysis/agent-skill-migration-sequencing/requirements.md`
  - `plan/agent-skill-migration-sequencing/agent-skill-migration-sequencing.plan.md`
  - `plan/agent-skill-migration-sequencing/agent-skill-migration-sequencing.step.md`
- Candidate sequencing uses `topic / candidate` granularity.
- The primary migration planning view is:
  - `can_start_now`
  - `after-workflow-baseline`
  - `shared-governance-blocked`
- Artifact gaps are first-pass classification signals:
  - `bootstrap-artifact-gap`
  - `step-gap`
  - `summary-gap`
  - `close-semantics-gap`
  - `shared-governance-gap`
  - `sequencing-gap`
- This worktree may use shared workflow files as read-only evidence only.
- No skill-move execution is authorized until explicit human permission.
- Topic-local publish handoff is governed by `plan/agent-handoff-workflow.md`.
- `docs/process/workflows/migration-implementation.workflow.md` and
  `docs/process/workflows/migration-publish-handoff.workflow.md` are reference
  shapes only for this topic, not executable workflow contracts.
- Because no repo-visible `migration-implementation` run exists for this topic,
  publish handoff must remain topic-local and stop at `STOP POINT 1`.

## Boundaries / Exclusions

- Do not modify:
  - `plan/agent-handoff-workflow.md`
  - `docs/process/workflows/topic-bootstrap.workflow.md`
  - `docs/process/workflows/migration-implementation.workflow.md`
  - `docs/process/workflows/migration-publish-handoff.workflow.md`
  - `docs/process/workflows/release-cleanup.workflow.md`
- Do not create or edit skill folders in this phase.
- Do not assume the workflow baseline topic has already been implemented.

## Status / Allowed Transitions

- Current status: `publish-in-progress`
- Allowed transitions:
  - `planned` -> `creator-in-progress`
  - `creator-in-progress` -> `review-ready`
  - `review-ready` -> `reviewer-in-progress`
  - `reviewer-in-progress` -> `approved`
  - `reviewer-in-progress` -> `needs-rework`
  - `needs-rework` -> `creator-in-progress`
  - `approved` -> `publish-in-progress`
  - `publish-in-progress` -> `pr-open`
  - `pr-open` -> `merged`
  - `merged` -> `released`
- Phase note:
- first topic commit already materialized the planning baseline as commit `26a4b16`
- sequencing, flow verification, and independent reviewer approval are complete
- planner alignment and topic-local publish handoff are complete
- the topic is now stopped at topic-local `STOP POINT 1` within
  `publish-in-progress`
- commit / push / PR progression remains intentionally unstarted until a later
  explicit human approval passes topic-local `STOP POINT 1`

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Requirements baseline | `analysis/agent-skill-migration-sequencing/requirements.md` | Planning actor | Frozen business baseline for migration sequencing |
| Topic plan | `plan/agent-skill-migration-sequencing/agent-skill-migration-sequencing.plan.md` | Planning actor | Repo-visible execution contract |
| Topic step tracker | `plan/agent-skill-migration-sequencing/agent-skill-migration-sequencing.step.md` | Planning actor | Workflow progression checklist for this topic |
| Sequencing result | `plan/agent-skill-migration-sequencing/agent-skill-migration-sequencing.sequencing.md` | Implementer subAgent | Repo-visible candidate ordering, exclusions, and flow-verification result |
| Publish alignment record | `plan/agent-skill-migration-sequencing/agent-skill-migration-sequencing.publish-alignment.md` | Main Agent | Topic-local planner/publish alignment and workflow-basis record |
| Publish readiness record | `plan/agent-skill-migration-sequencing/agent-skill-migration-sequencing.publish-readiness.md` | Implementer subAgent | Frozen topic-local publish-ready artifact set for the later single-topic commit |
| STOP POINT 1 record | `plan/agent-skill-migration-sequencing/agent-skill-migration-sequencing.stop-point-1.md` | Main Agent | Explicit topic-local authorization gate that keeps commit / push / PR blocked |
| Workflow baseline dependency | `analysis/workflow-artifact-standardization/requirements.md` | Upstream topic | Read-only upstream dependency once available |
| Workflow governance surface | `plan/agent-handoff-workflow.md` | Shared governance | Read-only evidence in this phase |
| Workflow governance surface | `docs/process/workflows/topic-bootstrap.workflow.md` | Shared governance | Read-only evidence in this phase |
| Workflow governance surface | `docs/process/workflows/migration-implementation.workflow.md` | Shared governance | Read-only evidence in this phase |
| Workflow governance surface | `docs/process/workflows/migration-publish-handoff.workflow.md` | Shared governance | Read-only evidence in this phase |
| Workflow governance surface | `docs/process/workflows/release-cleanup.workflow.md` | Shared governance | Read-only evidence in this phase |

## Implementation Steps

1. Keep the first topic commit (`26a4b16`) as the fixed planning baseline for this topic.
2. Inventory migration candidates from existing repo-visible planning and migration artifacts only.
3. Classify each candidate into:
   - `can_start_now`
   - `after-workflow-baseline`
   - `shared-governance-blocked`
4. Record applicable gap classes for each candidate, using only:
   - `bootstrap-artifact-gap`
   - `step-gap`
   - `summary-gap`
   - `close-semantics-gap`
   - `shared-governance-gap`
   - `sequencing-gap`
5. Materialize `agent-skill-migration-sequencing.sequencing.md` with:
   - next-wave queue rows
   - excluded existing topic/results
   - explicit evidence basis
   - flow-verification results
6. Update `agent-skill-migration-sequencing.step.md` so creator and reviewer work are complete and the topic stops at `approved` before publish.
7. Revise this topic plan so topic-local publish handoff through `STOP POINT 1`
   is explicitly in scope and the new publish artifacts are part of the
   contract.
8. Materialize these topic-local publish artifacts:
   - `agent-skill-migration-sequencing.publish-alignment.md`
   - `agent-skill-migration-sequencing.publish-readiness.md`
   - `agent-skill-migration-sequencing.stop-point-1.md`
9. Run independent reviewer confirmation on the publish artifacts and update
   `agent-skill-migration-sequencing.step.md` to `publish-in-progress` only
   after reviewer approval is recorded.
10. Leave the later single-topic commit, push, and PR work for a future explicit
    human approval after `STOP POINT 1`; do not publish, move skills, or enter
    PR flow here.

## Validation / Acceptance Checks

- The three planning-baseline artifacts remain committed in `26a4b16`.
- `agent-skill-migration-sequencing.sequencing.md` contains only `topic / candidate` rows and does not mix in completed results as queue items.
- Candidates depending on workflow-baseline semantics are explicitly labeled `after-workflow-baseline`.
- Candidates needing repo-wide workflow / governance alignment remain `shared-governance-blocked`.
- the topic plan no longer leaves publish handoff out of scope
- `Artifact Paths` lists the three topic-local publish artifacts explicitly
- `agent-skill-migration-sequencing.publish-alignment.md` explains why
  topic-local publish is valid despite no repo-visible `migration-implementation`
  run
- `agent-skill-migration-sequencing.publish-readiness.md` freezes the exact
  topic-local artifact set and excludes non-topic surfaces
- `agent-skill-migration-sequencing.stop-point-1.md` states that commit / push /
  PR remain unauthorized
- `step.md` shows creator completion, flow verification completion, reviewer
  approval of publish artifacts, and `publish-in-progress` with `STOP POINT 1`
  still pending
- No skill folder or shared governance file is modified during this phase.

## Reviewer Handoff

```json
{
  "verdict": "approved|needs-rework",
  "blocking_issues": [],
  "notes": [
    "Check that the migration planning baseline is scheduling-oriented rather than generic inventory only.",
    "Check that shared workflow governance remains read-only and separate from this topic."
  ]
}
```

## Post-merge / Release Actions

- No release action is declared in this sequencing-only phase.
- The next bounded end state for this topic is `publish-in-progress` with
  topic-local `STOP POINT 1` pending.
- Any later commit, push, or PR action requires a separate explicit human
  approval message that authorizes topic-local commit / push / PR for
  `agent-skill-migration-sequencing`.
- Any later migration execution still requires a separate explicit human resume
  and a separate topic contract.

## Open Questions / Unresolved Items

- None for the creator-stage sequencing result.
- Candidate execution remains intentionally deferred to later topics.
