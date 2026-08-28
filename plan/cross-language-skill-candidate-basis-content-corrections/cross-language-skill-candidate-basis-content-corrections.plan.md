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

Establish a clean, reviewable recovery baseline for a future correction of
exactly six `可攜核心` cells in
`docs/agent-skills-convergence/cross-language-candidate-basis.md`. Before an
independent Plan-Reviewer approves this baseline, no candidate-basis edit is
authorized.

## Scope

- **In scope**:
  - Establish the four listed planning and correction artifacts for this
    recovery baseline, then record the independent Plan-Reviewer handoff in
    the listed review log.
  - After the separate Plan-Reviewer gate, allow an independent Implementer to
    edit only the `可攜核心` cells for `python-tdd-test-authoring`,
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
- The sole future existing-file write is
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
- This recovery baseline records high-severity phase and role-separation drift
  prospectively. It does not certify the removed implementation or any prior
  review as current truth.

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
- The recovery-baseline commit added only the parent plan, parent step,
  correction plan, and correction step. The later Plan-Reviewer approval is
  recorded separately. There is no candidate-basis implementation commit,
  push, PR or force-push, merge, release, document review, Phase 4.5 result,
  summary, or completion claim.
- A Plan-Reviewer finding of scope, contract, or workflow drift returns only to
  Plan-Creator. A later document-review finding returns only to the independent
  Implementer. Neither route reopens the locked scope.

## Status / Allowed Transitions

- **Current**: `approved`. The independent Plan-Reviewer approved recovery
  baseline `a725e71fd8cbe9ce6fb35fbf85ac7e250f878feb`; the review log preserves
  the exact handoff. Candidate implementation has not started. The next actor
  is an independent Implementer.
- **Execution model**: canonical creator -> reviewer -> publish -> merge path,
  stopping after merge; no release transition applies. Planning review is a
  hard pre-implementation gate and does not replace later independent review
  of the document edit.
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
- **Routing notes**: recovery chronology is prospective: independent
  Plan-Reviewer review; bounded six-cell implementation only after approval;
  independent document review; Phase 4.5 alignment; then, only with STOP POINT
  1 authorization, publication and PR. STOP POINT 2 applies after merge.

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Parent topic plan | `plan/cross-language-skill-candidate-basis-content-corrections/cross-language-skill-candidate-basis-content-corrections.plan.md` | Plan-Creator | Execution-facing current-truth contract and frozen scope. |
| Parent progression | `plan/cross-language-skill-candidate-basis-content-corrections/cross-language-skill-candidate-basis-content-corrections.step.md` | Plan-Creator, then Main Agent | Progression truth; it does not approve or close the topic. |
| Correction plan | `plan/cross-language-skill-candidate-basis-content-corrections/cross-language-skill-candidate-basis-content-corrections.correction-plan.md` | Plan-Creator | Historical-truth record of high-severity recovery direction. |
| Correction progression | `plan/cross-language-skill-candidate-basis-content-corrections/cross-language-skill-candidate-basis-content-corrections.correction-step.md` | Plan-Creator, then Main Agent | Historical recovery progression; it cannot replace parent current truth. |
| Plan-review log | `plan/cross-language-skill-candidate-basis-content-corrections/cross-language-skill-candidate-basis-content-corrections.review-log.md` | Plan-Creator | Exact delivered independent Plan-Reviewer handoff and next-actor routing. |
| Candidate basis | `docs/agent-skills-convergence/cross-language-candidate-basis.md` | Independent Implementer after Plan-Reviewer approval | Sole future existing-file write, limited to the six locked `可攜核心` cells. |

Artifact path notes:

- `README.md`, `VERSION`, `.github/copilot-instructions.md`, `skills/**`,
  `agents/**`, `.github/**`, and `.codex/**` are not write paths.
- The plan-review log records only the completed independent Plan-Reviewer
  gate. No summary artifact exists; topic-close conditions must add its exact
  path before a summary can be created.
- Future work outside this table is a plan-alignment failure and must return to
  Plan-Creator before continuing.

## Implementation Steps

1. Independent Plan-Reviewer evaluated recovery baseline
   `a725e71fd8cbe9ce6fb35fbf85ac7e250f878feb` and returned `approved`; the
   plan-review log preserves its exact handoff.
2. An independent Implementer next commits the review record and synchronized
   progression, then updates the
   six locked `可攜核心` cells and no other existing file.
3. Independent Reviewer evaluates the bounded document diff against this
   frozen parent contract. Phase 4.5 routing and all publication actions remain
   outside creator and reviewer implementation work.

## Validation / Acceptance Checks

- Verify that this baseline adds exactly the four planning artifacts listed
  above and does not modify the candidate-basis document or any other existing
  file.
- Verify all required plan sections, exact paths, non-stable intent, semantic
  warning, role separation, parent/current-truth versus correction/historical-
  truth separation, and canonical transitions.
- Verify all six locked cell requirements and every exclusion are preserved
  verbatim in execution meaning.
- Verify the review log preserves the independent Plan-Reviewer `approved`
  handoff for the recovery baseline and does not claim candidate
  implementation, document review, Phase 4.5, publication, summary,
  completion, or Swift/TypeScript validation.
- Verify Plan-Reviewer approval is required before any candidate-basis edit;
  scope, contract, or workflow drift is blocking and conservatively returns to
  the owning role.

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

After merge, STOP POINT 2 requires explicit human resume for any separate
follow-up. This topic has no README, VERSION, release, or tag action.

## Open Questions / Unresolved Items

- None. The absent analysis layer is a semantic warning, not an invitation to
  infer additional scope.
