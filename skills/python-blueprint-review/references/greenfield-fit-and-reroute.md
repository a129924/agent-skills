# Greenfield Fit and Reroute

Use this reference when deciding whether an authored `blueprint.md` still belongs
to the greenfield lane.

## Ownership split

| Task | `python-blueprint-review` | Other owner |
| --- | --- | --- |
| Review an authored greenfield `blueprint.md` design baseline | Yes | No |
| Author or repair a greenfield blueprint | No | `python-blueprint-authoring` |
| Execute a blueprint | No | execution owner outside this review skill |
| Review a skill folder | No | `agent-skill-reviewer` |
| Handle retrofit or migration planning | No | `python-retrofit-plan-authoring` |

## What still counts as greenfield

Greenfield review is appropriate when the blueprint and surrounding facts describe:

- an empty, near-empty, or baseline-only repository
- the repository's first governed Python structure
- no need to preserve meaningful legacy entrypoints, packages, or config surfaces
- no migration or coexistence requirements

## Lane-mismatch signals

Return `needs-rework` and reroute when any of these appear:

- the blueprint says to preserve, move, merge, or retire existing files
- the request mentions legacy entrypoints, legacy packages, or current behavior preservation
- the work includes config migration such as `requirements.txt -> pyproject.toml`
- the blueprint tries to reshape an existing service into `src/` layout while keeping live surfaces intact
- the review request is really asking for authoring, execution, or approval of a non-blueprint artifact

## Reroute guidance

### Reroute to `python-blueprint-authoring`

When the issue is a malformed greenfield blueprint that should be repaired while
staying in the same lane.

### Reroute to `python-retrofit-plan-authoring`

When the blueprint or repository facts show retrofit or migration pressure.

## Review language pattern

When lane fit fails:

1. name the retrofit or migration signal explicitly
2. state that greenfield review cannot approve the contract as-is
3. return `needs-rework`
4. point the workflow toward the correct upstream lane instead of absorbing the mismatch
