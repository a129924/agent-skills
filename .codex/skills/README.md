# `.codex/skills` Validation Surface

This directory is a bounded validation/projection surface for a dedicated Codex
spec worktree topic.

It is intentionally not the repository's canonical source of truth.

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

## Boundary

- do not treat this directory as cutover evidence
- do not edit projected skill content here as if it were canonical
- if a projected skill points to the wrong upstream source, fix the mapping
  rather than editing around the mismatch
