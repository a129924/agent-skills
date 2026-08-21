# Boundary Outcome Design Checklist

Use this checklist before handing off a review or recommendation.

## A. Boundary and vocabulary

- [ ] The observed boundary names both the owning layer and receiving layer.
- [ ] Each alternative's vocabulary owner is identified.
- [ ] No HTTP, SDK, ORM, driver, or transport term survives inward without a
      documented semantic reason.
- [ ] A `Protocol` is not treated as a runtime failure boundary.

## B. Decision relevance

- [ ] Each preserved distinction maps to a different meaningful caller action.
- [ ] Each compressed distinction maps to the same caller action.
- [ ] The recommendation does not collapse meaningful `NotFound`, `Conflict`,
      rate-limit, availability, or other operation distinctions into `Failed`.
- [ ] The recommendation does not mirror lower-layer exceptions one-for-one
      without semantic translation.

## C. State and persistence

- [ ] Optional Domain state has been tested against its own invariant before
      being called invalid.
- [ ] An operation-specific rejection of legal state is placed in the UseCase
      or Domain policy that owns that operation.
- [ ] Repository capability failures and Unit of Work transaction outcomes are
      located at their actual decision boundary.
- [ ] The analysis does not assume all persistence failures occur at commit.

## D. Handoff quality

- [ ] Expected failures have a named consumer decision.
- [ ] Defects, impossible states, and unknown technical failures are not added
      to a Result union merely for completeness.
- [ ] The review output includes observed boundary, potential vocabulary leak,
      decision-relevant distinctions, suggested translation point, suggested
      outcome granularity, and boundary action.
- [ ] Missing evidence is marked `INCOMPLETE`; materially different plausible
      policies are marked `BLOCKED` rather than guessed.
