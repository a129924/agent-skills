---
topic: cross-language-skill-candidate-basis
correction-severity: high
status: review-ready
---

# Cross-Language Skill Candidate Basis — Historical-Remediation Progression

## Recovery Steps

- [X] Planner froze the prospective route: fixed current tree governance only;
  no retrospective authorization of the `python-code-review` repair in
  `c285c3a`.
- [X] Plan-Creator prepared exactly the five baseline artifacts: parent plan,
  parent progression, parent summary, correction plan, and this correction
  progression. No candidate document or review log was written.
- [ ] Main Agent directly completes the Phase 2 verification of the scoped
  branch/HEAD and exact five-path pending diff, including clean and untracked
  disposition. Dispatcher cannot perform or attest this check.
- [ ] After that verification, Main Agent creates and pushes the first additive
  baseline commit containing exactly the five prepared artifacts.
- [ ] Main Agent routes `review-ready` -> `reviewer-in-progress` and dispatches
  independent Plan-Reviewer review of that committed baseline.
- [ ] Only after the first baseline commit and routing, Plan-Reviewer appends
  only its canonical JSON verdict to the existing review log. The verdict must
  state that the historical `python-code-review` remediation remains suspect.
- [ ] Main Agent creates and pushes the second additive commit containing only
  that review-log verdict; the first baseline commit is its ancestor.
- [ ] An `approved` verdict permits `approved` ->
  `publish-in-progress` -> `pr-open`; a `needs-rework` verdict returns to
  `creator-in-progress`. Neither path resolves threads by assertion.
- [ ] Planner alone verifies that the future route is compliant and that the
  historical remediation remains explicitly suspect before closing this
  high-severity correction.

## Phase 2 evidence — Main Agent direct verification required

Before the first baseline commit, Main Agent must directly verify and retain
the command evidence for all of the following:

- The scoped branch is
  `docs/andrew/cross-language-skill-candidate-basis` and the current HEAD used
  for the check is identified.
- `git status --short` contains only the five allowed modifications and no
  untracked path.
- `git diff --name-status` contains exactly these paths:
  - `plan/cross-language-skill-candidate-basis/cross-language-skill-candidate-basis.plan.md`
  - `plan/cross-language-skill-candidate-basis/cross-language-skill-candidate-basis.step.md`
  - `plan/cross-language-skill-candidate-basis/cross-language-skill-candidate-basis.summary.md`
  - `plan/cross-language-skill-candidate-basis/cross-language-skill-candidate-basis.correction-plan.md`
  - `plan/cross-language-skill-candidate-basis/cross-language-skill-candidate-basis.correction-step.md`
- No candidate document, review log, platform surface, Phase 1 artifact, or
  unrelated path is in the first commit.

## Gate

Current status is `review-ready` because Plan-Creator completed the bounded
five-artifact baseline. Main Agent's direct Phase 2 validation and first
commit/push are required before the independent Plan-Reviewer may write its
review-log JSON. The review-log verdict is a separate second commit/push and
cannot certify `c285c3a`'s unproven historical repair. Planner closure requires
future compliance plus explicit retention of that historical limitation.
