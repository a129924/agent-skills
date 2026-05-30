# Technical Specification — codex-skill-direct-move-impl-ab

**Status**: PLANNED
**Derived from**: `requirements.md` R1-R7
**Risk level**: `medium`
**Planned target branch**: `feat/andrew/codex-skill-direct-move-impl-ab`

---

## R->T Mapping

| Requirement | Technical task | Artifact path |
| --- | --- | --- |
| R1 | T1: Freeze the implementation write set to the 7 A/B skills plus topic-owned planning artifacts | `analysis/codex-skill-direct-move-impl-ab/requirements.md`, `plan/codex-skill-direct-move-impl-ab/codex-skill-direct-move-impl-ab.plan.md` |
| R2 | T2: Encode A-class direct-move implementation rules for the two semantic skills | `plan/codex-skill-direct-move-impl-ab/codex-skill-direct-move-impl-ab.plan.md`, `plan/codex-skill-direct-move-impl-ab/codex-skill-direct-move-impl-ab.step.md` |
| R3 | T3: Encode B-class rewrite implementation rules for the five semantic skills | `plan/codex-skill-direct-move-impl-ab/codex-skill-direct-move-impl-ab.plan.md`, `plan/codex-skill-direct-move-impl-ab/codex-skill-direct-move-impl-ab.step.md` |
| R4 | T4: Mark `.github/skills/` as read-only source context and `skills/` as the only skill-content write target | `analysis/codex-skill-direct-move-impl-ab/requirements.md`, `plan/codex-skill-direct-move-impl-ab/codex-skill-direct-move-impl-ab.plan.md` |
| R5 | T5: Materialize a required progression artifact for the later implementation workflow | `plan/codex-skill-direct-move-impl-ab/codex-skill-direct-move-impl-ab.step.md` |
| R6 | T6: Materialize a pre-launch summary artifact that records launch blockers and next handoff | `plan/codex-skill-direct-move-impl-ab/codex-skill-direct-move-impl-ab.summary.md` |
| R7 | T7: Preserve transition-era wording and prevent cutover claims in all implementation-topic artifacts, while using the reviewed overlay as repo-visible workflow input | all implementation-topic artifacts plus `docs/process/overlays/agent-skills-transition-overlay.md` |

---

## T1 — Frozen implementation write set

The later implementation topic may write only:

- `skills/python-package-layout/`
- `skills/python-library-architecture/`
- `skills/python-plan-authoring/`
- `skills/python-blueprint-authoring/`
- `skills/python-pre-commit/`
- `skills/python-pyproject-toolconfig/`
- `skills/python-tdd-test-authoring/`
- topic-owned artifacts under `analysis/codex-skill-direct-move-impl-ab/`
- topic-owned artifacts under `plan/codex-skill-direct-move-impl-ab/`
- workflow-run evidence under `.workflow-runs/<run-id>/`

Everything else is read-only unless a future planner explicitly re-plans.

---

## T2 — A-class direct-move implementation rules

The later implementation topic must treat these as semantic direct moves:

- `python-package-layout`
- `python-library-architecture`

### Required signals

- preserve the current skill's design / review semantics
- remove any residual workflow framing that is not needed for a Codex semantic
  skill
- implement the new version under `skills/`
- do not require edits to `.github/skills/` during this topic

### Acceptance shape

- skill exists under `skills/`
- trigger and boundaries remain clear
- no machine-verdict contract or acceptance-command dependency remains in the
  new Codex skill

---

## T3 — B-class rewrite implementation rules

The later implementation topic must implement these as semantic rewrites:

- `python-plan-authoring`
- `python-blueprint-authoring`
- `python-pre-commit`
- `python-pyproject-toolconfig`
- `python-tdd-test-authoring`

### Required rewrite dimensions

- retain the frozen semantic value from the bootstrap baseline
- remove repo-visible workflow artifact coupling from the new skill contract
- avoid script-wrapper behavior as the core contract
- keep strong fit / non-fit boundaries explicit

### Per-skill frozen direction

- `python-plan-authoring`
  - keep Python planning semantics
  - remove mandatory `.plan.md` / `.step.md` / `.spec.md` co-artifact contract
- `python-blueprint-authoring`
  - keep greenfield baseline design semantics
  - remove executor-consumable locked blueprint contract coupling
- `python-pre-commit`
  - keep uv-scoped hook and stage policy
  - remove fixed write/install-flow coupling as the core contract
- `python-pyproject-toolconfig`
  - keep append-only / preserve-existing policy
  - remove script/template-centric contract language
- `python-tdd-test-authoring`
  - keep test-first / RED-test semantics
  - remove workflow-gated verdict artifact requirements

---

## T4 — Read-only source context rule

During the later implementation topic:

- `.github/skills/` is the read-only comparison source
- `skills/` is the only skill-content output location
- no deletion, rename, or rewrite is authorized under `.github/skills/`
- no artifact may claim the repository has already cut over to `skills/`

---

## T5 — Required progression artifact

`plan/codex-skill-direct-move-impl-ab/codex-skill-direct-move-impl-ab.step.md`
is mandatory for the later implementation workflow.

The step artifact must remain the repo-visible progression truth for:

- implementation start
- reviewer handoff
- overlay-gate status
- migration-status confirmation
- publish handoff readiness

---

## T6 — Launch-blocker summary contract

The summary artifact must tell the next agent:

- which committed bootstrap artifacts are required inputs
- which branch and worktree are planned for the implementation topic
- that the reviewed overlay file is available as repo-visible workflow input
- that overlay binding is determined from the approved topic scope at launch
  time, not by chat-only inference
- that migration implementation must not start until target-branch/worktree
  preparation is explicitly resolved

---

## Architecture / policy compliance

| Check | Result |
| --- | --- |
| Writable scope excludes `.github/skills/` | PASS |
| Writable scope excludes shared governance files | PASS |
| Required `step.md` is part of first planning batch | PASS |
| Implementation topic consumes committed bootstrap truth | PASS |
| Topic does not authorize commit / push / PR | PASS |
| Overlay uncertainty is recorded as unresolved | PASS |

---

## Rollback-to-alignment triggers

Return to planning instead of starting implementation if any of these occurs:

- a proposed implementation step requires editing `.github/skills/`
- any C-class skill enters the write set
- a future agent tries to treat unresolved overlay guidance as implicit
  approval
- branch/worktree preparation points at a different topic family than this
  implementation topic
- a future reviewer cannot tell launch blockers from the summary artifact alone
