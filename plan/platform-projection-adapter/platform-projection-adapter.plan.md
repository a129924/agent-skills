# Platform Projection Adapter Plan

## Analysis Inputs

This topic plan operates in strict mode because both analysis artifacts exist
and are frozen:

- `analysis/platform-projection-adapter/requirements.md`
  - SHA-256: `e34ac61996355243e62ba10beaaece8bf222459016326b86657cbf40b26d6e65`
- `analysis/platform-projection-adapter/technical-spec.md`
  - SHA-256: `7d1b257d30ac380b6fa6fdb34b6a3797634559663e1d261a4fa9f52704b27d59`

The implementation plan must map 100% to those frozen analysis artifacts.
Chat-time convenience does not override them without an explicit human
`override`.

## Goal / Outcome

- **Goal**: deliver one bounded `CLI + 薄 Agent Skill` topic that projects the
  canonical `skills/` library to a caller-specified platform root via explicit
  `--platform-root`, with dry-run as the default and `--apply` / `--force`
  gating for writes.
- **Outcome**: future implementation creates exactly one new canonical skill at
  `skills/platform-projection-adapter/` containing the thin skill wrapper, the
  CLI, and CLI-only tests, while leaving existing canonical `skills/` content
  untouched.
- **Non-goal**: this topic does not publish stable-library metadata, does not
  update `README.md` or `VERSION`, does not edit `.github/**` or `.codex/**`,
  and does not materialize repo-visible projection outputs under any concrete
  platform root.

## Scope

- **In scope**:
  - create `skills/platform-projection-adapter/SKILL.md`
  - create `skills/platform-projection-adapter/examples.md`
  - create `skills/platform-projection-adapter/reference.md`
  - create `skills/platform-projection-adapter/scripts/platform_projection_adapter.py`
  - create `skills/platform-projection-adapter/tests/test_platform_projection_adapter.py`
  - update `plan/platform-projection-adapter/platform-projection-adapter.step.md`
  - implement whole-library projection from canonical `skills/` to runtime
    `<platform-root>/skills/`
  - implement dry-run default, `--apply`, `--force`, conflict reporting, and
    placeholder rewrite rules
  - validate the CLI with the fixed pytest command

- **Out of scope**:
  - modifying any pre-existing file under `skills/`
  - modifying `.github/**`
  - modifying `.codex/**`
  - modifying `README.md`
  - modifying `VERSION`
  - adding stable-library metadata, release notes, or tag actions
  - partial-scope projection of one skill subset
  - target-root pruning or delete-sync behavior
  - repo-visible `.codex/...` or other platform projection outputs committed by
    this topic

## Locked Decisions

1. **Canonical source is fixed and read-only**
   - `skills/` remains the canonical source.
   - Implementation may read from `skills/` but must not modify any existing
     canonical artifact.

2. **v1 scope is fixed**
   - v1 projects the entire `skills/` library.
   - v1 requires explicit `--platform-root`.

3. **CLI is the only transformation core**
   - All transformation logic lives in
     `skills/platform-projection-adapter/scripts/platform_projection_adapter.py`.
   - `SKILL.md` only collects parameters, defaults to dry-run, enforces
     `--apply` / `--force` gating, and reports the CLI summary.

4. **Apply safety contract is fixed**
   - No writes occur without `--apply`.
   - Existing differing target files block apply unless `--force` is present.
   - `--force` does not authorize extra source scope or target pruning.

5. **Test surface is fixed**
   - Automated tests cover the CLI only.
   - The required command is exactly:
     `uv run --with pytest pytest skills/platform-projection-adapter/tests/ -v`

6. **Stable-library and release intent are absent**
   - This is not a stable-library publish topic.
   - `README.md` and `VERSION` remain unchanged.
   - No release or tagging action exists in this topic.

## Boundaries / Exclusions

- **ReadOnly**:
  - every pre-existing file under `skills/`
  - `analysis/platform-projection-adapter/requirements.md`
  - `analysis/platform-projection-adapter/technical-spec.md`
  - `plan/platform-projection-adapter/platform-projection-adapter.plan.md`
  - `.github/**`
  - `.codex/**`
  - `README.md`
  - `VERSION`
- **Create**:
  - `skills/platform-projection-adapter/SKILL.md`
  - `skills/platform-projection-adapter/examples.md`
  - `skills/platform-projection-adapter/reference.md`
  - `skills/platform-projection-adapter/scripts/platform_projection_adapter.py`
  - `skills/platform-projection-adapter/tests/test_platform_projection_adapter.py`
- **Modify**:
  - `plan/platform-projection-adapter/platform-projection-adapter.step.md`
- Do not widen the topic from runtime-target projection behavior into platform
  directory maintenance, compatibility-surface repair, or canonical-content
  rewrite.
- Do not let creator, reviewer, or Main Agent ownership collapse into one role.
- If later work requires any path outside the exact create/modify set above,
  stop and repair the plan before implementation continues.

## Status / Allowed Transitions

- **Current**: `planned`
- **Execution model**: follow the canonical creator -> reviewer -> publish ->
  merge path, with no stable-library or release phase
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

- Use the standard Phase 4.5 planner contract alignment checkpoint from
  `plan/agent-handoff-workflow.md`.
- Missing or drifting CLI behavior against the frozen analysis artifacts routes
  back to creator rework; it does not reopen requirements or technical spec in
  this topic.
- `plan/platform-projection-adapter/platform-projection-adapter.step.md` is
  required because this topic uses two or more workflow-role handoffs
  (creator, reviewer, Main Agent).

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/platform-projection-adapter/platform-projection-adapter.plan.md` | Planning actor | Repo-visible execution contract for this topic |
| Topic progression artifact | `plan/platform-projection-adapter/platform-projection-adapter.step.md` | Planning actor / Main Agent | Current-truth workflow progression status for this topic |
| Review routing log | `plan/platform-projection-adapter/platform-projection-adapter.review-log.md` | Reviewer / Planning actor | Repo-visible routing log if reviewer findings control rework or re-review |
| Requirements baseline | `analysis/platform-projection-adapter/requirements.md` | Planning actor | Frozen business baseline for scope and safety rules |
| Technical baseline | `analysis/platform-projection-adapter/technical-spec.md` | Planning actor | Frozen technical translation and exact implementation write set |
| Skill contract | `skills/platform-projection-adapter/SKILL.md` | Creator | Thin Agent Skill wrapper that invokes the CLI and reports the summary |
| Skill examples | `skills/platform-projection-adapter/examples.md` | Creator | Positive and negative wrapper-usage examples |
| Skill reference | `skills/platform-projection-adapter/reference.md` | Creator | Stable CLI contract, placeholder rewrite rule, and apply/force behavior notes |
| Projection CLI | `skills/platform-projection-adapter/scripts/platform_projection_adapter.py` | Creator | Sole transformation core for whole-library projection |
| CLI tests | `skills/platform-projection-adapter/tests/test_platform_projection_adapter.py` | Creator | pytest coverage for the fixed CLI contract |

Artifact path notes:

- This topic does **not** modify `README.md`, `VERSION`, `.github/**`, or
  `.codex/**`.
- Runtime projection outputs under a caller-specified `<platform-root>` are not
  repo-visible implementation artifacts and therefore are not staged repo
  paths.
- If future work attempts to stage a repo-visible `.codex/...` projection
  output or any other extra file, treat it as plan drift and stop.

## Implementation Steps

1. Re-read the frozen analysis artifacts and this topic plan before creating
   implementation files.
2. Create `skills/platform-projection-adapter/scripts/platform_projection_adapter.py`
   with the fixed CLI contract:
   - required `--platform-root`, with immediate CLI validation failure when the
     flag is omitted
   - dry-run default
   - `--apply` write gate
   - `--force` overwrite gate
   - whole-library discovery from canonical `skills/`
   - placeholder rewrite from `.<platform>/...` to `<platform-root>/...`
   - fail-fast behavior when any source input is unreadable or undecodable,
     instead of skipping or degrading that file silently
   - per-run summary fields that always report mode, target root, source count,
     action counts, and conflicts
   - failure reporting that never claims apply succeeded when the write phase is
     blocked, interrupted, or otherwise unsuccessful
   - rerun behavior where a subsequent dry-run recomputes from the actual
     current target state after any prior failed or partial apply
3. Create `skills/platform-projection-adapter/tests/test_platform_projection_adapter.py`
   so the fixed pytest command validates dry-run, apply, force, conflict,
   whole-library traversal, placeholder rewrite, unreadable/undecodable source
   failure, required `--platform-root` validation, apply-failure truthfulness,
   and rerun/noop behavior from actual target state.
4. Create `skills/platform-projection-adapter/SKILL.md`,
   `skills/platform-projection-adapter/examples.md`, and
   `skills/platform-projection-adapter/reference.md` as a thin wrapper surface
   around the CLI, without duplicating transformation logic.
5. Update `plan/platform-projection-adapter/platform-projection-adapter.step.md`
   with workflow facts only; do not use it to widen scope or alter locked
   decisions.

## Validation / Acceptance Checks

- the implementation creates only the five planned files under
  `skills/platform-projection-adapter/` and updates only the topic-local
  `step.md`
- the CLI is the sole transformation core; the skill wrapper contains no second
  projection algorithm
- the CLI reads from canonical `skills/` and does not modify any pre-existing
  source artifact
- omission of `--platform-root` fails validation immediately and does not
  proceed with discovery or writes
- dry-run performs zero writes and every run summary reports mode, target root,
  source count, action counts, and conflicts
- `--apply` writes only when safe; conflicting target files block apply unless
  `--force` is present
- apply failure caused by conflicts, interruption, permissions, unreadable
  input, or undecodable input does not report success
- whole-library traversal preserves relative paths under
  `<platform-root>/skills/`
- placeholder strings beginning with `.<platform>/` are rewritten correctly in
  target content while canonical `skills/` wording stays unchanged
- unreadable or undecodable source input fails fast as a blocking error; the
  CLI does not silently skip, truncate, or corrupt that file
- after any failed or partial apply, the next dry-run reflects the actual
  current target state and recomputes the remaining create / update / noop /
  conflict actions truthfully
- the required command
  `uv run --with pytest pytest skills/platform-projection-adapter/tests/ -v`
  passes
- no repo-visible `.codex/...`, `.github/...`, `README.md`, or `VERSION`
  changes appear in the staged set

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

- STOP POINT 2 applies after merge handoff: once merge is confirmed, the current
  execution stops and must not continue into local sync by polling, inference,
  or implicit continuation.
- Only after merge is confirmed and a human explicitly resumes execution may the
  Main Agent enter Phase 9 to run post-merge local sync.
- No repository release action is required.
- No `README.md` update, `VERSION` bump, or tag creation is allowed in this
  topic.

## Open Questions / Unresolved Items

- None. The topic slug, frozen analysis inputs, exact create/modify surface,
  non-stable intent, CLI test command, and v1 scope are all locked.
