---
name: python-project-retrofit
description: Retrofit an existing Python repository to a locked `retrofit-plan.md` baseline with mandatory human gates for shadow-file conflicts, implicit config remnants, Git safety blocking, and acceptance handoff through `sense_env.py`.
---

# Purpose
Retrofit an existing Python project to align with governed initialization standards without losing human control over conflicts, destructive actions, or acceptance.

# Trigger / When to use
Use this skill when:
- an existing Python repository already has an approved `retrofit-plan.md`
- the task is to reorganize an established project toward a target structure rather than create a greenfield baseline
- the workflow must detect shadow files, mine implicit configuration remnants, and emit a Sensing Delta Report before acceptance
- the retrofit must hand off immediately to `python3 .github/skills/sense-env-scaffold/scripts/sense_env.py --mode acceptance --contract-file retrofit-plan.md`

Do not use this skill when:
- the repository is greenfield or baseline-only; use `python-project-init-greenfield`
- `retrofit-plan.md` is missing, malformed, or still under negotiation
- the task is only to tweak one file, generate business logic, or author `.github/copilot-instructions.md`
- the user expects the agent to auto-merge conflicting config files or guess through ambiguous structure changes

# Inputs
- the target repository root
- the locked `retrofit-plan.md` path
- the current filesystem state, including existing entrypoints, packages, and config remnants
- current Git working-tree state before any move, deletion, or overwrite
- explicit human decisions for Gate 1 and Gate 2, plus destructive-operation confirmation when a clean or backed-up path is ready
- the provenance destination at `.github/skills-provenance.json`

# Process
1. Confirm retrofit fit first.
   - Read `retrofit-plan.md`.
   - Require the locked sections `## Project Overview`, `## Target Structure`, and `## Acceptance Criteria`.
   - Require a parseable ````yaml [sensing-assertions]```` block under `## Acceptance Criteria`.
   - Stop on syntax or contract errors instead of guessing.
2. Capture the pre-retrofit state.
   - Sense the current layout, package paths, entrypoints, and toolchain remnants.
   - Record the facts that will later populate the Sensing Delta Report.
3. Parse the target structure and acceptance contract from `retrofit-plan.md`.
   - Treat prose notes as human context only.
   - Do not reinterpret missing targets or invent migration policy.
4. Run **Gate 1: Shadow File Detection** before any restructure.
   - Detect duplicate semantic intent at different paths, such as a root `app.py` versus a target `src/service/main.py`.
   - Present exactly four human choices: **move**, **delete**, **coexist**, or **abort**.
   - Do not continue until the human chooses one option for each conflict.
5. Run **Gate 2: Implicit Config Mining** after Gate 1 is resolved.
   - Scan for `poetry.lock`, `pyproject.toml`, `setup.py`, `setup.cfg`, `.venv`, `conda.yml`, `requirements.txt`, and `Pipfile`.
   - Present exactly four human choices when remnants are found: **migrate**, **delete**, **preserve**, or **abort**.
   - Do not continue until the human confirms the disposition of each config family.
6. Respect the locked gate order.
   - If multiple gates trigger together, handle Gate 1 first, then Gate 2, then Gate 3.
   - Keep each gate explicit; do not collapse several conflicts into a vague “continue?” prompt.
7. Run **Gate 3: Git safety and pre-destructive check** before any move, deletion, or overwrite.
   - Inspect Git working-tree status immediately before the destructive step.
   - If the tree is dirty, hard-block the retrofit.
   - Require an explicit human path of either committing existing changes or creating a backup before destructive work can resume.
   - This gate cannot be bypassed.
8. Apply only human-confirmed retrofit operations.
   - Move, delete, preserve, or migrate only what the human approved.
   - Never auto-merge conflicting configurations.
   - If config divergence would require line-by-line synthesis, stop and ask which file survives or how migration should be scoped.
9. Generate the Sensing Delta Report after the retrofit changes land.
   - Emit JSON with a top-level `delta_summary` object.
   - Include `timestamp`, `pre_retrofit_state`, `post_retrofit_state`, `changes`, `new_files`, `deleted_files`, and `modified_files`.
   - For every change record include `fact_key`, `before`, `after`, and `operation`, where `operation` is one of `MOVED`, `CREATED`, `MODIFIED`, or `DELETED`.
10. Record provenance in `.github/skills-provenance.json`.
    - Record the retrofit date, creator, and Delta Report reference.
    - Keep provenance repo-visible and governance-oriented.
11. Close the loop with acceptance.
    - Hand off to `python3 .github/skills/sense-env-scaffold/scripts/sense_env.py --mode acceptance --contract-file retrofit-plan.md`.
    - If acceptance cannot run, report the blocking reason instead of claiming success.
12. Clean up scratch artifacts created during the retrofit flow while preserving `retrofit-plan.md`, the Delta Report artifact, and provenance.

# Examples
- Positive: Read a locked `retrofit-plan.md`, detect that root `app.py` shadows the planned `src/weather_service/main.py`, stop for a human `move` decision, ask whether `poetry.lock` should `migrate` or `preserve`, hard-block a dirty working tree before any file move, emit the Sensing Delta Report, then hand off to `python3 .github/skills/sense-env-scaffold/scripts/sense_env.py --mode acceptance --contract-file retrofit-plan.md`.
- Negative: Silently merge `setup.cfg` into `pyproject.toml`, move files while `git status` is dirty, or continue past ambiguous conflicts because the retrofit “looks obvious.”

# Outputs
- an existing Python project restructured to the approved `retrofit-plan.md` target
- explicit human gate outcomes for shadow files, implicit configs, and destructive paths
- a Sensing Delta Report JSON artifact with before/after facts and `MOVED` / `CREATED` / `MODIFIED` / `DELETED` operations
- provenance recorded in `.github/skills-provenance.json`
- an acceptance handoff result or a concrete blocking error

# Verification
- confirm `retrofit-plan.md` contains the locked sections and a valid `[sensing-assertions]` block
- confirm all three gates block progress rather than warn passively
- confirm dirty Git state stops destructive retrofit until the human commits or produces a backup
- confirm examples cover `move` / `delete` / `coexist` / `abort`, `migrate` / `delete` / `preserve` / `abort`, and simultaneous-gate ordering
- confirm the Delta Report uses the required JSON fields and only the allowed operations
- confirm acceptance uses the exact `sense_env.py --mode acceptance --contract-file retrofit-plan.md` handoff

# Red Flags
- a request to “just pick the most likely path” for conflicting files or configs
- conflicting config surfaces that would need heuristic line-by-line merging
- a dirty working tree immediately before a move, delete, or overwrite
- simultaneous gate hits being collapsed into one generic prompt
- a claim that acceptance can be skipped because the filesystem now looks correct

# Common Rationalizations
- “These files probably mean the same thing, so move them automatically.”
- “We can merge `pyproject.toml` and `setup.cfg` heuristically.”
- “The repo is dirty, but Git can recover it later.”
- “We will generate the Delta Report after acceptance if someone asks.”
- “Abort is unnecessary because one of the other options is probably safe.”

# Boundaries
- Do not validate retrofit requirements beyond syntax; design quality belongs upstream to the planner and human review.
- Do not execute or broaden acceptance assertions; `sense_env.py --mode acceptance` owns assertion execution.
- Do not replace human-authored design or business logic; only restructure baseline and configuration surfaces.
- Do not auto-merge conflicting configurations.
- Do not generate `.github/copilot-instructions.md` content.
- Do not proceed through any gate without explicit human confirmation.

# Local references
- `examples.md`: detailed multi-gate retrofit scenarios, failure modes, and anti-patterns
- `references/retrofit-conflict-resolution.md`: Shadow File Detection, Implicit Config Mining, gate ordering, and stop-and-ask resolution rules
- `references/retrofit-safety-guidelines.md`: Git safety checks, destructive-operation rules, backup expectations, and hard-block behavior
- `references/sensing-delta-contract.md`: Sensing Delta Report schema, operation semantics, and interpretation guidance
