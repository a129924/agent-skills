---
topic: agent-skills-published-asset-hygiene-baseline
status: needs-rework
---

# Agent Skills Published Asset Hygiene Baseline Steps

## Workflow Stages

- [X] branch-and-worktree
- [X] initial-implementation
- [X] all-files-discovery
- [X] planner-replan
- [X] first-correction-implementation
- [X] second-correction-planning
- [X] second-correction-implementation
- [X] independent-review
- [X] planner-alignment
- [X] phase-4.5-plan-review
- [X] human-publish-authorization
- [X] commit-push-ready-pr
- [X] pr-comment-triage
- [ ] pr-feedback-correction-implementation
- [ ] pr-feedback-independent-review
- [ ] pr-comment-review-and-fix

## Actionable Steps

1. PR #120 is `needs-rework` only for P2-1: the canonical
   `skills/plan-step-tracker/examples.md` lost two Markdown hard-break markers.
   Its two projections are the locked three-file synchronization write set.
2. P2-2 (completed human publish authorization and the `pr-open` to
   `needs-rework` workflow state) is Planner-owned and resolved in this topic
   step and the parent plan. P2-3 (portable current verification) is
   Planner-owned and resolved in the parent plan's `PATH`-resolvable
   `pre-commit` and writable `PRE_COMMIT_HOME` prerequisite. Neither authorizes
   an Implementer write.
3. Route the exact P2-1 contract in
   `agent-skills-published-asset-hygiene-baseline.pr-feedback-correction-plan.md`
   to an independent Implementer. The only implementation writes are the three
   named examples; the Implementer must replace the two relevant trailing
   double-space hard-break markers with `<br>` in each file.
4. After implementation evidence is recorded in the PR-feedback correction
   step, route the result to an independent Reviewer. Only an `approved`
   reviewer verdict returns the topic to `pr-open` and resumes
   `pr-comment-review-and-fix`.
5. The prior Copilot quota limitation remains an external-review limitation;
   it does not resolve, replace, or reduce the three P2 comments.

## Handoff / Gate Notes

- Parent plan is current truth; correction artifacts are historical routing
  truth and do not override it.
- Worktree: `/Users/andrew/code/python/agent-skills.worktrees/agent-20260728-agent-skills-published-asset-hygiene-baseline`
- Branch: `feature/andrew/agent-skills-published-asset-hygiene-baseline`
- Current status: `needs-rework`; human publish authorization was received,
  the bounded changes were committed and pushed, and Ready PR #120 remains
  open. P2-2 and P2-3 are resolved Planner-owned corrections; only P2-1 routes
  to `pr-feedback-correction-implementation`.
- Current verification evidence for the 46 tracked published-skill assets is
  normalized byte equality against `HEAD`: apply only trailing horizontal
  whitespace removal, terminal-blank-line removal, and exactly one final LF
  to both versions, then compare the results. This passed for all 46 assets.
  `git diff -w --exit-code` is intentionally not recorded as passing because
  permitted terminal blank-line removals make that command return nonzero.
- The first correction artifacts are historical truth and remain unchanged.
  The second correction artifacts are also retained historical truth and are
  `resolved`. Its historical `git diff -w --exit-code` pass statement is
  superseded by the parent plan: a direct rerun exits `1` for allowed terminal
  blank-line removals. The parent plan's restricted-normalizer equality plus
  existing dynamic validation is the sole valid 46-asset format-only proof.
  The review log contains the sole implementation-review `approved` JSON
  verdict; the separately approved Phase 4.5 Plan-Reviewer result is recorded
  in the parent plan without changing that log.
- P2-1 remains unresolved pending independent implementation and review.
  P2-2 and P2-3 are resolved by the named parent and topic-step planning
  updates. The requested Copilot review could not run because of quota
  exhaustion; that remains an external limitation, not an approved review or a
  reason to close the PR loop.
- Current dynamic verification requires a `pre-commit` executable on `PATH`
  and a writable `PRE_COMMIT_HOME`; the historical correction-step evidence
  retains its original machine-local commands.
- Merge remains outside this step and requires the applicable human
  authorization.
