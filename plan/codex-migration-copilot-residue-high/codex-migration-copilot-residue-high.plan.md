# codex-migration-copilot-residue-high

## Goal / Outcome

- Freeze the high-residue candidate set.
- Produce a branch-local report for high Copilot-residue skills.
- Freeze redesign-oriented classification and reclassification boundaries from
  repo-visible evidence.
- Do not execute branch-local candidate-skill modification from this topic.

## Scope

- **In scope**:
  - `analysis/codex-migration-copilot-residue-high/requirements.md`
  - `plan/codex-migration-copilot-residue-high/codex-migration-copilot-residue-high.plan.md`
  - `docs/migration/codex-migration-copilot-residue-high-report.md`
  - `.github/skills/git-post-merge-workflow/`

- **Out of scope**:
  - direct-move and low/medium residue skills
  - Copilot-specific-only skills
  - runtime/tooling blocker repair
  - repo-wide cutover

## Locked Decisions

- This branch handles only class `B3. high Copilot residue`.
- The candidate set is locked to:
  - `.github/skills/git-post-merge-workflow/`
- The branch may analyze redesign paths but must not hide Copilot-specific-only
  conclusions.
- Runtime/tooling blocker repair remains out of scope.
- Execution mode for this topic is report-first and classification-only.
- Implementation in this topic means report production, not candidate-skill
  modification.
- Each skill must end with a branch-local `redesign`, `defer`, or `reclassify`
  verdict plus explicit reasons.
- This topic is review-ready-only with no stable-library release action.

## Boundaries / Exclusions

- Do not convert high-residue analysis into repo-wide cutover work.
- Do not absorb runtime/tooling transition work here.
- Do not force Copilot-specific skills into migration if evidence says
  reference-only or no-migrate.
- Do not edit `.github/skills/git-post-merge-workflow/` from this branch.

## Status / Allowed Transitions

- **Current**: `planned`
- **Execution model**: follow the canonical creator -> reviewer -> publish ->
  merge path for contract compatibility, but active execution for this topic
  stops at `approved`
- **Plan-vs-topic note**: approval of this topic plan authorizes creator-side
  production of the branch-local report artifact. The topic itself reaches its
  stop point only when that report artifact is reviewed and the topic returns
  `approved`.
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

- Branch target: `feat/andrew/codex-migration-copilot-residue-high`
- Base branch: `feat/andrew/codex-skills-spec-worktree`
- Active execution stop point: `approved`
- The stop point refers to approval of the branch-local report artifact under
  this topic, not merely approval of the topic plan contract itself.
- `publish-in-progress`, `pr-open`, and `merged` remain listed only for
  canonical contract compatibility; they are not exercised in this topic

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/codex-migration-copilot-residue-high/codex-migration-copilot-residue-high.plan.md` | Planning actor | Repo-visible execution contract for this branch topic |
| Requirements baseline | `analysis/codex-migration-copilot-residue-high/requirements.md` | Planning actor | Branch-local classification baseline |
| Migration report | `docs/migration/codex-migration-copilot-residue-high-report.md` | Implement Agent | Skill verdicts, redesign paths, and follow-up items |
| High-residue skill | `.github/skills/git-post-merge-workflow/` | Implement Agent | Allowed read/verify candidate path for high-residue classification only |

Artifact path notes:

- This topic does not require `VERSION` changes.
- This topic does not require `README.md` changes before the candidate set is frozen.
- The candidate skill path is read/verify scope only.
- No branch-local candidate-skill modification is authorized by this plan.

## Implementation Steps

1. Collect candidate skills that fit the high-residue class.
2. Evaluate whether a credible redesign path can be described from repo-visible
   evidence alone without widening scope.
3. Freeze `redesign`, `defer`, or `reclassify` verdicts for each skill.
4. Produce the branch-local report with explicit redesign boundaries and
   reclassification triggers.
5. Stop at report-ready / approved output; do not modify the candidate skill in
   this branch.

## Validation / Acceptance Checks

- Every skill has a high-residue rationale.
- Copilot-specific-only skills are not forced through redesign.
- Blocker interactions are visible in the report.
- The report states whether redesign remains credible or must be reclassified.
- No branch-local candidate-skill modification is performed.

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

- No repository release action is part of this topic.
- No post-merge action is expected inside this topic because active execution
  stops at `approved`.

## Open Questions / Unresolved Items

- A redesign path is non-credible and must trigger reclassification when any of
  the following becomes true:
  - runtime/tooling blocker repair would be required
  - the skill is better described as Copilot-specific-only or reference-only
  - a bounded redesign objective cannot be stated from repo-visible evidence
    alone
  - executing the redesign would require editing files outside the locked report
    path or changing repo-wide cutover semantics
