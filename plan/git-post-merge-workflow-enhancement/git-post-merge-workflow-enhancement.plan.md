---
name: git-post-merge-workflow-enhancement
status: planned
---

# Git Post-Merge Workflow Enhancement

## Goal / Outcome

- `git-post-merge-workflow` becomes self-contained for STOP POINT 2 resume behavior instead of relying on repository-global instructions for its core checklist.
- `.github/skills/git-post-merge-workflow/SKILL.md` explicitly defines when post-merge execution may begin and what boundaries still apply.
- `.github/skills/git-post-merge-workflow/references/stop-point-2-checklist.md` exists as a portable local reference for merge-confirmation and local-sync checks.
- `.github/copilot-instructions.md` is simplified so it points to the skill-local checklist instead of carrying the full operational detail.
- The updated skill passes independent `agent-skill-reviewer` review with `approved`.

## Scope

- **In scope**:
  - `.github/skills/git-post-merge-workflow/SKILL.md` — clarify STOP POINT 2 entry conditions, execution boundary, and local references
  - `.github/skills/git-post-merge-workflow/references/stop-point-2-checklist.md` — new portable checklist for post-merge resume validation
  - `.github/copilot-instructions.md` — replace detailed STOP POINT 2 checklist prose with a concise reference to the skill-local checklist
  - `plan/git-post-merge-workflow-enhancement/git-post-merge-workflow-enhancement.plan.md` — execution contract for this topic

- **Out of scope**:
  - changing `plan/agent-handoff-workflow.md`
  - changing `workflow-gate.agent.md`
  - changing `git-release-management` or other post-merge / release skills
  - changing `README.md`
  - changing `VERSION`
  - adding release automation, merge polling, or nonlocal workflow helpers

## Locked Decisions

1. **This is not a stable-library promotion topic**:
   - The topic enhances an existing stable skill.
   - `README.md` and `VERSION` do not change in this topic.
   - No `## Stable library metadata` section applies.

2. **STOP POINT 2 checklist moves into the skill folder**:
   - The checklist belongs to `.github/skills/git-post-merge-workflow/`, not to repository-global instructions.
   - The checklist must be portable and remain useful when the skill is copied to another repository.

3. **Role ownership remains explicit**:
   - Creator updates the skill folder only.
   - Reviewer independently evaluates the updated skill folder.
   - Main Agent performs planner alignment, publish routing, and the `.github/copilot-instructions.md` simplification after reviewer approval.

4. **No release action exists for this topic**:
   - The workflow ends at `merged`.
   - There is no `merged` -> `released` transition for this topic.

## Boundaries / Exclusions

- Do not broaden this topic into a generic workflow-gate refactor.
- Do not move STOP POINT 1 or STOP POINT 2 semantics out of `plan/agent-handoff-workflow.md`; this topic only improves one skill's local self-containment.
- Do not change adjacent skills just because they reference merge timing.
- Do not let creator self-approve or let reviewer author the final implementation directly.
- Do not modify files outside the exact paths listed under `Artifact Paths` unless the plan is revised first.

## Status / Allowed Transitions

- **Current**: `planned`
- **Execution model**: standard creator -> reviewer -> publish -> merge path per `plan/agent-handoff-workflow.md`; this topic stops at `merged` and has no release phase
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
  - `merged` -> terminal

- **Routing notes**:
  - Use the standard Phase 4.5 planner-contract-alignment rule before publish.
  - Creator implementation stays inside the skill folder paths listed below.
  - `.github/copilot-instructions.md` changes are Main Agent publish work after reviewer approval, not creator work.
  - STOP POINT 1 still blocks commit / push / PR creation until explicit human approval.
  - STOP POINT 2 still requires an explicit human resume after merge confirmation; the topic only relocates the checklist detail into the skill.

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/git-post-merge-workflow-enhancement/git-post-merge-workflow-enhancement.plan.md` | Planning actor | Repo-visible execution contract for this topic |
| Skill contract | `.github/skills/git-post-merge-workflow/SKILL.md` | Creator | Define trigger, boundaries, and STOP POINT 2 entry conditions in the skill itself |
| STOP POINT 2 checklist reference | `.github/skills/git-post-merge-workflow/references/stop-point-2-checklist.md` | Creator | Portable local reference for merge confirmation, local sync, and branch cleanup checks |
| Global instruction simplification | `.github/copilot-instructions.md` | Main Agent | Replace detailed STOP POINT 2 checklist prose with a concise pointer to the skill-local reference |

Artifact path notes:

- This topic modifies `.github/copilot-instructions.md`.
- This topic does **not** modify `README.md`.
- This topic does **not** modify `VERSION`.
- Treat the listed paths as an executable contract; if later work appears outside them, stop and revise the topic plan before continuing.

## Implementation Steps

1. **Plan review**
   - Review this topic plan against `plan/agent-handoff-workflow.md` and the plan-creator contract sources.
   - Repair any contract-breaking ambiguity before creator work begins.

2. **Creator implementation**
   - Use `agent-skill-creator` to revise `.github/skills/git-post-merge-workflow/SKILL.md` so the skill explicitly states:
     - when post-merge work may start
     - what must already be true before the skill is triggered
     - what remains out of scope for the skill
   - Create `.github/skills/git-post-merge-workflow/references/stop-point-2-checklist.md` with the concrete STOP POINT 2 resume checks, including merge confirmation, local sync expectations, and branch cleanup checks.
   - Update `Local references` in `SKILL.md` so the new checklist file has an explicit declared role.
   - Stop when the skill folder is `review-ready`.

3. **Independent reviewer pass**
   - Use `agent-skill-reviewer` to evaluate the updated skill folder.
   - If the reviewer returns `needs-rework`, route back to creator and iterate until the skill returns `approved`.

4. **Planner alignment and publish**
   - After reviewer approval, Main Agent confirms the final work still matches this topic plan.
   - Main Agent updates `.github/copilot-instructions.md` to point to the skill-local STOP POINT 2 checklist instead of carrying the detailed checklist itself.
   - Main Agent prepares the exact listed paths only for commit / push / PR flow.

## Validation / Acceptance Checks

1. `agent-skill-reviewer` returns `approved` for the updated `.github/skills/git-post-merge-workflow/` folder.
2. `.github/skills/git-post-merge-workflow/SKILL.md` contains explicit trigger timing and boundary language for post-merge execution.
3. `.github/skills/git-post-merge-workflow/references/stop-point-2-checklist.md` exists and has a clearly declared role in `SKILL.md`.
4. The STOP POINT 2 checklist is understandable without relying on `.github/copilot-instructions.md`.
5. `.github/copilot-instructions.md` no longer carries the detailed STOP POINT 2 checklist and instead points to the skill-local reference.
6. No changes land outside the exact `Artifact Paths` listed above.
7. Reviewer handoff remains machine-consumable JSON only.

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

- After merge, Main Agent may run the normal post-merge local sync flow only after an explicit human resume message confirms merge completion.
- No repository release action exists for this topic.
- The topic reaches terminal state at `merged`.

## Open Questions / Unresolved Items

- None.
