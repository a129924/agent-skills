# Cross-Language Skill Candidate Basis — Historical-Remediation Correction Plan

## Correction status

`high` — a prospective historical-remediation baseline is prepared at
`review-ready`, but it is not yet committed or pushed. This correction artifact
is historical truth; the synchronized parent artifacts remain current execution
truth. No PR thread is resolved by preparation of this baseline.

## Frozen correction scope

- The candidate scope remains exactly the locked 11 candidates in four groups.
- `python-implementation-review`'s earlier ordering repair remains a recorded
  historical fact. It is not reopened by this route.
- The `python-code-review` portable-core repair in `c285c3a` is retained as a
  historical remediation in the current tree. No committed artifact before
  that repair provides its implementation authorization; it therefore remains
  historically suspect. This route neither re-executes it nor retroactively
  certifies it.
- No skill, candidate document, platform surface, workflow contract, README,
  VERSION, target project, candidate name, or candidate classification may
  change.
- Recovery is additive. Never amend, rebase, reset, force-push, delete, or
  otherwise rewrite the historical branch or PR commits.

## High-severity issues

All three issues remain `high`; none may be downgraded or closed by assertion.

1. **Missing committed planning baseline:** original implementation and
   approvals occurred without an earlier committed `planned` baseline. That
   sequence is suspect and cannot be certified compliant.
2. **Missing Phase 2 readiness gate:** branch/worktree readiness was not
   recorded by Main Agent before creator work. Main Agent must directly verify
   the prospective baseline before committing it; Dispatcher cannot substitute
   for that verification.
3. **Unproven historical authorization:** `python-code-review` was repaired in
   `c285c3a`, but the preceding committed correction contract authorized only
   the `python-implementation-review` repair. The current fixed tree may be
   governed prospectively, but this historical repair remains suspect and may
   not support a claim of historical workflow compliance.

## Prospective recovery route and acceptance

1. Plan-Creator authors only the five baseline artifacts listed in `Artifact
   Paths`: parent plan, parent progression, parent summary, correction plan,
   and correction progression. This is the prospective governance contract for
   the fixed current tree; it is not a new candidate-document implementation.
2. Main Agent directly performs the Phase 2 branch/worktree check before the
   first commit: confirm the scoped branch and current HEAD, clean/untracked
   disposition, and that the pending diff contains exactly those five paths and
   no candidate document or review log. If any check fails, stop at
   `needs-rework`.
3. With that check passing, Main Agent creates and pushes the first additive
   baseline commit containing exactly those five paths. It is the immutable
   review input and the required ancestor of the later verdict commit.
4. Main Agent records the canonical `review-ready` ->
   `reviewer-in-progress` routing and dispatches an independent Plan-Reviewer.
   After the first commit exists, Plan-Reviewer may write only its canonical
   JSON verdict to the existing review log. Its verdict must explicitly state
   that `python-code-review`'s historical remediation remains suspect; it may
   approve or reject only the prospective baseline's current-tree governance.
5. Main Agent creates and pushes the second additive commit containing only
   that Plan-Reviewer review-log verdict. The five-path baseline commit must be
   its ancestor. A `needs-rework` verdict returns to
   `creator-in-progress`; an `approved` verdict permits
   `publish-in-progress` -> `pr-open` without resolving a PR thread by
   assertion.
6. Planner may close this correction only after the future route is compliant,
   all required evidence and reviews are present, and the historical
   `python-code-review` remediation is explicitly retained as suspect rather
   than retrospectively accepted as compliant.

## Closure

Retain this file and the correction progression after closure; deletion is
forbidden. Historical acceptance means accepting the limitation of the record,
not certifying the pre-existing repair. Planner alone verifies the prospective
route and closure conditions.
