---
topic: cross-language-skill-candidate-basis-content-corrections
status: planned
current_plan_input: plan/cross-language-skill-candidate-basis-content-corrections/cross-language-skill-candidate-basis-content-corrections.plan.md
---

# Cross-Language Skill Candidate Basis Content Corrections Steps

## Workflow Stages

- [ ] independent-plan-review
- [ ] bounded-six-cell-implementation
- [ ] independent-document-review
- [ ] phase-4.5-alignment
- [ ] commit-push-pr
- [ ] human-review-and-merge-handoff

## Actionable Steps

### independent-plan-review

- Next actor: independent Plan-Reviewer.
- Review the parent plan and step together with the correction plan and
  correction step. Return the single required JSON handoff.
- No candidate-basis modification may start unless the verdict is `approved`.

### bounded-six-cell-implementation

- Entry condition: independent Plan-Reviewer `approved` handoff.
- Next actor: independent Implementer.
- Change only the six frozen `可攜核心` cells in
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
- No review-log or summary exists. Neither may be created until its own
  routing or close gate first requires an exact path in the parent plan.
- The next permitted handoff is independent Plan-Reviewer only.
