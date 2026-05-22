# Workflow Recovery Alignment Plan

## Goal / Outcome

- Restore this workflow-recovery topic to a correct repo-visible execution
  contract before further bounded workflow-document implementation continues.
- Produce a bounded set of documentation changes that align the existing
  Markdown-first migration workflow files with the approved reviewer guidance
  and the repository's role / review discipline.

## Scope

- **In scope**:
  - `analysis/workflow-recovery-alignment/requirements.md`
  - `plan/workflow-recovery-alignment/workflow-recovery-alignment.plan.md`
  - `plan/workflow-recovery-alignment/workflow-recovery-alignment.review-log.md`
  - `docs/process/policies/migration-workflow-common-policy.md`
  - `docs/process/workflows/topic-bootstrap.workflow.md`
  - `docs/process/workflows/migration-implementation.workflow.md`
  - `docs/process/workflows/pr-comment-correction.workflow.md`
  - `docs/process/workflows/release-cleanup.workflow.md`

- **Out of scope**:
  - `docs/process/overlays/agent-skills-transition-overlay.md`
  - `.codex/skills/...`
  - executable runners
  - installer or platform adapter design
  - `README.md`
  - `VERSION`
  - broad workflow architecture redesign

## Locked Decisions

- This is a **workflow recovery and alignment topic**, not a new skill, release,
  or platform-adapter topic.
- The execution lane for this recovery remains
  **topic-bootstrap-like alignment work**.
- Repo-root `dev` must remain clean; ongoing recovery work stays in the
  dedicated worktree on branch `fix/andrew/workflow-recovery-alignment`.
- The implementation is limited to:
  1. repo-visible recovery planning artifacts
  2. bounded patches requested by reviewer guidance
  3. the optional `Role Execution Model` patch in common policy
  4. the optional common `status.json` extension rule in common policy
  5. the optional skipped-state precision patch in release cleanup
- Planning authority remains with the planning actor / planner. Main Agent is
  limited to orchestration, routing, and post-review progression, and must not
  self-approve plan or implementation gates.
- Review must stay independent and contract-focused rather than reopening broad
  design questions.
- This topic does not affect stable-library surfaces.

## Boundaries / Exclusions

- Do not modify `docs/process/overlays/agent-skills-transition-overlay.md`
  unless a direct contradiction is discovered later; none is currently declared.
- Do not add new workflow files beyond the existing set.
- Do not add `.codex/skills`, runner, installer, or platform adapter artifacts.
- Do not move work back to repo-root `dev`.
- Do not treat reviewer commentary as permission to rewrite the workflow system.

## Status / Allowed Transitions

- **Current**: `planned`
- **Execution model**: follow the canonical creator -> reviewer -> publish ->
  merge path; this topic stops before release and uses independent plan review
  plus independent implementation review.
- **Allowed transitions**:
  - `planned` -> `creator-in-progress`
  - `creator-in-progress` -> `review-ready`
  - `review-ready` -> `reviewer-in-progress`
  - `reviewer-in-progress` -> `approved`
  - `reviewer-in-progress` -> `needs-rework`
  - `needs-rework` -> `creator-in-progress`
  - `approved` -> `creator-in-progress`
  - `approved` -> `publish-in-progress`
  - `publish-in-progress` -> `pr-open`
  - `publish-in-progress` -> `merged`
  - `pr-open` -> `needs-rework`
  - `pr-open` -> `merged`
  - `merged` -> terminal

Routing notes:

- Plan review must pass before bounded implementation begins.
- Implementation review must pass before any publish or PR handling is
  considered.
- This topic uses standard reviewer reroute semantics and does not declare a
  release action.

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Requirements baseline | `analysis/workflow-recovery-alignment/requirements.md` | Planning actor | Repo-visible recovery intent and bounded requirements baseline |
| Topic plan | `plan/workflow-recovery-alignment/workflow-recovery-alignment.plan.md` | Planning actor | Repo-visible execution contract for this recovery topic |
| Review log | `plan/workflow-recovery-alignment/workflow-recovery-alignment.review-log.md` | Main Agent (maintains file); Reviewer (provides verdict) | Repo-visible trail for independent review verdicts and bounded reroute notes |
| Common policy | `docs/process/policies/migration-workflow-common-policy.md` | Creator / correction role | Optional bounded policy patch for role execution model |
| Topic bootstrap workflow | `docs/process/workflows/topic-bootstrap.workflow.md` | Creator / correction role | Workflow patch target for existing-valid-worktree reuse recording |
| Migration implementation workflow | `docs/process/workflows/migration-implementation.workflow.md` | Creator / correction role | Workflow patch target for overlay gate states and routing |
| PR comment correction workflow | `docs/process/workflows/pr-comment-correction.workflow.md` | Creator / correction role | Workflow patch target for no-correction routing states |
| Release cleanup workflow | `docs/process/workflows/release-cleanup.workflow.md` | Creator / correction role | Workflow patch target for conditional release actions |

Artifact path notes:

- `README.md`, `VERSION`, and `docs/process/overlays/agent-skills-transition-overlay.md`
  are intentionally outside this topic's editable artifact set.
- Listed paths are the executable contract. If later work drifts outside these
  paths, stop and repair the plan before continuing.
- This topic does not use a separate technical spec artifact; the requirements
  baseline is sufficient because the implementation is a bounded documentation
  repair.

## Implementation Steps

1. Author `analysis/workflow-recovery-alignment/requirements.md` as the
   recovery baseline.
2. Author and maintain this topic plan as the repo-visible execution contract.
3. Run independent plan review against this topic plan before further bounded
   documentation implementation.
4. Apply only the bounded workflow-document patches declared in this topic:
   - add `Role Execution Model` to common policy
   - add the common `status.json` extension rule to common policy
   - add overlay-gate state / step / stop hooks to migration implementation
   - add explicit no-correction routing to PR comment correction
    - mark release actions as conditional in release cleanup
   - add explicit skipped states for optional release follow-up actions in
     release cleanup
   - record existing valid worktree reuse in topic bootstrap
5. Record implementation review verdicts and reroute notes in the review log
   when review feedback affects routing.
6. Run independent implementation review focused on bounded patch completeness
   and layer separation.

## Validation / Acceptance Checks

- `analysis/workflow-recovery-alignment/requirements.md` exists and matches this
  topic plan's bounded scope.
- Plan review passes independently before bounded implementation begins.
- `migration-workflow-common-policy.md` explicitly states Planner authority and
  bounded role limits.
- `migration-workflow-common-policy.md` allows workflow-specific extra
  `status.json` fields without allowing removal or renaming of the common
  required fields.
- `migration-implementation.workflow.md` adds overlay gate states, routing step,
  and stop conditions without hardcoding repository-specific gate names.
- `pr-comment-correction.workflow.md` explicitly supports no-correction routing
  after planner triage.
- `release-cleanup.workflow.md` marks version/docs/tag actions as conditional
  and records skipped-vs-required behavior clearly, including explicit skipped
  states for optional release follow-up actions.
- `topic-bootstrap.workflow.md` records existing valid worktree reuse when no
  new worktree creation is required.
- Implementation review passes independently and no out-of-scope file edits are
  introduced.

## Reviewer Handoff

```json
{
  "verdict": "approved|needs-rework",
  "blocking_issues": [],
  "copilot_feedback_triage": {
    "ADDRESS": [],
    "DISCUSS": [],
    "SKIP": []
  }
}
```

## Post-merge / release actions

- After merge, keep repo-root `dev` clean and release the dedicated recovery
  worktree only through the normal worktree lifecycle path.
- No repository release action is required for this topic.
- This topic is terminal at `merged`.

## Open Questions / Unresolved Items

- None. The optional `Role Execution Model` patch is accepted into this topic
  rather than left ambiguous.
