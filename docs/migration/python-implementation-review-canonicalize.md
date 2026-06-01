# python-implementation-review-canonicalize

## Candidate

- `python-implementation-review`

## Verdict

- bounded canonical copy: completed
- confirmed-blocker preservation: completed
- runtime/tooling blocker repair: deferred

## Source And Target

- source root: `.github/skills/python-implementation-review/`
- target root: `skills/python-implementation-review/`

## Copied File Set

- `SKILL.md`
- `examples.md`
- `reference.md`
- `references/contract-deviation-rules.md`
- `references/plan-section-structure.md`
- `references/semantic-boundaries.md`
- `references/traceability-status.md`

## Compatibility Boundary

- `.github/skills/python-implementation-review/` remains present and unchanged
- compatibility layer preserved: yes
- active path changed: no
- transition-era gate surfaces changed: no
- live gate / sequencing expectations remain:
  - formal approval still comes from `python-plan-review`
  - optional step gating still resolves through `plan/<topic>/<topic>.step.md`
  - pending implementation steps still produce a BLOCKED plain-text refusal
  - `python-implementation-review` still runs before `python-code-review`

## Confirmed-Blocker Context

- confirmed-blocker context preserved: yes
- confirmed-blocker status remains evidence context only in this topic
- no runtime/tooling blocker repair was performed in this topic

## Deferred Lanes / Blocker Context

- changing approval proof requirements away from the current
  `python-plan-review` contract
- changing `plan/<topic>/<topic>.step.md` gating semantics or pending-step
  detection rules
- changing BLOCKED refusal output semantics
- changing the sequencing dependency between
  `python-implementation-review` and `python-code-review`
- changing downstream active-path assumptions for review execution
- changing projection, stable-library metadata, or release surfaces

## Validation Notes

- `diff -rq .github/skills/python-implementation-review skills/python-implementation-review`
  returned no differences after the copy
- no `.github/skills/python-implementation-review/` content was modified in
  this topic
- no approval-gate, step-gate, refusal-output, or sequencing behavior was
  changed in this topic

## Excluded Surfaces

- `AGENTS.md`
- `docs/repo-positioning.md`
- `README.md`
- `VERSION`
- `.codex/*`
