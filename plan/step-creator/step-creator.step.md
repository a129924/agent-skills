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
| planned | creator-in-progress | Creator |

## Actionable Steps

### Main Agent — Fixed Head

- [ ] **Actor:** Main Agent — **Action:** create-worktree — **Selector:** topic=step-creator; branch=feat/andrew/step-creator; managed-path-intent=/Users/andrew/code/python/agent-skills.worktrees/agent-20260715-step-creator
- [ ] **Actor:** Main Agent — **Action:** prepare-topic-branch — **Selector:** topic=step-creator; branch=feat/andrew/step-creator; managed-path-intent=/Users/andrew/code/python/agent-skills.worktrees/agent-20260715-step-creator

### Contextual Actions

- [ ] **Actor:** Creator — **Action:** Author the exact `skills/step-creator/` Written set from the approved plan and hand off at `review-ready` without self-approval.

## Implementation Steps

- [ ] 1. Create `skills/step-creator/SKILL.md` with explicit caller profiles, per-profile eligibility/fidelity preflight, create-only behavior, evidence phases, marker/tracker rules, shared-shell routing and blockers.
- [ ] 2. Create `skills/step-creator/templates/shared-lifecycle-shell.md` with selector/path intent, pending initial worktree lifecycle, evidence updates, 26-slot tail, three sentinels/tag-only, release ranges and tracker scope.
- [ ] 3. Create `skills/step-creator/references/base-plan-profile.md` with Base eligibility, wire, extraction fidelity, contextual dedup and mapping.
- [ ] 4. Create `skills/step-creator/references/agent-skill-plan-profile.md` with single-skill eligibility, canonical paths/ownership/handoff and wire/context mapping.
- [ ] 5. Create `skills/step-creator/references/python-plan-authoring-adapter.md` with caller-selected routing, Python-intent plus canonical-contract eligibility without source profile marker, exact scaffold/six stages, Contextual Actions, tracker distinction and shell insertion.
- [ ] 6. Create `skills/step-creator/reference.md` consolidating profile validation, extraction, evidence phases, markers, trackers, release branches, managed identity, owner updates and blockers.
- [ ] 7. Create `skills/step-creator/examples.md` with valid profiles including Python source without literal profile marker; blockers for non-Python/incomplete/ambiguous Python source, invalid caller profile, existing output, extraction mismatch, lowercase x, unmappable progress, unknown release, claimed-X conflict, cleanup ambiguity; valid pending generation, release substitutions and Python tracker split.
- [ ] 8. Create `skills/step-creator/checklist.md` covering paths, eligibility, create-only, wires, Python source-intent/canonical-contract test, contextual mapping, worktree phases, tail, release substitution, trackers, projections and handoff.

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
- [ ] **Actor:** Main Agent — **Action:** Resolve remote topic branch deletion or retention.
- [ ] **Actor:** Main Agent — **Action:** Resolve whether release work is required from the source plan.
- [X] release-not-applicable — source plan declares terminal at merged
- [ ] **Actor:** Main Agent — **Action:** Inspect the selected managed topic worktree and prove clean/release evidence — **Selector:** topic=step-creator; branch=feat/andrew/step-creator; managed-path-intent=/Users/andrew/code/python/agent-skills.worktrees/agent-20260715-step-creator
- [ ] **Actor:** Main Agent — **Action:** Obtain exact destructive approval to remove the selected managed topic worktree — **Selector:** topic=step-creator; branch=feat/andrew/step-creator; managed-path-intent=/Users/andrew/code/python/agent-skills.worktrees/agent-20260715-step-creator
- [ ] **Actor:** Main Agent — **Action:** Remove the selected managed topic worktree and verify removal — **Selector:** topic=step-creator; branch=feat/andrew/step-creator; managed-path-intent=/Users/andrew/code/python/agent-skills.worktrees/agent-20260715-step-creator
- [ ] **Actor:** Main Agent — **Action:** Delete the local topic branch after verified managed worktree removal.
- [ ] **Actor:** Main Agent — **Action:** Perform final verification and record close-semantics evidence without equating merged with closed.

## Handoff / Gate Notes

- Selected profile: agent-skill-plan
- Source plan: plan/step-creator/step-creator.plan.md
- Shared lifecycle shell: skills/step-creator/templates/shared-lifecycle-shell.md
- Managed worktree intent: topic=step-creator; branch=feat/andrew/step-creator; managed-path-intent=/Users/andrew/code/python/agent-skills.worktrees/agent-20260715-step-creator; primary-worktree=false
- Progression truth inputs: plan/step-creator/step-creator.plan.md; plan/step-creator/step-creator.step.md
- Completion evidence inputs: none claimed at bootstrap; lifecycle and creator actions remain pending unless an exact plan decision sentinel applies.
- Marker semantics: `[X]` exact one-to-one evidence; `[ ]` pending/planned/unproved; lowercase source `[x]` is pending and warns.
- Tracker semantics: `check_all_succeeded` covers rendered head/contextual/Implementation/tail checkboxes; `check_impl_steps_succeeded` covers only Implementation Steps.
- Owner-only updates: only the action owner may update after exact evidence; step-creator never updates an existing output.
