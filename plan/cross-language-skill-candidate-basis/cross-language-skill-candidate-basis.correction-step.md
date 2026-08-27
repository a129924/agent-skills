---
topic: cross-language-skill-candidate-basis
correction-severity: high
status: needs-rework
---

# Cross-Language Skill Candidate Basis — Recovery Progression

## Recovery Steps

- [ ] Main Agent directly verifies and confirms the published `c285c3a`
  baseline and the exact five-file execution-worktree comparison below;
  Dispatcher may route the result but cannot substitute for the observation or
  confirmation.
- [ ] Route `needs-rework` -> `creator-in-progress`; Plan-Creator's prepared
  changes remain limited to the exact five recovery artifacts.
- [ ] Route `creator-in-progress` -> `review-ready`; no candidate document,
  review log, or unrelated artifact is added to the edit set.
- [ ] Main Agent stages exactly those five planning artifacts, confirms no other
  staged, unstaged, or untracked change exists, and executes the new additive
  recovery-baseline commit without amending, rebasing, resetting, force-pushing,
  or deleting historical commits.
- [ ] Route `review-ready` -> `reviewer-in-progress`; independent Plan-Reviewer
  reviews that newly committed additive baseline and returns the canonical JSON
  verdict.
- [ ] On `approved`, Main Agent completes only `approved` ->
  `publish-in-progress` -> `pr-open` with push and PR observation evidence. A
  `needs-rework` verdict restarts this same loop; no direct status jump exists.
- [X] Independent Implementer makes the one frozen portable-core repair.
- [X] Independent Reviewer returns the canonical JSON implementation verdict:
  `approved`.
- [ ] Planner alone may complete this checkbox after verifying parent sync, both
  independent approvals, the corrective commit and push, and post-push PR
  confirmation in the listed artifacts; then and only then may it close this
  high-severity correction.

## Phase 2 evidence — Main Agent direct verification required

- Execution baseline: `c285c3a11be3a26dfaa661f88e4ace4973829d1f`.
- Branch: `docs/andrew/cross-language-skill-candidate-basis`.
- Worktree path:
  `/Users/andrew/code/python/agent-skills.worktrees/agent-20260827-cross-language-skill-candidate-basis`.
- Published-baseline check: Main Agent must verify that the checked-out branch
  and `HEAD` identify the published `c285c3a` baseline before assessing the
  additive edit set. This is a clean immutable reference, not a claim that the
  prepared execution worktree has no changes.
- Execution-worktree disposition to verify directly before staging: compared
  with `c285c3a`, exactly the five allowed recovery-file modifications below,
  no untracked files, and no unrelated modification.
- Previous recovery baseline SHA: `9173c66` (historical only).
- Previous Plan-Reviewer verdict commit: `67ba9d7` (historical only).
- Required staged set after the direct published-baseline observation: exactly
  `cross-language-skill-candidate-basis.plan.md`,
  `cross-language-skill-candidate-basis.step.md`,
  `cross-language-skill-candidate-basis.correction-plan.md`,
  `cross-language-skill-candidate-basis.correction-step.md`, and
  `cross-language-skill-candidate-basis.summary.md` under
  `plan/cross-language-skill-candidate-basis/`; no other staged, unstaged, or
  untracked change is allowed.

## Gate

The listed prior post-push state is historical evidence only. Main Agent must
directly re-observe and confirm every published-baseline and
execution-worktree-comparison field before routing `needs-rework` ->
`creator-in-progress`, then confirm the exact allowed staged set and absence of
all other staged, unstaged, and untracked changes before the additive commit.
Dispatcher may route but cannot perform or attest either confirmation. The
required loop is `needs-rework` -> `creator-in-progress` -> `review-ready` ->
`reviewer-in-progress` -> `approved` -> `publish-in-progress` -> `pr-open`.
It resolves no PR thread. Any failed, unrelated, untracked, or reviewer
`needs-rework` result returns or keeps the loop at `needs-rework`.

## Historical post-review publication evidence

- The independent Implementer repair and independent Reviewer `approved`
  verdict are complete. They are historical repair evidence and do not produce
  a current-loop transition.
- The latest published corrective head is
  `c285c3a11be3a26dfaa661f88e4ace4973829d1f`.
- Post-push repository observation found the scoped branch synchronized with
  `origin`, clean porcelain status, and no untracked files. This record
  resolves no thread and does not close this high-severity correction.
- Next: Main Agent performs the override-owned direct Phase 2 verification and
  additive baseline commit. Planner alone may later verify correction acceptance
  before closure.
