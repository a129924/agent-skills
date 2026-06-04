# Python Blueprint Authoring Checklist

Use this checklist before handing a draft to reviewer.

- [ ] The task is really greenfield blueprint authoring, not retrofit planning, execution, or review.
- [ ] The draft stays inside the existing blueprint v1 contract and adds no new headings or compatibility aliases.
- [ ] The section order is exactly:
  - [ ] `## Project Overview`
  - [ ] `## Required Skills`
  - [ ] `## Toolchain Expectation`
  - [ ] `## Structural Invariants`
  - [ ] `## Quality Thresholds`
  - [ ] `## Acceptance Criteria`
- [ ] `## Required Skills` uses exact current-library directory names.
- [ ] No required or optional skill name was normalized for case, `_`, or `-`.
- [ ] Any missing named skill triggered stop-and-ask instead of a placeholder or substitution.
- [ ] `## Toolchain Expectation` names concrete tools and versions when they matter.
- [ ] `## Structural Invariants` uses concrete package names, paths, and entrypoints.
- [ ] Abstract or non-locatable structure triggered stop-and-ask instead of guessed drafting.
- [ ] Contradictory structure details triggered clarification before handoff.
- [ ] `## Acceptance Criteria` contains a parseable `yaml [sensing-assertions]` block immediately under the heading.
- [ ] Every sensing assertion includes `kind`, `target`, and `expected`.
- [ ] Acceptance targets are concrete enough for `sense-env-scaffold` to evaluate without reinterpretation.
- [ ] Lane mismatch rerouted to retrofit authoring or greenfield execution instead of being absorbed.
- [ ] The draft stays upstream-authoring-only and does not change executor behavior.
- [ ] The handoff stops at `review-ready` and does not self-approve.
