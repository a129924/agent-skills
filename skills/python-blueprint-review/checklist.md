# Python Blueprint Review Checklist

Use this checklist before returning a verdict for an authored greenfield
`blueprint.md`.

- [ ] The task is really blueprint review, not authoring, execution, retrofit planning, or skill-folder review.
- [ ] The review stays text-first and does not require a fixed heading order or exact schema placement.
- [ ] The blueprint clearly covers project purpose or overview.
- [ ] The blueprint clearly defines capability requirements rather than vague dependency wishes.
- [ ] The blueprint states toolchain expectations concretely enough to implement.
- [ ] The blueprint provides concrete structure, locators, and invariants where implementation depends on them.
- [ ] Structural claims are internally consistent and locatable; abstract phrases like `modern layout` were treated as blocking issues.
- [ ] Quality thresholds are present and specific enough to review.
- [ ] Acceptance criteria define observable or verifiable outcomes, not only aspirations.
- [ ] No required design dimension is missing, contradictory, placeholder-filled, or vague enough to force downstream guessing.
- [ ] Greenfield-only lane fit is still true; migration, preservation, or retrofit pressure was not silently absorbed.
- [ ] The verdict reports blocking issues instead of rewriting the blueprint on the reviewer's behalf.
- [ ] The final output is exactly one JSON object using the local verdict contract.
