# Technical Spec: python-step-tracking-integration

**Status**: FROZEN — ready for plan creation
**Topic**: `python-step-tracking-integration`
**Produced by**: business-to-technical-translation
**Input baseline**: `analysis/python-step-tracking-integration/requirements.md`
**Date**: 2026-05-07

---

## Architecture Compliance Self-Check

| Rule | Status | Notes |
|------|--------|-------|
| Each skill is self-contained | ✅ PASS | Both skills reference `plan-step-tracker/reference.md` for grep patterns; no runtime import |
| plan-step-tracker is read-only | ✅ PASS | Neither skill modifies plan-step-tracker |
| Portable (no hard CLI dependency) | ✅ PASS | grep-first, plan-step-tracker CLI as optional enhancement |
| No new skills required | ✅ PASS | Only 2 existing SKILL.md files need edits |
| No verdict schema change | ✅ PASS | BLOCKED fires as pre-review refusal (plain text), not a new YAML verdict value |
| Format conformance to plan-step-tracker/reference.md | ✅ PASS | step.md template uses `^\- \[.\]` regex-compatible lines |

No architecture conflicts detected. No waivers needed.

---

## Requirement-to-Technical Mapping

### R1 → T1-A: Add step.md production to `python-plan-authoring`

**What changes:**
- `outputs` frontmatter: add `*.step.md` as a required co-artifact alongside `*.plan.md`
- Process authoring step 4 (verify plan): add sub-step instructing skill to also produce `plan/<topic>/<topic>.step.md`
- Process authoring steps section: add the step.md template inline (see Template Spec below)

**File changed:** `.github/skills/python-plan-authoring/SKILL.md`

**Dependency:** plan-step-tracker format spec (reference.md) — read-only reference, stable

---

### R2 + R3 → T1-B: Step.md initial state template

The following template is the canonical output of `python-plan-authoring` for step.md.
It MUST be reproduced exactly in the SKILL.md Process section.

```markdown
---
topic: <topic>
phase: plan-authoring
created: YYYY-MM-DD
---

# <topic> — Step Tracking

> **Executor**: Mark each step `[X]` when complete.
> All Implementation Steps must be `[X]` before submitting for `python-implementation-review`.
> Update this file at: `plan/<topic>/<topic>.step.md`

## Workflow Stages

- [X] plan-authoring
- [ ] plan-review
- [ ] tdd-test-authoring
- [ ] implementation
- [ ] implementation-review
- [ ] code-review

## Implementation Steps

- [ ] 1. <mirrored from plan.md step 1>
- [ ] 2. <mirrored from plan.md step 2>
...
```

**Format rules (from plan-step-tracker/reference.md):**
- Checkbox marker: `- [X]` (uppercase X = done), `- [ ]` (space = pending)
- Each step line must match `^\- \[(.)\](.*)` — leading `- ` prefix required
- `plan-authoring` stage is initialized `[X]` (authoring just completed)
- All 6 Workflow Stages are always present; no stages are omitted

**Executor note (R3):** embedded in the template as a blockquote at file top — actionable,
includes the exact file path to edit.

---

### R4 + R5 + R6 → T2-A: Add step gate to `python-implementation-review`

**What changes:**
- `inputs` frontmatter: add `*.step.md` as an optional input
- Process: insert step **1.5** between existing step 1 (Confirm inputs) and step 2 (Build traceability matrix)
- Failure Handling: add BLOCKED-step-gate refusal format description

**File changed:** `.github/skills/python-implementation-review/SKILL.md`

---

### T2-B: Step gate process step 1.5 (exact language)

Insert as new Process step 1.5 in python-implementation-review SKILL.md:

```
1.5 Check step completion (step gate).
    Resolve the topic name from the plan file name (e.g. `plan/my-feature/my-feature.plan.md` → topic `my-feature`).
    a. If `plan/<topic>/<topic>.step.md` does NOT exist:
       - Emit the following warning and continue to step 2:
         ⚠️  WARNING: plan/<topic>/<topic>.step.md not found.
                      Proceeding without step gate check.
                      Suggestion: re-run python-plan-authoring to produce a step.md.
    b. If step.md exists:
       - Primary (plan-step-tracker CLI available):
           python .github/skills/plan-step-tracker/scripts/step_tracker.py check_all_succeeded <topic>
           Exit 0 → all steps done → continue to step 2.
           Exit 1 → pending steps found → go to step 1.5c.
       - Fallback (CLI unavailable — use this by default for portability):
           PENDING=$(sed -n '/^## Implementation Steps$/,/^## /p' plan/<topic>/<topic>.step.md | grep -c '^\- \[[ x]\]')
           0 matches in `## Implementation Steps` → all steps done → continue to step 2.
           1+ matches in `## Implementation Steps` → pending steps found → go to step 1.5c.
           `## Workflow Stages` is out of scope for this gate; lowercase `[x]` remains pending.
    c. If pending steps found:
       - Emit the BLOCKED refusal output (see below) and stop.
       - Do NOT produce a YAML verdict block.
       - Do NOT proceed to the traceability matrix.
```

---

### T2-C: BLOCKED refusal output format

Add to the Outputs section (alongside existing Refusal output description):

```
BLOCKED — Step gate failed.

The following Implementation Steps are still pending in plan/<topic>/<topic>.step.md:

  - [ ] N. <pending step text>
  - [ ] M. <pending step text>

Action required:
  Complete all pending steps and mark them [X] in plan/<topic>/<topic>.step.md
  before re-submitting for python-implementation-review.
```

This is plain-text output only. The YAML verdict block is NOT produced for BLOCKED step-gate results.

---

## Cost of Realization

| Workstream | Complexity | Notes |
|------------|------------|-------|
| T1: python-plan-authoring edits | Low | ~50 lines added: step.md template block + 1 process sub-step + outputs update |
| T2: python-implementation-review edits | Low-Medium | ~40 lines added: step 1.5 + BLOCKED format + inputs update |
| Testing surface | None | SKILL.md text-only changes; no runtime code |
| Rollback cost | Trivial | Revert 2 SKILL.md files → v0.48.0 behavior restored |
| Backward compatibility | Free | R5 (WARN + proceed) already accounted for in T2-A |

Total: 2 files, text-only, no new scripts, no new skills, no dependency additions.

---

## Sequencing and Dependencies

```
T1 (python-plan-authoring)  ──┐
                              ├─→ can be done in either order or in parallel
T2 (python-implementation-review) ──┘
```

No ordering constraint between T1 and T2.
Both reference `plan-step-tracker/reference.md` (format spec) which is frozen at v0.42.1.

---

## Feasibility Assessment

**FEASIBLE.** All requirements translate to SKILL.md text edits. No runtime code, no new
dependencies, no architecture exceptions. Format spec (`plan-step-tracker/reference.md`) is
stable. Grep fallback is universally available. Backward compatibility is built into T2 via
the WARN-and-proceed path.

**Risk surface:**
- If `plan-step-tracker/reference.md` format spec changes, both skills need re-sync. Low probability.
- If executor forgets to update step.md, T2 produces BLOCKED on a complete implementation.
  Mitigation: R3 executor note is embedded in step.md itself; BLOCKED message is actionable.

---

## Rollback Triggers

No rollback-to-alignment triggers needed. All requirements mapped cleanly. No business
assumption failed during translation.

Revert path: `git revert` or manual edit of 2 SKILL.md files restores v0.48.0 behavior.

---

## Artifacts for plan-creator

| Artifact | Path | Produced by |
|----------|------|-------------|
| requirements.md | `analysis/python-step-tracking-integration/requirements.md` | business-intent-alignment |
| technical-spec.md | `analysis/python-step-tracking-integration/technical-spec.md` | business-to-technical-translation |
| plan.md | `plan/python-step-tracking-integration/python-step-tracking-integration.plan.md` | plan-creator (next step) |

**Files to be modified by creator:**
- `.github/skills/python-plan-authoring/SKILL.md`
- `.github/skills/python-implementation-review/SKILL.md`

**Files NOT to be modified:**
- `.github/skills/plan-step-tracker/` (read-only)
- Any other skill
