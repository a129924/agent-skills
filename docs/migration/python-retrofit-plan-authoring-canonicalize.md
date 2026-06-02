# python-retrofit-plan-authoring-canonicalize

## Candidate

- `python-retrofit-plan-authoring`

## Verdict

- bounded canonical copy: completed
- planning-spine redesign: deferred

## Source And Target

- source root: `.github/skills/python-retrofit-plan-authoring/`
- target root: `skills/python-retrofit-plan-authoring/`

## Copied File Set

- `SKILL.md`
- `examples.md`
- `checklist.md`
- `references/authoring-vs-executor-boundaries.md`
- `references/migration-strategy-risk-model.md`
- `references/retrofit-v2-contract.md`

## Compatibility Boundary

- `.github/skills/python-retrofit-plan-authoring/` remains present and unchanged
- transition-era compatibility surface preserved: yes
- active authored/reviewed path changed: no
- Retrofit V2 section-order, risk-metadata, and sensing-assertion authoring
  semantics changed: no

## Deferred Coupled Lanes

- `python-retrofit-plan-review` canonicalization
- `python-project-retrofit` canonicalization or contract synchronization
- any `sense-env-scaffold` assertion execution or CLI-path change
- any stable-library metadata, projection, or release-surface update

## Validation Notes

- `diff -rq .github/skills/python-retrofit-plan-authoring skills/python-retrofit-plan-authoring`
  returned no differences after the copy
- no `.github/skills/python-retrofit-plan-authoring/` content was modified in
  this topic
- no downstream planning-spine or executor artifact was changed in this topic

## Excluded Surfaces

- `AGENTS.md`
- `docs/repo-positioning.md`
- `README.md`
- `VERSION`
- `.codex/*`
- `docs/migration/migration-runway-checklist.md`
- `docs/migration/platform-coupling-inventory.md`
