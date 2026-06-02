# python-project-init-greenfield-canonicalize

## Candidate

- `python-project-init-greenfield`

## Verdict

- bounded canonical copy: completed
- confirmed-blocker preservation: completed
- runtime/tooling blocker repair: deferred

## Source And Target

- source root: `.github/skills/python-project-init-greenfield/`
- target root: `skills/python-project-init-greenfield/`

## Copied File Set

- `SKILL.md`
- `examples.md`
- `references/baseline-generation-rules.md`
- `references/blueprint-parsing-contract.md`

## Compatibility Boundary

- `.github/skills/python-project-init-greenfield/` remains present and unchanged
- compatibility layer preserved: yes
- active path changed: no
- transition-era output surfaces changed: no
- live acceptance handoff remains:
  - `python3 .github/skills/sense-env-scaffold/scripts/sense_env.py --mode acceptance --contract-file blueprint.md`

## Confirmed-Blocker Context

- confirmed-blocker context preserved: yes
- confirmed-blocker status remains evidence context only in this topic
- no runtime/tooling blocker repair was performed in this topic

## Deferred Lanes / Blocker Context

- changing required-skill deployment away from `.github/skills/`
- moving governance provenance away from `.github/skills-provenance.json`
- changing `.github/copilot-instructions.md` output policy or destination
- changing the acceptance handoff path away from
  `.github/skills/sense-env-scaffold/scripts/sense_env.py`
- changing projection, stable-library metadata, or release surfaces

## Validation Notes

- `diff -rq .github/skills/python-project-init-greenfield skills/python-project-init-greenfield`
  returned no differences after the copy
- no `.github/skills/python-project-init-greenfield/` content was modified in
  this topic
- no runtime/tooling caller or output-surface behavior was changed in this topic

## Excluded Surfaces

- `AGENTS.md`
- `docs/repo-positioning.md`
- `README.md`
- `VERSION`
- `.codex/*`
