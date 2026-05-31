---
name: python-blueprint-review
description: Review an authored greenfield `blueprint.md` as a portable design baseline and return a machine-consumable verdict about clarity, locatability, verifiability, and greenfield fit.
---

# Purpose
Review an authored greenfield `blueprint.md` and decide whether it is specific,
complete, and verifiable enough to serve as a portable design baseline without
downstream guesswork.

# When to use
Use this skill when:
- a drafted greenfield `blueprint.md` already exists and needs review
- the workflow needs a domain-specific check for design completeness, structural locatability, acceptance verifiability, and greenfield lane fit
- the expected output is a review verdict with blocking issues rather than blueprint authoring or execution

Do not use this skill when:
- the task is to author or repair the blueprint; use `python-blueprint-authoring`
- the task is to execute a blueprint
- the task is to review a skill folder, topic plan, or implementation diff
- the repository is clearly retrofit-shaped and needs a retrofit contract instead of greenfield blueprint review

# Inputs
- the target `blueprint.md` path
- the authored blueprint text
- any concrete repository facts needed to judge greenfield-versus-retrofit lane fit

# Review basis
Review is `blueprint-text first` with limited fit checks.

The blueprint does not need a fixed heading order or exact schema shape. It does
need to cover these review dimensions clearly enough that a downstream builder
would not need to guess:
- purpose or project overview
- capability requirements
- toolchain expectation
- structure, locators, or invariants
- quality thresholds
- acceptance or verification shape

The reviewer may additionally reject:
- obvious retrofit-looking or migration-looking work
- contradictory or non-locatable structure claims
- acceptance criteria that are aspirational but not observable

The reviewer must not:
- require a locked heading order
- require a specific fenced YAML block or exact placement
- validate skill names by exact directory match
- act as an execution gatekeeper or handoff router

# Process
1. Confirm the task is blueprint review, not authoring, execution, or generic skill-folder review.
2. Read the target `blueprint.md` and local review references before judging it.
3. Review the blueprint text against the six design dimensions.
   - Accept different section names or ordering when the content is still clear.
   - Treat missing dimensions, unresolved placeholders, or vague prose as blocking issues when downstream implementation would require guessing.
4. Check capability requirements.
   - Require the blueprint to state what capabilities or dependencies are needed.
   - Do not require exact current-library skill-name matches.
   - Reject capability requirements that stay abstract enough that the author's intended dependency surface cannot be inferred safely.
5. Check structure and locatability.
   - Require concrete package names, filesystem paths, entrypoints, interfaces, or equivalent locators where implementation depends on them.
   - Reject contradictory, abstract, or non-locatable structure claims.
6. Check acceptance and verification shape.
   - Require observable, testable, or otherwise verifiable outcomes.
   - Accept prose, lists, tables, or machine-readable blocks when they are concrete.
   - Reject acceptance language that is only aspirational, aesthetic, or subjective without observable outcomes.
7. Check greenfield lane fit.
   - Reject preservation, migration, coexistence, or retrofit pressure as a lane mismatch.
   - Limited fit checking is enough; do not expand into full repository forensics unless the request already surfaces those facts.
8. Return exactly one JSON object and no trailing prose:
   - `verdict`: `approved` or `needs-rework`
   - `blocking_issues`: array of objects with `issue`, `section`, and `fix`
9. Stop at review.
   - Do not rewrite the blueprint on behalf of the author.
   - Do not execute initialization steps or reshape the request into another workflow.

# Outputs
- exactly one machine-consumable JSON verdict object
- `verdict`: `approved` or `needs-rework`
- `blocking_issues`: concrete design-review failures with the failing section or dimension and required fix
- reroute guidance only as part of a blocking issue fix when the blueprint belongs in another lane

# Validation
- `blueprint.md` is provided and locatable before review begins
- the blueprint text covers all six review dimensions clearly enough for downstream implementation without guessing
- capability requirements are concrete enough to understand the intended dependency or tooling surface
- structure and locators are concrete, internally consistent, and implementable
- acceptance criteria define observable or verifiable outcomes
- no placeholder values remain in required design details
- the blueprint remains within a greenfield lane rather than preservation, migration, or coexistence work

# Failure handling
- BLOCKED: if `blueprint.md` is not provided or cannot be located at the stated path, stop and ask for the correct path before proceeding; do not attempt a partial review
- if a section is structurally present but still leaves implementation-critical interpretation open, record it as a blocking issue with a concrete `fix`; do not downgrade implementation-blocking ambiguity to a warning
- if local reference files cannot be read, note the limitation explicitly in the verdict and proceed using the review rules embedded in this `SKILL.md`

# Verification
- confirm the review stays inside blueprint review scope
- confirm the blueprint covers purpose, capability requirements, toolchain expectation, structure or locators, quality thresholds, and acceptance or verification shape
- confirm capability requirements are concrete enough to act on without guessing
- confirm structural claims are locatable and mutually consistent
- confirm acceptance outcomes are observable or otherwise verifiable
- confirm retrofit-looking requests are rejected instead of absorbed into greenfield approval
- confirm the final output is one JSON object with no prose outside it

# Boundaries
- Do not author or repair the blueprint.
- Do not execute the blueprint.
- Do not require a fixed heading order or exact schema placement.
- Do not require exact current-library skill-name matches.
- Do not invent missing capabilities, locators, or acceptance criteria for the author.
- Do not absorb mixed greenfield and retrofit requests into approval.
- Do not review skill folders, topic plans, or implementation diffs with this skill.
- Do not emit anything except the single JSON verdict object.

# Local references
- `examples.md`: approved and needs-rework blueprint-review scenarios, including abstract structure, non-verifiable acceptance, and lane-mismatch cases
- `checklist.md`: repeatable higher-risk review checks before returning the final verdict
- `references/blueprint-v1-review-checks.md`: blueprint-text-first review dimensions and common failure patterns
- `references/review-verdict-contract.md`: JSON verdict shape, blocking-issue expectations, and review-output boundaries
- `references/greenfield-fit-and-reroute.md`: greenfield-versus-retrofit review criteria and reroute expectations
- `references/required-skills-and-locatability-checks.md`: capability-requirement clarity and structural-locatability review checks
