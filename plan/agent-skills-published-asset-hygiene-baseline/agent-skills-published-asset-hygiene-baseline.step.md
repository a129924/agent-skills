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
- [X] pr-feedback-correction-implementation
- [X] pr-feedback-independent-review
- [X] pr-feedback-follow-up-correction-planning
- [X] pr-feedback-follow-up-correction-implementation
- [X] pr-feedback-follow-up-independent-review
- [X] pr-feedback-current-correction-planning
- [X] pr-feedback-current-correction-implementation
- [X] pr-feedback-current-correction-review-routing
- [X] pr-feedback-final-reconciliation-planning
- [X] pr-feedback-final-reconciliation-implementation
- [X] pr-feedback-final-reconciliation-independent-review
- [X] pr-feedback-final-reconciliation-current-truth-replan
- [ ] pr-feedback-final-reconciliation-current-correction-implementation
- [ ] pr-feedback-final-reconciliation-current-correction-independent-review
- [ ] pr-comment-review-and-fix

## Actionable Steps

1. All work through Commit D is completed historical evidence. Commit C changed
   exactly three `version-pinning.md` paths; dependent Commit D changed exactly
   the inventory and Codex provenance records required for that canonical hash.
2. The sole active contract is
   `agent-skills-published-asset-hygiene-baseline.pr-feedback-final-reconciliation-plan.md`.
   Route Commit E's six `git-branch-naming` and `git-commit-convention`
   canonical/projection paths to an independent Implementer; each intended
   `PASS:` Markdown hard break becomes literal `<br>`.
3. Route dependent Commit F's two generated paths to the Implementer after Commit
   E. The deterministic rebuild updates only the two affected canonical hashes
   and their two Codex provenance rows to cite Commit E.
4. Verify the final PR-base classification: 34 hygiene-only published-skill
   assets plus 12 explicit rendering exceptions. The isolated all-files
   temporary workspace must reproduce exactly the 17-path non-skill inventory;
   its diff is never retained in this feature worktree.
5. Route the E6/F2 evidence to an independent Reviewer. Only `approved`
   resumes `pr-comment-review-and-fix`; the Main Agent resolves satisfied
   threads and replies only to unresolved actionable threads.

## Handoff / Gate Notes

- Parent plan is current truth; correction artifacts are historical routing
  truth and do not override it.
- Worktree: `/Users/andrew/code/python/agent-skills.worktrees/agent-20260728-agent-skills-published-asset-hygiene-baseline`
- Branch: `feature/andrew/agent-skills-published-asset-hygiene-baseline`
- Current status: `needs-rework`; Ready PR #120 remains open. Earlier P2
  repairs, Commit A/B, and the completed C3/D2 final-reconciliation route are
  historical. The active route is
  `pr-feedback-final-reconciliation-current-correction-implementation`.
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
- The final reconciliation remains unresolved pending independent implementation
  and review. The requested Copilot review could not run because of quota
  exhaustion; that remains an external limitation, not an approved review or
  a reason to close the PR loop.
- Current dynamic verification requires a `pre-commit` executable on `PATH`
  and a writable `PRE_COMMIT_HOME`; the historical correction-step evidence
  retains its original machine-local commands.
- Commit A/B and C3/D2 inventory/provenance results are completed historical
  evidence. The current correction locks E6/F2, an exact 17-path temporary
  all-files inventory, and a PR-base diff classification of 34 hygiene-only
  assets plus 12 `<br>` exceptions; the consumer-like workspace remains the
  required passing gate.
- Merge remains outside this step and requires the applicable human
  authorization.
