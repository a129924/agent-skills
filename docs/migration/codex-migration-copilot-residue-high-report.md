# codex-migration-copilot-residue-high report

## Branch

- `feat/andrew/codex-migration-copilot-residue-high`

## Candidate

- candidate skill: `.github/skills/git-post-merge-workflow/`

## Verdict

- verdict: `redesign`
- migration action in this branch: `none`
- actual migration action performed in this branch: `none`
- future move recommended: `yes`

## Why

- The skill still expresses a portable post-merge safety workflow rather than a
  Copilot-only behavior.
- The core behavior is product-agnostic: verify STOP POINT 2 resume
  conditions, protect local state, perform ff-only sync, and apply guarded
  branch cleanup.
- The current implementation remains tightly coupled to transition-era
  repository workflow semantics, `.github/skills/` placement, and git command
  execution details, so it does not qualify for direct move or low-residue
  treatment.
- Repo-visible evidence is sufficient to state a bounded redesign objective:
  preserve the post-merge safety contract while later translating the skill
  into a Codex-aligned source/projection model and updated workflow surface.
- This branch does not authorize that redesign implementation, so the correct
  action here is classification and reporting only.

## Residue / Blocker Note

- residue note: high Copilot residue remains credible because the skill depends
  on explicit STOP POINT 2 handoff semantics, destructive branch-cleanup
  safeguards, and repo-specific workflow coordination.
- blocker repair performed in this branch: `no`
- blocker note: no runtime/tooling blocker repair is required to keep the skill
  classed as high residue in this branch.
- reclassification trigger not met: the skill is not better described as
  reference-only or Copilot-specific-only from the current repo-visible
  evidence set.

## Follow-up

- follow-up branch or topic: planner-owned follow-up on
  `feat/andrew/codex-skills-spec-worktree` or a later Codex migration topic
  that explicitly authorizes candidate-skill redesign with acceptance criteria.
- recommended follow-up objective: define a Codex-native redesign contract for
  post-merge cleanup and local-sync workflow behavior before any candidate
  content move or projection update is attempted.

## Upstream Spec Status

- upstream spec-worktree artifact remains unchanged in this branch: `yes`
- unchanged artifact: `docs/migration/codex-skills-spec-worktree.md`
- note: this branch records classification output only and does not alter
  upstream first-wave inclusion records.
