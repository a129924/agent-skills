---
name: python-project-init-greenfield
description: Create a governed Python project baseline from a locked `blueprint.md` contract. Use this when a greenfield repository needs its first uv-aligned structure, copied Agent Skills, and a closed acceptance handoff through the canonical `sense-env-scaffold` CLI path.
---

# Purpose
Turn a greenfield `blueprint.md` into a concrete, governance-aware Python project baseline.

# Trigger / When to use
Use this skill when:
- a new or near-empty repository already has a review-ready `blueprint.md`
- the task is to create the first Python baseline rather than retrofit an existing project
- the repository should start with uv-aligned tooling, required Agent Skills, and acceptance-ready structure
- the workflow needs build-first execution followed by `python3 .github/skills/sense-env-scaffold/scripts/sense_env.py --mode acceptance --contract-file blueprint.md`

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
7. Record governance provenance in `.github/skills-provenance.json`.
   - Capture at least skill name, source version, and source hash.
   - Keep the provenance file governance-oriented; do not overload the sensing manifest.
8. Merge only when safe.
   - Additive, low-risk updates may be merged.
   - Materially different config, README, or skill content requires explicit human guidance.
9. Close the loop with acceptance.
   - Ensure the canonical CLI path is actually available through an installed `sense-env-scaffold` skill or an already-present equivalent local install.
   - Run acceptance against `blueprint.md`.
   - If acceptance fails, report the concrete gaps and stop; do not silently reinterpret the contract.
10. Leave `blueprint.md` in place as the persistent design contract and clean up any scratch artifacts created during init.

# Examples
- Positive: Read a locked `blueprint.md`, create the uv baseline under `src/` and `tests/`, copy the listed skills, record provenance in `.github/skills-provenance.json`, then run `python3 .github/skills/sense-env-scaffold/scripts/sense_env.py --mode acceptance --contract-file blueprint.md`.
- Negative: Use this skill to retrofit an existing service with lots of pre-existing structure, invent missing blueprint fields, or overwrite divergent governance files without asking the human.

# Outputs
- a greenfield Python baseline aligned to `blueprint.md`
- copied required skill folders under `.github/skills/`
- governance provenance recorded in `.github/skills-provenance.json`
- a repository ready for acceptance verification against the same `blueprint.md`

# Verification
- confirm `blueprint.md` follows the fixed heading order and contains a valid `[sensing-assertions]` block
- confirm every required skill exists in the source library before copying starts
- confirm generated outputs include uv-aligned `pyproject.toml`, governance-aware `README.md`, and typed entrypoint boilerplate
- confirm placeholder `.github/copilot-instructions.md` tells Copilot to consult installed skills and prefer the canonical sensing / acceptance command first
- confirm placeholder files remain placeholders and do not contain business logic or secrets
- confirm acceptance is run only when `python3 .github/skills/sense-env-scaffold/scripts/sense_env.py` is available locally

# Red Flags
- a request to "just guess" missing blueprint sections or assertion kinds
- a target repository already containing materially different `.github/skills/` content
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

# Local references
- `examples.md`: detailed greenfield-init scenarios, branching paths, and anti-patterns
- `references/blueprint-parsing-contract.md`: ordered heading contract, bullet syntax, normalization rules, and contract-error conditions
- `references/baseline-generation-rules.md`: layout rules, file-generation policy, provenance recording, safe-merge policy, and acceptance handoff requirements
