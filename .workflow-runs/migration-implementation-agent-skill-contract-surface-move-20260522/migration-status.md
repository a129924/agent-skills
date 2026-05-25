# Migration Status

- topic: `agent-skill-contract-surface-move`
- classification: `copied`
- reviewer_verdict: `approved`
- overlay_bound: `false`
- overlay_result: `skipped-not-bound`

## Decision

The topic is classified as `copied` because the three contract-surface skill
trees were added under `skills/` while the `.github/skills/agent-skill-*`
source trees remained unchanged for transition-era compatibility. Final
review-approved rework was limited to target-side canonical wording alignment
inside the approved Topic A write set.

## Deferred Lanes

- Active workflow-path cutover from `.github/skills/` to `skills/`
- `.codex/*`, runtime, installer, or projection retargeting
- Downstream planning-spine or duplicate-tree cleanup outside this bounded move
