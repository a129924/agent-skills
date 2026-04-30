# python-blueprint-review topic plan

## Goal / Outcome

Create a repo-visible execution plan for a new stable skill at
`.github/skills/python-blueprint-review/` that reviews authored greenfield
`blueprint.md` contracts before they are handed to
`python-project-init-greenfield`.

When complete, this topic should produce:

- a new stable skill that reviews blueprint contracts themselves rather than
  skill folders or topic plans
- a domain-specific quality gate between `python-blueprint-authoring` and
  `python-project-init-greenfield`
- repeatable `approved|needs-rework` review outcomes for blueprint-specific
  contract defects

**Semantic warning**: `analysis/python-blueprint-review/requirements.md` and
`analysis/python-blueprint-review/technical-spec.md` do not exist at plan time,
so this topic plan is authored without the optional analysis layer.

## Scope

- **In scope**:
  - create `.github/skills/python-blueprint-review/SKILL.md`
  - create `.github/skills/python-blueprint-review/examples.md`
  - create `.github/skills/python-blueprint-review/checklist.md`
  - create `.github/skills/python-blueprint-review/references/blueprint-v1-review-checks.md`
  - create `.github/skills/python-blueprint-review/references/review-verdict-contract.md`
  - create `.github/skills/python-blueprint-review/references/greenfield-fit-and-reroute.md`
  - create `.github/skills/python-blueprint-review/references/required-skills-and-locatability-checks.md`
  - add a stable-library row for `python-blueprint-review` to `README.md`
  - bump `VERSION` for the new stable skill topic
  - declare post-merge tag creation for the repository release tied to this topic

- **Out of scope**:
  - modifying `.github/skills/python-blueprint-authoring/` unless plan repair is
    approved first
  - modifying `.github/skills/python-project-init-greenfield/` unless plan repair
    is approved first
  - modifying the locked blueprint v1 schema
  - creating `python-retrofit-plan-review`
  - creating `python-project-lane-router` or `python-project-shape-assessment`
  - implementing or modifying `sense_env.py`
  - generating `.github/copilot-instructions.md`

## Locked Decisions

- This topic is a **stable-library-affecting topic** with declared publish and
  release timing.
- The topic adds one new domain-specific reviewer skill:
  `.github/skills/python-blueprint-review/`.
- `python-blueprint-review` reviews authored `blueprint.md` contracts; it does
  **not** review skill folders, repo-visible topic plans, or implementation
  diffs.
- The skill must reuse the existing blueprint v1 contract already consumed by
  `python-project-init-greenfield`; it must not invent a new schema.
- The locked blueprint section order remains:
  1. `## Project Overview`
  2. `## Required Skills`
  3. `## Toolchain Expectation`
  4. `## Structural Invariants`
  5. `## Quality Thresholds`
  6. `## Acceptance Criteria`
- `## Acceptance Criteria` must still contain a fenced
  ````yaml [sensing-assertions]```` block immediately under the heading.
- Each assertion record must include at least:
  - `kind`
  - `target`
  - `expected`
- The reviewer must explicitly check:
  - section order and presence
  - `yaml [sensing-assertions]` placement and parseability
  - exact-name `Required Skills` validity against the current library
  - concrete, locatable `Structural Invariants`
  - greenfield-vs-retrofit lane fit
- The skill's review outcome is locked to a machine-consumable verdict concept:
  - `approved`
  - `needs-rework`
  - plus concrete blocking issues when it fails
- The skill must not widen into authoring or execution:
  - it does not draft the blueprint
  - it does not execute the blueprint
  - it does not replace `agent-skill-reviewer` for skill-folder review
- This topic does **not** widen scope into
  `.github/skills/python-blueprint-authoring/` or
  `.github/skills/python-project-init-greenfield/` by default.
  If creator work discovers a true contract mismatch that would require touching
  either skill, stop and repair the topic plan before continuing execution.
- Stable-library timing is locked to `publish-in-progress`, meaning:
  - `README.md` and `VERSION` update during publish
  - annotated tag creation happens only after merge and explicit post-merge
    human resume
- The repository version baseline at plan time is `0.32.0`; this topic's
  release target is the next MINOR version `0.33.0`.

## Boundaries / Exclusions

- `python-blueprint-review`
  - owns review of drafted greenfield `blueprint.md` contracts
  - returns a contract-quality verdict and concrete blocking issues
  - does not author the blueprint
  - does not execute greenfield initialization

- `python-blueprint-authoring`
  - continues to own upstream blueprint drafting and repair
  - does not absorb reviewer responsibility into authoring

- `python-project-init-greenfield`
  - continues to own blueprint consumption, scaffolding, provenance, and
    acceptance handoff
  - does not become part of this topic's change set unless planner repair is
    explicitly approved

- `agent-skill-reviewer`
  - continues to review skill folders for repository compliance
  - this topic must not redefine it into a blueprint-contract reviewer

- `sense-env-scaffold`
  - continues to own acceptance assertion execution
  - this topic must not broaden its assertion-kind set

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
- Reviewer should assess whether the new skill stays strictly in blueprint
  review scope and does not silently widen into authoring, execution, or
  generic skill-folder review.

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/python-blueprint-review/python-blueprint-review.plan.md` | Planning actor | Repo-visible execution contract for this topic |
| Reviewer skill contract | `.github/skills/python-blueprint-review/SKILL.md` | Creator | Executable contract for reviewing authored greenfield `blueprint.md` files |
| Reviewer examples | `.github/skills/python-blueprint-review/examples.md` | Creator | Layered examples for valid blueprints, blocked blueprints, and lane-mismatch review outcomes |
| Reviewer checklist | `.github/skills/python-blueprint-review/checklist.md` | Creator | Higher-risk review checklist for blueprint contract safety and misuse prevention |
| Review reference: blueprint v1 checks | `.github/skills/python-blueprint-review/references/blueprint-v1-review-checks.md` | Creator | Locked section-order, assertion-block, and schema-alignment checks |
| Review reference: verdict contract | `.github/skills/python-blueprint-review/references/review-verdict-contract.md` | Creator | Expected verdict shape, blocking-issue expectations, and review-output boundaries |
| Review reference: lane boundaries | `.github/skills/python-blueprint-review/references/greenfield-fit-and-reroute.md` | Creator | How to detect greenfield fit and reroute retrofit-looking requests |
| Review reference: skill and locatability checks | `.github/skills/python-blueprint-review/references/required-skills-and-locatability-checks.md` | Creator | Exact-name required-skills validation and structural-locatability review rules |
| Stable library row | `README.md` | Main Agent | Add the stable-skill table row for `python-blueprint-review` at publish time |
| Repo version baseline | `VERSION` | Main Agent | Apply the `0.32.0` -> `0.33.0` MINOR bump when the topic is published |

Artifact path notes:

- This topic modifies `README.md` and `VERSION`.
- This topic does not modify `.github/copilot-instructions.md`.
- This topic does not modify `.github/skills/python-blueprint-authoring/` or
  `.github/skills/python-project-init-greenfield/` unless the topic plan is
  explicitly repaired first.
- Treat the listed paths as an executable contract; if later work drifts
  outside them, stop and repair the topic plan before continuing execution.

## Stable library metadata

- `README row`: insert this exact table row immediately after
  `| \`python-blueprint-authoring\` | authors review-ready greenfield \`blueprint.md\` contracts with locked section order, exact Required Skills library validation, stop-and-ask handling for abstract structure, and strict greenfield-only lane boundaries |`
  and before
  `| \`python-project-retrofit\` | retrofits existing Python projects with safe structural conflict detection (Shadow File Detection), implicit configuration discovery (Implicit Config Mining), Git safety checks, and Sensing Delta Report for transparent state transformation |`:
  `| \`python-blueprint-review\` | reviews authored greenfield \`blueprint.md\` contracts against the locked blueprint v1 schema, exact Required Skills validity, structural locatability, and greenfield-only lane fit before executor handoff |`
- `VERSION bump`: `0.32.0` -> `0.33.0`
- `timing`: `publish-in-progress`
- `rationale`: this topic adds a new stable domain-specific review skill for the
  greenfield lane, so the stable skill table and repository version baseline
  must move together when the approved draft is published
- `release notes`: no separate release-notes artifact is planned; the annotated
  git tag message is the release-facing metadata for this topic

## Implementation Steps

1. **Branch preparation** (via Main Agent):
   - create or repair the semantic execution branch for
     `python-blueprint-review`
   - verify worktree readiness before creator work begins
   - do not begin drafting from chat-only planning once this repo-visible plan
     exists

2. **Draft phase: new review skill** (via `agent-skill-creator`):
   - create `.github/skills/python-blueprint-review/SKILL.md` with:
     - explicit trigger: review a drafted greenfield blueprint before execution
     - locked blueprint v1 schema checks
     - exact-name `Required Skills` review behavior
     - structural-locatability and lane-mismatch review behavior
     - concise positive and negative examples
   - create `.github/skills/python-blueprint-review/examples.md` with branching
     scenarios for:
     - valid blueprint approved
     - wrong section order
     - missing or malformed `yaml [sensing-assertions]`
     - missing library skill or abstract `Structural Invariants`
     - lane mismatch that should reroute to retrofit
   - create focused reference files for schema checks, verdict shape, lane fit,
     and required-skills / locatability review rules
   - create `checklist.md` tuned to this higher-risk contract-review skill

3. **Review phase** (via independent `agent-skill-reviewer`):
   - verify the new skill is single-purpose and review-ready
   - verify it reviews blueprint contracts rather than skill folders
   - verify it mirrors the existing blueprint v1 executor contract instead of
     inventing new schema requirements
   - verify verdict expectations, lane-mismatch checks, and locatability checks
     are explicit and misuse-resistant
   - return `approved` or `needs-rework`

4. **Publish phase** (if `approved`):
   - commit the new review skill
   - update `README.md` with the stable-skill row at publish time
   - update `VERSION` from `0.32.0` to `0.33.0`
   - open PR after STOP POINT 1 approval
   - after merge and explicit human resume, create annotated tag `v0.33.0` and
     push it
   - update topic status to `released`

## Validation / Acceptance Checks

- confirm all required topic-plan sections are present and canonical
- confirm missing analysis artifacts are called out explicitly instead of being
  ignored silently
- confirm artifact paths are exact, bounded, and limited to the new review
  skill plus stable-library publish surfaces
- confirm the skill is explicitly about reviewing `blueprint.md`, not skill
  folders or execution outputs
- confirm blueprint v1 section order and `yaml [sensing-assertions]` placement
  are documented as locked review checks
- confirm exact-name `Required Skills` validation remains part of the review
  contract
- confirm abstract or non-locatable `Structural Invariants` fail review
  explicitly instead of being tolerated
- confirm greenfield-vs-retrofit lane mismatch is explicit and reroutes instead
  of being absorbed
- confirm the topic does not silently widen into
  `.github/skills/python-blueprint-authoring/` or
  `.github/skills/python-project-init-greenfield/`
- confirm stable-library metadata is complete and matches the current repo
  version baseline `0.32.0`
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
  - confirm `VERSION` equals `0.33.0`
  - create and push annotated tag `v0.33.0`
- When those release actions complete, transition the topic from `merged` to
  `released`.

## Open Questions / Unresolved Items

- None. This topic's blocking planning decisions are locked:
  - blueprint-contract review, not skill-folder review
  - existing blueprint v1 contract reuse
  - exact-name `Required Skills` review checks
  - locatability and lane-mismatch review checks
  - no default widening into authoring or executor changes
