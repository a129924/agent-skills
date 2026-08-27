---
topic: cross-language-skill-candidate-basis
correction-severity: high
status: pending
---

# Cross-Language Skill Candidate Basis — Recovery Progression

## Recovery Steps

- [ ] Commit the recovery planning baseline without amending, rebasing,
  resetting, force-pushing, or deleting historical commits.
- [ ] Independent Plan-Reviewer reviews the committed recovery baseline and
  returns the canonical JSON verdict.
- [ ] Dispatcher records the observed Phase 2 evidence below after a Plan-Reviewer
  `approved` verdict.
- [ ] Independent Implementer makes the one frozen portable-core repair.
- [ ] Independent Reviewer returns the canonical JSON implementation verdict.
- [ ] Planner verifies parent sync and correction acceptance before closure.

## Phase 2 evidence — Dispatcher only

- Branch: pending direct observation
- HEAD: pending direct observation
- Worktree path: pending direct observation
- `git status`: pending direct observation; required disposition is clean
- Untracked-file disposition: pending direct observation
- Recovery baseline SHA: pending creation and direct observation

## Gate

All fields above are intentionally pending. Do not mark a step complete or
invent a SHA, clean status, or branch evidence before the recovery baseline is
committed and independently plan-reviewed. Any failed field keeps the parent
topic at `needs-rework`.
