# python-async-planning-canonicalize

## Candidate

- `python-async-planning`

## Verdict

- bounded canonical copy: completed
- broader workflow repair: deferred

## Source And Target

- source root: `.github/skills/python-async-planning/`
- target root: `skills/python-async-planning/`

## Copied File Set

- `SKILL.md`
- `reference.md`
- `examples.md`

## Compatibility Boundary

- `.github/skills/python-async-planning/` remains present and unchanged
- compatibility layer preserved: yes
- active path changed: no
- async trigger / exemption semantics changed: no

## Deferred Broader Workflow Lanes

- active-path switching for this skill
- repo-wide workflow or governance integration changes
- projection or release-surface updates

## Validation Notes

- `diff -rq .github/skills/python-async-planning skills/python-async-planning`
  should return no differences after the copy
- no `.github/skills/python-async-planning/` content should be modified in this topic
- no async-planning rule semantics should be changed in this topic

## Excluded Surfaces

- `AGENTS.md`
- `docs/repo-positioning.md`
- `README.md`
- `VERSION`
- `.codex/*`
