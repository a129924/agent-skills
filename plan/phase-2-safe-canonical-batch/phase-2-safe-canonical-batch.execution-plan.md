# phase-2-safe-canonical-batch execution bootstrap

## Purpose

Activate the approved safe-batch planning baseline after `human-check`
without widening scope, guessing a skill-surface write set, or treating chat
claims as execution authority.

This artifact defines the exact write set for the current bootstrap run only.
It does not reopen the parent planning baseline and does not authorize any
skill-surface edits by analogy.

## Parent Truth

- Approved planning parent:
  `plan/phase-2-safe-canonical-batch/phase-2-safe-canonical-batch.plan.md`
- Current progression truth:
  `plan/phase-2-safe-canonical-batch/phase-2-safe-canonical-batch.step.md`
- Publish / merge target branch:
  `feat/andrew/phase-2-umbrella`
- Frozen analysis prerequisites:
  - `analysis/phase-2-safe-canonical-batch/requirements.md`
  - `analysis/phase-2-safe-canonical-batch/technical-spec.md`
- Repo-level authority:
  - `AGENTS.md`
  - `plan/agent-handoff-workflow.md`
  - `plan/topic-plan-contract.md`

## Current Evidence Snapshot

- Human review approved the committed safe-batch planning baseline on
  2026-06-05, and that approval is now reflected in the topic-local
  `*.step.md`.
- Local branch ancestry confirms `feat/andrew/phase-2-safe-canonical-batch`
  is directly stacked on `feat/andrew/phase-2-umbrella` at parent commit
  `9d1d784`.
- The frozen safe batch remains exactly:
  - `agent-skill-reviewer`
  - `business-intent-alignment`
  - `business-to-technical-translation`
  - `git-branch-naming`
  - `git-commit-convention`
  - `git-post-merge-workflow`
  - `python-project-init-greenfield`
  - `python-project-retrofit`
  - `worktree-manager`
- Repo inspection on 2026-06-05 found byte-equivalent parity between
  `skills/` and `.github/skills/` for all nine frozen safe skills.
- `.codex/skills/` remains a non-authority projection surface and is out of
  scope for this run.

## Immediate Bounded Execution Slice

- Slice name: `safe-batch-bootstrap/no-op-parity-confirmation`
- Objective: freeze a no-guess post-human-check execution entry point and
  confirm whether any creator implementation is honestly required now.
- Decision: no creator implementation on skill surfaces is authorized in this
  bootstrap run because current repo evidence shows no byte-level delta within
  the frozen safe batch.
- Result: this run is execution bootstrap only, not canonical convergence
  implementation.

## Exact Write Set For This Bootstrap Run

The only writable paths in this run are:

- `plan/phase-2-safe-canonical-batch/phase-2-safe-canonical-batch.step.md`
- `plan/phase-2-safe-canonical-batch/phase-2-safe-canonical-batch.execution-plan.md`

The following remain read-only in this run:

- all `skills/**` paths
- all `.github/skills/**` paths
- all `.codex/skills/**` paths
- all `agents/**` paths
- all shared contract files
- all umbrella topic artifacts

## Stop Rules

- If later work would require any skill-surface edit, stop and define a new
  narrower execution slice with exact file paths before dispatching an
  Implementer.
- Do not infer that the frozen nine-skill list is itself a writable set.
- Do not widen into:
  - `phase-2-merge-into-skills-batch`
  - `phase-2-planning-spine-exceptions`
  - projection materialization
  - runtime adaptation
  - copilot-only work
- If any future implementation route would require guessing beyond current
  repo-visible evidence, mark it `human_review_required`.

## Acceptance Checks

- `phase-2-safe-canonical-batch.step.md` records completed `human-check`.
- The topic-local execution bootstrap records `feat/andrew/phase-2-umbrella`
  as the explicit publish / merge target branch.
- The parent planning baseline is treated as approved execution input, not as
  blanket skill-surface write authority.
- The current bootstrap write set is exact and topic-local.
- No skill-surface diff is opened unless a later bounded execution artifact
  explicitly freezes exact writable file paths first.
