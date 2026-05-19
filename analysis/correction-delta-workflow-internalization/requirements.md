# Correction / Delta Workflow Internalization — Requirements

## Status

- **Status**: frozen for technical translation
- **Topic**: `correction-delta-workflow-internalization`
- **Scope**: analysis-only internalization assessment
- **Bounded evidence source**: `/Users/andrew/code/python/mlops-async`
- **Target repository**: `agent-skills`

## Problem Statement

The `mlops-async` repository used a correction / delta artifact workflow during a
merged and released topic. The business question is whether that workflow should
be internalized into `agent-skills` as reusable skill, prompt, checklist, or
workflow-contract guidance.

This assessment must separate durable workflow behavior from the sample topic
payload. The reusable concern is not `HttpClient`, exception naming, non-finite
JSON handling, nominal inheritance, or any `mlops-async` module path. The
reusable concern is how accepted drift, reviewer feedback, correction artifacts,
parent artifact backfill, and creator / reviewer ownership should be handled in a
repo-visible workflow.

## Evidence Read

The analysis used these required `mlops-async` evidence files:

- `plan/core-concrete-client-minimal/core-concrete-client-minimal.correction-plan.md`
- `plan/core-concrete-client-minimal/core-concrete-client-minimal.nominal-inheritance.correction-plan.md`
- `plan/core-concrete-client-minimal/core-concrete-client-minimal.object-typehint.correction-plan.md`
- `plan/core-concrete-client-delta-backfill/core-concrete-client-delta-backfill.plan.md`
- `plan/core-concrete-client-delta-backfill/core-concrete-client-delta-backfill.review-log.md`
- `analysis/core-concrete-client-minimal/requirements.md`
- `analysis/core-concrete-client-minimal/technical-spec.md`
- `plan/core-concrete-client-minimal/core-concrete-client-minimal.plan.md`
- `plan/core-concrete-client-minimal/core-concrete-client-minimal.step.md`
- `README.md` v0.9.2 status wording

The analysis also checked relevant `agent-skills` workflow surfaces:

- `plan/agent-handoff-workflow.md`
- `.github/agents/python-implementation-workflow.agent.md`
- `.github/skills/plan-creator/references/artifact-path-rule.md`
- `.github/skills/plan-creator/references/role-boundary-rule.md`
- `.github/skills/plan-reviewer/checklist.md`
- `analysis/python-implementation-workflow-drift-handling/requirements.md`
- `analysis/python-implementation-workflow-drift-handling/technical-spec.md`

## Actors and Boundaries

| Actor | Role | Boundary |
| --- | --- | --- |
| Internalization analyst | Classifies which workflow behaviors are reusable | Must not implement skill, prompt, template, workflow spec, or agent changes in this round |
| Workflow / governance maintainer | Decides whether to refresh workflow guidance later | Must not treat sample domain rules as universal process rules |
| Plan authoring contract owner | Owns future plan-creator / template wording if refreshed | Must keep creator execution steps bounded to creator-owned work |
| Plan reviewer contract owner | Owns future reviewer checklist wording if refreshed | Must review role boundaries, exact paths, and correction lifecycle without authoring the implementation |
| Creator | Executes creator-owned artifact updates in a future topic | Must not own reviewer verdict logging or final approval |
| Reviewer | Produces independent verdict and feedback in a future topic | Must not author the final implementation contract directly |

## Measurable Requirements

### R1. Classify workflow behavior before internalization

| Element | Requirement |
| --- | --- |
| Actor | Internalization analyst |
| Condition | A merged sample workflow contains correction / delta artifacts and domain-specific implementation content |
| Observable result | Each candidate rule is labeled as one of: portable workflow invariant, repo-specific sample, optional policy, or topic-local decision that must not be internalized |
| Metric / decision rule | A rule may be called portable only when it describes artifact authority, role ownership, review routing, or path-bounding behavior independent of `mlops-async` domain details |
| Failure meaning | Domain payload such as `HttpClient` or exception hierarchy could be accidentally promoted into a universal Agent Skill rule |

### R2. Preserve current-truth versus historical-truth separation

| Element | Requirement |
| --- | --- |
| Actor | Workflow / governance maintainer |
| Condition | A correction / delta artifact records accepted drift or needs-rework decisions |
| Observable result | Parent artifacts are identified as the execution-facing current truth after acceptance, while correction / delta artifacts remain historical decision trail |
| Metric / decision rule | The final analysis must state that correction artifacts do not replace parent plan/spec/step/analysis artifacts after backfill |
| Failure meaning | Future executors may treat sidecar correction files as the only final contract, leaving parent artifacts stale |

### R3. Require repo-visible correction trail for material drift

| Element | Requirement |
| --- | --- |
| Actor | Workflow / governance maintainer |
| Condition | Drift or reviewer feedback changes source-of-truth semantics, architecture boundary, public contract meaning, phase routing, or accepted execution criteria |
| Observable result | The correction decision is captured in a repo-visible artifact before downstream execution relies on it |
| Metric / decision rule | Chat-only correction is insufficient for material drift; the artifact must state trigger, scope, what stays, what changes, acceptance delta, and retention intent |
| Failure meaning | A future agent may resume from hidden chat memory and silently fork the contract |

### R4. Keep creator and reviewer ownership separate

| Element | Requirement |
| --- | --- |
| Actor | Plan authoring contract owner + Plan reviewer contract owner |
| Condition | A topic has creator-owned backfill work and reviewer-owned verdict / feedback logging |
| Observable result | Creator implementation steps contain only creator-owned execution work; reviewer feedback and review-log ownership are expressed in reviewer handoff / routing surfaces |
| Metric / decision rule | Any reviewer-owned logging or verdict-generation task inside creator implementation steps is a blocking role-boundary violation |
| Failure meaning | The creator can appear responsible for producing or satisfying the independent reviewer verdict, weakening role separation |

### R5. Bound artifact paths exactly

| Element | Requirement |
| --- | --- |
| Actor | Plan authoring contract owner |
| Condition | A correction / delta backfill topic relies on prior artifacts or merged implementation evidence |
| Observable result | Artifact paths list exact repo-visible files, owners, and roles; vague phrases such as `merged implementation` are not accepted as execution evidence |
| Metric / decision rule | If evidence is used for execution or review, the plan must name the exact file paths or explicitly limit itself to already-listed artifacts |
| Failure meaning | Future agents may infer evidence scope differently and modify or evaluate unbounded files |

### R6. Make reviewer feedback handoff repo-visible when it controls rework

| Element | Requirement |
| --- | --- |
| Actor | Reviewer + Main Agent / routing owner |
| Condition | Reviewer feedback changes whether the topic loops, passes, or escalates |
| Observable result | Verdict rounds and blocking issues are recorded in a repo-visible handoff or review log |
| Metric / decision rule | The log must be sufficient for another agent to reconstruct each reviewer decision without reading hidden conversation state |
| Failure meaning | Rework routing becomes non-reproducible and the next actor cannot tell why a round passed or failed |

### R7. Treat round limits as explicit optional policy, not an invariant

| Element | Requirement |
| --- | --- |
| Actor | Workflow / governance maintainer |
| Condition | A topic declares a creator / reviewer loop cap such as three rounds |
| Observable result | The cap is treated as a declared topic policy that may be internalized as an optional guardrail pattern, not as a universal default for every workflow |
| Metric / decision rule | `three rounds` may be recommended when the plan declares it, but internal guidance must not require all creator / reviewer loops to stop at exactly three rounds |
| Failure meaning | Ordinary low-risk rework could be over-escalated or blocked by a sample-specific cap |

### R8. Explicitly exclude topic-local sample decisions

| Element | Requirement |
| --- | --- |
| Actor | Internalization analyst |
| Condition | Sample evidence includes implementation and domain decisions |
| Observable result | The final analysis names decisions that must not be internalized, including `HttpClient`, nominal inheritance, non-finite JSON handling, `MlopsAsyncBaseException`, and `transport/http_client.py` |
| Metric / decision rule | These details may appear only as evidence examples, not as reusable workflow requirements |
| Failure meaning | Future skills could impose `mlops-async` architecture on unrelated repositories |

## Candidate Rule Classification

| Candidate rule | Classification | Requirement outcome |
| --- | --- | --- |
| Material drift should be captured in repo-visible correction / delta artifacts | Portable workflow invariant | Worth internalizing; already partly present in `agent-skills` drift guidance |
| Accepted corrections must be backfilled into parent artifacts as execution-facing current truth | Portable workflow invariant | Worth internalizing; should be emphasized wherever correction closure is reviewed |
| Correction / delta artifacts should remain as historical decision trail | Portable workflow invariant | Worth internalizing; direct deletion should remain forbidden when they explain accepted drift |
| Reviewer feedback that controls rework should have repo-visible handoff / review-log | Portable workflow invariant for multi-agent workflows | Worth internalizing; exact file name may remain flexible |
| Reviewer-owned work must not be placed inside creator implementation steps | Portable workflow invariant | Worth internalizing through plan authoring and plan review checks |
| Artifact paths must be exact and bounded | Portable workflow invariant | Already present; sample reinforces that unbounded `merged implementation` wording should fail review |
| Creator / reviewer loop had a maximum of three rounds | Optional policy | Internalize only as declared loop-cap pattern, not as universal default |
| `HttpClient` must nominally inherit `Client` | Topic-local decision | Do not internalize |
| `NaN`, `Infinity`, and `-Infinity` are invalid JSON success bodies | Topic-local decision | Do not internalize |
| `MlopsAsyncBaseException` at package root with transport-local concrete exceptions | Repo-specific sample | Do not internalize |
| `src/mlops_async/transport/http_client.py` is the concrete client path | Repo-specific sample | Do not internalize |
| Correction files use exactly the sampled filenames | Repo-specific sample / optional convention | Internalize only the need for explicit paths, not the exact names |

## Recommended Landing Layers

| Internalizable rule | Best landing layer |
| --- | --- |
| Distinguish current truth from historical correction trail | Correction / delta lifecycle guidance |
| Require parent artifact backfill before correction closure | Correction / delta lifecycle guidance + plan review contract |
| Require exact, bounded artifact paths for correction evidence | Plan authoring contract + plan review contract |
| Keep reviewer-owned logging out of creator implementation steps | Plan authoring contract + plan review contract + reviewer handoff contract |
| Record reviewer verdict rounds when feedback controls routing | Reviewer handoff contract |
| Require analysis/spec to explain accepted correction backfill without becoming the correction sidecar | Analysis guidance + technical-spec guidance |
| Treat loop caps as declared policy, not global invariant | Reviewer handoff contract + optional workflow policy |

## Non-goals

- Do not modify skills, prompts, templates, workflow specs, agents, README, or VERSION in this analysis topic.
- Do not produce implementation plans or skill code.
- Do not migrate skill paths or alter `.github/skills/` versus `skills/` positioning.
- Do not generalize `mlops-async` domain or module-specific contracts.
- Do not define a new parser or automation contract for correction artifacts.

## Surfaced Contradictions and Resolutions

| Contradiction | Conflict | Resolution |
| --- | --- | --- |
| Correction artifacts are important enough to preserve, but parent artifacts must be current truth | If correction artifacts stay visible, later agents may treat them as final source of truth | Preserve correction artifacts as historical truth and require parent backfill before closure |
| Reviewer feedback must be logged, but reviewer work must not be in creator implementation steps | A plan can accidentally make creator responsible for reviewer-owned review-log work | Put review logging in reviewer handoff / routing surfaces, not creator implementation steps |
| The sample used a three-round cap, but existing `agent-skills` ordinary `needs-rework` loops are not globally capped | A universal cap could contradict existing ordinary rework behavior | Treat round limits as optional declared policy for topics that need bounded escalation |
| The sample includes concrete Python client decisions, but the requested internalization is workflow-level | Domain details are visible and tempting to reuse | Explicitly mark domain details as sample payload and exclude them from reusable requirements |

## Extreme-boundary Checks

| Boundary | Requirement result |
| --- | --- |
| No network or inaccessible sample repo | The assessment must stop and ask for a readable bounded evidence path; this was satisfied by `/Users/andrew/code/python/mlops-async` |
| Wrong role or missing approval | Analysis may recommend later changes but must not self-perform creator/reviewer/implementation work |
| Interrupted or partial completion | If only correction artifacts exist and parent backfill is absent, the workflow remains open; current truth is incomplete |
| Lowest-volume condition | A single accepted correction still needs current-vs-historical truth separation if it changes execution-facing meaning |
| Peak-volume condition | Multiple correction rounds need repo-visible logs and exact paths so later agents can reconstruct decisions without hidden chat |
| Audit reconstruction | The retained correction artifacts and review log must explain why the final parent artifacts changed |

## Success Signals

This analysis is successful when it:

1. clearly separates workflow invariant, repo-specific sample, optional policy, and topic-local decision;
2. identifies which rules are worth internalizing and where they should land;
3. states why a new independent skill is or is not justified;
4. names at least three incorrect-generalization risks;
5. recommends the smallest viable next topic for a future implementation round.

## Blockers

None. The bounded evidence was readable, and the baseline is ready for technical translation.

## Handoff Boundary for Technical Translation

Technical translation may map the reusable requirements to existing `agent-skills`
surfaces and recommend a minimal future topic. It must not start implementation,
write a topic plan for implementation, or edit any skill / prompt / template /
workflow spec in this analysis-only round.
