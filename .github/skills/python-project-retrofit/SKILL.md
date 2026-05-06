---
name: python-project-retrofit
description: Retrofit an existing Python repository from a locked Retrofit V2 `retrofit-plan.md`, with risk-alignment blocking, mandatory human gates, destructive preview for HIGH-risk plans, and acceptance handoff through `sense_env.py`.
complexity: high
risk_profile:
  - destructive_action
  - multi_agent_handoff
  - code_modification
inputs:
  - target repository root
  - locked Retrofit V2 retrofit-plan.md path
  - current filesystem state, including existing entrypoints, packages, and config remnants
  - current Git working-tree state before any move, deletion, or overwrite
  - parsed yaml [migration-strategy] fields: risk_level, destructive_actions, and backup_required
  - explicit human decisions for Gate 1 and Gate 2, plus any HIGH-risk destructive authorization when a clean or backed-up path is ready
  - provenance destination at .github/skills-provenance.json
outputs:
  - existing Python project restructured to the approved Retrofit V2 target
  - explicit human gate outcomes for shadow files, implicit configs, and destructive paths
  - Sensing Delta Report JSON artifact with before/after facts and MOVED / CREATED / MODIFIED / DELETED operations
  - provenance recorded in .github/skills-provenance.json
  - acceptance handoff result or a concrete blocking error
use_when:
  - an existing Python repository already has an approved Retrofit V2 retrofit-plan.md
  - the task is to execute retrofit work rather than author the retrofit contract
  - the workflow must detect shadow files, mine implicit configuration remnants, enforce risk alignment, and emit a Sensing Delta Report before acceptance
  - the retrofit must hand off immediately to sense-env-scaffold acceptance via sense_env.py
do_not_use_when:
  - the repository is greenfield or baseline-only; use python-project-init-greenfield
  - retrofit-plan.md is missing, malformed, still under negotiation, or still uses pre-V2 headings
  - the task is to author or review the retrofit plan itself
  - the user expects the agent to auto-merge conflicting config files or guess through ambiguous structure changes
---

# Purpose
Execute a Retrofit V2 `retrofit-plan.md` against an existing Python project without losing human control over conflicts, destructive actions, risk mismatches, or acceptance.

# Trigger / When to use
Use this skill when:
- an existing Python repository already has an approved Retrofit V2 `retrofit-plan.md`
- the task is to execute retrofit work rather than author the retrofit contract
- the workflow must detect shadow files, mine implicit configuration remnants, enforce risk alignment, and emit a Sensing Delta Report before acceptance
- the retrofit must hand off immediately to `python3 .github/skills/sense-env-scaffold/scripts/sense_env.py --mode acceptance --contract-file retrofit-plan.md`

Do not use this skill when:
- the repository is greenfield or baseline-only; use `python-project-init-greenfield`
- `retrofit-plan.md` is missing, malformed, still under negotiation, or still uses pre-V2 headings
- the task is to author or review the retrofit plan itself
- the user expects the agent to auto-merge conflicting config files or guess through ambiguous structure changes

# Inputs
- the target repository root
- the locked Retrofit V2 `retrofit-plan.md` path
- the current filesystem state, including existing entrypoints, packages, and config remnants
- current Git working-tree state before any move, deletion, or overwrite
- the parsed `yaml [migration-strategy]` fields: `risk_level`, `destructive_actions`, and `backup_required`
- explicit human decisions for Gate 1 and Gate 2, plus any HIGH-risk destructive authorization when a clean or backed-up path is ready
- the provenance destination at `.github/skills-provenance.json`

# Process
1. Confirm retrofit fit and parse the Retrofit V2 contract first.
   - Read `retrofit-plan.md`.
   - Require this exact heading order:
     1. `## Survey Summary`
     2. `## Gap Analysis`
     3. `## Target Transformation`
     4. `## Migration Strategy`
     5. `## Acceptance Criteria`
   - Require a parseable ````yaml [migration-strategy]```` block under `## Migration Strategy`.
   - Require a parseable ````yaml [sensing-assertions]```` block under `## Acceptance Criteria`.
   - Reject old headings or compatibility mapping instead of guessing.
2. Validate the machine-readable risk metadata before touching the workspace.
   - Require `risk_level`, `destructive_actions`, and `backup_required`.
   - Allow only `LOW` or `HIGH` for `risk_level`; `MEDIUM` is not executable yet.
   - Treat prose outside the blocks as human context only.
3. Capture the pre-retrofit state.
   - Sense the current layout, package paths, entrypoints, and toolchain remnants.
   - Record the facts that will later populate the Sensing Delta Report.
4. Parse the target transformation and declared strategy.
   - Use `## Target Transformation` plus `yaml [migration-strategy]` as the execution contract.
   - Treat `Migration Direction` as strategy declaration only.
   - Do not reinterpret missing targets or invent migration policy.
5. Run the Risk Alignment Check before execution gates.
   - Compare the declared risk metadata to the observable workspace and planned operations.
   - If the contract says `LOW` but scanning reveals destructive actions, hard-block and require plan or risk correction.
   - If destructive intent is obvious but `destructive_actions` is incomplete, stop instead of improvising a partial preview.
6. Run **Gate 1: Shadow File Detection** before any restructure.
   - Detect duplicate semantic intent at different paths, such as root `app.py` versus target `src/service/main.py`.
   - Present exactly four human choices: **move**, **delete**, **coexist**, or **abort**.
   - Do not continue until the human chooses one option for each conflict.
7. Run **Gate 2: Implicit Config Mining** after Gate 1 is resolved.
   - Scan for `poetry.lock`, `pyproject.toml`, `setup.py`, `setup.cfg`, `.venv`, `conda.yml`, `requirements.txt`, and `Pipfile`.
   - Present exactly four human choices when remnants are found: **migrate**, **delete**, **preserve**, or **abort**.
   - Do not continue until the human confirms the disposition of each config family.
8. Choose the runtime confirmation lane from `risk_level`.
   - `LOW`: use the lightweight confirmation path for additive or non-destructive work only.
   - `HIGH`: generate a destructive preview from `destructive_actions` plus current scan results, regenerate or update that preview if Gate 1 or Gate 2 decisions change the destructive scope, then require explicit human authorization for the final destructive scope before any destructive step.
   - Neither lane bypasses Gate 1, Gate 2, or Git safety.
9. Run **Gate 3: Git safety and pre-destructive check** immediately before any move, deletion, or overwrite.
   - Inspect Git working-tree status immediately before the destructive step.
   - If the tree is dirty, hard-block the retrofit.
   - Require an explicit human path of either committing existing changes or creating a backup before destructive work can resume.
   - This gate cannot be bypassed.
10. Apply only human-confirmed retrofit operations.
    - Move, delete, preserve, or migrate only what the human approved.
    - Never auto-merge conflicting configurations.
    - Do not let `Migration Direction` or `destructive_actions` substitute for runtime gate answers.
11. Generate the Sensing Delta Report after the retrofit changes land.
    - Emit JSON with a top-level `delta_summary` object.
    - Include `timestamp`, `pre_retrofit_state`, `post_retrofit_state`, `changes`, `new_files`, `deleted_files`, and `modified_files`.
    - For every change record include `fact_key`, `before`, `after`, and `operation`, where `operation` is one of `MOVED`, `CREATED`, `MODIFIED`, or `DELETED`.
12. Record provenance in `.github/skills-provenance.json`.
    - Record the retrofit date, creator, and Delta Report reference.
    - Keep provenance repo-visible and governance-oriented.
13. Close the loop with acceptance.
    - Hand off to `python3 .github/skills/sense-env-scaffold/scripts/sense_env.py --mode acceptance --contract-file retrofit-plan.md`.
    - If acceptance cannot run, report the blocking reason instead of claiming success.
14. Clean up scratch artifacts created during the retrofit flow while preserving `retrofit-plan.md`, the Delta Report artifact, and provenance.

# Examples
- Positive: Read a Retrofit V2 `retrofit-plan.md`, block a mislabeled `LOW` plan if the workspace reveals destructive moves, otherwise run Gate 1 and Gate 2, require HIGH-risk destructive preview and authorization when needed, emit the Sensing Delta Report, then hand off to `python3 .github/skills/sense-env-scaffold/scripts/sense_env.py --mode acceptance --contract-file retrofit-plan.md`.
- Negative: Accept old Retrofit headings, treat `Migration Direction` as permission to skip human choices, or continue with destructive work after a `LOW` risk mismatch or dirty Git state.

# Outputs
- an existing Python project restructured to the approved Retrofit V2 target
- explicit human gate outcomes for shadow files, implicit configs, and destructive paths
- a Sensing Delta Report JSON artifact with before/after facts and `MOVED` / `CREATED` / `MODIFIED` / `DELETED` operations
- provenance recorded in `.github/skills-provenance.json`
- an acceptance handoff result or a concrete blocking error

# Verification
- confirm `retrofit-plan.md` contains the locked Retrofit V2 sections and valid `[migration-strategy]` and `[sensing-assertions]` blocks
- confirm `risk_level` is explicit, executable, and aligned with observed destructive surfaces
- confirm a `LOW` plan hard-blocks when scanning reveals destructive actions
- confirm `HIGH` plans require destructive preview plus explicit human authorization before destructive work
- confirm all three gates block progress rather than warn passively
- confirm dirty Git state stops destructive retrofit until the human commits or produces a backup
- confirm the Delta Report uses the required JSON fields and only the allowed operations
- confirm acceptance uses the exact `sense_env.py --mode acceptance --contract-file retrofit-plan.md` handoff

# Red Flags
- a request to “just pick the most likely path” for conflicting files or configs
- a Retrofit V2 contract marked `LOW` even though the workspace reveals moves, deletes, overwrites, or relocations
- conflicting config surfaces that would need heuristic line-by-line merging
- `Migration Direction` being treated as runtime consent instead of strategy context
- a claim that acceptance can be skipped because the filesystem now looks correct

# Common Rationalizations
- “The plan says replace the old entrypoint, so we do not need Gate 1.”
- “This is probably still LOW because the move is small.”
- “We can merge `pyproject.toml` and `setup.cfg` heuristically.”
- “The repo is dirty, but Git can recover it later.”
- “Acceptance is redundant because the contract already describes the target state.”

# Boundaries
- Do not author or redesign the retrofit plan; consume the locked Retrofit V2 contract that already exists.
- Do not execute or broaden acceptance assertions; `sense_env.py --mode acceptance` owns assertion execution.
- Do not replace human-authored design or business logic; only restructure baseline and configuration surfaces.
- Do not auto-merge conflicting configurations.
- Do not generate `.github/copilot-instructions.md` content.
- Do not proceed through any gate without explicit human confirmation.

# Validation

## Required Checks
- `retrofit-plan.md` is present, readable, and contains the locked Retrofit V2 section order
- `yaml [migration-strategy]` block is parseable and `risk_level` is `LOW` or `HIGH`
- `yaml [sensing-assertions]` block is parseable under `## Acceptance Criteria`
- `risk_level` is aligned with observable destructive surfaces before any gate runs
- Git working-tree is clean before any destructive step (Gate 3)

## Quality Checks
- All three gates produced explicit human-confirmed outcomes before execution proceeded
- The Sensing Delta Report includes all required fields: `delta_summary`, `timestamp`, `pre_retrofit_state`, `post_retrofit_state`, `changes`, `new_files`, `deleted_files`, `modified_files`
- Every change record includes `fact_key`, `before`, `after`, and a valid `operation` value
- Provenance is recorded in `.github/skills-provenance.json`
- Acceptance handoff used the exact `sense_env.py --mode acceptance --contract-file retrofit-plan.md` invocation

## On Soft Fail
- Mark output as INCOMPLETE; emit the blocking reason explicitly; continue with best-effort output when possible rather than halting entirely
- Mark INCOMPLETE if partial — e.g., if acceptance cannot run, emit the blocking reason and mark the retrofit INCOMPLETE rather than claiming success

# Failure Handling

## Missing Context
- BLOCKED — if `retrofit-plan.md` is not provided or cannot be read, stop and ask for the correct path before proceeding

## Ambiguous Requirement
- If a `retrofit-plan.md` section is ambiguous or missing required machine-readable blocks, stop and request clarification or a corrected plan; do not infer intent from prose
- If `risk_level` is `MEDIUM` or absent, hard-block and require a corrected `[migration-strategy]` block
- If Gate 1 or Gate 2 presents a conflict without a clear human choice, re-present the four options and wait; do not default to any option

## Execution Limitation
- If the repository cannot be inspected (permissions, missing Git state, or inaccessible paths), stop and report the specific blocking condition
- If a destructive migration step partially fails, do not attempt to roll back automatically; report what succeeded and what failed, mark the retrofit INCOMPLETE, and require human review before retrying
- If `sense_env.py` is unavailable or returns a non-zero exit code, report the exact error and mark the retrofit INCOMPLETE rather than claiming success

# Local references
- `examples.md`: detailed Retrofit V2 execution scenarios, risk-lane behavior, and anti-patterns
- `references/retrofit-plan-v2-contract.md`: executor-side parsing contract for Retrofit V2 headings and machine-readable blocks
- `references/retrofit-conflict-resolution.md`: Shadow File Detection, Implicit Config Mining, gate ordering, and runtime stop-and-ask rules
- `references/retrofit-safety-guidelines.md`: risk-alignment blocking, destructive preview, Git safety checks, backup expectations, and hard-block behavior
- `references/sensing-delta-contract.md`: Sensing Delta Report schema, operation semantics, and interpretation guidance
