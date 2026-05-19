# Correction / Delta Workflow Internalization — Technical Spec

## Status

- **Status**: analysis-only technical baseline
- **Topic**: `correction-delta-workflow-internalization`
- **Source baseline**: `analysis/correction-delta-workflow-internalization/requirements.md`
- **Translation scope**: internalization assessment and landing-layer recommendation only
- **Implementation status**: no implementation authorized in this round

## Baseline Summary

The `mlops-async` evidence supports internalizing the workflow pattern, not the
sample domain content. The reusable pattern is:

1. material drift / needs-rework decisions should become repo-visible correction
   or delta artifacts;
2. once accepted, parent artifacts must be backfilled as the execution-facing
   current truth;
3. correction / delta artifacts should remain as historical decision trail and
   workflow sample;
4. creator-owned work, reviewer-owned verdicts, and main-agent routing must stay
   separate;
5. artifact paths must be exact, bounded, repo-visible, and role-labeled;
6. reviewer feedback that controls rework should be recoverable from a
   repo-visible handoff or review log;
7. round limits are useful only when explicitly declared as topic policy.

The sample payload is not reusable as process law: `HttpClient`, nominal
inheritance, non-finite JSON handling, `MlopsAsyncBaseException`,
`transport/http_client.py`, and other `mlops-async` module/API details are only
evidence carriers.

## Requirement Traceability

| Requirement | Technical realization | Dependencies | Cost / burden | Status |
| --- | --- | --- | --- | --- |
| R1 Classify workflow behavior before internalization | Future guidance should require a classification table separating invariant, sample, optional policy, and topic-local decision | Existing analysis-layer discipline; `business-intent-alignment` style artifact | Low; documentation/checklist burden only | feasible |
| R2 Preserve current-truth vs historical-truth separation | Correction lifecycle guidance should state parent artifacts are current truth after backfill; correction artifacts remain historical truth | `plan/agent-handoff-workflow.md` already contains this rule | Low; mostly reinforcement and examples | feasible |
| R3 Require repo-visible correction trail for material drift | Existing drift policy can be refreshed with an example-backed minimum correction artifact content list | `plan/agent-handoff-workflow.md`; `.github/agents/python-implementation-workflow.agent.md` | Medium; wording must avoid making correction artifacts always-on | feasible with care |
| R4 Keep creator and reviewer ownership separate | Plan authoring and review checks should reject reviewer-owned logging inside creator `Implementation Steps` | `plan-creator` role-boundary rule; `plan-reviewer` checklist | Low to medium; likely checklist/reference refresh | feasible |
| R5 Bound artifact paths exactly | Plan review should explicitly fail vague evidence sources such as `merged implementation` when exact file paths are needed | Existing artifact-path rule and plan-review checklist | Low; already mostly covered | feasible |
| R6 Make reviewer feedback handoff repo-visible when it controls rework | Reviewer handoff guidance can require review-log or equivalent repo-visible record for multi-round routing | Existing reviewer handoff section; sample review-log | Medium; must define when needed without forcing logs for trivial one-pass review | feasible |
| R7 Treat round limits as optional policy | Reviewer handoff guidance can say loop caps are valid only when declared in the topic plan | Existing status model; sample three-round cap | Low; avoid universal default | feasible |
| R8 Exclude topic-local sample decisions | Analysis guidance should require explicit non-internalizable sample list | This analysis artifact; future checklist wording | Low | feasible |

## Direct Answers to the Six Assessment Questions

### 1. Which rules are generalizable?

Generalizable rules:

- Material drift that changes source-of-truth semantics, architecture boundary,
  public contract meaning, phase routing, or accepted execution criteria should
  be captured in repo-visible correction / delta artifacts.
- Accepted correction decisions should be backfilled into parent artifacts so the
  parent analysis/spec/plan/step becomes the execution-facing source of truth.
- Correction / delta artifacts should not be deleted after backfill; they remain
  historical decision trail, reviewer evidence, and workflow sample.
- Correction artifacts should clearly state trigger, scope, what stays, what is
  removed or rewritten, acceptance delta, affected artifacts, and retention
  intent when those fields are relevant.
- Reviewer feedback that changes routing should have repo-visible handoff or
  review-log evidence.
- Creator-owned execution steps must not contain reviewer-owned verdict logging
  or review decision work.
- Artifact paths used for execution or review evidence must be exact and bounded;
  vague phrases like `merged implementation` are not enough.
- Round limits can be generalized only as an explicit topic-level policy pattern,
  not as a universal constant.

### 2. Which rules are only `mlops-async` sample and should not be internalized?

Do not internalize these sample details:

- `HttpClient` or any concrete client architecture.
- The decision that `HttpClient` must nominally inherit `Client`.
- The `NaN` / `Infinity` / `-Infinity` JSON boundary.
- `MlopsAsyncBaseException` naming or hierarchy.
- `src/mlops_async/transport/http_client.py`.
- `src/mlops_async/exceptions.py` and `src/mlops_async/transport/exceptions.py`
  placement rules.
- Any auth, retry, JSON, transport, exception, module, test, or API-specific
  contract from `mlops-async`.
- The exact correction artifact filenames as universal names; only the exact-path
  requirement is portable.

### 3. Where should internalized guidance land?

| Landing layer | Recommended content |
| --- | --- |
| Analysis guidance | Require explicit classification of invariant vs sample vs optional policy vs topic-local decision before internalization |
| Technical-spec guidance | Require mapping accepted corrections back to parent current-truth artifacts and naming feasibility / burden of doing so |
| Plan authoring contract | Require exact artifact paths, correction artifact listing when used, parent-sync intent, and creator-only `Implementation Steps` |
| Plan review contract | Reject stale parent artifacts, vague evidence paths, wrong status, mixed role ownership, and missing correction lifecycle closure checks |
| Correction / delta lifecycle guidance | Define current truth vs historical truth, parent backfill before closure, retention after closure, and severity-gated artifact use |
| Reviewer handoff contract | Require repo-visible review-log / equivalent handoff for multi-round or routing-controlling feedback; allow declared round caps |

### 4. New skill / prompt / workflow rule, or refresh existing assets?

Do not create a new standalone skill as the first move. The behavior is a
cross-cutting workflow contract already partially present in `agent-skills`, not
a single-purpose user-invoked skill.

Recommended shape for a future implementation topic:

1. refresh existing workflow / plan assets rather than create a new skill;
2. update `plan-creator` guidance and template checks for correction / delta
   artifact listing, parent-sync intent, and role-owned implementation steps;
3. update `plan-reviewer` checklist / examples so it catches the exact failures
   seen in the sample: wrong current status, reviewer-owned work in
   implementation steps, and unbounded evidence paths;
4. optionally add or refresh a correction / delta lifecycle reference if existing
   surfaces need a single shared wording source;
5. avoid touching stable skill library or release surfaces unless a later topic
   explicitly authorizes that scope.

### 5. Where would over-internalization cause incorrect generalization?

Key risks:

1. **Domain payload becomes process law**: turning `HttpClient`, exception
   hierarchy, module placement, or non-finite JSON rules into universal workflow
   requirements would impose `mlops-async` architecture on unrelated repos.
2. **Correction artifacts replace parent truth**: preserving sidecars without
   requiring parent backfill would make future executors chase stale or competing
   contracts.
3. **Three rounds becomes a universal cap**: the sample cap is useful as declared
   escalation policy, but a global cap would conflict with ordinary low-risk
   `needs-rework` loops that may not need human escalation.
4. **Review logs become mandatory for every review**: requiring a review-log for
   trivial one-pass reviews would add noise; the invariant is repo-visible
   handoff when feedback controls routing or multi-round rework.
5. **Exact filename conventions become universal**: requiring the sampled
   filenames everywhere would be less important than the portable rule: exact,
   bounded, role-labeled artifact paths.
6. **Implementation evidence becomes unbounded**: accepting phrases like `merged
   implementation` lets different agents infer different evidence scopes.
7. **Reviewer work leaks into creator contract**: making creators log reviewer
   verdicts or own reviewer feedback weakens independent review.

### 6. What is the smallest viable next topic?

The smallest viable next topic should be:

`correction-delta-lifecycle-contract-refresh`

Scope:

- refresh existing plan-authoring / plan-review guidance to encode correction /
  delta lifecycle checks;
- add example-backed checks for exact artifact paths, parent-sync before
  closure, retained historical artifacts, repo-visible review-log handoff when
  feedback controls routing, and role-boundary separation;
- explicitly document that loop caps are topic-declared optional policy;
- explicitly list sample-domain decisions as non-internalizable in the example.

Non-scope:

- no new standalone skill;
- no parser or automation;
- no migration from `.github/skills/` to `skills/`;
- no release or stable-library promotion unless separately planned.

## Internalization Surface Assessment

| Surface | Current coverage | Gap from sample | Recommendation |
| --- | --- | --- | --- |
| `plan/agent-handoff-workflow.md` | Already states parent artifacts are current truth, correction artifacts are historical truth, severity-gated artifacts, parent sync, and deletion forbidden | Does not necessarily include the concrete review-log / delta-backfill sample failures | Refresh examples or add concise lifecycle reference only if future topic proceeds |
| `.github/agents/python-implementation-workflow.agent.md` | Already defines correction-triggering drift, provisional routing, parent sync, and correction closure | Python-specific and implementation-flow-specific, not the best universal landing for all correction/delta lifecycle rules | Keep as consumer of shared workflow wording; avoid making it sole owner |
| `plan-creator` | Has artifact-path and role-boundary rules | Could more explicitly require correction artifacts and parent-sync intent when a topic uses them | Refresh reference/checklist/template guidance |
| `plan-reviewer` | Checks exact bounded paths and role ownership | Sample shows three concrete review failures that should become review examples/checks | Refresh checklist/examples |
| Analysis / technical-spec skills | Provide measurable baseline and technical translation patterns | Could use this assessment as a model for internalization analysis | No immediate skill change unless repeated use proves need |

## Cost-of-Realization Assessment

| Workstream | Complexity | Sequencing | Burden |
| --- | --- | --- | --- |
| Refresh plan-creator correction/delta guidance | Low to medium | First, because plan authors need correct contracts before review can enforce them | Moderate wording precision; low operational overhead |
| Refresh plan-reviewer checks/examples | Low to medium | Same topic as plan-creator refresh to avoid asymmetry | Low runtime burden; improves review signal |
| Add shared correction/delta lifecycle reference | Medium | Only if duplicate wording appears across multiple surfaces | Reduces drift but adds another local reference to maintain |
| Add new independent skill | Medium to high | Not recommended as first move | Likely over-fragments workflow governance |
| Add parser/tooling support | High | Out of scope for smallest viable topic | Unnecessary until machine-readable correction artifacts are required |

## Architecture-compliance Self-check

| Dimension | Result | Notes |
| --- | --- | --- |
| Repository positioning | fits existing architecture | Analysis artifacts under `analysis/<topic>/` are already used in this repo |
| Active skill path | fits existing architecture | Future changes, if any, should target `.github/skills/` during transition |
| Role separation | fits with prerequisites | Guidance must keep creator, reviewer, planner, and Main Agent responsibilities distinct |
| Existing correction policy | fits existing architecture | The sample reinforces existing drift-handling policy rather than replacing it |
| Skill proliferation control | fits existing architecture | A new skill is not justified before refreshing existing workflow contracts |
| Workflow portability | fits with prerequisites | Must avoid importing `mlops-async` domain rules |
| Automation assumptions | fits with prerequisites | No parser/tooling change should be implied by this analysis |

## Conflicts, Constraints, and Rollback Triggers

| Issue | Type | Handling |
| --- | --- | --- |
| Existing `agent-skills` already has correction drift rules | Duplication risk | Refresh existing surfaces instead of creating a new standalone skill first |
| Review-log requirement could become noisy | Overreach risk | Require repo-visible handoff only when feedback controls routing or multi-round rework |
| Round cap could conflict with ordinary `needs-rework` loops | Policy conflict | Treat caps as explicit topic policy only |
| Sample domain details are prominent | Generalization risk | Keep a required non-internalizable sample list |
| Parent backfill may be expensive in large topics | Operational burden | Require parent-sync intent and exact affected artifacts before closure |

Rollback to alignment if a future implementation topic discovers any of these:

1. **Failing assumption**: existing plan-creator / plan-reviewer surfaces can
   absorb the lifecycle guidance cleanly.
   - **Contradicting fact**: the guidance needs a standalone lifecycle owner or
     machine-readable artifact contract.
   - **Required decision**: decide whether to create a dedicated workflow rule or
     skill before editing existing assets.
2. **Failing assumption**: review logs can remain conditional.
   - **Contradicting fact**: governance requires every review to be auditable in
     the same artifact shape.
   - **Required decision**: define a universal review-log contract separately.
3. **Failing assumption**: exact-path rules are sufficient without parser support.
   - **Contradicting fact**: future agents repeatedly miss unbounded evidence
     wording even after checklist refresh.
   - **Required decision**: consider parser/tooling support in a separate topic.

## Recommended Next Topic Contract

If this proceeds, create a later implementation topic with this narrow contract:

- **Topic name**: `correction-delta-lifecycle-contract-refresh`
- **Primary surfaces**:
  - `.github/skills/plan-creator/` reference/checklist/template guidance
  - `.github/skills/plan-reviewer/` checklist/examples
  - optionally a shared local reference if duplication becomes unavoidable
- **Required checks to encode**:
  - correction artifacts listed explicitly when used;
  - parent artifacts remain current truth after backfill;
  - correction artifacts remain historical truth and are not deleted;
  - creator implementation steps exclude reviewer-owned logging;
  - reviewer handoff / review-log is repo-visible when feedback controls routing;
  - artifact paths are exact, bounded, repo-visible, and role-labeled;
  - round caps are declared topic policy, not global default;
  - sample-domain rules are marked non-internalizable.
- **Out of scope**:
  - new skill creation;
  - prompt or agent rewrite beyond directly affected references/checklists;
  - parser/tooling changes;
  - release or stable-library promotion.

## Final Verdict

This workflow is worth partial internalization as lifecycle and review-contract
guidance. It should not become a new independent skill first, and it should not
import the `mlops-async` topic payload. The correct next move is a small contract
refresh of existing plan-authoring and plan-review surfaces, backed by the
correction / delta lifecycle distinction already present in repo workflow
guidance.
