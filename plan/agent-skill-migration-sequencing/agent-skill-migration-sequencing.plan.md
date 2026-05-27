# Agent Skill Migration Sequencing Plan

## Goal / Outcome

Freeze a repo-visible execution contract for the `agent-skill-migration-sequencing`
topic so later migration planning can classify and order candidates without
depending on chat memory or prematurely editing shared workflow governance.

## Scope

- In scope for this phase:
  - create the topic worktree planning artifacts
  - freeze the migration sequencing view and gap classes
  - freeze the dependency boundary on the workflow baseline topic
  - freeze the rule that this worktree stays planning-only until explicit human permission
- Out of scope for this phase:
  - skill folder migration or copying
  - workflow governance edits
  - implementation of any candidate move topic

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

- Current status: `planned`
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
  - this worktree stops after planning artifacts are materialized and before any migration planning deepens into move execution

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Requirements baseline | `analysis/agent-skill-migration-sequencing/requirements.md` | Planning actor | Frozen business baseline for migration sequencing |
| Topic plan | `plan/agent-skill-migration-sequencing/agent-skill-migration-sequencing.plan.md` | Planning actor | Repo-visible execution contract |
| Topic step tracker | `plan/agent-skill-migration-sequencing/agent-skill-migration-sequencing.step.md` | Planning actor | Workflow progression checklist for this topic |
| Workflow baseline dependency | `analysis/workflow-artifact-standardization/requirements.md` | Upstream topic | Read-only upstream dependency once available |
| Workflow governance surface | `plan/agent-handoff-workflow.md` | Shared governance | Read-only evidence in this phase |
| Workflow governance surface | `docs/process/workflows/topic-bootstrap.workflow.md` | Shared governance | Read-only evidence in this phase |
| Workflow governance surface | `docs/process/workflows/migration-implementation.workflow.md` | Shared governance | Read-only evidence in this phase |
| Workflow governance surface | `docs/process/workflows/migration-publish-handoff.workflow.md` | Shared governance | Read-only evidence in this phase |
| Workflow governance surface | `docs/process/workflows/release-cleanup.workflow.md` | Shared governance | Read-only evidence in this phase |

## Implementation Steps

1. Materialize the worktree-local planning artifacts for this topic.
2. Stop and wait for explicit human permission before candidate sequencing deepens.
3. After permission, inventory migration candidates at `topic / candidate` granularity.
4. Classify each candidate into:
   - `can_start_now`
   - `after-workflow-baseline`
   - `shared-governance-blocked`
5. Record applicable gap classes for each candidate.
6. Produce a bounded next-wave sequence without modifying shared governance files or moving skill folders.

## Validation / Acceptance Checks

- The three planning artifacts exist in the topic worktree.
- `requirements.md` freezes the candidate-view and gap-class decisions clearly enough for later sequencing work.
- `plan.md` keeps migration execution and shared-governance edits blocked until human permission.
- `step.md` expresses the wait-for-permission stop point and the later sequencing progression path.
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

- No release action is declared in this planning-only phase.
- After merge, run normal post-merge sync only if this topic later reaches merge.
- Any later migration execution still requires a separate explicit human resume.

## Open Questions / Unresolved Items

- The exact first candidate set to classify after permission is intentionally left for the next phase.
- Whether migration planning will need additional repo-visible inventory artifacts beyond this planning spine remains unresolved in this phase.

