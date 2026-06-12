# Lane Fit and Reroute

Use this reference when deciding whether an authored contract still belongs in the
Retrofit V2 review lane.

## Ownership split

| Task | `python-retrofit-plan-review` | Other owner |
| --- | --- | --- |
| Review an authored Retrofit V2 `retrofit-plan.md` contract | Yes | No |
| Author or repair a retrofit plan | No | `python-retrofit-plan-authoring` |
| Execute a valid retrofit plan | No | `python-project-retrofit` |
| Review an authored greenfield `blueprint.md` | No | `python-blueprint-review` |
| Author a greenfield blueprint | No | `python-blueprint-authoring` |
| Review a skill folder | No | `agent-skill-reviewer` |
| Review an implementation diff | No | `/review` or equivalent diff-review path |

## What still counts as retrofit review

Retrofit review is appropriate when the authored contract and surrounding facts
describe:
- an existing Python repository with meaningful current-state surfaces
- migration or preservation pressure that requires retrofit planning
- concrete before-versus-after structure that `python-project-retrofit` could execute once approved
- a review request focused on the authored `retrofit-plan.md` contract itself

## Lane-mismatch signals

Return `needs-rework` and reroute when any of these appear:
- the repository is empty, near-empty, or baseline-only and needs first-structure setup instead of migration
- the request is really asking to author or repair the retrofit contract rather than review it
- the request is really asking to execute retrofit work
- the artifact is actually a greenfield blueprint or a greenfield-shaped request with no meaningful current-state preservation
- the task is a skill-folder review, topic-plan review, or implementation-diff review

## Reroute guidance

### Reroute to `python-retrofit-plan-authoring`

When the artifact is still retrofit-shaped but malformed, contradictory, too
abstract, or otherwise needs contract repair before it can be reviewed cleanly.

### Reroute to `python-blueprint-authoring`

When the contract or repository facts show first-structure baseline work rather
than retrofit migration.

### Reroute to `python-blueprint-review`

When the review target is an authored greenfield `blueprint.md`, not a
`retrofit-plan.md`.

### Reroute to `python-project-retrofit`

Only after the retrofit review verdict is `approved`.

## Review language pattern

When lane fit fails:
1. name the wrong-lane signal explicitly
2. state that Retrofit V2 review cannot approve the contract as-is
3. return `needs-rework`
4. point the workflow toward the correct upstream or downstream lane instead of absorbing the mismatch
