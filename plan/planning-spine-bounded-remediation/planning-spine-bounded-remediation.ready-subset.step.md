---
topic: planning-spine-bounded-remediation/ready-subset
status: pr-open
created: 2026-05-28
approved_plan_input: plan/planning-spine-bounded-remediation/planning-spine-bounded-remediation.plan.md
---

# Planning Spine Bounded Remediation Ready Subset Steps

## Workflow Stages

- [X] plan
- [X] branch-ready
- [X] implement
- [X] review
- [X] overlay
- [X] publish
- [X] pr-open
- [ ] merged
- [ ] released

## Actionable Steps

### plan
- [X] Freeze topic as `planning-spine-bounded-remediation/ready-subset`
- [X] Validate `analysis/planning-spine-bounded-remediation/requirements.md` and the existing approved `plan/planning-spine-bounded-remediation/planning-spine-bounded-remediation.plan.md` as the execution basis
- [X] Materialize `plan/planning-spine-bounded-remediation/planning-spine-bounded-remediation.ready-subset.step.md`

### branch-ready
- [X] Prepare branch `feat/andrew/planning-spine-bounded-remediation-ready-subset`
- [X] Record worktree routing and current-workspace reuse evidence

### implement
- [X] Copy the nine ready-subset files from `.github/skills/...` into `skills/...`
- [X] Keep `skills/plan-creator/SKILL.md`, `skills/plan-reviewer/SKILL.md`, and all blocked units untouched
- [X] Keep `.github/skills/plan-creator/...` and `.github/skills/plan-reviewer/...` unchanged
- [X] Prepare implementation evidence for the bounded write set

### review
- [X] Obtain an independent reviewer verdict on scope, 1:1 preserve-semantics alignment, and blocked-unit avoidance
- [X] Record the reviewer result under `.workflow-runs/migration-implementation-planning-spine-bounded-remediation-ready-subset-20260528/`

### overlay
- [X] Confirm no contract-external writable paths or authority changes were required
- [X] Record the migration status classification

### publish
- [X] Create the single-topic publish handoff tied to this implementation run
- [X] Enter `publish-in-progress`
- [X] Stop at topic-local `STOP POINT 1` without commit, push, or PR creation

### pr-open
- [X] Receive explicit human approval to pass topic-local `STOP POINT 1`
- [X] Commit the topic-local publish set
- [X] Push branch `feat/andrew/planning-spine-bounded-remediation-ready-subset`
- [X] Open a Ready PR against `dev`
- [X] Keep PR comment handling out of scope unless actual actionable PR comments appear later

## Handoff / Gate Notes

- The approved execution contract comes from `plan/planning-spine-bounded-remediation/planning-spine-bounded-remediation.plan.md`; this step file is a topic-local progression artifact for the ready subset only.
- The current workspace was reused on the dedicated topic branch. No repo-external managed worktree was created in this run, and that deviation is recorded explicitly in the bootstrap routing artifact.
- Independent reviewer `Curie` returned `approved` with no blocking issues and confirmed byte-for-byte equality for all nine ready-subset source/target pairs.
- Overlay checks passed: no writable path outside the nine ready-subset files plus topic-local workflow artifacts was required, and no `SKILL.md` authority or active-path cutover was introduced.
- Explicit human approval was received to pass topic-local `STOP POINT 1` for publish.
- The topic is now in `pr-open` after the topic-local commit, branch push, and Ready PR creation.
- Do not enter `docs/process/workflows/pr-comment-correction.workflow.md` unless the PR later receives actual actionable comments.
- Blocked units remain out of scope:
  - `plan-creator/fallback-contract-source`
  - `plan-reviewer/review-basis-path`
  - `plan-reviewer/blocked-behavior-for-missing-sources-or-plan`
- If later work would need any file outside the nine ready-subset paths plus topic-local workflow artifacts, stop and re-plan.
