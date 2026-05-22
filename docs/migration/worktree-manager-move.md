# worktree-manager-move

## Candidate verdict

| Candidate | Verdict | Source path | Target path | Notes |
| --- | --- | --- | --- | --- |
| `worktree-manager` | `copied` | `.github/skills/worktree-manager/` | `skills/worktree-manager/` | Direct copy completed within the approved write set; source tree left unchanged |

## Copied result

- Added `skills/worktree-manager/` with:
  - `SKILL.md`
  - `checklist.md`
  - `reference.md`
  - `examples.md`
- Copy intent was exact content preservation from `.github/skills/worktree-manager/`.
- Local same-directory references remain usable after the copy because all referenced files were copied together without path rewriting.

## Preserved compatibility boundary

- `.github/skills/worktree-manager/` was not modified.
- This move does not change the current transition-era active workflow path.
- This move does not change `.codex/*`, repository governance files, runway checklist files, or any `.workflow-runs` artifact.
- Compatibility remains: source workflow content still exists under `.github/skills/worktree-manager/`, while `skills/worktree-manager/` now holds the copied canonical-target version for this topic.

## Deferred follow-up lanes

- Any projection or adapter switch that changes runtime/tool discovery from `.github/skills/` to `skills/`
- Any `.codex/skills` retargeting, provenance, or readability reconciliation
- Any repo-wide workflow cutover that changes authored/reviewed path semantics
- Any consolidation or cleanup decision for duplicate `worktree-manager` trees after the broader migration program authorizes it
