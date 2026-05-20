# `agent-skills` Merge-to-`dev` Freeze Checklist

## Summary

This checklist answers one question only:

- should `feat/andrew/codex-skills-spec-worktree` merge back into `dev`
- and, if merged, is `agent-skills` ready to operate as a single-line
  Codex-takeover repository rather than a dual Copilot/Codex migration surface

This is not a release checklist.
This is not an `mlops-async` integration checklist.
This is not proof that runtime/tooling blockers are complete.

As of `2026-05-20`, the known live worktrees are:

- `dev` at `/Users/andrew/code/python/agent-skills`
- `feat/andrew/codex-skills-spec-worktree` at
  `/Users/andrew/code/python/agent-skills.worktrees/agent-20260516-codex-skills-spec-worktree`

## Checklist

### A. Branch Convergence

- [x] `feat/andrew/codex-skills-spec-worktree` contains the retained results from
      the 5 codex migration branches
- [x] the repository no longer depends on other parallel worktree branches as
      primary migration evidence sources
- [ ] after merge, `feat/andrew/codex-skills-spec-worktree` will no longer be
      treated as a long-lived second mainline
- [ ] after merge, the worktree branch will be deleted or explicitly downgraded
      to historical snapshot use only

### B. Artifact Acceptance Scope

- [x] `.codex/skills/` is accepted as a validation / projection surface
- [x] `docs/migration/codex-skills-spec-worktree.md` is accepted as validation
      history, not a new canonical workflow
- [x] `docs/migration/plan-review-protocol.md` is accepted as a reusable review
      protocol
- [x] the 5 migration `plan` / `report` / `handoff` artifact sets are accepted
      as evidence artifacts, not as a second permanent execution system
- [ ] the `README.md` changes are explicitly accepted as part of the freeze
      snapshot narrative
- [ ] the `VERSION` bump carried by the worktree branch is explicitly accepted as
      part of the merge snapshot

### C. Known Exceptions That Do Not Block Merge

- [x] `mlops-async` is treated as a transition exception and does not block
      `agent-skills` merge-to-`dev`
- [x] runtime/tooling blockers remain future topics and do not need to be solved
      before this merge
- [x] temporary survival of `.github/skills/` is not itself a merge blocker
- [x] merging `.codex/skills/` into `dev` does not by itself mean active-path
      cutover is complete

### D. Post-merge Operating Model

- [ ] after merge, new changes no longer use `.github/skills/` as the default
      primary write surface
- [ ] same-name skills are no longer allowed to evolve independently in both
      `skills/` and `.github/skills/`
- [ ] `skills/` is accepted as the only future source-of-truth direction
- [ ] `.github/skills/` is accepted as compatibility / projection / residual
      maintenance surface rather than long-term co-equal source
- [ ] `.codex/skills/` is prevented from becoming a third long-lived mainline

### E. Immediate Post-merge Actions

- [ ] merge is followed by a freeze / takeover governance document
- [ ] no new parallel spec line is opened after merge
- [ ] the next topic is explicitly one of:
  - canonical-authority freeze
  - runtime/tooling blocker baseline
- [x] `mlops-async` remains a month-end cleanup topic only and does not reverse
      the `agent-skills` operating-model decision

## Self-check

### Passed

- [x] A1
- [x] A2
- [x] B1
- [x] B2
- [x] B3
- [x] B4
- [x] C1
- [x] C2
- [x] C3
- [x] C4
- [x] E4

### Pending explicit human acceptance before merge

- [ ] A3
- [ ] A4
- [ ] B5
- [ ] B6
- [ ] D1
- [ ] D2
- [ ] D3
- [ ] D4
- [ ] D5
- [ ] E1
- [ ] E2
- [ ] E3

### Not a current hard blocker

- [x] no new hard blocker was discovered during this check
- [x] the remaining gap is operating-model acceptance, not missing migration
      evidence

## Merge Decision Rule

`feat/andrew/codex-skills-spec-worktree` is ready to merge into `dev` once the
following are explicitly accepted:

1. the branch will not remain a second long-lived mainline after merge
2. `skills/` is the only future source-of-truth direction, while
   `.github/skills/` keeps only compatibility / projection / residual duties
3. `mlops-async` is a month-end transition exception and does not delay
   `agent-skills` convergence

## Observed Diff Scope

The current worktree branch carries these merge-relevant artifact groups:

- `.codex/skills/` validation / projection surface
- migration protocol docs:
  - `docs/migration/codex-skills-spec-worktree.md`
  - `docs/migration/plan-review-protocol.md`
  - `docs/migration/implement-agent-prompt-pack.md`
- 5 migration branch artifact sets:
  - `analysis/codex-migration-*`
  - `plan/codex-migration-*`
  - `docs/migration/codex-migration-*`
- small bounded remediation in:
  - `.github/skills/agent-skill-creator/SKILL.md`
  - `.github/skills/agent-skill-template/template.md`
  - `.github/skills/git-branch-naming/SKILL.md`
  - `.github/skills/git-branch-naming/references/naming-patterns.md`
- freeze snapshot updates:
  - `README.md`
  - `VERSION`

## Assumptions

- Date baseline: `2026-05-20`
- `mlops-async` is expected to finish its Copilot-era cleanup before
  `2026-05-31`
- this merge is for single-line convergence, not runtime/tooling completion
- merge acceptance does not by itself authorize immediate deletion of
  `.github/skills/`; that remains follow-up work
