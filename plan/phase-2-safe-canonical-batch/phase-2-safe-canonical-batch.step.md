---
topic: phase-2-safe-canonical-batch
status: approved
created: 2026-06-05
---

# Phase 2 Safe Canonical Batch Steps

## Workflow Stages

- [X] worktree
- [X] analysis
- [X] plan
- [X] draft-plan-commit-by-topic
- [X] review
- [X] final-gate
- [X] human-check

## Closeout Workflow Stages

- [X] self-check
- [X] target-branch-confirmed
- [X] publish-in-progress
- [ ] pr-open
- [ ] merged
- [ ] worktree-closeout

## Actionable Steps

### worktree
- [X] Use managed worktree `/Users/andrew/code/python/agent-skills.worktrees/agent-20260605-phase-2-safe-canonical-batch`
- [X] Keep all work inside the declared safe-batch write set

### analysis
- [X] Read repo governance, workflow, and topic-plan contract artifacts
- [X] Read umbrella baseline artifacts and confirm this topic is the first slice after umbrella
- [X] Read Phase 1 summary, convergence candidates, and Phase 2 inputs
- [X] Freeze the exact nine-skill safe canonical batch list
- [X] Freeze current turn as planning only

### plan
- [X] Create `analysis/phase-2-safe-canonical-batch/requirements.md`
- [X] Create `analysis/phase-2-safe-canonical-batch/technical-spec.md`
- [X] Create `plan/phase-2-safe-canonical-batch/phase-2-safe-canonical-batch.plan.md`
- [X] Create `plan/phase-2-safe-canonical-batch/phase-2-safe-canonical-batch.step.md`
- [X] Record that later implementation stays bounded to the frozen safe list only
- [X] Record that guessed later implementation write scope is `human_review_required`

### draft-plan-commit-by-topic
- [X] Commit the safe-batch planning artifacts by topic before formal review routing
- [X] Record the draft planning commit in this step artifact once it exists: `4a5160d`

### review
- [X] Route the first-slice planning baseline for independent review
- [X] Confirm the plan does not widen into implementation, later slices, or shared-contract edits

### final-gate
- [X] Confirm the planning baseline stays within the declared write set
- [X] Confirm the topic still records planning-only status for the current workflow stage

### human-check
- [X] Obtain explicit human approval before using this plan as the execution parent for later creator work

## Closeout Actionable Steps

### self-check
- [X] Confirm the approved planning baseline and execution bootstrap remain the
  only repo-visible outputs for this topic
- [X] Confirm no skill-surface implementation slice is open for this topic
- [X] Confirm the topic-local writable set remains limited to
  `phase-2-safe-canonical-batch.step.md` and
  `phase-2-safe-canonical-batch.execution-plan.md`

### target-branch-confirmed
- [X] Record the explicit publish / merge target branch as
  `feat/andrew/phase-2-umbrella`
- [X] Confirm the topic branch is directly stacked on that target branch at
  parent commit `9d1d784`

### publish-in-progress
- [X] Prepare the minimal closeout diff for this topic only
- [ ] Commit the topic-local closeout truth updates
- [ ] Push `feat/andrew/phase-2-safe-canonical-batch`
- [ ] Ensure target branch `feat/andrew/phase-2-umbrella` is available for PR base

### pr-open
- [ ] Open a Ready PR from `feat/andrew/phase-2-safe-canonical-batch` into
  `feat/andrew/phase-2-umbrella`

### merged
- [ ] Merge the Ready PR into `feat/andrew/phase-2-umbrella`

### worktree-closeout
- [ ] Confirm the merge result is reflected in local repo state
- [ ] Finish the topic-local branch / worktree closeout steps without widening scope

## Handoff / Gate Notes

- This topic branches from approved umbrella baseline
  `feat/andrew/phase-2-umbrella` at `9d1d784`.
- This topic is the first execution slice after umbrella.
- The current turn is planning only and does not implement canonical
  convergence.
- The safe canonical batch list is frozen exactly to:
  - `agent-skill-reviewer`
  - `business-intent-alignment`
  - `business-to-technical-translation`
  - `git-branch-naming`
  - `git-commit-convention`
  - `git-post-merge-workflow`
  - `python-project-init-greenfield`
  - `python-project-retrofit`
  - `worktree-manager`
- `skills/` remains the canonical convergence target.
- `.github/skills/` and `.codex/skills/` remain non-authority surfaces.
- `.codex/skills/` remains a partial projection surface only.
- Later slices remain out of scope:
  - `phase-2-merge-into-skills-batch`
  - `phase-2-planning-spine-exceptions`
- Projection materialization, runtime adaptation, and copilot-only work remain
  out of scope.
- `docs/status.md` remains optional only.
- Draft planning artifacts were committed by topic as `4a5160d`.
- Formal review has passed on the committed safe-batch baseline.
- Formal final gate passed on the committed safe-batch baseline with
  `READY_FOR_HUMAN_REVIEW`.
- Human review approved the committed safe-batch planning baseline on
  2026-06-05.
- The approved planning baseline may now serve as the execution parent for
  later bounded creator work only through
  `plan/phase-2-safe-canonical-batch/phase-2-safe-canonical-batch.execution-plan.md`.
- Execution bootstrap was synchronized on 2026-06-05 to freeze a no-guess
  write set for the first bounded post-human-check run.
- Closeout self-check on 2026-06-10 confirmed that no skill-surface
  implementation slice is open and that the minimal remaining work is publish /
  PR / merge closeout only.
- The explicit publish / merge target branch for this topic is
  `feat/andrew/phase-2-umbrella`, matching the approved umbrella parent branch
  recorded in the planning baseline and the current local branch ancestry.
- Current repo evidence shows byte-equivalent parity across all nine frozen
  safe skills between `skills/` and `.github/skills/`.
- No skill-surface implementation was opened by this bootstrap run.
- If later implementation write scope would require guessing beyond current
  Phase 1 + umbrella evidence, route that item to `human_review_required`.
- If planning-stage review later requires `review-log.md` or `summary.md` for
  this topic, do not create them under current scope; route to
  `human_review_required`.
