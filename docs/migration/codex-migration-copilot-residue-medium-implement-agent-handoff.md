# codex-migration-copilot-residue-medium Implement Agent Handoff

## Branch

- `feat/andrew/codex-migration-copilot-residue-medium`

## Required worktree path

- `/Users/andrew/code/python/agent-skills.worktrees/agent-20260516-codex-migration-copilot-residue-medium`

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
        "comment": "If any candidate reveals executable-path or generator coupling during implementation, stop and reroute it instead of absorbing it into medium-residue work.",
        "optional": true,
        "why": "The current branch boundary is coherent, but medium-residue candidates are the most likely to expose hidden blocker behavior."
      }
    ],
    "SKIP": []
  }
}
```

## Exact candidate set

- `.github/skills/agent-skill-creator/`
- `.github/skills/agent-skill-reviewer/`
- `.github/skills/agent-skill-template/`
- `.github/skills/worktree-manager/`

## Required reading order

1. `plan/agent-handoff-workflow.md`
2. `docs/migration/plan-review-protocol.md`
3. `docs/migration/codex-skills-spec-worktree.md`
4. `analysis/codex-migration-copilot-residue-medium/requirements.md`
5. `plan/codex-migration-copilot-residue-medium/codex-migration-copilot-residue-medium.plan.md`
6. this handoff file

## Allowed output path

- `docs/migration/codex-migration-copilot-residue-medium-report.md`

## Branch-specific rules

- bounded workflow and contract remediation is allowed
- runtime/tooling blocker repair is not allowed
- if executable-path or generator coupling appears, stop and reroute
- if the current cwd/worktree root does not match the required worktree path, stop and report path mismatch

## Required final return

1. what changed
2. what did not change
3. report path updated
4. any blocker or reclassification discovered
5. whether the branch still stays inside its approved contract
