---
topic: platform-projection-adapter
status: planned
created: 2026-06-11
---

# Platform Projection Adapter Steps

## Workflow Stages

- [X] planned
- [ ] creator-in-progress
- [ ] review-ready
- [ ] reviewer-in-progress
- [ ] approved
- [ ] needs-rework
- [ ] publish-in-progress
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

- [ ] Create `skills/platform-projection-adapter/SKILL.md`
- [ ] Create `skills/platform-projection-adapter/examples.md`
- [ ] Create `skills/platform-projection-adapter/reference.md`
- [ ] Create `skills/platform-projection-adapter/scripts/platform_projection_adapter.py`
- [ ] Create `skills/platform-projection-adapter/tests/test_platform_projection_adapter.py`
- [ ] Make `--platform-root` required and fail fast when omitted
- [ ] Make dry-run / apply / force behavior match the frozen analysis artifacts
- [ ] Make every run summary report mode, target root, source count, action
  counts, and conflicts
- [ ] Make unreadable or undecodable source input fail fast
- [ ] Make failed or partial apply report failure truthfully and preserve
  accurate rerun behavior for the next dry-run
- [ ] Run `uv run --with pytest pytest skills/platform-projection-adapter/tests/ -v`
- [ ] Keep existing `skills/`, `.github/**`, `.codex/**`, `README.md`, and
  `VERSION` untouched

### review-ready

- [ ] Hand off the completed creator draft only after the fixed pytest command
  passes and the write set still matches the plan

### reviewer-in-progress

- [ ] Perform independent review against
  `plan/platform-projection-adapter/platform-projection-adapter.plan.md`,
  `plan/agent-handoff-workflow.md`, and `plan/topic-plan-contract.md`
- [ ] Record reviewer-controlled routing in
  `plan/platform-projection-adapter/platform-projection-adapter.review-log.md`
  if rework or re-review control is needed

### approved

- [ ] Accept the creator draft with the canonical JSON reviewer verdict before
  publish work begins

### needs-rework

- [ ] Route blocking reviewer findings back to `creator-in-progress` without
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
- After `merged`, STOP POINT 2 blocks any implicit continuation; Main Agent may
  enter Phase 9 post-merge local sync only after merge is confirmed and a human
  explicitly resumes execution.
- Next actor: Creator.
- Next gate: produce the five planned files under
  `skills/platform-projection-adapter/` and pass the fixed pytest command.
