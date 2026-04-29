# Python Package Layout Skill Plan

## Goal / Outcome

Create a repo-visible execution plan for a new stable skill at
`.github/skills/python-package-layout/` that teaches how to structure a
distributable Python package with conservative, reusable defaults. The completed
topic should produce a review-ready skill that covers `src/` layout, package
root placement, `pyproject.toml` as the package/distribution config anchor,
library-vs-CLI boundaries, tests relative to packaged code, package data, and
extras, without drifting into architecture-policy or release-automation rules.

## Scope

- **In scope**:
  - create `.github/skills/python-package-layout/SKILL.md`
  - create `.github/skills/python-package-layout/reference.md` as the focused
    overview and navigation file
  - create `.github/skills/python-package-layout/examples.md` for branching
    examples, anti-patterns, and split signals
  - define first-draft rules for:
    - when to prefer `src/` layout for reusable packages
    - how to place importable code under `src/<package_name>/`
    - how to separate reusable library code from CLI / scripts / ad-hoc execution
    - how to use `pyproject.toml` as the package/distribution config anchor
    - how to place tests relative to packaged code without relying on local-path
      accidents
    - how to expose console entry points and keep `__main__.py` / CLI launchers
      thin
    - how to treat package data and extras as packaging decisions
    - how to keep the first draft on regular packages with `__init__.py`
  - declare stable-library promotion timing for `README.md` and `VERSION`
  - declare the post-merge tag action for this new stable skill topic

- **Out of scope**:
  - feature-folder, bounded-context, or screaming-architecture policy
  - facade/client composition rules for a library API
  - `Protocol`, `ABC`, dependency inversion, or contract-modeling strategy
  - domain entity placement or shared schema promotion rules
  - exception hierarchy or translation strategy
  - import-linter / tach enforcement workflow
  - publishing steps, PyPI credentials, release automation, or versioning policy
  - namespace-package strategy as a first-class path
  - framework-specific project structure or application architecture

## Locked Decisions

- This topic is a **stable-library-affecting topic** with declared publish and
  release timing.
- The skill's primary scope is **general reusable package-layout guidance** for
  ordinary Python library packages, not organization-specific architecture
  policy.
- **Scope breadth is locked to `package-layout-and-distribution-structure`**,
  meaning:
  - `src/` layout is a mainline topic
  - regular packages with `__init__.py` are the default path
  - `pyproject.toml` as config anchor is in scope
  - CLI entry points, `__main__.py`, package data, and extras are in scope
  - namespace packages are out of the first-draft mainline path
- **Conservative-defaults emphasis is locked**, meaning:
  - the skill should optimize for clarity, portability, and install-time
    correctness over highly customized or architecture-heavy layouts
  - examples should prefer one clear default before introducing exceptions
  - the skill should explain why flat local execution can hide packaging errors
- **Boundary ownership is locked**, meaning:
  - public import surfaces, `__all__`, deep imports, and circular-import repair
    stay owned by `python-module-boundaries`
  - `Protocol` / `ABC` / dataclass structural choices stay owned by
    `python-model-selection`
  - package error hierarchy and translation stay owned by `python-error-handling`
  - repository bootstrap / scaffold execution stays owned by
    `python-project-init-greenfield` and `python-project-retrofit`
- **Stable-library timing is locked to `stable-library-affecting-now`**, meaning:
  - this topic should update `README.md` and `VERSION` at
    `publish-in-progress`
  - a post-merge tag action is expected if the topic reaches the stable library
- **Version baseline**:
  - guidance should work for **Python 3.10+**
  - examples may assume modern typing syntax already used by this repository

## Boundaries / Exclusions

- `python-module-boundaries`
  - owns `__init__.py` gateway policy, public import surfaces, `__all__`,
    deep-import avoidance, and circular-import handling
  - this topic only decides where packaged code, CLI code, tests, data files,
    and metadata should live

- `python-model-selection`
  - owns `Enum`, dataclass, `ABC`, and `Protocol` selection
  - this topic may mention that optional capability contracts exist, but it does
    not choose modeling constructs

- `python-error-handling`
  - owns error hierarchy, translation boundaries, and propagation rules
  - this topic may mention CLI-vs-library boundary shape, but it does not define
    exception strategy

- `python-project-init-greenfield` / `python-project-retrofit`
  - own repository creation and retrofit workflows
  - this topic only defines reusable package-layout guidance, not execution of a
    project transformation

- Future `python-library-architecture` or similar topic
  - would own stronger opinions about feature slicing, bounded contexts, facade
    clients, and architecture enforcement
  - this topic should stay layout-focused and portable

## Status / Allowed Transitions

**Current status**: `publish-in-progress`

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
- STOP POINT 2 applies after merge handoff; release work resumes only after a new
  explicit human message.

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/python-package-layout/python-package-layout.plan.md` | Planning actor | Repo-visible execution contract for this topic |
| Skill contract | `.github/skills/python-package-layout/SKILL.md` | Creator | Executable skill contract with trigger, process, examples, boundaries, and local references |
| Focused reference | `.github/skills/python-package-layout/reference.md` | Creator | Stable layout defaults, exclusions, and decision notes |
| Layered examples | `.github/skills/python-package-layout/examples.md` | Creator | Branching scenarios such as library-only, CLI-enabled, package-data, and extras cases |
| Stable library row | `README.md` | Main Agent | Add the stable-skill table row for `python-package-layout` at publish time |
| Repo version baseline | `VERSION` | Main Agent | Apply the next MINOR version bump when the topic is promoted to the stable library |

Artifact path notes:
- This topic modifies `README.md` and `VERSION`.
- This topic does not modify `.github/copilot-instructions.md`.
- Treat the listed paths as an executable contract; if later work drifts outside
  them, stop and repair the topic plan before continuing execution.

## Stable library metadata

- `README row`: add a stable-skill row for `python-package-layout` in the
  README skills table; place it after `python-naming` and before
  `python-project-init-greenfield`
- `VERSION bump`: next MINOR bump from the repository's current `VERSION`
- `timing`: `publish-in-progress`
- `rationale`: this topic adds a new stable Python skill to the library, so the
  stable skill table and repository version baseline must be updated when the
  approved draft is published
- `release notes`: no separate release-notes artifact is planned; the annotated
  git tag message is the release-facing metadata for this topic

## Implementation Steps

1. **Branch preparation** (via Main Agent):
   - create or repair the semantic execution branch for `python-package-layout`
   - verify worktree readiness before creator work begins
   - do not start drafting from chat-only state once repo-visible plan exists

2. **Draft phase** (via `agent-skill-creator`):
   - create `.github/skills/python-package-layout/SKILL.md` with:
     - explicit trigger: when to use this skill
     - process: decision path for package layout choices
     - concise positive/negative examples
     - clear boundaries vs related skills
   - create `.github/skills/python-package-layout/reference.md` as overview
   - create `.github/skills/python-package-layout/examples.md` for branching
     scenarios
   - keep the draft on regular packages with `__init__.py`
   - update topic plan status to `review-ready`

3. **Review phase** (via independent `agent-skill-reviewer`):
   - verify required files present (SKILL.md, reference.md, examples.md)
   - verify the skill stays layout-focused and does not absorb architecture
     policy from the source report
   - verify boundaries are explicit vs `python-module-boundaries`,
     `python-model-selection`, `python-error-handling`, and project-init skills
   - verify no hidden repo context is assumed
   - return `approved` or `needs-rework`
   - update topic plan status to reviewer verdict

4. **Publish phase** (if `approved`):
   - commit skill files to the execution branch
   - add row to `README.md` in alphabetical order
   - update `VERSION` (MINOR bump, e.g., X.Y.Z → X.(Y+1).0)
   - open PR after STOP POINT 1 approval
   - after merge and explicit human resume, create annotated git tag matching the
     version and push it
   - update topic plan status to `released`

## Validation / Acceptance Checks

**Draft must pass**:
- [ ] SKILL.md includes explicit trigger (when to use)
- [ ] SKILL.md includes concise positive and negative examples
- [ ] reference.md explains default layout choices and exclusions
- [ ] examples.md covers branching scenarios such as library-only package,
      CLI-enabled package, package data, and optional dependency extras
- [ ] the skill clearly distinguishes layout guidance from module-boundary,
      model-selection, and error-handling rules
- [ ] no file assumes hidden repo context or project-specific architecture

**Review phase verdict**: `approved`

**Publish phase success**:
- [ ] committed to the execution branch
- [ ] README.md updated with alphabetical row
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
   - README.md row added in alphabetical order
   - VERSION bumped: X.Y.Z → X.(Y+1).0
   - plan status updated to `publish-in-progress`

2. **Release tagging** (post-merge, after explicit human resume):
   - Create annotated tag matching the version:
     `git tag -a v<VERSION> -m "Release v<VERSION>: add python-package-layout skill"`
   - Push tag: `git push origin v<VERSION>`
   - plan status updated to `released`

3. **Verification**:
   - Confirm tag exists on remote
   - Confirm README includes the new skill row
   - Confirm VERSION file matches the new version

## Open Questions / Unresolved Items

- None at plan creation time. The first-draft boundary is locked to general
  reusable package layout, not architecture governance.

All locked decisions are explicit. All workflow phases are defined. All
transition rules match canonical handoff-workflow semantics.
