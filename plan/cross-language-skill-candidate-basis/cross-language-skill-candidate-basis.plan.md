# Cross-Language Skill Candidate Basis — Topic Plan

## Analysis-layer routing

**Semantic warning — optional analysis layer absent:** neither
`analysis/cross-language-skill-candidate-basis/requirements.md` nor
`analysis/cross-language-skill-candidate-basis/technical-spec.md` exists.
This plan is based on the explicit human-approved topic boundary. If either
analysis artifact is introduced, stop and reconcile its authority before
changing this plan or implementing the candidate-basis document.

## Goal / Outcome

- Recover a trustworthy, repository-visible execution baseline for the existing
  11-candidate inventory topic without rewriting its history.
- After the recovery gates pass, allow an independent Implementer to make only
  the bounded candidate-document correction required by the fixed scope.

## Scope

- **In scope**:
  - Create the high-severity recovery contract and progression artifacts listed
    in `Artifact Paths`, and synchronize the four parent truth artifacts.
  - Evaluate only these four groups and their 11 candidates:
    - Testing and validation: `python-tdd-test-authoring`,
      `python-testing-pytest`, `python-implementation-review`.
    - Code review: `python-code-review`.
    - Design boundaries: `semantic-first-design`, `boundary-outcome-design`,
      `python-error-handling`, `python-serialization-boundaries`.
    - Coding style: `python-naming`, `python-control-flow`,
      `python-docstrings`.
  - Correct only the missing committed planning baseline, missing Phase 2
    branch/worktree readiness gate, and Python-specific ordering in
    `python-implementation-review`'s portable core.

- **Out of scope**:
  - Editing, moving, deleting, renaming, publishing, or projecting any skill.
  - Assessing Python runtime/toolchain, project-lifecycle, object-model,
    syntax-specific, API/module, or async skills beyond the locked 11.
  - Verifying an unprovided Swift or TypeScript repository, or claiming such
    validation occurred.
  - Amending, rebasing, resetting, force-pushing, merging, releasing, or
    rewriting the existing PR/commit history.
  - Changing existing Phase 1 artifacts, platform surfaces, `README.md`,
    `VERSION`, workflow contracts, or runtime behavior.

## Locked Decisions

- This is a review-ready-only, non-stable topic: it does not affect the stable
  library and has no `README.md`, `VERSION`, release, or tag action.
- The candidate model is **generic core + language appendix**. A candidate may
  be routed as blocked or deferred; none is presumed portable merely because it
  appears in this inventory.
- Swift and TypeScript entries describe required future validation or blockers,
  not asserted repository evidence.
- The prior commit, push, PR opening, and approval entries are historical facts
  but are **suspect for workflow compliance**. They must never be represented
  as evidence that the original sequence satisfied its prerequisite gates.
- Recovery is additive: create and commit this recovery baseline, retain the
  open PR, and never amend, rebase, reset, or force-push history.
- **ReadOnly** inputs are exactly:
  - `AGENTS.md`; `docs/repo-positioning.md`;
    `plan/agent-handoff-workflow.md`; and `plan/topic-plan-contract.md`.
  - `docs/agent-skills-convergence/phase-1/**` and
    `docs/agent-skills-convergence/phase-3/projection-adapter-design.md`.
  - The 11 candidate `skills/<candidate>/SKILL.md` files named in `Scope`.
- **Written now** is exactly the six planning/correction artifacts listed in
  `Artifact Paths`. The existing candidate document is read-only during this
  Plan-Creator pass; a later Implementer may edit only its one bounded portable
  core entry after all recovery gates pass.
- **Modify** outside those exact paths is prohibited. **Deleted** paths are
  none. If an additional path becomes necessary, stop and repair this plan.

## Boundaries / Exclusions

- Plan-Creator owns the parent planning artifacts and correction artifacts in
  this pass. Plan-Reviewer independently reviews the committed recovery
  baseline. Dispatcher records gate evidence and routes work. Implementer only
  performs the frozen candidate-document repair. Reviewer independently checks
  that repair. Main Agent owns PR transport and thread resolution, but no actor
  may treat this recovery plan as authority to alter history.
- Existing Phase 1 artifacts remain historical evidence and are not modified,
  reinterpreted as implementation authorization, or extended by this topic.
- `skills/` remains the canonical source; `.github/**`, `.codex/**`, and other
  platform surfaces remain out of scope compatibility surfaces.
- Any request to select a final cross-language architecture, change a candidate
  name/path, or begin language-specific implementation is a separately scoped
  follow-up topic.
- Parent plan, step, review log, and summary are current truth. The correction
  artifacts explain recovery and remain historical truth; they do not replace
  the parent contract after parent sync.

## Status / Allowed Transitions

- **Current**: `needs-rework` — recovery pending. The PR remains open, but the
  prior execution and approvals are historical/suspect until this recovery
  baseline is committed and independently reviewed.
- **Pre-creator Phase 2 gate**: this is a Status/Gate prerequisite, not an
  `Implementation Steps` item. Before `needs-rework` ->
  `creator-in-progress`, the recovery baseline must be committed, an independent
  Plan-Reviewer must return `approved`, and Dispatcher must record the actual
  branch, HEAD, worktree path, clean `git status`, untracked-file disposition,
  and baseline SHA in the correction step. Missing or non-clean evidence keeps
  the topic at `needs-rework`.
- **Execution model**: canonical creator -> reviewer -> publish -> merge path;
  `pr-open` retains the canonical PR feedback loop until merge handoff. This
  topic has no release transition.
- **Allowed transitions**:
  - `planned` -> `creator-in-progress`
  - `creator-in-progress` -> `review-ready`
  - `review-ready` -> `reviewer-in-progress`
  - `reviewer-in-progress` -> `approved`
  - `reviewer-in-progress` -> `needs-rework`
  - `needs-rework` -> `creator-in-progress` (only after the pre-creator Phase 2 gate)
  - `approved` -> `creator-in-progress`
  - `approved` -> `publish-in-progress`
  - `publish-in-progress` -> `pr-open`
  - `publish-in-progress` -> `merged`
  - `pr-open` -> `needs-rework`
  - `pr-open` -> `merged`
  - `merged` -> terminal
- **Routing note**: after implementation review approval, Main Agent performs
  Phase 4.5 plan-contract alignment. Any path, contract, scope, or workflow
  drift routes to `creator-in-progress`; it does not reopen the locked candidate
  set or invent a new language architecture.
- **Recovery route**: the Planner has frozen all three findings as high-severity
  correction. Only passed correction acceptance and independent re-review can
  return the parent artifacts to execution-facing current truth.

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/cross-language-skill-candidate-basis/cross-language-skill-candidate-basis.plan.md` | Plan-Creator | Current execution contract and locked write boundary |
| Topic progression | `plan/cross-language-skill-candidate-basis/cross-language-skill-candidate-basis.step.md` | Plan-Creator; then Dispatcher | Current workflow-stage and gate truth |
| Review routing log | `plan/cross-language-skill-candidate-basis/cross-language-skill-candidate-basis.review-log.md` | Plan-Reviewer; Reviewer; Planner | Separate independent verdict entries and recovery-routing trail |
| Topic close summary | `plan/cross-language-skill-candidate-basis/cross-language-skill-candidate-basis.summary.md` | Plan-Creator; then Main Agent | Current PR/recovery handoff truth, then close outcome |
| Correction plan | `plan/cross-language-skill-candidate-basis/cross-language-skill-candidate-basis.correction-plan.md` | Plan-Creator; Planner | Historical high-severity correction contract |
| Correction progression | `plan/cross-language-skill-candidate-basis/cross-language-skill-candidate-basis.correction-step.md` | Plan-Creator; then Dispatcher | Historical correction-gate evidence and sequencing |
| Candidate-basis document | `docs/agent-skills-convergence/cross-language-candidate-basis.md` | Implementer | Evidence-backed 11-candidate inventory for human review |

Artifact path notes:

- This topic does not modify `README.md`, `VERSION`, `.github/copilot-instructions.md`,
  `skills/**`, `.github/**`, or `.codex/**`.
- The four parent planning paths and two correction paths are the only
  Plan-Creator writes in this recovery pass. The candidate document remains a
  later Implementer-only repair after its required gates.
- Plan-Reviewer and Reviewer each append only their own distinct verdict entry
  to the review log; neither role overwrites, approves, or reuses the other
  role's verdict.
- If a required action falls outside this table, stop and repair this plan.
  Correction artifacts are retained; deletion is forbidden.

## Implementation Steps

1. After the pre-creator Phase 2 gate, the independent Implementer re-reads the
   committed recovery baseline, correction artifacts, and locked candidate
   evidence.
2. Implementer edits only
   `docs/agent-skills-convergence/cross-language-candidate-basis.md`: the
   `python-implementation-review` portable core must state plan-alignment
   verification without a universal review/test ordering; retain any ordering
   only as Python evidence or a language-bound blocker.
3. Implementer verifies the fixed 11-candidate scope and returns
   `review-ready` for independent Reviewer re-review. The Implementer must not
   change planning artifacts, correction evidence, history, or PR threads.

## Validation / Acceptance Checks

- Exactly 11 candidates appear once each, within the four locked groups.
- Each candidate states a non-Python-specific portable core and distinct Python,
  Swift, and TypeScript treatment; Swift/TypeScript claims are marked as
  appendix needs or blockers unless evidence is present in the locked inputs.
- No portable-core entry relies on Python syntax, `pytest`, `pyproject.toml`, or
  Python runtime/toolchain rules.
- The candidate-basis document makes no path migration, projection, runtime,
  workflow-binding, implementation, or stable-library recommendation.
- Only paths listed in `Artifact Paths` are changed, no pre-existing tracked
  path is modified or deleted, and existing Phase 1 files remain unchanged.
- The plan and step artifact retain canonical sections and transitions; the
  Plan-Reviewer handoff and later Reviewer handoff use the fixed JSON shape.
- Independent review confirms no scope, contract, workflow, or authority drift
  before publication; publication still requires STOP POINT 1 human approval.
- While `pr-open`, Main Agent triages PR review comments, issue comments, and
  checks. Actionable findings route to `needs-rework`; STOP POINT 2 applies
  only after merge handoff.
- The correction plan records three high-severity issues, fixed 11-candidate
  scope, no-history-rewrite rule, acceptance criteria, and required re-reviews.
- The correction step starts with every task unchecked and no fabricated Phase
  2 evidence, status tick, SHA, or clean-state assertion.
- Before creator dispatch, the committed recovery baseline, independent
  Plan-Reviewer approval, and Dispatcher-recorded Phase 2 evidence exist.

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

- No repository release action, tag, `README.md` update, or `VERSION` bump is
  required.
- After a human merges the PR, STOP POINT 2 applies. The current execution must
  stop; only a new explicit human resume can begin post-merge local sync.
- Main Agent updates the listed close summary to the merged handoff before
  declaring the topic closed; its next handoff remains human review of the
  candidate basis and any later implementation topic.

## Open Questions / Unresolved Items

- None blocking. The future Swift and TypeScript evidence collection is an
  explicit follow-up route, not an unresolved requirement for this bounded
  candidate-basis topic.
