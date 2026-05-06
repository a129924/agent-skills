---
name: python-retrofit-plan-authoring
description: Author a review-ready Retrofit V2 `retrofit-plan.md` for an existing Python repository, with locked section order, machine-readable migration risk metadata, and strict separation between planning strategy and runtime gate decisions.
complexity: high

risk_profile:
  - ambiguity_sensitive
  - multi_agent_handoff
  - destructive_action

inputs:
  - current repository facts (entrypoints, packages, config surfaces, toolchain remnants)
  - concrete target paths, files, entrypoints, and tool choices for the post-retrofit state
  - known conflict surfaces or destructive candidates the strategy must acknowledge
  - verifiable acceptance targets for yaml [sensing-assertions]
  - lane-fit facts proving this is retrofit work rather than greenfield initialization
  - explicit human clarification when the request is abstract, contradictory, or missing locatable detail

outputs:
  - review-ready Retrofit V2 retrofit-plan.md for an existing Python repository
  - locked section order with machine-readable migration-strategy and sensing-assertions blocks
  - explicit risk metadata that executor can consume without a compatibility layer
  - concrete stop-and-ask feedback when the requested contract is too abstract or misrouted

use_when:
  - an existing Python repository needs a retrofit contract before execution starts
  - the task is to author or repair retrofit-plan.md to the locked Retrofit V2 shape
  - the plan must encode risk_level, destructive_actions, backup_required, and acceptance assertions
  - the workflow needs explicit stop-and-ask handling for abstract, contradictory, or misrouted retrofit requests

do_not_use_when:
  - the repository is greenfield or baseline-only; use python-project-init-greenfield
  - the task is to execute retrofit steps; use python-project-retrofit
  - the task is to review or approve an existing retrofit plan
  - the requested contract lacks concrete paths, concrete tool names, or verifiable targets
---

# Purpose
Turn retrofit intent for an existing Python repository into a review-ready `retrofit-plan.md` that executor skills can consume without reinterpretation.

# Trigger / When to use
Use this skill when:
- an existing Python repository needs a retrofit contract before execution starts
- the task is to author or repair `retrofit-plan.md` to the locked Retrofit V2 shape
- the plan must encode `risk_level`, `destructive_actions`, `backup_required`, and acceptance assertions
- the workflow needs explicit stop-and-ask handling for abstract, contradictory, or misrouted retrofit requests

Do not use this skill when:
- the repository is greenfield or baseline-only; use `python-project-init-greenfield`
- the task is to execute retrofit steps; use `python-project-retrofit`
- the task is to review or approve an existing retrofit plan
- the requested contract lacks concrete paths, concrete tool names, or verifiable targets

# Inputs
- current repository facts such as entrypoints, packages, config surfaces, and toolchain remnants
- concrete target paths, files, entrypoints, and tool choices for the post-retrofit state
- known conflict surfaces or destructive candidates that the strategy must acknowledge
- verifiable acceptance targets for `yaml [sensing-assertions]`
- lane-fit facts proving this is retrofit work rather than greenfield initialization
- explicit human clarification whenever the request is abstract, contradictory, or missing locatable detail

# Process
1. Confirm lane fit first.
   - Use this skill only for existing-repository retrofit planning.
   - If the task is greenfield, route to `python-project-init-greenfield` instead of drafting a retrofit contract.
   - If the task is execution or review, hand off to the executor or reviewer instead of absorbing those roles.
2. Reject abstract inputs early.
   - Require locatable paths, concrete tool names, and verifiable targets.
   - If the request says only “modernize the layout”, “clean it up”, or similar abstract goals, stop and ask.
   - If current facts and requested outcomes contradict each other, stop and ask before drafting.
3. Author the locked Retrofit V2 section order exactly:
   1. `## Survey Summary`
   2. `## Gap Analysis`
   3. `## Target Transformation`
   4. `## Migration Strategy`
   5. `## Acceptance Criteria`
   - Do not emit old headings or compatibility aliases.
4. Write `## Survey Summary` from observable current-state facts only.
   - Name current entrypoints, packages, config files, and structural constraints that matter to retrofit planning.
   - Do not hide missing facts behind generalized prose.
5. Write `## Gap Analysis` with concrete before-versus-target gaps.
   - Call out likely shadow-file conflicts, config-remnant conflicts, and destructive surfaces with exact paths when known.
6. Write `## Target Transformation` as a concrete end-state declaration.
   - Describe desired paths, entrypoints, config outcomes, and toolchain outcomes in locatable terms.
   - `Migration Direction` may appear only as strategy declaration.
   - Do not let `Migration Direction` choose runtime gate answers or authorize deletion, overwrite, or coexistence automatically.
7. Write `## Migration Strategy` with a machine-readable fenced block tagged `yaml [migration-strategy]`.
   - Include at least `risk_level`, `destructive_actions`, and `backup_required`.
   - Classify `risk_level` from observable physical traits, not intuition:
     - `LOW`: pure additions or non-destructive configuration changes
     - `HIGH`: directory reshaping, code relocation, or multiple core-toolchain replacements
   - Reserve `MEDIUM` for future extension only; do not author it in current contracts.
8. Write `## Acceptance Criteria` with a fenced `yaml [sensing-assertions]` block.
   - Each assertion record must include `kind`, `target`, and `expected`.
   - Keep assertions concrete enough for `sense-env-scaffold` to evaluate without guesswork.
9. Run the authoring self-check before handoff.
   - Ensure `LOW` does not hide destructive actions.
   - Ensure the plan will pass the executor-side **Risk Alignment Check** instead of deferring an obvious mismatch downstream.
   - Ensure `destructive_actions` matches the written strategy and target transformation.
   - Ensure old Retrofit V1 headings are gone and no compatibility mapping is implied.
   - Ensure the contract stays within authoring scope and leaves runtime gate choices to the executor.
10. Stop at `review-ready`.
    - Do not approve the plan.
    - Hand it to the reviewer flow once the draft is complete.

# Examples
- Positive: Author a Retrofit V2 `retrofit-plan.md` that names current `app.py`, target `src/weather_service/main.py`, includes `yaml [migration-strategy]` with `risk_level: HIGH`, and leaves runtime delete or move authorization to the executor.
- Negative: Draft a plan that says “modernize the package layout”, uses old `## Project Overview` headings, or marks `LOW` while listing file moves and overwrites.

# Outputs
- a review-ready Retrofit V2 `retrofit-plan.md` for an existing Python repository
- locked section order with machine-readable `migration-strategy` and `sensing-assertions` blocks
- explicit risk metadata that executor can consume without a compatibility layer
- concrete stop-and-ask feedback when the requested contract is too abstract or misrouted

# Validation

## Required Checks
- Locked section order is present exactly: Survey Summary → Gap Analysis → Target Transformation → Migration Strategy → Acceptance Criteria.
- `yaml [migration-strategy]` block contains all three required fields: `risk_level`, `destructive_actions`, and `backup_required`.
- `yaml [sensing-assertions]` block uses only supported assertion kinds: `path_exists`, `path_type`, `command_available`.
- `risk_level` uses only `LOW` or `HIGH`; `MEDIUM` must not appear.

## Quality Checks (best effort)
- `risk_level` is consistent with `destructive_actions`; `LOW` does not list moves, deletes, overwrites, or package relocations.
- All section headings match the V2 contract; no V1 headings such as `## Project Overview` are present.
- Acceptance targets are concrete enough for `sense-env-scaffold` to evaluate without guesswork.
- Strategy text stays within planning scope and does not authorize runtime gate decisions.

## On Soft Fail
- Mark the plan as INCOMPLETE.
- List all missing or non-compliant sections explicitly.
- Do not block output; deliver the best-effort draft with gaps noted.

# Failure Handling

## Missing Context
BLOCKED — if repository structure or migration intent is not provided, stop and ask before drafting. Do not invent paths, tool names, or structural facts.

## Ambiguous Requirement
If `risk_level` cannot be determined from observable physical traits, default to `HIGH` and note the assumption explicitly in the plan.

## Execution Limitation
If the repository cannot be inspected directly, state that limitation clearly in the plan. If target paths or command availability cannot be determined, emit BLOCKED and request the missing information. Do not insert placeholder assertions.

# Verification
- confirm the section order is exactly Survey Summary -> Gap Analysis -> Target Transformation -> Migration Strategy -> Acceptance Criteria
- confirm `yaml [migration-strategy]` and `yaml [sensing-assertions]` blocks are present and parseable
- confirm `risk_level` uses only `LOW` or `HIGH`
- confirm `LOW` plans do not hide destructive actions
- confirm the authored plan is explicit enough for the executor-side Risk Alignment Check
- confirm target paths, tool names, and acceptance targets are concrete and locatable
- confirm strategy text does not replace runtime gate decisions

# Red Flags
- target transformation contains only style words such as “modernize” or “clean up”
- requested toolchain migration has no named source or target files
- `LOW` risk is claimed while moves, deletes, overwrites, or package relocations are planned
- `Migration Direction` is being used to skip human runtime choices
- the request is really a greenfield baseline or an execution task

# Common Rationalizations
- “The executor can infer the exact paths later.”
- “LOW just means we feel comfortable with it.”
- “If the strategy says replace the entrypoint, runtime gates are unnecessary.”
- “Old Retrofit headings are close enough.”
- “Acceptance targets can stay broad because the repo structure is obvious.”

# Boundaries
- Do not execute the retrofit plan.
- Do not approve the authored plan.
- Do not invent missing paths, tool names, or acceptance targets.
- Do not use `Migration Direction` as a substitute for runtime authorization.
- Do not broaden `sense-env-scaffold` assertion kinds.
- Do not author compatibility mappings from old retrofit section names.

# Local references
- `examples.md`: layered Retrofit V2 authoring scenarios, anti-patterns, and stop-and-ask cases
- `checklist.md`: repeatable review-ready checks for higher-risk retrofit-plan authoring
- `references/retrofit-v2-contract.md`: locked section order, block placement, and contract-error rules for Retrofit V2
- `references/migration-strategy-risk-model.md`: `risk_level`, `destructive_actions`, `backup_required`, and alignment rules
- `references/authoring-vs-executor-boundaries.md`: planning-versus-runtime ownership and stop-and-ask triggers
