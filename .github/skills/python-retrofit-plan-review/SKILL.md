---
name: python-retrofit-plan-review
description: Review an authored Retrofit V2 `retrofit-plan.md` contract against the locked section order, machine-readable risk metadata, supported sensing assertion kinds, authoring-versus-executor boundaries, and locatability before `python-project-retrofit` execution begins.
complexity: high

risk_profile:
  - ambiguity_sensitive
  - multi_agent_handoff
  - destructive_action

inputs:
  - the target `retrofit-plan.md` path
  - the locked Retrofit V2 review rules already consumed by `python-project-retrofit`
  - the current supported `sense_env.py` assertion-kind subset
  - any concrete repository facts needed to judge retrofit-versus-greenfield lane fit
  - the authored contract text needed to assess risk alignment, runtime-boundary violations, and locatability

outputs:
  - exactly one machine-consumable JSON verdict object with `verdict` and `blocking_issues`

use_when:
  - a drafted Retrofit V2 `retrofit-plan.md` already exists and needs review before execution
  - the workflow needs a domain-specific check for locked section order, `migration-strategy` validity, supported sensing assertion kinds, risk alignment, and locatability
  - the expected output is a review verdict with blocking issues rather than plan authoring or retrofit execution

do_not_use_when:
  - the task is to author or repair the retrofit plan; use `python-retrofit-plan-authoring`
  - the task is to execute a valid retrofit plan; use `python-project-retrofit`
  - the task is to review a skill folder, topic plan, or implementation diff
  - the repository is greenfield or baseline-only and needs the blueprint lane instead of retrofit-plan review
---

# Purpose
Review an authored Retrofit V2 `retrofit-plan.md` and return a contract-quality verdict before executor handoff.

# Trigger / When to use
Use this skill when:
- a drafted Retrofit V2 `retrofit-plan.md` already exists and needs review before execution
- the workflow needs a domain-specific check for locked section order, `migration-strategy` validity, supported sensing assertion kinds, risk alignment, and locatability
- the expected output is a review verdict with blocking issues rather than plan authoring or retrofit execution

Do not use this skill when:
- the task is to author or repair the retrofit plan; use `python-retrofit-plan-authoring`
- the task is to execute a valid retrofit plan; use `python-project-retrofit`
- the task is to review a skill folder, topic plan, or implementation diff
- the repository is actually greenfield or baseline-only and needs the blueprint lane instead of retrofit-plan review

# Inputs
- the target `retrofit-plan.md` path
- the locked Retrofit V2 review rules already consumed by `python-project-retrofit`
- the current supported `sense_env.py` assertion-kind subset
- any concrete repository facts needed to judge retrofit-versus-greenfield lane fit
- the authored contract text needed to assess risk alignment, runtime-boundary violations, and locatability

# Process
1. Confirm the task is Retrofit V2 contract review only.
   - Reject authoring, execution, skill-folder review, topic-plan review, and implementation-diff review.
   - If the contract is really greenfield-shaped or belongs in another lane, return a blocking reroute instead of absorbing the job.
2. Read the target `retrofit-plan.md` and all local review references before judging it.
3. Review the authored plan against the locked Retrofit V2 heading contract.
   - Confirm the required headings exist and stay in this exact order:
     1. `## Survey Summary`
     2. `## Gap Analysis`
     3. `## Target Transformation`
     4. `## Migration Strategy`
     5. `## Acceptance Criteria`
   - Reject missing headings, reordered headings, old-heading compatibility attempts, or mixed heading sets.
4. Validate `## Migration Strategy` strictly.
   - Require a parseable fenced `yaml [migration-strategy]` block.
   - Require at least `risk_level`, `destructive_actions`, and `backup_required`.
   - Allow only `LOW` or `HIGH` for `risk_level`; block `MEDIUM` and any other unsupported value.
   - Require `destructive_actions` to stay a YAML sequence, even when empty.
   - Require `backup_required` to be the YAML boolean `true` or `false`.
   - Treat the YAML block as the execution-facing source of truth; prose must not override it.
5. Validate `## Acceptance Criteria` strictly.
   - Require a parseable fenced `yaml [sensing-assertions]` block.
   - Require every assertion record to include `kind`, `target`, and `expected`.
   - Allow only `path_exists`, `path_type`, and `command_available`.
   - Reject malformed assertions, unsupported kinds, or attempts to widen the current `sense_env.py` contract.
6. Run risk, boundary, and locatability checks across the full contract.
   - Fail `LOW` plans whose target transformation, migration prose, or destructive surfaces imply moves, deletes, overwrites, reshaping, or toolchain replacement.
   - Fail destructive plans whose `destructive_actions` list is empty or incomplete for the written strategy.
   - Reject language that uses planning prose as if it already chose runtime outcomes such as `move`, `delete`, `coexist`, `migrate`, `preserve`, or destructive authorization.
   - Require concrete source paths, target paths, entrypoints, config surfaces, and tool names instead of abstract phrases.
7. Return exactly one JSON object and no trailing prose:
   - `verdict`: `approved` or `needs-rework`
   - `blocking_issues`: array of objects with `issue`, `section`, and `fix`
8. Stop at review.
   - Do not rewrite the retrofit plan on behalf of the author.
   - Do not execute retrofit steps.
   - Do not broaden the schema, supported risk values, or supported assertion kinds.

# Examples
- Positive: Review a drafted `retrofit-plan.md` that uses the locked Retrofit V2 order, contains valid `yaml [migration-strategy]` and `yaml [sensing-assertions]` blocks, keeps `LOW` plans additive or `HIGH` plans explicitly destructive, names concrete paths such as `app.py` and `src/weather_service/main.py`, and return JSON with `"verdict": "approved"` when no blocking issues remain.
- Negative: Approve a plan that uses old headings, sets `risk_level: MEDIUM`, lists `config_key_exists` in `yaml [sensing-assertions]`, says only “modernize the layout”, treats `Migration Direction` as permission to delete files automatically, or responds with rewritten plan text instead of a JSON verdict.

# Outputs
- exactly one machine-consumable JSON verdict object
- `verdict`: `approved` or `needs-rework`
- `blocking_issues`: concrete contract failures with the failing section and required fix
- reroute guidance only as part of a blocking issue fix when the plan belongs in another lane

# Validation

## Required Checks
- `retrofit-plan.md` is provided and its path is readable
- locked Retrofit V2 section order is intact: Survey Summary → Gap Analysis → Target Transformation → Migration Strategy → Acceptance Criteria
- `## Migration Strategy` contains a parseable fenced `yaml [migration-strategy]` block with `risk_level`, `destructive_actions`, and `backup_required`; `risk_level` is `LOW` or `HIGH` only; `destructive_actions` is a YAML sequence; `backup_required` is a YAML boolean
- `## Acceptance Criteria` contains a parseable fenced `yaml [sensing-assertions]` block; every assertion record includes `kind`, `target`, and `expected`; every `kind` value is within `path_exists`, `path_type`, or `command_available`

## Quality Checks (best effort)
- `risk_level` is consistent with the `destructive_actions` list (e.g., `LOW` plans should not list moves, deletes, or overwrites)
- no `TBD`, placeholder text, or abstract wording appears in contract-critical fields such as source paths, target paths, entrypoints, or tool names

## On Soft Fail
- mark review as INCOMPLETE
- return `verdict: needs-rework` with `blocking_issues` populated for each failing check
- list each missing or malformed section explicitly so the author knows exactly what to repair

# Failure Handling

## Missing Context
- BLOCKED — if `retrofit-plan.md` is not provided or cannot be read, stop and ask for the correct path before proceeding; do not attempt a partial review against an absent or unreadable contract

## Ambiguous Requirement
- if a section is present but its content is ambiguous on a non-schema dimension (e.g., prose wording is unclear but structurally compliant), record it as a non-blocking observation in a `blocking_issues` entry with `"issue": "WARNING: <description>"` so executors can distinguish it from hard failures
- block only when the ambiguity directly violates a schema rule (e.g., unreadable YAML block, unsupported assertion kind, missing required field)

## Execution Limitation
- if `yaml [sensing-assertions]` references file paths or commands that cannot be verified in the current environment, note the limitation explicitly in the verdict; assess schema compliance only and do not fabricate runtime verification results
- do not infer missing YAML fields from prose context; require them to be present in the fenced block

# Verification
- confirm the review stays inside authored `retrofit-plan.md` contract review scope
- confirm the section order is exactly Survey Summary -> Gap Analysis -> Target Transformation -> Migration Strategy -> Acceptance Criteria
- confirm `## Migration Strategy` contains a parseable `yaml [migration-strategy]` block with supported `risk_level`, sequence `destructive_actions`, and boolean `backup_required`
- confirm `## Acceptance Criteria` contains a parseable `yaml [sensing-assertions]` block and every assertion includes `kind`, `target`, and `expected`
- confirm every sensing assertion `kind` stays within `path_exists`, `path_type`, or `command_available`
- confirm `LOW` is not contradicted by destructive reality and destructive plans do not hide or truncate `destructive_actions`
- confirm planning prose does not pre-authorize runtime gate answers owned by `python-project-retrofit`
- confirm paths, entrypoints, config surfaces, and tool names are concrete and locatable enough for executor handoff without guesswork
- confirm wrong-lane requests are rejected or rerouted instead of absorbed
- confirm the final output is exactly one JSON object using the local verdict contract

# Red Flags
- the plan adds, renames, or reorders Retrofit V2 headings
- `risk_level` is `MEDIUM` or any value outside `LOW` / `HIGH`
- `destructive_actions` is missing, not a sequence, or too incomplete for the written destructive scope
- `yaml [sensing-assertions]` contains a kind outside `path_exists`, `path_type`, or `command_available`
- `Migration Direction` or similar prose is being treated as runtime consent
- target transformation uses phrases such as “modernize”, “clean up”, or “reorganize” without concrete locators
- the review response drifts into authoring or execution instead of verdict-only review

# Common Rationalizations
- “`MEDIUM` is close enough until execution decides.”
- “The executor can infer the missing destructive actions later.”
- “If the plan says replace the old entrypoint, Gate 1 choices are already decided.”
- “The target structure is obvious, so abstract wording is fine.”
- “Adding a new sensing assertion kind in review is harmless.”
- “Suggestions are enough even if the output is not valid JSON.”

# Boundaries
- Do not author or repair the retrofit plan.
- Do not execute `python-project-retrofit`.
- Do not invent a new Retrofit schema or compatibility layer.
- Do not tolerate unsupported `risk_level` values or unsupported sensing assertion kinds.
- Do not let planning prose substitute for runtime gate choices.
- Do not accept abstract or contradictory locators that the executor would need to guess.
- Do not review skill folders, topic plans, or implementation diffs with this skill.
- Do not emit anything except the single JSON verdict object.

# Local references
- `examples.md`: approved and needs-rework retrofit-plan review scenarios, including schema, risk, boundary, locatability, and lane-mismatch cases
- `checklist.md`: repeatable higher-risk review checks before returning the final verdict
- `references/retrofit-v2-review-checks.md`: locked section-order, machine-readable block, and supported-schema review rules for Retrofit V2
- `references/review-verdict-contract.md`: JSON verdict shape, blocking-issue expectations, and review-output boundaries
- `references/risk-boundary-and-locatability-checks.md`: risk-alignment review rules, authoring-versus-executor boundaries, and locatability checks
- `references/lane-fit-and-reroute.md`: retrofit-lane fit criteria and reroute expectations for wrong-lane requests
