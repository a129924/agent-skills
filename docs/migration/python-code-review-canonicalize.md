# python-code-review-canonicalize

## Candidate

- `python-code-review`

## Verdict

- bounded canonical copy: completed
- confirmed-blocker preservation: completed
- runtime/tooling blocker repair: deferred

## Source And Target

- source root: `.github/skills/python-code-review/`
- target root: `skills/python-code-review/`

## Copied File Set

- `SKILL.md`
- `examples.md`
- `reference.md`
- `references/anti-patterns.md`
- `references/cross-skill-signposts.md`
- `references/observability.md`
- `references/test-quality.md`
- `references/tooling-detection.md`

## Compatibility Boundary

- `.github/skills/python-code-review/` remains present and unchanged
- compatibility layer preserved: yes
- active path changed: no
- transition-era sequencing/tooling surfaces changed: no
- live gate / tooling / verdict expectations remain:
  - `python-code-review` still requires prior
    `python-implementation-review` approval
  - tooling detection still stops at the first positive match across
    `pyproject.toml`, `Makefile`, `README.md` / `CONTRIBUTING.md`, then fallback
  - strict-mode projects still escalate `Any`, missing annotations, and
    unjustified ignores per the current source contract
  - one or more `blocking` findings still produces `needs-rework`

## Confirmed-Blocker Context

- confirmed-blocker context preserved: yes
- confirmed-blocker status remains evidence context only in this topic
- no runtime/tooling blocker repair was performed in this topic

## Deferred Lanes / Blocker Context

- changing the sequencing gate away from
  `python-implementation-review` approval
- changing tooling detection priority order or strict-mode escalation behavior
- changing verdict mapping from `blocking` findings to `needs-rework`
- changing cross-skill routing or quality-dimension ownership rules
- changing downstream active-path assumptions for review execution
- changing projection, stable-library metadata, or release surfaces

## Validation Notes

- `diff -rq .github/skills/python-code-review skills/python-code-review`
  returned no differences after the copy
- no `.github/skills/python-code-review/` content was modified in this topic
- no sequencing-gate, tooling-detection, verdict-output, or routing behavior
  was changed in this topic

## Excluded Surfaces

- `AGENTS.md`
- `docs/repo-positioning.md`
- `README.md`
- `VERSION`
- `.codex/*`
