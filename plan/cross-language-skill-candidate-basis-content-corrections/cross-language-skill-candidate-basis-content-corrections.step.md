---
topic: cross-language-skill-candidate-basis-content-corrections
status: needs-rework
current_plan_input: plan/cross-language-skill-candidate-basis-content-corrections/cross-language-skill-candidate-basis-content-corrections.plan.md
---

# Cross-Language Skill Candidate Basis Content Corrections Steps

## Workflow Stages

- [x] independent-plan-review
- [x] bounded-six-cell-implementation
- [x] independent-document-review
- [x] phase-4.5-planning-rework
- [x] independent-plan-re-review
- [x] phase-4.5-alignment
- [x] commit-push-pr
- [x] new-pr-feedback-routed
- [x] pr-loop-contract-rework
- [x] independent-plan-review-of-pr-loop-contract
- [ ] planning-repair-commit-push
- [ ] independent-thread-coverage-verification
- [ ] feedback-driven-rework
- [ ] pr-feedback-coverage-and-bounded-observation
- [ ] human-merge-handoff

## Actionable Steps

### independent-plan-review

- Completed by: independent Plan-Reviewer.
- Recovery baseline reviewed:
  `a725e71fd8cbe9ce6fb35fbf85ac7e250f878feb`.
- Result: `approved`, preserved verbatim in the plan-review log.

### commit-push-pr

- Completed by: Main Agent after STOP POINT 1 authorization.
- Result: the bounded candidate correction was committed as
  `75676e2f472abeb04a034ab765f1973d6b4dfcf5` and force-pushed to the current
  head of ready-for-review PR #125.
- This records neither resolved threads nor any merge, release, or close claim.

### new-pr-feedback-routed

- Entry condition: a fresh PR #125 snapshot after the PR was ready.
- Completed by: Main Agent routing.
- Result: new actionable PR-head feedback routes the topic from `pr-open` to
  `needs-rework`. This progression artifact does not claim that every feedback
  item was answered, resolved, or otherwise covered.

### pr-loop-contract-rework

- Completed by: Plan-Creator.
- Result: parent and correction artifacts now truthfully record the committed /
  force-pushed candidate edit, the open PR feedback route, Phase 7--8 signal
  fetch and bounded observation requirements, and the pre-merge STOP POINT 2
  boundary.
- The output is `review-ready` for independent Plan-Reviewer review. It makes
  no candidate-basis change and does not answer or resolve PR threads.

### independent-plan-review-of-pr-loop-contract

- Entry condition: `pr-loop-contract-rework` is `review-ready`.
- Owner: independent Plan-Reviewer.
- Completed result: `approved`, preserved verbatim in the plan-review log.
- The approval covers the PR-loop planning repair only; it does not authorize
  candidate implementation, publication, thread action, clean observation,
  human merge handoff, merge, release, summary, or close.

### planning-repair-commit-push

- Entry condition: recorded independent Plan-Reviewer `approved` handoff for
  the PR-loop planning repair.
- Owner: Main Agent.
- Required result: commit and push only the bounded planning/progression
  repair. This step does not reply to or resolve PR threads and does not alter
  the candidate basis.

### independent-thread-coverage-verification

- Entry condition: `planning-repair-commit-push` completes.
- Owner: independent Reviewer.
- Required result: use a fresh PR snapshot to classify and verify coverage of
  every actionable thread before any thread reply, resolution, or further
  feedback-driven implementation route. This verification records neither a
  resolved-thread claim nor clean observation unless those facts are separately
  established.

### feedback-driven-rework

- Entry condition: independent thread-coverage verification identifies a
  bounded change that is required.
- Owner: independent Implementer when a bounded change is required; independent
  Reviewer when feedback affects logic, scope, requirements, boundaries, or
  the locked contract.
- Main Agent must re-fetch PR reviews / review state, review comments and
  threads, issue comments, and checks after each relevant change. New
  actionable feedback returns to `needs-rework`; direct-apply iterations are
  limited to three. A thread may be replied to and resolved only when its
  applicable outcome is actually satisfied; otherwise it remains blocking.

### pr-feedback-coverage-and-bounded-observation

- Entry condition: fresh PR signals establish full coverage of actionable
  feedback and no currently blocking review, unresolved blocking thread,
  actionable comment, or non-clean check remains.
- Owner: Main Agent.
- Run the bounded `consecutive-empty-checks` observations at exactly
  `30s -> 60s -> 120s`, re-fetching all required PR signals after each wait.
  Any new blocking signal resets the clean count and routes to `needs-rework`.
- Only after three clean snapshots may Main Agent produce a bounded
  clean-observation report for a human merge-readiness decision. A draft or
  ready PR alone is not eligible for human merge handoff.

### human-merge-handoff

- Entry condition: bounded clean-observation report is complete and a human
  explicitly chooses merge handoff.
- STOP POINT 2: Main Agent stops immediately before the actual human merge;
  it must not poll, wait, infer merge completion, or start post-merge work.
- Phase 9 may begin only after a new explicit human message both confirms PR
  #125 was merged and authorizes post-merge resume.

## Handoff / Gate Notes

- Parent plan is current truth; this step is progression truth only.
- Correction artifacts preserve high-severity recovery history only and do not
  approve work or replace the parent contract.
- Phase 4.5 and publication are completed facts. PR #125 remains open in
  `needs-rework`; the PR-loop planning repair is independently approved and
  awaits its planning-only commit/push followed by independent thread-coverage
  verification. No thread coverage, clean observation, human merge handoff,
  merge, release, summary, or topic-close fact is recorded.
- This non-stable topic has no README, VERSION, release, or tag route.
