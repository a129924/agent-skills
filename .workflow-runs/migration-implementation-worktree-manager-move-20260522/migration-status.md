# Migration Status

- topic: `worktree-manager-move`
- classification: `copied`
- reviewer_verdict: `approved`
- overlay_bound: `false`
- overlay_result: `skipped-not-bound`

## Decision

The topic is classified as `copied` because `skills/worktree-manager/` was
added as an exact-copy target-architecture tree while
`.github/skills/worktree-manager/` remained unchanged for transition-era
compatibility. Reviewer approval confirmed the copy stayed within the approved
bounded scope.

## Deferred Lanes

- Runtime or tool discovery cutover from `.github/skills/` to `skills/`
- `.codex/*` retargeting or provenance updates
- Repo-wide workflow path cutover or duplicate-tree cleanup
