# `.codex/skills` Validation Surface

This directory is a bounded validation/projection surface for a dedicated Codex
spec worktree topic.

It is intentionally not the repository's canonical source of truth.

> **Read-only projection**: the skill entries in this directory are symlink
> projections to upstream sources in `skills/` or `.github/skills/`. Do not
> edit projected skill content here as if it were canonical. If a change is
> needed, make it in the upstream source and then revalidate the projection.

## Source Rule

- prefer `skills/<skill-name>/` when that skill already exists there
- otherwise project from `.github/skills/<skill-name>/`

## First-Wave Mapping

| Projected skill | Upstream source |
| --- | --- |
| `business-intent-alignment` | `skills/business-intent-alignment/` |
| `business-to-technical-translation` | `skills/business-to-technical-translation/` |
| `plan-creator` | `skills/plan-creator/` |
| `plan-reviewer` | `skills/plan-reviewer/` |
| `agent-skill-creator` | `.github/skills/agent-skill-creator/` |
| `agent-skill-reviewer` | `.github/skills/agent-skill-reviewer/` |
| `agent-skill-template` | `.github/skills/agent-skill-template/` |
| `git-commit-convention` | `.github/skills/git-commit-convention/` |
| `git-branch-naming` | `.github/skills/git-branch-naming/` |
| `git-post-merge-workflow` | `.github/skills/git-post-merge-workflow/` |
| `worktree-manager` | `.github/skills/worktree-manager/` |

## How to update a projected skill

1. Make the change in the upstream source listed in the table above.
2. Verify that `.codex/skills/<skill-name>` still points to the correct
   upstream path.
3. Update `.codex/skills/provenance.md` with the upstream path and the commit
   hash at which that projection was last revalidated.
4. Do not modify the projected path independently — divergence from upstream is
   a contract violation.

## Provenance requirement

Each projected skill must be traceable to exactly one upstream source path and
one last-validated source commit. Maintain `.codex/skills/provenance.md` with
at least:
- `skill_name`
- `upstream_path` (canonical source path in this repo)
- `projection_mode` (`symlink` for the current first-wave implementation)
- `source_commit` (commit hash at which the projection was last validated)

If provenance cannot be established for a projected skill, treat it as stale
and revalidate it against the current upstream source before use.

## Boundary

- do not treat this directory as cutover evidence
- do not edit projected skill content here as if it were canonical
- if a projected skill points to the wrong upstream source, fix the mapping
  rather than editing around the mismatch
