## Analysis-layer routing

- Mode: `strict`
- Requirements baseline:
  `analysis/skills-canonical-inventory/requirements.md`
  - SHA-256: `c65500a8fe26d0e325e631bc483be6c9983a9d6498627d799cb1ed6d279e754e`
- Technical baseline:
  `analysis/skills-canonical-inventory/technical-spec.md`
  - SHA-256: `47735142a8291b0123e1433545c532657e74852d255d6e99096b763ae3cfec89`
- Priority rule: this topic plan and later creator execution must map 100% to
  the technical baseline above. The requirements baseline remains the business
  guardrail. No human `override` instruction exists for this topic.

# Skills Canonical Inventory Plan

## Goal / Outcome

Produce a bounded implementation contract for a deterministic inventory of the
canonical `skills/` tree only.

When this topic is complete:

- `scripts/build_skills_inventory.py` exists as the repository-local builder
  for canonical skill inventory
- `artifacts/skills-inventory.jsonl` exists as deterministic UTF-8 JSON Lines
  output with one complete record per in-scope canonical skill root
- the resulting inventory reflects only top-level canonical `skills/` content
  and excludes projection, agent, runtime, and release surfaces

## Scope

### In scope

- maintain topic-local planning artifacts for this topic:
  - `plan/skills-canonical-inventory/skills-canonical-inventory.plan.md`
  - `plan/skills-canonical-inventory/skills-canonical-inventory.step.md`
  - `plan/skills-canonical-inventory/skills-canonical-inventory.checklist.md`
- use these frozen analysis inputs as read-only prerequisites:
  - `analysis/skills-canonical-inventory/requirements.md`
  - `analysis/skills-canonical-inventory/technical-spec.md`
- later creator implementation is limited to:
  - canonical skill discovery under top-level `skills/` only
  - deterministic per-skill `tree_hash` computation using the already-frozen
    hash contract
  - deterministic JSONL emission at
    `artifacts/skills-inventory.jsonl`
  - safe publish / explicit failure behavior in
    `scripts/build_skills_inventory.py`
  - bounded test coverage for the inventory builder at
    `tests/test_build_skills_inventory.py`

### Out of scope

- `agents/` or custom-agent inventory
- `.github/skills/`, `.codex/skills/`, or any other `.<platform>/skills/`
  projection surface
- runtime orchestration, projection sync, release automation, or non-skill
  artifact inventory
- any README, VERSION, stable-library, or release-note work
- any implementation file outside the exact artifact set declared below

### Modify

- planning actor may modify only:
  - `plan/skills-canonical-inventory/skills-canonical-inventory.plan.md`
  - `plan/skills-canonical-inventory/skills-canonical-inventory.step.md`
  - `plan/skills-canonical-inventory/skills-canonical-inventory.checklist.md`
- after human check and implementation start, creator may modify only:
  - `scripts/build_skills_inventory.py`
  - `artifacts/skills-inventory.jsonl`
  - `tests/test_build_skills_inventory.py`

### Read-only

- `analysis/skills-canonical-inventory/requirements.md`
- `analysis/skills-canonical-inventory/technical-spec.md`
- canonical source input surface `skills/**`
- out-of-scope surfaces:
  - `agents/**`
  - `.github/**`
  - `.codex/**`
  - `README.md`
  - `VERSION`

## Locked Decisions

- This topic is not a stable-library publish topic. No `README.md` update,
  `VERSION` bump, tag, or release action is allowed.
- The topic remains bounded to canonical `skills/` inventory only.
- The only later implementation targets are:
  - `scripts/build_skills_inventory.py`
  - `artifacts/skills-inventory.jsonl`
  - `tests/test_build_skills_inventory.py`
- One in-scope inventory unit equals one directory under top-level `skills/`
  that contains `SKILL.md`.
- The minimum record contract stays bounded to the technical baseline:
  one canonical skill-root path field and one `tree_hash` field per line.
- The `tree_hash` contract is already frozen and must not be redefined in this
  topic.
- The exact `tree_hash` byte stream for this topic is locked to skill-root-
  relative POSIX paths in lexicographic order, hashed as:
  `relative_path + NUL + file_bytes + NUL` for each included file.
- `skills/**` is an input surface for discovery and hashing, not an editable
  surface in this topic.
- `plan/skills-canonical-inventory/skills-canonical-inventory.review-log.md`
  is not created yet. If reviewer feedback later controls routing or creates a
  multi-round rework loop, execution must stop and amend the plan before
  continuing without silently relying on chat history.
- Any need for helper modules, docs, projection updates, or additional
  implementation paths beyond the locked script, artifact, and single bounded
  test file is plan drift and requires replanning before creator work
  continues.

## Boundaries / Exclusions

### Non-goals

- redesigning the hash contract or junk exclusions
- widening scope into agent inventory or projection-surface inventory
- changing repository governance or canonical-source definitions
- implementing runtime loading, registry semantics, or installer behavior
- entering implementation during this planning handoff

### Workflow boundaries

- planning actor authors the plan, step, and checklist artifacts only
- creator later implements within the locked write set only
- reviewer evaluates the plan or later implementation independently
- planner final gate happens only after reviewer approval is reflected in
  repo-visible truth
- human check is a required stop before any implementation work begins

### Stop conditions

- if later execution needs any file outside the exact artifact paths below,
  stop and repair the plan before continuing
- if analysis intent appears to conflict with later chat-time convenience and no
  explicit human `override` exists, stop and route back to planning
- if reviewer routing becomes active and no repo-visible review log has been
  added, stop instead of simulating that handoff in hidden context

## Status / Allowed Transitions

- **Current**: `creator-in-progress`
- **Execution model**: follow the canonical creator -> reviewer -> publish ->
  merge path, with no release action for this topic
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

Routing notes:

- The human-locked planning progression for this handoff is:
  `create worktree` ->
  `.github/prompts/create-analysis.prompt.md` ->
  `.github/prompts/create-agent-plan.prompt.md` ->
  `draft plan commit by topic` ->
  `plan-reviewer review and feedback` ->
  `plan-creator fix and update and feedback` ->
  `planner final gate` ->
  `wait human check`
- The planning workflow above is complete in repo-visible truth; human check
  has passed and creator implementation may proceed within the locked write
  set.
- This topic does not declare `merged` -> `released`.

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Requirements baseline | `analysis/skills-canonical-inventory/requirements.md` | Planning actor | Frozen business baseline for canonical inventory scope |
| Technical baseline | `analysis/skills-canonical-inventory/technical-spec.md` | Planning actor | Execution-facing technical baseline for the bounded implementation |
| Topic plan | `plan/skills-canonical-inventory/skills-canonical-inventory.plan.md` | Planning actor | Repo-visible execution contract for this topic |
| Topic progression artifact | `plan/skills-canonical-inventory/skills-canonical-inventory.step.md` | Planning actor / Main Agent | Current-truth progression artifact for the locked planning workflow |
| Topic planning checklist | `plan/skills-canonical-inventory/skills-canonical-inventory.checklist.md` | Planning actor | Topic-specific review and final-gate checklist for planning artifacts |
| Inventory builder script | `scripts/build_skills_inventory.py` | Creator | Canonical-scope inventory builder defined by the technical baseline |
| Inventory artifact | `artifacts/skills-inventory.jsonl` | Creator | Deterministic JSONL output for canonical skill inventory |
| Inventory builder tests | `tests/test_build_skills_inventory.py` | Creator | Bounded verification for canonical discovery, stable output, hash sensitivity, and junk exclusion |

Artifact path notes:

- This topic does not modify `README.md`.
- This topic does not modify `VERSION`.
- This topic does not modify any file under `skills/**`; those paths are
  discovery inputs only.
- This topic does not modify `agents/**`, `.github/**`, or `.codex/**`.
- `plan/skills-canonical-inventory/skills-canonical-inventory.review-log.md`
  is intentionally absent at this stage because reviewer-routing state is not
  yet active.
- Treat the listed paths as an executable contract. Any need to touch another
  path is a plan-alignment failure, not a harmless implementation detail.

## Implementation Steps

1. Implement canonical skill discovery inside
   `scripts/build_skills_inventory.py` by scanning top-level `skills/` only,
   treating each directory that contains `SKILL.md` as one skill root,
   normalizing to canonical repo-relative paths, de-duplicating, and stable
   sorting before downstream work begins.
2. Implement deterministic `tree_hash` calculation for each discovered skill
   root using the already-frozen skill-root-relative SHA-256 stream and junk
   exclusions contract without redefining that contract in this topic. Use
   skill-root-relative POSIX paths in lexicographic order and hash the exact
   byte stream `relative_path + NUL + file_bytes + NUL` for each included
   file.
3. Implement deterministic UTF-8 JSONL emission at
   `artifacts/skills-inventory.jsonl` with one complete JSON object per skill
   root in stable record order and with the minimum record contract required by
   the technical baseline.
4. Implement safe publish behavior by writing to a temporary file in the target
   directory, validating line count and parseability, then atomically replacing
   `artifacts/skills-inventory.jsonl` only after validation succeeds.
5. Implement bounded tests at `tests/test_build_skills_inventory.py` covering
   canonical top-level `skills/` discovery, deterministic byte-stable output,
   `tree_hash` change on included-file changes, and `tree_hash` stability when
   only excluded junk files change.
6. Stop and route back to planning if creator work requires any file outside
   `scripts/build_skills_inventory.py`,
   `artifacts/skills-inventory.jsonl`, and
   `tests/test_build_skills_inventory.py`, or would widen scope beyond
   canonical `skills/` inventory.

## Validation / Acceptance Checks

### Checklist

- Use `plan/skills-canonical-inventory/skills-canonical-inventory.checklist.md`
  during independent plan review and planner final gate.
- The checklist must pass before the topic leaves the planning workflow and
  enters human check.

### Acceptance checks

- Coverage check:
  the artifact record count equals the number of directories under top-level
  `skills/` that contain `SKILL.md`, with zero duplicate canonical paths.
- Scope check:
  every emitted canonical path stays under `skills/`, and zero records come
  from `agents/`, `.github/skills/`, `.codex/skills/`, or another
  `.<platform>/skills/` root.
- Hash contract check:
  recomputation of each `tree_hash` under the frozen contract exactly matches
  the emitted value, using skill-root-relative POSIX paths in lexicographic
  order and the exact byte stream
  `relative_path + NUL + file_bytes + NUL`.
- Format check:
  every JSONL line parses as one JSON object and includes the minimum required
  record fields.
- Repeatability check:
  two runs against unchanged in-scope inputs produce byte-identical
  `artifacts/skills-inventory.jsonl`.
- Local-only check:
  generation and validation succeed without network access.
- Safe-failure check:
  unwritable-target or interrupted-publish conditions do not leave a new
  truncated final artifact that can be mistaken for success.
- Planning-boundary check:
  no implementation path, release action, or reviewer-routing artifact exists
  outside the exact contract above without a plan amendment first.

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

## Post-merge / release actions

- If later implementation for this topic is merged, only normal post-merge
  local sync may occur.
- No repository release action is required.
- No `VERSION` bump, tag creation, README update, or stable-library promotion
  is allowed in this topic.

## Open Questions / Unresolved Items

- None. Scope, analysis prerequisites, implementation targets, non-release
  intent, and workflow gates are locked for this topic.
