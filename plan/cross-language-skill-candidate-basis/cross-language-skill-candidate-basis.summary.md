# Cross-Language Skill Candidate Basis — Close Summary

## Current state

`review-ready`: Plan-Creator has prepared a prospective
historical-remediation baseline for the fixed current tree. It is limited to
the five parent/correction planning artifacts and is not committed or pushed
yet. No PR thread is resolved and no new Plan-Reviewer verdict is claimed.

The `python-code-review` portable-core repair in `c285c3a` remains present as
historical remediation, but no preceding committed artifact proves its
implementation authorization. It remains suspect; this topic does not
retroactively certify or re-execute it.

## Completed

- The first-pass inventory exists with its locked four groups and 11 candidates.
- Existing historical commits and PR observations are retained without history
  rewrite, but do not establish that the original workflow was compliant.
- The Planner has frozen a prospective route that governs acceptance of the
  fixed current tree while preserving the historical authorization limitation.
- Plan-Creator has written exactly five baseline artifacts: parent plan, parent
  progression, parent summary, correction plan, and correction progression.

## Not completed

- Main Agent's direct Phase 2 verification of branch/HEAD, exact five-path
  diff, and clean/untracked disposition.
- The first baseline commit/push containing exactly those five paths.
- Independent Plan-Reviewer JSON verdict in the existing review log after that
  first commit and `reviewer-in-progress` routing.
- The second commit/push containing only that review-log verdict, with the
  first commit as ancestor.
- Evidence-based PR comment triage and any thread resolution.
- Planner verification of future compliance and correction closure.

## Required follow-up

1. Main Agent performs the direct Phase 2 validation described in the
   correction progression; if it passes, commit and push only the five baseline
   artifacts.
2. Main Agent routes to `reviewer-in-progress` and dispatches Plan-Reviewer.
   Plan-Reviewer writes only its canonical JSON verdict to the existing review
   log, explicitly retaining the historical `python-code-review` limitation.
3. Main Agent commits and pushes only that verdict as the second commit. An
   `approved` verdict applies prospectively to current-tree governance only;
   it does not certify the historical repair.
4. Planner closes only after the future route is compliant and the historical
   remediation remains explicitly accepted as suspect.

## Next handoff

- **Next actor:** Main Agent (publisher / routing owner).
- **Next step:** directly validate the prepared five-path baseline, then create
  and push the first additive baseline commit.

## Stop condition

Stop if the Phase 2 diff contains any path outside the five listed artifacts,
if the worktree is not clean apart from those edits, or if a proposed verdict
certifies `python-code-review`'s historical repair. Do not resolve threads,
merge, or release before the prospective route and its gates complete.
