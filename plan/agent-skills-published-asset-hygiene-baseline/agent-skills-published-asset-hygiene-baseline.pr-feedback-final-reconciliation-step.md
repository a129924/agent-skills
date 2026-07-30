---
topic: agent-skills-published-asset-hygiene-baseline
status: needs-rework
---

# PR #120 Final Reconciliation Steps

## Workflow Stages

- [X] final-reconciliation-planning
- [X] final-reconciliation-implementation
- [X] final-reconciliation-independent-review
- [X] final-reconciliation-current-truth-replan
- [X] final-reconciliation-current-correction-implementation
- [X] final-reconciliation-current-correction-review
- [ ] final-reconciliation-soft-fail-correction-implementation
- [ ] final-reconciliation-soft-fail-correction-review
- [ ] pr-comment-review-and-fix

## Actionable Steps

1. Commits C3/D2 and the completed `PASS:` E6/F2 are historical evidence: C changed the three
   `version-pinning.md` paths, then D refreshed its inventory and Codex
   provenance record. Do not re-run or reopen them.
2. Route exactly the six final Commit E `git-branch-naming` and
   `git-commit-convention` canonical/projection paths to an independent
   Implementer. Each replaces only its intended `SOFT FAIL:` Markdown hard break
   with `<br>` and synchronizes projections from canonical.
3. After final Commit E, route exactly the two Commit F generated paths to that
   Implementer. Rebuild the 57-record inventory deterministically and update only
   the two matching Codex provenance rows to cite the final Commit E.
4. Validate scoped hooks, `pre-commit validate-config`, `git diff --check`,
   projection equality, the deterministic 57-record inventory/two-row
   provenance result, and the consumer-like no-rewrite gate. Do not run
   `pre-commit run --all-files` in the feature worktree; the 17-path inventory
   remains retained disposable-workspace evidence.
5. An independent Reviewer verifies the C3/D2 and completed `PASS:` E6/F2
   historical boundaries, final `SOFT FAIL:` E6/F2
   implementation boundary, and final PR-base classification of 34
   hygiene-only assets plus 12 rendering exceptions. It appends an `approved`
   or `needs-rework` JSON verdict to the review log.
6. Only after `approved` may the Main Agent resume thread handling: resolve
   satisfied threads and post scoped replies only on unresolved actionable
   threads.

## Handoff / Gate Notes

- Parent plan is current truth. This step and its paired final-reconciliation
  plan own the only active correction route; earlier correction files are
  historical and must not be edited.
- The temporary all-files inventory is a test artifact, not a write set.
- No merge or release is authorized by this step.
- The prior final reconciliation is closed historical evidence. This current
  `needs-rework` route owns only the final `SOFT FAIL:` E6/F2. The Main Agent
  resumes PR thread handling and resolves the remaining thread only after the
  independent review records `approved`.
