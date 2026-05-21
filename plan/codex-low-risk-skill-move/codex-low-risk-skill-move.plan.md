# codex-low-risk-skill-move

## Goal / Outcome

- Move the two first-wave low-risk candidates into `skills/`:
  - `git-commit-convention`
  - `git-branch-naming`
- Preserve transition-era `.github/skills/` compatibility semantics while the
  move is implemented.
- Leave one repo-visible migration artifact that records move completion,
  Codex readability, and deferred boundaries.

## Scope

- **In scope**:
  - `analysis/codex-low-risk-skill-move/requirements.md`
  - `plan/codex-low-risk-skill-move/codex-low-risk-skill-move.plan.md`
  - `docs/migration/codex-low-risk-skill-move.md`
  - `skills/git-commit-convention/`
  - `skills/git-branch-naming/`
  - minimal `.codex/skills` consistency updates if needed to keep the two
    candidates readable and provenance-backed

- **Out of scope**:
  - same-name skill convergence
  - `.github/skills/agent-skill-*` or `.github/skills/worktree-manager/`
    medium-residue work
  - `.github/skills/git-post-merge-workflow/` redesign
  - runtime/tooling blocker repair
  - repo-wide active-path cutover wording changes in governance artifacts

## Locked Decisions

- This topic implements only the two low-risk candidates selected by
  `docs/migration/codex-readability-baseline.md`.
- This topic is a stable-library-affecting move topic with deferred release
  timing.
- `skills/` receives the new target-architecture copies for the two candidates.
- `.github/skills/` remains the transition-era compatibility surface and is not
  demoted or retired by this branch.
- `.codex/skills` may be touched only for minimal mapping/provenance
  consistency related to these two candidates.
- README / VERSION / tag work is deferred until after merge and explicit human
  release handling.

## Boundaries / Exclusions

- Do not edit any same-name pass candidate under this topic.
- Do not widen into creator/reviewer/template contract transition.
- Do not repair executable-path or generator-coupled runtime/tooling surfaces.
- Do not change `AGENTS.md`, `docs/repo-positioning.md`, or
  `.github/copilot-instructions.md` to claim repo-wide current-path cutover.
- If the move requires editing any path outside `Artifact Paths`, stop and
  re-plan instead of improvising.

## Status / Allowed Transitions

- **Current**: `planned`
- **Execution model**: follow the canonical creator -> reviewer -> publish ->
  merge -> release path; this topic implements branch-local move work first and
  defers README / VERSION / tag handling to the explicit post-merge release
  step
- **Allowed transitions**:
  - `planned` -> `creator-in-progress`
  - `creator-in-progress` -> `review-ready`
  - `review-ready` -> `reviewer-in-progress`
  - `reviewer-in-progress` -> `approved`
  - `reviewer-in-progress` -> `needs-rework`
  - `needs-rework` -> `creator-in-progress`
  - `approved` -> `creator-in-progress`
  - `approved` -> `publish-in-progress`
  - `publish-in-progress` -> `pr-open`
  - `publish-in-progress` -> `merged`
  - `pr-open` -> `needs-rework`
  - `pr-open` -> `merged`
  - `merged` -> `released`
  - `released` -> terminal

Routing notes:

- Branch target: `feat/andrew/codex-low-risk-skill-move`
- Base branch: `dev`
- Use the standard Phase 4.5 planner-alignment rule after reviewer approval.
- This topic should not be reclassified into same-name divergence or
  runtime/tooling blocker work without a new plan.
- Semantic warning: `analysis/codex-low-risk-skill-move/technical-spec.md` is
  intentionally absent; this plan is authored from the locked requirements
  baseline only.

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/codex-low-risk-skill-move/codex-low-risk-skill-move.plan.md` | Planning actor | Repo-visible execution contract |
| Requirements baseline | `analysis/codex-low-risk-skill-move/requirements.md` | Planning actor | Locked candidate set, move rules, and stop conditions |
| Migration report | `docs/migration/codex-low-risk-skill-move.md` | Creator | Repo-visible move result and deferred-boundary evidence |
| Target skill file | `skills/git-commit-convention/SKILL.md` | Creator | New target-architecture primary instruction file for low-risk candidate |
| Target skill file | `skills/git-commit-convention/examples.md` | Creator | Target-architecture example set copied from the current compatibility surface |
| Target skill file | `skills/git-commit-convention/references/scope-alignment.md` | Creator | Target-architecture reference file required by the moved skill |
| Target skill file | `skills/git-commit-convention/references/type-selection.md` | Creator | Target-architecture reference file required by the moved skill |
| Target skill file | `skills/git-commit-convention/references/split-and-repair.md` | Creator | Target-architecture reference file required by the moved skill |
| Target skill file | `skills/git-branch-naming/SKILL.md` | Creator | New target-architecture primary instruction file for low-risk candidate |
| Target skill file | `skills/git-branch-naming/examples.md` | Creator | Target-architecture example set copied from the current compatibility surface |
| Target skill file | `skills/git-branch-naming/references/migration-playbooks.md` | Creator | Target-architecture reference file required by the moved skill |
| Target skill file | `skills/git-branch-naming/references/conflict-and-fallbacks.md` | Creator | Target-architecture reference file required by the moved skill |
| Target skill file | `skills/git-branch-naming/references/naming-patterns.md` | Creator | Target-architecture reference file required by the moved skill |
| Compatibility source file | `.github/skills/git-commit-convention/SKILL.md` | Existing repo artifact | Transition-era compatibility source to copy from and preserve |
| Compatibility source file | `.github/skills/git-commit-convention/examples.md` | Existing repo artifact | Transition-era compatibility example source to copy from and preserve |
| Compatibility source file | `.github/skills/git-commit-convention/references/scope-alignment.md` | Existing repo artifact | Transition-era compatibility reference source to copy from and preserve |
| Compatibility source file | `.github/skills/git-commit-convention/references/type-selection.md` | Existing repo artifact | Transition-era compatibility reference source to copy from and preserve |
| Compatibility source file | `.github/skills/git-commit-convention/references/split-and-repair.md` | Existing repo artifact | Transition-era compatibility reference source to copy from and preserve |
| Compatibility source file | `.github/skills/git-branch-naming/SKILL.md` | Existing repo artifact | Transition-era compatibility source to copy from and preserve |
| Compatibility source file | `.github/skills/git-branch-naming/examples.md` | Existing repo artifact | Transition-era compatibility example source to copy from and preserve |
| Compatibility source file | `.github/skills/git-branch-naming/references/migration-playbooks.md` | Existing repo artifact | Transition-era compatibility reference source to copy from and preserve |
| Compatibility source file | `.github/skills/git-branch-naming/references/conflict-and-fallbacks.md` | Existing repo artifact | Transition-era compatibility reference source to copy from and preserve |
| Compatibility source file | `.github/skills/git-branch-naming/references/naming-patterns.md` | Existing repo artifact | Transition-era compatibility reference source to copy from and preserve |
| Baseline evidence | `docs/migration/codex-readability-baseline.md` | Existing repo artifact | Source of low-risk candidate selection and current readability state |
| Low-residue evidence | `docs/migration/codex-migration-copilot-residue-low-report.md` | Existing repo artifact | Evidence for why the two candidates qualify as low-residue move targets |
| Projection rule | `.codex/skills/README.md` | Existing repo artifact | Read-only source-rule evidence unless minimal consistency update becomes necessary |
| Projection provenance | `.codex/skills/provenance.md` | Existing repo artifact | Read-only mapping evidence unless minimal consistency update becomes necessary |

Artifact path notes:

- This topic does not modify `AGENTS.md`, `docs/repo-positioning.md`, or
  `.github/copilot-instructions.md`.
- `README.md` and `VERSION` are intentionally excluded from branch-local
  implementation and are handled only after merge by the release actor.
- If execution requires editing any other path, stop and repair this plan
  before continuing.

## Stable library metadata

- `README row`: no README row change; the existing `git-branch-naming` and
  `git-commit-convention` rows remain unchanged during the release step for
  this topic
- `VERSION bump`: patch bump during the explicit post-merge release step
- `timing`: `release`
- `rationale`: this topic creates new `skills/` target-architecture folders,
  but release-visible metadata should change only after merge and human-approved
  release handling, not during branch-local implementation
- `release-note expectations`: if merged, the post-merge release actor should
  mention that two low-risk skills now exist under `skills/` while
  `.github/skills/` remains the transition-era compatibility surface

## Implementation Steps

1. Copy the current transition-era source content from:
   - `.github/skills/git-commit-convention/`
   - `.github/skills/git-branch-naming/`
   into new `skills/` target-architecture folders.
2. Preserve current `.github/skills/` compatibility content unless a minimal
   consistency repair is required for the two moved candidates.
3. Verify whether `.codex/skills` mappings or provenance need a bounded update
   to keep the two candidates readable after the move.
4. Write `docs/migration/codex-low-risk-skill-move.md` with:
   - candidate verdict
   - move result
   - Codex readability result
   - deferred boundaries and follow-up lanes

## Validation / Acceptance Checks

- Only the two locked candidates are moved into `skills/`.
- No same-name, medium-residue, high-residue, or blocker-bearing skill path is
  edited.
- Both candidates remain readable through `.codex/skills` after implementation.
- `.github/skills/` compatibility semantics remain intact and are not rewritten
  into repo-wide cutover claims.
- The migration report states what moved, what stayed deferred, and whether any
  minimal projection consistency update was required.

## Reviewer Handoff

```json
{
  "verdict": "approved|needs-rework",
  "blocking_issues": [],
  "copilot_feedback_triage": {
    "ADDRESS": [],
    "DISCUSS": [],
    "SKIP": []
  }
}
```

## Post-merge / release actions

- No automatic release action happens inside this topic branch before merge.
- If the topic merges, README / VERSION / tag handling is deferred to an
  explicit post-merge release step on `dev`, which is why this plan keeps the
  `merged` -> `released` transition.
- No repo-wide current-path governance change is part of this topic.

## Open Questions / Unresolved Items

- No unresolved candidate-selection question remains.
- The post-merge release actor should execute the already-locked patch bump and
  does not need to rediscover VERSION direction.
