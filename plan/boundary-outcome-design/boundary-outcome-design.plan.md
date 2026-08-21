# Boundary Outcome Design Skill Plan

> **Analysis-layer semantic warning (non-blocking):**
> `analysis/boundary-outcome-design/requirements.md` and
> `analysis/boundary-outcome-design/technical-spec.md` do not exist. This plan
> is therefore authored from the human-approved Boundary Outcome Design draft,
> which is the frozen requirements baseline for this topic. Creator and reviewer
> must not infer additional requirements or regenerate the absent analysis layer.

## Goal / Outcome

Create the stable canonical skill `boundary-outcome-design`. It must guide
semantic Outcome and Exception design across Domain, Application / UseCase,
Port, Adapter, Repository, Unit of Work, and Infrastructure boundaries, without
requiring a particular Result type, Exception hierarchy, or modelling library.

## Scope

- **In scope**:
  - create the canonical `skills/boundary-outcome-design/` skill package at the
    exact paths in **Artifact Paths**;
  - address PR thread `PRRT_kwDOSC_kWs6bDGEX` by regenerating the existing
    canonical inventory snapshot at `artifacts/skills-inventory.jsonl` after
    the complete new canonical skill exists; the independent Implementer may
    change only that generated snapshot for this rework;
  - define the A--D review decision flow: identify layer, vocabulary owner,
    decision consumer, then choose Preserve, Translate, Compress, Promote to an
    application-safe exception, or leave as an unexpected exception;
  - cover semantic compression, lower-layer vocabulary leakage, Port and
    Adapter responsibilities, UseCase outcome interpretation, legitimate
    optional Domain state, Repository and Unit of Work boundaries, Protocol
    limitations, and expected versus unexpected failures;
  - add the locked stable-library README row and bump `VERSION` from `0.77.0`
    to `0.78.0` during `publish-in-progress` after independent approval and
    planner alignment.

- **Out of scope**:
  - application code, code refactors, framework integrations, or concrete
    Exception / Result class hierarchies;
  - mandatory `Result[T, E]`, Unit of Work, Repository, or Adapter patterns;
  - `.github/**`, `.codex/**`, and every other platform projection or
    compatibility surface;
  - any change to the inventory builder or its tests; this topic consumes the
    existing inventory contract without redefining it;
  - tags, GitHub Releases, release notes, or any post-merge release action;
  - architecture, path, or contract changes outside this topic's exact artifact
    set.

## Locked Decisions

- This is a **stable-library-affecting** topic. Its canonical source is
  `skills/boundary-outcome-design/`; no platform projection is created or
  changed in this topic.
- Each layer owns its semantics. Lower-layer facts may influence upper-layer
  decisions, but HTTP, SDK, ORM, database, driver, and transport vocabulary
  must not escape accidentally into a higher-layer contract.
- Outcome granularity follows the receiving layer's meaningful decisions, not
  the number of infrastructure exceptions. Preserve distinctions for distinct
  decisions; compress distinctions that have identical handling.
- A Port describes an inner-layer-required external capability. An Adapter
  translates external representation and failures into Port vocabulary. A
  UseCase may further translate a Port outcome into an operation outcome.
- A Domain object's optional field can be a valid state. It becomes a failure
  only when a particular operation rejects that state.
- A Repository is an outbound Port. Transaction-level outcomes may belong at a
  Unit of Work boundary; this does not imply that all persistence failures occur
  only at commit.
- A Protocol describes dependency shape only. It does not establish an
  exception or runtime failure boundary.
- Expected failures with meaningful caller decisions may become explicit
  outcomes. Programming defects, corrupted invariants, impossible states, and
  unexpected driver failures are not forced into an ever-growing outcome union.
- Stable metadata timing is locked to `publish-in-progress`: after Reviewer
  `approved` and passing Phase 4.5 planner alignment, Main Agent updates
  `README.md` and `VERSION` in the same bounded publication diff. No tag,
  release note, or GitHub Release is part of this topic.
- This plan is the frozen execution contract. The missing optional analysis
  layer is a warning, not permission to reopen scope or invent requirements.

## Boundaries / Exclusions

- Creator writes only the six canonical skill files listed below. Creator does
  not write reviewer verdicts, alter workflow state, update stable metadata, or
  perform git / PR actions. For the planner-confirmed low-severity inventory
  rework, an independent Implementer writes only the generated inventory
  snapshot listed below; it does not reopen the six-file skill draft.
- Reviewer independently evaluates the latest creator draft and records only
  the required JSON verdict in the review-log routing artifact. Reviewer does
  not implement corrections.
- Main Agent owns branch/worktree preparation, Phase 4.5 alignment,
  `publish-in-progress` stable metadata, commit, push, Draft PR, PR routing,
  and the post-merge stop. Main Agent must route any needed correction to a
  separate Creator / Implementer rather than modifying the skill directly.
- The topic must not reopen architecture or path choices recorded above. Any
  needed file outside **Artifact Paths** is plan drift: stop and repair this
  plan before work continues.
- Related skills may be named only to clarify ownership. This skill does not
  absorb generic Python exception hierarchy, model-selection, or framework
  design policy.

## Status / Allowed Transitions

- **Current**: `needs-rework`
- **Execution model**: canonical creator -> independent reviewer -> planner
  alignment -> publish -> Draft PR -> human review / merge handoff. The topic
  stops after merge and does not enter a release phase.
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

Routing notes:

- The independent Plan-Reviewer accepted the planning baseline recorded at
  commit `125c928`; the independent Skill Reviewer has accepted the Creator's
  six canonical skill files. The current state is `needs-rework` at
  `pr-comment-review-and-fix` on Ready PR #123, pending the bounded repair and
  independent re-review before its PR thread can be resolved.
- Apply the standard Phase 4.5 planner-alignment rule. An `approved` reviewer
  verdict may still return the topic to `creator-in-progress` for scope,
  contract, path, ownership, or stable-metadata drift.
- Reviewer feedback that controls rework must be persisted at the exact
  `review-log.md` path; hidden chat is not a routing artifact.
- PR thread `PRRT_kwDOSC_kWs6bDGEX` is planner-confirmed `low`-severity
  artifact-scope drift. Its routing is `IMPLEMENT_PATCH`: the topic moves
  through `pr-open` -> `needs-rework` -> `creator-in-progress` for an
  independent Implementer to regenerate only the canonical inventory snapshot,
  then returns to independent review before the PR thread can be resolved.
- The inventory rework is `ADDRESS`, not `DISCUSS`: a stable canonical skill
  absent from the checked-in canonical inventory is an incomplete published
  artifact, even though the existing builder, tests, and inventory schema stay
  unchanged.
- STOP POINT 1 blocks publication until explicit human commit / push / PR
  authority exists. STOP POINT 2 begins once merge handoff is reached: stop;
  do not poll, sync, tag, release, or infer a resume without a new human
  instruction.

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/boundary-outcome-design/boundary-outcome-design.plan.md` | Planning actor | Frozen repo-visible execution contract |
| Topic progression | `plan/boundary-outcome-design/boundary-outcome-design.step.md` | Planning actor / Main Agent | Current workflow progression and gate truth |
| Topic review log | `plan/boundary-outcome-design/boundary-outcome-design.review-log.md` | Reviewer / Main Agent | Persisted independent review verdicts and rework routing |
| Topic close summary | `plan/boundary-outcome-design/boundary-outcome-design.summary.md` | Main Agent | Current-truth close and human-handoff summary |
| Skill contract | `skills/boundary-outcome-design/SKILL.md` | Creator | Trigger, semantic decision procedure, review output, validation, failure handling, and local references |
| Overview reference | `skills/boundary-outcome-design/reference.md` | Creator | Navigation and concise boundary-reasoning overview |
| Layer semantics reference | `skills/boundary-outcome-design/references/layer-semantics.md` | Creator | Domain, Application / UseCase, Port, and Adapter semantic ownership |
| Persistence failures reference | `skills/boundary-outcome-design/references/persistence-and-failures.md` | Creator | Repository, Unit of Work, Protocol, expected, and unexpected failure guidance |
| Examples | `skills/boundary-outcome-design/examples.md` | Creator | Positive and negative boundary-design scenarios |
| Review checklist | `skills/boundary-outcome-design/checklist.md` | Creator | Repeatable review prompts and anti-pattern detection |
| Canonical inventory builder | `scripts/build_skills_inventory.py` | Existing inventory contract (read-only) | Sole generator for the deterministic canonical inventory; this topic must not modify it |
| Inventory builder tests | `tests/test_build_skills_inventory.py` | Existing inventory contract (read-only) | Existing validation of canonical discovery, record schema, determinism, and hash behavior; this topic must not modify them |
| Generated canonical inventory | `artifacts/skills-inventory.jsonl` | Independent Implementer | Complete deterministic snapshot produced by the existing builder; must contain exactly one `skills/boundary-outcome-design` record and no projection or agent path |
| Stable-library summary | `README.md` | Main Agent | Exact stable-skill row at `publish-in-progress` |
| Repository version baseline | `VERSION` | Main Agent | MINOR bump at `publish-in-progress` |

Artifact path notes:

- This topic changes `README.md` and `VERSION`; it does not change
  `.github/copilot-instructions.md`.
- Planning artifacts are created in Phase 1. During creator implementation,
  they remain workflow truth and are not a substitute for creator-owned skill
  source. The Reviewer / Main Agent update routing artifacts only as their
  respective workflow duties require.
- If a later task needs a path not listed here, stop and repair this plan before
  any implementation, review, publication, or metadata change.

## Stable library metadata

- `README row`: insert exactly
  `| \`boundary-outcome-design\` | guides semantic Outcome and exception design across Domain, Application, Port, Adapter, Repository, and Unit of Work boundaries |`
  in the README skills table after
  `business-to-technical-translation` and before `copilot-instructions-init`.
- `VERSION bump`: `0.77.0` -> `0.78.0` (MINOR).
- `timing`: `publish-in-progress`, after independent reviewer `approved` and
  Phase 4.5 planner alignment; include both metadata files in the same bounded
  publication diff as the approved skill.
- `rationale`: a new canonical stable-library skill needs discoverability in the
  human-facing catalog and a corresponding backward-compatible MINOR version.
- `release notes / tags`: none. Post-merge has no tag, release-note, or GitHub
  Release action, and `merged` is terminal for this topic.

## Implementation Steps

1. Create the six creator-owned skill files at their exact canonical paths.
   Make `SKILL.md` the concise executable entry point and declare every
   companion file through local references.
2. Encode the A--D review decision flow and the boundary principles in the
   locked decisions. State that the selected action is context-sensitive rather
   than a mandatory Result / Exception taxonomy.
3. Put layer-specific meaning in the two references: one for Domain,
   Application / UseCase, Port, and Adapter semantics; one for Repository,
   Unit of Work, Protocol, expected failure, and unexpected failure handling.
4. Add examples and checklist coverage for infrastructure vocabulary leakage,
   one-to-one exception mirroring, over-compression, optional-means-failure,
   and protocol-means-safe. Require a review output with observed boundary,
   potential vocabulary leak, decision-relevant distinctions, suggested
   translation point, and suggested outcome granularity.
5. Keep scope neutral: do not prescribe concrete outcome classes, force every
   function to return Result, or turn this into a Python framework / code
   implementation guide. Hand the completed draft to independent review as
   `review-ready`.
6. For PR thread `PRRT_kwDOSC_kWs6bDGEX`, after the planner contract update,
   an independent Implementer runs the unchanged
   `python3 scripts/build_skills_inventory.py --repo-root .` only after the
   complete canonical skill package is present. This overwrites only
   `artifacts/skills-inventory.jsonl`; it must not hand-author JSONL records or
   modify the builder or tests.

## Validation / Acceptance Checks

- All twelve exact artifact paths exist at the appropriate phase; all six
  creator-owned companion files are declared by `SKILL.md` local references.
- The skill frontmatter and body agree on trigger, purpose, input, process,
  validation, failure handling, and exclusions.
- Guidance distinguishes infrastructure facts, Port capability outcomes,
  UseCase decisions, and Domain state; it does not leak lower vocabulary into
  higher contracts by accident.
- Examples prove that distinct caller decisions preserve distinctions and equal
  decisions may compress them. They also prove that an optional value can be a
  valid Domain state and Protocol does not guarantee runtime safety.
- The skill does not mandate a Result type, an Exception hierarchy, Unit of
  Work, or a uniform outcome taxonomy.
- The topic plan uses only canonical status transitions, keeps Creator,
  Reviewer, and Main Agent ownership separate, and contains the one JSON
  reviewer handoff object below.
- At `publish-in-progress`, README contains the exact row once and at the exact
  placement; `VERSION` is exactly `0.78.0`. No platform projection is changed.
- The checked-in inventory is regenerated by the existing builder and validates
  as a complete, sorted canonical `skills/` snapshot. It contains exactly one
  `skills/boundary-outcome-design` record, no `agents/` or platform-projection
  record, and a second unchanged builder run is byte-identical. The builder and
  its tests remain unchanged.
- Independent Reviewer returns `approved` or `needs-rework` through the JSON
  contract. Main Agent may advance only after approved review and passing Phase
  4.5 alignment.

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

- After a human merges the Draft PR, the topic reaches `merged` and is
  terminal for release purposes. No tag, release note, GitHub Release, or
  additional implementation is authorized by this topic after merge.
- STOP POINT 2 requires a new explicit human resume before Phase 9 local sync
  and final summary handoff. That resume does not authorize a tag, a release,
  or any further implementation.

## Open Questions / Unresolved Items

- None. The human-approved Boundary Outcome Design draft, stable-library timing,
  exact artifact paths, README placement, version bump, and no-release decision
  are locked.
