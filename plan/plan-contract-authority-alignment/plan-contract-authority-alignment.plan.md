**Analysis-layer routing**: Strict mode. `analysis/plan-contract-authority-alignment/technical-spec.md` is the execution-facing source of truth for this topic plan, `analysis/plan-contract-authority-alignment/requirements.md` is the business-intent guardrail, and `analysis/plan-contract-authority-alignment/upstream-decision-basis.md` is the exact upstream evidence manifest. No chat-time convenience instruction may override these artifacts without an explicit human `override`.

# plan-contract-authority-alignment

## Goal / Outcome

Produce a bounded repo-visible governance topic that establishes the shared
repo-level plan-contract authority baseline before any canonical convergence
work begins.

When this topic is complete:

- `plan/topic-plan-contract.md` exists as the shared repo-level authority
  surface for topic-plan contract rules
- `plan/agent-handoff-workflow.md` explicitly states how repo-level workflow
  semantics and repo-level topic-plan contract authority relate to each other
- source-of-truth ordering for planning governance is explicit
- the shared contract exposes a human-facing `contract_version`
- accepted Phase 1 conclusions are preserved as planning inputs without being
  reinterpreted as implementation approval

## Scope

- **In scope**:
  - read and validate frozen
    `analysis/plan-contract-authority-alignment/upstream-decision-basis.md`
  - read and validate frozen
    `analysis/plan-contract-authority-alignment/requirements.md`
  - read and validate frozen
    `analysis/plan-contract-authority-alignment/technical-spec.md`
  - create `plan/plan-contract-authority-alignment/plan-contract-authority-alignment.plan.md`
  - create `plan/plan-contract-authority-alignment/plan-contract-authority-alignment.step.md`
  - create `plan/plan-contract-authority-alignment/plan-contract-authority-alignment.review-log.md`
  - create `plan/plan-contract-authority-alignment/plan-contract-authority-alignment.summary.md`
  - create `plan/topic-plan-contract.md`
  - update `plan/agent-handoff-workflow.md` only as required to reference the
    shared contract and clarify authority layering

- **Out of scope**:
  - editing `skills/**`
  - editing `.github/skills/**`
  - editing `.codex/skills/**`
  - editing `.github/agents/**`
  - editing `.codex/agents/**`
  - canonical convergence implementation
  - projection materialization
  - runtime adaptation work
  - absorbing `python-blueprint-review` into `skills/`
  - generic convergence for `copilot-instructions-init`
  - editing `README.md`
  - editing `VERSION`
  - editing `.github/copilot-instructions.md`

## Locked Decisions

### 1. Topic type is governance-only

- This topic is governance / contract alignment only.
- It must not be framed as Phase 2 implementation.
- It must not widen into convergence, projection, or runtime work.

### 2. Analysis-layer priority is fixed

- `analysis/plan-contract-authority-alignment/requirements.md`
  - SHA-256: `0962f43fe17accbf6647461c72e2507f50b36de87dc612083dbe6a027eb61a81`
- `analysis/plan-contract-authority-alignment/technical-spec.md`
  - SHA-256: `7f61cbdb05e2fb1dcc9158e14f0b88e22a4d7d6b2f2c5ccbe70cf23215994438`
- `analysis/plan-contract-authority-alignment/upstream-decision-basis.md`
  - SHA-256: `f3d3b9f07d989fba3e80291f5c3b49c08d250d624d66eb378444670da3504ce6`

These artifacts outrank chat-time convenience instructions unless a human
explicitly says `override`.

For this execution stage, they are frozen read-only prerequisites:

- execution may read, validate, and compare them
- execution may not reopen, regenerate, or silently revise them
- if any of them is missing, contradictory, or insufficient for bounded
  execution, stop and route to `human_review_required` / plan repair instead of
  improvising

### 3. Authority ordering is fixed

The future topic must preserve this authority order:

1. `AGENTS.md` — repo governance canonical source
2. `plan/agent-handoff-workflow.md` — repo-level workflow-phase contract
3. `plan/topic-plan-contract.md` — shared repo-level topic-plan contract
4. `plan/<topic>/<topic>.plan.md` — topic-specific execution contract
5. `skills/plan-creator/**` and `skills/plan-reviewer/**` — consumer guidance
   and bounded evidence surfaces, not authority owners

### 4. Shared contract versioning is fixed

- The shared plan contract must expose a human-facing `contract_version`.
- `contract_hash` may be added later for strict verification, but it is not the
  primary contract language in this topic.
- Contract versioning must remain repo-local and must not move to `~/.` or any
  cross-repo storage.

### 5. Read-only planning skill surfaces are fixed

- `skills/plan-creator/**` is read-only evidence in this topic.
- `skills/plan-reviewer/**` is read-only evidence in this topic.
- If honest authority alignment would require editing either skill surface,
  stop and repair the plan rather than widening by assumption.

### 6. Accepted downstream effects remain deferred

- `python-blueprint-review` remains a later canonical convergence topic.
- `copilot-instructions-init` remains `copilot_only` and `platform_native`.
- `.codex/skills/` remains a partial projection surface only.
- None of those outcomes are implemented here.

### 7. Stable-library and release intent are absent

- This topic is not a stable-library publish topic.
- `README.md` stays unchanged.
- `VERSION` stays unchanged.
- No release, tag, or release-note work belongs to this topic.

## Boundaries / Exclusions

- Do not edit `skills/plan-creator/**` or `skills/plan-reviewer/**` just to
  make the new repo-level contract true by implication.
- Do not reinterpret accepted Phase 1 planning inputs as direct permission for
  convergence implementation.
- Do not create `.codex/skills/<skill-name>/` or `.codex/agents/**`.
- Do not widen this topic into `python-blueprint-review` absorption work.
- Do not widen this topic into platform adapter design for
  `copilot-instructions-init`.
- If later work drifts outside `Artifact Paths`, stop and repair the plan
  before execution continues.

## Status / Allowed Transitions

- **Current**: `planned`
- **Execution model**: follow the canonical creator -> reviewer -> publish ->
  merge path, with no release action
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
- Any attempt to turn accepted Phase 1 planning inputs into direct
  implementation instructions is plan drift.
- Any attempt to widen into skill migration, projection materialization, or
  runtime adaptation is plan drift.

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/plan-contract-authority-alignment/plan-contract-authority-alignment.plan.md` | Planning actor | Repo-visible execution contract for this topic |
| Topic progression artifact | `plan/plan-contract-authority-alignment/plan-contract-authority-alignment.step.md` | Planning actor | Current-truth workflow progression status for this topic |
| Review routing log | `plan/plan-contract-authority-alignment/plan-contract-authority-alignment.review-log.md` | Reviewer / Planning actor | Repo-visible routing log for reviewer findings and re-review outcomes |
| Topic close summary artifact | `plan/plan-contract-authority-alignment/plan-contract-authority-alignment.summary.md` | Planning actor | Current-truth close outcome and handoff semantics for this topic |
| Upstream evidence manifest | `analysis/plan-contract-authority-alignment/upstream-decision-basis.md` | Planning actor | Exact accepted Phase 1 evidence and human decision paths for this topic |
| Requirements baseline | `analysis/plan-contract-authority-alignment/requirements.md` | Planning actor | Frozen business baseline for authority ownership and scope boundaries |
| Technical baseline | `analysis/plan-contract-authority-alignment/technical-spec.md` | Planning actor | Frozen technical translation for shared contract path, authority order, and bounded writable scope |
| Shared topic-plan contract | `plan/topic-plan-contract.md` | Creator | Repo-level shared contract for topic-plan authority, required sections, reviewer handoff rules, and `contract_version` |
| Repo workflow contract | `plan/agent-handoff-workflow.md` | Creator | Repo-level workflow-phase contract updated only to align with the shared topic-plan contract |
| Governance canonical source | `AGENTS.md` | Existing repo artifact | Read-only governance authority source for this topic |
| Positioning contract | `docs/repo-positioning.md` | Existing repo artifact | Read-only positioning evidence confirming canonical and projection roles |
| Planning skill evidence | `skills/plan-creator/SKILL.md` | Existing repo artifact | Read-only evidence for current plan-authoring authority expectations |
| Planning skill evidence | `skills/plan-creator/reference.md` | Existing repo artifact | Read-only evidence for current plan-authoring review basis and fallback wording |
| Planning skill evidence | `skills/plan-creator/checklist.md` | Existing repo artifact | Read-only evidence for current plan-authoring contract checks |
| Planning skill evidence | `skills/plan-creator/templates/topic-plan-template.md` | Existing repo artifact | Read-only evidence for the current topic-plan template contract surface |
| Planning skill evidence | `skills/plan-reviewer/SKILL.md` | Existing repo artifact | Read-only evidence for current plan-review routing and review-basis expectations |
| Planning skill evidence | `skills/plan-reviewer/reference.md` | Existing repo artifact | Read-only evidence for current cross-skill review-basis dependency wording |
| Planning skill evidence | `skills/plan-reviewer/checklist.md` | Existing repo artifact | Read-only evidence for current reviewer contract checks |

Artifact path notes:

- This topic does **not** modify `README.md`.
- This topic does **not** modify `VERSION`.
- This topic does **not** modify `.github/copilot-instructions.md`.
- The analysis artifacts listed above are frozen read-only prerequisites at
  this execution stage, not writable outputs.
- The listed `skills/plan-creator/*` and `skills/plan-reviewer/*` paths are
  read-only evidence only and are not writable scope.
- This topic does **not** modify `skills/**`, `.github/skills/**`,
  `.codex/skills/**`, `.github/agents/**`, or `.codex/agents/**`.
- If later work requires editing any path outside this table, stop and repair
  the plan instead of staging extra files.

## Implementation Steps

1. Read the frozen analysis artifacts and upstream evidence manifest before
   changing any repo-level planning contract file.
2. Stop and route to `human_review_required` / plan repair if the frozen
   analysis prerequisites are missing, contradictory, or insufficient for
   bounded execution.
3. Create `plan/topic-plan-contract.md` so it defines:
   - repo-level topic-plan required sections
   - source-of-truth ordering for topic-plan contract authority
   - reviewer handoff contract expectations at repo level
   - human-facing `contract_version`
   - clear statement that skill-local planning guidance is consumer guidance,
     not the authority owner
4. Update `plan/agent-handoff-workflow.md` only as needed to:
   - reference `plan/topic-plan-contract.md`
   - distinguish workflow-phase semantics from topic-plan contract semantics
   - remove ambiguity that would otherwise leave `plan-creator` or
     `plan-reviewer` as implicit owners of repo-level planning contract
5. Record explicit deferred follow-up boundaries for:
   - `python-blueprint-review` absorption into `skills/`
   - later canonical convergence topics
   - later projection and runtime topics
   - platform-specific handling for `copilot-instructions-init`
6. Stop and route back to plan repair if execution would require:
   - editing `skills/plan-creator/**`
   - editing `skills/plan-reviewer/**`
   - editing any skill or agent path
   - implementing convergence, projection, or runtime adaptation

## Validation / Acceptance Checks

- `plan/topic-plan-contract.md` exists and is named as the shared repo-level
  topic-plan contract authority surface
- `plan/agent-handoff-workflow.md` and `plan/topic-plan-contract.md` have
  non-overlapping, explicit authority roles
- the authority order among governance, workflow, shared plan contract, topic
  plans, and skill-local guidance is explicit
- `contract_version` is present as a human-facing contract field
- accepted Phase 1 evidence paths are preserved through
  `analysis/plan-contract-authority-alignment/upstream-decision-basis.md`
- analysis artifacts remain frozen read-only prerequisites for this execution
  stage
- no path outside `Artifact Paths` is modified
- no accepted Phase 1 planning input is treated as approved implementation spec
- no convergence, projection, runtime, or skill-move work appears in current
  writable scope
- any execution-meaning conflict among `plan.md`, `step.md`, `review-log.md`,
  and `summary.md` is surfaced instead of silently resolved
- reviewer handoff remains one JSON object

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

- Run normal post-merge local sync if the topic is merged.
- No repository release action is required.
- No VERSION bump or tag creation is allowed in this topic.

## Open Questions / Unresolved Items

- Whether a later bounded topic should update `skills/plan-creator/**` and
  `skills/plan-reviewer/**` to consume the shared repo-level contract after the
  authority baseline lands.
- Whether future strict verification should add `contract_hash` in addition to
  `contract_version`.
