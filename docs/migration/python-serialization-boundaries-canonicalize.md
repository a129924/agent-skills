# python-serialization-boundaries-canonicalize

## Candidate

- `python-serialization-boundaries`

## Verdict

- bounded canonical copy: completed
- routing / active-path repair: deferred

## Source And Target

- source root: `.github/skills/python-serialization-boundaries/`
- target root: `skills/python-serialization-boundaries/`

## Copied File Set

- `SKILL.md`
- `reference.md`
- `examples.md`
- `REVIEW.md`

## Compatibility Boundary

- `.github/skills/python-serialization-boundaries/` remains present and unchanged
- compatibility layer preserved: yes
- active path changed: no
- boundary semantics changed: no

## Deferred Lanes

- active-path switching
- adjacent-skill routing changes
- release-surface changes

## Validation Notes

- `diff -rq .github/skills/python-serialization-boundaries skills/python-serialization-boundaries`
  should return no differences after the copy
- no `.github/skills/python-serialization-boundaries/` content should be modified in this topic
