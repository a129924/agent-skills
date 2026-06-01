# git-release-management-canonicalize

## Goal / Outcome

- Create `skills/git-release-management/` as the canonical copy of the existing
  transition-era candidate.
- Preserve `.github/skills/git-release-management/` as the compatibility and
  active workflow surface during transition.
- Leave one repo-visible migration artifact that records the copied file set and
  deferred release-policy / active-path work.

## Scope

- **In scope**:
  - `analysis/git-release-management-canonicalize/requirements.md`
  - `analysis/git-release-management-canonicalize/technical-spec.md`
  - `plan/git-release-management-canonicalize/git-release-management-canonicalize.plan.md`
  - `skills/git-release-management/`
  - `docs/migration/git-release-management-canonicalize.md`

- **Out of scope**:
  - `.github/skills/git-release-management/`
  - `AGENTS.md`
  - `docs/repo-positioning.md`
  - `README.md`
  - `VERSION`
  - `.codex/*`

## Locked Decisions

- bounded canonical copy only
- target root is `skills/git-release-management/`
- `.github/skills/git-release-management/` remains the active compatibility surface
- the canonical copy must include `SKILL.md`, `examples.md`, and all four reference files

## Boundaries / Exclusions

- do not change release gate semantics
- do not change emergency-path semantics
- do not change tag/version policy
- do not change shared governance or release metadata

## Status / Allowed Transitions

- **Current**: `planned`
- **Execution model**: branch-local bounded copy work first
- **Allowed transitions**: `planned -> creator-in-progress -> review-ready -> reviewer-in-progress -> approved -> publish-in-progress -> pr-open|merged`

Routing notes:

- Branch target: `feat/andrew/git-release-management-canonicalize`
- Base branch: `dev`

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/git-release-management-canonicalize/git-release-management-canonicalize.plan.md` | Planning actor | Repo-visible execution contract |
| Requirements baseline | `analysis/git-release-management-canonicalize/requirements.md` | Planning actor | Locked single-candidate scope and stop conditions |
| Technical baseline | `analysis/git-release-management-canonicalize/technical-spec.md` | Planning actor | Copy rules, deferred work, and verification contract |
| Migration report | `docs/migration/git-release-management-canonicalize.md` | Creator | Repo-visible copy result |
| Target skill folder | `skills/git-release-management/` | Creator | New target-architecture canonical copy |
| Compatibility source | `.github/skills/git-release-management/` | Existing repo artifact | Read-only source to copy from and preserve |

## Implementation Steps

1. verify the source inventory
2. copy the full required file set into `skills/git-release-management/`
3. preserve `.github/skills/git-release-management/` without edits
4. write the migration report with explicit deferred work
5. stop if any release-policy or shared-surface change would be required

## Validation / Acceptance Checks

- full file set present in `skills/git-release-management/`
- `.github/skills/git-release-management/` unchanged
- no release-gate semantics changed
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
