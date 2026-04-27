# PR Comment Observation Gate Plan

## Goal / Outcome

Create a repo-visible execution plan for a workflow-contract topic that fixes the
PR comment loop before manual merge handoff. The completed topic should update
the canonical workflow documents so they no longer treat one empty PR-comment
fetch as proof that a PR is merge-ready. Instead, the workflow should require a
bounded observation window that makes the PR eligible for the `STOP POINT 2`
human merge-confirmation prompt, while still preserving the hard-stop rule that
no automatic polling or resume may happen after merge handoff.

## Scope

- **In scope**:
  - update `plan/agent-handoff-workflow.md`
  - update `.github/guides/MAIN-AGENT-WORKFLOW.md`
  - define the bounded observation-window contract for PR comment and check
    monitoring before merge handoff
  - define how an exhausted clean observation window becomes eligible for the
    `STOP POINT 2` human merge-confirmation prompt
  - make the pre-handoff / post-handoff stop semantics explicit so the workflow
    does not silently re-check merge state after handoff

- **Out of scope**:
  - changing `.github/copilot-instructions.md`
  - changing `README.md` or `VERSION`
  - changing any skill under `.github/skills/`
  - changing `.github/agents/workflow-gate.agent.md` or
    `.github/guides/COPILOT-CLI-WORKFLOW.md` in this topic
  - modifying GitHub Copilot CLI product behavior outside repo-visible workflow
    rules
  - implementing runtime-level protections against external autopilot or
    completion reminders beyond what this repository can express in its own
    workflow contract

## Locked Decisions

- This topic is **review-ready-only with no stable-library surfaces**.
- First-draft output is limited to the two canonical workflow documents:
  - `plan/agent-handoff-workflow.md`
  - `.github/guides/MAIN-AGENT-WORKFLOW.md`
- Replace the current optimistic rule:
  - `If NO comments -> PR is clean -> proceed to STOP POINT 2`
- With a stricter gate:
  - use a bounded observation window before merge handoff
  - observation shape: `consecutive-empty-checks`
  - observation backoff schedule:
    - first wait: 30 seconds
    - second wait: 60 seconds
    - third wait: 120 seconds
  - observation signals must include:
    - PR reviews / current review state
    - review comments
    - issue comments
    - check runs
  - blocking signals must include any newly observed:
    - PR review with a blocking review state, especially `CHANGES_REQUESTED`
    - unresolved blocking review thread
    - actionable review comment that still requires action
    - actionable issue comment that still requires action
    - non-clean check run state:
      - status is not `completed`, or
      - conclusion is not a success-like state such as `success`, `neutral`, or
        `skipped`
- Exhausting a clean observation window does **not** automatically trigger merge
  handoff.
- After the observation window is exhausted with no blocking signal, the agent
  may report only:
  - that no new blocking signal was seen within the bounded observation window,
    including PR reviews, comments, and check runs
  - that this is not a guarantee no later feedback will arrive
  - that a human must decide whether to check the PR and hand off merge
- `STOP POINT 2` remains a hard stop:
  - once the workflow enters merge handoff, the agent must fully stop
  - it must not poll for merge detection
  - it must not reawaken and re-check merge state without a new explicit human
    resume message
- This topic fixes repo-visible execution contract language only; it does not
  claim to change the Copilot CLI runtime or suppress external system reminders.

## Boundaries / Exclusions

- `plan/agent-handoff-workflow.md` remains the canonical phase and stop-point
  contract.
- `.github/guides/MAIN-AGENT-WORKFLOW.md` remains the executable guide that must
  mirror, not redefine, the canonical workflow semantics.
- This topic must not broaden into:
  - generic PR automation policy
  - release-gate redesign
  - reviewer logic redesign
  - topic-plan authoring rules
- If later work needs changes to:
  - `workflow-gate.agent.md`
  - `COPILOT-CLI-WORKFLOW.md`
  - broader autopilot / reminder behavior guidance
  create a separate topic rather than expanding this workflow-contract fix.

## Status / Allowed Transitions

- **Current**: `planned`
- **Execution model**: follow the canonical creator -> reviewer -> publish ->
  merge path; this topic ends at `merged` with no separate Phase 10 release
  action.
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

- Use the standard Phase 4.5 planner-alignment checkpoint from
  `plan/agent-handoff-workflow.md`.
- If creator or reviewer drifts into CLI product speculation, skill-folder
  editing, or stable-library discoverability work, route back to
  `creator-in-progress` and repair scope before publish.

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/pr-comment-observation-gate/pr-comment-observation-gate.plan.md` | Planning actor | Repo-visible execution contract for this topic |
| Canonical workflow spec | `plan/agent-handoff-workflow.md` | Creator | Canonical workflow contract updated to use bounded observation and human-confirmed merge handoff |
| Executable workflow guide | `.github/guides/MAIN-AGENT-WORKFLOW.md` | Creator | Executable phase guide updated to mirror the new observation-window and stop semantics |

Artifact path notes:

- This topic does **not** modify `README.md`, `VERSION`,
  `.github/copilot-instructions.md`, `.github/skills/`, `.github/agents/`, or
  `.github/guides/COPILOT-CLI-WORKFLOW.md`.
- These paths are an executable contract.
- `Stable library metadata` is intentionally absent because this topic is not a
  stable-library publish topic.
- If later work appears outside these paths, treat that as plan drift and split
  it into a separate topic.

## Implementation Steps

### Creator Phase (after plan approval)

1. Update `plan/agent-handoff-workflow.md` Phase 7-8 logic so the PR loop no
   longer treats one empty comment fetch as merge readiness.
2. Define the bounded observation window explicitly:
    - `consecutive-empty-checks`
    - backoff schedule `30s -> 60s -> 120s`
    - signals: PR reviews / review state, review comments, issue comments,
      check runs
3. Define which events reset the observation window, including new actionable
   comments, blocking PR review states, unresolved blocking comment or thread
   signals, failed checks, or other newly blocking PR state.
4. Separate the workflow states conceptually so the documents no longer collapse
   these into one step:
   - clean snapshot
   - observation window still active
   - observation window exhausted with no blocking signal
   - eligible for human merge-readiness confirmation
   - `STOP POINT 2`
5. Update merge-handoff wording so the agent may report bounded observation
   results but may not automatically advance to manual merge handoff.
6. Preserve the existing hard-stop rule after `STOP POINT 2`:
   - no merge polling
   - no automatic re-check
   - no automatic resume without a new human message
7. Mirror the same contract in `.github/guides/MAIN-AGENT-WORKFLOW.md` without
   inventing a conflicting second workflow model.

### Reviewer Phase (after creator delivers review-ready)

1. Verify both workflow documents exist at the locked paths.
2. Verify the old rule `If NO comments -> PR is clean` is no longer the
   operative merge-handoff gate.
3. Verify the bounded observation window is explicit and includes:
    - `consecutive-empty-checks`
    - `30s -> 60s -> 120s`
    - PR reviews / review state, review comments, issue comments, and check runs
 4. Verify the blocking-signal definition is explicit and includes blocking PR
    review states, unresolved blocking threads, comments, and non-clean check
    states.
5. Verify exhausting the clean observation window does **not** automatically
    move the workflow to `STOP POINT 2`.
6. Verify observation-window exhaustion becomes eligible for the `STOP POINT 2`
   human merge-confirmation prompt rather than bypassing or duplicating that
   stop point.
7. Verify both documents still preserve the hard-stop semantics after
    `STOP POINT 2`.
8. Verify the guide mirrors the canonical contract instead of diverging from it.

### Main Agent Publish Phase (after approval + planner alignment)

1. Stage only:
   - `plan/agent-handoff-workflow.md`
   - `.github/guides/MAIN-AGENT-WORKFLOW.md`
   - `plan/pr-comment-observation-gate/pr-comment-observation-gate.plan.md`
2. Do not stage unrelated docs or workflow-adjacent files.
3. Open the PR with the canonical spec change and executable guide update
   visible together.

## Validation / Acceptance Checks

- [ ] The topic plan remains valid at
  `plan/pr-comment-observation-gate/pr-comment-observation-gate.plan.md`.
- [ ] `Status / Allowed Transitions` uses canonical workflow transitions only.
- [ ] `Artifact Paths` remain exact and bounded to the listed repo-visible files.
- [ ] Non-stable intent is explicit:
  - [ ] `README.md` is unchanged
  - [ ] `VERSION` is unchanged
  - [ ] `Stable library metadata` is intentionally absent
- [ ] Creator output is limited to:
  - [ ] `plan/agent-handoff-workflow.md`
  - [ ] `.github/guides/MAIN-AGENT-WORKFLOW.md`
- [ ] Main Agent publish output is limited to those files plus this topic plan.
- [ ] The new PR loop contract is explicit:
  - [ ] no single empty fetch may trigger merge handoff
  - [ ] the bounded observation window is defined as `consecutive-empty-checks`
  - [ ] the backoff schedule is `30s -> 60s -> 120s`
  - [ ] observation signals include PR reviews / review state, review comments,
    issue comments, and check runs
  - [ ] blocking signals explicitly include blocking PR review states,
    unresolved blocking threads, comments, and non-clean check states
  - [ ] observation-window exhaustion does not auto-handoff merge
  - [ ] observation-window exhaustion becomes eligible for the `STOP POINT 2`
    human merge-confirmation prompt
- [ ] `STOP POINT 2` remains a true hard stop:
  - [ ] no merge polling after handoff
  - [ ] no automatic re-check after handoff
  - [ ] no automatic resume without a new explicit human message
- [ ] Reviewer handoff remains a single machine-consumable JSON object.

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

- After merge handoff, Main Agent must remain stopped at `STOP POINT 2` until a
  new explicit human resume message arrives.
- Phase 9 post-merge local sync may run only after:
  - the human explicitly resumes the workflow in a new message
  - the merge is confirmed on GitHub
- Once those conditions are satisfied, Main Agent performs normal post-merge
  local sync and marks the topic `merged`.
- No separate Phase 10 release action is required in this topic.
- Do not create a tag, release notes artifact, or version bump from this topic.

## Open Questions / Unresolved Items

- None. The bounded observation window, signal set, and human-confirmed handoff
  gate are locked for first-draft execution.
