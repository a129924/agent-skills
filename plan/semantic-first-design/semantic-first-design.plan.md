# Semantic-First Design — Topic Plan

## Analysis-layer routing

**Semantic warning — optional analysis layer absent:** neither
`analysis/semantic-first-design/requirements.md` nor
`analysis/semantic-first-design/technical-spec.md` exists. This plan uses the
explicit human decisions for this topic. If either artifact is introduced,
stop and reconcile its authority before changing this plan.

## Goal / Outcome

- Maintain a Python-first reusable `semantic-first-design` skill whose important
  semantics are visible locally in names, types, signatures, composition, and
  distinguishable failure paths.
- Repair the PR feedback without changing the topic's architecture, canonical
  source surface, stable-library intent, or release boundary.

## Scope

- **In scope**:
  - Repair this topic's three planning artifacts and re-run independent
    planning review before any implementation repair.
  - Maintain the exact six-file canonical skill document set listed in
    `Artifact Paths`, including the three named split references.
  - Regenerate the checked-in canonical-skill inventory once, only after all
    six canonical skill files are final.
  - Keep the approved README row and `VERSION` `0.78.0` stable unless a
    reviewer identifies a directly related correction.

- **Out of scope**:
  - Changes to existing specialised Python skills or their contracts.
  - `.github/**`, `.codex/**`, platform projections, runtime code, tags,
    releases, merge, and post-merge cleanup.

## Locked Decisions

- This is a Python-first semantic guardrail, not a replacement for specialised
  Python design skills.
- The canonical implementation is exactly this six-file document set:
  `skills/semantic-first-design/SKILL.md`, `reference.md`, `examples.md`,
  `references/contracts-and-state.md`, `references/policy-and-failure.md`, and
  `references/boundary-composition-and-abstraction.md`.
- `reference.md` is a short index and routing surface; the split references own
  the detailed material named by their filenames. `examples.md` supplies
  compact positive and negative examples only.
- The skill output narrows the assessment to **one material ambiguity** and its
  smallest explicit distinction; it does not emit a prioritized collection of
  ambiguities.
- The normal-absence example keeps `customer_id: str`; this topic must not
  invent `CustomerId` merely to demonstrate semantic-first design.
- Serialization is a bounded handoff: the skill and one example may identify a
  serialization-boundary ambiguity and route the concrete decision to
  `python-serialization-boundaries`; they must not redefine that skill's rules.
- Stable-library metadata remains published: README row and VERSION `0.78.0`
  are already part of the PR. There is no automatic release or tag after merge.

## Boundaries / Exclusions

- Plan-Creator changes only this plan, progression, and review-routing log.
- Implementer changes only listed implementation/inventory paths; it does not
  alter existing specialised skills or platform projections.
- Plan-Reviewer independently reviews the repaired planning artifacts before
  any Implementer work. Reviewer independently evaluates implementation work.
- Human PR feedback is triaged in the review log; it does not self-approve the
  repair or bypass either independent review.
- A path, contract, or scope request outside `Artifact Paths` requires a new
  planning repair before execution continues.

## Status / Allowed Transitions

- **Historical PR return**: `pr-open` -> `needs-rework` occurred after human
  review. It records why this bounded repair started; it is not the current
  active stage.
- **Historical renewed review**: the renewed Plan-Reviewer returned `approved`;
  the renewed Implementation Reviewer later returned `needs-rework` solely for
  a planning lifecycle/log contradiction. The latter is the received trigger
  for this planning-state repair; all skill and inventory thread content passed.
- **Historical post-repair planning approval**: the independent Plan-Reviewer
  returned `approved` for this Planning-state repair. That fifth recorded
  verdict completes planning repair and does not require new Implementer work.
- **Historical final implementation approval**: the sixth recorded Final
  Implementation Reviewer verdict is `approved`. All six review gates are
  complete; no further content repair is required.
- **Current**: `publish-in-progress`. The next actor is the
  Implementer/Main Agent publication flow: Main Agent owns publication, with
  Implementer validation support only. Commit/push still require passing
  validation and the explicit prior user authorization already recorded.
- **Historical completed stages**: original plan authoring, independent
  planning approval, feature implementation, independent implementation
  approval, publish preparation, commit/push, and PR opening remain completed
  history. They are not re-executed or represented as fresh approvals.
- **Current repair lifecycle**:
  1. Historical `needs-rework` -> `creator-in-progress` -> `review-ready`:
     Plan-Creator completed the first bounded planning-artifact repair.
  2. Historical `review-ready` -> `reviewer-in-progress` -> `approved`:
     the renewed Plan-Reviewer approved that prior planning round.
  3. Historical implementation work and its renewed Reviewer pass reached
     `needs-rework` only because planning lifecycle/log state contradicted the
     recorded review history; skill and inventory content passed.
  4. Historical `needs-rework` -> `creator-in-progress` -> `review-ready` ->
     `reviewer-in-progress` -> `approved`: Plan-Creator completed this
     Planning-state repair and the post-repair Plan-Reviewer approved it.
  5. Historical final implementation review `reviewer-in-progress` ->
     `approved`: the sixth review gate accepted the existing seven fixes.
  6. Current `approved` -> `publish-in-progress`: no content repair remains.
     Main Agent may commit/push only after current validation passes and the
     explicit prior user authorization is confirmed; the existing PR then
     returns to `pr-open` for human review.
- **Allowed transitions** additionally retain the canonical historical path:
  `planned` -> `creator-in-progress` -> `review-ready` ->
  `reviewer-in-progress` -> `approved` -> `publish-in-progress` -> `pr-open`;
  `pr-open` -> `needs-rework|merged`; `merged` -> terminal.
- Commit/push requires the already-authorized topic scope plus passing current
  validation. Human review remains required after the new push; merge, tag,
  release, and post-merge work are stop points.

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/semantic-first-design/semantic-first-design.plan.md` | Plan-Creator | Current execution contract and locked scope |
| Topic progression | `plan/semantic-first-design/semantic-first-design.step.md` | Plan-Creator; then Main Agent | Current stage readiness and gates |
| Review routing log | `plan/semantic-first-design/semantic-first-design.review-log.md` | Plan-Creator initializes; independent reviewers append verdicts | Historical verdicts and PR-feedback routing |
| Canonical skill instructions | `skills/semantic-first-design/SKILL.md` | Implementer | Python-first trigger, output, boundary, workflow, and local-reference contract |
| Short semantic index | `skills/semantic-first-design/reference.md` | Implementer | Concise decision index routing to the split references and specialised skills |
| Worked examples | `skills/semantic-first-design/examples.md` | Implementer | Positive and negative ambiguity-resolution examples, including bounded serialization handoff |
| Contracts and state reference | `skills/semantic-first-design/references/contracts-and-state.md` | Implementer | Truthful contracts, earned guarantees, and normal absence |
| Policy and failure reference | `skills/semantic-first-design/references/policy-and-failure.md` | Implementer | Boolean/policy choices and distinguishable failure semantics |
| Boundary, composition, and abstraction reference | `skills/semantic-first-design/references/boundary-composition-and-abstraction.md` | Implementer | External translation, visible composition, and meaningful variation boundaries |
| Generated skills inventory | `artifacts/skills-inventory.jsonl` | Implementer via generator | Checked-in canonical-skill completeness and tree-hash snapshot; never hand-edit |
| Stable-library index | `README.md` | Main Agent | Existing approved semantic-first-design row |
| Repository version | `VERSION` | Main Agent | Existing `0.78.0` stable-library version |

Artifact path notes:

- After all six canonical skill documents are final, Implementer invokes
  `scripts/build_skills_inventory.py` **exactly once** with its default output
  to regenerate `artifacts/skills-inventory.jsonl`. No role hand-edits that
  generated file.
- The managed feature-worktree is execution context, not a repo-visible
  artifact. No other tracked path is authorized by this plan.

## Stable library metadata

- **README row** remains exactly:

  ```markdown
  | `semantic-first-design` | guides Python-first design and review toward explicit contracts, states, policies, boundaries, composition, and failure semantics |
  ```

- **VERSION** remains `0.78.0`.
- **Timing**: those stable-library changes were published in the original
  `publish-in-progress` stage. This repair does not change release timing.
- **Release**: after merge, STOP POINT 2 applies. Any tag or release needs a
  new explicit human authorization.

## Implementation Steps

1. Implementer updates the exact six-file document set. `SKILL.md` declares
   each local reference, keeps `reference.md` short, and emits one material
   ambiguity, its smallest distinction, caller guarantee, and bounded route.
2. Implementer places contract/state/normal-absence guidance only in
   `references/contracts-and-state.md`; boolean/policy and distinguishable
   failure guidance only in `references/policy-and-failure.md`; and boundary,
   visible composition, and abstraction guidance only in
   `references/boundary-composition-and-abstraction.md`.
3. Implementer updates examples so normal absence uses
   `find_customer(customer_id: str) -> Customer | None`, and adds one bounded
   serialization example that routes to `python-serialization-boundaries`
   without specifying its concrete policy.
4. After all six canonical documents are final, Implementer runs
   `scripts/build_skills_inventory.py` once with default output, validates the
   generated JSONL, and returns `review-ready`.

## Validation / Acceptance Checks

- The plan, step, and review log agree that all six review gates are complete,
  including the final Implementation Reviewer `approved`; current status is
  `publish-in-progress`, and no content repair remains.
- Publication may proceed only after validation passes and explicit prior user
  authorization for commit/push is confirmed. The next publication flow is
  Main Agent-owned with Implementer validation support.
- Every `## ... verdict` section in the review log contains exactly one valid
  JSON object; the preserved historical approved verdicts remain byte-for-byte
  equivalent in content. PR-feedback triage is prose outside verdict sections.
- Exactly the six named canonical skill documents exist with non-overlapping
  roles. `SKILL.md` and `reference.md` declare the local reference paths.
- The skill output contains one material ambiguity, not a prioritized list;
  the absence example uses `customer_id: str`; and the serialization handoff is
  bounded to `python-serialization-boundaries`.
- `artifacts/skills-inventory.jsonl` is regenerated once by the default
  `scripts/build_skills_inventory.py` output after all canonical documents are
  final, is valid JSONL, and contains the resulting semantic-first-design hash.
- Validate planning contract sections, JSON objects, and whitespace before
  handoff. Validate skill YAML/body alignment, local references, examples, and
  inventory after implementation.
- Existing specialised Python skills, platform projections, README row, and
  VERSION remain unchanged during planning repair.

## Reviewer Handoff

```json
{
  "verdict": "approved",
  "blocking_issues": [],
  "copilot_feedback_triage": {
    "ADDRESS": [
      "Run publication prerequisites; commit and push only after validation and explicit prior user authorization."
    ],
    "DISCUSS": [],
    "SKIP": []
  }
}
```

## Post-merge / release actions

- After a human merges the PR, stop at STOP POINT 2.
- There is no automatic release, annotated tag, release note, or local cleanup.
- A new explicit human resume and release authorization are required before
  assessing any `v0.78.0` tag or release.

## Open Questions / Unresolved Items

- None. The PR feedback has a bounded planning repair direction. Independent
  review is required for acceptance; it is not an unresolved design choice.
