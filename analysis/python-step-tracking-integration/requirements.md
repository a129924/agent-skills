# Requirements: python-step-tracking-integration

**Status**: FROZEN — ready for technical translation
**Topic**: `python-step-tracking-integration`
**Produced by**: business-intent-alignment
**Date**: 2026-05-07

---

## Business Intent

SubAgents executing a Python implementation plan have no shared visible state.
When one agent completes work, the next agent cannot confirm what was done without
reading the full diff or asking. This creates invisible handoffs and premature reviews.

`plan-step-tracker` + `*.step.md` (v0.42.1) already solves this problem structurally,
but has never been wired into the Python workflow skills. This integration closes that gap.

---

## Actors

| Actor | Role |
|-------|------|
| `python-plan-authoring` | Produces plan artifacts; must also produce step.md |
| Executor | Developer or agent implementing the plan; must update step.md |
| `python-implementation-review` | Reviews implementation; must gate on step.md before proceeding |

---

## Frozen Requirements

### R1 — Co-artifact production

**When** `python-plan-authoring` produces a `*.plan.md`,
**it MUST also produce** `plan/<topic>/<topic>.step.md` in the same operation.

- Actor: `python-plan-authoring`
- Condition: any plan authoring invocation that produces a `*.plan.md`
- Observable: `plan/<topic>/<topic>.step.md` exists after authoring completes
- Acceptance: step.md parses cleanly by `plan-step-tracker` (or grep fallback)
- Failure: plan.md exists but step.md is absent → authoring is incomplete

### R2 — Step.md initial state

The produced `*.step.md` MUST contain:

1. YAML frontmatter: `topic`, `phase: plan-authoring`, `created: <date>`
2. `## Workflow Stages` section: all 6 fixed stages as `[ ]`, except `plan-authoring` which is `[X]` (completed by authoring)
3. `## Implementation Steps` section: mirrored from plan.md `## Implementation Steps`, all as `[ ]`
4. An executor instruction note: explicit text stating executor must mark `[ ]` → `[X]` upon completing each step

- Actor: `python-plan-authoring`
- Condition: producing step.md
- Observable: file contains all 4 elements above
- Acceptance: `grep '^\- \[ \]' <step.md>` returns Implementation Steps only (not plan-authoring stage)

### R3 — Executor update obligation

The step.md MUST communicate to the executor (via embedded note) that:
- Each Implementation Step must be marked `[X]` when completed
- All steps must be `[X]` before submitting for `python-implementation-review`
- The path to update is `plan/<topic>/<topic>.step.md`

- Actor: executor
- Condition: executor begins implementation
- Observable: executor marks steps without external instruction
- Acceptance: executor can act correctly with only the step.md file as reference

### R4 — Pre-review gate (step.md exists, has pending items)

When `python-implementation-review` is invoked and `plan/<topic>/<topic>.step.md` exists
and contains one or more `[ ]` items:

- **Verdict MUST be BLOCKED** (not `needs-rework`, not `approved`)
- Output MUST include: list of pending steps, actionable message pointing to `plan/<topic>/<topic>.step.md`
- Traceability matrix MUST NOT be built (gate fires before step 2)

- Actor: `python-implementation-review`
- Condition: step.md exists AND `grep '^\- \[ \]'` finds matches
- Observable: BLOCKED verdict with step list and instructions
- Acceptance: reviewer cannot produce `approved` or `needs-rework` when steps are pending

### R5 — Backward compatibility (step.md absent)

When `python-implementation-review` is invoked and `plan/<topic>/<topic>.step.md`
does NOT exist:

- **MUST emit a WARN** noting that step.md was not found
- **MUST NOT BLOCK** — proceed to traceability matrix normally
- The warn message SHOULD suggest the executor generate a step.md

- Actor: `python-implementation-review`
- Condition: step.md missing
- Observable: WARN in output, review proceeds
- Acceptance: all plans created before this integration continue to work unmodified

### R6 — No hard tool dependency

The step-completion check in `python-implementation-review` MUST function without
the `plan-step-tracker` CLI being installed.

- Actor: any repo using `python-implementation-review` (portability)
- Condition: `plan-step-tracker` CLI unavailable
- Observable: skill still checks step.md using grep fallback
- Acceptance: copying skill to a repo without plan-step-tracker does not break the gate

### R7 — Format conformance

The `*.step.md` produced by `python-plan-authoring` MUST conform to the format
defined in `plan-step-tracker/reference.md`.

- Actor: `python-plan-authoring`
- Condition: producing step.md
- Observable: `plan-step-tracker/scripts/step_tracker.py check_all_succeeded <topic>` succeeds without parse error
- Acceptance: grep patterns in `plan-step-tracker/reference.md` work on the produced file

---

## Non-goals

- **Not** modifying `plan-step-tracker` skill itself
- **Not** modifying `python-plan-review`, `python-tdd-test-authoring`, or `python-code-review`
- **Not** adding entity verification (step.md records declared state only, not external evidence)
- **Not** auto-updating step.md from any skill (step-tracker is read-only; executor updates manually)
- **Not** enforcing step.md in non-Python workflow skills
- **Not** migrating existing plan.md files to produce step.md retroactively

---

## Surfaced Contradictions

### C1: plan-step-tracker is read-only vs. executor must write to step.md

`plan-step-tracker/SKILL.md` Boundaries: "Read-only: This skill does not modify `.step.md` files."

**Resolution**: No contradiction. The skill is read-only. The executor (human or implementation agent)
edits the file directly — they are not using the skill. The skill reads; the actor writes. Resolved.

### C2: Who marks `plan-authoring` Workflow Stage as `[X]`?

If step.md initializes with all `[ ]`, the authoring stage itself was just completed.
Marking it `[ ]` would be immediately stale.

**Resolution**: `python-plan-authoring` marks `plan-authoring` stage as `[X]` in the initial
step.md it produces. All other Workflow Stages remain `[ ]`. Resolved.

### C3: BLOCKED vs. needs-rework for pending steps

`python-implementation-review` already has a `needs-rework` verdict for plan gaps.
Having a third verdict `BLOCKED` adds a state not in the current output schema.

**Resolution**: Use a distinct `step_gate` prefix in the verdict output rather than adding
a new YAML verdict value. The BLOCKED signal is surfaced as a pre-review refusal
(plain text), not a traceability-matrix verdict. Same pattern as the existing refusal output.
Resolved — no schema change needed.

---

## Explicit Assumptions

- A1: Executor (human or agent) can directly edit `plan/<topic>/<topic>.step.md` as a plain file
- A2: `plan-step-tracker/reference.md` format spec is stable and will not change during this integration
- A3: Topic name used in step.md matches the directory name in `plan/<topic>/`

---

## Extreme-Boundary Checks

| Boundary | Outcome |
|----------|---------|
| Plan has 0 Implementation Steps | step.md has empty `## Implementation Steps` section; check finds no `[ ]`; gate passes |
| step.md exists but is empty | grep finds no `[ ]`; gate passes (not a false block) |
| Executor uses lowercase `[x]` | plan-step-tracker warns; grep `^\- \[ \]` won't match; treated as done (acceptable, matches plan-step-tracker spec) |
| Plan created before integration (no step.md) | R5: WARN + proceed, no block |
| step.md format spec changes in future | Both skills reference `plan-step-tracker/reference.md`; format change requires coordinated update |
| plan-step-tracker CLI absent | R6: grep fallback used; no functional difference |

---

## Blockers Before Technical Translation

None. All contradictions resolved. Assumptions declared. Requirements are measurable and
observable. Ready for `business-to-technical-translation`.
