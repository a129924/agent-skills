---
topic: agent-skill-migration-sequencing
status: planned
created: 2026-05-27
---

# Agent Skill Migration Sequencing Steps

## Workflow Stages

- [X] plan
- [X] branch-ready
- [ ] creator
- [ ] review
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
- [ ] Inventory migration candidates at `topic / candidate` granularity after human permission
- [ ] Classify candidates into `can_start_now`, `after-workflow-baseline`, or `shared-governance-blocked`
- [ ] Record applicable artifact and sequencing gap classes for each candidate

### review
- [ ] Run independent review on the first sequencing view after creator work exists

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
- Human permission is required before the `creator` stage may begin.
- `plan` and `branch-ready` are complete because the worktree, branch, and three planning artifacts already exist.
- If later sequencing work ends with topic-close handoff or `required follow-up`, a topic-close `summary artifact` will be required before close.
