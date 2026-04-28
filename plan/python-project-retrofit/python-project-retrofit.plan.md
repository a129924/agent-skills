# python-project-retrofit implementation plan

## Goal / Outcome

Produce an executable Agent Skill that retrofits an existing Python project to align with the repository's initialization standards, including:

- Detection and safe resolution of structural conflicts (Shadow File Detection)
- Discovery and confirmation of implicit toolchain configurations (Implicit Config Mining)
- Safe execution with Git working tree validation and pre-destructive backup checks
- Complete Sensing Delta Report documenting project state transformation
- Provenance recording in `.github/skills-provenance.json`

Upon completion, the skill hands the retrofitted workspace into
`python3 .github/skills/sense-env-scaffold/scripts/sense_env.py --mode acceptance --contract-file retrofit-plan.md`
so the retrofit-and-acceptance loop closes immediately and verifiably.

## Scope

### In scope

- `.github/skills/python-project-retrofit/` (new skill folder)
  - `SKILL.md` defining the skill's trigger, inputs, process, outputs, boundaries
  - `examples.md` with multi-gate decision scenarios, conflict resolution, and safety checks
  - `references/retrofit-conflict-resolution.md` explaining Shadow File Detection, Implicit Config Mining, and resolution strategies
  - `references/retrofit-safety-guidelines.md` explaining Git safety checks, destructive-operation lists, and backup strategies
  - `references/sensing-delta-contract.md` explaining the Sensing Delta Report JSON schema and interpretation
- the skill's implementation of:
  - retrofit-plan.md parsing (project overview, target structure, acceptance criteria)
  - Git working tree validation (blocking Dirty state with clear error)
  - Shadow File Detection: identifying structural conflicts between plan and current state
  - Implicit Config Mining: discovering tool-chain remnants (poetry.lock, .venv, setup.py, etc.)
  - Human confirmation gates for all detected conflicts
  - Pre-destructive operation checks (commit or backup requirement before file moves/overwrites)
  - Safe project restructuring (directory moves, file reorganization, configuration updates)
  - Post-Retrofit Sensing Delta Report generation with clear before/after state comparison
  - Provenance recording including retrofit date, creator, and Delta Report reference
- validation / acceptance checks
- examples suitable for testing the skill

### Out of scope

- creating the retrofit-plan.md template or example (future task for `python-first-project-planning`)
- implementing or modifying the `sense_env.py` script
- implementing `copilot-instructions-init` or `python-project-init-greenfield`
- automatic multi-path decision logic beyond the three detection gates
- any changes to `README.md` or `VERSION` (this topic does not touch stable-library surfaces)

## Locked Decisions

### Retrofit contract

- retrofit-plan.md uses semi-structured sections:
  - `## Project Overview` (current state description)
  - `## Target Structure` (desired layout and configuration)
  - `## Acceptance Criteria` (machine-readable assertions)
- Acceptance Criteria uses a fenced YAML block tagged `[sensing-assertions]` with records containing `kind`, `target`, `expected`
- Human-readable sections use semi-structured bullets following blueprint conventions

### Three-tier detection gates (Non-negotiable)

**Gate 1: Shadow File Detection**
- Identify files with duplicate semantic intent but different paths (e.g., plan says `src/` but `app.py` already exists at root)
- When conflict is detected, stop and ask:
  - Option A: Move existing file into target structure
  - Option B: Delete existing file (keep target version only)
  - Option C: Allow parallel existence (coexist)
  - Option D: Abort retrofit
- Do not proceed without Human confirmation

**Gate 2: Implicit Config Mining**
- Scan for tool-chain remnants: `poetry.lock`, `pyproject.toml`, `setup.py`, `setup.cfg`, `.venv`, `conda.yml`, `requirements.txt`, `Pipfile`
- When remnants are found, stop and ask:
  - Option A: Migrate existing configuration to target tool
  - Option B: Delete remnants (clean state)
  - Option C: Preserve existing setup (no change)
  - Option D: Abort retrofit
- Do not proceed without Human confirmation

**Gate 3: Git safety check**
- Before any file move, deletion, or overwrite, check Git working tree status
- If status is Dirty, hard-block retrofit:
  - Require explicit `git commit` of existing changes, or
  - Provide automated backup before proceeding
  - Cannot bypass this check

### Sensing Delta Report contract

- Output format: JSON object with `delta_summary` key
- Fields: `timestamp`, `pre_retrofit_state`, `post_retrofit_state`, `changes[]`, `new_files[]`, `deleted_files[]`, `modified_files[]`
- Each change record includes: `fact_key`, `before`, `after`, `operation` (MOVED/CREATED/MODIFIED/DELETED)
- Human use: single-view summary of "surgery" applied to the project
- Integration: stored alongside provenance as retrofit artifact

### Human gates (Non-negotiable)

- All three detection gates require explicit Human confirmation before proceeding
- Conflicting blueprint vs current state requires stop and ask (not auto-resolve)
- Destructive operations (file moves, deletions, config overwrites) require Pre-Destructive Check with Git safety validation
- Retrofit must never proceed when Git working tree is Dirty

### Fail-safe principle

- When in doubt, ask Human rather than auto-resolve
- If any two gates trigger simultaneously, prioritize Shadow File Detection, then Implicit Config Mining, then Pre-Destructive Check
- All gate interactions must be explicitly documented in examples

## Boundaries / Exclusions

- this skill does not **validate** retrofit requirements beyond syntax
  - validation responsibility belongs upstream in Human / planner review
- this skill does not **execute** assertions
  - assertion execution and acceptance verification happen downstream in `sense_env.py --mode acceptance`
- this skill does not **replace** Human-authored design or business logic
  - it only restructures the project baseline and configuration
- this skill does not **auto-merge** conflicting configurations
  - merge decisions remain Human responsibility
- this skill does not **generate** copilot-instructions content
  - instructions generation is handled by `copilot-instructions-init`

## Status / Allowed Transitions

- **Current**: `approved`
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

- **Routing notes**:
  - This topic uses standard Phase 4.5 rule (independent reviewer required)
  - All three detection gates must be validated in examples before approval

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/python-project-retrofit/python-project-retrofit.plan.md` | Planning actor | Repo-visible execution contract for this topic |
| Skill implementation | `.github/skills/python-project-retrofit/SKILL.md` | Creator | Executable instruction contract with trigger, process, outputs, boundaries |
| Examples | `.github/skills/python-project-retrofit/examples.md` | Creator | Detailed positive/negative scenarios covering all three gates and Delta Report interpretation |
| Conflict resolution guide | `.github/skills/python-project-retrofit/references/retrofit-conflict-resolution.md` | Creator | Shadow File Detection strategies, Implicit Config Mining decision tree, resolution options |
| Safety guidelines | `.github/skills/python-project-retrofit/references/retrofit-safety-guidelines.md` | Creator | Git working tree checks, destructive operation list, backup strategies |
| Delta contract | `.github/skills/python-project-retrofit/references/sensing-delta-contract.md` | Creator | Sensing Delta Report JSON schema, field semantics, interpretation guide |
| Provenance record | `.github/skills-provenance.json` | Creator | Repo-visible provenance entry for retrofit creation metadata and Delta Report linkage |

**Artifact path notes**:
- This topic does not modify `README.md`, `VERSION`, or `.github/copilot-instructions.md`
- Artifact paths are bounded to the skill folder plus `.github/skills-provenance.json`; no other repo-visible outputs are in scope
- If creator work drifts outside these listed paths or adds new top-level paths without explicit scope, reviewer should block and request re-scoping

## Implementation Steps

Creator will:

1. Read this topic plan and all reference files from `python-project-init-greenfield` and `cli-workflow-alignment`
2. Design retrofit-plan.md parsing logic (fixed section order, YAML assertions)
3. Implement Git working tree validation (blocking on Dirty state)
4. Implement Shadow File Detection gate:
   - Identify files with duplicate semantic intent but different paths
   - Enumerate resolution options (move/delete/coexist/abort)
   - Prompt Human with clear choices
   - Block retrofit until confirmed
5. Implement Implicit Config Mining gate:
   - Scan for tool-chain remnants and configuration files
   - Ask Human about origin (migration/delete/preserve)
   - Block retrofit until confirmed
6. Implement Pre-Destructive Check gate:
   - Before file move, deletion, or config overwrite, validate Git state
   - Require `git commit` or backup production before proceeding
   - Hard-block if Dirty and no backup confirmed
7. Implement safe project restructuring:
   - Apply Human-confirmed changes
   - Record operations with rollback information
8. Implement Sensing Delta Report generation:
   - Re-sense project state after retrofit
   - Compare pre/post state snapshots
   - Generate clear before/after change records
   - Output JSON with all required fields
9. Implement provenance recording:
   - Add retrofit entry to `.github/skills-provenance.json`
   - Include timestamp, creator, Delta Report reference
10. Hand off to acceptance: `sense_env.py --mode acceptance --contract-file retrofit-plan.md`

## Validation / Acceptance Checks

Reviewer and Main Agent should verify:

- ✅ All three detection gates are implemented and documented with clear examples
- ✅ Gate interactions (simultaneous triggers) are explicitly documented
- ✅ Shadow File Detection examples include move, delete, coexist, abort scenarios
- ✅ Implicit Config Mining examples include migration, deletion, preservation scenarios
- ✅ Git working tree validation blocks Dirty state with clear error message
- ✅ Pre-Destructive Check is enforced before file moves/overwrites
- ✅ Sensing Delta Report JSON schema matches contract (timestamp, changes[], new_files[], deleted_files[], modified_files[])
- ✅ Human confirmation is required before any operation that could lose data
- ✅ Provenance recording includes retrofit metadata
- ✅ All artifact paths are exact and bounded as specified
- ✅ Examples cover success paths (clean retrofit) and failure modes (conflicts, safety blocks)
- ✅ Boundaries are respected: no auto-merge, no copilot-instructions generation, no infrastructure changes

## Reviewer Handoff

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

**Additional contract requirements for this higher-risk skill**:
- Reviewer must confirm that all three gates are non-negotiable and cannot be bypassed
- Reviewer must validate that Human confirmation gates truly block (not just warn)
- Reviewer must assess whether the fail-safe principle is consistently applied
- Reviewer must verify that Sensing Delta Report provides clear, actionable before/after visibility

## Post-merge / release actions

No repository release or stable-library actions are required.

After merge:
- Branch cleanup (via `git-post-merge-workflow`)
- Next phase: awaiting `copilot-instructions-init` topic planning

## Open Questions / Unresolved Items

None. All design decisions have been locked in the three-tier detection gates and safety guidelines.

Retrofit-plan.md schema and examples will be addressed in a future `python-first-project-planning` topic.
