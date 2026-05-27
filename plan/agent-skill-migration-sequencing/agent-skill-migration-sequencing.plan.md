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
- Out of scope for this phase:
  - skill folder migration or copying
  - workflow governance edits
  - implementation of any candidate move topic
  - publish / PR / merge progression for this topic

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

- Current status: `approved`
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
  - publish / PR / merge progression remains intentionally unstarted in this topic state

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Requirements baseline | `analysis/agent-skill-migration-sequencing/requirements.md` | Planning actor | Frozen business baseline for migration sequencing |
| Topic plan | `plan/agent-skill-migration-sequencing/agent-skill-migration-sequencing.plan.md` | Planning actor | Repo-visible execution contract |
| Topic step tracker | `plan/agent-skill-migration-sequencing/agent-skill-migration-sequencing.step.md` | Planning actor | Workflow progression checklist for this topic |
| Sequencing result | `plan/agent-skill-migration-sequencing/agent-skill-migration-sequencing.sequencing.md` | Implementer subAgent | Repo-visible candidate ordering, exclusions, and flow-verification result |
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
7. Leave the second topic commit for the Main Agent after approved review state is recorded; do not publish, move skills, or enter PR flow here.

## Validation / Acceptance Checks

- The three planning-baseline artifacts remain committed in `26a4b16`.
- `agent-skill-migration-sequencing.sequencing.md` contains only `topic / candidate` rows and does not mix in completed results as queue items.
- Candidates depending on workflow-baseline semantics are explicitly labeled `after-workflow-baseline`.
- Candidates needing repo-wide workflow / governance alignment remain `shared-governance-blocked`.
- `step.md` shows creator completion, flow verification completion, first topic commit completed, and second topic commit still pending Main Agent handling.
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
- The second topic commit is the last planned action for this phase and is owned by the Main Agent, not this Implementer subAgent.
- Any later migration execution still requires a separate explicit human resume and a separate topic contract.

## Open Questions / Unresolved Items

- None for the creator-stage sequencing result.
- Candidate execution remains intentionally deferred to later topics.
