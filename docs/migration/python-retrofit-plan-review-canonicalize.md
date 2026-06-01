# python-retrofit-plan-review-canonicalize

## Candidate

- `python-retrofit-plan-review`

## Verdict

- bounded canonical copy: completed
- planning-spine gate redesign: deferred

## Source And Target

- source root: `.github/skills/python-retrofit-plan-review/`
- target root: `skills/python-retrofit-plan-review/`

## Copied File Set

- `SKILL.md`
- `examples.md`
- `checklist.md`
- `references/lane-fit-and-reroute.md`
- `references/retrofit-v2-review-checks.md`
- `references/review-verdict-contract.md`
- `references/risk-boundary-and-locatability-checks.md`

## Compatibility Boundary

- `.github/skills/python-retrofit-plan-review/` remains present and unchanged
- transition-era compatibility surface preserved: yes
- active authored/reviewed path changed: no
- review-verdict JSON contract, Retrofit V2 review checks, and sensing-assertion
  review boundaries changed: no

## Deferred Coupled Lanes

- `python-retrofit-plan-authoring` synchronization beyond bounded copy
- `python-project-retrofit` downstream gate synchronization beyond bounded copy
- any `sense-env-scaffold` assertion-kind or CLI behavior change
- any stable-library metadata, projection, or release-surface update

## Validation Notes

- `diff -rq .github/skills/python-retrofit-plan-review skills/python-retrofit-plan-review`
  returned no differences after the copy
- no `.github/skills/python-retrofit-plan-review/` content was modified in this
  topic
- no downstream planning-spine or executor artifact was changed in this topic

## Excluded Surfaces

- `AGENTS.md`
- `docs/repo-positioning.md`
- `README.md`
- `VERSION`
- `.codex/*`
- `docs/migration/migration-runway-checklist.md`
- `docs/migration/platform-coupling-inventory.md`
