# python-testing-pytest schema v2 migration

**Semantic warning**: `analysis/python-testing-pytest/requirements.md` and `analysis/python-testing-pytest/technical-spec.md` are both absent. This plan is authored without the optional analysis layer and uses the current repo-visible skill files plus migration-tracker state as the planning baseline.

## Goal / Outcome

- Upgrade `.github/skills/python-testing-pytest/` from the legacy skill shape to the current schema v2 contract.
- Preserve the skill's existing responsibility: pure Python pytest unit-testing guidance for fixtures, parametrization, assertions, mocks, and no-real-I/O boundaries.
- Reach reviewer-approved status for this deferred skill so the migration tracker can move from `44/45` to `45/45`.

## Scope

- **In scope**:
  - `.github/skills/python-testing-pytest/SKILL.md`
  - `.github/skills/python-testing-pytest/examples.md`
  - `files/migration-tracker.md`
  - `plan/python-testing-pytest/python-testing-pytest.plan.md`

- **Out of scope**:
  - `README.md`
  - `VERSION`
  - git tag creation or changes
  - any skill other than `python-testing-pytest`
  - governance files such as `agent-skill-creator`, `agent-skill-reviewer`, `agent-skill-template`, `folder-contract.md`, or `blueprint.md`
  - the final integration PR from `feature/skill-migration-v1` to `dev`

## Locked Decisions

- This topic is a **stable-library-affecting topic with deferred release timing**.
- The migration mode starts as **Mode A+**: preserve the current skill contract and supplement only the missing schema v2 structure.
- Expected inference baseline:
  - `python-testing-pytest` should be evaluated as a **medium-complexity** helper/reference skill unless creator finds concrete evidence that a different classification is required.
  - The skill's pure-unit-testing, no-real-I/O boundary must remain unchanged.
  - `examples.md` remains a local companion file; update it only if schema v2 alignment or reviewer feedback makes that necessary.
- Rewrite mode (Mode B) is allowed only if creator produces a Preservation Map first and the human explicitly accepts the rewrite risk.
- `files/migration-tracker.md` is updated in this topic after reviewer approval so the integration branch reflects the true `45/45` completion state before the final integration PR.
- `README.md`, `VERSION`, and release/tag actions remain deferred to the later final integration PR topic.

## Boundaries / Exclusions

- Creator owns only the skill-folder draft within the listed artifact paths and must not self-approve.
- Reviewer owns only the independent verdict and must not author the final implementation directly.
- Main Agent owns tracker update, commit/push/PR handling, and stop-point routing after reviewer approval.
- Do not broaden this topic into README polish, release management, or any other deferred skill cleanup.
- If work appears to require files outside the listed artifact paths, stop and repair the plan before continuing.

## Status / Allowed Transitions

- **Current**: `planned`
- **Execution model**: plan-reviewer -> creator -> reviewer -> publish -> merge; this topic stops at `merged` and does not perform repository release actions.
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

Routing notes:

- Before creator work begins, this topic plan itself must be sent to `plan-reviewer`.
- Use the standard Phase 4.5 planner-alignment rule: after reviewer approval of the skill draft, ensure all changed files still match the plan's exact artifact paths before publish.
- STOP POINT 1 applies before commit / push / PR creation.
- STOP POINT 2 applies after merge handoff; no polling or implicit resume is allowed.

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/python-testing-pytest/python-testing-pytest.plan.md` | Planning actor | Repo-visible execution contract for this deferred migration topic |
| Skill contract | `.github/skills/python-testing-pytest/SKILL.md` | Creator | Primary schema v2 upgrade target |
| Local examples | `.github/skills/python-testing-pytest/examples.md` | Creator | Companion examples file; update only if needed for schema v2 alignment or reviewer-requested clarity |
| Migration tracker | `files/migration-tracker.md` | Main Agent | Records the topic as complete and moves aggregate progress to `45/45` after reviewer approval |

Artifact path notes:

- This topic does **not** modify `README.md`, `VERSION`, or `.github/copilot-instructions.md`.
- If creator or reviewer concludes that additional files are needed, stop and repair this plan instead of silently widening scope.

## Stable library metadata

- `README row`: no change in this topic; the existing `python-testing-pytest` row already exists in `README.md`, and final migration-summary edits stay deferred to the later final integration PR
- `VERSION bump`: no bump in this topic
- `timing`: deferred
- `rationale`: keep this branch tightly scoped to the deferred skill migration plus tracker truth update, while leaving release-surface consolidation to the final integration PR after this topic merges

## Implementation Steps

1. Prepare and use a dedicated clean worktree/branch for this topic in this repository on `migrate/python-testing-pytest-schema-v2`.
2. Send `plan/python-testing-pytest/python-testing-pytest.plan.md` to `/fleet @.github/skills/plan-reviewer/` and do not start creator work until the plan is accepted or repaired.
3. Send the approved plan plus current skill folder to `/fleet @.github/skills/agent-skill-creator/`:
   - preserve existing purpose, trigger, process, outputs, boundaries, and local-file roles
   - add schema v2 YAML metadata and any complexity-gated sections required by the inferred complexity/risk
   - keep the skill self-contained and copy-friendly
4. Send the creator result to `/fleet @.github/skills/agent-skill-reviewer/` for an independent verdict.
5. If reviewer returns `needs-rework`, route fixes back to creator and repeat step 4 until verdict is `approved`.
6. After approval, update `files/migration-tracker.md`:
   - mark `python-testing-pytest` as done
   - change Tier 2 to `5 / 5`
   - change Total to `45 / 45`
   - remove the deferred wording
7. At STOP POINT 1, wait for explicit human approval before commit, push, and PR creation to `feature/skill-migration-v1`.

## Validation / Acceptance Checks

- The topic plan stays within the exact artifact paths listed above.
- `plan-reviewer` returns a machine-consumable pass path for the topic plan before creator work proceeds.
- The upgraded `SKILL.md` includes schema v2 metadata aligned with its body content.
- Positive and negative examples remain present and the skill stays explicit about no-real-I/O boundaries.
- Any added `Validation`, `Failure Handling`, or `Workflow State Contract` sections must match the inferred complexity/risk rather than being copied mechanically.
- `agent-skill-reviewer` returns `approved`.
- `files/migration-tracker.md` truthfully reflects `45/45 complete` only after reviewer approval for this skill.
- No changes appear in `README.md`, `VERSION`, governance files, or unrelated skill folders.

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

- After merge to `feature/skill-migration-v1`, Main Agent may perform the normal post-merge branch cleanup and local sync.
- No repository release action occurs in this topic.
- The later final integration PR owns `README.md`, `VERSION`, and any release/tag narrative consolidation.

## Open Questions / Unresolved Items

- None for planning. If creator finds evidence that `python-testing-pytest` cannot stay in Mode A+ without guesswork, stop and return a Preservation Map for explicit human review before rewriting.
