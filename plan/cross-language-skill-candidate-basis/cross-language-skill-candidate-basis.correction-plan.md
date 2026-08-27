# Cross-Language Skill Candidate Basis — High-Severity Recovery Plan

## Correction status

`high` — recovery remains open in `needs-rework`. This artifact is historical
correction truth; the parent plan is the execution-facing contract after parent
sync. The latest published corrective baseline is
`c285c3a11be3a26dfaa661f88e4ace4973829d1f`. Main Agent must verify that exact
published baseline and then the intentionally dirty five-file recovery edit
set; neither observation resolves a PR thread.

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
   recorded by Main Agent before creator work. Under this explicit override,
   Main Agent must directly observe and confirm the current facts before the
   new additive baseline is committed and independently plan-reviewed; they
   must not be invented or delegated to Dispatcher.
3. **Python-specific portable core:** `python-implementation-review` states a
   review ordering as universal despite the locked evidence limiting that order
   to Python context.

## Recovery route and acceptance

1. Main Agent directly verifies and records that `c285c3a` is the published
   branch/HEAD baseline, then compares the execution worktree to it: exactly
   the five listed recovery artifacts are modified, with no untracked file and
   no unrelated modification. Dispatcher may route but cannot substitute for
   this observation or confirmation. Any failed field blocks progression.
2. The recovery loop moves only through `needs-rework` ->
   `creator-in-progress` -> `review-ready`. Plan-Creator's bounded five-file
   artifact preparation is the creator work; it changes neither candidate scope
   nor existing history.
3. Main Agent stages and commits exactly those five artifacts as one additive
   recovery baseline, without amending, rebasing, resetting, force-pushing, or
   otherwise rewriting history. The committed baseline is the fixed input to
   `review-ready` -> `reviewer-in-progress`.
4. An independent Plan-Reviewer performs `reviewer-in-progress` and returns the
   canonical verdict. Only `approved` permits Main Agent to complete
   `approved` -> `publish-in-progress` -> `pr-open`; `needs-rework` returns to
   the beginning of this same canonical loop.
5. The one candidate-document portable-core repair and its independent Reviewer
   verdict are historical and complete. This override authorizes no further
   candidate-document implementation or review.
6. Acceptance requires fixed 11-candidate scope, no history rewrite, Main
   Agent's direct baseline and five-file comparison evidence, the new additive
   baseline commit, parent truth synchronized to this route, independent
   Plan-Reviewer approval, publish/PR observation evidence, and evidence-based
   PR-thread routing.

## Closure

Planner may complete the correction-progression closure checkbox and close this
correction only after parent sync, all required reviews, the corrective commit
and push, and post-push PR confirmation are evidenced in the listed artifacts.
Those conditions do not by themselves close the correction; retain this file
and the correction step as historical evidence and do not delete either
artifact.
