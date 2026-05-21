# codex-low-risk-skill-move

## Branch

- `feat/andrew/codex-low-risk-skill-move`

## Topic result

- Branch-local execution mode: bounded low-risk move
- Candidate set executed: 2
- Skill content move performed: yes
- `.codex/skills` projection switch performed: no
- `.codex/skills` consistency metadata update performed: no

## Candidates moved

| Candidate | Source path | New target path | Move result | Codex readability | Notes |
| --- | --- | --- | --- | --- | --- |
| `git-commit-convention` | `.github/skills/git-commit-convention/` | `skills/git-commit-convention/` | moved | readable | `.codex/skills/git-commit-convention` still points to `.github/skills/git-commit-convention`; projection switch intentionally deferred |
| `git-branch-naming` | `.github/skills/git-branch-naming/` | `skills/git-branch-naming/` | moved | readable | `.codex/skills/git-branch-naming` still points to `.github/skills/git-branch-naming`; projection switch intentionally deferred |

## What moved

- Added `skills/git-commit-convention/` with:
  - `SKILL.md`
  - `examples.md`
  - `references/scope-alignment.md`
  - `references/type-selection.md`
  - `references/split-and-repair.md`
- Added `skills/git-branch-naming/` with:
  - `SKILL.md`
  - `examples.md`
  - `references/migration-playbooks.md`
  - `references/conflict-and-fallbacks.md`
  - `references/naming-patterns.md`

## What did not move

- `.github/skills/git-commit-convention/` remains unchanged.
- `.github/skills/git-branch-naming/` remains unchanged.
- `.github/skills/` remains the transition-era compatibility surface for this
  topic.
- `.codex/skills/git-commit-convention` remains projected to
  `.github/skills/git-commit-convention`.
- `.codex/skills/git-branch-naming` remains projected to
  `.github/skills/git-branch-naming`.
- No same-name divergence candidate was touched.
- No medium-residue, high-residue, or runtime/tooling blocker surface was
  touched.

## Projection status

- `.codex/skills` readability for both moved candidates remains `readable`.
- This topic does not claim that projection has switched to `skills/`.
- This topic does not change `.codex/skills/README.md`.
- This topic does not change `.codex/skills/provenance.md`.
- Projection switch remains a deferred follow-up topic.

## Validation summary

- Only the two locked `skills/...` targets were added.
- Source `.github/skills/...` files were not modified.
- Target file sets match the approved source file sets:
  - 5 files copied for `git-commit-convention`
  - 5 files copied for `git-branch-naming`
- Local relative references remain valid inside the new `skills/...` trees.
- No unapproved path was edited.

## Deferred items

- `.codex/skills` symlink retargeting to `skills/`
- `.codex/skills/README.md` source-rule reconciliation
- `.codex/skills/provenance.md` revalidation against any future projection
  switch
- repo-wide current-path governance change
