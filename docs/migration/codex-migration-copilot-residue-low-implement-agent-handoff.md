# codex-migration-copilot-residue-low Implement Agent Handoff

> Historical evidence only: this handoff records the branch-local execution
> contract used during the migration lane. The branch worktree named below was
> retired after merge-back and is not a current `dev` execution requirement.

## Branch

- `feat/andrew/codex-migration-copilot-residue-low`

## Historical worktree path

- `/Users/andrew/code/python/agent-skills.worktrees/agent-20260516-codex-migration-copilot-residue-low`

## Worktree rules

- Treat the worktree path above as historical evidence for the original branch-local execution root.
- Do not assume this path still exists on `dev`.
- If this handoff is ever reused, replace the retired worktree path with a live branch or repo-root instruction first.

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
- treat the historical worktree path above as branch-local evidence only
- do not assume that path still exists on `dev`
- if this handoff is reused, replace the retired worktree path with a live branch or repo-root instruction before execution

## Required final return

1. what changed
2. what did not change
3. report path updated
4. any blocker or reclassification discovered
5. whether the branch still stays inside its approved contract
