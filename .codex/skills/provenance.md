# `.codex/skills` Provenance

This file records the first-wave `.codex/skills` projection provenance.

Current implementation note:

- the first-wave surface now uses `materialized-copy` entries only
- materialized-copy entries are copied from canonical `skills/<skill-name>/`
  source folders into `.codex/skills/<skill-name>/`
- for materialized-copy entries, `.codex/skills/...` path concretization may be
  applied inside the copied files without modifying canonical source content
- `source_commit` records the commit at which the upstream source was last
  validated, not a copied snapshot commit
- this table is a partial allowlist only; it does not claim canonical
  completeness or authority symmetry

## First-wave provenance

| skill_name | upstream_path | materialization_mode | source_commit | validation_basis |
| --- | --- | --- | --- | --- |
| `business-intent-alignment` | `skills/business-intent-alignment/` | `materialized-copy` | `2bf4698` | `copied from canonical source; no .<platform>/skills/... residue remains` |
| `business-to-technical-translation` | `skills/business-to-technical-translation/` | `materialized-copy` | `2bf4698` | `copied from canonical source; no .<platform>/skills/... residue remains` |
| `plan-creator` | `skills/plan-creator/` | `materialized-copy` | `6056442` | `copied from canonical source; no .<platform>/skills/... residue remains` |
| `plan-reviewer` | `skills/plan-reviewer/` | `materialized-copy` | `c5bb8d6` | `copied from canonical source; no .<platform>/skills/... residue remains` |
| `agent-skill-creator` | `skills/agent-skill-creator/` | `materialized-copy` | `a4e6fe9` | `copied from canonical source and .codex/skills/... literals concretized where present` |
| `agent-skill-reviewer` | `skills/agent-skill-reviewer/` | `materialized-copy` | `a4e6fe9` | `copied from canonical source and .codex/skills/... literals concretized where present` |
| `agent-skill-template` | `skills/agent-skill-template/` | `materialized-copy` | `0528a54` | `copied from canonical source and .codex/skills/... literals concretized where present` |
| `git-commit-convention` | `skills/git-commit-convention/` | `materialized-copy` | `21cb5e5` | `copied from canonical source; no .<platform>/skills/... residue remains` |
| `git-branch-naming` | `skills/git-branch-naming/` | `materialized-copy` | `21cb5e5` | `copied from canonical source; no .<platform>/skills/... residue remains` |
| `git-post-merge-workflow` | `skills/git-post-merge-workflow/` | `materialized-copy` | `ff12a87` | `copied from canonical source; no .<platform>/skills/... residue remains` |
| `worktree-manager` | `skills/worktree-manager/` | `materialized-copy` | `00b6efd` | `copied from canonical source; no .<platform>/skills/... residue remains` |

## Revalidation rule

When an upstream source changes:

1. verify the entry's `materialization_mode`
2. rematerialize the `.codex` surface from canonical
   `skills/<skill-name>/` content and reapply required `.codex/skills/...`
   concretization inside copied files
3. confirm the mapping in `.codex/skills/README.md` is still correct
4. update the affected row in this file with the new validation commit and
   validation basis

If the source mapping cannot be verified, treat the materialized surface as
stale and do not use it as validation evidence.

Do not rewrite `source_commit` to describe uncommitted working-tree edits.
Revalidate and update the row after the relevant upstream change is committed.
