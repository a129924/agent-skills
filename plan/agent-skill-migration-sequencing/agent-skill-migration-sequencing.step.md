---
topic: agent-skill-migration-sequencing
status: approved
created: 2026-05-27
---

# Agent Skill Migration Sequencing Steps

## Workflow Stages

- [X] plan
- [X] branch-ready
- [X] creator
- [X] review
- [ ] publish
- [ ] pr-open
- [ ] merged
- [ ] released

## Actionable Steps

### plan
- [X] Freeze topic name, worktree split, and planning-only stop point
- [X] Materialize `analysis/agent-skill-migration-sequencing/requirements.md`
- [X] Materialize `plan/agent-skill-migration-sequencing/agent-skill-migration-sequencing.plan.md`
- [X] Materialize `plan/agent-skill-migration-sequencing/agent-skill-migration-sequencing.step.md`

### branch-ready
- [X] Create managed worktree at `../agent-skills.worktrees/agent-20260527-agent-skill-migration-sequencing`
- [X] Create branch `feat/andrew/agent-skill-migration-sequencing`

### creator
- [X] Inventory migration candidates at `topic / candidate` granularity from existing repo-visible artifacts only
- [X] Classify candidates into `can_start_now`, `after-workflow-baseline`, or `shared-governance-blocked`
- [X] Record applicable artifact and sequencing gap classes for each candidate
- [X] Materialize `plan/agent-skill-migration-sequencing/agent-skill-migration-sequencing.sequencing.md`
- [X] Exclude completed topic/results from the next-wave queue so sequencing rows remain schedulable
- [X] Verify the creator flow stayed inside topic boundaries and did not enter skill-move work

### review
- [X] Reviewer subAgent completed independent review of the sequencing view
- [X] Reviewer subAgent reported `no findings` and no blocking issues
- [X] Topic is review-passed and waiting for Main Agent planner alignment before any publish progression

### publish
- [ ] Apply any required review corrections and pass planner-alignment before publish progression

### pr-open
- [ ] Open and manage the PR after publish progression is authorized

### merged
- [ ] Complete merge and post-merge resume path if this topic later reaches merge

### released
- [ ] Record any release outcome only if a later topic revision explicitly declares release work

## Handoff / Gate Notes

- No skill-move execution is authorized in this phase.
- Shared workflow governance files remain read-only in this worktree.
- The first topic commit is complete as `26a4b16` and contains the planning baseline only.
- Creator work is complete and reviewer approval is now recorded.
- Flow verification is complete for the sequencing artifact and confirmed that no skill folder move or shared-governance edit occurred.
- Reviewer subAgent completed independent review with `no findings`.
- Publish remains not started; the topic is waiting for Main Agent planner alignment and second-topic-commit handling only.
- The second topic commit is intentionally still pending Main Agent integration after reviewer alignment; this subAgent must not commit.
- `plan` and `branch-ready` are complete because the worktree, branch, and three planning artifacts already exist and are already committed.
- If later sequencing work ends with topic-close handoff or `required follow-up`, a topic-close `summary artifact` will be required before close.
