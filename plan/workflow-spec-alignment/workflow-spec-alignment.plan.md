# workflow spec alignment plan

## Goal / outcome
- Update `plan/agent-handoff-workflow.md` so the repo-level execution flow is easier
  to run correctly in practice, with clearer phase boundaries and fewer late-stage
  surprises.
- Keep the focus on **process semantics**, not on re-litigating concrete skill
  implementation details.
- Produce a repo-visible handoff artifact so creator, reviewer, and main agent can
  execute this spec change without relying on hidden session context.

## Scope
- Clarify where planner-side contract alignment belongs in the workflow.
- Add a stronger validity gate for `Artifact paths`.
- Clarify how stable-library metadata declares README / VERSION timing.
- Add explicit post-merge safety guardrails and sequence expectations.
- Update tightly coupled wording in the same workflow file when necessary to keep
  the document internally consistent.

## Locked decisions
- This topic is a **workflow-spec change**, not a new skill and not a review of one
  concrete implementation.
- The accepted process changes for this topic are:
  1. add a distinct planner contract alignment checkpoint
  2. make artifact path validity an explicit gate
  3. require topic plans to declare stable-library / release timing when applicable
  4. write post-merge safety as explicit guardrails plus sequence, not just as a
     soft principle
- Planner contract alignment should be written as an **independent Phase 4.5**
  checkpoint, not folded into generic reviewer routing.
- Stable-library timing should use **topic-plan-must-declare-timing** semantics:
  if a topic needs README / VERSION updates, the topic plan must say when those
  updates happen; main agent must not infer the timing.
- This topic should stay process-focused and must not broaden into implementation
  review rules beyond what is necessary to express workflow boundaries.
- This topic does not introduce a release action for the repository itself.

## Boundaries / exclusions
- Do not modify `.github/skills/` skill content as part of this topic, except for
  narrowly scoped consistency updates to the explicitly coupled reviewer
  checklist in `Artifact paths`
  (`.github/skills/agent-skill-reviewer/review-checklist.md`).
- Do not change `README.md` or `VERSION` for this workflow-spec task.
- Do not rewrite the entire workflow from scratch when targeted clarification is
  sufficient.
- Do not collapse planner contract alignment into ordinary code-quality review.
- Do not use hidden session summaries as the execution source of truth once this
  repo-visible topic plan exists.

## Status / allowed transitions
- Current status: `pr-open`
- Allowed transitions:
  - `planned` -> `creator-in-progress`
  - `creator-in-progress` -> `review-ready`
  - `review-ready` -> `reviewer-in-progress`
  - `reviewer-in-progress` -> `approved`
  - `reviewer-in-progress` -> `needs-rework`
  - `needs-rework` -> `creator-in-progress`
  - `approved` -> `creator-in-progress`
  - `approved` -> `publish-in-progress`
  - `publish-in-progress` -> `pr-open`
  - `pr-open` -> `needs-rework`
  - `pr-open` -> `merged`
  - `merged` -> terminal

## Artifact paths
- Topic plan:
  - `plan/workflow-spec-alignment/workflow-spec-alignment.plan.md`
- Primary workflow spec to update:
  - `plan/agent-handoff-workflow.md`
- Tightly coupled references to review and update only if they become inconsistent:
  - `.github/guides/MAIN-AGENT-WORKFLOW.md`
  - `.github/skills/agent-skill-reviewer/review-checklist.md`

## Implementation steps
1. Create and maintain this repo-visible topic plan as the execution contract for
   the task.
2. Update `plan/agent-handoff-workflow.md` to add a distinct planner contract
   alignment checkpoint after reviewer approval and before publish.
3. Strengthen workflow language so `Artifact paths` becomes a validation gate, not
   just an informational list.
4. Clarify that stable-library metadata must declare timing when README / VERSION
   updates are part of the topic.
5. Expand post-merge local sync guidance into explicit guardrails and step order.
6. Check tightly coupled guide / checklist files only for direct contradictions; do
   not broaden the change set unnecessarily.

## Validation / acceptance checks
- The workflow still preserves role separation among planning actor, creator,
  reviewer, and main agent.
- Planner contract alignment is represented as a distinct checkpoint with clear
  routing when it fails.
- `Artifact paths` language now makes path validity a required gate.
- Stable-library timing language prevents main agent from guessing README /
  VERSION timing.
- Post-merge guidance now includes explicit safety order rather than a vague sync
  instruction.
- The resulting text remains consistent with the status model and does not create
  contradictory phase ownership.

## Reviewer handoff
- Reviewer should judge whether the updated workflow is clearer to execute, not
  whether one historical implementation detail was “correct.”
- Review focus:
  - phase ownership and transition clarity
  - planner checkpoint placement and routing
  - artifact path validation responsibility
  - stable-library / release timing semantics
  - post-merge safety wording

## Post-merge / release actions
- After merge, run the normal post-merge local sync flow on the spec branch.
- No repository release action is required for this topic by default.
- This topic is terminal at `merged` unless the human later decides the workflow
  spec change itself should trigger a separate release process.

## Open questions / unresolved items
- Whether `.github/guides/MAIN-AGENT-WORKFLOW.md` should be updated in the same PR
  or in a follow-up depends on whether the workflow-spec wording creates direct
  inconsistency there.
- Whether reviewer checklist changes belong in this same topic should be decided by
  direct coupling, not by convenience.
