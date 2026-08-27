# Cross-Language Skill Candidate Basis — Topic Plan

## Analysis-layer routing

**Semantic warning — optional analysis layer absent:** neither
`analysis/cross-language-skill-candidate-basis/requirements.md` nor
`analysis/cross-language-skill-candidate-basis/technical-spec.md` exists.
This plan follows the explicit human-approved topic boundary. If either
analysis artifact is introduced, stop and reconcile its authority before
changing this plan or implementing the candidate-basis document.

## Goal / Outcome

- Establish a prospective, repository-visible historical-remediation baseline
  for governance and acceptance of the fixed current 11-candidate tree.
- Preserve, but do not retrospectively certify or re-execute,
  `python-code-review`'s historically unproven repair in `c285c3a`.

## Scope

- **In scope**:
  - Author only the five parent/correction planning artifacts listed in
    `Artifact Paths` as the prospective baseline.
  - Govern only the locked four groups and 11 candidates:
    - Testing and validation: `python-tdd-test-authoring`,
      `python-testing-pytest`, `python-implementation-review`.
    - Code review: `python-code-review`.
    - Design boundaries: `semantic-first-design`, `boundary-outcome-design`,
      `python-error-handling`, `python-serialization-boundaries`.
    - Coding style: `python-naming`, `python-control-flow`,
      `python-docstrings`.
  - Require Main Agent Phase 2 validation, a five-path baseline commit/push,
    then a separate review-log verdict commit/push.

- **Out of scope**:
  - Editing, moving, deleting, renaming, publishing, or projecting any skill
    or candidate document.
  - Re-executing, certifying, or otherwise repairing the historical
    `python-code-review` implementation authorization.
  - Assessing Python runtime/toolchain, project-lifecycle, object-model,
    syntax-specific, API/module, or async skills beyond the locked 11.
  - Verifying an unprovided Swift or TypeScript repository, or claiming such
    validation occurred.
  - Changing Phase 1 artifacts, platform surfaces, `README.md`, `VERSION`,
    workflow contracts, runtime behavior, or historical branch/PR history.

## Locked Decisions

- This is a review-ready-only, non-stable topic: no `README.md`, `VERSION`,
  release, or tag action applies.
- The candidate model remains **generic core + language appendix**. Swift and
  TypeScript entries are future validation or blocker statements, not asserted
  project evidence.
- The `python-code-review` portable-core repair in `c285c3a` remains in the
  current tree as historical remediation. The preceding committed correction
  contract did not authorize it, so it remains historically suspect. A future
  compliant route may accept governance of the current tree only; it cannot
  provide retrospective authorization.
- Recovery is additive: do not amend, rebase, reset, force-push, delete, or
  rewrite existing commits or the open PR.
- **ReadOnly** inputs are `AGENTS.md`, `docs/repo-positioning.md`,
  `plan/agent-handoff-workflow.md`, `plan/topic-plan-contract.md`,
  `docs/agent-skills-convergence/phase-1/**`,
  `docs/agent-skills-convergence/phase-3/projection-adapter-design.md`, and
  the 11 listed candidate `skills/<candidate>/SKILL.md` files.
- The published prospective baseline is `62e8c1f`, whose first commit contains
  exactly the five parent/correction planning artifacts and excludes the review
  log. The next package is an additive **state-sync package** containing only
  the parent plan, parent progression, parent summary, and correction
  progression; it records the already-published Phase 2 evidence and
  `reviewer-in-progress` handoff. **Modify** outside those four paths is
  prohibited; **Deleted** paths are none.
- Main Agent must commit and push the state-sync package before another
  independent Plan-Reviewer appends one canonical JSON verdict to the existing
  review log. Main Agent then owns a separate, verdict-only commit/push. The
  review log is excluded from the state-sync package.

## Boundaries / Exclusions

- Plan-Creator owns authorship of the state-sync package. The preceding
  five-path prospective baseline was published by Main Agent as `62e8c1f`.
- Main Agent owns publication of the state-sync package, then routes its
  published current truth to the independent Plan-Reviewer. Dispatcher cannot
  substitute for this publication ownership.
- Only after the state-sync package is committed and pushed may an independent
  Plan-Reviewer append its canonical JSON verdict to the existing review log.
  Main Agent owns the subsequent verdict-only commit/push. That verdict reviews
  prospective current-tree governance and must state that historical
  `python-code-review` remediation remains suspect in its
  `copilot_feedback_triage.DISCUSS` entry.
- Planner alone determines correction closure. Closure requires future
  compliance and explicit retention of the historical limitation; it must not
  re-label the old repair as historically authorized.
- Existing Phase 1 artifacts remain read-only historical evidence. `skills/`
  remains canonical; `.github/**`, `.codex/**`, and other platform surfaces are
  compatibility surfaces and remain excluded.

## Status / Allowed Transitions

- **Current**: `reviewer-in-progress`. Main Agent directly completed the
  recorded Phase 2 check and published the five-path prospective baseline as
  `62e8c1f`; the parent progression, correction progression, and summary carry
  the same current state. No new approval or PR thread resolution is claimed.
- **Required route after `62e8c1f`**: Main Agent first commits and pushes the
  exact four-path state-sync package -> independent Plan-Reviewer appends only
  its canonical JSON verdict to the existing review log -> Main Agent creates
  and pushes the second, verdict-only commit -> verdict routes to `approved` or
  `needs-rework`.
- **Allowed transitions**:
  - `planned` -> `creator-in-progress`
  - `creator-in-progress` -> `review-ready`
  - `review-ready` -> `reviewer-in-progress`
  - `reviewer-in-progress` -> `approved`
  - `reviewer-in-progress` -> `needs-rework`
  - `needs-rework` -> `creator-in-progress`
  - `approved` -> `publish-in-progress`
  - `publish-in-progress` -> `pr-open`
  - `pr-open` -> `needs-rework|merged`
  - `merged` -> terminal
- **Stop rule**: any staged state-sync path outside its exact four-path package,
  any verdict-commit path outside the review log, or a verdict that certifies
  the historical repair routes to `needs-rework`. No thread is resolved by this
  synchronization.

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/cross-language-skill-candidate-basis/cross-language-skill-candidate-basis.plan.md` | Plan-Creator | Current prospective execution contract |
| Topic progression | `plan/cross-language-skill-candidate-basis/cross-language-skill-candidate-basis.step.md` | Plan-Creator; Main Agent | Current workflow progression |
| Topic close summary | `plan/cross-language-skill-candidate-basis/cross-language-skill-candidate-basis.summary.md` | Plan-Creator; Main Agent | Current handoff and close truth |
| Correction plan | `plan/cross-language-skill-candidate-basis/cross-language-skill-candidate-basis.correction-plan.md` | Plan-Creator; Planner | Historical remediation contract |
| Correction progression | `plan/cross-language-skill-candidate-basis/cross-language-skill-candidate-basis.correction-step.md` | Plan-Creator; Main Agent; Planner | Correction-gate sequencing and Phase 2 requirements |
| Review routing log | `plan/cross-language-skill-candidate-basis/cross-language-skill-candidate-basis.review-log.md` | Plan-Reviewer (verdict only); Main Agent (publisher) | Separate second-commit JSON verdict |
| Candidate-basis document | `docs/agent-skills-convergence/cross-language-candidate-basis.md` | Existing historical artifact | Read-only fixed candidate inventory |

Artifact path notes:

- `62e8c1f` is the already-published first baseline commit and contains the
  five paths before `review-log.md`.
- The next state-sync package contains exactly the topic plan, topic
  progression, topic close summary, and correction progression. The correction
  plan remains historical evidence and is excluded from this package; the
  review log is also excluded.
- Only after that state-sync package is pushed may Plan-Reviewer append the
  review-log verdict. Main Agent's immediately following verdict-only commit
  contains only `review-log.md`; the state-sync package commit must be its
  ancestor.
- No other artifact is authorized by this correction route. If a needed action
  falls outside this table, stop and repair the plan.

## Implementation Steps

1. Synchronize only the four state-sync artifacts named in `Artifact path
   notes` with the already-published `62e8c1f` Phase 2 and
   `reviewer-in-progress` state.
2. State the historical `python-code-review` limitation as a fixed fact without
   changing the candidate document, re-executing its repair, or asserting
   retrospective authorization.
3. Hand the bounded state-sync package to Main Agent for its publisher-owned
   commit/push, then the independent review-log-only and verdict-only route.

## Validation / Acceptance Checks

- Exactly 11 candidates remain once each in the four locked groups.
- `62e8c1f` remains the published five-path prospective baseline; no claim
  changes its historical or scope-limited meaning.
- The next state-sync commit contains exactly the four artifacts specified in
  `Artifact path notes`, is pushed before another review begins, and excludes
  both the correction plan and review log.
- The independent Plan-Reviewer appends only the canonical JSON verdict after
  the state-sync commit is published; Main Agent's next commit contains only
  that review-log update, with the state-sync commit as its ancestor.
- The Plan-Reviewer verdict covers prospective governance of the fixed tree,
  uses the canonical JSON shape, and includes in
  `copilot_feedback_triage.DISCUSS` that the historical
  `python-code-review` remediation remains suspect.
- A Planner closure decision verifies future compliant routing without claiming
  that `c285c3a` was historically authorized.
- No PR thread is resolved without evidence specific to that thread.

## Reviewer Handoff

```json
{
  "verdict": "approved|needs-rework",
  "blocking_issues": [],
  "copilot_feedback_triage": {
    "ADDRESS": [],
    "DISCUSS": [
      "Historical python-code-review remediation remains suspect; this verdict evaluates prospective current-tree governance only."
    ],
    "SKIP": []
  }
}
```

## Post-merge / release actions

- No repository release action, tag, `README.md` update, or `VERSION` bump is
  required.
- After human merge handoff, STOP POINT 2 applies. Main Agent must stop until a
  new explicit human resume message.

## Open Questions / Unresolved Items

- No implementation question is open. Historical compliance of the
  `python-code-review` repair is deliberately not reopened; its limitation is
  locked as a fact for future governance and Planner closure.
