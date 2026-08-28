---
topic: cross-language-skill-candidate-basis-content-corrections
status: approved
current_plan_input: plan/cross-language-skill-candidate-basis-content-corrections/cross-language-skill-candidate-basis-content-corrections.plan.md
---

# Cross-Language Skill Candidate Basis Content Corrections Steps

## Workflow Stages

- [x] independent-plan-review
- [ ] bounded-six-cell-implementation
- [ ] independent-document-review
- [ ] phase-4.5-alignment
- [ ] commit-push-pr
- [ ] human-review-and-merge-handoff

## Actionable Steps

### independent-plan-review

- Completed by: independent Plan-Reviewer.
- Recovery baseline reviewed:
  `a725e71fd8cbe9ce6fb35fbf85ac7e250f878feb`.
- Result: `approved`, preserved verbatim in the plan-review log.

### bounded-six-cell-implementation

- Entry condition: independent Plan-Reviewer `approved` handoff.
- Next actor: independent Implementer.
- First commit the plan-review record and synchronized progression, then
  change only the six frozen `可攜核心` cells in
  `docs/agent-skills-convergence/cross-language-candidate-basis.md`.

### independent-document-review

- Entry condition: Implementer returns `review-ready`.
- Next actor: independent Reviewer.
- Verify the six-cell write boundary, all locked text semantics, 11 candidates,
  four groups, five excluded rows, evidence, appendices, names, and paths.

### phase-4.5-alignment

- Entry condition: independent Reviewer `approved` handoff.
- Main Agent checks that the approved draft still matches the parent current-
  truth contract. Drift routes to the owning role; no role may self-approve.

### commit-push-pr

- Entry condition: alignment passes and STOP POINT 1 is explicitly authorized.
- Main Agent alone performs the bounded publication route. This baseline does
  not authorize commit, push, PR, force-push, merge, or release.

### human-review-and-merge-handoff

- Stop at the human PR-review / merge boundary. After merge, STOP POINT 2
  requires new explicit human resume; no release work applies.

## Handoff / Gate Notes

- Parent plan is current truth; this step is progression truth only.
- Correction artifacts preserve high-severity recovery history only and do not
  approve work or replace the parent contract.
- The plan-review log exists solely for the completed Plan-Reviewer gate. No
  summary exists and none may be created before its own topic-close gate adds
  an exact parent-plan path.
- The next permitted handoff is independent Implementer only.
