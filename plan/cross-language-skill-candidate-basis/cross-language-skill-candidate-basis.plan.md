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
- **Written** for the first prospective baseline commit is exactly the five
  planning artifacts in this plan's `Artifact Paths`, excluding the review log.
  **Modify** outside those five paths is prohibited; **Deleted** paths are none.
- The review log is written only after the first baseline commit, by
  Plan-Reviewer as one JSON verdict. Main Agent owns its separate commit/push.

## Boundaries / Exclusions

- Plan-Creator owns authorship of the five-path prospective baseline.
- Main Agent directly owns Phase 2 branch/worktree validation, the first
  five-path baseline commit/push, routing to `reviewer-in-progress`, and the
  second review-log-only commit/push. Dispatcher cannot substitute for Phase 2
  validation or publication ownership.
- Only after the first commit exists may an independent Plan-Reviewer append
  its canonical JSON verdict to the existing review log. That verdict reviews
  current-tree governance and must state that historical `python-code-review`
  remediation remains suspect in its `copilot_feedback_triage.DISCUSS` entry.
- Planner alone determines correction closure. Closure requires future
  compliance and explicit retention of the historical limitation; it must not
  re-label the old repair as historically authorized.
- Existing Phase 1 artifacts remain read-only historical evidence. `skills/`
  remains canonical; `.github/**`, `.codex/**`, and other platform surfaces are
  compatibility surfaces and remain excluded.

## Status / Allowed Transitions

- **Current**: `review-ready`. Plan-Creator prepared the prospective five-path
  baseline; no new Main Agent validation, commit, push, reviewer transition, or
  verdict is claimed.
- **Required route**: Main Agent directly validates Phase 2 -> creates and
  pushes first five-path baseline commit -> routes `review-ready` ->
  `reviewer-in-progress` -> Plan-Reviewer writes review-log JSON only -> Main
  Agent creates and pushes second review-log-only commit -> verdict routes to
  `approved` or `needs-rework`.
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
- **Stop rule**: any pending path outside the five-path baseline, a dirty or
  untracked disposition outside it, or a verdict that certifies the historical
  repair routes to `needs-rework`. No thread is resolved by this synchronization.

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

- The five paths before `review-log.md` are the exact first-commit set. The
  review log is excluded from that commit and appears only in the separate
  second commit after independent review.
- The first commit must be an ancestor of the review-log verdict commit.
- No other artifact is authorized by this correction route. If a needed action
  falls outside this table, stop and repair the plan.

## Implementation Steps

1. Write only the five parent/correction planning artifacts in `Artifact Paths`.
2. State the historical `python-code-review` limitation as a fixed fact without
   changing the candidate document, re-executing its repair, or asserting
   retrospective authorization.
3. Hand the bounded five-path diff to Main Agent for its direct Phase 2 check
   and publisher-owned two-commit route.

## Validation / Acceptance Checks

- Exactly 11 candidates remain once each in the four locked groups.
- No candidate document, skill, platform surface, Phase 1 artifact, README,
  VERSION, workflow contract, or review log is in the first commit.
- Main Agent's direct Phase 2 check confirms branch/HEAD, exact five-path diff,
  and no untracked or unrelated modification before the first commit.
- The first commit contains exactly the five planning artifacts; the second
  contains only the Plan-Reviewer review-log JSON, and the first is its
  ancestor.
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
