---
topic: python-helper-skill-promotion-wave-2
status: planned
created: 2026-05-28
---

# Python Helper Skill Promotion Wave 2 Steps

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
- [X] Freeze topic name, topic type, migration primitive, target branch, and
  worktree path
- [X] Record the locked 18-skill promotion set and explicit out-of-scope
  boundaries
- [X] Materialize `analysis/python-helper-skill-promotion-wave-2/requirements.md`
- [X] Materialize `plan/python-helper-skill-promotion-wave-2/python-helper-skill-promotion-wave-2.plan.md`
- [X] Materialize `plan/python-helper-skill-promotion-wave-2/python-helper-skill-promotion-wave-2.step.md`

### branch-ready
- [X] Reuse the prepared worktree at `/private/tmp/python-helper-skill-promotion-wave-2`
- [X] Confirm branch `feat/andrew/python-helper-skill-promotion-wave-2`
- [X] Record the worktree-routing audit at `.workflow-runs/topic-bootstrap-python-helper-skill-promotion-wave-2-20260528/worktree-routing-audit.txt`

### creator
- [ ] Re-read the frozen requirements and topic plan before changing promotion
  targets
- [ ] Create exactly 18 `skills/<skill-name>/` target folders from the matching
  `.github/skills/<skill-name>/` source folders by folder-level direct copy
- [ ] Preserve all in-scope `.github/skills/<skill-name>/` folders without
  edits
- [ ] Materialize `docs/migration/python-helper-skill-promotion-wave-2.md`
- [ ] Verify no out-of-scope governance, stable-library, contract-surface, or
  blocker paths were edited

### review
- [ ] Run independent review on the selective-promotion patch set after creator
  work exists
- [ ] Record whether any path drift, source-authority drift, or extra-scope
  promotion occurred

### publish
- [ ] Apply required review corrections if the independent reviewer returns
  `needs-rework`
- [ ] Complete planner final review after reviewer acceptance
- [ ] Pass the commit gate only after review and planner-alignment are both
  complete
- [ ] Commit plan and promotion artifacts by topic in one bounded commit

### pr-open
- [ ] Open and manage the PR after publish progression is explicitly authorized

### merged
- [ ] Complete merge and any later post-merge resume path if this topic reaches
  merge

### released
- [ ] No release action is expected unless a later plan revision explicitly adds
  one

## Handoff / Gate Notes

- `plan` and `branch-ready` are complete because the prepared worktree, target
  branch confirmation, routing audit, and three planning artifacts now exist.
- This step artifact is intentionally usable for later creator, reviewer, and
  publish handoff; it is not a placeholder.
- `.github/skills/` remains the current active authored/reviewed workflow path
  during transition; creator must treat it as preserved promotion input, not as
  a dual canonical-source declaration.
- The 18-skill promotion set is locked. Any additional skill, contract-surface
  lane, runtime/tooling lane, or governance edit requires re-planning.
- This bootstrap round stops before commit. Independent plan review, planner
  final review, and the commit gate all remain pending.
- A future topic-close summary artifact may still be required if this topic
  later closes with handoff or required follow-up.
