---
topic: agent-skills-published-asset-hygiene-baseline
status: complete
---

# PR #120 Final Reconciliation Steps

## Workflow Stages

- [X] final-reconciliation-planning
- [X] final-reconciliation-implementation
- [X] final-reconciliation-independent-review
- [ ] pr-comment-review-and-fix

## Actionable Steps

1. An independent Implementer changes only the three locked
   `version-pinning.md` paths, replacing the intentional Markdown hard break
   with `<br>` and synchronizing projections from canonical.
2. Validate the targeted hook run, `pre-commit validate-config`, `git diff
   --check`, exact projection equality, and the consumer-like no-rewrite gate.
3. In a disposable baseline Git workspace, reproduce exactly the 17-path
   expected non-skill all-files inventory and discard that workspace. Confirm
   the feature worktree has no diff for those paths.
4. An independent Reviewer verifies the three-path boundary and final
   PR-base classification (40 hygiene-only assets and six `<br>` exception
   assets). It appends an `approved` or `needs-rework` JSON verdict to the
   review log.
5. Only after `approved` may the Main Agent resume thread handling: resolve
   satisfied threads and post scoped replies only on unresolved actionable
   threads.

## Handoff / Gate Notes

- Parent plan is current truth. This step and its paired final-reconciliation
  plan own the only active correction route; earlier correction files are
  historical and must not be edited.
- The temporary all-files inventory is a test artifact, not a write set.
- No merge or release is authorized by this step.
- Final reconciliation is closed: the independent Reviewer recorded
  `approved` in the review log. The Main Agent now owns PR thread handling;
  only a new actionable thread may open a new bounded correction route.
