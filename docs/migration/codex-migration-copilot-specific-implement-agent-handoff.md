# codex-migration-copilot-specific Implement Agent Handoff

## Branch

- `feat/andrew/codex-migration-copilot-specific`

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
        "comment": "When producing the branch report, keep `reference-only` and `do-not-migrate` conclusions structurally distinct rather than folding them into one generic rejection bucket.",
        "optional": true,
        "why": "The plan already requires the split; keeping the report structure explicit will make later portfolio decisions easier."
      }
    ],
    "SKIP": []
  }
}
```

## Exact candidate set

- `.github/skills/copilot-instructions-init/`

## Repo-visible blocker note

- `docs/migration/migration-runway-checklist.md` currently classifies
  `.github/skills/copilot-instructions-init/` as a `confirmed-blocker`
  runtime/tooling surface.
- This branch is allowed to report that blocker status and classify the skill as
  `reference-only` or `do-not-migrate`.
- This branch is not allowed to repair the blocker or force migration.

## Required reading order

1. `plan/agent-handoff-workflow.md`
2. `docs/migration/plan-review-protocol.md`
3. `docs/migration/codex-skills-spec-worktree.md`
4. `analysis/codex-migration-copilot-specific/requirements.md`
5. `plan/codex-migration-copilot-specific/codex-migration-copilot-specific.plan.md`
6. this handoff file

## Allowed output path

- `docs/migration/codex-migration-copilot-specific-report.md`

## Branch-specific rules

- every final conclusion must remain either `reference-only` or `do-not-migrate`
- confirmed-blocker status must be reported explicitly when supported by the
  repo-visible evidence set
- do not force migration unless explicit branch-local reclassification occurs
- do not execute runtime/tooling blocker repair from this branch

## Required final return

1. what changed
2. what did not change
3. report path updated
4. any blocker or reclassification discovered
5. whether the branch still stays inside its approved contract
