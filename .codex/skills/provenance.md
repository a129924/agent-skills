# `.codex/skills` Provenance

This file records the first-wave `.codex/skills` projection provenance.

Current implementation note:

- projection mode is `symlink`
- projected entries point directly at upstream source paths in this repository
- `source_commit` records the commit at which the symlink target and mapping
  were last validated, not a copied snapshot commit

## First-wave provenance

| skill_name | upstream_path | projection_mode | source_commit |
| --- | --- | --- | --- |
| `business-intent-alignment` | `skills/business-intent-alignment/` | `symlink` | `0ac01d4688717252651239600eafb4494572e48a` |
| `business-to-technical-translation` | `skills/business-to-technical-translation/` | `symlink` | `0ac01d4688717252651239600eafb4494572e48a` |
| `plan-creator` | `skills/plan-creator/` | `symlink` | `0ac01d4688717252651239600eafb4494572e48a` |
| `plan-reviewer` | `skills/plan-reviewer/` | `symlink` | `0ac01d4688717252651239600eafb4494572e48a` |
| `agent-skill-creator` | `.github/skills/agent-skill-creator/` | `symlink` | `0ac01d4688717252651239600eafb4494572e48a` |
| `agent-skill-reviewer` | `.github/skills/agent-skill-reviewer/` | `symlink` | `0ac01d4688717252651239600eafb4494572e48a` |
| `agent-skill-template` | `.github/skills/agent-skill-template/` | `symlink` | `0ac01d4688717252651239600eafb4494572e48a` |
| `git-commit-convention` | `.github/skills/git-commit-convention/` | `symlink` | `0ac01d4688717252651239600eafb4494572e48a` |
| `git-branch-naming` | `.github/skills/git-branch-naming/` | `symlink` | `0ac01d4688717252651239600eafb4494572e48a` |
| `git-post-merge-workflow` | `.github/skills/git-post-merge-workflow/` | `symlink` | `0ac01d4688717252651239600eafb4494572e48a` |
| `worktree-manager` | `.github/skills/worktree-manager/` | `symlink` | `0ac01d4688717252651239600eafb4494572e48a` |

## Revalidation rule

When an upstream source changes:

1. verify the symlink still points to the intended upstream path
2. confirm the mapping in `.codex/skills/README.md` is still correct
3. update the affected row in this file with the new validation commit

If the symlink target or source mapping cannot be verified, treat the
projection as stale and do not use it as validation evidence.
