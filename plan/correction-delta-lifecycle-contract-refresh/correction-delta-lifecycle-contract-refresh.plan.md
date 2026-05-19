> **Analysis-layer strict mode**
>
> Both `analysis/correction-delta-workflow-internalization/requirements.md` and
> `analysis/correction-delta-workflow-internalization/technical-spec.md` exist.
> This plan treats `technical-spec.md` as the execution-facing source of truth and
> `requirements.md` as the business guardrail. Chat-time guidance in this topic
> only narrows execution boundary and stop conditions; it does not override the
> analysis artifacts.

## Goal / Outcome

- Refresh the repository workflow contract for correction / delta handling without
  creating a new standalone Agent Skill.
- When this topic is complete, the repo should express a slim correction
  lifecycle / routing contract in workflow surfaces, move detailed correction
  artifact schema guidance into reference / examples, and keep the Python
  implementation workflow agent aligned as a consumer of the repo-level rule.

## Scope

- **In scope**:
  - Refresh `plan/agent-handoff-workflow.md` so the workflow body keeps only the
    correction lifecycle policy:
    - drift trigger
    - severity classification
    - routing state
    - required artifacts
    - parent-sync timing
    - historical retention
    - reviewer acceptance checks
  - Refresh `plan-creator` authoring surfaces so topic plans that use correction
    artifacts must list them explicitly, keep artifact paths exact and
    role-labeled, keep creator `Implementation Steps` creator-owned, and route
    detailed correction artifact schema guidance to references/examples instead
    of the workflow body.
  - Refresh `plan-reviewer` review surfaces so review catches workflow-breaking
    issues around vague evidence paths, missing parent-sync closure logic, mixed
    creator/reviewer ownership, workflow-body bloat, unconditional review-log
    requirements, and mistaken global round caps.
  - Refresh `.github/agents/python-implementation-workflow.agent.md` only as
    needed so its correction wording stays aligned with the repo-level contract
    and does not become the sole owner of the lifecycle rule.
  - Keep the future extraction boundary explicit: if correction artifact authoring
    quality remains unstable across repeated use, or multiple workflows need the
    same artifact-generation behavior, a future dedicated Agent Skill may be
    proposed later.

- **Out of scope**:
  - Creating a new standalone Agent Skill in this topic
  - Parser or tooling automation for correction artifacts
  - README / VERSION / release changes
  - `.github/prompts/create-analysis.prompt.md` or
    `.github/prompts/create-agent-plan.prompt.md` changes
  - Repository positioning or skill-path migration work
  - Implementation of any correction artifact in another repository

## Locked Decisions

- This is a non-stable topic. It has no stable-library surfaces, no README row
  change, no VERSION bump, and no release action.
- The future execution branch is
  `feat/andrew/correction-delta-lifecycle-contract-refresh`.
- The intended worktree path is
  `/Users/andrew/code/python/agent-skills.worktrees/agent-20260519-correction-delta-lifecycle-contract-refresh`.
- Base branch and PR target branch are both `dev`.
- Workflow body stays slim and carries lifecycle / routing contract only.
- Detailed `correction-plan` / `correction-step` schema, field explanation, and
  examples belong in reference / examples, not in the workflow body.
- `review-log` remains conditional: require repo-visible review-log or equivalent
  handoff only when feedback controls routing or multi-round rework.
- Round limits remain optional topic policy. This topic must not turn a
  three-round sample cap into a repository-wide universal default.
- Do not create a new standalone Agent Skill in this topic. Keep a future
  extraction boundary explicit instead.
- The current analysis artifacts under
  `analysis/correction-delta-workflow-internalization/` are source inputs for
  this topic and must remain mapped 100% to the implementation contract.

## Boundaries / Exclusions

- Planning actor owns this topic plan only; it does not approve, publish, or
  implement the topic.
- Creator owns later contract updates inside the exact paths listed below.
- Reviewer owns independent plan review and later implementation review; reviewer
  work must not be written into creator `Implementation Steps`.
- Main Agent owns worktree setup, review routing, commit / push / PR flow, and
  the stop after human check in the current run.
- If later implementation needs files outside the listed artifact paths, stop and
  repair this plan before continuing.
- Shared-file coordination warning: this topic touches repo workflow and planning
  surfaces (`plan/agent-handoff-workflow.md`, `.github/skills/plan-*`, and
  `.github/agents/python-implementation-workflow.agent.md`) that can affect other
  worktrees. Treat this topic as planner / governance work and avoid concurrent
  edits to the same files from another worktree.

## Status / Allowed Transitions

- **Current**: `planned`
- **Execution model**: follow the canonical creator -> reviewer -> publish ->
  merge path; this topic is non-stable and terminal at `merged`.
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

- This plan was authored in a worktree-backed planning run that stops for human
  check after plan review; later implementation resumes from `planned` only after
  explicit human approval.
- In the current planning run, reviewer <-> planner iteration is capped at three
  rounds. If round three still returns `needs-rework`, stop and hand off to human
  check instead of continuing the loop.
- Use the standard Phase 4.5 planner-alignment rule for later implementation
  execution after human approval.

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/correction-delta-lifecycle-contract-refresh/correction-delta-lifecycle-contract-refresh.plan.md` | Planning actor | Repo-visible execution contract for this topic |
| Analysis requirements input | `analysis/correction-delta-workflow-internalization/requirements.md` | Planning actor -> Creator -> Reviewer | Frozen business baseline and non-internalizable-boundary guardrail for this topic |
| Analysis technical spec input | `analysis/correction-delta-workflow-internalization/technical-spec.md` | Planning actor -> Creator -> Reviewer | Execution-facing analysis source of truth for this topic in strict mode |
| Repo workflow contract | `plan/agent-handoff-workflow.md` | Creator | Slim repo-level correction lifecycle / routing contract |
| Python workflow agent | `.github/agents/python-implementation-workflow.agent.md` | Creator | Python-specific consumer aligned with the repo-level correction lifecycle rule |
| Plan-creator overview | `.github/skills/plan-creator/reference.md` | Creator | Authoring guidance entry point that must point to the refreshed correction lifecycle expectations |
| Plan-creator checklist | `.github/skills/plan-creator/checklist.md` | Creator | Authoring checks for exact artifact paths, role boundaries, and correction-artifact handling |
| Plan-creator examples | `.github/skills/plan-creator/examples.md` | Creator | Positive / negative authoring examples showing lifecycle-vs-reference separation |
| Plan-creator artifact-path rule | `.github/skills/plan-creator/references/artifact-path-rule.md` | Creator | Detailed rule for exact, role-labeled correction-related artifact paths |
| Plan-creator role-boundary rule | `.github/skills/plan-creator/references/role-boundary-rule.md` | Creator | Detailed rule preventing reviewer-owned work from entering creator implementation steps |
| Topic-plan template | `.github/skills/plan-creator/templates/topic-plan-template.md` | Creator | Canonical plan template that must support slim workflow body and exact correction artifact listing when used |
| Plan-reviewer reference | `.github/skills/plan-reviewer/reference.md` | Creator | Review basis description aligned to the refreshed lifecycle contract |
| Plan-reviewer checklist | `.github/skills/plan-reviewer/checklist.md` | Creator | Review gate that must fail workflow-breaking ambiguity and mixed ownership |
| Plan-reviewer examples | `.github/skills/plan-reviewer/examples.md` | Creator | Review examples covering approval / needs-rework behavior for correction lifecycle contract topics |

Artifact path notes:

- `README.md`: no change in this topic.
- `VERSION`: no change in this topic.
- `.github/copilot-instructions.md`: no change in this topic.
- Treat the listed paths as an executable contract. If later work drifts into
  prompts, stable-library files, parser/tooling code, or unrelated skill folders,
  stop and repair the plan first.

## Implementation Steps

1. Refresh `plan/agent-handoff-workflow.md` so the correction section states only
   the slim lifecycle / routing contract and leaves detailed artifact schema
   guidance out of the workflow body.
2. Refresh `plan-creator` surfaces:
   - `.github/skills/plan-creator/reference.md`
   - `.github/skills/plan-creator/checklist.md`
   - `.github/skills/plan-creator/examples.md`
   - `.github/skills/plan-creator/references/artifact-path-rule.md`
   - `.github/skills/plan-creator/references/role-boundary-rule.md`
   - `.github/skills/plan-creator/templates/topic-plan-template.md`
   so authoring guidance:
   - lists correction artifacts exactly when a topic uses them
   - keeps creator implementation steps creator-owned
   - keeps workflow-body lifecycle policy separate from reference/example-level
     schema details
   - preserves the future extraction boundary instead of adding a new skill now
3. Refresh `plan-reviewer` surfaces:
   - `.github/skills/plan-reviewer/reference.md`
   - `.github/skills/plan-reviewer/checklist.md`
   - `.github/skills/plan-reviewer/examples.md`
   so review guidance rejects:
   - vague correction evidence paths
   - reviewer-owned work inside creator implementation steps
   - missing parent-sync closure requirements
   - unconditional review-log requirements
   - universalized round-cap rules
   - workflow-body bloat caused by detailed artifact schema text
4. Refresh `.github/agents/python-implementation-workflow.agent.md` only as
   needed so its correction lifecycle language stays aligned with the repo
   workflow contract and the workflow/reference/future-skill boundary.

## Validation / Acceptance Checks

- `plan/agent-handoff-workflow.md` expresses correction lifecycle policy without
  embedding detailed `correction-plan` / `correction-step` schema text.
- `plan-creator` guidance requires exact, bounded, role-labeled artifact paths
  when correction artifacts are used.
- `plan-creator` guidance keeps reviewer-owned work out of creator
  `Implementation Steps`.
- `plan-creator` and `plan-reviewer` examples clearly show:
  - workflow body = lifecycle / routing contract
  - reference/examples = artifact schema and usage examples
  - future skill = optional extraction only if repeated quality problems justify it
- `plan-reviewer` checks can fail plans that use vague evidence paths such as
  `merged implementation`.
- `plan-reviewer` checks can fail plans that require review-log unconditionally
  when routing control or multi-round feedback is absent.
- `plan-reviewer` checks can fail plans that generalize a three-round sample cap
  into a global invariant.
- `.github/agents/python-implementation-workflow.agent.md` remains aligned with
  repo workflow wording and does not become the sole owner of the correction
  lifecycle contract.
- No stable-library file, release surface, prompt file, or standalone Agent Skill
  is introduced by this topic.

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

- After merge, Main Agent may handle the normal local sync flow only after an
  explicit human resume message.
- No repository release action belongs to this topic.
- This topic is terminal at `merged`.

## Open Questions / Unresolved Items

- None.
