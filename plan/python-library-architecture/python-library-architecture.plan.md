# Python Library Architecture Skill Plan

## Goal / Outcome

Create a repo-visible execution contract for a new stable skill at
`.github/skills/python-library-architecture/` that teaches clean internal
architecture for reusable Python libraries and SDK-style packages.

When this topic is complete, the repository should contain a review-ready skill
folder whose guidance is explicit about:
- theme isolation inside one library
- `core` as the shared contract center
- zero-exception prohibition on cross-theme imports
- facade/client as the recommended composition root
- dependency direction discipline that prevents a large coupled package

## Scope

- **In scope**:
  - create `.github/skills/python-library-architecture/SKILL.md`
  - create `.github/skills/python-library-architecture/reference.md`
  - create `.github/skills/python-library-architecture/examples.md`
  - define architecture rules for:
    - theme independence and isolation
    - `core` layer meaning, naming, and allowed contents
    - shared-contract promotion into `core`
    - cross-theme import prohibition
    - facade/client as the recommended public composition root
    - dependency direction between themes, `core`, adapters, and public entry
      points
    - SDK-style packages as a primary use case alongside pure libraries
  - stage stable-library metadata updates for this new stable skill topic

- **Out of scope**:
  - package/distribution layout policy (`python-package-layout`)
  - module export policy, `__all__`, and internal-module contracts
    (`python-module-boundaries`)
  - typing syntax and strict-typing baseline (`python-type-hints-strict`)
  - construct selection for `Enum`, dataclass, `ABC`, and `Protocol`
    (`python-model-selection`)
  - serialization boundary translation (`python-serialization-boundaries`)
  - exception hierarchy and translation policy (`python-error-handling`)
  - generic testing strategy
  - service/application architecture such as DDD, Hexagonal, or Clean
    Architecture
  - framework-specific layering or plugin systems

## Locked Decisions

- This is a **stable-library-affecting topic**.
- Stable-library timing is **`publish-in-progress`** for `README.md` and
  `VERSION`, with the annotated tag created after merge during release follow-up.
- Topic scope is **library/package architecture only**.
- SDK-style packages are a **primary use case**, not a side example.
- `core` is a **recommended baseline** for multi-theme libraries.
- `core` is the shared contract center and side-effect-free nucleus; it must not
  orchestrate outward.
- Cross-theme imports are **forbidden with zero exceptions**.
- Shared contracts that cross themes or external boundaries must be promoted
  into `core`.
- Facade/client is the **recommended default** consumer-facing composition root.
- One primary facade/client entry point is recommended; bounded secondary entry
  points are allowed only when they remain orchestration-only.
- Recommended default naming is `core/`; semantically explicit alternatives such
  as `kernel/` or `base/` are allowed.
- Vague names such as `utils/` and `common/` are forbidden as substitutes for
  `core`.
- Rules and checklists are the portable enforcement baseline; tools such as
  `import-linter` or Tach remain optional examples.

## Boundaries / Exclusions

- `python-module-boundaries` owns import/export policy, `__all__`, internal
  modules, and public-module gateways. This topic only owns theme-level
  architecture and dependency direction.
- `python-type-hints-strict` owns typing syntax, annotation form, and strict
  typing ergonomics. This topic may require strong contracts but does not define
  typing style.
- `python-model-selection` owns the choice between dataclass, `Enum`, `ABC`,
  and `Protocol`. This topic only decides where such constructs belong in the
  architecture.
- `python-serialization-boundaries` owns payload translation and deep
  conversion. This topic only defines where boundary-facing code sits relative
  to themes and `core`.
- `python-package-layout` owns package tree and distribution layout. This topic
  only governs logical architecture inside a library.
- `python-error-handling` owns exception hierarchy design and translation
  policy. This topic only permits shared base errors in `core`.
- This topic must stay single-purpose: it defines reusable library/package
  architecture discipline and must not widen into full application architecture.

## Status / Allowed Transitions

- **Current**: `merged`
- **Execution model**: follow the canonical creator -> reviewer -> publish -> PR
  -> merged -> released path for a stable-library-affecting topic.
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

Routing notes:

- Phase 4.5 uses the standard planner-alignment rule from
  `plan/agent-handoff-workflow.md`.
- STOP POINT 1 applies before commit/push/PR creation.
- STOP POINT 2 applies after human merge handoff; post-merge work resumes only
  on an explicit human resume message.

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/python-library-architecture/python-library-architecture.plan.md` | Planning actor | Repo-visible execution contract for this topic |
| Skill contract | `.github/skills/python-library-architecture/SKILL.md` | Creator | Executable skill instructions |
| Skill reference | `.github/skills/python-library-architecture/reference.md` | Creator | Stable local architecture guidance |
| Skill examples | `.github/skills/python-library-architecture/examples.md` | Creator | High-complexity examples and anti-patterns |
| Stable skill index | `README.md` | Main Agent | Stable-library table row for `python-library-architecture` |
| Repository version | `VERSION` | Main Agent | Canonical SemVer bump for stable-library publication |

Artifact path notes:

- This topic **does modify** `README.md` and `VERSION`.
- Listed paths are the executable contract for this topic.
- If later work drifts outside these paths, stop and repair the topic plan
  before continuing execution.

## Stable library metadata

- `README row`: insert this exact table row immediately after
  `| \`python-generators-iterators\` | defines general Python generator and iterator rules for choosing concrete collections versus generators, generator functions versus custom iterators, lazy evaluation discipline, and iterator-protocol design |`
  and before
  `| \`python-project-init-greenfield\` | executes Greenfield project initialization from blueprint contracts, including required skill installation, toolchain configuration, structural scaffolding, and acceptance handoff |`:
  `| \`python-library-architecture\` | defines clean Python library/package architecture rules for theme isolation, \`core\` contracts, facade/client composition, and zero-exception cross-theme dependency direction |`
- `VERSION bump`: `0.31.0` -> `0.32.0`
- `timing`: `publish-in-progress`
- `rationale`: this topic adds a new stable skill to the library, so stable
  index and version metadata should be staged with the approved publish-ready
  change rather than deferred to a separate follow-up topic.
- `release note expectation`: create annotated tag `v0.32.0` after merge during
  release follow-up.

## Implementation Steps

1. Creator drafts `.github/skills/python-library-architecture/SKILL.md` with:
   - required frontmatter and canonical sections
   - concise positive and negative examples
   - explicit trigger, boundaries, and local references
2. Creator drafts `reference.md` with focused architecture guidance covering:
   - theme definition and isolation
   - `core` purity and allowed contents
   - dependency direction and contract promotion
   - facade/client composition guidance
   - smell list and misuse-prevention guidance
3. Creator drafts `examples.md` because this is a high-complexity, branching
   skill. Examples must include:
   - a pure-library example
   - an SDK-style package example
   - anti-patterns for cross-theme imports and orchestration inside `core`
   - a migration/refactor example
4. Creator validates that the draft stays inside this topic's locked boundaries
   and reaches `review-ready` without modifying unrelated skills.

## Validation / Acceptance Checks

- The topic plan still matches the canonical section set and status model.
- Artifact paths remain exact and repo-visible.
- Stable-library intent and timing are explicit and internally consistent.
- `SKILL.md` stays single-purpose: reusable library/package architecture only.
- `SKILL.md` includes at least one concise positive example and one concise
  negative example.
- `examples.md` exists and covers pure libraries, SDKs, and anti-patterns.
- `Boundaries` clearly hand off adjacent concerns to neighboring skills.
- The skill states the zero-exception cross-theme import rule explicitly.
- The skill defines `core` allowed/forbidden contents clearly enough to prevent
  `core` from becoming a dump zone.
- Reviewer output follows the required machine-consumable verdict format.

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

- After merge and explicit human resume, sync local `dev` to the merge commit.
- Delete the feature branch locally and remotely if no longer needed.
- Confirm `README.md` and `VERSION` already reflect the approved publish-ready
  change staged at `publish-in-progress`.
- Create annotated tag `v0.32.0`.
- Push the tag.
- Update this topic status to `released`.

## Open Questions / Unresolved Items

- None. The architecture scope, stable-library timing, and workflow routing are
  locked for execution.
