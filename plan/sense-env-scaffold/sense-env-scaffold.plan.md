# sense_env scaffold implementation plan

## Goal / outcome
Produce a handoff-ready implementation contract for the first executable,
zero-dependency `sense_env` scaffold, including:

- a concrete manifest schema reference
- a concrete CLI contract reference
- a first runnable scaffold implementation

The intended code artifact is:

- `.github/skills/sense-env-scaffold/scripts/sense_env.py`

This topic plan exists so an executor Agent can implement the scaffold without
re-deciding workflow, CLI semantics, manifest shape, or acceptance behavior.

## Scope
- Create `.github/skills/sense-env-scaffold/references/env-manifest-schema.md`.
- Create `.github/skills/sense-env-scaffold/references/sense-env-cli-contract.md`.
- Create `.github/skills/sense-env-scaffold/scripts/sense_env.py`.
- Keep the script standard-library only and compatible with Python 3.10+.
- Implement the agreed CLI surface, exit-code model, fenced-block extraction, and
  stable JSON output shape.
- Ship a minimal but runnable discovery / acceptance scaffold rather than a full
  detector suite.
- Keep this work as a repo-internal prototype / planning artifact, not as a new
  stable-library surface.

## Locked decisions
- Script path is fixed:
  - `.github/skills/sense-env-scaffold/scripts/sense_env.py`
- Create `.github/skills/sense-env-scaffold/scripts/` even though it does not exist yet.
- This repo-root script is a **topic-specific prototype exception requested by the
  Human**, not a new general repository policy. Executor must not generalize this
  into “repo-root scripts are normally allowed here.”
- CLI flags must include:
  - `--mode discovery|acceptance`
  - `--contract-file`
  - `--output`
  - `--snapshot`
- Mode semantics are behavior-oriented, not project-stage-oriented:
  - `discovery` = tolerant, fact-first, harmless
  - `acceptance` = contract-first, strict assertion evaluation
- Exit codes are fixed:
  - `0` = success
  - `10` = operational error
  - `20` = acceptance failure
  - `30` = contract error
- Discovery mode should still return `0` when optional tools are missing, as long
  as sensing completes and the facts are recorded truthfully.
- Acceptance mode must load a machine-readable contract and fail hard when
  required assertions do not pass.
- Top-level manifest keys are a hard contract and must not be renamed:
  - `meta`
  - `fingerprint`
  - `facts`
  - `assertions`
  - `gaps`
- All JSON keys should use `snake_case`.
- JSON output should be formatted for human inspection with stable indentation.
- Snapshot export stays inside `.github/skills/sense-env-scaffold/scripts/sense_env.py`; do not create a separate
  exporter script.
- Snapshot output must normalize paths to repo-relative form and must not include
  secrets, usernames, absolute local paths, or machine-specific identifiers.
- Contract lookup priority in acceptance mode is:
  1. explicit `--contract-file`
  2. `retrofit-plan.md`
  3. `blueprint.md`
- The fenced machine-readable block tag is fixed across flows:
  - ````yaml [sensing-assertions]````
- Greenfield and Retrofit share one assertion parser; only contract source
  differs.
- In Retrofit acceptance, assertions cover only the scoped reinforcement targets.
- Gap remediation types must distinguish at least:
  - `MISSING`
  - `MISMATCH`
  - `DEPRECATED`
- First-pass supported assertion kinds are fixed to:
  - `path_exists`
  - `path_type`
  - `command_available`
- The first-pass parser must not claim general YAML support. It should support a
  narrow documented subset only.

## Boundaries / exclusions
- Do not write or modify `.github/copilot-instructions.md`.
- Do not install tools, create virtual environments, or start services.
- Do not add non-stdlib Python dependencies.
- Do not add deep business-code analysis or architecture commentary.
- Do not make the first version perform deep, unbounded recursive scanning.
- Do not expose a user-facing scan-depth flag in this iteration.
- Do not broaden the top-level JSON schema beyond the fixed five modules.
- Do not update stable-library surfaces such as `README.md` or `VERSION` as part
  of this scaffold task.
- Do not treat this prototype as proof that repo-root scripts are now part of the
  canonical repository shape.

## Status / allowed transitions
- Current status: `review-ready`
- Allowed transitions:
  - `planned` -> `creator-in-progress`
  - `creator-in-progress` -> `review-ready`
  - `review-ready` -> `reviewer-in-progress`
  - `reviewer-in-progress` -> `approved`
  - `reviewer-in-progress` -> `needs-rework`
  - `needs-rework` -> `creator-in-progress`
  - `approved` -> `publish-in-progress`
  - `publish-in-progress` -> `pr-open`
  - `pr-open` -> `needs-rework`
  - `pr-open` -> `merged`
  - `merged` -> terminal

## Artifact paths
- Topic plan:
  - `plan/sense-env-scaffold/sense-env-scaffold.plan.md`
- Read-first workflow references:
  - `plan/references/python-init-pipeline-skeleton.md`
  - `plan/agent-handoff-workflow.md`
  - `.github/copilot-instructions.md`
- Reference artifacts to create:
  - `.github/skills/sense-env-scaffold/references/env-manifest-schema.md`
  - `.github/skills/sense-env-scaffold/references/sense-env-cli-contract.md`
- Script scaffold to create:
  - `.github/skills/sense-env-scaffold/scripts/sense_env.py`
- Primary runtime outputs after implementation:
  - `.github/env-manifest.json`
  - `.github/env-manifest.snapshot.json`

## Execution checklist
- [ ] Read the three read-first documents before editing.
- [ ] Re-confirm that this task is executing under the Human-approved prototype
      exception for `.github/skills/sense-env-scaffold/scripts/sense_env.py`.
- [ ] Create `.github/skills/sense-env-scaffold/references/env-manifest-schema.md`.
- [ ] Create `.github/skills/sense-env-scaffold/references/sense-env-cli-contract.md`.
- [ ] Create `scripts/` and `.github/skills/sense-env-scaffold/scripts/sense_env.py`.
- [ ] Implement `argparse` with all four required flags.
- [ ] Implement repo-root detection and document it in the CLI reference.
- [ ] Implement acceptance-mode contract lookup in the agreed order.
- [ ] Implement fenced Markdown block extraction for `[sensing-assertions]`.
- [ ] Implement the narrow supported assertion subset only.
- [ ] Implement stable top-level JSON assembly with the five fixed modules.
- [ ] Implement exit-code routing for `0 / 10 / 20 / 30`.
- [ ] Keep imports standard-library only.
- [ ] Ensure discovery mode stays harmless when optional tools are absent.
- [ ] Ensure acceptance failures emit JSON and exit `20`.
- [ ] Ensure contract-input failures emit JSON and exit `30`.
- [ ] Ensure `--snapshot` behavior matches the locked CLI contract.
- [ ] Confirm snapshot filtering removes machine-local and secret-shaped data.

## Implementation steps
1. Read the repo policy and the existing pipeline reference so the implementation
   stays aligned with the already-locked workflow.
2. Treat this topic as a repo-internal prototype exception:
   - allowed because the Human explicitly requested `.github/skills/sense-env-scaffold/scripts/sense_env.py`
   - not a new repo-wide default
   - if branch / reviewer context rejects this exception, stop and return
     `needs-rework` rather than silently relocating the script
3. Create `.github/skills/sense-env-scaffold/references/env-manifest-schema.md` with:
   - purpose of `env-manifest.json`
   - stable top-level schema
   - example discovery-mode manifest
   - example acceptance-mode manifest
   - gap semantics
   - assertion record shape
   - snapshot filtering and promotion notes
4. Create `.github/skills/sense-env-scaffold/references/sense-env-cli-contract.md` with:
   - CLI synopsis
   - flag semantics
   - mode semantics
   - path-resolution rules
   - contract lookup order
   - exit-code table
   - invocation examples for:
     - discovery
     - acceptance with explicit contract
     - acceptance with implicit lookup
     - snapshot export
5. Create `.github/skills/sense-env-scaffold/scripts/sense_env.py` and define:
   - exit-code constants
   - typed manifest-construction helpers
   - typed assertion / gap record helpers
   - main argument parsing
   - main dispatch function
6. Implement repo-root detection and use it consistently:
   - search upward from the current working directory for `.git`
   - treat either a `.git` directory or a `.git` file as a valid repo marker
   - if found, that directory is the repo root
   - if not found, use the current working directory as the working root
7. Implement output-path handling exactly as follows:
   - default live manifest path:
     - `<repo_root>/.github/env-manifest.json`
   - `--output <path>` overrides the live manifest destination only
   - if `--output` is relative, resolve it against `repo_root`
   - when writing the live manifest to a path under `<repo_root>/.github/`, create
     the parent directory if it does not exist yet
   - if parent-directory creation or live-manifest writing fails, return exit `10`
   - snapshot path in v1 is fixed:
     - `<repo_root>/.github/env-manifest.snapshot.json`
   - create `<repo_root>/.github/` for the snapshot path as well when needed
   - v1 does not support a custom snapshot-output flag
8. Implement `--snapshot` exactly as follows:
   - it is a boolean flag
   - it does not replace live-manifest writing
   - when enabled, the script writes the live manifest first and then writes the
     filtered snapshot to the fixed snapshot path
   - v1 should treat `--snapshot` as valid only when the run would otherwise
     succeed with exit code `0`
   - if the run results in exit `10`, `20`, or `30`, do not write the snapshot
   - if live-manifest writing succeeds but snapshot writing fails, keep the live
     manifest in place and return exit `10`
   - workflow-level Human confirmation for snapshot promotion remains outside the
     script; the flag is a technical export action, not an approval signal
9. Implement acceptance contract lookup exactly as follows:
   - if `--contract-file` is provided and absolute, use it as-is
   - if `--contract-file` is provided and relative, resolve it against `repo_root`
   - if `--contract-file` is not provided:
     1. look for `<repo_root>/retrofit-plan.md`
     2. then look for `<repo_root>/blueprint.md`
   - if no readable contract file is found in acceptance mode, return exit `30`
10. Implement fenced-block extraction for ````yaml [sensing-assertions]````:
    - use a regex-based extractor
    - tolerate minor surrounding noise such as BOM, extra blank lines, or small
      indentation drift around the fenced block
    - in acceptance mode, absence of the required block is a contract error `30`
11. Implement a constrained parser for the first supported assertion subset.
    The first pass should be narrow and explicit rather than pretending to support
    arbitrary YAML.
12. Support only a narrow YAML-like subset in v1:
    - top-level sequence of assertion records
    - scalar keys and scalar values only
    - no nested mappings
    - no anchors
    - no multiline strings
    - no flow-style collections
    - no claim of general YAML compatibility in docs or help text
13. Implement minimal discovery facts collection with harmless fallbacks:
    - repo presence
    - current branch / HEAD when Git is available
    - workspace cleanliness signal when Git is available
    - presence of key files and directories such as:
      - `README.md`
      - `.github/`
      - `pyproject.toml`
      - `tests/`
      - `scripts/`
      - `.github/copilot-instructions.md`
14. Assemble the manifest with fixed top-level modules:
    - `meta`
    - `fingerprint`
    - `facts`
    - `assertions`
    - `gaps`
15. In acceptance mode, evaluate the supported assertion subset and:
    - record per-assertion results
    - mark blocking failures as `FAIL`
    - place unmet items into `gaps`
    - return exit code `20` when assertions were evaluated and any required one
      failed
16. Add snapshot shaping logic that filters or normalizes:
    - absolute paths
    - usernames
    - machine-specific identifiers
    - secret-shaped fields or values
17. Write JSON with stable formatting and ensure the script emits structured output
    even on contract and acceptance failures.
18. Run lightweight self-checks and capture representative command/output examples
    for the implementation summary.

## Validation / acceptance checks
- `.github/skills/sense-env-scaffold/references/env-manifest-schema.md` exists and is self-consistent with the
  fixed contract.
- `.github/skills/sense-env-scaffold/references/sense-env-cli-contract.md` exists and reflects the same flags,
  modes, exit codes, and path rules as the script.
- `.github/skills/sense-env-scaffold/scripts/sense_env.py` exists under `scripts/`.
- The script imports only standard-library modules.
- `python3 .github/skills/sense-env-scaffold/scripts/sense_env.py --help` succeeds.
- The CLI reference explicitly defines:
  - `--snapshot` as a boolean flag
  - default live-manifest output path
  - fixed snapshot output path
  - `--output` override behavior
  - repo-root lookup basis
  - `.git` file or directory as a valid repo-root marker
  - explicit relative-path resolution against `repo_root`
  - `.github/` parent-directory creation behavior
  - live-write-success plus snapshot-write-failure behavior
- Discovery mode without optional tools still returns structured JSON instead of a
  traceback-shaped crash.
- Acceptance mode without a readable contract source returns exit code `30`.
- Acceptance mode with a parsed contract and a failed required assertion returns
  exit code `20`.
- The script emits all five required top-level modules on success.
- Top-level key names remain exactly:
  - `meta`
  - `fingerprint`
  - `facts`
  - `assertions`
  - `gaps`
- The implementation summary explicitly states that v1 supports only the narrow
  documented YAML-like assertion subset, not general YAML.
- Snapshot shaping removes absolute local paths and other machine-local data.
- The implementation summary explicitly lists:
  - supported assertion kinds
  - intentionally unsupported assertion kinds
  - follow-up detector work left for later

## Reviewer handoff
- Hand the executor output to an independent reviewer using this topic plan and
  `plan/agent-handoff-workflow.md`.
- Ask the reviewer to focus on:
  - canonical workflow alignment
  - whether the plan-following implementation preserved the fixed five-module
    manifest contract
  - whether CLI behavior is fully defined and matches the implementation
  - whether repo-root script creation is clearly treated as a Human-approved
    exception rather than a repo-wide policy change
  - whether the docs truthfully describe the narrow YAML-like subset rather than
    claiming general YAML support
- Reviewer should return `approved` or `needs-rework` with blocking issues.
- If reviewer returns `needs-rework`, route the work back to the creator and move
  the topic status to `creator-in-progress`.

## Post-merge / release actions
- This topic does **not** imply stable-library publication.
- Do not update `README.md` or `VERSION` as part of this prototype scaffold task.
- After merge, only perform normal local sync / post-merge cleanup if a PR was
  opened.
- If the repository later decides to formalize repo-root prototype tooling as a
  broader policy, that requires a separate planning topic rather than being
  smuggled into this scaffold task.

## Open questions / unresolved items
- Whether later versions should support richer assertion kinds such as config-key
  checks or file-content expectations.
- Whether later versions should emit a richer fingerprint model.
- Whether later versions should add dedicated tests or fixtures for contract
  samples.
- Whether snapshot export should later support a dedicated output path flag.
- Whether the long-term home for this tooling should remain repo-root prototype
  code or move into a skill-local or different repository structure after the
  prototype proves out.
