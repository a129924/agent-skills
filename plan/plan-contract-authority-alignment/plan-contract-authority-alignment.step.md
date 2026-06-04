---
topic: plan-contract-authority-alignment
status: planned
created: 2026-06-04
---

# Plan Contract Authority Alignment Steps

## Workflow Stages

- [X] worktree
- [X] analysis
- [X] plan
- [ ] draft-plan-commit-by-topic
- [ ] review
- [ ] final-gate
- [ ] human-check

## Actionable Steps

### worktree
- [X] Create managed worktree at `/Users/andrew/code/python/agent-skills.worktrees/agent-20260604-plan-contract-authority-alignment`
- [X] Create branch `feat/andrew/plan-contract-authority-alignment`

### analysis
- [X] Freeze `analysis/plan-contract-authority-alignment/upstream-decision-basis.md`
- [X] Freeze `analysis/plan-contract-authority-alignment/requirements.md`
- [X] Freeze `analysis/plan-contract-authority-alignment/technical-spec.md`
- [X] Lock this topic as governance / contract alignment only
- [X] Lock `skills/**`, `.github/skills/**`, `.codex/skills/**`, `.github/agents/**`, and `.codex/agents/**` as read-only scope

### plan
- [X] Materialize `plan/plan-contract-authority-alignment/plan-contract-authority-alignment.plan.md`
- [X] Materialize `plan/plan-contract-authority-alignment/plan-contract-authority-alignment.step.md`
- [X] Materialize `plan/plan-contract-authority-alignment/plan-contract-authority-alignment.review-log.md`
- [X] Materialize `plan/plan-contract-authority-alignment/plan-contract-authority-alignment.summary.md`
- [X] Record strict-mode analysis prerequisites and SHA-256 values in the topic plan
- [X] Encode exact upstream evidence paths, authority ordering, and deferred-work boundaries in the topic plan

### draft-plan-commit-by-topic
- [X] Commit the draft planning artifacts for this topic before reviewer routing
- [X] Record the planning commit hash in this step artifact once the commit exists: `e461b90`

### review
- [ ] Run independent plan review against the topic plan and workflow contract
- [ ] Record reviewer findings in `plan/plan-contract-authority-alignment/plan-contract-authority-alignment.review-log.md`

### final-gate
- [ ] Run final gate after reviewer feedback is addressed
- [ ] Confirm planning artifacts are ready for human check

### human-check
- [ ] Wait for explicit human review before any creator implementation under this topic
- [ ] Confirm no convergence, projection, or runtime work begins before human approval

## Handoff / Gate Notes

- This topic bootstraps a new governance-only planning topic and does not
  authorize implementation yet.
- Upstream accepted evidence is frozen in:
  - `analysis/plan-contract-authority-alignment/upstream-decision-basis.md`
- Current authority remains:
  - `AGENTS.md` for governance
  - `plan/agent-handoff-workflow.md` for repo-level workflow semantics
- The future shared authority surface targeted by this topic is:
  - `plan/topic-plan-contract.md`
- This topic does not authorize:
  - canonical convergence implementation
  - projection materialization
  - runtime adaptation
  - direct absorption of `python-blueprint-review`
  - generic convergence for `copilot-instructions-init`
- Reviewer routing starts only after the topic's draft planning artifacts are
  committed by topic.
- Draft planning artifacts were committed on 2026-06-04 as `e461b90`.
