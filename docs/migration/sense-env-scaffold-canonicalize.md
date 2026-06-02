# sense-env-scaffold-canonicalize

## Candidate

- `sense-env-scaffold`

## Verdict

- bounded canonical copy: completed
- active runtime path cutover: deferred

## Source And Target

- source root: `.github/skills/sense-env-scaffold/`
- target root: `skills/sense-env-scaffold/`

## Copied File Set

- `SKILL.md`
- `examples.md`
- `references/env-manifest-schema.md`
- `references/sense-env-cli-contract.md`
- `scripts/sense_env.py`
- `scripts/sense_env_runtime/__init__.py`
- `scripts/sense_env_runtime/contract.py`
- `scripts/sense_env_runtime/models.py`
- `scripts/sense_env_runtime/runtime.py`

## Compatibility Boundary

- `.github/skills/sense-env-scaffold/` remains present and unchanged
- transition-era compatibility surface preserved: yes
- active runtime path changed: no
- live executable path remains:
  - `.github/skills/sense-env-scaffold/scripts/sense_env.py`

## Deferred Runtime / Tooling Blockers

- downstream caller rewrites that still reference
  `.github/skills/sense-env-scaffold/scripts/sense_env.py`
- compatibility alias or alternate active CLI path design
- runtime-path transition for:
  - `python-project-init-greenfield`
  - `python-retrofit-plan-authoring`
  - `python-retrofit-plan-review`
  - `python-project-retrofit`
- manifest-output or snapshot-policy changes

## Validation Notes

- `diff -rq .github/skills/sense-env-scaffold skills/sense-env-scaffold` returned
  no differences after the copy
- no `.github/skills/sense-env-scaffold/` content was modified in this topic
- no downstream caller path was changed in this topic

## Excluded Surfaces

- `AGENTS.md`
- `docs/repo-positioning.md`
- `README.md`
- `VERSION`
- `.codex/*`
- `docs/migration/migration-runway-checklist.md`
- `docs/migration/platform-coupling-inventory.md`
