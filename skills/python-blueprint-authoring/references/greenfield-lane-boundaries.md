# Greenfield Lane Boundaries

Use this reference to decide whether `python-blueprint-authoring` is the right
skill.

## Ownership split

| Task | `python-blueprint-authoring` | Other owner |
| --- | --- | --- |
| Author a review-ready greenfield `blueprint.md` | Yes | No |
| Repair a malformed greenfield `blueprint.md` without changing lanes | Yes | No |
| Execute a valid greenfield blueprint | No | `python-project-init-greenfield` |
| Author a plan for an existing Python repository | No | `python-retrofit-plan-authoring` |
| Execute retrofit changes | No | `python-project-retrofit` |
| Approve the authored blueprint | No | reviewer flow |

## What counts as greenfield or baseline-only

Use this skill when the repository is:

- empty, near-empty, or only baseline-like
- still choosing its first governed Python structure
- not trying to preserve meaningful legacy application structure
- not asking for migration of existing entrypoints, packages, or config surfaces

## Lane-mismatch triggers

Stop and ask or reroute when any of these is true:

- the repository already has meaningful files that must be preserved, moved,
  merged, or retired
- the request mentions current entrypoints, legacy packages, or config migration
  such as `requirements.txt -> pyproject.toml`
- the user wants to reshape an existing service into `src/` layout
- the request mixes “create the first baseline” with retrofit expectations such as
  coexistence, migration, or preservation of current runtime behavior
- the task is really execution, review, or approval rather than upstream authoring

## Rerouting guidance

### Route to `python-project-init-greenfield`

When the blueprint already exists and the task is to scaffold the repository from
that contract.

### Route to `python-retrofit-plan-authoring`

When an existing repository needs a retrofit contract because current structure,
config, or entrypoints materially matter.

### Route to reviewer flow

When the blueprint already exists and the task is to judge, approve, or reject it.

## Stop-and-ask rule

If lane fit cannot be established confidently from the available facts, stop and
ask before drafting. Do not force retrofit work into a greenfield blueprint just
because the target state sounds similar.
