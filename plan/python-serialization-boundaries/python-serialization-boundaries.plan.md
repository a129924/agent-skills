# Python Serialization Boundaries Skill Plan

## Goal / Outcome

Create a repo-visible execution plan for a new stable skill at
`.github/skills/python-serialization-boundaries/` that teaches semantic
boundary discipline for API / DB / message-queue data handling. The completed
topic should produce a review-ready skill that defines where transport shapes
must be translated, how internal models must stay separate from wire schemas
when semantics diverge, how missing/null/unchanged intent must be preserved, and
how type normalization and deep conversion prevent raw payload leakage into
internal logic.

## Scope

- **In scope**:
  - create `.github/skills/python-serialization-boundaries/SKILL.md`
  - create `.github/skills/python-serialization-boundaries/reference.md` as the
    focused overview and navigation file
  - create `.github/skills/python-serialization-boundaries/examples.md` for
    branching examples, anti-patterns, and split signals
  - define first-draft rules for:
    - where raw dict / JSON / payload shapes should stop
    - when and where conversion into internal objects or typed records should
      happen
    - how to distinguish transport schemas from internal value objects
    - how PATCH-like input must distinguish missing vs null vs unchanged
    - how input DTO and output DTO may be semantically independent
    - how UUID / datetime / decimal / enum-like primitives should be normalized
      at the boundary before entering core business logic
    - how deep conversion should prevent nested raw dict/list leakage
    - how lossy conversion and non-round-trip output are legitimate when the
      boundary contract requires them
    - how to decide when a boundary schema stays local versus becomes a shared
      contract
  - declare stable-library promotion timing for `README.md` and `VERSION`
  - declare the post-merge tag action for this new stable skill topic

- **Out of scope**:
  - generic `json.dumps` / `json.loads` tutorials
  - framework-specific schema-library selection as the default path
  - broad package architecture, bounded-context, or theme-dependency rules
  - `Protocol`, `ABC`, dataclass, or interface-selection policy
  - package import/export policy or `__all__` rules
  - error hierarchy and exception-translation policy
  - repository scaffold / retrofit execution
  - ORM/query design, HTTP framework mapping, or queue infrastructure setup

## Locked Decisions

- This topic is a **stable-library-affecting topic** with declared publish and
  release timing.
- The skill's primary scope is **semantic boundary discipline**, not a general
  serialization tutorial and not a full architecture-policy skill.
- **Scope breadth is locked to `semantic-translation-boundaries`**, meaning:
  - the skill should treat transport-to-internal translation as a semantic gate
  - the skill should emphasize asymmetry between external payload meaning and
    internal model meaning
  - the skill should not broaden into module dependency direction or theme
    independence rules
- **Semantic-gatekeeper emphasis is locked**, meaning:
  - PATCH semantics must distinguish missing, null, and unchanged intent
  - input DTO and output DTO may be intentionally different
  - boundary conversion is the place for type normalization
  - deep conversion is the default when the boundary claims to produce an
    internal object
  - lossy conversion is legitimate; round-trip symmetry is not a universal rule
- **Framework-neutrality is locked**, meaning:
  - sentinel-style handling is the preferred neutral framing for missing/null
    separation
  - framework-specific mechanisms such as Pydantic exclusion logic may appear as
    examples, but they are not the mandatory portable rule
- **Boundary ownership is locked**, meaning:
  - `python-type-hints-strict` owns generic typing rules and syntax, while this
    topic only decides when stronger types must replace transport primitives at
    the boundary
  - `python-model-selection` owns `Enum`, dataclass, `ABC`, and `Protocol`
    selection
  - `python-error-handling` owns exception hierarchy and translation policy
  - `python-module-boundaries` owns import/export and public gateway rules
  - `python-package-layout` owns package/distribution structure
  - a future `python-library-architecture` topic would own theme independence,
    `core`-layer policy, and dependency direction
- **Stable-library timing is locked to `stable-library-affecting-now`**, meaning:
  - this topic should update `README.md` and `VERSION` at
    `publish-in-progress`
  - a post-merge tag action is expected if the topic reaches the stable library
- **Version baseline**:
  - guidance should work for **Python 3.10+**
  - examples may assume modern typing syntax already used by this repository

## Boundaries / Exclusions

- `python-type-hints-strict`
  - owns generic typing policy, annotation form, and strict-type ergonomics
  - this topic only decides when raw transport primitives must be normalized to
    stronger semantic types at the boundary

- `python-model-selection`
  - owns dataclass / `Enum` / `ABC` / `Protocol` construct choice
  - this topic may mention typed records or internal objects, but it does not
    choose the modeling construct family

- `python-error-handling`
  - owns custom error hierarchy, translation boundaries, and propagation rules
  - this topic may mention invalid payload or boundary failure conceptually, but
    it does not define exception policy

- `python-module-boundaries`
  - owns package gateways, `__all__`, deep-import avoidance, and import-time
    safety
  - this topic only decides how data shapes cross API / DB / queue boundaries

- `python-package-layout`
  - owns where package code, CLI modules, tests, and package data live
  - this topic only decides how external shapes are translated once the code is
    already in the package

- Future `python-library-architecture` or similar topic
  - would own theme independence, `core` layer meaning, and dependency direction
  - this topic should stay data-boundary-focused and not define whole-library
    governance rules

## Status / Allowed Transitions

**Current status**: `released`

Canonical allowed transitions:
- `planned` → `creator-in-progress` (when branch is prepared and drafting starts)
- `creator-in-progress` → `review-ready` (when creator finishes draft)
- `review-ready` → `reviewer-in-progress` (when handed to reviewer)
- `reviewer-in-progress` → `approved` | `needs-rework` (reviewer verdict)
- `needs-rework` → `creator-in-progress` (if rework required)
- `approved` → `creator-in-progress` (if planner alignment or review feedback
  requires a creator revision before publish)
- `approved` → `publish-in-progress` (if stable-library update approved)
- `publish-in-progress` → `pr-open` (when PR is created)
- `publish-in-progress` → `merged` (if merge occurs without an intermediate
  long-lived PR loop)
- `pr-open` → `needs-rework` (if PR review or checks require a return to creator
  work)
- `pr-open` → `merged` (when PR is merged)
- `merged` → `released` (when version and tag actions complete)
- `released` → terminal

Routing notes:
- Follow the standard Phase 4.5 planner-alignment rule from
  `plan/agent-handoff-workflow.md`.
- STOP POINT 1 applies before commit / push / PR creation.
- STOP POINT 2 applies after merge handoff; release work resumes only after a
  new explicit human message.

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/python-serialization-boundaries/python-serialization-boundaries.plan.md` | Planning actor | Repo-visible execution contract for this topic |
| Skill contract | `.github/skills/python-serialization-boundaries/SKILL.md` | Creator | Executable skill contract with trigger, process, examples, boundaries, and local references |
| Focused reference | `.github/skills/python-serialization-boundaries/reference.md` | Creator | Stable semantic-boundary rules, exclusions, and decision notes |
| Layered examples | `.github/skills/python-serialization-boundaries/examples.md` | Creator | Branching scenarios such as PATCH semantics, asymmetric DTOs, deep conversion, and lossy output cases |
| Stable library row | `README.md` | Main Agent | Add the stable-skill table row for `python-serialization-boundaries` at publish time |
| Repo version baseline | `VERSION` | Main Agent | Apply the next MINOR version bump when the topic is promoted to the stable library |

Artifact path notes:
- This topic modifies `README.md` and `VERSION`.
- This topic does not modify `.github/copilot-instructions.md`.
- Treat the listed paths as an executable contract; if later work drifts outside
  them, stop and repair the topic plan before continuing execution.

## Stable library metadata

- `README row`: add a stable-skill row for `python-serialization-boundaries` in
  the README skills table; place it after
  `python-retrofit-plan-authoring` and before `sense-env-scaffold`
- `VERSION bump`: next MINOR bump from the repository's current `VERSION`
- `timing`: `publish-in-progress`
- `rationale`: this topic adds a new stable Python skill to the library, so the
  stable skill table and repository version baseline must be updated when the
  approved draft is published
- `release notes`: no separate release-notes artifact is planned; the annotated
  git tag message is the release-facing metadata for this topic

## Implementation Steps

1. **Branch preparation** (via Main Agent):
   - create or repair the semantic execution branch for
     `python-serialization-boundaries`
   - verify worktree readiness before creator work begins
   - do not start drafting from chat-only state once repo-visible plan exists

2. **Draft phase** (via `agent-skill-creator`):
   - create `.github/skills/python-serialization-boundaries/SKILL.md` with:
     - explicit trigger: when to use this skill
     - process: decision path for transport-to-internal translation boundaries
     - concise positive/negative examples
     - clear boundaries vs related skills
   - create `.github/skills/python-serialization-boundaries/reference.md` as
     overview
   - create `.github/skills/python-serialization-boundaries/examples.md` for
     branching scenarios
   - keep the draft portable and framework-neutral in its core rule set
   - update topic plan status to `review-ready`

3. **Review phase** (via independent `agent-skill-reviewer`):
   - verify required files present (SKILL.md, reference.md, examples.md)
   - verify the skill stays focused on semantic boundary translation rather than
     broad architecture or schema-library policy
   - verify boundaries are explicit vs `python-type-hints-strict`,
     `python-model-selection`, `python-error-handling`,
     `python-module-boundaries`, and `python-package-layout`
   - verify no hidden repo context is assumed
   - return `approved` or `needs-rework`
   - update topic plan status to reviewer verdict

4. **Publish phase** (if `approved`):
   - commit skill files to the execution branch
   - add the `python-serialization-boundaries` row to `README.md` after
     `python-retrofit-plan-authoring` and before `sense-env-scaffold`
   - update `VERSION` (MINOR bump, e.g., X.Y.Z → X.(Y+1).0)
   - open PR after STOP POINT 1 approval
   - after merge and explicit human resume, create annotated git tag matching the
     version and push it
   - update topic plan status to `released`

## Validation / Acceptance Checks

**Draft must pass**:
- [ ] SKILL.md includes explicit trigger (when to use)
- [ ] SKILL.md includes concise positive and negative examples
- [ ] reference.md explains semantic-gatekeeper framing and hard boundary rules
- [ ] examples.md covers branching scenarios such as missing/null/unchanged,
      asymmetric input/output DTOs, type normalization, deep conversion, and
      lossy non-round-trip output
- [ ] the skill clearly distinguishes data-boundary rules from architecture,
      model-selection, typing, and error-handling rules
- [ ] no file assumes hidden repo context or framework-specific mandatory tools

**Review phase verdict**: `approved` or `needs-rework`

**Publish phase success**:
- [ ] committed to the execution branch
- [ ] README.md updated with the exact stable-skill row placement
- [ ] VERSION bumped to next MINOR version
- [ ] PR opened only after STOP POINT 1 approval
- [ ] post-merge tag created and pushed after explicit STOP POINT 2 resume
- [ ] status verified as `released`

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

## Post-merge / Release Actions

When `approved` and merged to dev:

1. **Stable-library promotion** (stable-library-affecting-now):
   - README.md row added after `python-retrofit-plan-authoring` and before
     `sense-env-scaffold`
   - VERSION bumped: X.Y.Z → X.(Y+1).0
   - plan status updated to `publish-in-progress`

2. **Release tagging** (post-merge, after explicit human resume):
   - Create annotated tag matching the version:
     `git tag -a v<VERSION> -m "Release v<VERSION>: add python-serialization-boundaries skill"`
   - Push tag: `git push origin v<VERSION>`
   - plan status updated to `released`

3. **Verification**:
   - Confirm tag exists on remote
   - Confirm README includes the new skill row
   - Confirm VERSION file matches the new version

## Open Questions / Unresolved Items

- None at plan creation time. The first-draft boundary is locked to semantic
  transport-to-internal translation discipline rather than whole-library
  architecture governance.

All locked decisions are explicit. All workflow phases are defined. All
transition rules match canonical handoff-workflow semantics.
