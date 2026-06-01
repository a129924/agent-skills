# python-serialization-boundaries-canonicalize

## Goal / Outcome

- Create `skills/python-serialization-boundaries/` as the canonical copy of the
  existing transition-era candidate.
- Preserve `.github/skills/python-serialization-boundaries/` as the
  compatibility and active skill surface during transition.
- Leave one repo-visible migration artifact that records the copied file set and
  deferred routing / active-path work.

## Scope

- **In scope**:
  - `analysis/python-serialization-boundaries-canonicalize/requirements.md`
  - `analysis/python-serialization-boundaries-canonicalize/technical-spec.md`
  - `plan/python-serialization-boundaries-canonicalize/python-serialization-boundaries-canonicalize.plan.md`
  - `skills/python-serialization-boundaries/`
  - `docs/migration/python-serialization-boundaries-canonicalize.md`

- **Out of scope**:
  - `.github/skills/python-serialization-boundaries/`
  - `AGENTS.md`
  - `docs/repo-positioning.md`
  - `README.md`
  - `VERSION`
  - `.codex/*`

## Locked Decisions

- bounded canonical copy only
- target root is `skills/python-serialization-boundaries/`
- `.github/skills/python-serialization-boundaries/` remains the active compatibility surface
- the canonical copy must include `SKILL.md`, `reference.md`, `examples.md`, and `REVIEW.md`

## Boundaries / Exclusions

- do not change serialization-boundary semantics
- do not change adjacent-skill routing rules
- do not change shared governance or release metadata

## Status / Allowed Transitions

- **Current**: `planned`
- **Execution model**: branch-local bounded copy work first
- **Allowed transitions**: `planned -> creator-in-progress -> review-ready -> reviewer-in-progress -> approved -> publish-in-progress -> pr-open|merged`

Routing notes:

- Branch target: `feat/andrew/python-serialization-boundaries-canonicalize`
- Base branch: `dev`

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/python-serialization-boundaries-canonicalize/python-serialization-boundaries-canonicalize.plan.md` | Planning actor | Repo-visible execution contract |
| Requirements baseline | `analysis/python-serialization-boundaries-canonicalize/requirements.md` | Planning actor | Locked single-candidate scope and stop conditions |
| Technical baseline | `analysis/python-serialization-boundaries-canonicalize/technical-spec.md` | Planning actor | Copy rules, deferred work, and verification contract |
| Migration report | `docs/migration/python-serialization-boundaries-canonicalize.md` | Creator | Repo-visible copy result |
| Target skill folder | `skills/python-serialization-boundaries/` | Creator | New target-architecture canonical copy |
| Compatibility source | `.github/skills/python-serialization-boundaries/` | Existing repo artifact | Read-only source to copy from and preserve |

## Implementation Steps

1. verify the source inventory
2. copy the full required file set into `skills/python-serialization-boundaries/`
3. preserve `.github/skills/python-serialization-boundaries/` without edits
4. write the migration report with explicit deferred work
5. stop if any routing or shared-surface change would be required

## Validation / Acceptance Checks

- full file set present in `skills/python-serialization-boundaries/`
- `.github/skills/python-serialization-boundaries/` unchanged
- no boundary semantics changed
- no shared governance or release-surface edits performed

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
