---
topic: cross-language-skill-candidate-basis-content-corrections
status: publish-in-progress
current_plan_input: plan/cross-language-skill-candidate-basis-content-corrections/cross-language-skill-candidate-basis-content-corrections.plan.md
---

# Cross-Language Skill Candidate Basis Content Corrections Steps

## Workflow Stages

- [x] recovery-baseline-and-pr-loop-planning-repair
- [x] published-pr-loop-planning-repair-1885c35
- [x] canonical-source-override-planning-repair
- [x] independent-plan-review-of-latest-clarification
- [x] historical-four-cell-pre-review
- [x] planner-phase-4-5-alignment-input
- [x] main-agent-publish-or-rework-routing
- [ ] publication-of-approved-rework
- [ ] fresh-pr-signal-and-thread-coverage
- [ ] feedback-driven-rework
- [ ] bounded-clean-observation
- [ ] human-merge-handoff

## Actionable Steps

### historical-four-cell-pre-review

- Historical record: the four named portable-core cells, including the
  `boundary-outcome-design` Adapter--Port correction, were presented before
  the current `needs-rework` route. This record is pre-review only and does
  not assert a current approval, alignment, publication, or PR/thread result.

### planner-phase-4-5-alignment-input

- Entry condition: active parent `needs-rework` routing and the locked
  four-cell canonical correction scope.
- Owner: Planner.
- Completed result: Planner supplied Phase 4.5 alignment input without
  changing locked scope or deciding publication/rework.

### main-agent-publish-or-rework-routing

- Entry condition: the required independent gate and Phase 4.5 input are
  available.
- Owner: Main Agent.
- Completed result: after the independent Plan-Reviewer `approved` gate and
  existing STOP POINT 1 authorization, Main Agent selected publication. The
  bounded commit/push remains pending; no publication outcome is claimed.

### publication-of-approved-rework

- Entry condition: Main Agent routes approved rework to publication and STOP
  POINT 1 is explicitly authorized.
- Owner: Main Agent.
- Required result: commit/push approved change to PR #125; no thread result is
  inferred by publication.

### fresh-pr-signal-and-thread-coverage

- Entry condition: approved rework is published to PR #125.
- Owner: Main Agent, with independent Reviewer verification where required.
- Required result: fresh review state, comments/threads, issue comments, and
  checks; classify and cover each actionable signal. Reply/resolve only after
  outcome satisfaction. Blocking/contract-changing feedback returns to
  `needs-rework`.

### feedback-driven-rework

- Entry condition: fresh PR signals require a bounded change.
- Owner: independent Implementer; independent Reviewer re-enters for logic,
  scope, requirement, boundary, or contract feedback.
- Required result: fix, gain approval, publish, and re-fetch signals;
  direct-apply iterations are limited to three.

### bounded-clean-observation

- Entry condition: full actionable coverage and no blocking review, unresolved
  blocking thread, actionable comment, or failing check.
- Owner: Main Agent.
- Required result: clean snapshots exactly `30s -> 60s -> 120s`; new blockers
  reset the sequence and return to `needs-rework`. Three snapshots produce a
  bounded clean-observation report only.

### human-merge-handoff

- Entry condition: clean-observation report and explicit human merge choice.
- **STOP POINT 2:** Main Agent stops before actual merge; Phase 9 requires
  explicit human merge confirmation and resume authorization.

## Handoff / Gate Notes

- The current parent state is `publish-in-progress`. `1885c35` remains pushed
  to PR #125 with ten unresolved threads; the newly aligned bounded change is
  pending commit/push. No observation, thread completion, merge, release,
  summary, or topic close is recorded.
- The four-cell canonical correction, including the Adapter--Port fix, is
  historical/pre-review only. Phase 4.5 alignment and Main Agent publication
  routing are complete; Main Agent alone owns the pending commit/push. No
  publication is recorded.
