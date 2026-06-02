# copilot-instructions-init-canonicalize

## Candidate

- `copilot-instructions-init`

## Verdict

- bounded canonical copy: completed
- confirmed-blocker preservation: completed
- runtime/tooling blocker repair: deferred

## Source And Target

- source root: `.github/skills/copilot-instructions-init/`
- target root: `skills/copilot-instructions-init/`

## Copied File Set

- `SKILL.md`
- `checklist.md`
- `examples.md`
- `references/input-sources-and-priority.md`
- `references/instruction-layering.md`
- `references/merge-and-conflict-policy.md`

## Compatibility Boundary

- `.github/skills/copilot-instructions-init/` remains present and unchanged
- compatibility layer preserved: yes
- active path changed: no
- transition-era output surfaces changed: no
- live target output remains:
  - target-project `.github/copilot-instructions.md`

## Confirmed-Blocker Context

- confirmed-blocker context preserved: yes
- confirmed-blocker status remains evidence context only in this topic
- no runtime/tooling blocker repair was performed in this topic

## Deferred Lanes / Blocker Context

- changing the target output destination away from target-project `.github/copilot-instructions.md`
- changing stale-fact coupling away from `.github/skills/` summary fingerprints
- changing managed-block marker policy or materially-different classification behavior
- changing overwrite / keep / manual-merge decision policy
- changing downstream active-path assumptions for instruction generation
- changing projection, stable-library metadata, or release surfaces

## Validation Notes

- `diff -rq .github/skills/copilot-instructions-init skills/copilot-instructions-init`
  returned no differences after the copy
- no `.github/skills/copilot-instructions-init/` content was modified in this
  topic
- no target output-path, stale-fingerprint policy, or merge-policy behavior was
  changed in this topic

## Excluded Surfaces

- `AGENTS.md`
- `docs/repo-positioning.md`
- `README.md`
- `VERSION`
- `.codex/*`
