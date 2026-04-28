# Python Generators and Iterators Skill Plan

## Goal / Outcome

Create a repo-visible execution plan for a new stable skill at
`.github/skills/python-generators-iterators/` that teaches when Python code
should return a concrete collection versus a generator, when to use generator
functions versus custom iterator classes, and how to keep iteration semantics
explicit without drifting into async iteration, framework-specific patterns, or
lazy-evaluation architecture policy. The completed topic should produce a
review-ready skill that covers generator functions, generator expressions,
`yield` and `yield from`, iterator protocol (`__iter__`, `__next__`), single-pass
versus multi-pass exhaustion expectations, and custom iterator-class design
choices.

## Scope

- **In scope**:
  - create `.github/skills/python-generators-iterators/SKILL.md`
  - create `.github/skills/python-generators-iterators/reference.md` or split
    `references/` as needed
  - create `.github/skills/python-generators-iterators/examples.md` for layered
    examples and anti-patterns
  - define first-draft rules for:
    - concrete collection versus generator-returning function choice
    - generator function versus generator expression choice
    - `yield` and `yield from` readability and delegation rules
    - iterator exhaustion and single-pass versus multi-pass expectations
    - when to implement `__iter__` and `__next__` versus using a generator function
    - when a custom iterator class is warranted
  - declare stable-library promotion timing for `README.md` and `VERSION`
  - declare the post-merge tag action for this new stable skill topic

- **Out of scope**:
  - async iterators, async generators, and `async for` (owned by
    `python-async-await`)
  - pandas / NumPy / Spark / framework-specific iteration policy
  - queueing, backpressure, stream processing, or reactive architecture guidance
  - deep async testing rules for lazy pipelines
  - schema/model validation choices tied to iteration
  - descriptors, metaclasses, or `collections.abc` deep diving beyond ordinary
    iterator protocol

## Locked Decisions

- This topic is a **stable-library-affecting topic** with declared publish and
  release timing.
- The skill's primary scope is **general Python iteration semantics**, not async
  iteration or framework-specific policy.
- **Scope breadth is locked to `generator-plus-iterator-protocol`**, meaning:
  - generator functions and expressions are mainline topics
  - custom iterator classes and `__iter__`/`__next__` protocol are also mainline,
    not boundary notes
  - the topic should cover the ordinary decision between these approaches, not
    defer iterator-protocol guidance
- **Stable-library timing is locked to `stable-library-affecting-now`**, meaning:
  - this topic should update `README.md` and `VERSION` at
    `publish-in-progress`
  - a post-merge tag action is expected if the topic reaches stable library
- **Boundary stance**:
  - keep the topic **sync-only**
  - leave async iterators, async generators, and `async for` with
    `python-async-await`
  - do not let iterator-object examples turn into a general
    `ABC`/`Protocol`/model-selection guide; stay on ordinary iteration semantics
- **Version baseline**:
  - implementation guidance should work on **Python 3.6+** (when generator
    expressions and iterator protocol were stable)
  - no Python 3.10+ exclusions; maximize portability

## Boundaries / Exclusions

- `python-async-await`
  - already owns `async def`, `async for`, async iterators, async generators,
    and `async with`
  - this topic must stay on synchronous generators and ordinary iterators only
- `python-model-selection`
  - owns construct choice among `Enum`, `dataclass`, `ABC`, and `Protocol`
  - this topic may mention custom iterator classes only when iterator protocol
    pressure exists; it should not become an `ABC` vs dataclass selection skill
- `python-control-flow`
  - owns branch-shape decisions such as `if/elif`, `match/case`, guard clauses,
    and truthiness
  - this topic only cares about iteration/laziness design, not branching style
- `python-module-boundaries`
  - owns package/module public surfaces and import boundaries
  - this topic may discuss iterable-returning APIs, but not package export layout
- `python-testing-pytest`
  - owns test design; this topic should not become a lazy-testing or fixture
    policy skill
- If later work needs async iteration policy, reactive streams, or
  framework-specific lazy-evaluation rules, stop and split that into a separate
  topic instead of broadening this skill.

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
- If creator or reviewer drifts into async iteration, framework-specific lazy
  policy, or deep testing guidance, route back to `creator-in-progress` and
  repair scope before publish.

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/python-generators-iterators/python-generators-iterators.plan.md` | Planning actor | Repo-visible execution contract for this topic |
| Skill contract | `.github/skills/python-generators-iterators/SKILL.md` | Creator | Executable skill instructions for general Python generators and iteration semantics |
| Reference overview | `.github/skills/python-generators-iterators/reference.md` | Creator | Focused overview for the generators reference layer and navigation; may be split into `references/` if breadth exceeds three logical topics |
| Detailed examples | `.github/skills/python-generators-iterators/examples.md` | Creator | Multi-path examples, anti-patterns, and split signals for generator and iterator-class choices |
| Stable-library summary | `README.md` | Main Agent | Add the stable-library row for `python-generators-iterators` after approval |
| Repo version baseline | `VERSION` | Main Agent | Bump the repository version for a new stable skill |

Artifact path notes:

- This topic does **not** modify `.github/copilot-instructions.md`,
  `plan/agent-handoff-workflow.md`, or any existing `python-*` skill folder.
- These paths are an executable contract.
- If later work tries to add async iteration subfolders, framework-specific lazy
  examples, or other repo surfaces outside these paths, stop and repair the plan
  or split the work into a separate topic.

## Stable library metadata

### README row

- Table: `## Current skills`
- Exact row:

  `| \`python-generators-iterators\` | defines general Python generator and iterator rules for choosing concrete collections versus generators, generator functions versus custom iterators, lazy evaluation discipline, and iterator-protocol design |`

- Position:
  - after `python-async-await`
  - before `sense-env-scaffold`

### VERSION bump

- Current: `0.20.0`
- Direction: `MINOR`
- New: `0.22.0`
- Reason: new stable skill, non-breaking capability addition

### Timing

- README / VERSION timing: `publish-in-progress`
- Reason: the PR should show both the new stable skill and the stable-library
  surfaces it promotes

### Additional release metadata

- Tag action: create and push annotated tag `v0.22.0` at `release`
- Release notes artifact: none in this topic
- GitHub Release object: none in this topic unless a later release-specific topic
  adds one

## Implementation Steps

### Creator Phase (after plan approval)

1. Create `.github/skills/python-generators-iterators/`.
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
3. Keep the mainline trigger focused on general Python iteration semantics, not
   async or framework-specific policy.
4. In `SKILL.md`, make generator functions and expressions the baseline patterns,
   and treat custom iterator classes as a secondary but equally valid choice when
   protocol semantics or reusability warrant it.
5. Draft the reference layer as `reference.md` + optional `references/`:
   - `reference.md` as the focused overview and navigation file
   - if single `reference.md` becomes > 1000 tokens or covers > 3 logical topics,
     split into `references/` with topic-specific files
6. Draft `examples.md` with:
   - positive patterns for generator functions, generator expressions, and custom
     iterator classes
   - anti-patterns for scattered lazy-evaluation choices, iterator exhaustion
     surprises, and misuse of `__iter__`/`__next__`
   - split signals for choosing between approaches
7. Ensure all examples are self-contained and runnable on Python 3.6+.
8. Mark any examples requiring Python 3.10+ or later as version-gated notes.
9. Verify no drift into async iteration, framework-specific streams, or
   queueing architecture.

### Creator deliverable summary

- review-ready `.github/skills/python-generators-iterators/` folder with:
  - `SKILL.md` (required)
  - `reference.md` or `references/` (required)
  - `examples.md` (required for branching topic)
- all files contain explicit examples and clear boundaries
- all code examples run on Python 3.6+ or are clearly version-gated

## Validation / Acceptance Checks

1. **Path exactness**: artifact paths in the creator draft match those listed in
   `Artifact Paths` section.
2. **Scope enforcement**: no async iteration guidance in the new skill; no
   framework-specific lazy policy.
3. **Boundary clarity**: skill's `SKILL.md` explicitly states what
   `python-async-await`, `python-model-selection`, `python-control-flow`, and
   `python-module-boundaries` own.
4. **Example quality**: all examples are self-contained and runnable; no hidden
   imports or dependencies.
5. **Version portability**: no Python 3.10+ hard requirement unless explicitly
   version-gated in examples and justified.
6. **Reference structure**: if `references/` is used, each file is named and
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
- scope does not drift into async, framework-specific, or architecture policy
- artifact paths match the plan
- all code examples are runnable and Python 3.6+ portable or version-gated

## Post-merge / release actions

After the PR is merged into `dev`:

1. Switch to `dev` and sync: `git switch dev && git pull --ff-only origin dev`
2. Create and push the annotated tag: `git tag -a v0.22.0 -m v0.22.0 && git push origin refs/tags/v0.22.0`
3. Delete the feature branch locally and remotely (handled by
   `git-post-merge-workflow`).
4. Verify the tag is present on GitHub: `git ls-remote --tags origin refs/tags/v0.22.0`

These actions execute the `release` phase for this stable-library topic.

## Open Questions / Unresolved Items

None at this time. All required scope decisions, stable-library timing,
artifact paths, and role boundaries have been locked.
