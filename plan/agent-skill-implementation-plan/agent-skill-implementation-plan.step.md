# Windows-to-WSL Development Command Skill Progression

## Workflow Stages

| Stage | Current state | Entry evidence | Required next gate | Next owner |
| --- | --- | --- | --- | --- |
| Plan amendment re-review | `review-ready` | The authorized bounded plan amendment and this topic-local progression artifact exist but are not committed. | Independent Plan-Reviewer returns the exact topic-plan JSON verdict with `approved`. | Plan-Reviewer |
| Plan amendment commit | `blocked` | Plan-Reviewer approval is not yet recorded. | Explicit human authorization for one amendment-only commit containing only this plan and this step artifact. | Main Agent |
| Feature worktree provisioning | `blocked` | The amendment-only commit has not been created. | Verify the committed plan and step artifact remain aligned, then create `feature/andrew/windows-wsl-dev` from that commit. | Main Agent |
| External implementation dispatch | `blocked` | No feature worktree has been verified. | Record `feature-worktree-ready` with verified branch, worktree path, and base commit, then obtain separate explicit human authorization for external user-profile writes. | Main Agent / Human |
| External user-profile implementation | `blocked` | The external-write authorization has not been given after worktree validation. | Independent Implementer returns `review-ready` evidence for only the user-profile targets in the topic plan. | Implementer |
| Independent implementation review | `blocked` | No `review-ready` implementation evidence exists. | Independent Reviewer returns `approved` or `needs-rework`; rework returns only to an independent Implementer. | Reviewer |
| Close and follow-up handoff | `blocked` | Independent implementation review has not completed. | Create or validate the listed summary artifact before any close or human/agent follow-up handoff. | Main Agent |

## Actionable Steps

1. Plan-Reviewer independently re-reviews the amended topic plan and this
   progression artifact against `AGENTS.md`,
   `plan/agent-handoff-workflow.md`, and `plan/topic-plan-contract.md`.
2. After an `approved` verdict, stop for a human amendment-only commit
   authorization; do not create a worktree, write the user profile, push, or
   open a PR before that authorization.
3. After the authorized commit succeeds, Main Agent validates that this exact
   committed artifact remains aligned with the plan, creates the approved
   feature branch and worktree from the commit, and records the verified
   branch, path, and base commit as `feature-worktree-ready`.
4. Stop for a separate explicit human authorization covering only the external
   user-profile writes. After that authorization, dispatch an independent
   Implementer in the verified feature worktree.
5. Route any implementation finding to an independent Reviewer; a
   `needs-rework` verdict returns only the bounded repair to an independent
   Implementer. Do not treat a reviewer result as topic close.

## Handoff / Gate Notes

- This is the minimal topic-local progression artifact required because this
  topic has multiple workflow-role handoffs. Plan-Creator created it from the
  topic plan; it is not generated through `step-creator`, does not select a
  reusable-Skill profile, and must not add or claim `skills/**` or a platform
  projection.
- Plan-Creator owns the initial contract and any plan-alignment amendment.
  Main Agent may update only current state, completed-gate evidence, and next
  handoff after the corresponding gate actually completes. Such an update may
  not change a locked decision, implementation scope, user-profile path, WSL
  routing, or security boundary.
- The plan amendment commit is limited to
  `plan/agent-skill-implementation-plan/agent-skill-implementation-plan.plan.md`
  and this artifact. It does not authorize external writes, push, PR creation,
  release work, or a status of `publish-in-progress`.
- A feature worktree is a prerequisite to external implementation, not a
  substitute for authorization. It must use branch
  `feature/andrew/windows-wsl-dev` and the committed amendment as its base.
  Its actual path is recorded only after the Main Agent verifies creation.
- The external Implementer gate requires both `feature-worktree-ready` and
  separate explicit human authorization for the user-profile files. If either
  is absent or conflicts with the topic plan, stop as `blocked` or
  `human-check` and return to the appropriate independent role.
