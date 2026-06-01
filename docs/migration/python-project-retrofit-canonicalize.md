# python-project-retrofit-canonicalize

## Candidate

- `python-project-retrofit`

## Verdict

- bounded canonical copy: completed
- runtime/tooling blocker repair: deferred

## Source And Target

- source root: `.github/skills/python-project-retrofit/`
- target root: `skills/python-project-retrofit/`

## Copied File Set

- `SKILL.md`
- `examples.md`
- `references/retrofit-conflict-resolution.md`
- `references/retrofit-plan-v2-contract.md`
- `references/retrofit-safety-guidelines.md`
- `references/sensing-delta-contract.md`

## Compatibility Boundary

- `.github/skills/python-project-retrofit/` remains present and unchanged
- transition-era compatibility surface preserved: yes
- active runtime path changed: no
- acceptance handoff path changed: no
- live acceptance handoff remains:
  - `python3 .github/skills/sense-env-scaffold/scripts/sense_env.py --mode acceptance --contract-file retrofit-plan.md`

## Confirmed-Blocker Context

- confirmed-blocker context preserved: yes
- confirmed-blocker status remains evidence context only in this topic
- no runtime/tooling blocker repair was performed in this topic

## Deferred Runtime / Tooling Blockers

- downstream replacement of
  `.github/skills/sense-env-scaffold/scripts/sense_env.py` as the acceptance path
- compatibility alias or alternate active executor path design
- delta-report schema changes
- provenance path-policy or behavior changes
- runtime-path transition work for `python-project-init-greenfield`
- stable-library metadata, projection, or release-surface update

## Validation Notes

- `diff -rq .github/skills/python-project-retrofit skills/python-project-retrofit`
  returned no differences after the copy
- no `.github/skills/python-project-retrofit/` content was modified in this
  topic
- no runtime/tooling caller path was changed in this topic

## Excluded Surfaces

- `AGENTS.md`
- `docs/repo-positioning.md`
- `README.md`
- `VERSION`
- `.codex/*`
- `docs/migration/migration-runway-checklist.md`
- `docs/migration/platform-coupling-inventory.md`
