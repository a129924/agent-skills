---
topic: platform-projection-adapter
status: publish-in-progress
created: 2026-06-11
---

# Platform Projection Adapter Steps

## Workflow Stages

- [X] planned
- [X] creator-in-progress
- [X] review-ready
- [X] reviewer-in-progress
- [X] approved
- [ ] needs-rework
- [X] publish-in-progress
- [ ] pr-open
- [ ] merged

## Actionable Steps

### planned

- [X] Freeze `analysis/platform-projection-adapter/requirements.md`
- [X] Freeze `analysis/platform-projection-adapter/technical-spec.md`
- [X] Materialize `plan/platform-projection-adapter/platform-projection-adapter.plan.md`
- [X] Materialize `plan/platform-projection-adapter/platform-projection-adapter.step.md`
- [X] Lock v1 decisions: whole-library projection, explicit `--platform-root`,
  dry-run default, `--apply`, `--force`, CLI-only tests, and non-stable topic
  intent

### creator-in-progress

- [X] Create `skills/platform-projection-adapter/SKILL.md`
- [X] Create `skills/platform-projection-adapter/examples.md`
- [X] Create `skills/platform-projection-adapter/reference.md`
- [X] Create `skills/platform-projection-adapter/scripts/platform_projection_adapter.py`
- [X] Create `skills/platform-projection-adapter/tests/test_platform_projection_adapter.py`
- [X] Make `--platform-root` required and fail fast when omitted
- [X] Make dry-run / apply / force behavior match the frozen analysis artifacts
- [X] Make every run summary report mode, target root, source count, action
  counts, and conflicts
- [X] Make unreadable or undecodable source input fail fast
- [X] Make failed or partial apply report failure truthfully and preserve
  accurate rerun behavior for the next dry-run
- [X] Run `uv run --with pytest pytest skills/platform-projection-adapter/tests/ -v`
- [X] Keep existing `skills/`, `.github/**`, `.codex/**`, `README.md`, and
  `VERSION` untouched

### review-ready

- [X] Hand off the completed creator draft only after the fixed pytest command
  passes and the write set still matches the plan

### reviewer-in-progress

- [X] Perform independent review against
  `plan/platform-projection-adapter/platform-projection-adapter.plan.md`,
  `plan/agent-handoff-workflow.md`, and `plan/topic-plan-contract.md`
- [ ] Record reviewer-controlled routing in
  `plan/platform-projection-adapter/platform-projection-adapter.review-log.md`
  if rework or re-review control is needed

### approved

- [X] Accept the creator draft with the canonical JSON reviewer verdict before
  publish work begins

### needs-rework

- [X] Route blocking reviewer findings back to `creator-in-progress` without
  widening topic scope or reopening frozen analysis artifacts

### publish-in-progress

- [ ] Publish only the exact planned repo-visible artifacts; no stable-library
  updates
- [ ] Respect STOP POINT 1 before commit / push / PR creation
- [ ] Keep reviewer work separate from commit, push, PR, and merge routing

### pr-open

- [ ] Triage PR feedback through the normal `needs-rework` or `merged` routes

### merged

- [ ] Treat merge confirmation as STOP POINT 2; only a later human explicit
  resume may allow Main Agent Phase 9 post-merge local sync

## Handoff / Gate Notes

- `step.md` is required for this topic because the execution path will use
  creator, reviewer, and Main Agent handoffs.
- Frozen analysis inputs:
  - `requirements.md`
    `e34ac61996355243e62ba10beaaece8bf222459016326b86657cbf40b26d6e65`
  - `technical-spec.md`
    `7d1b257d30ac380b6fa6fdb34b6a3797634559663e1d261a4fa9f52704b27d59`
- Runtime projection outputs under caller-provided `<platform-root>` are not
  repo-visible staged files for this topic.
- This is a non-stable topic: no `README.md`, no `VERSION`, and no release
  action.
- Reviewer work ends at `approved` or `needs-rework`; publish work begins only
  after `approved`.
- Planner final gate confirmed reviewer findings are blocking and routed this
  topic to bounded `needs-rework`.
- Bounded rework scope is limited to:
  - `skills/platform-projection-adapter/scripts/platform_projection_adapter.py`
  - `skills/platform-projection-adapter/tests/test_platform_projection_adapter.py`
  - `plan/platform-projection-adapter/platform-projection-adapter.step.md`
- Frozen analysis stays unchanged; no write-set expansion is allowed.
- Bounded rework findings resolved in creator:
  - added a source/target overlap guard for canonical `skills/` safety
  - added a fail-fast overlap rejection test
  - added unreadable-source fail-fast coverage beyond undecodable UTF-8
- After `merged`, STOP POINT 2 blocks any implicit continuation; Main Agent may
  enter Phase 9 post-merge local sync only after merge is confirmed and a human
  explicitly resumes execution.
- Human authorized bounded creator rework under the existing plan.
- Fixed pytest command passed for this bounded rework.
- Planner final gate confirmed the bounded rework resolved the prior blocking
  findings and may advance to `approved`.
- Human authorized the separate publish flow after `approved`.
- Next actor: Main Agent.
- Current gate: `publish-in-progress`.
- Next gate: commit the bounded topic, push the branch, and open a ready PR
  against `dev`.
