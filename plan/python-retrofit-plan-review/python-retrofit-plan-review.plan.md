# python-retrofit-plan-review topic plan

## Goal / Outcome

Create a repo-visible execution plan for a new stable skill at
`.github/skills/python-retrofit-plan-review/` that reviews authored Retrofit V2
`retrofit-plan.md` contracts before they are handed to
`python-project-retrofit`.

When complete, this topic should produce:

- a new stable skill that reviews retrofit contracts themselves rather than
  skill folders, topic plans, or implementation diffs
- a domain-specific quality gate between `python-retrofit-plan-authoring` and
  `python-project-retrofit`
- repeatable `approved|needs-rework` review outcomes for retrofit-plan contract
  defects

**Semantic warning**:
`analysis/python-retrofit-plan-review/requirements.md` exists at plan time, but
`analysis/python-retrofit-plan-review/technical-spec.md` is missing. This topic
plan is therefore authored with an incomplete analysis layer and does not enter
strict-mode 100% technical-spec mapping.

## Scope

- **In scope**:
  - create `.github/skills/python-retrofit-plan-review/SKILL.md`
  - create `.github/skills/python-retrofit-plan-review/examples.md`
  - create `.github/skills/python-retrofit-plan-review/checklist.md`
  - create `.github/skills/python-retrofit-plan-review/references/retrofit-v2-review-checks.md`
  - create `.github/skills/python-retrofit-plan-review/references/review-verdict-contract.md`
  - create `.github/skills/python-retrofit-plan-review/references/risk-boundary-and-locatability-checks.md`
  - create `.github/skills/python-retrofit-plan-review/references/lane-fit-and-reroute.md`
  - add a stable-library row for `python-retrofit-plan-review` to `README.md`
  - bump `VERSION` for the new stable skill topic
  - declare post-merge tag creation for the repository release tied to this topic

- **Out of scope**:
  - modifying `.github/skills/python-retrofit-plan-authoring/` unless plan
    repair is approved first
  - modifying `.github/skills/python-project-retrofit/` unless plan repair is
    approved first
  - modifying the locked Retrofit V2 schema
  - broadening supported sensing assertion kinds beyond the current v1 subset
  - implementing or modifying `sense_env.py`
  - creating `python-project-lane-router` or other router/meta-agent topics
  - generating `.github/copilot-instructions.md`

## Locked Decisions

- This topic is a **stable-library-affecting topic** with declared publish and
  release timing.
- The topic adds one new domain-specific reviewer skill:
  `.github/skills/python-retrofit-plan-review/`.
- `python-retrofit-plan-review` reviews authored Retrofit V2
  `retrofit-plan.md` contracts; it does **not** review skill folders,
  repo-visible topic plans, or implementation diffs.
- The skill must reuse the existing Retrofit V2 contract already consumed by
  `python-project-retrofit` and authored by
  `python-retrofit-plan-authoring`; it must not invent a new schema.
- The locked Retrofit V2 section order remains:
  1. `## Survey Summary`
  2. `## Gap Analysis`
  3. `## Target Transformation`
  4. `## Migration Strategy`
  5. `## Acceptance Criteria`
- `## Migration Strategy` must contain a parseable fenced
  ````yaml [migration-strategy]```` block with at least:
  - `risk_level`
  - `destructive_actions`
  - `backup_required`
- `risk_level` review remains locked to:
  - `LOW`
  - `HIGH`
  - `MEDIUM` is unsupported for current execution and must fail review
- `destructive_actions` must remain a YAML sequence, even when empty.
- `backup_required` must remain the YAML boolean `true` or `false`.
- `## Acceptance Criteria` must contain a parseable fenced
  ````yaml [sensing-assertions]```` block whose records include at least:
  - `kind`
  - `target`
  - `expected`
- The current supported assertion-kind subset remains:
  - `path_exists`
  - `path_type`
  - `command_available`
  Unsupported kinds are blocking review failures.
- The reviewer must explicitly check:
  - section order and presence
  - `migration-strategy` block validity
  - `sensing-assertions` block validity
  - risk-alignment contradictions
  - authoring-versus-executor boundary violations
  - locatability and executability of the target contract
  - retrofit-versus-greenfield lane fit
- The skill's review outcome is locked to a machine-consumable verdict concept:
  - `approved`
  - `needs-rework`
  - plus concrete blocking issues when it fails
- The skill must not widen into authoring or execution:
  - it does not draft the retrofit plan
  - it does not execute retrofit work
  - it does not replace `agent-skill-reviewer` for skill-folder review
- This topic does **not** widen scope into
  `.github/skills/python-retrofit-plan-authoring/` or
  `.github/skills/python-project-retrofit/` by default.
  If creator work discovers a true contract mismatch that would require touching
  either skill, stop and repair the topic plan before continuing execution.
- Stable-library timing is locked to `publish-in-progress`, meaning:
  - `README.md` and `VERSION` update during publish
  - annotated tag creation happens only after merge and explicit post-merge
    human resume
- The repository version baseline at plan time is `0.35.0`; this topic's
  release target is the next MINOR version `0.36.0`.

## Boundaries / Exclusions

- `python-retrofit-plan-review`
  - owns review of drafted Retrofit V2 `retrofit-plan.md` contracts
  - returns a contract-quality verdict and concrete blocking issues
  - does not author the retrofit plan
  - does not execute retrofit work

- `python-retrofit-plan-authoring`
  - continues to own upstream retrofit-plan drafting and repair
  - does not absorb reviewer responsibility into authoring

- `python-project-retrofit`
  - continues to own runtime execution, human gates, risk alignment at execution
    time, and acceptance handoff
  - does not become part of this topic's change set unless planner repair is
    explicitly approved

- `agent-skill-reviewer`
  - continues to review skill folders for repository compliance
  - this topic must not redefine it into a retrofit-plan contract reviewer

- `sense-env-scaffold`
  - continues to own acceptance assertion execution
  - this topic must not broaden its assertion-kind set

## Status / Allowed Transitions

- **Current**: `released`
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
- Reviewer should assess whether the new skill stays strictly in retrofit-plan
  review scope and does not silently widen into authoring, execution, or
  generic skill-folder review.

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/python-retrofit-plan-review/python-retrofit-plan-review.plan.md` | Planning actor | Repo-visible execution contract for this topic |
| Requirements baseline | `analysis/python-retrofit-plan-review/requirements.md` | Analysis layer | Frozen business-intent baseline that informs this topic's scope and warnings |
| Reviewer skill contract | `.github/skills/python-retrofit-plan-review/SKILL.md` | Creator | Executable contract for reviewing authored Retrofit V2 `retrofit-plan.md` files |
| Reviewer examples | `.github/skills/python-retrofit-plan-review/examples.md` | Creator | Layered examples for valid retrofit plans, blocked retrofit plans, and lane-mismatch review outcomes |
| Reviewer checklist | `.github/skills/python-retrofit-plan-review/checklist.md` | Creator | Higher-risk review checklist for retrofit contract safety and misuse prevention |
| Review reference: Retrofit V2 checks | `.github/skills/python-retrofit-plan-review/references/retrofit-v2-review-checks.md` | Creator | Locked section-order, machine-readable block, and schema-alignment review rules |
| Review reference: verdict contract | `.github/skills/python-retrofit-plan-review/references/review-verdict-contract.md` | Creator | Expected verdict shape, blocking-issue expectations, and review-output boundaries |
| Review reference: risk, boundary, and locatability checks | `.github/skills/python-retrofit-plan-review/references/risk-boundary-and-locatability-checks.md` | Creator | Risk-alignment review rules, planning-versus-runtime boundaries, and locatability checks |
| Review reference: lane fit and reroute | `.github/skills/python-retrofit-plan-review/references/lane-fit-and-reroute.md` | Creator | How to detect retrofit fit and reroute greenfield-shaped requests |
| Stable library row | `README.md` | Main Agent | Add the stable-skill table row for `python-retrofit-plan-review` at publish time |
| Repo version baseline | `VERSION` | Main Agent | Apply the `0.35.0` -> `0.36.0` MINOR bump when the topic is published |

Artifact path notes:

- This topic consumes `analysis/python-retrofit-plan-review/requirements.md`.
- This topic does not have
  `analysis/python-retrofit-plan-review/technical-spec.md` at plan time.
- This topic modifies `README.md` and `VERSION`.
- This topic does not modify `.github/copilot-instructions.md`.
- This topic does not modify `.github/skills/python-retrofit-plan-authoring/` or
  `.github/skills/python-project-retrofit/` unless the topic plan is explicitly
  repaired first.
- Treat the listed paths as an executable contract; if later work drifts
  outside them, stop and repair the topic plan before continuing execution.

## Stable library metadata

- `README row`: insert this exact table row immediately after
  `| \`python-retrofit-plan-authoring\` | authors review-ready Retrofit V2 contracts with locked section order, migration-strategy risk metadata, stop-and-ask handling for abstract plans, and strict separation between planning strategy and runtime gate decisions |`
  and before
  `| \`python-serialization-boundaries\` | defines Python serialization boundaries as semantic translation gates for API, database, and message payloads, including missing/null intent preservation, type normalization, deep conversion, and asymmetric input/output contracts |`:
  `| \`python-retrofit-plan-review\` | reviews authored Retrofit V2 \`retrofit-plan.md\` contracts against the locked section order, machine-readable risk metadata, supported sensing assertion kinds, locatability, and retrofit lane fit before executor handoff |`
- `VERSION bump`: `0.35.0` -> `0.36.0`
- `timing`: `publish-in-progress`
- `rationale`: this topic adds a new stable domain-specific review skill for the
  retrofit lane, so the stable skill table and repository version baseline must
  move together when the approved draft is published
- `release notes`: no separate release-notes artifact is planned; the annotated
  git tag message is the release-facing metadata for this topic

## Implementation Steps

1. **Branch preparation** (via Main Agent):
   - create or repair the semantic execution branch for
     `python-retrofit-plan-review`
   - verify worktree readiness before creator work begins
   - do not begin drafting from chat-only planning once this repo-visible plan
     exists

2. **Draft phase: new review skill** (via `agent-skill-creator`):
   - create `.github/skills/python-retrofit-plan-review/SKILL.md` with:
     - explicit trigger: review a drafted Retrofit V2 contract before execution
     - locked Retrofit V2 schema checks
     - risk-alignment and unsupported-risk review behavior
     - supported sensing-assertion-kind review behavior
     - authoring-versus-executor boundary checks
     - locatability and lane-mismatch review behavior
     - concise positive and negative examples
   - create `.github/skills/python-retrofit-plan-review/examples.md` with
     branching scenarios for:
     - valid retrofit plan approved
     - wrong section order or old headings
     - malformed `yaml [migration-strategy]`
     - malformed or unsupported `yaml [sensing-assertions]`
     - `LOW` risk contradicted by destructive reality
     - abstract target transformation or wrong-lane request
   - create focused reference files for schema checks, verdict shape, risk and
     boundary checks, and lane-fit reroute rules
   - create `checklist.md` tuned to this higher-risk contract-review skill

3. **Review phase** (via independent `agent-skill-reviewer`):
   - verify the new skill is single-purpose and review-ready
   - verify it reviews `retrofit-plan.md` contracts rather than skill folders
     or execution outputs
   - verify it mirrors the existing Retrofit V2 executor contract instead of
     inventing new schema requirements
   - verify unsupported assertion kinds, unsupported `risk_level`, and
     locatability failures are explicit blocking issues
   - return `approved` or `needs-rework`

4. **Publish phase** (if `approved`):
   - commit the new review skill
   - update `README.md` with the stable-skill row at publish time
   - update `VERSION` from `0.35.0` to `0.36.0`
   - open PR after STOP POINT 1 approval
   - after merge and explicit human resume, create annotated tag `v0.36.0` and
     push it
   - update topic status to `released`

## Validation / Acceptance Checks

- confirm all required topic-plan sections are present and canonical
- confirm the plan names the incomplete analysis layer explicitly instead of
  silently acting as if `technical-spec.md` exists
- confirm artifact paths are exact, bounded, and limited to the new review
  skill plus stable-library publish surfaces
- confirm the skill is explicitly about reviewing `retrofit-plan.md`, not skill
  folders or execution outputs
- confirm Retrofit V2 section order and both machine-readable blocks are
  documented as locked review checks
- confirm unsupported `risk_level` values and unsupported sensing assertion
  kinds fail review explicitly
- confirm risk-alignment contradictions fail review explicitly instead of being
  deferred to runtime discovery
- confirm planning-versus-runtime boundary violations are treated as blocking
  review failures
- confirm abstract or non-locatable target transformation details fail review
  explicitly instead of being tolerated
- confirm retrofit-vs-greenfield lane mismatch is explicit and reroutes instead
  of being absorbed
- confirm the topic does not silently widen into
  `.github/skills/python-retrofit-plan-authoring/` or
  `.github/skills/python-project-retrofit/`
- confirm stable-library metadata is complete and matches the current repo
  version baseline `0.35.0`
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
  - confirm `VERSION` equals `0.36.0`
  - create and push annotated tag `v0.36.0`
- When those release actions complete, transition the topic from `merged` to
  `released`.

## Open Questions / Unresolved Items

- None. This topic's blocking planning decisions are locked:
  - retrofit-plan contract review, not skill-folder review
  - existing Retrofit V2 contract reuse
  - machine-readable block validation and supported assertion-kind checks
  - risk-alignment, locatability, and lane-mismatch review checks
  - no default widening into authoring or executor changes

