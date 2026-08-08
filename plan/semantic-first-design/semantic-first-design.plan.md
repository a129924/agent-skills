# Semantic-First Design — Topic Plan

## Analysis-layer routing

**Semantic warning — optional analysis layer absent:** neither
`analysis/semantic-first-design/requirements.md` nor
`analysis/semantic-first-design/technical-spec.md` exists. This plan uses the
explicit human decisions captured for this topic; it does not claim a frozen
analysis prerequisite. If either analysis artifact is introduced later, stop
and reconcile its authority before changing this plan.

## Goal / Outcome

- Add a Python-first reusable `semantic-first-design` skill at the canonical
  `skills/` source surface. It guides agents to make important semantics visible
  in names, types, signatures, composition, and explicit failure handling.
- The completed topic has three focused skill artifacts and a stable-library
  promotion contract; it does not change the existing specialised Python skills.

## Scope

- **In scope**:
  - Create the three canonical skill artifacts listed under `Artifact Paths`.
  - Create this topic's plan, progression, and review-routing artifacts.
  - After independent reviewer approval, update the designated README row and
    bump `VERSION` from `0.77.0` to `0.78.0` during `publish-in-progress`.

- **Out of scope**:
  - Changes to existing Python skills, their contracts, or their content.
  - `.github/**` and `.codex/**` skill projections or platform-path migration.
  - Runtime code, API changes, release notes, tags, releases, merge, and
    post-merge cleanup.

## Locked Decisions

- This is a Python-first reusable semantic guardrail, not a replacement for
  specialised Python design skills.
- The sole canonical implementation source is `skills/semantic-first-design/`.
  Its exact artifacts are `SKILL.md`, `reference.md`, and `examples.md`.
- The skill identifies ambiguity in contracts, type/state, absence,
  boolean/policy, boundaries, composition, abstraction, and failure semantics;
  it directs specialised work to existing skills rather than duplicating them.
- The implementation must prefer the smallest semantic distinction that removes
  ambiguity. It must not prescribe wrapper types, interfaces, enums, or patterns
  merely for uniformity.
- This is a stable-library-affecting topic. `README.md` and `VERSION` change only
  after independent review approval, at `publish-in-progress`.
- A merged change has no automatic release or tag: a human gate after merge must
  explicitly authorize any release action.

## Boundaries / Exclusions

- Plan-Creator owns only the topic planning artifacts. It does not implement or
  approve the skill.
- Implementer creates only the three canonical skill artifacts inside the locked
  scope. It must not update existing Python skills or projections.
- Plan-Reviewer independently reviews planning artifacts; Reviewer independently
  reviews the implementation. Neither role authors the implementation.
- Main Agent owns branch/worktree routing, publish actions, PR flow, and human
  gates. Human review is the terminal handoff after the draft PR opens.
- Any requested path outside `Artifact Paths`, contract drift, or semantic scope
  expansion requires plan repair before execution continues.

## Status / Allowed Transitions

- **Current**: `planned`
- **Execution model**: use the canonical creator -> reviewer -> publish -> merge
  path. An independent Plan-Reviewer check occurs before creator implementation;
  it validates the plan but does not replace a canonical topic status.
- **Phase 4.5**: apply the standard planner contract-alignment rule after the
  implementation Reviewer returns `approved`.
- **Human gates**: STOP POINT 1 governs commit, push, and draft PR preparation.
  After the draft PR is opened, stop for human review. After merge, STOP POINT 2
  applies; release/tag work requires a new explicit human resume and approval.
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

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/semantic-first-design/semantic-first-design.plan.md` | Plan-Creator | Current execution contract and locked scope |
| Topic progression | `plan/semantic-first-design/semantic-first-design.step.md` | Plan-Creator; then Main Agent | Current stage readiness and gate record |
| Review routing log | `plan/semantic-first-design/semantic-first-design.review-log.md` | Plan-Creator initializes; Plan-Reviewer and Reviewer append their own verdicts | Repo-visible routing record when independent review controls rework |
| Canonical skill instructions | `skills/semantic-first-design/SKILL.md` | Implementer | Python-first trigger, boundary, workflow, and output contract |
| Semantic reference | `skills/semantic-first-design/reference.md` | Implementer | Decision heuristics and routing to specialised Python skills |
| Worked examples | `skills/semantic-first-design/examples.md` | Implementer | Positive and negative ambiguity-resolution examples |
| Stable-library index | `README.md` | Main Agent | Add the approved skill row during `publish-in-progress` |
| Repository version | `VERSION` | Main Agent | Bump from `0.77.0` to `0.78.0` during `publish-in-progress` |

Artifact path notes:

- `README.md` and `VERSION` are intentionally deferred until independent
  implementation approval; `.github/copilot-instructions.md` is not modified.
- The external managed feature-worktree path is execution context, not a
  repo-visible artifact path. Any new tracked path requires topic-plan repair
  before modification.

## Stable library metadata

- **README row**: add exactly this row to `README.md` under `## Current skills`:

  ```markdown
  | `semantic-first-design` | guides Python-first design and review toward explicit contracts, states, policies, boundaries, composition, and failure semantics |
  ```

- **Placement**: append it after the existing `sense-env-scaffold` row and before
  `step-creator`, preserving the table's existing ordering convention for
  non-`python-` general skills.
- **VERSION bump**: MINOR, `0.77.0` -> `0.78.0`, because this adds a new
  backwards-compatible stable capability.
- **Timing**: `publish-in-progress`, only after the independent Reviewer returns
  `approved` and Phase 4.5 confirms the implementation still matches this plan.
- **Rationale**: the stable library should advertise only an approved canonical
  skill; no release note, tag, or release is part of this promotion.

## Implementation Steps

1. Implementer creates `skills/semantic-first-design/SKILL.md` as the bounded
   Python-first guardrail, including clear triggers, exclusions, semantic-first
   heuristics, minimal-change guidance, and direct routes to the existing
   specialised Python skills.
2. Implementer creates `reference.md` with the decision framework for explicit
   contracts, state guarantees, optional values, policies, boundaries,
   composition, abstraction, and failures. It must distinguish semantic
   guidance from a mandate to add abstractions.
3. Implementer creates `examples.md` with concise positive and negative Python
   examples for ambiguous optional values, booleans, failures, hidden
   dependencies, and unnecessary abstractions.
4. Implementer validates the three artifacts against their declared contract and
   returns `review-ready`. No stable-library metadata change occurs in these
   creator steps.

## Validation / Acceptance Checks

- All three planning artifacts exist at the listed paths and use canonical
  workflow/status semantics; this plan contains all required shared-contract
  sections in canonical order.
- `SKILL.md` YAML and body agree on the Python-first, ambiguity-sensitive scope;
  `reference.md` and `examples.md` have distinct, non-duplicative roles.
- The implementation gives an explicit resolution path for ambiguous optional,
  boolean/policy, and failure outcomes; it treats local reasoning and semantic
  boundaries as review criteria.
- The implementation does not prescribe fake steps, generic dependency
  containers, blanket primitive wrappers, or one-interface-per-function rules.
- Existing specialised Python skills and all `.github/**` / `.codex/**` paths
  remain unchanged.
- Independent Plan-Reviewer and Reviewer verdicts use the exact JSON contract in
  this plan; a `needs-rework` verdict routes to the appropriate independent
  creator/implementer rather than being self-approved.
- Before publish, Phase 4.5 confirms the approved implementation's paths and
  scope still match this plan. Before commit/push/PR, STOP POINT 1 must have
  explicit human authorization and validation must pass.

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

- After the human merges the draft PR, execution stops at STOP POINT 2.
- There is no automatic release, annotated tag, release note, or local cleanup.
- A new explicit human resume and release authorization is required to assess
  whether `v0.78.0` should be tagged or released.

## Open Questions / Unresolved Items

- None. The optional analysis layer is absent and recorded as a semantic warning,
  not an unresolved execution decision.
