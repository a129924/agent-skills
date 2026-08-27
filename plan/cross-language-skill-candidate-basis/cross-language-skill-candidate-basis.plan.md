# Cross-Language Skill Candidate Basis — Topic Plan

## Analysis-layer routing

**Semantic warning — optional analysis layer absent:** neither
`analysis/cross-language-skill-candidate-basis/requirements.md` nor
`analysis/cross-language-skill-candidate-basis/technical-spec.md` exists.
This plan is based on the explicit human-approved topic boundary. If either
analysis artifact is introduced, stop and reconcile its authority before
changing this plan or implementing the candidate-basis document.

## Goal / Outcome

- Create `docs/agent-skills-convergence/cross-language-candidate-basis.md` as
  a read-only, evidence-backed first-pass inventory of the 11 locked candidates
  that may later evolve into a generic core with Python, Swift, and TypeScript
  language appendices.
- The document records candidate classification and next-step evidence; it does
  not authorize or implement cross-language generalization.

## Scope

- **In scope**:
  - Create the topic-local planning, review-routing, close-summary, and
    candidate-basis artifacts listed in `Artifact Paths`.
  - Evaluate only these four groups and their 11 candidates:
    - Testing and validation: `python-tdd-test-authoring`,
      `python-testing-pytest`, `python-implementation-review`.
    - Code review: `python-code-review`.
    - Design boundaries: `semantic-first-design`, `boundary-outcome-design`,
      `python-error-handling`, `python-serialization-boundaries`.
    - Coding style: `python-naming`, `python-control-flow`,
      `python-docstrings`.
  - For each candidate, record its portable core, the existing Python evidence,
    prospective Swift and TypeScript appendix needs, language-bound blockers,
    risk, and a follow-up route.

- **Out of scope**:
  - Editing, moving, deleting, renaming, publishing, or projecting any skill.
  - Assessing Python runtime/toolchain, project-lifecycle, object-model,
    syntax-specific, API/module, or async skills beyond the locked 11.
  - Verifying an unprovided Swift or TypeScript repository, or claiming such
    validation occurred.
  - Changing existing topic plans, Phase 1 artifacts, platform surfaces,
    `README.md`, `VERSION`, workflow contracts, runtime behavior, release,
    commit, push, or PR behavior.

## Locked Decisions

- This is a review-ready-only, non-stable topic: it does not affect the stable
  library and has no `README.md`, `VERSION`, release, or tag action.
- The candidate model is **generic core + language appendix**. A candidate may
  be routed as blocked or deferred; none is presumed portable merely because it
  appears in this inventory.
- Swift and TypeScript entries describe required future validation or blockers,
  not asserted repository evidence.
- **ReadOnly** inputs are exactly:
  - `AGENTS.md`; `docs/repo-positioning.md`;
    `plan/agent-handoff-workflow.md`; and `plan/topic-plan-contract.md`.
  - `docs/agent-skills-convergence/phase-1/**` and
    `docs/agent-skills-convergence/phase-3/projection-adapter-design.md`.
  - The 11 candidate `skills/<candidate>/SKILL.md` files named in `Scope`.
- **Written** paths are exactly the five paths in `Artifact Paths`.
- **Modify** of pre-existing tracked files is prohibited. **Deleted** paths are
  none. If an additional tracked path becomes necessary, stop and repair this
  plan before work continues.
- The candidate-basis document is written by an Implementer only after an
  independent Plan-Reviewer approves this plan and its progression artifact.

## Boundaries / Exclusions

- Plan-Creator owns only this plan and its step artifact. Plan-Reviewer owns an
  independent planning verdict and its review-log entry. Implementer owns only
  the candidate-basis document. Main Agent owns branch, publication, PR,
  human-review routing, and close-summary handling.
- Existing Phase 1 artifacts remain historical evidence and are not modified,
  reinterpreted as implementation authorization, or extended by this topic.
- `skills/` remains the canonical source; `.github/**`, `.codex/**`, and other
  platform surfaces remain out of scope compatibility surfaces.
- Any request to select a final cross-language architecture, change a candidate
  name/path, or begin language-specific implementation is a separately scoped
  follow-up topic.

## Status / Allowed Transitions

- **Current**: `planned`; independent Plan-Reviewer validation of this plan and
  `step.md` is a pre-execution gate within `planned`, not a separate workflow
  state. It must pass before the canonical transition to
  `creator-in-progress`.
- **Execution model**: canonical creator -> reviewer -> publish -> merge path;
  this topic stops at human review after its draft PR is opened and has no
  release transition.
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
- **Routing note**: after implementation review approval, Main Agent performs
  Phase 4.5 plan-contract alignment. Any path, contract, scope, or workflow
  drift routes to `creator-in-progress`; it does not reopen the locked candidate
  set or invent a new language architecture.

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/cross-language-skill-candidate-basis/cross-language-skill-candidate-basis.plan.md` | Plan-Creator | Current execution contract and locked write boundary |
| Topic progression | `plan/cross-language-skill-candidate-basis/cross-language-skill-candidate-basis.step.md` | Plan-Creator; then Main Agent | Current workflow-stage and gate truth |
| Review routing log | `plan/cross-language-skill-candidate-basis/cross-language-skill-candidate-basis.review-log.md` | Plan-Reviewer | Independent planning/implementation verdict trail when its result controls routing |
| Topic close summary | `plan/cross-language-skill-candidate-basis/cross-language-skill-candidate-basis.summary.md` | Main Agent | Close outcome and required human follow-up after merge |
| Candidate-basis document | `docs/agent-skills-convergence/cross-language-candidate-basis.md` | Implementer | Evidence-backed 11-candidate inventory for human review |

Artifact path notes:

- This topic does not modify `README.md`, `VERSION`, `.github/copilot-instructions.md`,
  `skills/**`, `.github/**`, or `.codex/**`.
- The first two paths are the only Plan-Creator writes. The remaining three
  paths are later role-owned writes; their listing does not authorize an early
  write or replace their required gates.

## Implementation Steps

1. Implementer re-reads the approved plan, progression artifact, all locked
   read-only inputs, and the 11 named candidate skills.
2. Implementer creates only
   `docs/agent-skills-convergence/cross-language-candidate-basis.md`, grouping
   the candidates into the four locked categories and using one consistent row
   shape: candidate, portable core, Python evidence, Swift appendix need,
   TypeScript appendix need, blocker/risk, and follow-up route.
3. Implementer keeps language-specific framework, package-manager, test-runner,
   syntax, and runtime rules out of the portable-core column, and labels any
   unsupported cross-language assertion as a future-validation need.
4. Implementer checks the diff against `Artifact Paths`, does not modify the
   plan or progression artifact, and returns a `review-ready` handoff for
   independent review.

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
- Main Agent creates the listed close summary before declaring the topic closed;
  its next handoff remains human review of the candidate basis and any later
  implementation topic.

## Open Questions / Unresolved Items

- None blocking. The future Swift and TypeScript evidence collection is an
  explicit follow-up route, not an unresolved requirement for this bounded
  candidate-basis topic.
