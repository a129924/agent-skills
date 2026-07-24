# Scope Draft Plan Skill — PR #119 Correction Plan

## Classification

- **Severity:** `medium`
- **Routing state:** `PLANNER_REPLAN`
- **Trigger:** PR #119 P1 inventory drift. The newly added canonical skill is
  absent from the checked-in generated canonical inventory snapshot.
- **Parent truth:** `scope-draft-plan.plan.md`, `.step.md`, `.review-log.md`,
  and `.summary.md` remain current execution truth. This file is historical
  correction truth and does not replace them.

## Frozen correction direction

1. Add `artifacts/skills-inventory.jsonl` to the parent `Artifact Paths` as a
   generated canonical snapshot and correction write path.
2. Use the existing `scripts/build_skills_inventory.py` builder without
   changing the builder, its tests, inventory schema, or discovery contract.
3. Regenerate the snapshot after the final bounded skill-file fixes. The final
   JSONL must contain exactly 57 records and exactly one record whose
   `canonical_path` equals `skills/scope-draft-plan` (no trailing slash).
   Compared with the current 56-record snapshot, that record is the only
   permitted inventory-record addition; every pre-existing record must remain
   unchanged.
4. In the same bounded correction loop, make only these four independently
   reviewable PR-comment fixes:
   - `skills/scope-draft-plan/references/output-template.md` must describe
     only a BC Mission output. Cross-BC Mission and Feasibility Spike output
     modes are either removed from the template or explicitly `BLOCKED`; they
     must not be presented as valid Draft Plan modes.
   - `plan/scope-draft-plan/scope-draft-plan.step.md` must remove or correct
     wording that calls already-committed topic content `uncommitted by design`.
   - `plan/scope-draft-plan/scope-draft-plan.summary.md` must likewise remove
     or correct that stale `uncommitted by design` characterization.
   - `plan/scope-draft-plan/scope-draft-plan.review-log.md` must normalize the
     skill-review gate verdict to `approved`; `PASS` may remain only as
     explanatory reviewer prose, not as the controlling gate verdict.
   These are existing-scope implementation corrections, not new scope.

## Boundaries

- Stay on PR #119, branch `feat/andrew/scope-draft-plan`, and its existing
  feature worktree. Do not create a worktree, branch, PR, topic, or release
  route.
- Do not modify `README.md`, `VERSION`, `agents/**`, `.github/**`,
  `.codex/**`, projection surfaces, runtime behavior, the inventory builder,
  inventory tests, or any unrelated skill.
- The allowed correction writes are the exact paths declared in the parent
  plan's `Artifact Paths`; no new path is implied by this correction.
- This Planner correction does not itself edit the skill package, generated
  inventory, review log, or summary; those bounded writes belong to the
  separate Implementer named below.

## Required handoff and closure

- A separate Implementer performs the bounded fixes and inventory generation.
- A separate Reviewer verifies the final correction diff, all four bounded
  comment repairs, and inventory evidence before any patch commit/push.
- Parent artifacts must be synchronized before the correction can be marked
  resolved. The correction then remains retained historical truth.
