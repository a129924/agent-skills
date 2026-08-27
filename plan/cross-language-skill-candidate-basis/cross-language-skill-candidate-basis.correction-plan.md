# Cross-Language Skill Candidate Basis — High-Severity Recovery Plan

## Correction status

`high` — recovery remains open in `pr-open`. This artifact is historical
correction truth; the parent plan is the execution-facing contract after parent
sync. The frozen repair and its independent re-review have passed, and the
complete corrective package was committed and pushed at
`21af6fff4d5f167db3459b55f8ea061c0ecf4d42`. Post-push observation found the
PR `OPEN`, with `checks=[]` and no new threads or checks; all existing threads
remain unresolved.

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
   plan and correction step. Main Agent is accountable for routing the
   `planned` recovery transition and preserving its audit evidence; Dispatcher
   records only bounded transition evidence and routing. Neither commits. An
   independent Implementer performs the constrained baseline `git commit`
   without amending, rebasing, resetting, force-pushing, or otherwise rewriting
   history.
2. An independent Plan-Reviewer returns the canonical JSON verdict for the
   committed baseline. `needs-rework` keeps the topic here.
3. On `approved`, Dispatcher observes and records every required Phase 2 field
   in the correction step, then routes the evidence to Main Agent for the
   transition audit. Any dirty/unresolved state blocks creator dispatch.
4. Independent Implementer repairs only the one candidate-document portable
   core entry; independent Reviewer re-reviews it with the canonical JSON
   verdict.
5. Acceptance requires: fixed 11-candidate scope, no history rewrite, parent
   truth synchronized to the recovery route, Phase 2 evidence present, both
   independent reviews passed, the complete corrective package committed and
   pushed, and completed post-push PR observation before evidence-based
   PR-thread routing.

## Closure

Planner may complete the correction-progression closure checkbox and close this
correction only after parent sync, all required reviews, the corrective commit
and push, and post-push PR confirmation are evidenced in the listed artifacts.
Those conditions do not by themselves close the correction; retain this file
and the correction step as historical evidence and do not delete either
artifact.
