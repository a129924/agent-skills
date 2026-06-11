# `.codex/skills` Validation Surface

This directory is a bounded validation/projection surface for a dedicated Codex
spec worktree topic.

It is intentionally not the repository's canonical source of truth.

It is also intentionally partial:

- only the explicitly listed first-wave entries are projected here
- absence from this directory does not imply a skill is non-canonical
- presence here does not imply symmetric authority with `skills/` or
  `.github/skills/`

> **Read-only projection**: the first-wave skill entries in this directory are
> `.codex`-local materialized copies sourced from canonical skill folders in
> this repository. Do not edit skill content here as if it were canonical. If a
> change is needed, make it in the upstream source and then rematerialize this
> surface.

## Source Rule

- use `skills/<skill-name>/` as the canonical upstream source for every
  first-wave entry listed below
- rematerialize `.codex/skills/<skill-name>/` from `skills/<skill-name>/`
  whenever the upstream canonical source changes
- apply `.codex/skills/...` concretization only inside this materialized
  surface when copied content still contains `.<platform>/skills/...`
- do not infer completeness, cutover readiness, or authority parity from the
  current first-wave mapping table

## First-Wave Mapping

| Projected skill | Upstream source | Surface mode |
| --- | --- | --- |
| `business-intent-alignment` | `skills/business-intent-alignment/` | `materialized-copy` |
| `business-to-technical-translation` | `skills/business-to-technical-translation/` | `materialized-copy` |
| `plan-creator` | `skills/plan-creator/` | `materialized-copy` |
| `plan-reviewer` | `skills/plan-reviewer/` | `materialized-copy` |
| `agent-skill-creator` | `skills/agent-skill-creator/` | `materialized-copy` |
| `agent-skill-reviewer` | `skills/agent-skill-reviewer/` | `materialized-copy` |
| `agent-skill-template` | `skills/agent-skill-template/` | `materialized-copy` |
| `git-commit-convention` | `skills/git-commit-convention/` | `materialized-copy` |
| `git-branch-naming` | `skills/git-branch-naming/` | `materialized-copy` |
| `git-post-merge-workflow` | `skills/git-post-merge-workflow/` | `materialized-copy` |
| `worktree-manager` | `skills/worktree-manager/` | `materialized-copy` |

## How to update a projected skill

1. Make the change in the upstream source listed in the table above.
2. Rematerialize the `.codex/skills/<skill-name>`
   directory from the canonical `skills/<skill-name>/` source and reapply any
   required `.codex/skills/...` path concretization inside the copied files.
3. Update `.codex/skills/provenance.md` with the upstream path, surface mode,
   source commit, and validation basis.
4. Do not modify the projected path independently — divergence from upstream is
   a contract violation.

## Provenance requirement

Each projected skill must be traceable to exactly one upstream source path,
one materialization mode, and one last-validated source commit. Maintain
`.codex/skills/provenance.md` with at least:
- `skill_name`
- `upstream_path` (canonical source path in this repo)
- `materialization_mode` (`materialized-copy` for the current first-wave surface)
- `source_commit` (commit hash at which the upstream source was last validated)
- `validation_basis` (what was checked or rematerialized)

If provenance cannot be established for a projected skill, treat it as stale
and revalidate it against the current upstream source before use.

## Boundary

- do not treat this directory as cutover evidence
- do not treat this directory as a third authority tree
- do not reason about canonical-scope completeness from this partial allowlist
- do not edit projected skill content here as if it were canonical
- if a projected skill points to the wrong upstream source, fix the mapping
  rather than editing around the mismatch
