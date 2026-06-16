## Analysis-layer routing

- Mode: `strict`
- Requirements baseline:
  `analysis/spec-docs-mvp-generator/requirements.md`
  - SHA-256: `c76a0cba925a696042bbf33ec2fb46d9cb1ffa2cc6ff6472337da72ef1c578c1`
- Technical baseline:
  `analysis/spec-docs-mvp-generator/technical-spec.md`
  - SHA-256: `38019538ad0856407a08532848325f30597935d292fb4b5c6fd1d2c06e7bc962`
- Priority rule: this topic plan and later creator execution must map 100% to
  the technical baseline above. The requirements baseline remains the business
  guardrail. No human `override` instruction exists for this topic.
- Artifact / input mapping:
  - `Goal / Outcome`, `Scope`, and `Locked Decisions` map to `Source Baseline Summary`
    and `Translation Stance`.
  - `Artifact Paths` map to `Exact Implementation Write Set`.
  - `Implementation Steps` map 1:1 to `Technical Design` sections 1 through 7.
  - `Validation / Acceptance Checks` map to `Requirement-to-Technical Mapping`,
    `Architecture-Compliance Self-Check`, and `Conflicts and Rollback Triggers`.

# Spec Docs MVP Generator Plan

## Goal / Outcome

Produce a bounded implementation contract for the canonical skill package
`skills/spec-docs-mvp-generator/` and the required progression artifact
`plan/spec-docs-mvp-generator/spec-docs-mvp-generator.step.md`.

When this topic is complete:

- `skills/spec-docs-mvp-generator/SKILL.md` exists and freezes the single-spec
  v1 input contract, exact downstream docs write targets, and refusal boundary
- `skills/spec-docs-mvp-generator/reference.md` exists and freezes local-only,
  safe-rerun, non-destructive merge behavior
- `skills/spec-docs-mvp-generator/examples.md` exists and covers new-file,
  patch-existing, and refusal scenarios
- `skills/spec-docs-mvp-generator/templates/spec-template.md` exists with the
  nine fixed non-empty starter sections
- `skills/spec-docs-mvp-generator/templates/data-ownership-map-template.md`
  exists with the fixed ownership-map structure and required table header
- the topic remains bounded to canonical `skills/` implementation only and does
  not reopen canonical/path/projection/runtime decisions or expand into a full
  architecture docs suite

## Scope

### In scope

- maintain topic-local planning artifacts for this topic:
  - `plan/spec-docs-mvp-generator/spec-docs-mvp-generator.plan.md`
  - `plan/spec-docs-mvp-generator/spec-docs-mvp-generator.step.md`
- use these frozen analysis inputs as read-only prerequisites:
  - `analysis/spec-docs-mvp-generator/requirements.md`
  - `analysis/spec-docs-mvp-generator/technical-spec.md`
- use these governance inputs as read-only prerequisites during later
  implementation:
  - `AGENTS.md`
  - `docs/repo-positioning.md`
- later creator implementation is limited to:
  - `skills/spec-docs-mvp-generator/SKILL.md`
  - `skills/spec-docs-mvp-generator/reference.md`
  - `skills/spec-docs-mvp-generator/examples.md`
  - `skills/spec-docs-mvp-generator/templates/spec-template.md`
  - `skills/spec-docs-mvp-generator/templates/data-ownership-map-template.md`
- later creator progression updates may modify only
  `plan/spec-docs-mvp-generator/spec-docs-mvp-generator.step.md` to reflect
  repo-visible workflow truth

### Out of scope

- `agents/**`, custom agent behavior, workflow-to-agent binding, or runtime
  orchestration
- `.github/**`, `.codex/**`, or any other projection/path migration work
- `README.md`, `VERSION`, release notes, tags, or any stable-library publish
  action
- generating repo-local implementation artifacts for
  `docs/01-specs/<spec-name>.md` or
  `docs/02-spec-relations/data-ownership-map.md`; those are downstream skill
  execution outputs, not this topic's implementation artifacts
- any expansion into `docs/00-overview/architecture-principles.md`,
  multi-spec maps, interfaces, flows, state machines, ADRs, implementation
  notes, or a broader architecture docs suite
- reviewer execution, commit work, PR work, or implementation inside this
  planning batch

## Locked Decisions

- This topic is not a stable-library publish topic. No `README.md` update,
  `VERSION` bump, tag, release action, or `merged` -> `released` transition is
  allowed.
- The only canonical implementation surface for this topic is
  `skills/spec-docs-mvp-generator/`.
- v1 remains single-spec only: one required `spec-name` drives the downstream
  target `docs/01-specs/<spec-name>.md`, and the only other downstream target
  is `docs/02-spec-relations/data-ownership-map.md`.
- The spec template contract is frozen to these sections in this exact order:
  `Summary`, `Problem`, `Goals`, `Non-goals`, `Actors`, `Requirements`,
  `Data Ownership Notes`, `Acceptance Signals`, `Open Questions`.
- The ownership-map template contract is frozen to these sections in this exact
  order: `Purpose`, `Ownership Table`, `Shared or Derived Data`,
  `Boundary Notes`, `Open Questions`, with the fixed table header
  `| Data Item | System of Record | Upstream Writers | Downstream Readers | Notes |`.
- Safe rerun is mandatory: preserve existing user content, fill only missing
  fixed sections or table header, do not duplicate same-name sections, and do
  not use destructive whole-file rewrite.
- Local-only generation is mandatory: no network fetch, external service,
  runtime orchestration, or extra platform-install dependency may be introduced.
- Reviewer feedback has already controlled routing once for this planning run.
  The repo-visible handoff path for further plan-review verdict history and
  re-review routing is
  `plan/spec-docs-mvp-generator/spec-docs-mvp-generator.review-log.md`.
  This slice declares that exact path but does not materialize the file.
- This planning batch produces only `plan.md` and `step.md`. It does not enter
  plan review, commit, implementation, or any other workflow role.

## Boundaries / Exclusions

### Non-goals

- rewriting repo governance or canonical-source policy
- treating projection surfaces as implementation targets
- adding scripts, CLI tooling, tests, or any extra implementation artifact
  outside the exact write set frozen by the technical baseline
- approximating out-of-scope document requests instead of refusing or rerouting
- entering implementation during `create-agent-plan.prompt.md`

### Workflow boundaries

- planning actor authors only the repo-visible planning artifacts for this
  phase
- creator later implements only inside the locked skill package write set and
  may update `step.md` from repo-visible facts
- reviewer later evaluates the plan and then the implementation independently
- Main Agent later owns commit, push, PR, merge, and post-merge routing only
  after reviewer approval

### Stop conditions

- if later work needs any file outside the exact artifact paths below, stop and
  repair the plan before continuing
- if any request reopens canonical/path/projection/runtime decisions, stop and
  route back to planning instead of widening this topic
- if any request expands the topic into a broader architecture docs suite,
  stop and require replanning
- if the frozen analysis layer appears to conflict with later convenience
  instructions and no human `override` exists, stop and surface the conflict
- if later plan-review or implementation-routing feedback must be persisted and
  the declared `plan/spec-docs-mvp-generator/spec-docs-mvp-generator.review-log.md`
  has not been materialized yet, stop instead of simulating that handoff in
  hidden context

## Status / Allowed Transitions

- **Current**: `planned`
- **Execution model**: follow the canonical creator -> reviewer -> publish ->
  merge path, with no release action for this topic
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

- The current workflow phase stops after
  `.github/prompts/create-agent-plan.prompt.md`.
- The next allowed role for this topic is `Plan-Reviewer`.
- One `needs-rework` plan-review verdict has already occurred for this planning
  run, so reviewer-routing state is active for this topic.
- The exact repo-visible handoff path for that bounded re-review loop is
  `plan/spec-docs-mvp-generator/spec-docs-mvp-generator.review-log.md`.
- No publish, merge, or creator implementation progress has happened yet in
  repo-visible truth.
- This topic does not declare `merged` -> `released`.

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Requirements baseline | `analysis/spec-docs-mvp-generator/requirements.md` | Planning actor | Frozen business baseline for the single-spec docs-generator scope |
| Technical baseline | `analysis/spec-docs-mvp-generator/technical-spec.md` | Planning actor | Execution-facing technical baseline for the bounded canonical skill implementation |
| Governance source | `AGENTS.md` | Planning actor / Creator | Canonical governance boundary for repository authority and topic limits |
| Repo positioning source | `docs/repo-positioning.md` | Planning actor / Creator | Read-only repository positioning guardrail for canonical-source and migration boundaries |
| Topic plan | `plan/spec-docs-mvp-generator/spec-docs-mvp-generator.plan.md` | Planning actor | Repo-visible execution contract for this topic |
| Topic progression artifact | `plan/spec-docs-mvp-generator/spec-docs-mvp-generator.step.md` | Planning actor / Creator / Main Agent | Current-truth workflow progression artifact for this topic |
| Review routing log | `plan/spec-docs-mvp-generator/spec-docs-mvp-generator.review-log.md` | Reviewer / Planning actor | Repo-visible verdict history and routing handoff for plan-review feedback that already entered the rework loop |
| Skill contract | `skills/spec-docs-mvp-generator/SKILL.md` | Creator | Canonical skill entrypoint defining required inputs, exact downstream targets, and refusal boundaries |
| Reference contract | `skills/spec-docs-mvp-generator/reference.md` | Creator | Deterministic local-only creation, merge, and rerun rules for the skill |
| Example surface | `skills/spec-docs-mvp-generator/examples.md` | Creator | Positive and refusal examples that make v1 scope and rerun behavior reviewable |
| Spec template | `skills/spec-docs-mvp-generator/templates/spec-template.md` | Creator | Fixed nine-section starter template for `docs/01-specs/<spec-name>.md` |
| Ownership-map template | `skills/spec-docs-mvp-generator/templates/data-ownership-map-template.md` | Creator | Fixed ownership-map template for `docs/02-spec-relations/data-ownership-map.md` |

Artifact path notes:

- This topic does not modify `README.md`.
- This topic does not modify `VERSION`.
- This topic does not modify any file under `agents/**`, `.github/**`, or
  `.codex/**`.
- This topic does not add scripts, tests, or any extra helper file outside the
  exact paths listed above.
- The downstream runtime write targets
  `docs/01-specs/<spec-name>.md` and
  `docs/02-spec-relations/data-ownership-map.md` are part of the skill
  contract only; they are not repo-local implementation artifacts for this
  topic and must not be created during this planning batch.
- The exact review-log path above is required because reviewer feedback has
  already controlled routing for this planning topic.
- This slice declares that repo-visible path only; it does not materialize an
  empty `review-log.md` file.
- Treat the listed paths as an executable contract. Any need to touch another
  path is a plan-alignment failure, not a harmless implementation detail.

## Implementation Steps

1. Create `skills/spec-docs-mvp-generator/SKILL.md` and define the canonical
   single-spec v1 contract: required `spec-name`, optional background inputs,
   exact downstream doc targets, stop-and-ask behavior when `spec-name` is
   missing, and explicit refusal / reroute handling for every excluded output
   family frozen by the analysis layer.
2. Create `skills/spec-docs-mvp-generator/reference.md` and codify the
   deterministic local-only write semantics: first creation, existing-file
   patching, partial-completion recovery, missing-section backfill, missing
   table-header backfill, no duplicate fixed headings, no destructive rewrite,
   and no network dependency.
3. Create `skills/spec-docs-mvp-generator/templates/spec-template.md` with the
   exact nine fixed sections from the technical baseline, preserving order and
   providing non-empty starter text, prompts, or bullets in every section.
4. Create
   `skills/spec-docs-mvp-generator/templates/data-ownership-map-template.md`
   with the exact five fixed sections from the technical baseline, the required
   ownership-table header, and non-empty seed content so the file is never a
   blank skeleton.
5. Create `skills/spec-docs-mvp-generator/examples.md` with at least these
   reviewable scenarios: new spec generation, existing spec missing-section
   backfill, existing ownership-map missing-header backfill, and refusal for an
   out-of-scope request such as architecture principles or multi-spec output.
6. Update `plan/spec-docs-mvp-generator/spec-docs-mvp-generator.step.md` from
   repo-visible creator-work facts only so the planning artifact stays aligned
   with the locked implementation scope and the next reviewer handoff, without
   using `step.md` to simulate reviewer, publish, or merge progression.
7. Stop and route back to planning if implementation requires any additional
   file path, any projection/runtime change, any full architecture docs-suite
   expansion, or any destructive whole-file rewrite behavior not frozen by the
   analysis layer.

## Validation / Acceptance Checks

- Analysis mapping check:
  the plan and later implementation remain in strict mode and map 100% to
  `analysis/spec-docs-mvp-generator/technical-spec.md`.
- Path contract check:
  creator work stays inside the exact `Artifact Paths` contract with no extra
  file creation or modification.
- Input-contract check:
  `skills/spec-docs-mvp-generator/SKILL.md` requires `spec-name`, lists only
  the two downstream doc targets, and refuses every excluded output family from
  the analysis layer.
- Spec-template check:
  `skills/spec-docs-mvp-generator/templates/spec-template.md` contains exactly
  the nine frozen sections in order and every section has non-empty starter
  content.
- Ownership-map-template check:
  `skills/spec-docs-mvp-generator/templates/data-ownership-map-template.md`
  contains exactly the five frozen sections in order, the required table
  header, and non-empty seed content.
- Safe-rerun check:
  `skills/spec-docs-mvp-generator/reference.md` explicitly preserves existing
  user content, fills only missing fixed structure, prevents duplicate
  same-name sections, and forbids destructive whole-file overwrite.
- Example coverage check:
  `skills/spec-docs-mvp-generator/examples.md` includes the four required
  scenario classes from the technical baseline.
- Local-only check:
  no network, external service, runtime orchestration, or platform-install
  dependency is introduced.
- Planning-boundary check:
  this planning batch creates only `plan.md` and `step.md`; it does not claim
  review completion, commit completion, or implementation progress that has not
  occurred yet.

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

- If later implementation for this topic is merged, only normal post-merge
  local sync may occur.
- No repository release action is required.
- No `README.md` update, `VERSION` bump, tag creation, or stable-library
  promotion is allowed in this topic.

## Open Questions / Unresolved Items

- None. Scope, analysis prerequisites, fixed template contracts, implementation
  write set, and non-stable intent are locked for this topic.
