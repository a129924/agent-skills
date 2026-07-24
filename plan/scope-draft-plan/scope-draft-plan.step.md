---
topic: scope-draft-plan
status: pr-open
created: 2026-07-24
current_plan_input: plan/scope-draft-plan/scope-draft-plan.plan.md
---

# Scope Draft Plan Skill Steps

## Workflow Stages

- [X] create feature worktree
- [X] materialize topic planning artifacts
- [X] independent plan review
- [X] Plan-Creator correction for existing-role routing
- [X] Plan-Creator correction for release-route wording
- [X] Plan-Creator correction for obsolete second-release lifecycle
- [X] independent plan re-review
- [X] canonical skill creation
- [X] independent skill review
- [X] Phase 4.5 planner contract alignment and STOP POINT 1
- [X] feature publication (commit, push, and PR)
- [X] Planner correction contract for PR #119 inventory drift
- [ ] bounded PR-comment correction, inventory regeneration, and independent review
- [ ] human merge handoff (PR #119 is open)
- [ ] post-merge synchronization, deferred release metadata, release gate,
  explicit tag approval, and tag push

## Actionable Steps

### create feature worktree

- [X] Use managed worktree
  `/Users/andrew/code/python/agent-skills.worktrees/agent-20260724-scope-draft-plan`.
- [X] Use branch `feat/andrew/scope-draft-plan`.
- [X] Keep all feature planning and Creator work inside this worktree.

### materialize topic planning artifacts

- [X] Create the four exact topic-local artifacts listed in the topic plan.
- [X] Record the missing optional analysis layer as a named semantic warning.
- [X] Lock the canonical skill write set, deferred `release` timing, catalog
  row, `0.77.0` -> `0.78.0` bump, and post-merge tag intent.

### independent plan review

- [X] Hand the current plan, step, review-log, and summary artifacts to an
  independent Plan-Reviewer.
- [X] Receive the fixed `needs-rework` verdict and materialize it in the review
  log before creator work starts.
- [X] Return the affected planning artifacts to Plan-Creator; do not start
  skill creation.

### Plan-Creator correction for existing-role routing

- [X] Replace the unauthorized release-specific role designation with existing
  role ownership.
- [X] Preserve the bounded feature write set and release metadata boundary.

### Plan-Creator correction for release-route wording

- [X] Remove obsolete separate-release routing from the topic-local current
  truth.
- [X] Preserve the feature PR's exclusion of `README.md` and `VERSION` and the
  required STOP POINT 2 human resume before any deferred release work.

### Plan-Creator correction for obsolete second-release lifecycle

- [X] Synchronize all topic-local artifacts with the human-locked single-topic
  route: one feature PR, then after merge / STOP POINT 2 / explicit resume,
  Main Agent performs Phase 10 release metadata and tag work.
- [X] Lock `timing=release`; remove all separate-worktree, separate-PR, and
  independent deferred-metadata review language.
- [X] Confirm that Phase 10 advances only `merged` -> `released`, never back to
  `publish-in-progress`.

### independent plan re-review

- [X] Hand the corrected plan, step, review-log, and summary artifacts to an
  independent Plan-Reviewer.
- [X] Receive the required fixed `approved` verdict before Creator
  work starts.
- [X] Keep the `needs-rework` return route limited to affected planning
  artifacts to Plan-Creator; do not start skill creation.

### canonical skill creation

- [X] After plan approval, Creator created only the seven locked files under
  `skills/scope-draft-plan/`.
- [X] Kept `README.md`, `VERSION`, existing skills, agents, projections, and
  runtime surfaces untouched.
- [X] No implementation path or decision outside the locked
  contract.

### independent skill review

- [X] Hand the Creator output and topic plan to independent
  `agent-skill-reviewer`.
- [X] Record the independent `PASS` verdict with no blockers in the review log.
- [X] No Creator rework is required; the seven-file package is review-ready.

### Phase 4.5 planner contract alignment and STOP POINT 1

- [X] Main Agent performed the Phase 4.5 planner contract-alignment check
  against the approved topic contract and reviewed seven-file package.
- [X] Alignment passed with no scope, contract, ownership, path, or
  release-timing drift; STOP POINT 1 received explicit human authorization
  before publication.

### PR #119 correction loop

- [X] Planner classified the P1 inventory drift as `medium / PLANNER_REPLAN`.
- [X] Added parent-contract paths for the correction artifacts and generated
  canonical inventory snapshot; the original exact-11 publication count is no
  longer the current PR write-set contract.
- [ ] A separate Implementer completes exactly four bounded PR-comment repairs:
  the output template permits only a BC Mission or blocks Cross-BC / Spike
  alternatives; this step artifact corrects the stale post-publication
  characterization; the summary corrects the same characterization; and the review log records
  `approved` as the skill-review gate verdict, with `PASS` only explanatory
  prose if retained. The Implementer then regenerates the inventory with the
  existing builder and verifies exactly 57 records: exactly one newly added
  record whose `canonical_path` equals `skills/scope-draft-plan` (no trailing
  slash), with all existing 56 records unchanged.
- [ ] A separate Reviewer approves the bounded correction before Main Agent
  commits and pushes it to PR #119.

### feature PR and human merge handoff

- [X] Pre-commit validation passed, STOP POINT 1 authorization was received,
  and commit `71f56cb1646dc218ba8b7cbd10409a60229faa3a` was created and pushed
  on `feat/andrew/scope-draft-plan`.
- [X] Opened Draft PR #119 to `dev`; the original publication commit contained
  four topic-local artifacts and seven canonical skill files. The current PR
  correction write set is defined by the parent plan and additionally includes
  the two correction artifacts and generated inventory snapshot; `README.md`
  and `VERSION` remain excluded.
- [ ] PR #119 is `pr-open` at the human review / merge boundary. STOP POINT 2
  applies after the human merge handoff; do not poll or start Phase 9 / 10
  until a new explicit human resume follows confirmed merge.

### post-merge synchronization, deferred release metadata, release gate, explicit tag approval, and tag push

- [ ] Only after confirmed feature-PR merge and explicit human resume, Main
  Agent runs normal Phase 9 synchronization and enters Phase 10.
- [ ] Main Agent re-inventories version authorities and, if the locked evidence
  remains valid, updates only `README.md` and `VERSION` with the locked row and
  `0.77.0` -> `0.78.0` value as the deferred release action.
- [ ] Run the existing release gate; require passing evidence, clean release
  state, and remote uniqueness of `v0.78.0`.
- [ ] Obtain distinct explicit human tag approval, then create and push the
  annotated tag. Update progression and close summary from observed facts.

## Handoff / Gate Notes

- This step artifact is progression truth only. It does not redefine the plan,
  approve work, or authorize release actions.
- Creator never writes the review log, summary, `README.md`, or `VERSION`.
  Reviewer is independent from Creator. The topic is `pr-open` after passing
  Phase 4.5 and STOP POINT 1; Main Agent owns the deferred Phase 10 metadata
  and tag route only after merge, STOP POINT 2, and explicit human resume.
- The managed feature worktree was clean immediately after publication. The
  current topic-local correction artifacts and status updates await the same
  PR #119 correction commit and do not record a new reviewer verdict; the
  review log awaits its bounded gate-verdict repair.
- Analysis artifacts are absent. Do not create them implicitly; treat a
  plan-review finding that they are required as a blocker.
- Any unsupported expansion routes to plan repair before work continues.
- The PR #119 correction is bounded to the existing topic. It does not create a
  new worktree, PR, release route, or Human Gate.
