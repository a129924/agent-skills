# Cross-Language Skill Candidate Basis Content Corrections

## Analysis-Layer Routing

**Semantic warning:** neither
`analysis/cross-language-skill-candidate-basis-content-corrections/requirements.md`
nor
`analysis/cross-language-skill-candidate-basis-content-corrections/technical-spec.md`
exists. The explicit human canonical-source override is the execution basis
for this bounded correction only; it does not authorize inferred language
validation, migration, platform work, or scope outside the four named cells.

## Goal / Outcome

Correct the four affected portable-core cells in
`docs/agent-skills-convergence/cross-language-candidate-basis.md` to match
their canonical skills, then complete the existing PR #125 loop truthfully.
The four-cell work recorded below remains historical/pre-review evidence, not
a replacement candidate-review verdict. The required Phase 4.5 alignment and
independent planning gate are complete; Main Agent has selected the authorized
publication route, which is now pending its bounded commit and push.

## Scope

- **In scope:** only `python-tdd-test-authoring`, `python-testing-pytest`,
  `python-serialization-boundaries`, and `boundary-outcome-design` portable-
  core cells, plus the five listed planning/progression artifacts.
- **Current PR fact:** `1885c359dffa89fdeb40bb4ad1d498637553f463` is pushed
  to PR #125. Ten threads remain unresolved; coverage, replies, resolutions,
  clean observation, merge, and close are incomplete.

## Locked Decisions

- `AGENTS.md` and `docs/repo-positioning.md` govern; `skills/` is canonical.
  The human selected canonical content over conflicting or incomplete wording.
- The candidate basis is the only existing-file write. Its 11 candidates, four
  groups, all columns other than the four named portable-core cells, and locked
  `python-implementation-review` / `python-error-handling` cells stay unchanged.
- `python-tdd-test-authoring`: run D1; `trivial` emits `skip_with_reason` and
  stops. A non-trivial path uses `red-tests-ready`, `needs-rework`,
  `insufficient-context`, `skip_with_reason`, or `BLOCKED`, and maps behavior
  only when the active behavior contract permits it.
- `python-testing-pytest`: pure unit tests, no real I/O, inline-first setup;
  extract only for real reuse/shared preconditions/noise reduction;
  parameterize only identical behavior with changing data; prefer state/output
  assertions unless interaction is the contract or unavoidable side effect.
- `python-serialization-boundaries`: raw transport shapes stop at the boundary;
  inbound/outbound contracts may differ; omitted/null/unchanged applies only to
  PATCH-like partial input; deep conversion requires a promised internal object
  or typed record.
- `boundary-outcome-design`: define boundary contract and vocabulary ownership
  before preserve, translate, compress, promote, or leave; distinguish expected,
  unexpected, and not-failure. Only expected failure may promote to an
  application-safe exception on a controlled path; unexpected failure remains
  an exception under controlled propagation. Adapter translates external
  HTTP/SDK/ORM/driver vocabulary at Adapter--Port; Port receives Application
  capability vocabulary. No retry, logging, handler, or result-type policy.
- This is non-stable: no README, VERSION, tag, release, or platform-surface change.

## Boundaries / Exclusions

- Do not change Python evidence, Swift/TypeScript appendices, names, paths,
  `skills/**`, `agents/**`, `.github/**`, `.codex/**`, README, VERSION, or
  release surfaces. Do not claim Swift/TypeScript validation or reopen
  `python-code-review` remediation.
- Plan-Creator owns planning/progression artifacts. Independent Implementer
  owns the document fix; independent Reviewer owns review; Planner supplies
  only Phase 4.5 alignment input and a pending recommendation; Main Agent owns
  publish-or-rework routing, publication, and PR-loop operations. Parent
  artifacts are current truth; correction artifacts are historical routing
  truth.

## Status / Allowed Transitions

- **Current topic state:** `publish-in-progress`. The four-cell canonical
  work, including the `boundary-outcome-design` Adapter--Port fix, remains
  historical/pre-review evidence only; this planning gate does not replace a
  candidate-review verdict. Phase 4.5 alignment and Main Agent's publication
  routing are complete. The already authorized bounded commit and push are the
  next action; no publication outcome is claimed until they complete.
- **PR state:** PR #125 remains open with ten unresolved threads after pushed
  `1885c35`; no signal coverage, reply, resolution, clean observation, merge,
  release, summary, or close is claimed.
- **Rework route:** `needs-rework` -> `creator-in-progress` -> `review-ready`
  -> `reviewer-in-progress` -> `approved`. Planner supplied Phase 4.5
  alignment; Main Agent selected publication under the already granted STOP
  POINT 1 authorization. The active transition is `publish-in-progress` ->
  `pr-open`; unapproved work cannot publish.
- **Phase 7--8 after publication:** Main Agent fetches fresh review state,
  review comments/threads, issue comments, and checks; classifies and covers
  every actionable signal. Required bounded changes return to `needs-rework`;
  independent Reviewer re-enters when feedback changes logic, scope,
  requirements, boundaries, or contract. Reply/resolve happens only when the
  outcome is satisfied. Direct-apply iterations are limited to three.
- **Bounded observation:** after full coverage and no blocking review,
  unresolved blocking thread, actionable comment, or failing check, take fresh
  clean snapshots exactly at `30s -> 60s -> 120s`. New blocking signal resets
  the sequence and returns to `needs-rework`. Three clean snapshots permit a
  bounded report for human merge-readiness only.

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Parent plan | `plan/cross-language-skill-candidate-basis-content-corrections/cross-language-skill-candidate-basis-content-corrections.plan.md` | Plan-Creator | Current-truth contract. |
| Parent progression | `plan/cross-language-skill-candidate-basis-content-corrections/cross-language-skill-candidate-basis-content-corrections.step.md` | Plan-Creator | Progression truth. |
| Correction plan | `plan/cross-language-skill-candidate-basis-content-corrections/cross-language-skill-candidate-basis-content-corrections.correction-plan.md` | Plan-Creator | Historical recovery/rework route. |
| Correction progression | `plan/cross-language-skill-candidate-basis-content-corrections/cross-language-skill-candidate-basis-content-corrections.correction-step.md` | Plan-Creator | Historical correction progression. |
| Review log | `plan/cross-language-skill-candidate-basis-content-corrections/cross-language-skill-candidate-basis-content-corrections.review-log.md` | Plan-Creator | Verdict and routing history. |
| Candidate basis | `docs/agent-skills-convergence/cross-language-candidate-basis.md` | Independent Implementer | Sole existing-file write: four named cells. |

## Implementation Steps

1. Plan-Creator records the latest independent Plan-Reviewer `approved`
   verdict and synchronizes the five planning/progression artifacts with the
   completed Phase 4.5 alignment and Main Agent publication route; it does not
   edit the candidate basis.
2. Main Agent performs the already authorized bounded commit and push. It does
   not infer thread coverage, reply/resolution, clean observation, merge,
   release, summary, or close from publication.

## Validation / Acceptance Checks

- Verify the candidate diff changes only the four named cells and expresses
  every locked canonical rule.
- Verify the four-cell record remains explicitly historical/pre-review, the
  latest planning gate is recorded as `approved`, Phase 4.5 alignment is
  complete, and Main Agent alone owns the selected publication route.
- Verify all five artifacts agree that `1885c35` is pushed, ten threads remain
  unresolved, and observation, thread work, merge, and close remain incomplete.
- Verify Phase 7--8 requires fresh signals, coverage/rework, and exactly
  `30s -> 60s -> 120s` before human merge-readiness.

## Reviewer Handoff

The latest independent Plan-Reviewer gate is `approved`. It confirms only the
planning/progression synchronization: the four-cell record remains
historical/pre-review, Phase 4.5 alignment is complete, and Main Agent owns
the authorized publication route. It does not approve candidate content,
thread action, observation, merge, release, summary, or close. The operational
next owner is Main Agent for the bounded commit and push.

```json
{"verdict":"approved","blocking_issues":[],"copilot_feedback_triage":{"ADDRESS":[],"DISCUSS":[],"SKIP":[]}}
```

## Post-merge / release actions

Before human merge, the clean-observation report must exist and a human must
explicitly choose merge handoff. That choice is **STOP POINT 2**: Main Agent
stops immediately before merge and does not poll, infer merge, or start
post-merge work. Phase 9 needs a new explicit human message confirming merge
and authorizing resume. No release action exists.

## Open Questions / Unresolved Items

- Coverage and disposition of the ten unresolved PR #125 threads await the
  fresh-signal PR-loop stage.
