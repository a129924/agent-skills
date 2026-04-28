# Stop Point Terminal State Hardening

## Goal / Outcome

Harden the repository's workflow documentation so that STOP POINT 2 is modeled as
a true terminal state in the workflow state machine, operator guidance explicitly
teaches when to use autopilot safely with the `--max-autopilot-continues` flag,
and all four canonical workflow documents align on the same terminal-state
semantics. By the end of this topic:

- STOP POINT 2 is defined as a terminal/no-op state with no polling or implicit
  transitions.
- Resume is modeled as an explicit transition with strict entry conditions.
- Operators have clear guidance on combining STOP POINT 1 vs. STOP POINT 2 with
  autopilot mode.
- The `--max-autopilot-continues <count>` flag is documented as an authoritative
  control for bounding autonomous continuation turns.
- Premium request waste from unintended continuation at STOP POINT 2 is mitigated.

## Scope

### In scope

**Workflow / documentation files (4 files)**:

1. `plan/agent-handoff-workflow.md` — canonical repo-level workflow contract
   - Add "Workflow layering" section explaining repo-level vs skill-local semantics
   - Add "State machine rules" section with explicit entry/transition/terminal rules
   - Tighten STOP POINT 1 and STOP POINT 2 rule sections with explicit
     terminal-state language
   - Add "Source of truth" clarification

2. `.github/guides/MAIN-AGENT-WORKFLOW.md` — executable guide for Main Agent phases
   - Mirror the workflow-layering and state-machine rules from canonical spec
   - Update STOP POINT 2 language to match terminal-state model
   - Add explicit operator guidance for autopilot behavior before STOP POINT 2

3. `.github/agents/workflow-gate.agent.md` — workflow router agent
   - Add explicit guidance on STOP POINT 1 vs. STOP POINT 2 semantics
   - Clarify that stop points override skill-local routing decisions
   - Document `--max-autopilot-continues` usage rules in agent context

4. `.github/guides/COPILOT-CLI-WORKFLOW.md` — CLI operating guide
   - Add section on `--max-autopilot-continues <count>` flag and when to use it
   - Explain the difference between STOP POINT 1 (positive authorization)
     and STOP POINT 2 (terminal/no-op)
   - Provide examples of safe autopilot usage (through next explicit positive gate)
   - Provide guidance on leaving autopilot before STOP POINT 2

**Scope output**:

- Four updated workflow documents with aligned terminal-state language
- No changes to stable-library files (README, VERSION)
- No changes to skill implementation directories
- All workflow-level changes are backward-compatible with existing topics

### Out of scope

- Modifying the Copilot CLI product or runtime behavior
- Changing the definition of STOP POINT 1 or adding new stop points
- Modifying individual skill execution flows inside `.github/skills/*/`
- Release timing or versioning decisions
- Changes to README.md or VERSION
- Merging or releasing this topic as part of a stable-library update

## Locked Decisions

- This is a **non-stable-library topic**: the outcome is improved operator guidance
  and workflow hardening, not a new stable skill or feature release. No README
  row or VERSION bump is required.
- Scope is locked at exactly 4 files: the two canonical workflow specs, the
  router agent, and the CLI guide.
- STOP POINT 2 is modeled as a terminal/no-op state, not as an async-polling
  state. This is a modeling decision, not a guarantee that the Copilot CLI
  runtime will never reawaken an autopilot session, but it hardens the repo
  contract to guide operator behavior.
- The `--max-autopilot-continues <count>` flag is documented as the primary
  technical control for bounding continuation turns. This is an operator-level
  control, not a code implementation in this repository.
- STOP POINT 1 and STOP POINT 2 are fundamentally different types of gates and
  must have different autopilot usage guidance. STOP POINT 1 allows
  continuation; STOP POINT 2 stops.

## Boundaries / Exclusions

- **Role boundaries**: This topic is planning + workflow docs only; creator will
  update documents, not implement code changes.
- **Workflow-level changes only**: Do not modify skills, agents, or task
  implementations beyond the canonical workflow guidance.
- **No CLI product changes**: The topic documents operator usage of existing CLI
  features; it does not modify the CLI itself.
- **Backward compatibility**: All changes must preserve existing topic behavior
  and not retroactively alter completed workflows.
- **Assumption boundary**: The topic assumes `--max-autopilot-continues` works as
  documented in current Copilot CLI (`copilot --help`); if the flag's behavior
  changes, the documented guidance may need refresh.

## Status / Allowed Transitions

- **Current**: `planned`
- **Execution model**: follow the canonical creator → reviewer → publish → merge
  path
- **No stable-library timing**: This topic does not declare a release action; it
  is complete when merged.

**Allowed transitions**:

- `planned` → `creator-in-progress`
- `creator-in-progress` → `review-ready`
- `review-ready` → `reviewer-in-progress`
- `reviewer-in-progress` → `approved` | `needs-rework`
- `needs-rework` → `creator-in-progress`
- `approved` → `publish-in-progress`
- `publish-in-progress` → `pr-open` | `merged`
- `pr-open` → `needs-rework` | `merged`
- `merged` → terminal

**Routing notes**:

- Standard Phase 4.5 routing: after `approved`, Main Agent decides whether to
  publish immediately or await additional review. Use standard routing.
- This is a workflow docs topic, not a skill topic, so the creator artifact will
  be four updated Markdown files, not a `.github/skills/<name>/` directory.

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/stop-point-terminal-state-hardening/stop-point-terminal-state-hardening.plan.md` | Planning actor | Repo-visible execution contract for this topic |
| Canonical workflow hardening | `plan/agent-handoff-workflow.md` | Creator | State machine rules, workflow layering, terminal-state STOP POINT 2 model, source-of-truth clarification |
| Executive guide update | `.github/guides/MAIN-AGENT-WORKFLOW.md` | Creator | Mirror workflow-layering and state-machine rules; add autopilot operator guidance for STOP POINT 2 |
| Workflow router agent update | `.github/agents/workflow-gate.agent.md` | Creator | STOP POINT 1 vs. 2 semantics, `--max-autopilot-continues` guidance in agent context |
| CLI operating guide update | `.github/guides/COPILOT-CLI-WORKFLOW.md` | Creator | `--max-autopilot-continues` flag documentation, STOP POINT 1 vs. 2 autopilot usage patterns, operator examples |

**Artifact path notes**:

- All four paths are existing workflow files; no new files are created.
- `README.md` and `VERSION` are **not** modified in this topic.
- `.github/copilot-instructions.md` is **not** modified in this topic.
- The topic plan itself lives in `plan/stop-point-terminal-state-hardening/` and
  serves as the execution contract.
- If implementation work drifts outside these four files, stop and update the plan
  before continuing.

## Implementation Steps

### Phase: Creator drafting

1. **Read and understand the current contract**:
   - Review `plan/agent-handoff-workflow.md` current sections on STOP POINT 1 and
     STOP POINT 2.
   - Review `.github/guides/MAIN-AGENT-WORKFLOW.md` sections on execution phases
     and stop-point handling.
   - Review `.github/agents/workflow-gate.agent.md` for existing routing logic.
   - Review `.github/guides/COPILOT-CLI-WORKFLOW.md` for current operator
     guidance.

2. **Harden `plan/agent-handoff-workflow.md`**:
   - Add a new top-level section: "Workflow layering"
     - Explain that repo-level phase semantics override skill-local execution
       details.
     - State that stop points are explicit workflow contract, not internal
       implementation detail.
   - Add a new top-level section: "State machine rules"
     - Define required elements: entry condition, allowed transitions,
       stop/terminal rules.
     - Require explicit entry conditions instead of inferred progress.
     - Require explicit allowed next statuses.
     - Require explicit terminal-state rules (no polling, no implicit resume).
   - Update existing STOP POINT 1 section:
     - Clarify that STOP POINT 1 is a positive authorization gate.
     - After human approval, continuation is expected behavior.
   - Update existing STOP POINT 2 section:
     - Explicitly model as a terminal/no-op state.
     - After merge handoff, no polling, no background waiting, no inferred
       progress.
     - Resume is only via new explicit human message.
   - Add a new section: "Source of truth"
     - State that repo-visible topic plans are authoritative for single topics.
     - State that this workflow spec is authoritative for repo-level phases.
     - State that skill-local instructions are authoritative only within their
       skill boundary.
     - Explicitly forbid relying on hidden chat context to override repo-visible
       artifacts.

3. **Update `.github/guides/MAIN-AGENT-WORKFLOW.md`**:
   - Mirror the "Workflow layering" and "State machine rules" sections from the
     canonical spec.
   - Update Phase 8-9 (merge and STOP POINT 2) language to match terminal-state
     model.
   - Add explicit operator guidance:
     - If using autopilot, consider `copilot --max-autopilot-continues 1` or `0`
       before STOP POINT 2.
     - If not using autopilot, ensure explicit post-merge resume message.
     - Document that STOP POINT 2 is a terminal/no-op state, not a validation
       gate.

4. **Update `.github/agents/workflow-gate.agent.md`**:
   - Add a section explaining STOP POINT 1 vs. STOP POINT 2 semantics to the
     workflow router agent.
   - Clarify that stop points are hard constraints that override skill-local
     routing.
   - Document `--max-autopilot-continues` usage in the agent's context:
     - Suggest using `--max-autopilot-continues N` when the user wants safe
       bounds on continuation.
     - Explain that this is an operator control, not an agent decision.
     - Provide examples of safe usage patterns.

5. **Update `.github/guides/COPILOT-CLI-WORKFLOW.md`**:
   - Add a new section: "Autopilot and continuation limits"
     - Document the `--max-autopilot-continues <count>` flag.
     - Explain what it does: limits the number of autonomous continuation turns.
     - Provide examples:
       - `copilot --max-autopilot-continues 3` for general exploration.
       - `copilot --max-autopilot-continues 1` before STOP POINT 2.
       - `copilot --max-autopilot-continues 0` to disable autopilot continuation
         entirely.
   - Add explicit STOP POINT 1 vs. STOP POINT 2 usage guidance:
     - STOP POINT 1: Autopilot can safely run through this gate after human
       approval; continuation is expected.
     - STOP POINT 2: Autopilot should not continue past this gate; use
       `--max-autopilot-continues 1` or leave autopilot, then send explicit
       resume message after merge.
   - Provide real-world examples:
     - Safe autopilot path: start → approve STOP POINT 1 → continue to next
       validation gate.
     - Safe manual path: start autopilot → hit STOP POINT 2 → use `Shift+Tab` to
       leave → merge manually → send explicit resume message.
     - Unsafe path (now documented as problematic): autopilot continues infinitely
       after STOP POINT 2 emitting "Continuing autonomously" turns.

6. **Verify consistency across all four files**:
   - Ensure STOP POINT 1 and STOP POINT 2 are described identically across all
     files.
   - Ensure terminal-state language is consistent.
   - Ensure no contradictory guidance.

### Phase: Validation and acceptance

After creator drafting completes, reviewer will verify:

- All four files have been updated with terminal-state language.
- STOP POINT 2 is explicitly modeled as a terminal/no-op state with no polling.
- Resume is modeled as an explicit transition with strict entry conditions.
- `--max-autopilot-continues` flag is documented in CLI workflow guide.
- Examples clearly show STOP POINT 1 vs. STOP POINT 2 autopilot usage patterns.
- No contradictions or vague "TBD" sections remain.

## Validation / Acceptance Checks

**Creator must verify before handing off to reviewer**:

1. All four artifact paths are updated.
2. STOP POINT 2 section in all files now uses explicit terminal-state language
   (no polling, no background waiting, explicit resume transition).
3. `--max-autopilot-continues` flag is documented with examples.
4. STOP POINT 1 vs. STOP POINT 2 usage patterns are explained for both autopilot
   and non-autopilot modes.
5. No vague language like "TBD", "later", "follow normal process" remains.
6. The four files are self-consistent (same STOP POINT definitions across all).
7. Examples are actionable (e.g., actual command lines, real PR workflow
   sequences).

**Reviewer must verify before approving**:

1. Terminal-state modeling is mathematically sound (no implicit transitions
   possible).
2. Backward compatibility: existing topics' workflows are not broken by these
   changes.
3. Scope boundaries are respected: no changes to skills, README, VERSION, or
   `.github/copilot-instructions.md`.
4. Operator guidance is clear and actionable (operators should be able to read
   the guide and immediately know whether to use `--max-autopilot-continues` and
   what value to choose).
5. The `--max-autopilot-continues` flag documentation is honest about what it
   controls and what it does not (e.g., it does not replace explicit operator
   attention; it is a safety limit, not a guarantee).

## Reviewer Handoff

Use this JSON template:

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

**For `approved` verdict, confirm**:

- All four workflow files have been updated.
- STOP POINT 2 is consistently modeled as a terminal/no-op state across all files.
- `--max-autopilot-continues` flag is documented with clear usage patterns.
- No backward-compatibility breaks are present.
- All artifact paths match the locked scope.
- Examples are actionable and grounded in real usage.

**For `needs-rework` verdict, identify**:

- Which sections remain vague or contradictory.
- Which files are missing updates.
- Which examples are unclear.
- Any backward-compatibility concerns.

## Post-merge / release actions

**No stable-library or release action is required** for this topic. This is a
workflow hardening topic, not a stable-library feature or skill release.

**After merge**:

- Main Agent will perform standard post-merge cleanup (branch deletion, local
  sync).
- The updated workflow guidance becomes immediately effective for all future
  topics in this repository.
- No README update.
- No VERSION bump.
- No release tag.
- Future topics and operators should reference the updated workflow documents.

## Open Questions / Unresolved Items

1. **Flag configuration persistence**: Can `--max-autopilot-continues` be set
   persistently in `~/.copilot/settings.json`, or is it CLI-flag-only? This is
   for user education; the documentation should note where operators can set it.
   (This question does not block the topic; documentation can say "use CLI flag"
   as the primary method.)

2. **Recommended limit for this repo**: Should the repository recommend a default
   max-continues limit for operators working on workflow topics? Examples:
   - `--max-autopilot-continues 3` for general exploration
   - `--max-autopilot-continues 1` before STOP POINT 2
   - `--max-autopilot-continues 0` for explicit control

   (The topic can document these as "patterns to consider" without mandating a
   single global limit.)

3. **CLI documentation sync**: The Copilot CLI's authoritative docs may also need
   updates to feature the `--max-autopilot-continues` flag more prominently. This
   is out of scope for this repository topic but noted for awareness.

---

**Plan status**: `planned` — ready for creator handoff.

**Date created**: 2026-04-28

**Topic owner**: Not yet assigned.
