# Migration Status

- topic: `python-helper-skill-promotion-wave-2`
- classification: `copied`
- reviewer_verdict: `approved`
- overlay_bound: `false`
- overlay_result: `skipped-not-bound`

## Decision

The topic is classified as `copied` because this wave promoted exactly the
locked 18 Python helper skill folders into `skills/` as folder-level direct
copies while preserving the corresponding `.github/skills/<skill-name>/`
folders unchanged as the transition-era active authored/reviewed path. Review
evidence records an `approved` verdict, matching file sets and file-content
hashes for all 18 direct-copy pairs, and no scope drift beyond the approved
promotion surfaces and workflow run directory.

## Deferred Lanes

- Any repo-wide active-path cutover from `.github/skills/` to `skills/`
- Any migration of `agent-skill-creator`, `agent-skill-reviewer`, or `agent-skill-template`
- Any runtime/tooling blocker repair or path-retargeting
- Any installer, projection, or platform-adapter switching work
- Any governance, positioning, README, VERSION, or release-surface updates
