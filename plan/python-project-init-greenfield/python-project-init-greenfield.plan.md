# python-project-init-greenfield implementation plan

## Goal / Outcome

Produce an executable Agent Skill that reads a `blueprint.md` Greenfield contract and
builds a minimal yet complete Python project baseline, including:

- Directory structure and entrypoint scaffolding
- `pyproject.toml` with uv-aligned configuration
- Required Agent Skills copied from the source library
- README with governance notes
- Placeholder configuration surfaces
- Version / provenance recording in manifest

Upon completion, the skill hands the built workspace into
`python3 .github/skills/sense-env-scaffold/scripts/sense_env.py --mode acceptance --contract-file blueprint.md`
so the build-and-acceptance loop closes immediately and verifiably.

## Scope

### In scope

- `.github/skills/python-project-init-greenfield/` (new skill folder)
  - `SKILL.md` defining the skill's trigger, inputs, process, outputs, boundaries
  - `examples.md` with multi-path decision examples and anti-patterns
  - `references/blueprint-parsing-contract.md` explaining how to interpret the blueprint
    schema and allowed optional-item behavior
  - `references/baseline-generation-rules.md` explaining scaffolding, naming, and
    fallback rules for `src/`, `tests/`, entrypoints, and configuration
- the skill's implementation of:
  - blueprint.md parsing (fixed heading order, semi-structured sections, YAML block)
  - directory and entrypoint creation
  - `pyproject.toml` generation
  - Required Skills copying with validation
  - `.github/skills-provenance.json` provenance recording
  - README + placeholder instructions generation
  - hard-blocking blueprint-validation failures
  - safe conflict handling and Human confirmation gates
- validation / acceptance checks
- examples suitable for testing the skill

### Out of scope

- creating the canonical blueprint-example artifact (that is a future task for
  `python-first-project-planning`)
- implementing or modifying the `sense_env.py` script
- implementing `copilot-instructions-init` or `python-project-retrofit`
- modifying the `blueprint.md` schema itself (schema is locked separately in
  `define-blueprint-schema`)
- any changes to `README.md` or `VERSION` (this topic does not touch stable-library
  surfaces)

## Locked Decisions

### Blueprint contract

- blueprint.md uses fixed ordered headings:
  1. `## Project Overview`
  2. `## Required Skills`
  3. `## Toolchain Expectation`
  4. `## Structural Invariants`
  5. `## Quality Thresholds`
  6. `## Acceptance Criteria`
- `## Acceptance Criteria` is mandatory
- machine-readable assertions live in a fenced block immediately after
  `## Acceptance Criteria`:
  - tag: ````yaml [sensing-assertions]````
  - minimum record keys: `kind`, `target`, `expected`
  - unsupported kinds cause `contract error` (init blocks)
- Human-readable sections use semi-structured bullets:
  - `- Key: Value` or `- Key @ Version: Purpose`
  - default all items as required unless marked `(Optional)`
- parser should skip non-matching lines as Human-only notes

### Project layout and baseline files

- default layout: **src-layout plus tests and scripts**
- baseline files to create:
  - `pyproject.toml` (uv-aligned)
  - `README.md` (with governance section + quick-start)
  - `.gitignore`
  - `.env.example` (placeholder only)
  - `.github/copilot-instructions.md` (placeholder guidance)
  - `src/__init__.py`
  - `tests/__init__.py`
  - entrypoint from `## Structural Invariants` with typed boilerplate
  - copied `.github/skills/<required-skill-name>/` folders with validation
- `pyproject.toml` should include config for pytest, ruff, pyright
- `.pre-commit-config.yaml` should be generated
- package name under `src/` should come from blueprint or normalize repo name to
  `snake_case`

### Entrypoint scaffolding

- files tagged with `entrypoint:` prefix should generate typed minimal boilerplate
- boilerplate must include `main() -> None` with type hints
- boilerplate must import at least `sys` or `logging`
- boilerplate must include a constitutional comment noting governance by `.github/skills`

### Required Skills behavior

- copy from current repo library with version pinning
- validate that each source skill folder contains at least `SKILL.md`
- copy full skill folder (including `references/`, `scripts/`, `templates/`)
- record provenance in `.github/skills-provenance.json`
- if target repo already contains the same-named skill with divergent content,
  **always ask Human** rather than overwrite or merge

### Human gates

- trigger for destructive actions (overwriting skill, replacing config)
- trigger for ambiguous actions (divergent existing skill, unclear naming)
- do not trigger on validation errors alone; if blueprint is invalid, block init
  cleanly with specific error message

### Non-goals

- do not generate business-domain models or service implementations
- do not fabricate concrete `.env` contents
- do not auto-generate infrastructure or CI/CD files beyond placeholder surfaces
- do not modify `sense_env.py` or the assertion-kind set
- this topic is **not** a stable-library affecting topic (no README/VERSION bump)

## Boundaries / Exclusions

- this skill does not **validate** blueprint requirements beyond syntax
  - validation responsibility belongs upstream in Human / planner review
- this skill does not **execute** assertions
  - assertion execution and acceptance verification happen downstream in
    `python3 .github/skills/sense-env-scaffold/scripts/sense_env.py --mode acceptance --contract-file blueprint.md`
- this skill does not **replace** Human-authored design or business logic
  - it only builds the project baseline and skeleton
- this skill does not **migrate** or **retrofit** existing projects
  - retrofit-specific init logic is a separate skill
- this skill does not **generate** copilot-instructions content
  - instructions generation is handled by `copilot-instructions-init`

## Status / Allowed Transitions

- **Current**: `pr-open`
- **Execution model**: creator -> reviewer -> publish -> merge (terminal)
- **Allowed transitions**:
  - `planned` -> `creator-in-progress`
  - `creator-in-progress` -> `review-ready`
  - `review-ready` -> `reviewer-in-progress`
  - `reviewer-in-progress` -> `approved`
  - `reviewer-in-progress` -> `needs-rework`
  - `needs-rework` -> `creator-in-progress`
  - `approved` -> `creator-in-progress`
  - `approved` -> `publish-in-progress`
  - `publish-in-progress` -> `pr-open`
  - `publish-in-progress` -> `merged`
  - `pr-open` -> `needs-rework`
  - `pr-open` -> `merged`
  - `merged` -> terminal

**Routing notes**: this topic follows the standard Phase 4.5 rule: after `approved`,
main agent handles commit / push / PR open / merge. No release action is required for
this topic.

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/python-project-init-greenfield/python-project-init-greenfield.plan.md` | Planning actor | Repo-visible execution contract for this topic |
| Skill folder | `.github/skills/python-project-init-greenfield/` | Creator | New skill folder for this topic |
| SKILL.md | `.github/skills/python-project-init-greenfield/SKILL.md` | Creator | Executable contract for the skill |
| examples.md | `.github/skills/python-project-init-greenfield/examples.md` | Creator | Multi-path usage patterns and anti-patterns |
| Reference: blueprint parsing | `.github/skills/python-project-init-greenfield/references/blueprint-parsing-contract.md` | Creator | How to interpret the blueprint contract and optional-item behavior |
| Reference: baseline generation | `.github/skills/python-project-init-greenfield/references/baseline-generation-rules.md` | Creator | Rules for directory creation, scaffolding, naming, fallback behavior |

**Artifact path notes**:

- This topic does **not** modify `README.md` or `VERSION`
- This topic creates a new **skill folder only**, not a stable-library-affecting
  change
- All paths listed above are exact and must be created
- If creator work drifts outside these paths, that is a plan-alignment issue and
  must be discussed before merging

## Implementation Steps

1. **Blueprint parsing**
   - Read the fixed ordered headings
   - Reject missing required sections or malformed `[sensing-assertions]` block
   - Parse semi-structured bullet lines
   - Record required skills, toolchain, invariants, and quality thresholds

2. **Blueprint validation**
   - Confirm `## Acceptance Criteria` is present
   - Confirm fenced `yaml [sensing-assertions]` block exists and contains parseable
     YAML records
   - Confirm all assertion kinds are in the v1 supported subset
   - Return explicit error message if validation fails
   - Do not proceed to file creation if blueprint is invalid

3. **Directory structure**
   - Create base directories: `src/`, `tests/`, `scripts/`
   - From `## Structural Invariants`, interpret path and entrypoint prefixes
   - Create required invariant paths and touch entrypoint files
   - Generate typed minimal boilerplate for files with `entrypoint:` prefix

4. **Package naming**
   - Check blueprint for an explicit package name
   - If not present, derive from repo name using `snake_case`
   - Normalize `-` to `_`
   - Create `src/<package_name>/` structure

5. **pyproject.toml generation**
   - Generate uv-aligned baseline configuration
   - Extract toolchain expectations and translate to `[tool.*]` sections
   - Include config for pytest, ruff, pyright
   - Extract quality thresholds and populate corresponding config
   - Support required items and optional items separately

6. **Required Skills deployment**
   - Iterate through `## Required Skills`
   - For each listed skill:
     - Check source library for the skill folder
     - Validate that it contains at least `SKILL.md`
     - Copy full skill folder to target repo's `.github/skills/`
     - If divergent content already exists at target, ask Human before overwriting
     - Record skill name, version, source hash in `.github/skills-provenance.json`

7. **Configuration surface generation**
   - Create `.gitignore` with Python-appropriate defaults
   - Create `.env.example` as a placeholder (no real secrets)
   - Create `.pre-commit-config.yaml` placeholder
   - Create placeholder `.github/copilot-instructions.md` referencing installed skills
     and the canonical acceptance command path

8. **README generation**
   - Include project title and brief description
   - Include `## Governance` section listing installed skills and versions
   - Include quick-start section showing how to use `uv`
   - Include the canonical acceptance command for verification:
     `python3 .github/skills/sense-env-scaffold/scripts/sense_env.py --mode acceptance --contract-file blueprint.md`

9. **Manifest recording**
   - Create or update `.github/skills-provenance.json`
   - Record skill installation in that provenance file
   - Include skill name, version, source hash for later comparison

10. **Post-init guidance**
    - After successful init, print summary of what was created
    - Suggest running
      `python3 .github/skills/sense-env-scaffold/scripts/sense_env.py --mode acceptance --contract-file blueprint.md`
      to verify baseline
    - Preserve `blueprint.md` as the persistent design contract

## Validation / Acceptance Checks

Reviewer and executor should verify:

1. **Blueprint contract validation**
   - blueprint.md is syntactically valid
   - all required sections are present
   - `[sensing-assertions]` block exists and is parseable
   - all assertion kinds are in the v1 supported subset

2. **Artifact completeness**
   - all files listed in `Artifact Paths` exist at exact locations
   - SKILL.md includes all required sections with examples
   - examples.md covers multi-path decisions and anti-patterns
   - references/ files are complete and accurate

3. **Skill folder integrity**
   - folder structure matches canonical skill expectations
   - no hidden chat context requirements
   - examples are concise and concrete

4. **Implementation correctness**
   - blueprint parsing handles the fixed section order
   - optional-item behavior is correct (marked with "(Optional)" only)
   - directory creation respects structural invariants
   - entrypoint scaffolding generates typed boilerplate, not empty files
   - pyproject.toml is uv-aligned and parseable
   - Required Skills are copied with validation
   - manifest provenance is recorded
   - Human gates are triggered for destructive / ambiguous actions
   - non-goals are genuinely excluded (no business logic, no CI/CD beyond
     placeholder)

5. **Docstring and example quality**
   - SKILL.md trigger is explicit and concrete
   - examples include positive multi-path scenarios and negative anti-patterns
   - reference files are focused and not bloated

## Reviewer Handoff

When the creator finishes and marks this topic as `review-ready`, the reviewer should
evaluate using this JSON format:

```json
{
  "verdict": "approved|needs-rework",
  "blocking_issues": [],
  "copilot_feedback_triage": {
    "ADDRESS": [],
    "DISCUSS": [],
    "SKIP": []
  }
}
```

The reviewer's verdict is either:
- `approved`: the skill is review-ready and meets the spec; main agent may proceed to
  publish
- `needs-rework`: blocking issues exist; creator should address and re-submit

## Post-merge / release actions

After merge is complete:

- **No repository release action is required for this topic.**
- The new skill is now part of the repository.
- The skill is not added to `README.md` or `VERSION` as part of this merge.
- Stable-library updates may happen in a separate topic or publisher action later.
- Main agent should verify that the new skill folder is accessible and that basic
  import / documentation checks pass.

## Open Questions / Unresolved Items

None. All design decisions are locked and ready for implementation.

---

**Version control**: This plan is revision 1.0, created after full alignment of the
Greenfield init contract in plan mode. Creator implementation should follow this plan
exactly; if drift occurs, stop and discuss with planning before continuing.
