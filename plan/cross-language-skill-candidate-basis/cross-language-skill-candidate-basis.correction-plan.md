# Cross-Language Skill Candidate Basis — High-Severity Recovery Plan

## Correction status

`high` — recovery publication pending. This artifact is historical correction
truth; the parent plan is the execution-facing contract after parent sync. The
frozen repair and its independent re-review have passed, but the complete
corrective change set is not yet committed and pushed and the already-open PR
has not yet undergone post-recovery thread routing.

## Frozen correction scope

- The candidate scope remains exactly the locked 11 candidates in four groups.
- No skill, platform surface, workflow contract, README, VERSION, target
  project, candidate name, or candidate classification may change.
- Recovery is additive. Never amend, rebase, reset, force-push, delete, or
  otherwise rewrite the historical branch/PR commits.

## High-severity issues

All three issues below are frozen as `high` correction; none may be downgraded
or closed by assertion.

1. **Missing committed planning baseline:** original implementation and
   approvals occurred without an earlier committed `planned` baseline, so the
   historical sequence is suspect and cannot be certified compliant.
2. **Missing Phase 2 readiness gate:** branch/worktree readiness was not
   recorded before creator work; its current truth must be observed after the
   committed recovery baseline and independent plan review, not invented.
3. **Python-specific portable core:** `python-implementation-review` states a
   review ordering as universal despite the locked evidence limiting that order
   to Python context.

## Recovery route and acceptance

1. Plan-Creator creates the parent-sync recovery baseline plus this correction
   plan and correction step; a baseline-commit Implementer commits them.
2. An independent Plan-Reviewer returns the canonical JSON verdict for the
   committed baseline. `needs-rework` keeps the topic here.
3. On `approved`, Dispatcher observes and records every required Phase 2 field
   in the correction step. Any dirty/unresolved state blocks creator dispatch.
4. Independent Implementer repairs only the one candidate-document portable
   core entry; independent Reviewer re-reviews it with the canonical JSON
   verdict.
5. Acceptance requires: fixed 11-candidate scope, no history rewrite, parent
   truth synchronized to the recovery route, Phase 2 evidence present, both
   independent reviews passed, the complete corrective change set committed and
   pushed, and only then evidence-based PR-thread routing.

## Closure

Planner may close this correction only after parent sync, all required reviews,
the corrective commit and push, and post-push PR confirmation. Retain this file
and the correction step as historical evidence; do not delete either artifact.
