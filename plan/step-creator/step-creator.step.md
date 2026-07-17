---
topic: step-creator
step_profile: agent-skill-plan
source_plan: plan/step-creator/step-creator.plan.md
created: 2026-07-16
---

# step-creator — Step Tracking

## Workflow Stages

| Current status | Allowed next transitions | Next actor |
| --- | --- | --- |
| `BLOCKED` | None — the selected source plan does not uniquely declare the current status, allowed transition and next actor required for this generated tracker. | None — do not synthesize an actor from GitHub PR, review, branch, chat or completion context. |

## Actionable Steps

### Main Agent — Fixed Head

- [ ] **Actor:** Main Agent — **Action:** create-worktree — **Selector:** topic=step-creator; branch=feat/andrew/step-creator; managed-path-intent=/Users/andrew/code/python/agent-skills.worktrees/agent-20260715-step-creator; primary-worktree=false
- [ ] **Actor:** Main Agent — **Action:** prepare-topic-branch — **Selector:** topic=step-creator; branch=feat/andrew/step-creator; managed-path-intent=/Users/andrew/code/python/agent-skills.worktrees/agent-20260715-step-creator; primary-worktree=false

### Contextual Actions

- [ ] **Actor:** Creator — **Action:** Author the exact `skills/step-creator/` Written set from the approved plan and hand off at `review-ready` without self-approval.

## Implementation Steps

- [ ] 1. Create `skills/step-creator/SKILL.md` with explicit caller profiles, per-profile eligibility/fidelity preflight, same-directory temporary-file atomic create-only behavior and cleanup, evidence phases, marker/tracker rules including eligible-only template-defined Python `[X] plan-authoring`, shared-shell routing and blockers.
- [X] 2. Create `skills/step-creator/templates/shared-lifecycle-shell.md` with selector/path intent, pending initial worktree lifecycle, evidence updates, 26-slot tail, remote-retention safety default, three sentinels/tag-only, release ranges and tracker scope.
- [X] 3. Create `skills/step-creator/references/base-plan-profile.md` with Base eligibility, wire, extraction fidelity, contextual dedup and mapping.
- [X] 4. Create `skills/step-creator/references/agent-skill-plan-profile.md` with single-skill eligibility, canonical paths/ownership/handoff and wire/context mapping.
- [ ] 5. Create `skills/step-creator/references/python-plan-authoring-adapter.md` with caller-selected routing, Python-intent plus canonical-contract eligibility without source profile marker, exact scaffold/six stages including canonical-template-defined fixed `[X] plan-authoring` only after eligibility, Contextual Actions, tracker distinction and shell insertion.
- [X] 6. Create `skills/step-creator/reference.md` with exactly three coherent shared topics: generation/eligibility, evidence/tracker, and lifecycle rendering; keep detailed rules in the owning SKILL, template, profile references and examples.
- [ ] 7. Create `skills/step-creator/examples.md` with valid profiles including an eligible Python source without literal profile marker and its fixed template-defined `[X] plan-authoring`; blockers for non-Python/incomplete/ambiguous Python source, invalid caller profile, existing output, extraction mismatch, lowercase x, unmappable progress, unknown release, claimed-X conflict, cleanup ambiguity; valid pending generation, remote-retention unknown safety default, release substitutions and Python tracker split.
- [ ] 8. Create `skills/step-creator/checklist.md` covering paths, eligibility, atomic create-only and temporary-file cleanup, wires, Python source-intent/canonical-contract test plus eligible-only fixed `[X] plan-authoring` wire, contextual mapping, worktree phases, remote-retention safety default, tail, release substitution, trackers, projections and handoff.
- [X] 9. Existing local `scripts/build_skills_inventory.py` recomputation is byte-identical to `artifacts/skills-inventory.jsonl`: 56 sorted canonical `skills/` records, exactly one `skills/step-creator/` record, no `agents/` or projection records, and current `skills/step-creator/` tree hash `e83363bcd299b9c55df81cf4b673a6f3470c826adb8adda97776387314d3dca4`; the builder and tests are unchanged.

## Main Agent Actionable Steps — Fixed Tail

- [ ] **Actor:** Main Agent — **Action:** Validate the approved Written set and perform bounded staging only.
- [ ] **Actor:** Main Agent — **Action:** Obtain explicit human approval at STOP POINT 1 before commit, push, or PR creation.
- [ ] **Actor:** Main Agent — **Action:** Commit the approved bounded changes.
- [ ] **Actor:** Main Agent — **Action:** Push the topic branch.
- [ ] **Actor:** Main Agent — **Action:** Open the pull request.
- [ ] **Actor:** Main Agent — **Action:** Review and observe the pull request and route actionable feedback.
- [ ] **Actor:** Main Agent — **Action:** Hand off for human merge at STOP POINT 2 and completely stop.
- [ ] **Actor:** Main Agent — **Action:** Record exact human merge evidence after a new execution begins.
- [ ] **Actor:** Main Agent — **Action:** Require a new explicit human resume before post-merge work.
- [ ] **Actor:** Main Agent — **Action:** Verify the pull request is merged.
- [ ] **Actor:** Main Agent — **Action:** Fast-forward-only sync the target/default branch.
- [ ] remote-retained — preserve the remote branch; retention is required or unknown, and human/policy follow-up is required before deletion
- [X] Determine release requirement — release not required
- [X] release-not-applicable — source plan declares terminal at merged
- [ ] **Actor:** Main Agent — **Action:** Inspect the selected managed topic worktree and prove clean/release evidence — **Selector:** topic=step-creator; branch=feat/andrew/step-creator; managed-path-intent=/Users/andrew/code/python/agent-skills.worktrees/agent-20260715-step-creator; primary-worktree=false
- [ ] **Actor:** Main Agent — **Action:** Obtain exact destructive approval to remove the selected managed topic worktree — **Selector:** topic=step-creator; branch=feat/andrew/step-creator; managed-path-intent=/Users/andrew/code/python/agent-skills.worktrees/agent-20260715-step-creator; primary-worktree=false
- [ ] **Actor:** Main Agent — **Action:** Remove the selected managed topic worktree and verify removal — **Selector:** topic=step-creator; branch=feat/andrew/step-creator; managed-path-intent=/Users/andrew/code/python/agent-skills.worktrees/agent-20260715-step-creator; primary-worktree=false
- [ ] **Actor:** Main Agent — **Action:** Delete the local topic branch after verified managed worktree removal.
- [ ] **Actor:** Main Agent — **Action:** Perform final verification and record close-semantics evidence without equating merged with closed.

## Handoff / Gate Notes

- Selected profile: agent-skill-plan
- Source plan: plan/step-creator/step-creator.plan.md
- Shared lifecycle shell: skills/step-creator/templates/shared-lifecycle-shell.md
- Managed worktree intent: topic=step-creator; branch=feat/andrew/step-creator; managed-path-intent=/Users/andrew/code/python/agent-skills.worktrees/agent-20260715-step-creator; primary-worktree=false
- Workflow-state source: `plan/step-creator/step-creator.plan.md` only. It does not uniquely declare the current status, allowed transition and next actor required for this tracker; generated progression is therefore BLOCKED.
- Progression truth inputs: `plan/step-creator/step-creator.plan.md` only for status, transition and next actor; `plan/step-creator/step-creator.step.md` is never a source-state substitute.
- Completion evidence inputs: commit `aa74b5b69f0b5c4cdb8b37cd8b61f897240edcd4` proves the prior versions of artifacts mapped to Implementation Steps 1–8; commit `8a5406b5f0ca7c6744206fd5fc365be8be31f3bf` proves the then-builder-generated inventory. Current local read-only builder evidence for Step 9 recomputes a byte-identical inventory with 56 sorted canonical `skills/` records, exactly one `skills/step-creator/` record, no `agents/` or projection records, and current tree hash `e83363bcd299b9c55df81cf4b673a6f3470c826adb8adda97776387314d3dca4`; builder and tests are unchanged, so Step 9 is `[X]` without waiting for a post-amendment commit. Steps 1, 5, 7 and 8 remain pending for the amended eligible-only template-defined Python `[X] plan-authoring` contract. This evidence, GitHub PR/review/branch metadata and chat context do not synthesize workflow status, transition or next actor.
- Marker semantics: `[X]` exact one-to-one evidence; `[ ]` pending/planned/unproved; lowercase source `[x]` is pending and warns.
- Tracker semantics: `check_all_succeeded` covers rendered head/contextual/Implementation/tail checkboxes; `check_impl_steps_succeeded` covers only Implementation Steps.
- Owner-only updates: only the action owner may update after exact evidence; step-creator never updates an existing output.
