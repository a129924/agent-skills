# Codex Readability Baseline

## Branch

- `feat/andrew/codex-readability-baseline`

## Topic result

- Branch-local execution mode: inventory-only
- Candidate set source: `.codex/skills/provenance.md`
- Skill content migration performed: no
- Projection repair performed: no

## Evidence basis

- `.codex/skills/README.md`
- `.codex/skills/provenance.md`
- `analysis/codex-readability-baseline/requirements.md`
- `plan/codex-readability-baseline/codex-readability-baseline.plan.md`
- `docs/migration/migration-runway-checklist.md`
- `docs/migration/platform-coupling-inventory.md`
- `docs/migration/codex-migration-direct-move-report.md`
- `docs/migration/codex-migration-copilot-residue-low-report.md`
- `docs/migration/codex-migration-copilot-residue-medium-report.md`
- `docs/migration/codex-migration-copilot-residue-high-report.md`

## Baseline field semantics

- `move_status`
  - `moved`: upstream canonical exists under `skills/`
  - `not-moved`: no upstream canonical exists under `skills/`
  - `same-name-pass`: same-name skill exists under both `skills/` and
    `.github/skills/`; this branch records it but does not resolve it
- `codex_readability`
  - `readable`: `.codex/skills/<name>` exists and matches provenance-backed
    upstream mapping
  - `not-readable`: no usable projection exists
  - `stale-projection`: projection exists but mapping or provenance is not safe
- `source_authority`
  - `skills/`
  - `.github/skills/`
  - `mixed/unresolved`
- `follow_up`
  - `none`
  - `divergence-review`
  - `projection-fix`
  - `runtime/tooling-blocker`

## First-wave baseline

| Skill | move_status | codex_readability | source_authority | follow_up | Why |
| --- | --- | --- | --- | --- | --- |
| `business-intent-alignment` | `same-name-pass` | `readable` | `mixed/unresolved` | `divergence-review` | Both `skills/business-intent-alignment/` and `.github/skills/business-intent-alignment/` exist. `.codex/skills/business-intent-alignment` points to `skills/` and is provenance-backed, but this branch does not resolve dual-surface authority. |
| `business-to-technical-translation` | `same-name-pass` | `readable` | `mixed/unresolved` | `divergence-review` | Both `skills/business-to-technical-translation/` and `.github/skills/business-to-technical-translation/` exist. The Codex projection is valid, but same-name authority still belongs to a later divergence topic. |
| `plan-creator` | `same-name-pass` | `readable` | `mixed/unresolved` | `divergence-review` | Both `skills/plan-creator/` and `.github/skills/plan-creator/` exist. The first-wave projection prefers `skills/`, but repo-wide canonical convergence is still unresolved in this branch. |
| `plan-reviewer` | `same-name-pass` | `readable` | `mixed/unresolved` | `divergence-review` | Both `skills/plan-reviewer/` and `.github/skills/plan-reviewer/` exist. The projection is readable and provenance-backed, but same-name authority is intentionally deferred. |
| `agent-skill-creator` | `not-moved` | `readable` | `.github/skills/` | `divergence-review` | No `skills/agent-skill-creator/` exists. `.codex/skills/agent-skill-creator` points to `.github/skills/agent-skill-creator/`, and the transition-complete authoring-path evidence remains readable. The candidate still belongs to a downstream path-transition / convergence lane rather than low-risk completion. |
| `agent-skill-reviewer` | `not-moved` | `readable` | `.github/skills/` | `divergence-review` | No `skills/agent-skill-reviewer/` exists. The Codex projection is present and provenance-backed, and the current candidate remains a medium-residue but readable contract surface that still needs later convergence work. |
| `agent-skill-template` | `not-moved` | `readable` | `.github/skills/` | `divergence-review` | No `skills/agent-skill-template/` exists. The projection works and provenance is complete, while actual template-path transition remains out of scope for this branch and still requires later convergence review. |
| `git-commit-convention` | `not-moved` | `readable` | `.github/skills/` | `none` | No `skills/git-commit-convention/` exists. The low-residue report found no blocker-bearing follow-up, and the current projection remains readable. |
| `git-branch-naming` | `not-moved` | `readable` | `.github/skills/` | `none` | No `skills/git-branch-naming/` exists. The low-residue report confirms the current `.github/skills/` wording is stable, and the Codex projection maps cleanly to that path. |
| `git-post-merge-workflow` | `not-moved` | `readable` | `.github/skills/` | `divergence-review` | No `skills/git-post-merge-workflow/` exists, but the high-residue report marks the candidate `redesign`. The projection is readable, yet this candidate is not a low-risk completion and needs a later redesign-oriented follow-up. |
| `worktree-manager` | `not-moved` | `readable` | `.github/skills/` | `divergence-review` | No `skills/worktree-manager/` exists. The medium-residue report found bounded workflow/contract residue without blocker coupling, so Codex can read it now, but later convergence still needs an explicit follow-up topic. |

## Same-name pass backlog

These skills were intentionally collected but not converged in this branch:

- `business-intent-alignment`
- `business-to-technical-translation`
- `plan-creator`
- `plan-reviewer`

Backlog rule:

- do not treat their `readable` projection state as proof that same-name
  dual-surface evolution is resolved
- route them to a later divergence topic before declaring single-source
  convergence

## Summary

- All 11 first-wave projected skills are currently `readable` through
  `.codex/skills`.
- 4 first-wave skills are `same-name-pass` and therefore not counted as
  low-risk migration completion.
- 7 first-wave skills remain `not-moved + readable`, which is an allowed state
  in this baseline.
- No candidate in this branch required `projection-fix`.
- No candidate in this branch required runtime/tooling blocker routing from the
  current evidence set.

## Next routing recommendation

- First follow-up candidate: same-name divergence review for:
  - `business-intent-alignment`
  - `business-to-technical-translation`
  - `plan-creator`
  - `plan-reviewer`
- Separate later follow-up candidate:
  - redesign-oriented review for `git-post-merge-workflow`
