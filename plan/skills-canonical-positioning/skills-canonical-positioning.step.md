---
topic: skills-canonical-positioning
status: publish-in-progress
created: 2026-06-02
---

# Skills Canonical Positioning Steps

## Planning Workflow Stages

- [X] worktree
- [X] analysis
- [X] plan
- [X] review
- [X] final-gate
- [X] human-check

## Planning Steps

### worktree
- [X] Create managed worktree at `/Users/andrew/code/python/agent-skills.worktrees/agent-20260602-skills-canonical-positioning`
- [X] Create branch `feat/andrew/skills-canonical-positioning`

### analysis
- [X] Freeze `analysis/skills-canonical-positioning/requirements.md`
- [X] Freeze `analysis/skills-canonical-positioning/technical-spec.md`
- [X] Lock the business baseline to four editable files only
- [X] Lock `.github/skills/**`, `.codex/skills/**`, and `skills/**` as forbidden scope

### plan
- [X] Materialize `plan/skills-canonical-positioning/skills-canonical-positioning.plan.md`
- [X] Materialize `plan/skills-canonical-positioning/skills-canonical-positioning.step.md`
- [X] Record strict-mode analysis prerequisites and SHA-256 values in the topic plan
- [X] Encode editable scope and forbidden scope in the topic plan

### review
- [X] Reviewer subAgent `Lovelace` ran round-1 independent plan review
- [X] Reviewer round 1 returned `needs-rework`
- [X] Reviewer findings were materialized at `plan/skills-canonical-positioning/skills-canonical-positioning.review-log.md`
- [X] Reviewer subAgent `Kepler` ran round-2 re-review
- [X] Reviewer round 2 returned `approved`

### final-gate
- [X] Final gate subAgent `James` ran independent final gate
- [X] Final gate verdict: `approved`
- [X] Final gate result: `GO for human check`
- [X] Remaining risks were recorded from the final gate output

### human-check
- [X] Human review of the planning artifacts completed before implementation round 1 began

## Implementation Workflow Stages

- [X] baseline-confirmed
- [X] implementation-round-1
- [X] review-round-1
- [X] rework-round-2
- [X] review-round-2
- [X] rework-round-3
- [X] review-round-3
- [X] final-gate
- [X] human-check
- [ ] pr-open

## Implementation Steps

### baseline-confirmed
- [X] Confirm planning-state baseline commit `cb20437`
- [X] Reuse managed worktree `/Users/andrew/code/python/agent-skills.worktrees/agent-20260602-skills-canonical-positioning`
- [X] Reuse branch `feat/andrew/skills-canonical-positioning`
- [X] Confirm planning human check was already complete before implementation round 1 started

### implementation-round-1
- [X] Implementation round 1 started in the topic worktree on 2026-06-02
- [X] Re-read the frozen analysis artifacts and approved topic plan before editing repo files
- [X] Update `AGENTS.md`, `docs/repo-positioning.md`, `.github/copilot-instructions.md`, and `README.md` within the frozen write set
- [X] Update `plan/skills-canonical-positioning/skills-canonical-positioning.step.md` with implementation facts only
- [X] Implementation round 1 completed within the allowed five-file scope on 2026-06-02

### review-round-1
- [X] Independent implementation review round 1 occurred after implementation round 1
- [X] Review round 1 verdict: `needs-rework`

### rework-round-2
- [X] Implementation rework round 2 occurred after review round 1 returned `needs-rework`
- [X] Round 2 rework stayed within the allowed five-file scope

### review-round-2
- [X] Independent implementation review round 2 occurred after rework round 2
- [X] Review round 2 verdict: `needs-rework`

### rework-round-3
- [X] Final implementation rework round 3 started on 2026-06-03
- [X] Round 3 rework updated only `plan/skills-canonical-positioning/skills-canonical-positioning.step.md`
- [X] Final implementation rework round 3 completed on 2026-06-03

### review-round-3
- [X] Final implementation review occurred after rework round 3
- [X] Review round 3 verdict: `approved`

### final-gate
- [X] Prior final gate attempt on 2026-06-03 returned `NO-GO` because this step artifact lagged the approved review state
- [X] Final gate rerun on 2026-06-03 returned `approved`
- [X] Final gate rerun result: `GO for implementation human check`

### human-check
- [X] Human approved implementation on 2026-06-03 and authorized the `pr-comment` workflow to proceed

## PR Comment Workflow Stages

- [ ] commit-by-topic
- [ ] push
- [ ] pr-open
- [ ] wait-human-merge-or-feedback

## PR Comment Steps

### commit-by-topic
- [ ] Commit implementation diff and updated step truth for this topic

### push
- [ ] Push branch `feat/andrew/skills-canonical-positioning` to `origin`

### pr-open
- [ ] Open a ready PR against `dev`

### wait-human-merge-or-feedback
- [ ] Wait for human merge or human feedback on PR comments

### pr-open
- [ ] No PR is open for this implementation run

## Handoff / Gate Notes

- Planning-state worktree, analysis, plan review, and planning final gate remain
  recorded above as completed facts for the topic plan.
- Planning human check is also complete and is treated as a prerequisite that
  occurred before implementation round 1 started.
- Baseline commit for this implementation run is `cb20437`.
- Implementation round 1 is complete.
- Independent implementation review round 1 occurred and returned
  `needs-rework`.
- Implementation rework round 2 occurred, followed by independent
  implementation review round 2 with verdict `needs-rework`.
- Final implementation rework round 3 completed on 2026-06-03.
- Independent implementation review round 3 occurred and returned `approved`.
- A first implementation final gate attempt on 2026-06-03 returned `NO-GO`
  because this step artifact had not yet been updated to reflect the approved
  review state.
- Human authorized this single-file step-truth correction on 2026-06-03 so the
  final gate can be rerun from repo-visible current truth.
- Final gate rerun on 2026-06-03 returned `approved` with `GO for
  implementation human check`.
- Human approved implementation on 2026-06-03 and authorized the `pr-comment`
  workflow to proceed.
- The next required action is `pr-comment` step 1: commit by topic.
- No push or PR-open event has occurred yet for this implementation run.
- The only editable repo files authorized by the topic plan remain:
  - `AGENTS.md`
  - `docs/repo-positioning.md`
  - `.github/copilot-instructions.md`
  - `README.md`
- Forbidden scope remains `.github/skills/**`, `.codex/skills/**`, `skills/**`,
  `.github/guides/MAIN-AGENT-WORKFLOW.md`, any `agent-skill-*`, and all
  runtime/tooling/install/sync/projection automation surfaces.
