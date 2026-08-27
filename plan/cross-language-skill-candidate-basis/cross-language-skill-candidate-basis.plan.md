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
- Complete the committed five-artifact additive recovery baseline and its
  independent Plan-Reviewer gate; the candidate-document repair remains
  historical evidence and is not future Implementer work in this recovery loop.

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
  - Correct only the missing committed planning baseline and missing Phase 2
    branch/worktree readiness gate. The Python-specific ordering repair in
    `python-implementation-review` is fixed historical evidence, not active
    implementation scope.

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
- **Main Agent additive recovery-baseline edit set** was exactly these five
  planning and correction artifacts: the parent plan, parent progression,
  parent summary, correction plan, and correction progression listed in
  `Artifact Paths`. The candidate document was changed only by the independent
  Implementer for its one bounded portable-core repair; this recovery loop does
  not reopen that document.
- **Modify** outside those five paths was prohibited for Main Agent's additive
  baseline commit; **Deleted** paths were none. After Main Agent routes the
  topic to `reviewer-in-progress`, the independent Plan-Reviewer may append
  only its verdict to the existing review log. Main Agent retains commit and
  push ownership for that bounded record. This exception does not expand
  candidate, history-rewrite, or implementation scope.

## Boundaries / Exclusions

- Plan-Creator owns the parent planning artifacts and correction artifacts in
  this pass. Under the explicit human override, Main Agent directly verifies
  and confirms Phase 2 branch/worktree readiness; Dispatcher may route that
  result but cannot substitute for its observation or confirmation. Main Agent
  also owns and executes the new additive recovery-baseline commit, without
  amending, rebasing, resetting, force-pushing, or otherwise rewriting history.
  Plan-Reviewer independently reviews that committed baseline only after Main
  Agent routes the topic to `reviewer-in-progress`. An independent
  Implementer remains limited to the frozen candidate-document repair, and an
  independent Reviewer checks that repair. Main Agent owns PR transport and
  thread resolution, including publisher-owned commit and push actions.
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

- **Current**: `review-ready` — Main Agent directly completed the override-owned
  Phase 2 verification against published baseline
  `c285c3a11be3a26dfaa661f88e4ace4973829d1f` on branch
  `docs/andrew/cross-language-skill-candidate-basis`, then committed the exact
  five additive recovery artifacts as `b25c2a209cf3c22244543cbbc67a3eb02a866c48`.
  The resulting worktree is clean with no untracked files. `git diff --name-status
  c285c3a..b25c2a2` lists exactly those five paths; no candidate document or
  history rewrite is included. No PR thread is resolved and no reviewer verdict
  is claimed.
- **Pre-creator Phase 2 gate**: completed by Main Agent as a Status/Gate
  prerequisite, not an `Implementation Steps` item. Its direct observation and
  confirmation are recorded in the correction progression. Dispatcher did not
  substitute for the verification.
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
- **Routing note**: the recovery loop has reached `review-ready` through
  `needs-rework` -> `creator-in-progress` -> `review-ready`. Commit `b25c2a2`
  is the fixed review input. Next, Main Agent routes
  `review-ready` -> `reviewer-in-progress` and dispatches the independent
  Plan-Reviewer. Only after that transition may Plan-Reviewer append its
  independent verdict to the existing review log; Main Agent then owns commit
  and push of the bounded record and routes the verdict to `approved` or
  `needs-rework`. No action reopens the locked candidate set or invents a new
  language architecture.
- **Recovery route**: the Planner has frozen all three findings as high-severity
  correction. Recovery remains open until the override-owned baseline and
  direct Phase 2 confirmation are independently plan-reviewed and recorded.
  No thread is resolved by this synchronization.

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/cross-language-skill-candidate-basis/cross-language-skill-candidate-basis.plan.md` | Plan-Creator | Current execution contract and locked write boundary |
| Topic progression | `plan/cross-language-skill-candidate-basis/cross-language-skill-candidate-basis.step.md` | Plan-Creator; Main Agent (override-owned Phase 2 evidence and state routing); Dispatcher (routing only) | Current workflow-stage and gate truth |
| Review routing log | `plan/cross-language-skill-candidate-basis/cross-language-skill-candidate-basis.review-log.md` | Plan-Reviewer (bounded verdict only); Reviewer; Planner; Main Agent (publisher) | Separate independent verdict entries and recovery-routing trail |
| Topic close summary | `plan/cross-language-skill-candidate-basis/cross-language-skill-candidate-basis.summary.md` | Plan-Creator; Main Agent | Current PR/recovery handoff truth, then close outcome |
| Correction plan | `plan/cross-language-skill-candidate-basis/cross-language-skill-candidate-basis.correction-plan.md` | Plan-Creator; Planner; Main Agent (override-owned baseline execution) | Historical high-severity correction contract |
| Correction progression | `plan/cross-language-skill-candidate-basis/cross-language-skill-candidate-basis.correction-step.md` | Plan-Creator; Main Agent (override-owned baseline and Phase 2 evidence); Dispatcher (routing only); Planner (evidence-based closure only) | Historical correction-gate evidence and sequencing |
| Candidate-basis document | `docs/agent-skills-convergence/cross-language-candidate-basis.md` | Implementer | Evidence-backed 11-candidate inventory for human review |

Artifact path notes:

- This topic does not modify `README.md`, `VERSION`, `.github/copilot-instructions.md`,
  `skills/**`, `.github/**`, or `.codex/**`.
- The five parent/correction planning paths other than `review-log.md` were the
  only Plan-Creator writes in this recovery pass and were the exact Main Agent
  additive recovery-baseline commit set in `b25c2a2`. The candidate document's one
  Implementer-only repair and its independent Reviewer verdict are already
  present; neither is a Plan-Creator write in this recovery loop.
- Plan-Reviewer and Reviewer each append only their own distinct verdict entry
  to the review log; neither role overwrites, approves, or reuses the other
  role's verdict. For the pending Plan-Reviewer gate, Plan-Reviewer may append
  that bounded verdict only after `reviewer-in-progress`; Main Agent alone
  commits and pushes it. This does not expand the five-file Main Agent baseline
  scope.
- The explicit human override authorized Main Agent to directly verify and
  record the published `c285c3a` baseline, verify that the execution worktree
  contained exactly the five additive recovery-artifact edits with no untracked
  or unrelated change, then stage and commit that exact set as `b25c2a2`.
  Dispatcher routed observations only. This completed exception does not
  authorize history rewriting, candidate-document changes, or thread resolution
  without supporting evidence.
- If a required action falls outside this table, stop and repair this plan.
  Correction artifacts are retained; deletion is forbidden.

## Implementation Steps

1. No candidate-document implementation is authorized by this override. The
   frozen `python-implementation-review` portable-core repair and its
   independent Reviewer verdict remain historical evidence.
2. Main Agent's direct Phase 2 verification and additive baseline commit are
   Status/Gate work only and are governed by `Status / Allowed Transitions`;
   they do not authorize a new Implementer task.

## Validation / Acceptance Checks

- Exactly 11 candidates appear once each, within the four locked groups.
- Each candidate states a non-Python-specific portable core and distinct Python,
  Swift, and TypeScript treatment; Swift/TypeScript claims are marked as
  appendix needs or blockers unless evidence is present in the locked inputs.
- No portable-core entry relies on Python syntax, `pytest`, `pyproject.toml`, or
  Python runtime/toolchain rules.
- The candidate-basis document makes no path migration, projection, runtime,
  workflow-binding, implementation, or stable-library recommendation.
- Relative to `c285c3a`, `b25c2a2` modifies only the exact five additive
  recovery artifacts; no other tracked path changed, no path was deleted, no
  untracked file remained, and existing Phase 1 files remain unchanged.
- The plan and step artifact retain canonical sections and transitions; the new
  Plan-Reviewer handoff uses the fixed JSON shape. No new Reviewer handoff is
  created for the historical candidate-document repair.
- Independent review confirms no scope, contract, workflow, or authority drift
  before publication; publication still requires STOP POINT 1 human approval.
- While `pr-open`, Main Agent triages PR review comments, issue comments, and
  checks. Actionable findings route to `needs-rework`; STOP POINT 2 applies
  only after merge handoff.
- The correction plan records three high-severity issues, fixed 11-candidate
  scope, no-history-rewrite rule, acceptance criteria, and required re-reviews.
- The correction step records only Main Agent's directly observed Phase 2
  evidence and committed baseline; it does not fabricate a Plan-Reviewer
  verdict, status transition, or thread resolution.
- Main Agent directly recorded the published baseline and exact five-file
  execution-worktree comparison, then committed that exact set as `b25c2a2`.
  Main Agent must route to `reviewer-in-progress` before an independent
  Plan-Reviewer may return its verdict; only that verdict can route to
  `approved` or `needs-rework`. Main Agent owns commit and push of the verdict
  record. Dispatcher routing does not satisfy any of those Main Agent
  responsibilities.
- The new loop reaches `pr-open` only after `approved` ->
  `publish-in-progress` -> `pr-open`, with commit/push/PR observation evidence.
  Neither the new loop nor historical observations resolve a thread or claim
  correction closure.

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
- Main Agent updates the existing listed close summary to the merged handoff
  before declaring the topic closed; it must not create a replacement close
  summary. Its next handoff remains human review of the candidate basis and any
  later implementation topic.

## Open Questions / Unresolved Items

- None blocking. The future Swift and TypeScript evidence collection is an
  explicit follow-up route, not an unresolved requirement for this bounded
  candidate-basis topic.
