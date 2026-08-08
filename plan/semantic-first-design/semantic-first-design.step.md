# Semantic-First Design — Progression

## Workflow Stages

| Stage | Status | Owner | Entry condition | Exit / next gate |
| --- | --- | --- | --- | --- |
| Plan authoring | done | Plan-Creator | Locked human decisions and readable shared contracts | Plan artifacts are ready for independent review |
| Planning-artifact review | pending | Plan-Reviewer | This plan, progression artifact, and review log exist | `approved` proceeds to Implementer; `needs-rework` returns only to Plan-Creator |
| Feature implementation | blocked by planning review | Implementer | Independent planning review is approved | Creates only the three locked `skills/semantic-first-design/*` artifacts and returns `review-ready` |
| Implementation review | pending | Reviewer | Implementer returns `review-ready` | `approved` or `needs-rework` verdict |
| Publish preparation | pending | Main Agent | Reviewer approval and Phase 4.5 alignment | Update `README.md` and `VERSION` only at `publish-in-progress`; STOP POINT 1 before commit/push/draft PR |
| Human review | pending | Human | Draft PR is open | Human review and merge decision; no automatic continuation |
| Post-merge release assessment | blocked by human gate | Human then Main Agent | Explicit human resume after merge | No automatic tag or release |

## Actionable Steps

1. Plan-Reviewer reviews the planning artifacts independently and records its
   JSON verdict in the review log.
2. On planning approval, Main Agent routes the locked plan to an Implementer in
   the feature worktree.
3. On implementation approval, Main Agent performs Phase 4.5 alignment, then
   stages stable-library metadata during `publish-in-progress`.
4. Main Agent verifies the allowed paths, honours STOP POINT 1, then commits,
   pushes, and opens a draft PR.
5. Stop for human review. Do not merge, release, tag, or perform post-merge work
   without the required subsequent human action.

## Handoff / Gate Notes

- Current topic status is `planned`; the immediate next actor is Plan-Reviewer.
- The analysis layer is absent: see the named semantic warning in the topic plan.
  This is not a blocker because the human supplied the locked decisions.
- `needs-rework` from planning review is bounded to planning artifacts. Semantic
  scope, path, or workflow drift must be resolved before implementation begins.
- `needs-rework` from implementation review is bounded to the Implementer;
  planning changes require explicit planner re-entry.
- Reviewer acceptance never self-authorizes the review verdict. Reviewer and
  creator/implementer must remain distinct roles.
- The draft PR is the final automatic boundary. Human review is required before
  any merge decision.
