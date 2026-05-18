# codex-migration-copilot-residue-low Implement Agent Handoff

## Branch

- `feat/andrew/codex-migration-copilot-residue-low`

## Required worktree path

- `/Users/andrew/code/python/agent-skills.worktrees/agent-20260516-codex-migration-copilot-residue-low`

## Worktree rules

- Treat the required worktree path above as the only valid execution root for this handoff.
- If the current workspace path does not match it, stop and report path mismatch instead of continuing.
- Resolve all repo-relative paths from this worktree root only.

## Current plan-review status

- Round 1 formal review verdict: `approved`

## Formal review JSON

```json
{
  "verdict": "approved",
  "blocking_issues": [],
  "copilot_feedback_triage": {
    "ADDRESS": [],
    "DISCUSS": [
      {
        "comment": "Keep remediation strictly limited to wording, examples, projection notes, and local path cleanup; reclassify immediately if workflow semantics start to shift.",
        "optional": true,
        "why": "This branch is valid as written, but low-residue work can drift into medium-residue changes if not watched closely."
      }
    ],
    "SKIP": []
  }
}
```

## Exact candidate set

- `.github/skills/git-commit-convention/`
- `.github/skills/git-branch-naming/`

## Required reading order

1. `plan/agent-handoff-workflow.md`
2. `docs/migration/plan-review-protocol.md`
3. `docs/migration/codex-skills-spec-worktree.md`
4. `analysis/codex-migration-copilot-residue-low/requirements.md`
5. `plan/codex-migration-copilot-residue-low/codex-migration-copilot-residue-low.plan.md`
6. this handoff file

## Allowed output path

- `docs/migration/codex-migration-copilot-residue-low-report.md`

## Branch-specific rules

- remediation is limited to wording, examples, projection notes, and local path cleanup
- if workflow or contract redesign appears, stop and report for reclassification
- if the current cwd/worktree root does not match the required worktree path, stop and report path mismatch

## Required final return

1. what changed
2. what did not change
3. report path updated
4. any blocker or reclassification discovered
5. whether the branch still stays inside its approved contract
