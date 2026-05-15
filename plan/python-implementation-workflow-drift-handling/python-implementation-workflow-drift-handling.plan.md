## Analysis Layer Routing

- **Mode**: strict
- **Human override**: none
- **Requirements baseline**:
  - path: `analysis/python-implementation-workflow-drift-handling/requirements.md`
  - sha256: `cb04255f33bc74d4c296a57ef41ec5da68258c8e5231309caf380a75fadc70b3`
- **Technical baseline**:
  - path: `analysis/python-implementation-workflow-drift-handling/technical-spec.md`
  - sha256: `d8c98639fb79739b81e87dc3f73707bc003dc08e1a8a7e0b2438aa2c31881554`
- **Repository baseline commit when this plan was authored**:
  - `b0e067ea8c07f05bb5d41b5b12d35dcd2983315f`
- **Routing rule**:
  - This topic plan maps to the technical spec as the execution-facing source of truth.
  - `requirements.md` remains the business-intent guardrail.
  - If later chat instructions conflict with these analysis artifacts and no explicit human `override` is provided, stop and repair the analysis/plan contract instead of silently merging intent.

## Inputs / Prerequisites

- The repo-visible analysis layer already exists for this topic:
  - `analysis/python-implementation-workflow-drift-handling/requirements.md`
  - `analysis/python-implementation-workflow-drift-handling/technical-spec.md`
- Worktree execution is required for later authoring / implementation work:
  - worktree path: `/Users/andrew/code/python/agent-skills.worktrees/python-implementation-workflow-drift-handling`
  - base branch: `dev`
  - feature branch: `feat/andrew/python-implementation-workflow-drift-handling`
  - PR target branch: `dev`
- Repo workflow authority for this topic:
  - `plan/agent-handoff-workflow.md`

## Goal / Outcome

- Add a repo-visible execution contract for `python-implementation-workflow-drift-handling` so later creator work can update:
  - `.github/agents/python-implementation-workflow.agent.md`
  - `plan/agent-handoff-workflow.md`
- When this topic is complete, both files consistently define:
  - impact-based routing between ordinary `needs-rework` and correction-triggering drift
  - planner-confirmed severity after workflow-agent provisional classification
  - conditional correction artifact requirements
  - parent/current truth versus correction/historical truth semantics
  - correction closure only after review completion and parent sync

## Scope

- **In scope**:
  - Update `.github/agents/python-implementation-workflow.agent.md` with drift/correction handling policy
  - Update `plan/agent-handoff-workflow.md` so the repo-level workflow contract matches the custom agent
  - Keep all routing within the existing 6-phase custom-agent structure
  - Define conditional use of `*.correction-plan.md` / `*.correction-step.md` as topic-level correction artifacts for medium/high drift
  - Preserve the existing role boundary:
    - human raises direction concern
    - workflow agent does provisional routing
    - planner confirms severity and closes correction
    - implementer performs the repair work

- **Out of scope**:
  - Editing `.github/copilot-instructions.md`, `README.md`, or `VERSION`
  - Adding parser/tooling support that machine-reads correction artifacts
  - Changing git STOP POINT behavior, merge flow, or release flow
  - Updating unrelated python-* skills in the same topic
  - Creating always-on correction artifacts for every workflow topic

## Locked Decisions

- This is a **review-ready-only topic with no stable-library surfaces**.
- The analysis layer is already frozen and outranks conversation-time restatements unless a human explicitly says `override`.
- Severity authority is fixed:
  - workflow agent may perform provisional classification
  - planner must confirm final severity
 - Correction closure authority is fixed:
   - planner closes correction only after the required reviews pass
 - Success signals are fixed and all three are in scope:
   - medium/high drift cannot silently advance
   - required correction artifacts and parent sync must occur
   - role boundaries must remain explicit
 - Workstream A routing contract is fixed:
   - routing states must be exactly:
     - `IMPLEMENT_CONTINUE`
     - `IMPLEMENT_PATCH`
     - `PLANNER_CLARIFY`
     - `PLANNER_REPLAN`
   - the custom agent must include one routing decision table row per state
   - each routing decision table row must define:
     - trigger
     - owner
     - required artifact
     - next phase
     - acceptance condition
 - Workstream A reporting contract is fixed:
   - the custom agent must define a `Deviation / Correction Report`
   - that report must include markdown explanatory sections plus a fixed JSON `Machine Verdict` block
 - The ordinary-rework boundary is fixed:
   - if the issue changes source-of-truth semantics, public contract meaning, architecture boundary, or phase routing, it is correction-triggering drift
   - otherwise it may remain ordinary `needs-rework`
 - Correction artifact policy is fixed:
   - low severity -> note only
   - medium severity -> `*.correction-plan.md`, plus `*.correction-step.md` when multi-step repair is required
   - high severity -> both correction artifacts and current implementation treated as suspect code
 - Parent artifacts remain current truth; correction artifacts remain historical truth and must not replace the parent contract.
 - Correction artifact retention is fixed:
   - correction artifacts may be marked `resolved` or `superseded`
   - direct deletion is forbidden
 - Parent sync note contract is fixed for applicable correction artifacts:
   - each medium/high correction artifact must include a parent sync note
   - the parent sync note must state:
     - which parent plan section is added or corrected
     - whether acceptance criteria changed
     - whether phase routing changed
     - whether existing tasks changed

## Boundaries / Exclusions

- The planning actor defines the execution contract; it does not implement the custom agent or workflow document in this topic-plan authoring step.
- Creator work must stay limited to:
  - `.github/agents/python-implementation-workflow.agent.md`
  - `plan/agent-handoff-workflow.md`
- Reviewer evaluates the creator output against this plan; reviewer does not author the final correction policy directly.
- Main Agent must not retroactively change the planning intent without updating this plan.
- If implementation later reveals that safe execution also requires parser/script/tooling changes, stop and split or expand scope explicitly instead of silently editing extra surfaces.
- Future ADR or workflow-policy promotion is a separate topic; do not smuggle that work into this one.

## Status / Allowed Transitions

- **Current**: `planned`
- **Execution model**: follow the canonical creator -> reviewer -> publish -> merge path; this topic stops at `merged` and does not declare a release action
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

- Use the standard Phase 4.5 planner contract alignment rule before publish work.
- If later creator output introduces artifact paths outside this plan, treat that as plan-alignment drift and repair the plan before execution continues.
- If creator output weakens the strict analysis-layer contract, route back to `creator-in-progress` rather than publishing a softened implementation.

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/python-implementation-workflow-drift-handling/python-implementation-workflow-drift-handling.plan.md` | Planning actor | Repo-visible execution contract for this topic |
| Requirements baseline | `analysis/python-implementation-workflow-drift-handling/requirements.md` | Planning actor | Frozen business baseline that defines the authority, success signals, and correction boundaries |
| Technical baseline | `analysis/python-implementation-workflow-drift-handling/technical-spec.md` | Planning actor | Frozen execution-facing technical baseline that this plan must map to 100% |
| Custom agent contract | `.github/agents/python-implementation-workflow.agent.md` | Creator | Primary implementation target for drift/correction routing behavior |
| Repo workflow contract | `plan/agent-handoff-workflow.md` | Creator | Repo-level workflow contract that must be updated to remain consistent with the custom agent |

Artifact path notes:

- `README.md`: no change in this topic
- `VERSION`: no change in this topic
- `.github/copilot-instructions.md`: no change in this topic
- Treat the listed paths as an executable contract.
- If later work proposes edits outside the listed paths, stop and repair the plan or split the topic instead of widening scope implicitly.

## Implementation Steps

1. Update `.github/agents/python-implementation-workflow.agent.md` so it adds a global drift/correction policy, defines the four routing states, records provisional-versus-final severity authority, adds the Deviation / Correction Report format, and updates Phase 3 / 4 / 5 so medium/high drift cannot silently advance and correction closure requires planner-confirmed completion.
2. Update `plan/agent-handoff-workflow.md` so it explicitly defines parent artifacts as current truth, correction artifacts as historical truth, encodes the severity-gated correction artifact rule, requires parent sync before correction closure, and forbids silent deletion of resolved/superseded correction artifacts.
   - preserve correction artifacts as historical truth by allowing `resolved` / `superseded` status changes but forbidding direct deletion
3. Verify the two edited workflow surfaces remain aligned with the frozen analysis layer:
   - no contradiction with source-of-truth authority
   - no contradiction with role ownership
   - no contradiction with STOP POINT semantics
   - no accidental expansion into parser/tooling or stable-library work
   - no missing routing-state, decision-table, or Machine Verdict contract from Workstream A
   - no missing parent sync note requirement for applicable correction artifacts

## Validation / Acceptance Checks

- The topic plan remains in strict-mode alignment with:
  - `analysis/python-implementation-workflow-drift-handling/requirements.md`
  - `analysis/python-implementation-workflow-drift-handling/technical-spec.md`
- `.github/agents/python-implementation-workflow.agent.md` keeps the 6-phase structure intact.
- The custom agent explicitly distinguishes:
  - ordinary `needs-rework`
  - correction-triggering drift
  - provisional severity classification
  - planner-confirmed final severity
- The custom agent defines all four routing states exactly as locked in this plan:
  - `IMPLEMENT_CONTINUE`
  - `IMPLEMENT_PATCH`
  - `PLANNER_CLARIFY`
  - `PLANNER_REPLAN`
- The custom agent includes a routing decision table whose rows each specify:
  - trigger
  - owner
  - required artifact
  - next phase
  - acceptance condition
- The custom agent includes a `Deviation / Correction Report` with markdown explanatory sections and a fixed JSON `Machine Verdict` block.
- `plan/agent-handoff-workflow.md` and the custom agent agree on:
  - current truth vs historical truth
  - correction closure authority
  - severity-gated correction artifact requirements
 - required parent sync note fields for applicable correction artifacts
  - resolved / superseded allowed, direct deletion forbidden
- No new stable-library metadata is required because this topic does not modify `README.md`, `VERSION`, or release timing.
- No file outside `Artifact Paths` is required to satisfy the plan; if such a file becomes necessary, execution must stop and repair scope first.
- Any future use of correction artifacts in later topics must still be explicitly listed in those topics' `Artifact Paths`.

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

- After STOP POINT 2 is reached, this topic remains stopped until a human explicitly confirms the merge is complete and asks the workflow to continue.
- Only after that explicit STOP POINT 2 resume message may local cleanup and sync route through the repository's post-merge workflow.
- No repository release action is required for this topic.
- No `README.md` or `VERSION` change should be deferred to release because this topic has no stable-library intent.

## Open Questions / Unresolved Items

- None.
