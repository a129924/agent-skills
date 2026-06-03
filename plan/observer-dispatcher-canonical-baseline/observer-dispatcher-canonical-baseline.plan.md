## Analysis-layer routing

- Mode: `strict`
- Requirements baseline:
  `analysis/observer-dispatcher-canonical-baseline/requirements.md`
- Technical baseline:
  `analysis/observer-dispatcher-canonical-baseline/technical-spec.md`
- Priority rule: implementation must map 100% to the technical baseline above.
  Chat-time intent in this topic is already frozen into those repo-visible
  artifacts and must not be rediscovered during implementation.

# Observer / Dispatcher Canonical Baseline Plan

## Goal / Outcome

Create a bounded Feature 1 baseline that introduces one canonical workflow
agent artifact under `agents/`, three supporting skills under `skills/`, and
aligned repo-truth wording across the four designated documentation surfaces.

When the topic is complete:

- `skills/` still reads as the repository's primary canonical skill source
- `agents/` exists as the canonical source for repo-defined workflow agent
  artifacts
- the Observer / Dispatcher role is defined without expanding into a broader
  agent system
- Feature 1 remains explicitly bounded away from concrete agents, registry
  behavior, workflow binding, and runtime semantics

## Scope

- **In scope**:
  - Create `agents/observer-dispatcher.agent.md`
  - Create `skills/subagent-dispatch-policy/SKILL.md`
  - Create `skills/subagent-dispatch-policy/examples.md`
  - Create `skills/context-package-builder/SKILL.md`
  - Create `skills/context-package-builder/examples.md`
  - Create `skills/handoff-routing-policy/SKILL.md`
  - Create `skills/handoff-routing-policy/examples.md`
  - Update `AGENTS.md`
  - Update `docs/repo-positioning.md`
  - Update `.github/copilot-instructions.md`
  - Update `README.md`
  - Maintain topic-local planning artifacts at:
    - `analysis/observer-dispatcher-canonical-baseline/requirements.md`
    - `analysis/observer-dispatcher-canonical-baseline/technical-spec.md`
    - `plan/observer-dispatcher-canonical-baseline/observer-dispatcher-canonical-baseline.plan.md`
    - `plan/observer-dispatcher-canonical-baseline/observer-dispatcher-canonical-baseline.step.md`
    - `plan/observer-dispatcher-canonical-baseline/observer-dispatcher-canonical-baseline.review-log.md`

- **Out of scope**:
  - Create concrete Planner / Implementer / Reviewer / Correction Planner agent
    files
  - Create any agent registry, catalog, or mapping table
  - Define workflow-to-agent binding
  - Define runtime orchestration semantics or launcher behavior
  - Create compatibility mirrors such as `.github/agents/**`
  - Encode, migrate, normalize, or bind existing human-operated workflows
  - Modify `VERSION`, perform release work, or add release metadata
  - Modify any file outside the exact paths listed in `Artifact Paths`

## Locked Decisions

- This topic is **not** a stable-library publish topic. No `VERSION` bump or
  release action is allowed.
- Root `agents/` is introduced as a bounded canonical source for repo-defined
  workflow agent artifacts, but `skills/` remains the repository's primary
  canonical source for reusable skill behavior.
- Feature 1 creates exactly one concrete workflow agent artifact:
  `agents/observer-dispatcher.agent.md`.
- The Observer contract must contain:
  - a hard stop rule
  - a real-dispatch definition
  - fixed Observer state values:
    `INTAKE`, `DISPATCHED`, `WAITING`, `ROUTING`, `BLOCKED`, `COMPLETE`
  - fixed subAgent verdict values:
    `PASS`, `PATCH_REQUIRED`, `REPLAN_REQUIRED`, `MISSING_EVIDENCE`,
    `BLOCKED`
- `Required Dispatch`, `Target Role`, and `Next Route` may point only to these
  role names:
  - `Planner`
  - `Implementer`
  - `Reviewer`
  - `Correction Planner`
- `.codex/**` may be described only as a repo-policy projection /
  compatibility surface. It must not be described as a canonical source or an
  external platform authority model.
- Existing workflows remain external to this baseline. When workflow execution
  state is needed, the only allowed workflow-derived input is a topic-local
  step artifact such as `plan/<topic>/<topic>.step.md`.
- If later implementation needs concrete agents, registry behavior,
  workflow-to-agent binding, runtime semantics, or any file outside the exact
  write set, stop and re-plan instead of stretching Feature 1.

## Boundaries / Exclusions

- The Observer artifact must stay routing-only. It must not implement, review,
  fix, rewrite, approve, or simulate missing roles.
- The supporting skills must stay sharply separated:
  - `subagent-dispatch-policy` chooses the next role or stop
  - `context-package-builder` packages one minimal task context
  - `handoff-routing-policy` routes one subAgent result
- Do not encode the repository's existing human-operated workflow into the
  Observer baseline.
- Do not infer current workflow progression from chat history. Only repo-visible
  planning artifacts may carry that truth.
- Do not add any path beyond the exact artifact contract below.

## Status / Allowed Transitions

- **Current**: `planned`
- **Execution model**: follow the canonical creator -> reviewer -> publish ->
  merge path, but this topic does not declare release work
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

- Use the standard Phase 4.5 planner-alignment rule from
  `plan/agent-handoff-workflow.md`.
- Reviewer feedback that changes scope, artifact paths, or fixed contract values
  must route back to `creator-in-progress`.
- Reviewer feedback that controls routing or multi-round rework must be
  materialized at
  `plan/observer-dispatcher-canonical-baseline/observer-dispatcher-canonical-baseline.review-log.md`.
- If required implementation expands outside the exact artifact set, stop and
  repair the plan before any creator work continues.

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic requirements baseline | `analysis/observer-dispatcher-canonical-baseline/requirements.md` | Planning actor | Frozen business baseline for Feature 1 |
| Topic technical baseline | `analysis/observer-dispatcher-canonical-baseline/technical-spec.md` | Planning actor | Execution-facing technical baseline for Feature 1 |
| Topic plan | `plan/observer-dispatcher-canonical-baseline/observer-dispatcher-canonical-baseline.plan.md` | Planning actor | Repo-visible execution contract for Feature 1 |
| Topic step artifact | `plan/observer-dispatcher-canonical-baseline/observer-dispatcher-canonical-baseline.step.md` | Planning actor / Main Agent | Topic-local workflow progression artifact |
| Topic review log | `plan/observer-dispatcher-canonical-baseline/observer-dispatcher-canonical-baseline.review-log.md` | Reviewer / Main Agent | Repo-visible reviewer feedback and rework-routing handoff |
| Observer agent artifact | `agents/observer-dispatcher.agent.md` | Creator | Bounded Observer / Dispatcher contract |
| Dispatch policy skill | `skills/subagent-dispatch-policy/SKILL.md` | Creator | Role-selection policy for Observer dispatch |
| Dispatch policy examples | `skills/subagent-dispatch-policy/examples.md` | Creator | Positive and negative dispatch examples |
| Context packaging skill | `skills/context-package-builder/SKILL.md` | Creator | Minimal-context packaging rules for one handoff |
| Context packaging examples | `skills/context-package-builder/examples.md` | Creator | Positive and negative bounded-context examples |
| Routing policy skill | `skills/handoff-routing-policy/SKILL.md` | Creator | Result-routing rules after one subAgent response |
| Routing policy examples | `skills/handoff-routing-policy/examples.md` | Creator | Positive and negative routing examples |
| Governance source update | `AGENTS.md` | Creator | Repo governance update for root `agents/` plus projection-surface wording |
| Positioning doc update | `docs/repo-positioning.md` | Creator | Authority-model and boundary update for Feature 1 |
| Copilot compatibility guidance update | `.github/copilot-instructions.md` | Creator | Compatibility guidance aligned to the new canonical baseline |
| Human summary update | `README.md` | Creator | Human-facing summary of the bounded Feature 1 baseline |

Artifact path notes:

- This topic **does not** modify `VERSION`.
- `README.md` is updated only as a human-facing repository summary, not as
  stable-library publish metadata.
- The listed paths are an executable contract. Any need to edit additional
  files is a plan violation that must stop execution and return to planning.
- The review log is required because reviewer feedback controls routing and may
  trigger multi-round rework.
- Topic-local planning artifacts are planning / routing surfaces, not creator
  implementation write targets unless a later plan revision explicitly says so.
- No compatibility mirrors, registry files, workflow-binding files, or runtime
  semantics files are implied by this path list.

## Implementation Steps

1. **Update repo-truth wording**
   - Align `AGENTS.md`, `docs/repo-positioning.md`,
     `.github/copilot-instructions.md`, and `README.md` on the same authority
     model.
   - State that `skills/` remains primary, `agents/` is the canonical workflow
     agent source, and `.github/**` / `.codex/**` are projection /
     compatibility surfaces in repo policy.
   - State that the repository does not own runtime orchestration, agent
     loading / execution capability, install, sync, or deploy.

2. **Create the bounded Observer artifact**
   - Author `agents/observer-dispatcher.agent.md` with:
     - role identity
     - responsibility boundary
     - forbidden behavior
     - hard stop rule
     - real dispatch definition
     - fixed state and verdict values
     - role-only dispatch targets
     - concrete intake / status / handoff / result / final-report templates

3. **Create the three supporting skills**
   - Author `skills/subagent-dispatch-policy/SKILL.md` and `examples.md`
     strictly for choosing the next role or stop.
   - Author `skills/context-package-builder/SKILL.md` and `examples.md`
     strictly for bounded minimal-context packaging.
   - Author `skills/handoff-routing-policy/SKILL.md` and `examples.md`
     strictly for routing one subAgent result to the next role or stop.

4. **Preserve the workflow boundary**
   - Ensure the Observer baseline does not encode or restate full
     human-operated workflows.
   - Allow workflow-derived state only from topic-local step artifacts.
   - If any requested behavior requires workflow binding or runtime semantics,
     stop and surface the drift explicitly.

5. **Validate the bounded contract**
   - Check every changed path against the exact implementation artifact list in
     the technical baseline.
   - Confirm no concrete role-agent files, registry artifacts, compatibility
     mirrors, or runtime semantics were added.
   - Creator implementation stops if later work requires any planning-artifact
     mutation beyond the frozen execution contract.

## Validation / Acceptance Checks

- All changed implementation paths match the exact `Artifact Paths` contract for
  creator-owned implementation targets.
- `skills/` still reads as the primary canonical source in all four updated
  documentation surfaces.
- `agents/observer-dispatcher.agent.md` defines one bounded Observer role and no
  broader taxonomy.
- The Observer artifact contains:
  - the hard stop rule
  - the real-dispatch definition
  - the fixed Observer state values
  - the fixed subAgent verdict values
  - role-only dispatch targets
- Each supporting skill contains `SKILL.md` and `examples.md`.
- The three supporting skills do not overlap in responsibility.
- `.codex/**` is described only as a repo-policy projection / compatibility
  surface.
- No concrete agents, registry behavior, workflow binding, runtime semantics,
  or compatibility mirrors appear in the creator implementation write set.

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

- No repository release action is part of this topic.
- No `VERSION` update is allowed in this topic.
- If the topic later merges, post-merge cleanup or any later workflow resume
  remains outside Feature 1 planning and implementation scope.

## Open Questions / Unresolved Items

- No contract-level open question remains for Feature 1.
- Topic-branch / managed-worktree bootstrap is already satisfied by the managed
  worktree and feature branch created for this topic.
