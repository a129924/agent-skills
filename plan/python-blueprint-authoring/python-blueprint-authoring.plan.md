# python-blueprint-authoring topic plan

## Goal / Outcome

Create a repo-visible execution plan for a new stable skill at
`.github/skills/python-blueprint-authoring/` that authors review-ready
greenfield `blueprint.md` contracts for new or baseline-only Python
repositories.

When complete, this topic should produce:

- a new stable skill that turns greenfield intent into a review-ready
  `blueprint.md`
- a contract-writing lane that matches the existing
  `python-project-init-greenfield` executor instead of leaving blueprint quality
  to ad hoc human drafting
- explicit stop-and-ask behavior for abstract structure, missing locatability,
  missing required skills, and lane mismatch

**Semantic warning**: `analysis/python-blueprint-authoring/requirements.md` and
`analysis/python-blueprint-authoring/technical-spec.md` do not exist at plan
time, so this topic plan is authored without the optional analysis layer.

## Scope

- **In scope**:
  - create `.github/skills/python-blueprint-authoring/SKILL.md`
  - create `.github/skills/python-blueprint-authoring/examples.md`
  - create `.github/skills/python-blueprint-authoring/checklist.md`
  - create `.github/skills/python-blueprint-authoring/references/blueprint-contract.md`
  - create `.github/skills/python-blueprint-authoring/references/required-skills-validation.md`
  - create `.github/skills/python-blueprint-authoring/references/greenfield-lane-boundaries.md`
  - create `.github/skills/python-blueprint-authoring/references/structural-invariants-locatability.md`
  - add a stable-library row for `python-blueprint-authoring` to `README.md`
  - bump `VERSION` for the new stable skill topic
  - declare post-merge tag creation for the repository release tied to this topic

- **Out of scope**:
  - modifying `.github/skills/python-project-init-greenfield/` unless plan repair
    is approved first
  - modifying the locked blueprint schema consumed by the existing executor
  - creating a dedicated `python-blueprint-review` skill
  - creating a `python-project-lane-router` or other meta-routing skill
  - implementing or modifying `sense_env.py`
  - generating `.github/copilot-instructions.md`

## Locked Decisions

- This topic is a **stable-library-affecting topic** with declared publish and
  release timing.
- The topic adds one new upstream authoring skill:
  `.github/skills/python-blueprint-authoring/`.
- This topic is intentionally asymmetric with retrofit:
  - greenfield authoring belongs to `python-blueprint-authoring`
  - greenfield execution remains in `python-project-init-greenfield`
  - existing-project authoring remains in `python-retrofit-plan-authoring`
  - existing-project execution remains in `python-project-retrofit`
- `python-blueprint-authoring` must author the blueprint contract already
  consumed by `python-project-init-greenfield`; it must not invent a new schema.
- The locked blueprint section order is:
  1. `## Project Overview`
  2. `## Required Skills`
  3. `## Toolchain Expectation`
  4. `## Structural Invariants`
  5. `## Quality Thresholds`
  6. `## Acceptance Criteria`
- `## Acceptance Criteria` must contain a fenced
  ````yaml [sensing-assertions]```` block immediately under the heading.
- Each assertion record must include at least:
  - `kind`
  - `target`
  - `expected`
- `Required Skills` validation is mandatory at authoring time:
  - skill names must match exact directory names in the current library
  - if a required skill is absent from the library, authoring must stop and ask
    instead of guessing, normalizing, or deferring the error downstream
- `Structural Invariants` must stay locatable:
  - paths, entrypoints, packages, and tool choices must be concrete enough for
    the greenfield executor to consume without reinterpretation
  - abstract inputs such as "modern layout" or "good defaults" are authoring
    stop-and-ask conditions
- Lane mismatch is an authoring stop-and-ask condition:
  - if the request is not truly greenfield or baseline-only, route away from
    blueprint authoring instead of forcing retrofit work into a blueprint
- This topic does **not** widen the scope to executor changes by default.
  If creator work discovers a real contract mismatch that would require touching
  `.github/skills/python-project-init-greenfield/`, stop and repair the topic
  plan before continuing execution.
- Stable-library timing is locked to `publish-in-progress`, meaning:
  - `README.md` and `VERSION` update during publish
  - annotated tag creation happens only after merge and explicit post-merge
    human resume
- The repository version baseline at plan time is `0.30.0`; this topic's
  release target is the next MINOR version `0.31.0`.

## Boundaries / Exclusions

- `python-blueprint-authoring`
  - owns authoring of review-ready greenfield `blueprint.md`
  - does not execute greenfield initialization
  - does not approve its own authored contract
  - does not absorb retrofit planning or runtime routing

- `python-project-init-greenfield`
  - continues to own blueprint consumption, baseline scaffolding, required skill
    copying, provenance writing, and acceptance handoff
  - does not become part of this topic's change set unless planner repair is
    explicitly approved

- `sense-env-scaffold`
  - continues to own acceptance assertion execution
  - this topic must not broaden its assertion-kind set

- `copilot-instructions-init`
  - continues to own generated `.github/copilot-instructions.md`
  - this topic must not absorb instructions generation

- Future `python-blueprint-review`
  - may later own dedicated review of authored blueprints
  - this topic must not backfill reviewer responsibility into the authoring
    skill itself

## Status / Allowed Transitions

- **Current**: `pr-open`
- **Execution model**: follow the canonical creator -> reviewer -> publish ->
  merge -> release path for a stable-library-affecting topic
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
  - `merged` -> `released`
  - `released` -> terminal

Routing notes:

- Follow the standard Phase 4.5 planner-alignment rule from
  `plan/agent-handoff-workflow.md`.
- STOP POINT 1 applies before commit / push / PR creation.
- STOP POINT 2 applies after merge handoff; post-merge tag work resumes only
  after a new explicit human message.
- Reviewer should assess whether the new authoring skill stays aligned to the
  existing greenfield executor contract without silently widening scope into
  executor changes.

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/python-blueprint-authoring/python-blueprint-authoring.plan.md` | Planning actor | Repo-visible execution contract for this topic |
| Authoring skill contract | `.github/skills/python-blueprint-authoring/SKILL.md` | Creator | Executable contract for drafting review-ready greenfield `blueprint.md` |
| Authoring examples | `.github/skills/python-blueprint-authoring/examples.md` | Creator | Layered examples for correct blueprints, stop-and-ask cases, and lane mismatch |
| Authoring checklist | `.github/skills/python-blueprint-authoring/checklist.md` | Creator | Higher-risk authoring validation checklist for blueprint contract quality |
| Authoring reference: blueprint contract | `.github/skills/python-blueprint-authoring/references/blueprint-contract.md` | Creator | Locked section order, assertion-block placement, and parser-facing contract rules |
| Authoring reference: required skills validation | `.github/skills/python-blueprint-authoring/references/required-skills-validation.md` | Creator | Exact-name library validation rules, missing-skill stops, and optional-item handling |
| Authoring reference: lane boundaries | `.github/skills/python-blueprint-authoring/references/greenfield-lane-boundaries.md` | Creator | Greenfield-only fit rules and rerouting boundaries versus retrofit |
| Authoring reference: locatability | `.github/skills/python-blueprint-authoring/references/structural-invariants-locatability.md` | Creator | Concrete path, entrypoint, package, and tool-choice requirements for `Structural Invariants` |
| Stable library row | `README.md` | Main Agent | Add the stable-skill table row for `python-blueprint-authoring` at publish time |
| Repo version baseline | `VERSION` | Main Agent | Apply the `0.30.0` -> `0.31.0` MINOR bump when the topic is published |

Artifact path notes:

- This topic modifies `README.md` and `VERSION`.
- This topic does not modify `.github/copilot-instructions.md`.
- This topic does not modify `.github/skills/python-project-init-greenfield/`
  unless the topic plan is explicitly repaired first.
- Treat the listed paths as an executable contract; if later work drifts outside
  them, stop and repair the topic plan before continuing execution.

## Stable library metadata

- `README row`: insert this exact table row immediately after
  `| \`python-project-init-greenfield\` | executes Greenfield project initialization from blueprint contracts, including required skill installation, toolchain configuration, structural scaffolding, and acceptance handoff |`
  and before
  `| \`python-project-retrofit\` | retrofits existing Python projects with safe structural conflict detection (Shadow File Detection), implicit configuration discovery (Implicit Config Mining), Git safety checks, and Sensing Delta Report for transparent state transformation |`:
  `| \`python-blueprint-authoring\` | authors review-ready greenfield \`blueprint.md\` contracts with locked section order, exact Required Skills library validation, stop-and-ask handling for abstract structure, and strict greenfield-only lane boundaries |`
- `VERSION bump`: `0.30.0` -> `0.31.0`
- `timing`: `publish-in-progress`
- `rationale`: this topic adds a new stable upstream authoring skill for the
  greenfield lane, so the stable skill table and repository version baseline
  must move together when the approved draft is published
- `release notes`: no separate release-notes artifact is planned; the annotated
  git tag message is the release-facing metadata for this topic

## Implementation Steps

1. **Branch preparation** (via Main Agent):
   - create or repair the semantic execution branch for
     `python-blueprint-authoring`
   - verify worktree readiness before creator work begins
   - do not begin drafting from chat-only planning once this repo-visible plan
     exists

2. **Draft phase: new authoring skill** (via `agent-skill-creator`):
   - create `.github/skills/python-blueprint-authoring/SKILL.md` with:
     - explicit trigger: when to author a greenfield blueprint rather than
       execute one
     - locked blueprint section order and acceptance-block requirements
     - mandatory exact-name `Required Skills` validation against the library
     - stop-and-ask behavior for abstract, contradictory, or misrouted requests
     - concise positive and negative examples
   - create `.github/skills/python-blueprint-authoring/examples.md` with
     branching scenarios for:
     - valid greenfield blueprint authoring
     - missing required skill in the library
     - abstract `Structural Invariants` that must stop and ask
     - lane mismatch where the request is really retrofit
   - create focused reference files for blueprint contract, required-skills
     validation, greenfield-lane boundaries, and structural-invariant
     locatability
   - create `checklist.md` tuned to this higher-risk contract-authoring skill

3. **Review phase** (via independent `agent-skill-reviewer`):
   - verify the new authoring skill is single-purpose and review-ready
   - verify the authored contract mirrors the existing greenfield executor
     schema instead of inventing a competing blueprint shape
   - verify required-skills validation, lane mismatch handling, and locatability
     rules are explicit and misuse-resistant
   - verify the skill stays in authoring scope and does not absorb execution or
     reviewer responsibilities
   - return `approved` or `needs-rework`

4. **Publish phase** (if `approved`):
   - commit the new authoring skill
   - update `README.md` with the stable-skill row at publish time
   - update `VERSION` from `0.30.0` to `0.31.0`
   - open PR after STOP POINT 1 approval
   - after merge and explicit human resume, create annotated tag `v0.31.0` and
     push it
   - update topic status to `released`

## Validation / Acceptance Checks

- confirm all required topic-plan sections are present and canonical
- confirm missing analysis artifacts are called out explicitly instead of being
  ignored silently
- confirm artifact paths are exact, bounded, and limited to the new skill plus
  stable-library publish surfaces
- confirm the blueprint section order matches the existing greenfield executor
  contract exactly
- confirm `yaml [sensing-assertions]` placement and minimum assertion keys are
  documented as locked contract requirements
- confirm `Required Skills` validation uses exact library names and blocks
  missing skills at authoring time
- confirm abstract or non-locatable `Structural Invariants` trigger
  authoring-time stop-and-ask instead of vague drafting
- confirm lane mismatch with non-greenfield repositories is explicit and
  reroutes instead of being absorbed
- confirm the topic does not silently widen into
  `.github/skills/python-project-init-greenfield/`
- confirm stable-library metadata is complete and matches the current repo
  version baseline `0.30.0`
- confirm reviewer handoff stays a single machine-consumable JSON object

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

- After merge, STOP POINT 2 applies until an explicit human resume message
  confirms merge completion and asks to continue.
- On valid post-merge resume, Main Agent performs release handling:
  - synchronize local branch state
  - confirm `README.md` includes the new stable-skill row
  - confirm `VERSION` equals `0.31.0`
  - create and push annotated tag `v0.31.0`
- When those release actions complete, transition the topic from `merged` to
  `released`.

## Open Questions / Unresolved Items

- None. This topic's blocking planning decisions are locked:
  - greenfield-only authoring lane
  - existing blueprint v1 contract reuse
  - exact-name `Required Skills` validation
  - authoring stop-and-ask for abstract structure
  - no default widening into executor changes
