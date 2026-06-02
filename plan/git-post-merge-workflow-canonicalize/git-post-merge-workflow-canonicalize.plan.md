# git-post-merge-workflow-canonicalize

## Goal / Outcome

- Create `skills/git-post-merge-workflow/` as the canonical copy of the existing
  transition-era candidate.
- Preserve `.github/skills/git-post-merge-workflow/` as the compatibility and
  active workflow surface during transition.
- Leave one repo-visible migration artifact that records the copied file set and
  deferred branch-policy / active-path work.

## Scope

- **In scope**:
  - `analysis/git-post-merge-workflow-canonicalize/requirements.md`
  - `analysis/git-post-merge-workflow-canonicalize/technical-spec.md`
  - `plan/git-post-merge-workflow-canonicalize/git-post-merge-workflow-canonicalize.plan.md`
  - `skills/git-post-merge-workflow/`
  - `docs/migration/git-post-merge-workflow-canonicalize.md`

- **Out of scope**:
  - `.github/skills/git-post-merge-workflow/`
  - `AGENTS.md`
  - `docs/repo-positioning.md`
  - `README.md`
  - `VERSION`
  - `.codex/*`

## Locked Decisions

- bounded canonical copy only
- target root is `skills/git-post-merge-workflow/`
- `.github/skills/git-post-merge-workflow/` remains the active compatibility surface
- the canonical copy must include `SKILL.md`, `examples.md`, and `references/stop-point-2-checklist.md`

## Boundaries / Exclusions

- do not change STOP POINT 2 semantics
- do not change branch retention, sync, or cleanup policy
- do not change shared governance or release metadata

## Status / Allowed Transitions

- **Current**: `planned`
- **Execution model**: branch-local bounded copy work first
- **Allowed transitions**: `planned -> creator-in-progress -> review-ready -> reviewer-in-progress -> approved -> publish-in-progress -> pr-open|merged`

Routing notes:

- Branch target: `feat/andrew/git-post-merge-workflow-canonicalize`
- Base branch: `dev`

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/git-post-merge-workflow-canonicalize/git-post-merge-workflow-canonicalize.plan.md` | Planning actor | Repo-visible execution contract |
| Requirements baseline | `analysis/git-post-merge-workflow-canonicalize/requirements.md` | Planning actor | Locked single-candidate scope and stop conditions |
| Technical baseline | `analysis/git-post-merge-workflow-canonicalize/technical-spec.md` | Planning actor | Copy rules, deferred work, and verification contract |
| Migration report | `docs/migration/git-post-merge-workflow-canonicalize.md` | Creator | Repo-visible copy result |
| Target skill folder | `skills/git-post-merge-workflow/` | Creator | New target-architecture canonical copy |
| Compatibility source | `.github/skills/git-post-merge-workflow/` | Existing repo artifact | Read-only source to copy from and preserve |

## Implementation Steps

1. verify the source inventory
2. copy the full required file set into `skills/git-post-merge-workflow/`
3. preserve `.github/skills/git-post-merge-workflow/` without edits
4. write the migration report with explicit deferred work
5. stop if any branch-policy or release-surface change would be required

## Validation / Acceptance Checks

- full file set present in `skills/git-post-merge-workflow/`
- `.github/skills/git-post-merge-workflow/` unchanged
- no STOP POINT 2 semantics changed
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
