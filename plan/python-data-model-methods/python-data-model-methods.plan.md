# Python Data Model Methods Skill Plan

## Goal / Outcome

Create a repo-visible execution plan for a new stable skill at
`.github/skills/python-data-model-methods/` that teaches when Python code
should implement foundational data-model methods and base container protocols,
when `@dataclass`-generated behavior is sufficient, and when manual
implementation is required to preserve explicit semantics and safety. The
completed topic should produce a review-ready skill that covers `__init__`,
`__repr__`, `__str__`, `__eq__`, `__hash__`, `__bool__`, `__len__`,
`__getitem__`, `__contains__`, and `__iter__`, while routing async protocol
questions to `python-async-await` and iteration-heavy design questions to
`python-generators-iterators`.

## Scope

- **In scope**:
  - create `.github/skills/python-data-model-methods/SKILL.md`
  - create `.github/skills/python-data-model-methods/reference.md` as the
    focused overview and navigation file
  - split deeper reference material into
    `.github/skills/python-data-model-methods/references/` when topic breadth
    warrants it
  - create `.github/skills/python-data-model-methods/examples.md` for layered
    examples, anti-patterns, and split signals
  - define first-draft rules for:
    - `__init__` responsibility and constructor boundaries
    - `__repr__` as developer-meaningful diagnostics
    - `__str__` versus `__repr__`
    - `__eq__` / `__hash__` pairing safety, especially for mutable objects
    - `__bool__` as substantive truth semantics
    - `__len__`, `__getitem__`, `__contains__`, and `__iter__` as base
      container behavior declarations
    - when `@dataclass`-generated dunders are safe versus when manual override
      is required
  - declare stable-library promotion timing for `README.md` and `VERSION`
  - declare the post-merge tag action for this new stable skill topic

- **Out of scope**:
  - async data-model methods such as `__aiter__` and `__anext__` (owned by
    `python-async-await`)
  - complex iterator logic, stateful iteration design, or custom iterator
    strategy beyond base container declaration (owned by
    `python-generators-iterators`)
  - operator-overloading families such as arithmetic, ordering, numeric, or bit
    operations
  - descriptors, `__getattr__`, `__getattribute__`, `__setattr__`, and other
    attribute-access protocol deep dives
  - `__new__`, `__del__`, metaclasses, or object-lifecycle edge-case policy
  - a general `@dataclass` tutorial or broad model-selection guidance

## Locked Decisions

- This topic is a **stable-library-affecting topic** with declared publish and
  release timing.
- The skill's primary scope is **foundational data-model semantics** for
  ordinary classes and container-like objects, not async protocols or operator
  overloading.
- **Scope breadth is locked to `foundational-dunders-plus-base-container-protocol`**,
  meaning:
  - `__init__`, `__repr__`, `__str__`, `__eq__`, `__hash__`, and `__bool__`
    are mainline topics
  - `__len__`, `__getitem__`, `__contains__`, and `__iter__` are also mainline
    topics because they declare container-like meaning
  - the topic should define when a class should behave like a container without
    drifting into complex iterator implementation guidance
- **`@dataclass` boundary guidance is in scope**, meaning:
  - generated `__eq__` / `__hash__` behavior must be assessed explicitly
  - the skill should define when generated behavior is acceptable and when
    manual override is required for mutability, hashing, or semantic clarity
  - the topic should frame this as an explicit-vs-implicit safety boundary, not
    as a general dataclass selection tutorial
- **Stable-library timing is locked to `stable-library-affecting-now`**, meaning:
  - this topic should update `README.md` and `VERSION` at
    `publish-in-progress`
  - a post-merge tag action is expected if the topic reaches stable library
- **Boundary stance**:
  - keep the topic **sync-only**
  - allow only a brief async signpost to `python-async-await`
  - do not let container-protocol examples become iteration-strategy or
    generator-design guidance
- **Core semantic emphasis**:
  - `__repr__` must optimize for developer-meaningful diagnostics
  - `__bool__` must reflect substantive emptiness / truth semantics rather than
    cosmetic convenience
  - `__eq__` / `__hash__` pairing safety is a central decision path, especially
    for mutable objects
- **Version baseline**:
  - implementation guidance should work on **Python 3.10+** to match the
    repository's existing Python typing baseline
  - examples may use modern built-in generics and PEP 604 unions
  - examples should avoid Python 3.11+ only syntax unless clearly version-gated

## Boundaries / Exclusions

- `python-class-design`
  - owns public surface design, constructor thinness, instance-state discipline,
    and broad class-shape guidance
  - this topic only decides which data-model methods to implement and how to
    keep their semantics explicit
- `python-model-selection`
  - owns construct choice among `Enum`, `dataclass`, `ABC`, and `Protocol`
  - this topic may discuss `@dataclass` only when generated dunders affect
    semantic safety; it must not become a general construct-selection skill
- `python-generators-iterators`
  - owns generator functions, iterator classes, iterator exhaustion, and deeper
    iteration semantics
  - this topic may mention `__iter__` only as a container behavior declaration
    and should hand off if iteration strategy becomes the main problem
- `python-async-await`
  - owns async protocols such as `__aiter__`, `__anext__`, and async
    I/O-oriented iteration
  - this topic may provide only a brief signpost to that skill
- `python-api-signature`
  - owns public function and method signature shape
  - this topic should not drift into broad parameter-ordering or API-call
    contract design
- If later work needs operator overloading, descriptor policy, async protocol
  design, or lifecycle hooks such as `__new__`, stop and split that into a
  separate topic instead of broadening this skill.

## Status / Allowed Transitions

- **Current**: `planned`
- **Execution model**: follow the canonical creator -> reviewer -> publish ->
  merge -> release path; this topic reaches `released` because it declares a
  post-merge tag action.
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
  - `merged` -> `released`
  - `released` -> terminal

Routing notes:

- Use the standard Phase 4.5 planner-alignment checkpoint from
  `plan/agent-handoff-workflow.md`.
- If creator or reviewer drifts into operator overloading, descriptors, async
  data-model methods, or deep iterator strategy, route back to
  `creator-in-progress` and repair scope before publish.

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/python-data-model-methods/python-data-model-methods.plan.md` | Planning actor | Repo-visible execution contract for this topic |
| Skill contract | `.github/skills/python-data-model-methods/SKILL.md` | Creator | Executable skill instructions for general Python data-model method decisions |
| Reference overview | `.github/skills/python-data-model-methods/reference.md` | Creator | Focused overview and navigation file for the data-model method reference layer |
| Split references | `.github/skills/python-data-model-methods/references/` | Creator | Topic-specific deep reference files if `reference.md` becomes too broad |
| Detailed examples | `.github/skills/python-data-model-methods/examples.md` | Creator | Multi-path examples, anti-patterns, and split signals for dunder and container-protocol choices |
| Stable-library summary | `README.md` | Main Agent | Add the stable-library row for `python-data-model-methods` after approval |
| Repo version baseline | `VERSION` | Main Agent | Bump the repository version for a new stable skill |

Artifact path notes:

- This topic does **not** modify `.github/copilot-instructions.md`,
  `plan/agent-handoff-workflow.md`, or any existing `python-*` skill folder.
- These paths are an executable contract.
- If later work tries to add async protocol examples, operator-overloading
  subfolders, or unrelated repo surfaces outside these paths, stop and repair
  the plan or split the work into a separate topic.

## Stable library metadata

### README row

- Table: `## Current skills`
- Exact row:

  `| \`python-data-model-methods\` | defines general Python data-model method rules for choosing foundational dunder methods, base container protocols, dataclass-generated behavior boundaries, and safe equality/hash semantics |`

- Position:
  - after `python-class-design`
  - before `python-api-signature`

### VERSION bump

- Current: `0.22.0`
- Direction: `MINOR`
- New: `0.23.0`
- Reason: new stable skill, non-breaking capability addition

### Timing

- README / VERSION timing: `publish-in-progress`
- Reason: the PR should show both the new stable skill and the stable-library
  surfaces it promotes

### Additional release metadata

- Tag action: create and push annotated tag `v0.23.0` at `release`
- Release notes artifact: none in this topic
- GitHub Release object: none in this topic unless a later release-specific
  topic adds one

## Implementation Steps

### Creator Phase (after plan approval)

1. Create `.github/skills/python-data-model-methods/`.
2. Draft `SKILL.md` with the required repository shape:
   - YAML frontmatter
   - Purpose
   - Trigger / When to use
   - Inputs
   - Process
   - Examples
   - Outputs
   - Boundaries
   - Local references
3. Keep the mainline trigger focused on foundational data-model decisions, not
   async protocols, operator overloading, or broad class-design guidance.
4. In `SKILL.md`, make the following mainline decision paths explicit:
   - when `__repr__` alone is enough versus when `__str__` adds value
   - when `__eq__` requires explicit `__hash__` treatment
   - when `__bool__` should be omitted versus defined
   - when a class should expose base container protocols
   - when `@dataclass`-generated behavior is sufficient versus risky
5. Draft the reference layer as `reference.md` + optional `references/`:
   - `reference.md` as the focused overview and navigation file
   - if `reference.md` becomes > 1000 tokens or covers > 3 logical topics,
     split into `references/` with topic-specific files
6. Draft `examples.md` with:
   - positive patterns for representation, truth semantics, equality/hash
     safety, and base container declaration
   - anti-patterns for meaningless `__repr__`, unsafe hashing of mutable
     objects, cosmetic `__bool__`, and accidental over-containerization
   - split signals for `@dataclass` generation versus manual implementation
7. Ensure all examples are self-contained and runnable on Python 3.10+.
8. Mark any examples requiring Python 3.11+ or later as version-gated notes.
9. Verify no drift into async protocols, operator overloading, descriptor policy,
   or deep iterator-strategy guidance.

### Creator deliverable summary

- review-ready `.github/skills/python-data-model-methods/` folder with:
  - `SKILL.md` (required)
  - `reference.md` (required)
  - optional `references/` if reference depth requires splitting
  - `examples.md` (required for branching topic)
- all files contain explicit examples and clear boundaries
- all code examples run on Python 3.10+ or are clearly version-gated

## Validation / Acceptance Checks

1. **Path exactness**: artifact paths in the creator draft match those listed in
   `Artifact Paths` section.
2. **Scope enforcement**: no async data-model guidance, operator-overloading
   policy, descriptor deep dive, or lifecycle-hook guidance in the new skill.
3. **Boundary clarity**: skill's `SKILL.md` explicitly states what
   `python-class-design`, `python-model-selection`,
   `python-generators-iterators`, and `python-async-await` own.
4. **Semantic clarity**: `__repr__` guidance emphasizes diagnostic value,
   `__bool__` guidance emphasizes substantive truth semantics, and container
   protocols are framed as behavior declarations rather than mere convenience.
5. **Equality/hash safety**: the skill treats `__eq__` / `__hash__` as a linked
   decision path and covers mutable-object safety.
6. **Dataclass boundary**: the skill explicitly addresses when generated dunders
   are safe and when manual override is required.
7. **Example quality**: all examples are self-contained and runnable; no hidden
   imports or dependencies.
8. **Version portability**: no Python 3.11+ hard requirement unless explicitly
   version-gated in examples and justified.
9. **Reference structure**: if `references/` is used, each file is named and
   role-labeled in `SKILL.md` under `Local references`.

## Reviewer Handoff

The following JSON contract is machine-consumable and will be used by both
reviewer and main agent for Phase 5 evaluation:

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

The reviewer is responsible for checking:
- single responsibility and clear trigger
- boundaries against existing skills are explicit and honored
- examples include at least one correct and one incorrect case per major topic
- scope does not drift into async protocols, operator overloading, descriptor
  policy, or deep iteration strategy
- artifact paths match the plan
- equality/hash guidance is semantically safe and dataclass boundaries are
  explicit
- all code examples are runnable and Python 3.10+ portable or version-gated

## Post-merge / release actions

After the PR is merged into `dev`:

1. Switch to `dev` and sync: `git switch dev && git pull --ff-only origin dev`
2. Create and push the annotated tag:
   `git tag -a v0.23.0 -m v0.23.0 && git push origin refs/tags/v0.23.0`
3. Delete the feature branch locally and remotely (handled by
   `git-post-merge-workflow`).
4. Verify the tag is present on GitHub:
   `git ls-remote --tags origin refs/tags/v0.23.0`

These actions execute the `release` phase for this stable-library topic.

## Open Questions / Unresolved Items

None at this time. Scope breadth, dataclass boundary, async signpost, semantic
emphasis, stable-library timing, artifact paths, and role boundaries have been
locked.
