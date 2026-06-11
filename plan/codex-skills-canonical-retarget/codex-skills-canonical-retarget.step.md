---
topic: codex-skills-canonical-retarget
status: publish-in-progress
created: 2026-06-11
---

# Codex Skills Canonical Retarget Steps

## Workflow Stages

- [X] repo-contract-read
- [X] topic-facts-read
- [X] plan-artifacts-authored
- [X] independent-plan-review
- [X] plan-fix-if-needed
- [X] branch-ready
- [X] implementation
- [X] implementation-review
- [ ] publish
- [ ] pr-open
- [ ] merged

## Actionable Steps

### repo-contract-read

- [X] Read `plan/agent-handoff-workflow.md`
- [X] Read `plan/topic-plan-contract.md`
- [X] Read `skills/plan-creator/templates/topic-plan-template.md`
- [X] Read `skills/subagent-dispatch-policy/SKILL.md` for role-boundary checks

### topic-facts-read

- [X] Confirm `analysis/codex-skills-canonical-retarget/requirements.md` is
      absent
- [X] Confirm `analysis/codex-skills-canonical-retarget/technical-spec.md` is
      absent
- [X] Confirm the 11 target directories exist under `skills/`
- [X] Confirm `.codex/skills/README.md` and `.codex/skills/provenance.md`
      required topic-local rematerialization updates after the user changed the
      target from symlink retarget to `.codex`-local materialized copies
- [X] Confirm the first implementation pass drifted because it only retargeted
      7 symlinks and did not complete the full first-wave materialization

### plan-artifacts-authored

- [X] Materialize
      `plan/codex-skills-canonical-retarget/codex-skills-canonical-retarget.plan.md`
- [X] Materialize
      `plan/codex-skills-canonical-retarget/codex-skills-canonical-retarget.step.md`
- [X] Freeze feature branch
      `feat/andrew/codex-skills-canonical-retarget`
- [X] Freeze PR target branch `dev`
- [X] Freeze implementation write set to the exact `.codex/skills/**` paths
      named in the topic plan
- [X] Freeze `skills/**` and `.github/skills/**` as read-only for this topic
- [X] Freeze topic non-goals: no hash/JSONL/versioning work and no platform-
      wide residue cleanup

### independent-plan-review

- [X] Run independent `plan-reviewer` review before branch preparation or
      implementation begins
- [X] Materialize
      `plan/codex-skills-canonical-retarget/codex-skills-canonical-retarget.review-log.md`
      because reviewer feedback controlled routing in Round 1
- [X] Re-run independent `plan-reviewer` after the bounded planning repair
- [X] Do not prepare branch
      `feat/andrew/codex-skills-canonical-retarget` until reviewer verdict is
      `approved`

### plan-fix-if-needed

- [X] If reviewer returns `needs-rework`, limit corrections to this topic's
      `*.plan.md`, `*.step.md`, and, when routing feedback exists,
      `*.review-log.md`
- [X] Re-run independent plan review until repo-visible planning truth reaches
      `approved`

### branch-ready

- [X] Prepare branch `feat/andrew/codex-skills-canonical-retarget` from `dev`
      only after approved plan review
- [X] Keep branch preparation outside this planning-only write set

### implementation

- [X] Replace the first-wave 11 `.codex/skills/*` surfaces with `.codex`-local
      materialized directories copied from same-name canonical `skills/*`
- [X] Update `.codex/skills/README.md` and `.codex/skills/provenance.md`
- [X] Concretize copied `.<platform>/skills/...` literals to
      `.codex/skills/...` only within the materialized `.codex` surface
- [X] Keep `skills/**` and `.github/skills/**` read-only
- [X] Repair the earlier mistaken symlink-retarget implementation and the
      accidental canonical nested-copy pollution before continuing

### implementation-review

- [X] Run bounded implementation review against the current 11-item
      materialized `.codex/skills/**` surface and this topic's workflow truth
- [X] Confirm no execution-meaning conflict remains among
      `*.plan.md`, `*.step.md`, `*.review-log.md`, and the implemented
      materialized skill surfaces
- [X] Resolve the implementation-review rework by repairing topic truth and
      staging the materialized replacement directories before final reviewer
      acceptance

### publish

- [ ] Enter canonical publish routing only after implementation review returns
      `approved`

### pr-open

- [ ] Open and manage the PR only after publish progression is authorized

### merged

- [ ] Record merge and post-merge local sync facts only if the topic later
      reaches merge

## Handoff / Gate Notes

- Analysis-layer semantic warning: no topic-local `requirements.md` or
  `technical-spec.md` exists for this topic; the plan is derived from locked
  human decisions plus repo-level contracts only.
- Round 1 independent plan review returned `needs-rework` because the plan
  required a routing `review-log` but simultaneously forbade updating it in the
  planning correction loop.
- The topic-local `review-log` records that reviewer verdict and the bounded
  planning repair.
- Round 2 independent plan review returned `approved` with no blocking issues.
- Feature branch `feat/andrew/codex-skills-canonical-retarget` was created from
  `dev` after approved plan review.
- The bounded implementation diff now exists only in the frozen `.codex/skills`
  write set:
  - `.codex/skills/README.md`
  - `.codex/skills/provenance.md`
  - `.codex/skills/business-intent-alignment/`
  - `.codex/skills/business-to-technical-translation/`
  - `.codex/skills/plan-creator/`
  - `.codex/skills/plan-reviewer/`
  - `.codex/skills/agent-skill-creator/`
  - `.codex/skills/agent-skill-reviewer/`
  - `.codex/skills/agent-skill-template/`
  - `.codex/skills/git-branch-naming/`
  - `.codex/skills/git-commit-convention/`
  - `.codex/skills/git-post-merge-workflow/`
  - `.codex/skills/worktree-manager/`
- Round 1 bounded implementation review returned `needs-rework` because the
  topic artifacts still described the superseded 7-entry symlink-retarget
  contract and the materialized replacement directories had not yet been staged
  as branch content.
- Round 2 bounded implementation review returned `approved` after the topic
  truth was repaired to the 11-entry materialized-copy contract and the staged
  branch content reflected the directory replacements.
- Current stop condition: local publish routing may proceed under the explicit
  human commit approval already granted for this topic; push / PR work remain
  blocked until separately authorized.
