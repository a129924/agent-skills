# python-retrofit-plan-authoring topic plan

## Goal / Outcome

Create a repo-visible execution plan for a new stable skill at
`.github/skills/python-retrofit-plan-authoring/` that authors review-ready
Retrofit V2 contracts for existing Python repositories, while synchronously
upgrading `.github/skills/python-project-retrofit/` to consume the same V2
contract without a compatibility layer.

When complete, this topic should produce:

- a new stable skill that turns retrofit intent into a locked, review-ready
  `retrofit-plan.md`
- a synchronized Retrofit V2 contract shared by authoring and executor
- a risk-aware `Migration Strategy` protocol with machine-readable risk fields
  and executor guardrails
- updated executor guidance so runtime gates, risk alignment checks, and
  destructive previews all consume the same contract shape

## Scope

- **In scope**:
  - create `.github/skills/python-retrofit-plan-authoring/SKILL.md`
  - create `.github/skills/python-retrofit-plan-authoring/examples.md`
  - create `.github/skills/python-retrofit-plan-authoring/references/retrofit-v2-contract.md`
  - create `.github/skills/python-retrofit-plan-authoring/references/migration-strategy-risk-model.md`
  - create `.github/skills/python-retrofit-plan-authoring/references/authoring-vs-executor-boundaries.md`
  - create `.github/skills/python-retrofit-plan-authoring/checklist.md`
  - upgrade `.github/skills/python-project-retrofit/SKILL.md` to Retrofit V2
    contract semantics
  - upgrade `.github/skills/python-project-retrofit/examples.md` to cover V2
    section order, `migration-strategy` YAML, risk-alignment mismatch, and
    destructive-preview behavior
  - upgrade `.github/skills/python-project-retrofit/references/retrofit-conflict-resolution.md`
    where V2 contract wording affects runtime-gate interpretation
  - upgrade `.github/skills/python-project-retrofit/references/retrofit-safety-guidelines.md`
    to consume `Risk Level`, destructive preview, and confirmation behavior
  - create `.github/skills/python-project-retrofit/references/retrofit-plan-v2-contract.md`
    as the executor-side parsing contract for Retrofit V2
  - add a stable-library row for `python-retrofit-plan-authoring` to `README.md`
  - bump `VERSION` for the new stable skill topic
  - declare post-merge tag creation for the repository release tied to this topic

- **Out of scope**:
  - creating `python-retrofit-plan-reviewer`
  - creating `python-blueprint-authoring` or `python-blueprint-reviewer`
  - implementing or modifying `sense_env.py`
  - broadening supported assertion kinds beyond the current sensing contract
  - adding a compatibility layer from old retrofit-plan section names to Retrofit
    V2 section names
  - adding Medium-risk runtime execution behavior in this topic
  - performing real target-project retrofit execution, provenance writing, or
    Delta Report generation outside the skill contracts and examples

## Locked Decisions

- This topic is a **stable-library-affecting topic** with declared publish and
  release timing.
- The topic has **two coupled outputs** that must stay synchronized:
  1. a new upstream authoring skill:
     `.github/skills/python-retrofit-plan-authoring/`
  2. a synchronized executor upgrade:
     `.github/skills/python-project-retrofit/`
- **Retrofit V2 Protocol** is locked as the only target contract for this topic.
  The locked section order is:
  1. `## Survey Summary`
  2. `## Gap Analysis`
  3. `## Target Transformation`
  4. `## Migration Strategy`
  5. `## Acceptance Criteria`
- `## Acceptance Criteria` must contain a fenced
  ````yaml [sensing-assertions]```` block whose records include at least
  `kind`, `target`, and `expected`.
- `## Migration Strategy` must contain a machine-readable
  ````yaml [migration-strategy]```` block rather than free-form-only risk prose.
- `migration-strategy` must at minimum support:
  - `risk_level`
  - `destructive_actions`
  - `backup_required`
- `risk_level` is currently locked to:
  - `LOW`
  - `HIGH`
  - `MEDIUM` reserved for future extension only
- `Risk Level` must be classified from observable physical traits, not agent
  intuition:
  - `LOW`: pure additions or non-destructive configuration changes
  - `HIGH`: existing directory reshaping, existing code relocation, or multiple
    core-toolchain replacements
- `Risk Level` is not decorative. It must change executor behavior:
  - `LOW`: lightweight confirmation path
  - `HIGH`: hard gate with destructive preview plus explicit authorization and
    commit / backup precondition
- A **Risk Alignment Check** is required:
  - if the contract says `LOW` but executor scanning finds destructive actions,
    executor must hard-block and require plan or risk correction
- `Migration Direction` is allowed in planning only as a **strategy
  declaration**, not as a substitute for runtime gate choices.
- `contract 太抽象` is locked as **authoring stop-and-ask**:
  if the contract lacks locatability such as concrete paths, concrete tool names,
  or verifiable targets, authoring must stop and require clarification.
- Blueprint-side concerns such as `Required Skills` validation remain out of this
  topic's ownership.
- No compatibility mapping layer is allowed. Authoring and executor must upgrade
  together to Retrofit V2 in the same topic.
- Stable-library timing is locked to `stable-library-affecting-now`, meaning:
  - `README.md` and `VERSION` are updated at `publish-in-progress`
  - annotated tag creation happens after merge on explicit post-merge resume
- The repository version baseline at plan time is `0.27.0`; this topic's
  release target is the next MINOR version `0.28.0`.

## Boundaries / Exclusions

- `python-retrofit-plan-authoring`
  - owns authoring of review-ready Retrofit V2 `retrofit-plan.md`
  - does not execute retrofit operations or bypass runtime human gates

- `python-project-retrofit`
  - owns runtime execution, conflict gates, destructive preview, risk alignment
    check, and acceptance handoff
  - does not author the retrofit plan itself

- `sense-env-scaffold`
  - continues to own assertion execution and manifest-based acceptance
  - this topic must not broaden its assertion-kind set

- `copilot-instructions-init`
  - continues to own formal `.github/copilot-instructions.md` generation / refresh
  - this topic must not absorb instructions generation

- Future `python-retrofit-plan-reviewer`
  - may later own dedicated review of authored retrofit plans
  - this topic must not backfill that role into the authoring skill itself

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
- Reviewer must assess the new authoring skill and the synchronized executor
  upgrade as one contract pair, not as two unrelated drafts.

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/python-retrofit-plan-authoring/python-retrofit-plan-authoring.plan.md` | Planning actor | Repo-visible execution contract for this topic |
| Authoring skill contract | `.github/skills/python-retrofit-plan-authoring/SKILL.md` | Creator | Executable contract for drafting review-ready Retrofit V2 `retrofit-plan.md` |
| Authoring examples | `.github/skills/python-retrofit-plan-authoring/examples.md` | Creator | Layered examples for good / bad Retrofit V2 plans, ambiguity stops, and planning-vs-runtime boundaries |
| Authoring reference: V2 contract | `.github/skills/python-retrofit-plan-authoring/references/retrofit-v2-contract.md` | Creator | Locked section order, parsing expectations, and required machine-readable blocks for Retrofit V2 |
| Authoring reference: risk model | `.github/skills/python-retrofit-plan-authoring/references/migration-strategy-risk-model.md` | Creator | `Risk Level` semantics, `migration-strategy` YAML schema, and alignment rules |
| Authoring reference: boundaries | `.github/skills/python-retrofit-plan-authoring/references/authoring-vs-executor-boundaries.md` | Creator | What belongs in strategy declaration versus runtime gate choice |
| Authoring checklist | `.github/skills/python-retrofit-plan-authoring/checklist.md` | Creator | Higher-risk authoring validation checklist for V2 contract quality and ambiguity handling |
| Executor skill contract | `.github/skills/python-project-retrofit/SKILL.md` | Creator | Upgrade executor to consume Retrofit V2 sections, risk metadata, and risk-alignment blocking |
| Executor examples | `.github/skills/python-project-retrofit/examples.md` | Creator | Show V2 parsing, destructive preview, risk mismatch, and gate sequencing |
| Executor conflict reference | `.github/skills/python-project-retrofit/references/retrofit-conflict-resolution.md` | Creator | Keep runtime-gate wording consistent with V2 plan semantics |
| Executor safety reference | `.github/skills/python-project-retrofit/references/retrofit-safety-guidelines.md` | Creator | Document how `Risk Level`, destructive preview, and commit / backup safety interact |
| Executor V2 parsing reference | `.github/skills/python-project-retrofit/references/retrofit-plan-v2-contract.md` | Creator | Executor-side parsing contract for Retrofit V2 sections and `migration-strategy` YAML |
| Stable library row | `README.md` | Main Agent | Add the stable-skill table row for `python-retrofit-plan-authoring` at publish time |
| Repo version baseline | `VERSION` | Main Agent | Apply the `0.27.0` -> `0.28.0` MINOR bump when the topic is published |

Artifact path notes:

- This topic modifies `README.md` and `VERSION`.
- This topic does not modify `.github/copilot-instructions.md`.
- Treat the listed paths as an executable contract; if later work drifts outside
  them, stop and repair the topic plan before continuing execution.

## Stable library metadata

- `README row`: insert this exact table row immediately after
  `| \`python-project-retrofit\` | retrofits existing Python projects with safe structural conflict detection (Shadow File Detection), implicit configuration discovery (Implicit Config Mining), Git safety checks, and Sensing Delta Report for transparent state transformation |`
  and before
  `| \`sense-env-scaffold\` | scaffolds environmental-constraint check scripts with JSON manifest output |`:
  `| \`python-retrofit-plan-authoring\` | authors review-ready Retrofit V2 contracts with locked section order, migration-strategy risk metadata, stop-and-ask handling for abstract plans, and strict separation between planning strategy and runtime gate decisions |`
- `VERSION bump`: `0.27.0` -> `0.28.0`
- `timing`: `publish-in-progress`
- `rationale`: this topic adds a new stable skill and simultaneously upgrades an
  existing stable retrofit executor to the same V2 contract, so the stable skill
  table and version baseline must move together when the approved draft is
  published
- `release notes`: no separate release-notes artifact is planned; the annotated
  git tag message is the release-facing metadata for this topic

## Implementation Steps

1. **Branch preparation** (via Main Agent):
   - create or repair the semantic execution branch for
     `python-retrofit-plan-authoring`
   - verify worktree readiness before creator work begins
   - do not begin drafting from chat-only planning once this repo-visible plan
     exists

2. **Draft phase: new authoring skill** (via `agent-skill-creator`):
   - create `.github/skills/python-retrofit-plan-authoring/SKILL.md` with:
     - explicit trigger: when to author a retrofit plan rather than execute one
     - Retrofit V2 section order
     - stop-and-ask behavior for abstract, contradictory, or misrouted plans
     - clear boundary between strategy declaration and runtime gate choice
     - concise positive and negative examples
   - create `.github/skills/python-retrofit-plan-authoring/examples.md` with
     branching scenarios for:
     - V2-compliant plan creation
     - abstract target transformation rejection
     - risk-level mismatches
     - lane mismatch (greenfield vs retrofit)
   - create reference files for V2 contract, risk model, and
     authoring-vs-executor boundary
   - create `checklist.md` tuned to this higher-risk contract-authoring skill

3. **Draft phase: synchronized executor upgrade** (via `agent-skill-creator`):
   - update `.github/skills/python-project-retrofit/SKILL.md` to consume:
     - Retrofit V2 section order
     - `yaml [migration-strategy]`
     - `Risk Level`
     - destructive preview behavior
     - Risk Alignment Check
   - update `.github/skills/python-project-retrofit/examples.md` to show:
     - `LOW` path with lightweight confirmation
     - `HIGH` path with destructive preview and explicit authorization
     - `LOW` mislabeled as destructive and blocked by risk-alignment mismatch
   - update retrofit conflict and safety references to remain consistent with V2
     semantics
   - create executor-side `retrofit-plan-v2-contract.md`

4. **Review phase** (via independent `agent-skill-reviewer`):
   - verify the new authoring skill is single-purpose and review-ready
   - verify executor changes stay within runtime-execution scope and do not
     absorb authoring responsibility
   - verify V2 section order and `migration-strategy` YAML are consistent across
     authoring and executor
   - verify risk-level semantics and Risk Alignment Check are explicit and
     misuse-resistant
   - return `approved` or `needs-rework`

5. **Publish phase** (if `approved`):
   - commit the new authoring skill and synchronized executor upgrade
   - update `README.md` with the stable-skill row at publish time
   - update `VERSION` from `0.27.0` to `0.28.0`
   - open PR after STOP POINT 1 approval
   - after merge and explicit human resume, create annotated tag `v0.28.0` and
     push it
   - update topic status to `released`

## Validation / Acceptance Checks

- confirm all required topic-plan sections are present and canonical
- confirm artifact paths are exact, bounded, and cover both the new authoring
  skill and the synchronized executor upgrade
- confirm this topic does not rely on any compatibility mapping with old
  retrofit-plan section names
- confirm Retrofit V2 section order is identical across authoring and executor
- confirm `yaml [migration-strategy]` is documented as machine-readable and not
  replaced by free-form-only prose
- confirm `risk_level` is explicit, uses `LOW` / `HIGH`, and reserves `MEDIUM`
  without requiring executor support today
- confirm Low/High runtime paths are distinct and the High path requires
  destructive preview plus explicit authorization
- confirm Risk Alignment Check blocks `LOW` plans that would execute destructive
  actions
- confirm boundaries remain explicit between authoring strategy declaration and
  executor runtime gate choice
- confirm stable-library metadata is complete and matches the current repo
  version baseline `0.27.0`
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
  - confirm `VERSION` equals `0.28.0`
  - create and push annotated tag `v0.28.0`
- When those release actions complete, transition the topic from `merged` to
  `released`.

## Open Questions / Unresolved Items

- None. This topic's blocking planning decisions are locked:
  - Retrofit V2 section order
  - authoring + executor synchronous upgrade path
  - machine-readable `migration-strategy` YAML
  - `Risk Level` semantics and guardrail behavior
  - Risk Alignment Check
