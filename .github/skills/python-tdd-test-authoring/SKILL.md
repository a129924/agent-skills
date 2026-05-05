---
name: python-tdd-test-authoring
description: Create RED tests from an approved Python implementation plan before implementation begins. Use this when a plan is approved and a behavior-change classifier detects a non-trivial change requiring test coverage.
---

# Purpose

Create RED (failing) tests from an approved implementation plan, mapping all requirements to test cases before implementation starts. Output a 3-verdict YAML result: `red-tests-ready`, `needs-rework`, or `insufficient-context`.

# Trigger / When to use

Use this skill when:
- an implementation plan is approved and ready for test authoring
- the D1 behavior-change classifier detects a non-trivial change (not doc-only, config-only, or trivial modification)
- existing test structure exists and can be extended with new RED tests
- you have validated that production code is not modified (only tests are added)

Do not use this skill when:
- the plan is not yet approved
- the classifier decision is `trivial` or `skip_with_reason`
- production code has already been modified (test authoring must happen first)
- plan context is insufficient to map requirements to test cases
- test structure does not exist or cannot be determined

# Inputs

- approved `plan.md` with clear Requirements section
- existing test structure (test file layout, test naming conventions, helper utilities)
- D1 classifier output (behavior-change verdict)
- validation commands that can verify test status (e.g., `pytest --collect-only`)
- evidence that production code is NOT modified yet

# Process

1. **Verify prerequisites**: Confirm plan is approved, D1 verdict is not `trivial`, and no production code modified.
2. **Classify behavior change**: Run D1 classifier to confirm non-trivial change type (e.g., feature, bug fix, refactor).
3. **Map requirements to tests**: Extract all Requirements from plan.md and create a test_mapping list with (requirement_id → test_case_name).
4. **Check existing tests**: Query test structure for `expected_initial_status` (pass, skip, xfail, or red).
5. **Validate public contract coverage**: Ensure tests cover all public functions, return types, error cases, and documented behavior.
6. **Verify 5 test categories present**: Assert coverage across (1) happy path, (2) error/exception cases, (3) boundary/edge cases, (4) state/side effects, (5) integration points.
7. **Set expected_initial_status**: Decide whether tests should start as red (fail), xfail, or skip based on implementation readiness.
8. **Enforce production_code_modified guard**: Verify `production_code_modified: false` before proceeding.
9. **Build output YAML**: Construct 3-verdict result with verdict, test_mapping, validation checks, and next_step.
10. **Return verdict**: One of `red-tests-ready` (all checks pass), `needs-rework` (fixable gaps), or `insufficient-context` (plan gaps).

# Examples

- **Positive**: Plan with clear Requirements (feature, two bug fixes, refactor), D1 says non-trivial, tests map to all requirements, coverage includes happy path + 3 error cases + boundary case + state assertion + endpoint mock, expected_initial_status is red, production code unmodified → verdict: `red-tests-ready`.
- **Negative (trivial skip)**: D1 classifier says `skip_with_reason: doc_only` → verdict is not an error; return `skip_with_reason` with explanation.

# Outputs

- YAML 3-verdict result file with schema:
  - `verdict: "red-tests-ready" | "needs-rework" | "insufficient-context" | "skip_with_reason"`
  - `test_mapping: [{requirement_id, test_case_name, coverage_category}]`
  - `validation_checks: {d1_decision, requirements_mapped, public_contract_coverage, test_categories_present, expected_initial_status, production_code_modified}`
  - `issues: []` (list of specific gaps or failures)
  - `next_step: string` (e.g., "Proceed to implementation" or "Fix test_mapping for Req#2")

# Verification

- Confirm D1 classifier decision matches verdict path (non-trivial → proceed; trivial → skip).
- Count test functions to verify 5 categories present (happy, errors, boundary, state, integration).
- Validate test_mapping cardinality: at least one test per requirement.
- Confirm `production_code_modified: false` in all cases.
- Query test file for expected_initial_status and assertion count.

# Red Flags

- Plan missing Requirements section or requirements are vague (insufficient-context).
- D1 verdict is `trivial` but skill is invoked anyway (boundary violation).
- Production code has been modified (hard constraint violated; abort immediately).
- Fewer than 5 test categories found (needs-rework).
- Tests map to fewer requirements than listed in plan (incomplete coverage).

# Common Rationalizations

- "D1 says it's a trivial change, can we skip?": Yes, return `skip_with_reason` with D1 verdict; this is a valid outcome, not an error.
- "Some requirements don't have obvious test cases": Needs-rework; add at least one test per requirement or clarify requirement.
- "Test file doesn't exist yet": That's OK; create the file structure and set expected_initial_status to red; still red-tests-ready if coverage is complete.
- "Production code is already half-written": Stop; this violates the hard constraint. Test authoring must happen first.

# Boundaries

- **Hard constraint 1: Never modify production code.** Test authoring happens first; violation → abort with error.
- **Hard constraint 2: D1 classifier decision gates the verdict.** If D1 says `trivial` or `skip_with_reason`, honor it; do not override.
- **Hard constraint 3: Test mapping must be complete.** Every requirement must have at least one test; partial coverage → needs-rework.
- **Hard constraint 4: Expected initial status must be set.** Verdict must declare whether tests start red, xfail, skip, or pass (for pass_existing case); absence → needs-rework.

# Local references

- `examples.md`: 5 detailed scenarios (non_trivial → red-tests-ready, trivial → skip, pass_existing case, needs-rework, insufficient-context) with full inputs/outputs.
- `checklist.md`: 9-item repeatable verification checklist (D1 decision, requirements mapped, public contract, test categories, expected_initial_status, production_code_modified guard, test file structure, YAML schema, boundaries enforced).
- `references/behavior-change-classifier.md`: D1 classifier rules and examples (non-trivial vs. trivial, feature vs. bug fix, when to skip).
- `references/codebase-evidence-levels.md`: D2 evidence classification (insufficient, minimal, sufficient context to author tests).
- `references/atomic-commit-order.md`: Commit sequencing rules (test-first, atomic requirements, enforcement modes).
