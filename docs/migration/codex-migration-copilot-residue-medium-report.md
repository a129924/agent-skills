# codex-migration-copilot-residue-medium report

Branch: `feat/andrew/codex-migration-copilot-residue-medium`

Plan contract: `plan/codex-migration-copilot-residue-medium/codex-migration-copilot-residue-medium.plan.md`

## Summary

This branch remains inside the approved `B2. medium Copilot residue` contract.

- Candidate set matches the approved plan.
- No executable-path or generator coupling was found that would force reroute
  into a blocker-bearing branch.
- No repo-wide cutover semantics were changed.
- No creator/template path-transition remediation is applied in this branch;
  current active-path semantics remain unchanged by design.

## Candidate verdicts

Field semantics for this report:

- `migration status`: whether the candidate is migrated in this branch or
  remains a medium-residue, not-yet-migrated candidate
- `branch action`: what this branch actually did for that candidate

| candidate skill | verdict | migration status | branch action | why | blocker or residue note | follow-up branch or topic |
| --- | --- | --- | --- | --- | --- | --- |
| `.github/skills/agent-skill-creator/` | medium residue confirmed | not migrated in this branch; remains medium-residue candidate | branch-local correction only | The skill remains in the transition-era `.github/skills/` inventory, and this topic does not authorize changing the active authoring target. | This branch removes the premature `skills/<skill-name>/` authoring-target wording and keeps `.github/skills/<skill-name>/` as the current active workflow path. Separate creator/reviewer/template path transition remains downstream work. | Follow the dedicated `skill-authoring-path-transition` phase for creator/reviewer/template contract transition. |
| `.github/skills/agent-skill-reviewer/` | medium residue confirmed | not migrated in this branch; remains medium-residue candidate | classification only; no file change | The skill still encodes transition review semantics that distinguish canonical source from mirror/projection review. | Residue remains at workflow/contract level only. No executable-path or generator coupling found. Report state matches unchanged candidate state. | None required unless a later path-cutover topic changes canonical vs mirror review rules. |
| `.github/skills/agent-skill-template/` | medium residue confirmed | not migrated in this branch; remains medium-residue candidate | branch-local correction only | The template remains part of the transition inventory, and this topic does not authorize changing scaffold output paths. | This branch removes the premature `skills/<skill-name>/` scaffold wording and keeps `.github/skills/<skill-name>/` as the current active template target. Separate creator/reviewer/template path transition remains downstream work. | Follow the dedicated `skill-authoring-path-transition` phase for creator/reviewer/template contract transition. |
| `.github/skills/worktree-manager/` | medium residue confirmed | not migrated in this branch; remains medium-residue candidate | classification only; no file change | The skill is migratable, but still carries transition-sensitive workflow/governance semantics around shared planning files, managed-path policy, and destructive routing. | Residue remains bounded to workflow/contract guidance. No executable-path or generator coupling found in this branch review. Report state matches unchanged candidate state. | Reclassify only if later evidence shows mandatory runtime/tooling repair or path-coupled execution behavior. |

## Branch-local corrections applied

- Reverted premature creator wording that changed the active authoring target
  from `.github/skills/<skill-name>/` to `skills/<skill-name>/`.
- Reverted premature template scaffold wording that changed the active starter
  path from `.github/skills/<skill-name>/` to `skills/<skill-name>/`.
- Kept migration-status reporting separate from branch-local corrective action so
  the report reflects frozen positioning accurately.

## Not changed

- `.github/skills/agent-skill-reviewer/` content was not changed because the
  reviewed residue is contract-level and did not require bounded repair here.
- `.github/skills/worktree-manager/` content was not changed because no
  blocker-bearing executable or generator coupling was found.
- These unchanged candidates remain classified as medium residue; this branch
  executed no file-level remediation for them.
- Creator/reviewer/template path transition remains a separate downstream phase;
  this branch does not claim that follow-up is unnecessary.
- No runtime/tooling repair was attempted.
- No README, VERSION, or repo-wide path semantics were changed.

## Contract status

- Reclassification discovered: none
- Blocker discovered: none
- Branch still inside approved contract: yes
