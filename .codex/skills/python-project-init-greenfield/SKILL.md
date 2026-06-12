---
name: python-project-init-greenfield
description: Create a governed Python project baseline from a locked `blueprint.md` contract. Use this when a greenfield repository needs its first uv-aligned structure, copied Agent Skills, and a closed acceptance handoff through the canonical `sense-env-scaffold` CLI path.
complexity: high
risk_profile:
  - destructive_action
  - multi_agent_handoff
inputs:
  - the target repository root
  - the blueprint.md path
  - the source skill-library root used to copy Required Skills
  - explicit human approval for destructive or ambiguous overwrite decisions
  - the target repository or directory name for package-name fallback
outputs:
  - a greenfield Python baseline aligned to blueprint.md
  - copied required skill folders under `.codex/skills/`
  - governance provenance recorded in `.codex/skills-provenance.json`
  - a repository ready for acceptance verification against the same blueprint.md
use_when:
  - a new or near-empty repository already has a review-ready blueprint.md
  - the task is to create the first Python baseline rather than retrofit an existing project
  - the repository should start with uv-aligned tooling, required Agent Skills, and acceptance-ready structure
  - the workflow needs build-first execution followed by the canonical sense-env-scaffold acceptance command
do_not_use_when:
  - the repository already has meaningful structure and needs retrofit or selective reinforcement
  - blueprint.md is missing, malformed, or still being negotiated
  - the task is only to generate .github/copilot-instructions.md or tweak one existing config file
  - the user wants business logic, domain models, CI/CD pipelines, or infrastructure setup
---

# Purpose
Turn a greenfield `blueprint.md` into a concrete, governance-aware Python project baseline.

# Trigger / When to use
Use this skill when:
- a new or near-empty repository already has a review-ready `blueprint.md`
- the task is to create the first Python baseline rather than retrofit an existing project
- the repository should start with uv-aligned tooling, required Agent Skills, and acceptance-ready structure
- the workflow needs build-first execution followed by `python3 .codex/skills/sense-env-scaffold/scripts/sense_env.py --mode acceptance --contract-file blueprint.md`

Do not use this skill when:
- the repository already has meaningful structure and needs retrofit or selective reinforcement
- `blueprint.md` is missing, malformed, or still being negotiated
- the task is only to generate `.github/copilot-instructions.md` or tweak one existing config file
- the user wants business logic, domain models, CI/CD pipelines, or infrastructure setup

# Inputs
- the target repository root
- the `blueprint.md` path
- the source skill-library root used to copy `Required Skills`
- explicit human approval for destructive or ambiguous overwrite decisions
- the target repository or directory name for package-name fallback

# Process
1. Confirm this is a greenfield fit: the repository is empty or baseline-only, and a readable `blueprint.md` exists.
2. Parse `blueprint.md` using the locked ordered-heading contract from `references/blueprint-parsing-contract.md`.
   - Reject missing required sections.
   - Reject a missing or malformed ````yaml [sensing-assertions]```` block.
   - Treat unsupported assertion kinds as contract errors.
   - Skip non-matching prose lines as human-only notes instead of guessing.
3. Extract the actionable inputs:
   - `Required Skills`
   - `Toolchain Expectation`
   - `Structural Invariants`
   - `Quality Thresholds`
   - `Acceptance Criteria`
4. Resolve baseline structure:
   - prefer an explicit `package:` invariant when present
   - otherwise derive the package name from the repository name using `snake_case`
   - create `src/`, `tests/`, and `scripts/`
   - create invariant paths and generate typed starter boilerplate for every `entrypoint:` item
5. Generate the baseline files:
   - `pyproject.toml` with uv-aligned metadata and pytest / ruff / pyright configuration
   - `README.md` with project summary, `## Governance`, uv quick-start, and acceptance note
   - `.gitignore`
   - `.env.example`
   - `.pre-commit-config.yaml`
   - placeholder `.github/copilot-instructions.md`
   - `src/__init__.py` and `tests/__init__.py`
6. Deploy `Required Skills` from the source skill library.
   - Validate each source skill folder contains at least `SKILL.md`.
   - Copy the full skill folder, including companion files and local assets.
   - If the target already contains materially different skill content, stop and ask the human instead of overwriting or merging.
7. Record governance provenance in `.codex/skills-provenance.json`.
   - Capture at least skill name, source version, and source hash.
   - Keep the provenance file governance-oriented; do not overload the sensing manifest.
8. Merge only when safe.
   - Additive, low-risk updates may be merged.
   - Materially different config, README, or skill content requires explicit human guidance.
9. Close the loop with acceptance.
   - Treat `skills/...` as the canonical source and `.codex/skills/...` as the install-time projection surface.
   - Ensure the canonical CLI projection path is actually available through an installed `sense-env-scaffold` skill or an already-present equivalent local install.
   - Run acceptance against `blueprint.md`.
   - If acceptance fails, report the concrete gaps and stop; do not silently reinterpret the contract.
10. Leave `blueprint.md` in place as the persistent design contract and clean up any scratch artifacts created during init.

# Examples
- Positive: Read a locked `blueprint.md`, create the uv baseline under `src/` and `tests/`, copy the listed skills, record provenance in `.codex/skills-provenance.json`, then run `python3 .codex/skills/sense-env-scaffold/scripts/sense_env.py --mode acceptance --contract-file blueprint.md`.
- Negative: Use this skill to retrofit an existing service with lots of pre-existing structure, invent missing blueprint fields, or overwrite divergent governance files without asking the human.

# Outputs
- a greenfield Python baseline aligned to `blueprint.md`
- copied required skill folders under `.codex/skills/`
- governance provenance recorded in `.codex/skills-provenance.json`
- a repository ready for acceptance verification against the same `blueprint.md`

# Verification
- confirm `blueprint.md` follows the fixed heading order and contains a valid `[sensing-assertions]` block
- confirm every required skill exists in the source library before copying starts
- confirm generated outputs include uv-aligned `pyproject.toml`, governance-aware `README.md`, and typed entrypoint boilerplate
- confirm placeholder `.github/copilot-instructions.md` tells Copilot to consult installed skills and prefer the canonical sensing / acceptance command first
- confirm placeholder files remain placeholders and do not contain business logic or secrets
- confirm acceptance is run only when `python3 .codex/skills/sense-env-scaffold/scripts/sense_env.py` is available locally

# Red Flags
- a request to "just guess" missing blueprint sections or assertion kinds
- a target repository already containing materially different `.codex/skills/` content
- a request to generate application-specific logic as part of baseline init
- a claim that acceptance can be skipped because the structure "looks right"
- a request to replace existing config wholesale without reviewing the diff

# Common Rationalizations
- "The blueprint is close enough; we can fill the rest in later."
- "This existing skill folder is probably the same, so just overwrite it."
- "Optional means we should install or generate the full thing anyway."
- "The README can stay title-only for now."
- "Acceptance is redundant because we just created the files ourselves."

# Boundaries
- Do not redesign `blueprint.md`; consume the locked schema that already exists.
- Do not use this skill for retrofit or incremental repair of an established repository.
- Do not invent business-domain code, `.env` secrets, CI pipelines, or infrastructure.
- Do not modify `sense_env.py` or broaden its supported assertion kinds.
- Do not bypass human approval on destructive or ambiguous overwrite paths.

# Validation

## Required Checks
- `blueprint.md` must exist at the provided path and be readable before any file generation begins
- `blueprint.md` must follow the fixed ordered-heading contract from `references/blueprint-parsing-contract.md`
- `blueprint.md` must contain a valid ` ```yaml [sensing-assertions]` `` ` block with supported assertion kinds only
- every skill named in `Required Skills` must exist in the source skill library before copying starts
- the target repository must be empty or baseline-only; stop if meaningful non-baseline structure is detected

## Quality Checks
- generated `pyproject.toml` is uv-aligned and includes pytest, ruff, and pyright configuration sections
- governance-aware `README.md` includes `## Governance`, uv quick-start, and acceptance note
- typed entrypoint boilerplate exists for every `entrypoint:` item declared in `blueprint.md`
- placeholder `.github/copilot-instructions.md` tells Copilot to consult installed skills and prefer the canonical acceptance command
- `.codex/skills-provenance.json` records at minimum skill name, source version, and source hash for each copied skill
- `sense-env-scaffold` acceptance command is available locally before it is invoked
- acceptance run produces a concrete pass/fail result; a silent or skipped run is a quality failure

## On Soft Fail
- Mark output as INCOMPLETE; list which artifacts were not created or which steps could not be completed; continue with best-effort output where safe to do so
- Mark INCOMPLETE if partial scaffolding was created but acceptance could not be run or failed
- Do not silently reinterpret contract gaps; surface them explicitly so the human can decide

# Failure Handling

## Missing Context
- BLOCKED — if `blueprint.md` is not provided or cannot be read, stop and ask for the correct path before proceeding
- BLOCKED — if the source skill-library root is not provided and required skills cannot be located, stop and ask

## Ambiguous Requirement
- If a `blueprint.md` section is present but ambiguous (e.g., unclear package name, conflicting invariants), surface the ambiguity and ask the human to clarify rather than guessing
- If an unsupported assertion kind appears in the `[sensing-assertions]` block, treat it as a contract error and stop
- If a non-matching prose line appears in the blueprint, skip it as a human-only note; do not infer an action from it

## Execution Limitation
- If a target directory already contains materially different skill content, stop and ask the human rather than overwriting or merging silently
- If `sense-env-scaffold` is not available locally, report the gap and stop; do not mark acceptance as passed
- If file generation partially fails (e.g., permission error, disk issue), mark the output INCOMPLETE and report which artifacts were not created

# Local references
- `examples.md`: detailed greenfield-init scenarios, branching paths, and anti-patterns
- `references/blueprint-parsing-contract.md`: ordered heading contract, bullet syntax, normalization rules, and contract-error conditions
- `references/baseline-generation-rules.md`: layout rules, file-generation policy, provenance recording, safe-merge policy, and acceptance handoff requirements
