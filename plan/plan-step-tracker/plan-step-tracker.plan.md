# Topic Plan: plan-step-tracker

**Status**: `planned`

---

## Analysis Layer Input (Strict Mode)

This topic plan operates in **strict mode** (per `plan-creator` requirements) because both analysis-layer artifacts exist and are frozen:

- **`analysis/plan-step-tracker/requirements.md` v2 (FROZEN)**
  - R1–R9 enumerated; C1–C3 resolved
  - Explicit boundary: single `.step.md` per topic, `[ ]`/`[X]` content-line markers only, binary states (done/pending)
  - Non-goals: cross-topic queries, file watching, state modification, SQL integration

- **`analysis/plan-step-tracker/technical-spec.md` v2 (FROZEN)**
  - Maps R1–R9 to technical realization
  - Core artifacts: `scripts/step_tracker.py` (Python CLI, uv script), `tests/test_step_tracker.py` (pytest 6 test classes)
  - Skill folder: `SKILL.md` (Python CLI primary, grep fallback), `reference.md` (format + patterns), `examples.md` (required: 4 operations + blocking + edge case)
  - README + VERSION 0.41.0 → 0.42.0

**Strict-mode contract**: This plan SHALL map 100% to `technical-spec.md`. Implementation Steps derive directly from technical artifacts and cost-of-realization workstreams. No scope drift. No new chat-time instructions override the frozen analysis.

---

## Goal / Outcome

Enable Main Agent and users to query step tracking status (pending/done) for `plan/<topic>/<topic>.step.md` files with minimal token cost and explicit blocking when incomplete.

**Concrete repository-visible result:**
- `.github/skills/plan-step-tracker/` skill folder: Agent Skill with SKILL.md, reference.md, examples.md
- `scripts/step_tracker.py` deployed: Python CLI (uv script) with 4 subcommands (read_all, read_not_run, read_success, check_all_succeeded)
- `tests/test_step_tracker.py` deployed: pytest suite covering R1–R9 with 6 test classes
- `README.md` updated: New row in "Current skills" table
- `VERSION` bumped: 0.41.0 → 0.42.0

---

## Scope

### In scope

- **`.github/skills/plan-step-tracker/` folder**
  - `SKILL.md`: Operational contract; Python CLI prioritized; grep fallback mechanism
  - `reference.md`: Format specification (`.step.md` YAML + content-line markers), grep pattern reference, `[x]` warning rule
  - `examples.md`: 4 operations (read_all, read_not_run, read_success, check_all_succeeded), blocking example, edge cases

- **`scripts/step_tracker.py`** (Python ≥ 3.11, uv script header)
  - Entry point: `python scripts/step_tracker.py <operation> <topic>`
  - `Step` dataclass: `text: str`, `status: Literal["done", "pending"]`
  - `parse_steps(topic, plan_dir)` → filters `.step.md` content lines `^\- \[.\]`
  - 4 subcommands:
    - `read_all`: Return all steps with status
    - `read_not_run`: Return pending steps only
    - `read_success`: Return done steps only
    - `check_all_succeeded`: Return SUCCESS (exit 0) or BLOCKED + list (exit 1)
  - Warning for `[x]` lowercase → treat as pending, output warning

- **`tests/test_step_tracker.py`** (pytest)
  - 6 test classes covering R1–R9:
    - `TestParseStatus`: `[X]` → done, `[ ]` → pending, non-matching lines ignored, `[x]` → pending + warning
    - `TestReadNotRun`: Mixed → pending only; all done → empty list
    - `TestReadSuccess`: Mixed → done only; all pending → empty list
    - `TestReadAll`: N checkbox lines → N Step objects
    - `TestCheckAllSucceeded`: All done → exit 0; has pending → exit 1 + list
    - `TestEdgeCases`: Empty file, `.step.md` not found (FileNotFoundError), no checkbox lines
  - Use `tmp_path` fixture; no real `plan/` directory reads

- **Repository documents**
  - `README.md`: Add 1 row to "Current skills" table
  - `VERSION`: Bump 0.41.0 → 0.42.0

### Out of scope

- Cross-topic step queries (non-goal per R7)
- File watching or real-time monitoring (non-goal)
- State modification (read-only skill per R7 assumption 5)
- SQL todos table integration (non-goal)
- Non-.step.md files (non-goal)
- Integration tests on live `plan/` directory (unit tests only per R9)
- support for multi-step files per topic (single file convention per R7)
- Deferred analysis or post-implementation planning

---

## Locked Decisions

1. **Format choice (C1 resolved)**: Content-line markers only (`- [X]`/`- [ ]` at start of markdown list items). Frontmatter and headers excluded automatically by `^\- \[.\]` regex. No YAML frontmatter status fields.

2. **Python CLI as primary execution layer (C3 resolved)**: Python `scripts/step_tracker.py` is the canonical implementation. SKILL.md directs Agent to invoke Python CLI first; grep is documented fallback only. Benefits: testable, cross-platform, exit code control for CI blocking.

3. **Scope timing**: This is a stable-library-affecting topic (new skill + VERSION bump + README update). Changes deploy at `publish-in-progress` (not deferred to release).

4. **No rollback needed**: C1, C2, C3 all resolved in frozen technical-spec. All R1–R9 feasible. No architectural conflicts. No infra dependencies.

---

## Boundaries / Exclusions

- **Creator work**: Implement only the artifacts listed in `Artifact Paths` below. Do not modify unrelated skills or create new conventions outside `plan-step-tracker`.
- **Reviewer work**: Evaluate creator's output against frozen technical-spec and `plan-step-tracker` checklist. Do not re-decide C1/C2/C3 or scope.
- **Post-review**: Stable library updates (README + VERSION) happen in `publish-in-progress` phase, not after.
- **Role separation**: Creator and Reviewer are independent. Reviewer uses `agent-skill-reviewer` subagent, not shared creator session.

---

## Status / Allowed Transitions

**Current status**: `planned`

**Execution model**: Standard creator → reviewer → publish → merge path. No deferred release phase (changes become stable at `publish-in-progress` with README/VERSION updates).

**Allowed transitions** (per `plan/agent-handoff-workflow.md`):
- `planned` → `creator-in-progress`
- `creator-in-progress` → `review-ready`
- `review-ready` → `reviewer-in-progress`
- `reviewer-in-progress` → `approved` | `needs-rework`
- `needs-rework` → `creator-in-progress`
- `approved` → `publish-in-progress`
- `publish-in-progress` → `pr-open`
- `pr-open` → `merged` (via human merge on GitHub)
- `merged` → terminal

**Routing note**: This topic uses standard Phase 4.5 (planner contract alignment is trivial because strict-mode analysis already locked all scope and artifacts). Main Agent may route directly from `approved` to `publish-in-progress` unless late defects require rework.

---

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/plan-step-tracker/plan-step-tracker.plan.md` | Planning actor | Repo-visible execution contract for this topic |
| Skill folder | `.github/skills/plan-step-tracker/` | Creator | Agent Skill implementation |
| SKILL.md | `.github/skills/plan-step-tracker/SKILL.md` | Creator | Operational contract + Python CLI primary + grep fallback |
| reference.md | `.github/skills/plan-step-tracker/reference.md` | Creator | Format spec + grep patterns + `[x]` warning rule |
| examples.md | `.github/skills/plan-step-tracker/examples.md` | Creator | 4 operations + blocking + edge cases |
| Python CLI | `scripts/step_tracker.py` | Creator | Executable Python uv script; 4 subcommands; exit code control |
| Tests | `tests/test_step_tracker.py` | Creator | pytest suite; 6 test classes; tmp_path fixture |
| README.md | `README.md` (current-skills row) | Main Agent | Stable-library update at publish-in-progress |
| VERSION | `VERSION` | Main Agent | Bump 0.41.0 → 0.42.0 at publish-in-progress |

**Artifact path notes:**
- All skill files live under `.github/skills/plan-step-tracker/` and are read-only stable-library assets once merged.
- `README.md` and `VERSION` are modified by Main Agent during Phase 5 (stable library handling), not by Creator.
- If Creator output drifts outside these paths (e.g., adds new files, modifies README early), that is a plan-alignment failure.

---

## Stable library metadata

**Status**: This topic affects stable-library surfaces.

- **README row**: Add 1 new row to "Current skills" table in `README.md`; exact wording TBD by Creator (suggest: "plan-step-tracker | Query step status for `plan/<topic>/<topic>.step.md` files; Python CLI or grep"). Row placement: after alphabetically-prior skill or at end if no alphabetic order enforced.

- **VERSION bump**: From `0.41.0` (MINOR) to `0.42.0` (new stable skill triggers MINOR bump per SemVer).

- **Timing**: Changes become stable at `publish-in-progress` (not deferred to release). Main Agent updates README and VERSION in Phase 5, then commits all changes together in Phase 6.

- **Rationale**: `plan-step-tracker` is a new stable skill extending Agent capabilities. README advertises it; VERSION marks the release boundary. No deferred release needed.

---

## Implementation Steps

Creator SHALL complete the following, staying within strict-mode technical-spec mapping:

### Step Group 1: Python CLI (scripts/step_tracker.py)

1. **Parse step files**
   - Implement `Step` dataclass with `text: str`, `status: Literal["done", "pending"]`
   - Implement `parse_steps(topic: str, plan_dir: Path) -> list[Step]`
   - Logic: Read `plan/<topic>/<topic>.step.md`; regex `^\- \[.\]` lines; extract checkbox status and text
   - `[X]` (uppercase) → done; `[ ]` (space) → pending; `[x]` (lowercase) → pending + warning to stderr

2. **Implement 4 subcommands**
   - `read_all <topic>`: Print all steps (done and pending); format: `[X] step text` or `[ ] step text`
   - `read_not_run <topic>`: Print pending steps only; exit 0 always
   - `read_success <topic>`: Print done steps only; exit 0 always
   - `check_all_succeeded <topic>`: If pending count = 0, print "SUCCESS: N steps completed"; exit 0. Else print "BLOCKED: M pending steps" + list pending steps; exit 1.

3. **CLI scaffolding**
   - Use argparse (subparser for 4 operations)
   - uv script header: `# /// script` with `requires-python = ">=3.11"`
   - Entrypoint: `python scripts/step_tracker.py <operation> <topic>`
   - Error handling: `.step.md` not found → explicit FileNotFoundError + stderr message + exit 1

### Step Group 2: pytest suite (tests/test_step_tracker.py)

1. **TestParseStatus**
   - `[X]` → done; `[ ]` → pending; `[x]` → pending + warning assertion
   - Non-matching lines (frontmatter, headers, plain text) → not parsed

2. **TestReadNotRun**
   - Mixed state → only pending returned
   - All done → empty list returned
   - Assertion: output contains no done steps

3. **TestReadSuccess**
   - Mixed state → only done returned
   - All pending → empty list returned
   - Assertion: output contains no pending steps

4. **TestReadAll**
   - N checkbox lines → N Step objects returned
   - Assertion: count matches

5. **TestCheckAllSucceeded**
   - All done → print "SUCCESS" + exit code 0
   - Has pending → print "BLOCKED" + list + exit code 1

6. **TestEdgeCases**
   - Empty `.step.md` (frontmatter only) → 0 steps
   - `.step.md` not found → FileNotFoundError raised
   - File with no checkbox lines → 0 steps

Use `tmp_path` pytest fixture for test data; do not read real `plan/` directory.

### Step Group 3: Agent Skill folder (.github/skills/plan-step-tracker/)

1. **SKILL.md**
   - Frontmatter: `name: plan-step-tracker`, `description: <short>`, required sections per SKILL.md template
   - Purpose: Query step status from plan-step-tracker files
   - Trigger: When Agent needs to check incomplete steps during plan execution
   - Inputs: topic name
   - Process:
     - Primary: Call `python scripts/step_tracker.py <operation> <topic>`
     - Fallback: Use grep (e.g., `grep -c '^\- \[ \]' plan/<topic>/<topic>.step.md`)
   - Examples: At least 1 positive + 1 negative (e.g., "check incomplete steps for topic X" vs. "cross-topic queries not supported")
   - Outputs: Step list + status
   - Boundaries: Single topic only; read-only
   - Local references: reference.md (format + grep patterns), examples.md (detailed cases)

2. **reference.md**
   - `.step.md` format spec: YAML frontmatter + content-line markers `- [ ]` or `- [X]`
   - Grep pattern reference: Examples for each operation (pending, done, all, count)
   - `[x]` lowercase rule: Only `[X]` uppercase is valid; `[x]` treated as pending + warning
   - Grouping convention: Mirror plan.md structure; no new groupings

3. **examples.md**
   - Detailed example: `read_all` for a multi-step topic (show output format)
   - Detailed example: `read_not_run` showing blocking (list pending steps)
   - Detailed example: `read_success` showing completed workflow
   - Detailed example: `check_all_succeeded` blocking on pending + exit code for CI
   - Edge case: Empty topic.step.md
   - Edge case: File not found

### Step Group 4: Repository updates

1. **README.md**
   - Add 1 new row to "Current skills" table
   - Example row: `plan-step-tracker | Query step status (pending/done) for plan tracking; Python CLI or grep`
   - Placement: Maintain alphabetical order if applicable, else end of table

2. **VERSION**
   - Bump from `0.41.0` to `0.42.0`

---

## Validation / Acceptance Checks

Creator work is **review-ready** when all of the following pass:

1. **Path exactness**
   - All 8 artifacts listed in `Artifact Paths` exist at their stated locations
   - No new files outside stated paths (e.g., no extra scripts, no README modifications by Creator)
   - README/VERSION changes are deferred to Main Agent (Phases 5–6)

2. **Python CLI functionality**
   - `python scripts/step_tracker.py read_all test-topic` returns all steps (done + pending)
   - `python scripts/step_tracker.py read_not_run test-topic` returns pending only (empty if all done)
   - `python scripts/step_tracker.py read_success test-topic` returns done only (empty if all pending)
   - `python scripts/step_tracker.py check_all_succeeded test-topic` exits 0 if all done; exit 1 if any pending; BLOCKED message shows pending list
   - `[x]` lowercase triggers warning to stderr but treats step as pending

3. **pytest suite quality**
   - All 6 test classes present: TestParseStatus, TestReadNotRun, TestReadSuccess, TestReadAll, TestCheckAllSucceeded, TestEdgeCases
   - Each test class has ≥2 test methods covering success + failure paths
   - `tmp_path` fixture used (no real `plan/` directory read during tests)
   - `pytest tests/test_step_tracker.py` returns all green

4. **Skill folder completeness**
   - `.github/skills/plan-step-tracker/SKILL.md` includes all required sections (Purpose, Trigger, Inputs, Process, Examples, Outputs, Boundaries, Local references)
   - SKILL.md contains ≥1 positive + ≥1 negative example
   - `reference.md` includes format spec + grep patterns + `[x]` warning rule
   - `examples.md` includes ≥4 operation examples + 1 blocking example + ≥2 edge cases
   - All paths and references are exact (no "see reference" vagueness)

5. **Strict-mode alignment**
   - All Implementation Steps map 1:1 to technical-spec workstreams (Step Groups 1–4)
   - No new scope, no scope reduction without plan update
   - No decisions re-made; frozen C1/C2/C3 honored throughout

---

## Reviewer Handoff

**Reviewer SHALL** read the completed creator draft and return a JSON verdict:

```json
{
  "verdict": "approved|needs-rework",
  "blocking_issues": [
    {
      "issue": "Description of blocking defect or scope drift",
      "file": "Affected artifact path",
      "fix": "Required fix or clarification"
    }
  ],
  "copilot_feedback_triage": {
    "ADDRESS": [
      {
        "comment": "Copilot feedback text",
        "reason": "Why this must be addressed before merge"
      }
    ],
    "DISCUSS": [
      {
        "comment": "Copilot feedback text",
        "reason": "Minor; discuss with Creator but not blocking"
      }
    ],
    "SKIP": [
      {
        "comment": "Copilot feedback text",
        "reason": "Not applicable to this repository or topic intent"
      }
    ]
  }
}
```

**Reviewer verification checklist:**
- All paths in creator output match `Artifact Paths` section above
- SKILL.md, reference.md, examples.md all present and aligned with technical-spec
- Python CLI implements all 4 subcommands and exit-code rules
- pytest suite covers all 6 test classes; `tmp_path` used throughout
- No scope drift from strict-mode technical-spec
- No pre-emptive README/VERSION modifications
- Copilot feedback categorized appropriately (ADDRESS/DISCUSS/SKIP)

**Reviewer independence**: Use `agent-skill-reviewer` subagent for this evaluation; do not share Creator's implementation session.

---

## Post-merge / release actions

**Phase 5 (Stable library handling)**:
- Main Agent updates `README.md`: Add 1 row to "Current skills" table (Creator drafts example text in PR comments; Main Agent applies)
- Main Agent updates `VERSION`: Bump 0.41.0 → 0.42.0

**Phase 6 (Commit, push, PR)**:
- Main Agent commits skill folder + README + VERSION together
- PR includes: new `.github/skills/plan-step-tracker/` directory, updated README row, VERSION bump

**Phase 10 (Release)**:
- Not applicable. Changes become stable immediately upon merge. No deferred release phase.
- Tag is created per standard release process (outside this topic's scope).

---

## Open Questions / Unresolved Items

None. Both analysis-layer artifacts are frozen v2. All R1–R9 are mapped. C1–C3 are resolved. Boundaries are locked.

**Creator may ask for clarification:**
- Exact wording for README row (suggested by Creator in PR; Main Agent confirms)
- Order of examples in examples.md (provided by technical-spec; Creator prioritizes per risk)
- Python package structure (single module `step_tracker.py` as uv script; no subpackage)

**These are implementation details, not plan changes.**
