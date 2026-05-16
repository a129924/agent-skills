# codex-migration-copilot-residue-high Implement Agent Handoff

## Branch

- `feat/andrew/codex-migration-copilot-residue-high`

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

## Branch-specific rules

- redesign-oriented work is allowed only inside the single locked candidate
- if the redesign path becomes non-credible, stop and report for reclassification

## Required final return

1. what changed
2. what did not change
3. report path updated
4. any blocker or reclassification discovered
5. whether the branch still stays inside its approved contract
