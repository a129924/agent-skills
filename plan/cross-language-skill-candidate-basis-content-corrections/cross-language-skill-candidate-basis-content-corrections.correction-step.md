---
topic: cross-language-skill-candidate-basis-content-corrections
correction_severity: high
status: planned
parent_plan: plan/cross-language-skill-candidate-basis-content-corrections/cross-language-skill-candidate-basis-content-corrections.plan.md
parent_step: plan/cross-language-skill-candidate-basis-content-corrections/cross-language-skill-candidate-basis-content-corrections.step.md
---

# Cross-Language Skill Candidate Basis Content Corrections — Recovery Steps

## Recovery Stages

- [ ] independent-plan-review
- [ ] approved-six-cell-repair
- [ ] independent-document-review
- [ ] parent-sync-and-planner-closure

## Actionable Steps

### independent-plan-review

- Next actor: independent Plan-Reviewer.
- Confirm the high-severity route, exact four-artifact baseline, six-cell
  future write set, exclusions, semantic warning, role separation, and
  current-truth / historical-truth boundary.

### approved-six-cell-repair

- Entry condition: Plan-Reviewer `approved` handoff.
- Next actor: independent Implementer.
- The repair may edit only the six parent-plan `可攜核心` cells. It must not
  resurrect prior implementation state or create a review-log or summary.

### independent-document-review

- Entry condition: Implementer returns `review-ready`.
- Next actor: independent Reviewer.
- A scope, contract, or workflow finding returns to the owner of the affected
  artifact; it does not weaken the frozen correction direction.

### parent-sync-and-planner-closure

- Entry condition: downstream review passes and any required parent sync is
  complete.
- Next actor: Planner. Only Planner may confirm correction closure; until then,
  this correction is open historical truth.

## Handoff / Gate Notes

- This correction step is historical recovery progression and cannot replace
  the parent plan or parent step.
- No reviewer verdict, review-log, summary, completion claim, publication, or
  candidate-basis edit exists at this baseline stage.
- The next permitted route is independent Plan-Reviewer review.
