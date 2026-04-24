# Python Decorators Skill Plan

## Goal / Outcome

Create a repo-visible execution plan for a new stable skill at
`.github/skills/python-decorators/` that teaches when to use decorators and how
to design them safely in ordinary Python code. The completed topic should
produce a review-ready skill that keeps decorator behavior explicit, preserves
signature integrity for transparent wrappers, and routes lifetime-driven
patterns away from decorator-based hiding and toward clearer alternatives such
as explicit function calls or context managers.

## Scope

- **In scope**:
  - create `.github/skills/python-decorators/SKILL.md`
  - create `.github/skills/python-decorators/reference.md`
  - create split references under `.github/skills/python-decorators/references/`
    for signature integrity, behavior visibility, and light framework notes
  - create `.github/skills/python-decorators/examples.md`
  - define first-draft rules for function decorators, method decorators, and
    decorator factories
  - define first-draft guidance for transparent decorator typing with
    `ParamSpec` and `TypeVar`
  - include light framework notes for developer-authored decorators in common
    ecosystems such as FastAPI, pytest, and Click
  - declare stable-library promotion timing for `README.md` and `VERSION`

- **Out of scope**:
  - implementing descriptor or metaclass machinery guidance
  - framework-private decorator internals
  - decorator-led hidden resource lifetime patterns that belong in
    `python-context-management`
  - broad repository-wide typing policy outside decorator-specific signature
    preservation
  - class decorators as a first-draft mainline pattern

## Locked Decisions

- This topic is a **stable-library-affecting topic** with declared timing.
- The skill's primary scope is **when to use decorators and how to design them
  safely**, not generic typing policy or framework architecture.
- First-draft included surface:
  - function decorators
  - method decorators
  - decorator factories
  - class decorators only as boundary notes
- First-draft excluded surface:
  - descriptors
  - metaclasses
  - framework-private decorator internals
- Lifetime/resource behavior stays explicit:
  - do not make `ContextDecorator` or implicit setup/cleanup the mainline
    pattern
  - hand lifetime-driven behavior to `python-context-management`
- Signature Integrity Contract:
  - ban lossy typing such as `Callable[..., Any]` when the decorator is intended
    to preserve the wrapped callable contract
  - require `ParamSpec` (`P`) and `TypeVar` (`R`) for transparent wrapper
    patterns
  - prefer `Callable[P, R]`-style preservation so caller-visible typing remains
    transparent
  - if a decorator is presented as transparent, caller-visible typing and static
    type-checker analysis should remain consistent before and after decoration
- First-draft contract-change policy: `transparent-only-mainline`
  - decorators that change return shape or caller-visible contract are not the
    normal pattern for this skill
  - treat contract-changing decorators as boundary, anti-pattern, or
    secondary-note material
- Framework interaction rule:
  - keep the core rules pure-Python-first
  - allow only light framework notes
  - framework notes must cover developer-authored custom decorators only
  - framework notes must not override the core explicitness and lifetime rules
- Stable-library timing:
  - update `README.md` and `VERSION` at `publish-in-progress`
  - do not defer stable-library promotion to a separate release-only topic

## Boundaries / Exclusions

- `python-api-signature` owns public parameter ordering, default semantics, and
  broad signature-shape design; `python-decorators` only owns
  decorator-specific signature preservation and contract transparency.
- `python-type-hints-strict` owns general strict-typing policy; this topic only
  defines decorator-specific use of `ParamSpec`, `TypeVar`, and transparent
  callable preservation.
- `python-class-design` owns ordinary method, property, and factory placement;
  this topic only decides when decorator use is appropriate or misleading.
- `python-module-boundaries` owns import surfaces and module layout; this topic
  does not define package export policy.
- `python-context-management` owns lifetime/resource management, acquisition,
  cleanup, and ambient-state restoration; decorator-led implicit lifetime
  management is out of scope except as a boundary warning.
- If later work needs framework-specific decorator policy deeper than light
  notes, stop and create a separate topic rather than expanding this skill.

## Status / Allowed Transitions

- **Current**: `pr-open`
- **Execution model**: follow the canonical creator -> reviewer -> publish ->
  merge path; this topic ends at `merged` with no separate Phase 10 release
  action.
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

- Use the standard Phase 4.5 planner-alignment checkpoint from
  `plan/agent-handoff-workflow.md`.
- If creator or reviewer drifts into framework-private behavior, descriptor /
  metaclass design, or implicit lifetime management, route back to
  `creator-in-progress` and repair scope before publish.

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/python-decorators/python-decorators.plan.md` | Planning actor | Repo-visible execution contract for this topic |
| Skill contract | `.github/skills/python-decorators/SKILL.md` | Creator | Executable skill instructions for when to use decorators and how to design them safely |
| Reference overview | `.github/skills/python-decorators/reference.md` | Creator | Focused overview for the reference layer and navigation entry for split local guidance |
| Reference split | `.github/skills/python-decorators/references/signature-integrity.md` | Creator | Detailed rules for `functools.wraps`, `ParamSpec`, `TypeVar`, transparent wrappers, and type-preservation anti-patterns |
| Reference split | `.github/skills/python-decorators/references/behavior-visibility.md` | Creator | Detailed rules for explicit side effects, retries, caching, auth, error behavior, and lifetime-boundary warnings |
| Reference split | `.github/skills/python-decorators/references/framework-notes.md` | Creator | Light framework notes for developer-authored decorators in FastAPI, pytest, Click, and similar ecosystems |
| Detailed examples | `.github/skills/python-decorators/examples.md` | Creator | Multi-path examples, anti-patterns, and split signals for decorator choices |
| Stable-library summary | `README.md` | Main Agent | Add the stable-library row for `python-decorators` after approval |
| Repo version baseline | `VERSION` | Main Agent | Bump the repository version for a new stable skill |

Artifact path notes:

- This topic does **not** modify `.github/copilot-instructions.md`,
  `plan/agent-handoff-workflow.md`, or any existing `python-*` skill folder.
- These paths are an executable contract.
- `references/` is intentionally part of this topic because the reference layer
  spans more than three logical topics.
- If later work tries to add `checklist.md`, framework-specific local
  subfolders, or additional repo surfaces, stop and repair the plan or split
  the work into a separate topic.

## Stable library metadata

### README row

- Table: `## Current skills`
- Exact row:

  `| \`python-decorators\` | defines ordinary Python decorator rules for when to use decorators, how to preserve signature transparency, and when explicit calls or context managers are clearer |`

- Position:
  - after `python-docstrings`
  - before `sense-env-scaffold`

### VERSION bump

- Current: `0.17.0`
- Direction: `MINOR`
- New: `0.18.0`
- Reason: new stable skill, non-breaking capability addition

### Timing

- README / VERSION timing: `publish-in-progress`
- Reason: the PR should show both the new stable skill and the stable-library
  surfaces it promotes
- Release action: no separate release action in this topic

### Additional release metadata

- Release notes artifact: none in this topic
- Tag action: none in this topic

## Implementation Steps

### Creator Phase (after plan approval)

1. Create `.github/skills/python-decorators/`.
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
3. Keep the mainline trigger focused on decorator choice and safe decorator
   design, not generic typing policy or framework internals.
4. In `SKILL.md`, make transparent decorators the normal case and push
   contract-changing decorators into boundary or anti-pattern treatment.
5. Draft the reference layer as `reference.md` + `references/`:
   - `reference.md` as the focused overview and navigation file
   - `references/signature-integrity.md` for `functools.wraps`, transparent
     typing, `ParamSpec`, `TypeVar`, and anti-patterns such as
     `Callable[..., Any]`
   - `references/behavior-visibility.md` for explicitness around side effects,
     retries, caching, auth, error behavior, and lifetime-boundary warnings
   - `references/framework-notes.md` for light framework notes limited to
     developer-authored custom decorators
6. Draft `examples.md` because this topic has branching choices and anti-pattern
   risk.
7. Ensure the examples set covers at minimum:
   - transparent function decorator with `ParamSpec` / `TypeVar`
   - transparent method decorator
   - decorator factory preserving caller-visible typing
   - anti-pattern using `Callable[..., Any]`
   - anti-pattern hiding resource lifetime or transaction scope
   - contract-only light framework note for developer-authored decorators
   - boundary example showing when an explicit function call or context manager
     is clearer than a decorator
8. Keep class decorators as boundary-only material; do not expand them into a
   first-draft decision matrix.

### Reviewer Phase (after creator delivers review-ready)

1. Verify the skill stays within ordinary decorator design and review scope.
2. Verify the full reference layer exists at the locked paths:
   `SKILL.md`, `reference.md`, `references/`, and `examples.md`.
3. Verify the mainline guidance treats transparent decorators as the default and
   does not normalize contract-changing wrappers.
4. Verify `Callable[..., Any]` is not recommended for transparent wrappers.
5. Verify `ParamSpec` / `TypeVar` are used or required where transparent typing
   is claimed.
6. Verify lifetime/resource anti-patterns are routed to
   `python-context-management`, not normalized here.
7. Verify framework notes stay light, custom-decorator-only, and subordinate to
   the pure-Python rules.

### Main Agent Publish Phase (after approval + planner alignment)

1. Update `README.md` with the exact locked `python-decorators` row at the
   locked position.
2. Update `VERSION` from `0.17.0` to `0.18.0`.
3. Stage only the locked artifact set for this topic; do not stage unrelated
   files.
4. Open the PR with the skill files plus stable-library surfaces visible
   together, because timing is locked to `publish-in-progress`.

## Validation / Acceptance Checks

- [ ] The topic plan remains valid at `plan/python-decorators/python-decorators.plan.md`.
- [ ] `Status / Allowed Transitions` uses canonical workflow transitions only.
- [ ] `Artifact Paths` remain exact and bounded to the listed repo-visible files.
- [ ] Stable-library intent is explicit and executable:
  - [ ] `README.md` row text is locked
  - [ ] `VERSION` bump is locked
  - [ ] timing is declared as `publish-in-progress`
- [ ] Creator output is limited to:
  - [ ] `.github/skills/python-decorators/SKILL.md`
  - [ ] `.github/skills/python-decorators/reference.md`
  - [ ] `.github/skills/python-decorators/references/signature-integrity.md`
  - [ ] `.github/skills/python-decorators/references/behavior-visibility.md`
  - [ ] `.github/skills/python-decorators/references/framework-notes.md`
  - [ ] `.github/skills/python-decorators/examples.md`
- [ ] Main Agent publish output is limited to:
  - [ ] `README.md`
  - [ ] `VERSION`
- [ ] `SKILL.md` contains concise positive and negative examples.
- [ ] `examples.md` covers transparent wrapper patterns, decorator-factory
  patterns, explicitness anti-patterns, and lifetime-boundary warnings.
- [ ] Transparent decorator guidance is type-safe:
  - [ ] no lossy `Callable[..., Any]` recommendation for transparent wrappers
  - [ ] transparent wrappers preserve caller-visible typing with `ParamSpec` /
    `TypeVar`
  - [ ] guidance states that transparent decorators should not change the
    caller-visible contract
  - [ ] checker-facing wording stays generic to static type checking rather than
    assigning ownership to one specific checker
- [ ] Boundary integrity holds:
  - [ ] no generic typing-policy drift into `python-type-hints-strict`
  - [ ] no ordinary class-placement drift into `python-class-design`
  - [ ] no package-layout drift into `python-module-boundaries`
  - [ ] no hidden lifetime management normalized in place of
    `python-context-management`
- [ ] Reviewer handoff remains a single machine-consumable JSON object.

## Reviewer Handoff

```json
{
  "verdict": "approved|needs-rework",
  "blocking_issues": [
    {
      "issue": "example",
      "file": "relative/path",
      "fix": "specific required correction"
    }
  ],
  "copilot_feedback_triage": {
    "ADDRESS": [
      {
        "comment": "required copilot feedback to apply",
        "location": "relative/path:line",
        "why": "why this feedback is required"
      }
    ],
    "DISCUSS": [
      {
        "comment": "optional or ambiguous feedback",
        "optional": true,
        "why": "why this is discussion-level only"
      }
    ],
    "SKIP": [
      {
        "comment": "feedback to skip",
        "why": "why this is not applicable"
      }
    ]
  }
}
```

## Post-merge / release actions

- After merge, Main Agent performs normal post-merge local sync and marks the
  topic `merged`.
- No separate Phase 10 release action is required in this topic.
- Do not create a tag, release notes artifact, or deferred release patch from
  this topic.

## Open Questions / Unresolved Items

- None. Current scope, stable-library timing, and artifact paths are locked for
  first-draft execution.
