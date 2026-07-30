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
- [ ] final-reconciliation-current-correction-implementation
- [ ] final-reconciliation-current-correction-review
- [ ] pr-comment-review-and-fix

## Actionable Steps

1. Commits C3 and D2 are completed historical evidence: C changed the three
   `version-pinning.md` paths, then D refreshed its inventory and Codex
   provenance record. Do not re-run or reopen them.
2. Route exactly the six Commit E `git-branch-naming` and
   `git-commit-convention` canonical/projection paths to an independent
   Implementer. Each replaces only its intended `PASS:` Markdown hard break
   with `<br>` and synchronizes projections from canonical.
3. After Commit E, route exactly the two Commit F generated paths to that
   Implementer. Rebuild the 57-record inventory deterministically and update only
   the two matching Codex provenance rows to cite Commit E.
4. Validate scoped hooks, `pre-commit validate-config`, `git diff --check`,
   projection equality, the deterministic 57-record inventory/two-row
   provenance result, the consumer-like no-rewrite gate, and the disposable
   exact 17-path all-files inventory.
5. An independent Reviewer verifies the C3/D2 historical boundary, E6/F2
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
  `needs-rework` route owns only E6/F2. The Main Agent resumes PR thread
  handling only after the independent review records `approved`.
