## Analysis-layer routing

- Mode: `incomplete-layer routing`.
- Semantic warning: neither
  `analysis/scope-draft-plan/requirements.md` nor
  `analysis/scope-draft-plan/technical-spec.md` exists. This plan uses the
  explicitly authorized human scope as its planning input; it must not claim
  strict analysis-layer mapping or invent either missing artifact.
- Guardrail: an independent Plan-Reviewer must verify that the incomplete
  analysis layer has not left a contract-breaking ambiguity. A conflict that
  affects the locked outcome, artifact paths, stable-library timing, or release
  route is `needs-rework` / `BLOCKED`, not permission to expand the topic.

# Scope Draft Plan Skill Plan

## Goal / Outcome

Create the canonical stable Agent Skill package `skills/scope-draft-plan/`.
The skill converts a vague or overly fragmented product / engineering request
into one independently acceptable Bounded Context (BC) Mission Draft Plan, and
offers only non-binding suggestions for the next planning skill.

When the topic is complete:

- the seven locked canonical skill files exist under `skills/scope-draft-plan/`
- repository, DTO, database, service, API, and test work are treated as
  technical tasks inside one Mission rather than separate SDD projects
- the skill produces one suggested Mission, bounded assumptions, observable
  acceptance criteria, and explicit follow-up capabilities
- no agent dispatch, implementation, projection, or runtime binding is added
- after the single feature PR is merged and STOP POINT 2 is explicitly resumed,
  Phase 10 applies the approved stable metadata (`README.md` catalog row and
  root `VERSION` `0.77.0` -> `0.78.0`) and completes the release / tag route

## Scope

- **In scope**:
  - Create and maintain these topic-local planning / routing artifacts:
    - `plan/scope-draft-plan/scope-draft-plan.plan.md`
    - `plan/scope-draft-plan/scope-draft-plan.step.md`
    - `plan/scope-draft-plan/scope-draft-plan.review-log.md`
    - `plan/scope-draft-plan/scope-draft-plan.summary.md`
  - Create exactly these canonical skill files:
    - `skills/scope-draft-plan/SKILL.md`
    - `skills/scope-draft-plan/reference.md`
    - `skills/scope-draft-plan/examples.md`
    - `skills/scope-draft-plan/checklist.md`
    - `skills/scope-draft-plan/references/scope-sizing.md`
    - `skills/scope-draft-plan/references/output-template.md`
    - `skills/scope-draft-plan/references/handoff-routing.md`
  - After the feature PR has independently passed skill review and planner
    alignment, merged, reached STOP POINT 2, and received an explicit human
    resume, have Main Agent execute the same topic's deferred Phase 10 release
    action: update only `README.md` and root `VERSION` to the locked metadata,
    run release validation, obtain required tag authorization, and create / push
    `v0.78.0` when the gate passes.

- **Out of scope**:
  - Any `agents/**` change, including the Observer / Dispatcher contract,
    agent taxonomy, workflow-to-agent binding, or runtime orchestration
  - Changes to existing skills, including `business-intent-alignment`,
    `business-to-technical-translation`, `plan-creator`, or Python planning
    skills
  - `.github/**`, `.codex/**`, or any other projection / compatibility surface
  - Automatic skill dispatch, mandatory workflow gates, creation of
    `analysis/` or `plan/` artifacts by the new skill, or user-feature
    implementation
  - Data migrations, API contracts, or technical implementation work for a
    Mission a user later scopes with this skill
  - Any additional worktree, release branch, release PR, independent deferred-
    metadata reviewer cycle, release notes, GitHub Release body, or README historical
    migration snapshot

## Locked Decisions

- `skills/` is the only canonical source for this topic. The new skill must not
  create or imply a projection, compatibility mirror, registry, or runtime
  binding.
- The skill's sole job is BC Mission scope convergence. It does not produce a
  full implementation plan or execute the resulting Mission.
- The recommended Mission is the smallest complete end-to-end business
  capability: one primary BC, one main observable outcome, a primary happy
  path, and the necessary core failure path. A distinct valuable outcome is a
  follow-up Mission, not an extra technical subproject.
- The skill outputs one recommended Mission. It asks at most three questions
  only when the answer would materially alter the primary BC, core result, data
  ownership, public contract, irreversible risk, or whether the work is a
  spike. Other unknowns become explicit assumptions.
- The skill's next-step routing is advisory only: it may suggest
  `business-intent-alignment`, `business-to-technical-translation`,
  `plan-creator`, or `python-plan-authoring` when their stated prerequisites
  apply, but must not invoke, require, or dispatch any of them.
- This is one stable-library topic with deferred release timing. The managed
  feature worktree `../agent-skills.worktrees/agent-20260724-scope-draft-plan`
  on `feat/andrew/scope-draft-plan` writes only the four topic artifacts and
  seven canonical skill files. `README.md` and `VERSION` are forbidden from
  its feature PR.
- The locked stable metadata is applied by Main Agent only in Phase 10, after
  the feature PR is merged, STOP POINT 2 is reached, and a human explicitly
  resumes. This is a deferred release action in the same topic; it creates no
  additional worktree, branch, PR, independent reviewer pass, or lifecycle.
- The locked catalog row is:

  `| \`scope-draft-plan\` | converges vague or over-fragmented requests into one independently acceptable BC Mission Draft Plan with non-binding next-step guidance |`

  It belongs alphabetically after `sense-env-scaffold` and before
  `step-creator` in `## Current skills`.
- The locked release value is `0.78.0`, a **MINOR** bump from `0.77.0` because
  it adds a backward-compatible stable capability. The post-merge tag is the
  annotated tag `v0.78.0`; it is an external action, not a repository path.

## Boundaries / Exclusions

- Planning actor owns the four topic-local planning / handoff artifacts;
  Creator owns only the seven canonical skill files; Reviewer owns independent
  verdicts; Main Agent owns branch, worktree, PR, human-gate, post-merge, and
  deferred-release routing.
- Creator implementation must not update the topic plan, review log, summary,
  `README.md`, or `VERSION` to simulate review or release progress. The step
  artifact is progression truth and is updated only by its declared planning /
  Main Agent owners.
- The feature PR contains only the topic artifacts and canonical skill package.
  `README.md` and `VERSION` are written only by Main Agent's Phase 10 action
  after merge and explicit resume; they must not cause a transition from
  `merged` back to `publish-in-progress`.
- Any need to change a path outside `Artifact Paths`, introduce mandatory
  downstream routing, add a new role, reopen canonical-source / projection /
  runtime decisions, or create an additional release lifecycle is scope drift: stop
  and repair this plan first.
- Missing analysis artifacts are a known soft failure, not permission to write
  substitute analysis documents in this topic. A reviewer finding that their
  absence prevents safe scope or release interpretation must stop progression.

## Status / Allowed Transitions

- **Current**: `approved`
- **Execution model**: plan review -> creator -> independent skill review ->
  planner alignment -> one feature PR / human merge -> STOP POINT 2 -> explicit
  human resume -> Main Agent Phase 9 synchronization and Phase 10 deferred
  stable metadata / release action -> `released`.
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

- An independent Plan-Reviewer must first review this current topic-plan
  revision. Its verdict is persisted in the declared review log; approval moves
  the topic to Creator work, while `needs-rework` returns it to planning.
- Use the standard Phase 4.5 planner contract-alignment check after the
  independent skill reviewer approval. Any scope, contract, ownership, path,
  or release-timing drift returns the topic to creator rework.
- STOP POINT 1 requires explicit human authorization before the feature
  commit / push / PR. STOP POINT 2 is terminal after the human merge handoff;
  no polling or automatic continuation is allowed. Only a new explicit human
  resume may enter Phase 9 and then Phase 10.
- Phase 10 is entered from `merged`, never from `publish-in-progress`. Main
  Agent updates the deferred stable metadata, performs the declared release
  validation, and obtains the existing explicit tag authorization before tag
  creation; a late defect follows the repository's explicit post-merge routing.

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Governance source | `AGENTS.md` | Planning actor / Creator / Reviewer | Read-only canonical governance and source-model boundary |
| Repository positioning | `docs/repo-positioning.md` | Planning actor / Creator / Reviewer | Read-only positioning and migration-boundary guardrail |
| Repo workflow contract | `plan/agent-handoff-workflow.md` | Planning actor / Reviewer / Main Agent | Read-only phase, status, stop-point, and role contract |
| Topic-plan contract | `plan/topic-plan-contract.md` | Planning actor / Reviewer / Main Agent | Read-only required-section and handoff contract |
| Topic plan | `plan/scope-draft-plan/scope-draft-plan.plan.md` | Planning actor | Current execution contract for this topic |
| Topic progression | `plan/scope-draft-plan/scope-draft-plan.step.md` | Planning actor / Main Agent | Current-truth workflow progression and gate record |
| Review routing log | `plan/scope-draft-plan/scope-draft-plan.review-log.md` | Reviewer / Main Agent | Persisted independent review verdicts and routing evidence |
| Topic close summary | `plan/scope-draft-plan/scope-draft-plan.summary.md` | Planning actor / Main Agent | Current-truth close / follow-up handoff; updated only at a real close boundary |
| Skill contract | `skills/scope-draft-plan/SKILL.md` | Creator | Canonical entrypoint with trigger, scope-convergence process, validation, and boundaries |
| Skill overview | `skills/scope-draft-plan/reference.md` | Creator | Concise local glossary and local-reference routing |
| Skill examples | `skills/scope-draft-plan/examples.md` | Creator | Positive, negative, cross-BC, and ambiguity examples |
| Skill checklist | `skills/scope-draft-plan/checklist.md` | Creator | Repeatable pre-output scope and handoff checks |
| Scope-sizing reference | `skills/scope-draft-plan/references/scope-sizing.md` | Creator | Detailed too-small, too-large, and right-sized Mission signals |
| Output-template reference | `skills/scope-draft-plan/references/output-template.md` | Creator | Localizable Draft Plan output template |
| Handoff-routing reference | `skills/scope-draft-plan/references/handoff-routing.md` | Creator | Advisory-only downstream suggestion matrix and stop rules |
| Stable-library summary | `README.md` | Main Agent | Phase 10 only: add the locked catalog row after the feature PR merge and explicit human resume |
| Version source | `VERSION` | Main Agent | Phase 10 only: update the sole currently discovered version source from `0.77.0` to `0.78.0` in the same deferred release action |

Artifact path notes:

- The feature PR written set is exactly the four topic-local planning artifacts
  and seven canonical skill files. `README.md` and `VERSION` are excluded from
  that PR and belong only to Main Agent's deferred Phase 10 action.
- `AGENTS.md`, `docs/repo-positioning.md`, workflow contracts, and existing
  skill folders are read-only inputs. `analysis/scope-draft-plan/**` does not
  exist and is neither an input nor an allowed output.
- No artifact under `agents/**`, `.github/**`, `.codex/**`, or another
  `.<platform>/**` path is authorized. The tag is an external post-merge action.
- A required path outside this table is a plan-alignment failure; stop and
  repair the topic plan before writing it.

## Stable library metadata

### README row

- Table: `## Current skills`
- Exact row:

  `| \`scope-draft-plan\` | converges vague or over-fragmented requests into one independently acceptable BC Mission Draft Plan with non-binding next-step guidance |`

- Position: immediately after `sense-env-scaffold` and before `step-creator`.

### VERSION bump

- Current: `0.77.0`
- Direction: `MINOR`
- New: `0.78.0`
- Rationale: a new stable, backward-compatible skill capability.

### Timing

- README / VERSION timing: `release`.
- Reason: the single feature PR remains limited to the new canonical skill and
  its topic artifacts; stable metadata is applied by Main Agent only during
  Phase 10 after merge and explicit STOP POINT 2 resume.
- Release action: Phase 10 applies the two locked metadata edits, runs the
  existing release gate, requires a clean release state and fresh remote
  uniqueness evidence, obtains explicit human tag approval, then creates and
  pushes annotated tag `v0.78.0`.

### Additional release metadata

- No additional worktree, branch, PR, reviewer pass, release notes artifact, or
  historical migration snapshot is created for these edits.
- Before writing `VERSION`, Main Agent re-inventories version authorities. If
  another authoritative source exists or `VERSION` no longer reads `0.77.0`,
  stop and repair this plan; do not write an unlisted path.

## Implementation Steps

1. Create `skills/scope-draft-plan/SKILL.md` as a medium-complexity,
   ambiguity-sensitive canonical skill. Define its one responsibility,
   positive and negative triggers, bounded context discovery, single-Mission
   selection, at-most-three material questions, assumptions, output boundary,
   validation, failure handling, and explicit stop after the Draft Plan.
2. Create `reference.md`, `references/scope-sizing.md`, and
   `references/output-template.md` so the skill consistently distinguishes
   business capability from technical layers and provides the locked
   Traditional-Chinese Draft Plan structure without turning it into a
   file-by-file implementation plan.
3. Create `references/handoff-routing.md` so advice is conditional and
   non-binding: ambiguous business intent may suggest
   `business-intent-alignment`; frozen requirements may suggest
   `business-to-technical-translation`; a frozen technical spec may suggest
   `plan-creator`; Python-specific implementation planning may suggest
   `python-plan-authoring`.
4. Create `examples.md` and `checklist.md` with reviewable examples and checks
   for technical-task over-fragmentation, overlarge lifecycle scope, cross-BC
   ownership, blocking ambiguity, and explicit assumptions for low-impact
   unknowns.
5. Validate that all seven skill files agree: exactly one recommended Mission,
   no automatic dispatch or mandatory downstream workflow, no code / artifact
   mutation by the skill, no projection-path implication, and no implementation
   plan or technical-layer-as-Mission output.
6. Stop at `review-ready` and hand the canonical skill package plus this topic
   plan to an independent `agent-skill-reviewer`. Do not write `README.md` or
   `VERSION` in feature work.

## Validation / Acceptance Checks

- Planning-contract check: all required topic-plan sections are present in
  canonical order; status transitions, artifact ownership, reviewer JSON, and
  stop points match the single-topic deferred-release route.
- Analysis warning check: the plan names both missing analysis files, does not
  claim strict mapping, and records the bounded reviewer check rather than
  fabricating analysis output.
- Scope convergence check: a request such as "create an OrderRepository" is
  reframed as a complete, observable order capability rather than a technical
  Mission; the necessary technical layers remain in one task map.
- Size check: an end-to-end order lifecycle request keeps one primary capability
  and moves payment, refund, shipment, returns, or other independent outcomes
  to follow-up Missions.
- Cross-BC check: a multi-BC request declares primary BC, ownership, and
  contract dependency without silently implementing another BC.
- Ambiguity check: material uncertainty produces no more than three questions;
  low-impact uncertainty becomes declared assumptions.
- Output check: the Draft Plan contains one Mission, in/out scope,
  Given/When/Then behavior, observable acceptance criteria, impact boundaries,
  technical-task map, risk gates, verification direction, follow-ups, and
  implementation-plan handoff constraints, in Traditional Chinese by default.
- Autonomy check: routing advice remains conditional and does not create files,
  invoke skills, dispatch agents, or impose a workflow gate.
- Independent review check: the feature skill package receives an independent
  `agent-skill-reviewer` `approved` verdict before planner alignment and PR.
- Release check: the feature PR excludes `README.md` / `VERSION`; after merge
  and explicit resume, Main Agent alone applies the locked row and version bump
  in Phase 10, validates release readiness and tag uniqueness, then waits for
  explicit human tag approval before tag creation.

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

- After the human merges the one feature PR and explicitly resumes, Main Agent
  verifies the merge and runs the normal Phase 9 post-merge synchronization.
- With `timing=release`, Main Agent then performs Phase 10 without opening a
  additional worktree, branch, PR, or reviewer loop: apply the exact `README.md`
  row and `VERSION` bump, complete any required release-history action under
  the existing release procedure, and run `git-release-management` validation.
- A clean release state, synchronized version inventory, passing required
  evidence, and remote uniqueness of `v0.78.0` are required before tag action.
  Obtain explicit human tag approval before creating and separately pushing the
  annotated tag. A late defect after merge follows the workflow's explicit
  post-merge route; it must not reopen `publish-in-progress`.
- Do not create a GitHub Release body, release notes file, historical migration
  snapshot entry, additional PR, additional worktree, or separate deferred-
  metadata review.
  Worktree removal or branch deletion is outside this topic unless separately
  authorized as destructive cleanup.

## Open Questions / Unresolved Items

- The optional analysis pair
  `analysis/scope-draft-plan/requirements.md` and
  `analysis/scope-draft-plan/technical-spec.md` is absent. This is an explicit
  semantic warning, not an open implementation decision: the human-authorized
  scope above is sufficient only if independent plan review finds no
  contract-breaking ambiguity.
- No other contract-level question remains. Main Agent must verify current
  default-branch, merge, release readiness, version-source, and remote-tag
  facts at their applicable workflow phases rather than guessing them now.
