# Workflow Artifact Standardization Plan

## Goal / Outcome

Freeze a repo-visible execution contract for the `workflow-artifact-standardization`
topic so later work can standardize repo-level workflow artifacts without relying
on chat memory, then apply the bounded shared workflow-contract update after
explicit human permission. The current outcome is a review-ready shared-contract
patch set plus the planning spine that authorized it.

## Scope

- In scope for this phase:
  - create the topic worktree planning artifacts
  - freeze the repo-level artifact baseline for `step.md`
  - freeze the repo-level artifact baseline for topic-close `summary artifact`
  - freeze progression and close gate semantics
  - record the workflow/migration worktree split and its authority boundary
  - after explicit human permission, update the bounded shared workflow
    governance surface for this topic
- Out of scope for this phase:
  - applying the new artifact rules to other topics
  - moving or editing skill folders
  - publish, PR, merge, or release execution for this topic

## Locked Decisions

- Topic name is `workflow-artifact-standardization`.
- Repo-root `dev` remains clean; repo-visible writes occur only in the topic worktree.
- The workflow and migration lines use separate worktrees and separate branches.
- The workflow worktree owns workflow spec and process-doc changes; the migration
  worktree only performs inventory, candidate sequencing, and bounded planning
  until the workflow baseline is authorized.
- The first batch in this worktree must materialize:
  - `analysis/workflow-artifact-standardization/requirements.md`
  - `plan/workflow-artifact-standardization/workflow-artifact-standardization.plan.md`
  - `plan/workflow-artifact-standardization/workflow-artifact-standardization.step.md`
- `step.md` is conditionally required when a topic has either:
  - two or more workflow-role handoffs
  - `required follow-up`
- Missing required `step.md` blocks workflow progression.
- Repo-level `step.md` minimum structure is:
  - `Workflow Stages`
  - `Actionable Steps`
  - `Handoff / Gate Notes`
- `Workflow Stages` is semantically aligned to repo-level workflow and uses the
  minimum stage set:
  - `plan`
  - `branch-ready`
  - `creator`
  - `review`
  - `publish`
  - `pr-open`
  - `merged`
  - `released`
- `Actionable Steps` is grouped by workflow stage.
- `summary artifact` is conditionally required when a topic has either:
  - topic-close handoff
  - `required follow-up`
- Missing required `summary artifact` blocks topic close.
- `summary artifact` minimum sections are:
  - `current state`
  - `completed`
  - `not completed`
  - `required follow-up`
  - `next handoff`
- `next handoff` minimum content is:
  - `next actor`
  - `next step`
- `required follow-up` allows explicit close-with-follow-up.
- `summary artifact` is the source of truth for close/handoff semantics; `step.md`
  only reflects progression status.
- Shared-contract file edits require explicit human permission before creator
  implementation begins.
- Human permission was later granted for this run, authorizing bounded edits to:
  - `plan/agent-handoff-workflow.md`
  - `docs/process/workflows/topic-bootstrap.workflow.md`
  - `docs/process/workflows/migration-implementation.workflow.md`
  - `docs/process/workflows/migration-publish-handoff.workflow.md`
  - `docs/process/workflows/release-cleanup.workflow.md`

## Boundaries / Exclusions

- Shared workflow governance edits stay bounded to:
  - `plan/agent-handoff-workflow.md`
  - `docs/process/workflows/topic-bootstrap.workflow.md`
  - `docs/process/workflows/migration-implementation.workflow.md`
  - `docs/process/workflows/migration-publish-handoff.workflow.md`
  - `docs/process/workflows/release-cleanup.workflow.md`
- Do not widen this topic to any other governance surface unless the plan is
  revised first.
- Do not create a separate testcase artifact in this first planning batch.
- Do not let this topic absorb migration sequencing execution or skill-move work.

## Status / Allowed Transitions

- Current status: `review-ready`
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
  - planning artifacts are materialized
  - bounded creator-stage shared-contract implementation is complete
  - the topic is now waiting for independent review before any publish
    progression

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Requirements baseline | `analysis/workflow-artifact-standardization/requirements.md` | Planning actor | Frozen business baseline for this topic |
| Topic plan | `plan/workflow-artifact-standardization/workflow-artifact-standardization.plan.md` | Planning actor | Repo-visible execution contract |
| Topic step tracker | `plan/workflow-artifact-standardization/workflow-artifact-standardization.step.md` | Planning actor | Workflow progression checklist for this topic |
| Repo workflow spec candidate | `plan/agent-handoff-workflow.md` | Creator in this topic | Shared contract update within bounded governance scope |
| Process workflow candidate | `docs/process/workflows/topic-bootstrap.workflow.md` | Creator in this topic | Shared contract update within bounded governance scope |
| Process workflow candidate | `docs/process/workflows/migration-implementation.workflow.md` | Creator in this topic | Shared contract update within bounded governance scope |
| Process workflow candidate | `docs/process/workflows/migration-publish-handoff.workflow.md` | Creator in this topic | Shared contract update within bounded governance scope |
| Process workflow candidate | `docs/process/workflows/release-cleanup.workflow.md` | Creator in this topic | Shared contract update within bounded governance scope |

## Implementation Steps

1. Materialize the worktree-local planning artifacts for this topic.
2. Stop and wait for explicit human permission before any shared-contract edits.
3. After permission, translate the frozen requirements baseline into the exact
   shared-doc patch set required for implementation.
4. Update the approved shared workflow-contract files within the bounded file set only.
5. Validate that:
   - `step.md` rules are represented as progression gates
   - `summary artifact` rules are represented as close gates
   - `explicit close with follow-up` is distinguishable from fully done
6. Route through independent review before any publish progression.

## Validation / Acceptance Checks

- The three planning artifacts exist in the topic worktree.
- `requirements.md` freezes the `step.md` and `summary artifact` baseline clearly enough for later implementation.
- `plan.md` records that shared workflow-contract edits stayed blocked until
  human permission was granted.
- `step.md` expresses stage-based progression and the creator-to-review handoff
  state correctly.
- Shared workflow spec and process-doc modifications remain bounded to the five
  approved governance files.

## Reviewer Handoff

```json
{
  "verdict": "approved|needs-rework",
  "blocking_issues": [],
  "notes": [
    "Check that the planning artifacts freeze gate semantics without already mutating shared workflow contracts.",
    "Check that the workflow/migration worktree split is explicit and bounded."
  ]
}
```

## Post-merge / Release Actions

- No release action is declared in this topic.
- After merge, run normal post-merge sync only if this topic later reaches merge.
- Any later shared-contract publication still requires review completion and the
  normal publish progression gates.

## Open Questions / Unresolved Items

- Whether `docs/process/policies/migration-workflow-common-policy.md` also
  requires updates remains intentionally unresolved and out of scope for this
  bounded topic revision.
