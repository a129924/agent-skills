# codex-migration-copilot-residue-high Implement Agent Handoff

## Branch

- `feat/andrew/codex-migration-copilot-residue-high`

## Required worktree path

- `/Users/andrew/code/python/agent-skills.worktrees/agent-20260516-codex-migration-copilot-residue-high`

## Worktree rules

- Treat the required worktree path above as the only valid execution root for this handoff.
- If the current workspace path does not match it, stop and report path mismatch instead of continuing.
- Resolve all repo-relative paths from this worktree root only.

## Current plan-review status

- Topic-plan review status: `approved`
- Requirements baseline status: `FROZEN-FOR-IMPLEMENTATION`

## Approval routing note

- The topic plan is already approved as a repo-visible execution contract.
- That approval does not mean the topic is complete.
- The only authorized post-approval execution in this branch is creator-side
  production or update of
  `docs/migration/codex-migration-copilot-residue-high-report.md`.
- The topic reaches its own stop point only after that report artifact is
  reviewed and the topic returns `approved`.

## Formal review JSON

```json
{
  "verdict": "approved",
  "blocking_issues": [],
  "copilot_feedback_triage": {
    "ADDRESS": [],
    "DISCUSS": [
      {
        "comment": "Preserve the option to reclassify `git-post-merge-workflow` as Copilot-specific or blocker-adjacent if redesign evidence weakens during execution.",
        "optional": true,
        "why": "The current plan is contract-safe, but this branch depends on honest reclassification if the redesign path stops being credible."
      }
    ],
    "SKIP": []
  }
}
```

## Exact candidate set

- `.github/skills/git-post-merge-workflow/`

## Required reading order

1. `plan/agent-handoff-workflow.md`
2. `docs/migration/plan-review-protocol.md`
3. `docs/migration/codex-skills-spec-worktree.md`
4. `analysis/codex-migration-copilot-residue-high/requirements.md`
5. `plan/codex-migration-copilot-residue-high/codex-migration-copilot-residue-high.plan.md`
6. this handoff file

## Allowed output path

- `docs/migration/codex-migration-copilot-residue-high-report.md`

## Required report contents

The report must clearly state:

- candidate skill
- verdict: `redesign`, `defer`, or `reclassify`
- migration action in this branch: `none`
- future move recommended: `yes` or `no`
- why
- blocker or residue note when applicable
- follow-up branch or topic if required

## Branch-specific rules

- execution mode is report-first and classification-only
- treat `.github/skills/git-post-merge-workflow/` as read/verify scope, not an
  authorized modification target in this branch
- final branch-local verdict must be one of:
  - `redesign`
  - `defer`
  - `reclassify`
- if the redesign path becomes non-credible, stop and report for reclassification
- if the current cwd/worktree root does not match the required worktree path, stop and report path mismatch
- do not treat topic-plan approval as authorization for publish, merge, or
  candidate-skill modification

## Frozen reclassification triggers

Treat redesign as non-credible and stop for reclassification when any of the
following becomes true:

- runtime/tooling blocker repair would be required
- the skill is better described as Copilot-specific-only or reference-only
- a bounded redesign objective cannot be stated from repo-visible evidence alone
- execution would require editing files outside
  `docs/migration/codex-migration-copilot-residue-high-report.md`
- execution would change repo-wide cutover semantics

## Required final return

1. what changed
2. what did not change
3. report path updated
4. any blocker or reclassification discovered
5. whether the branch still stays inside its approved contract
