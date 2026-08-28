# Cross-Language Skill Candidate Basis Content Corrections

## Analysis-Layer Routing

**Semantic warning:** neither
`analysis/cross-language-skill-candidate-basis-content-corrections/requirements.md`
nor
`analysis/cross-language-skill-candidate-basis-content-corrections/technical-spec.md`
exists. This recovery baseline uses the human-frozen six-cell correction
direction. The missing analysis layer does not authorize inferred language
validation, migration, platform work, or any scope beyond those six cells.

## Goal / Outcome

Maintain a truthful, reviewable recovery contract for the correction of exactly
six `可攜核心` cells in
`docs/agent-skills-convergence/cross-language-candidate-basis.md`. The bounded
candidate edit was committed in `75676e2f472abeb04a034ab765f1973d6b4dfcf5`
and force-pushed to the current head of ready-for-review PR #125. The repaired
planning contract was review-approved and Phase 4.5 / publication completed.
New PR-head feedback now routes the open PR to `needs-rework`; this planning
repair is independently Plan-Reviewer approved. It makes no claim that the
feedback, threads, clean observation, human merge handoff, merge, release, or
topic close has completed.

## Scope

- **In scope**:
  - Keep the parent and correction progression artifacts synchronized with the
    recovery chronology, completed Phase 4.5 / publication, the open ready PR
    #125, and its current `needs-rework` route.
  - Retain the bounded independent-Implementer edit, committed in `75676e2`, of only the
    `可攜核心` cells for `python-tdd-test-authoring`,
    `python-testing-pytest`, `python-implementation-review`,
    `python-error-handling`, `python-serialization-boundaries`, and
    `boundary-outcome-design`.

- **Out of scope**:
  - Changing the 11-candidate set, its four groups, the other five candidate
    rows, Python evidence, Swift or TypeScript appendices, names, links, or
    paths.
  - Reading or claiming validation of Swift or TypeScript projects; reopening
    `python-code-review` historical remediation; skill-path migration;
    platform-directory changes; creator/reviewer/template path transition;
    workflow-to-agent binding; runtime orchestration; README, VERSION, release,
    tag, or platform-surface work.

## Locked Decisions

- `AGENTS.md` and `docs/repo-positioning.md` govern this topic; `skills/` is
  canonical. `agents/` is canonical only for its bounded repo-defined workflow
  artifacts. `.github/**`, `.codex/**`, and all other platform surfaces remain
  unchanged compatibility surfaces.
- The sole existing-file write for the bounded candidate correction is
  `docs/agent-skills-convergence/cross-language-candidate-basis.md`, and only
  the six named `可攜核心` cells may change. Any write outside this set requires
  plan repair before implementation.
- `python-tdd-test-authoring`: perform D1 first; when trivial, emit
  `skip_with_reason` and stop. Only non-trivial work maps approved behavior to
  tests and requires a `RED`, `ready`, or `blocked` result.
- `python-testing-pytest`: use inline-first tests. Extract reusable setup only
  for real reuse, shared preconditions, or clear noise reduction. Use
  data-driven / parameterized cases only when behavior is the same and data
  changes.
- `python-implementation-review`: retain traceability to approved plan steps,
  Non-goals, and public contracts; additionally verify that test cases in the
  approved Test Plan materially exist. Do not restore Python-specific review
  ordering or workflow ownership.
- `python-error-handling`: distinguish known business/package failures from
  programmer misuse or obvious bugs. Translate only known, controllable
  failures once at a meaningful boundary and retain the cause.
- `python-serialization-boundaries`: omitted, explicit null, and unchanged
  semantics apply only to PATCH-like partial input. Deep conversion applies
  only where the boundary promises an internal object or typed record.
- `boundary-outcome-design`: define the boundary contract and vocabulary owner
  before preserve / translate / compress. Distinguish expected, unexpected,
  and not-failure; translate external HTTP / SDK / ORM / driver vocabulary at
  Adapter / Port boundaries into receiving-layer capability vocabulary; never
  compress unexpected failure into an ordinary expected outcome.
- This is a non-stable topic: `README.md` and `VERSION` do not change; no
  release or tag action exists.
- This recovery records high-severity phase and role-separation drift. The
  removed pre-recovery implementation remains suspect and is not certified by
  this contract. The committed six-cell edit in `75676e2` is a later, bounded
  independent-Implementer output; it is not a resurrection or certification of
  that removed implementation.

## Boundaries / Exclusions

- The Plan-Creator owns the planning and correction artifacts. An independent
  Plan-Reviewer owns the plan-review gate; Plan-Creator records its delivered
  handoff. Only after approval may an
  independent Implementer own the six-cell document edit; an independent
  Reviewer owns its later review. Main Agent owns branch, publication, PR, and
  post-merge routing.
- The parent plan is the future execution-facing current truth; the parent step
  is progression truth only. The correction plan and correction step explain
  the high-severity recovery history and never replace the parent contract.
- The recovery chronology is: baseline `a725e71fd8cbe9ce6fb35fbf85ac7e250f878feb`;
  independent Plan-Reviewer approval recorded in
  `4235c92a8d8bc09f86a2a3a37a0e1bbb5e85df34`; independent-Implementer
  completion and commit of the six-cell candidate edit in
  `75676e2f472abeb04a034ab765f1973d6b4dfcf5`;
  and independent document Code-Reviewer approval of that bounded edit.
  The fresh independent Plan-Reviewer handoff has approved the repaired
  planning contract. Independent final Code-Reviewer revalidation and Planner
  alignment completed Phase 4.5; Main Agent then committed and force-pushed
  `75676e2` to ready PR #125. New feedback on that PR routes the topic to
  `needs-rework`; the independent Plan-Reviewer has approved the resulting
  PR-loop planning repair.
- There is no claim that PR threads are resolved, that a clean observation was
  completed, that human merge handoff was selected, or that merge, release,
  summary, or topic completion occurred.
- A Plan-Reviewer finding of scope, contract, or workflow drift returns only to
  Plan-Creator. A later document-review finding returns only to the independent
  Implementer. Neither route reopens the locked scope.

## Status / Allowed Transitions

- **Current**: `needs-rework`. The baseline and fresh independent
  Plan-Reviewer handoffs, independent document Code-Reviewer approval, and
  final independent Code-Reviewer / Planner alignment are recorded in the
  recovery chronology. Phase 4.5 and publication completed with
  `75676e2` force-pushed to ready PR #125. Newly observed PR-head feedback is
  actionable and routes the open PR to `needs-rework`; the independent
  Plan-Reviewer has approved the PR-loop planning repair. Its coverage and
  resolution remain unclaimed.
- **Execution model**: canonical creator -> reviewer -> publish -> PR loop ->
  human merge handoff path. Planning review is a hard pre-implementation gate
  and does not replace later independent review of document changes.
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
  - `pr-open` -> `needs-rework`
  - `pr-open` -> `merged`
  - `merged` -> terminal
- **Routing notes**: Phase 4.5 and candidate publication are complete. The
  independent Plan-Reviewer approved this PR-loop contract repair. Main Agent
  must first commit and push that bounded planning-only repair. After that
  publication, an independent Reviewer verifies thread coverage from a fresh
  PR snapshot before any reply, resolution, or feedback-driven implementation.
  In Phase 7--8, Main Agent fetches PR reviews and
  review state, review comments and threads, issue comments, and check runs
  after the PR is ready and after each relevant change. New actionable feedback
  routes to `needs-rework`; all actionable thread coverage must be established
  before bounded observation begins. Main Agent replies to and resolves a
  thread only when its applicable outcome is actually satisfied; every other
  actionable or unresolved blocking thread remains a blocker. Direct-apply
  work is limited to three iterations; feedback that changes logic, scope,
  requirements, boundaries, or
  the locked contract returns to independent review. Only three consecutive
  clean snapshots at `30s -> 60s -> 120s` permit a bounded clean-observation
  report for human merge-readiness confirmation. A ready or draft PR never
  directly enters human merge handoff.

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Parent topic plan | `plan/cross-language-skill-candidate-basis-content-corrections/cross-language-skill-candidate-basis-content-corrections.plan.md` | Plan-Creator | Execution-facing current-truth contract and frozen scope. |
| Parent progression | `plan/cross-language-skill-candidate-basis-content-corrections/cross-language-skill-candidate-basis-content-corrections.step.md` | Plan-Creator, then Main Agent | Progression truth; it does not approve or close the topic. |
| Correction plan | `plan/cross-language-skill-candidate-basis-content-corrections/cross-language-skill-candidate-basis-content-corrections.correction-plan.md` | Plan-Creator | Historical-truth record of high-severity recovery direction. |
| Correction progression | `plan/cross-language-skill-candidate-basis-content-corrections/cross-language-skill-candidate-basis-content-corrections.correction-step.md` | Plan-Creator, then Main Agent | Historical recovery progression; it cannot replace parent current truth. |
| Plan-review log | `plan/cross-language-skill-candidate-basis-content-corrections/cross-language-skill-candidate-basis-content-corrections.review-log.md` | Plan-Creator | Preserved reviewer-handoff history and current routing; it records no invented verdict. |
| Candidate basis | `docs/agent-skills-convergence/cross-language-candidate-basis.md` | Independent Implementer | Sole existing-file write, completed in `75676e2` and limited to the six locked `可攜核心` cells. |

Artifact path notes:

- `README.md`, `VERSION`, `.github/copilot-instructions.md`, `skills/**`,
  `agents/**`, `.github/**`, and `.codex/**` are not write paths.
- The plan-review log preserves the baseline Plan-Reviewer approval and the
  later Phase 4.5 rework route. No summary artifact exists; topic-close
  conditions must add its exact path before a summary can be created.
- Future work outside this table is a plan-alignment failure and must return to
  Plan-Creator before continuing.

## Implementation Steps

1. Plan-Creator synchronizes the parent plan, parent step, correction plan,
   correction step, and review log with the verified recovery chronology and
   keeps the frozen write boundary unchanged.
2. Independent Plan-Reviewer approves the PR-loop planning repair with one
   JSON handoff, recorded by Plan-Creator. Main Agent then commits and pushes
   only that planning repair; an independent Reviewer next verifies thread
   coverage from fresh PR state. No candidate edit, thread response, thread
   resolution, merge, or release is performed by this planning step.

## Validation / Acceptance Checks

- Verify the planning/progression artifacts state the exact recovery chronology:
  baseline `a725e71`, its recorded independent Plan-Reviewer approval in
  `4235c92`, the committed and force-pushed six-cell implementation in
  `75676e2`, independent document Code-Reviewer approval, and completed Phase
  4.5 / publication.
- Verify all required plan sections, exact paths, non-stable intent, semantic
  warning, role separation, parent/current-truth versus correction/historical-
  truth separation, and canonical transitions.
- Verify all six locked cell requirements and every exclusion are preserved
  verbatim in execution meaning.
- Verify the review log preserves the independent baseline and fresh
  Plan-Reviewer `approved` handoffs, preserves the later document-review fact,
  records the committed / force-pushed PR fact, the approved PR-loop planning
  repair, and current `needs-rework` routing, and does not claim thread
  resolution, clean observation, human merge handoff, merge, summary, or
  Swift/TypeScript validation.
- Verify Phase 7--8 requires a complete fresh fetch of reviews / review state,
  review comments and threads, issue comments, and checks; routes new feedback
  to `needs-rework`; requires actionable-thread coverage; then uses exactly
  three clean observations (`30s -> 60s -> 120s`) before producing only a
  bounded clean-observation report for a human decision.

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

Before a human manually merges PR #125, the bounded clean-observation report
must be complete and a human must explicitly choose merge handoff. That choice
is STOP POINT 2: Main Agent stops immediately before any actual human merge and
does not poll or infer merge completion. Phase 9 is permitted only after a new,
explicit human resume that both confirms the merge occurred and authorizes
post-merge work. This topic has no README, VERSION, release, or tag action.

## Open Questions / Unresolved Items

- None. The absent analysis layer is a semantic warning, not an invitation to
  infer additional scope.
