# Migration Status

- topic: `codex-skill-direct-move-impl-ab`
- classification: `copied`
- reviewer_verdict: `approved`
- overlay_bound: `true`
- overlay_result: `passed`

## Decision

The topic is classified as `copied` because the run added the 7 approved
`skills/<skill-name>/` targets while preserving the `.github/skills/`
counterparts as untouched read-only source context. No move, delete, or
cutover action occurred in this workflow.

## Deferred Lanes

- Any repo-wide active-path cutover away from `.github/skills/`
- Any deletion, rename, or rewrite under `.github/skills/`
- Any shared-governance or workflow-policy change under `docs/process/`
- Any publish, commit, push, PR, merge, or release action
