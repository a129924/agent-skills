---
name: python-blueprint-review
description: Review an authored greenfield `blueprint.md` contract against the locked blueprint v1 schema before `python-project-init-greenfield` execution begins.
---

# Purpose
Review an authored greenfield `blueprint.md` and return a contract-quality verdict before executor handoff.

# Trigger / When to use
Use this skill when:
- a drafted greenfield `blueprint.md` already exists and needs review before execution
- the workflow needs a domain-specific check for blueprint v1 section order, exact `Required Skills`, structural locatability, and greenfield lane fit
- the expected output is a review verdict with blocking issues rather than blueprint authoring or project initialization

Do not use this skill when:
- the task is to author or repair the blueprint; use `python-blueprint-authoring`
- the task is to execute a valid blueprint; use `python-project-init-greenfield`
- the task is to review a skill folder, topic plan, or implementation diff
- the repository is clearly retrofit-shaped and needs a retrofit contract instead of greenfield blueprint review

# Inputs
- the target `blueprint.md` path
- the active skill-library root used to validate `Required Skills`
- the locked blueprint v1 review rules already consumed by `python-project-init-greenfield`
- any concrete repository facts needed to judge greenfield-versus-retrofit lane fit

# Process
1. Confirm the task is blueprint-contract review, not authoring, execution, or generic skill-folder review.
2. Read the target `blueprint.md` and all local review references before judging it.
3. Review the blueprint against the locked blueprint v1 contract.
   - Confirm the six required headings exist and stay in the exact order already consumed by `python-project-init-greenfield`.
   - Reject added compatibility aliases, reordered headings, or other schema drift.
4. Check `## Acceptance Criteria` strictly.
    - A fenced `yaml [sensing-assertions]` block must appear immediately under the heading.
    - Treat prose before the fenced block, malformed block structure, or missing `kind` / `target` / `expected` fields as blocking issues.
    - Reject any assertion `kind` outside the blueprint v1 supported subset: `path_exists`, `path_type`, `command_available`.
5. Validate `## Required Skills` against the current library by exact name.
   - Check `.github/skills/<skill-name>/SKILL.md` for every named item.
   - Do not normalize case, `_`, or `-`, and do not accept placeholders or “close enough” aliases.
6. Check locatability and greenfield fit.
   - Require concrete package names, paths, entrypoints, and tool choices where execution depends on them.
   - Treat abstract structure, contradictory locators, or retrofit-style preservation/migration pressure as review failures.
7. Return exactly one JSON object and no trailing prose:
   - `verdict`: `approved` or `needs-rework`
   - `blocking_issues`: array of objects with `issue`, `section`, and `fix`
8. Stop at review.
   - Do not rewrite the blueprint on behalf of the author.
   - Do not execute initialization steps or approve unrelated repository changes.

# Examples
- Positive: Review a drafted greenfield `blueprint.md` whose sections stay in locked v1 order, whose `yaml [sensing-assertions]` block appears immediately under `## Acceptance Criteria`, whose required skills match current-library directory names exactly, and whose structure names `src/weather_service/main.py`; return JSON with `"verdict": "approved"` and an empty `blocking_issues` array.
- Negative: Review a blueprint that uses `python_testing_pytest`, places prose before the fenced sensing block, introduces an unsupported assertion `kind`, says only “modern src layout”, or asks to preserve legacy files, then respond with authoring suggestions or executor actions instead of a blocking review verdict.

# Outputs
- exactly one machine-consumable JSON verdict object
- `verdict`: `approved` or `needs-rework`
- `blocking_issues`: concrete contract failures with the failing section and required fix
- reroute guidance only as part of a blocking issue fix when the blueprint belongs in another lane

# Verification
- confirm the review stays inside blueprint-contract review scope
- confirm the section order is exactly Project Overview -> Required Skills -> Toolchain Expectation -> Structural Invariants -> Quality Thresholds -> Acceptance Criteria
- confirm `## Acceptance Criteria` starts with a parseable `yaml [sensing-assertions]` block
- confirm every sensing assertion includes `kind`, `target`, and `expected`
- confirm every sensing assertion `kind` stays within the v1 supported subset: `path_exists`, `path_type`, `command_available`
- confirm every required skill name matches a real current-library directory name exactly
- confirm structural invariants are concrete and locatable enough for executor consumption without guessing
- confirm retrofit-looking requests are rejected or rerouted instead of absorbed into greenfield approval
- confirm the final output is one JSON object with no prose outside it

# Red Flags
- the blueprint adds or renames headings instead of reusing the locked v1 contract
- acceptance prose appears before the fenced `yaml [sensing-assertions]` block
- the blueprint introduces a sensing assertion `kind` outside `path_exists`, `path_type`, or `command_available`
- a required skill name differs only by case, `_`, or `-` from a real library skill
- `Structural Invariants` contain only phrases such as “clean”, “modern”, or “sensible”
- the blueprint tries to preserve, migrate, or coexist with meaningful legacy files while claiming to be greenfield
- the review response drifts into blueprint authoring or init execution advice

# Common Rationalizations
- “The executor can normalize the skill names later.”
- “The structure is obvious, so abstract wording is fine.”
- “This repo mostly exists already, but greenfield review is close enough.”
- “We can add the sensing block after init works once.”
- “Returning suggestions is enough even if the verdict is missing.”

# Boundaries
- Do not author or repair the blueprint.
- Do not execute `python-project-init-greenfield`.
- Do not invent a new blueprint schema or widen blueprint v1.
- Do not normalize missing or invalid `Required Skills` names.
- Do not tolerate abstract or contradictory locators that the executor would need to guess.
- Do not review skill folders, topic plans, or implementation diffs with this skill.
- Do not emit anything except the single JSON verdict object.

# Local references
- `examples.md`: approved and needs-rework blueprint-review scenarios, including section-order, sensing-block, locatability, and lane-mismatch cases
- `checklist.md`: repeatable higher-risk review checks before returning the final verdict
- `references/blueprint-v1-review-checks.md`: locked section-order, sensing-block placement, and blueprint-v1 schema-alignment review rules
- `references/review-verdict-contract.md`: JSON verdict shape, blocking-issue expectations, and review-output boundaries
- `references/greenfield-fit-and-reroute.md`: greenfield-versus-retrofit review criteria and reroute expectations
- `references/required-skills-and-locatability-checks.md`: exact-name required-skill validation and structural-locatability review checks
