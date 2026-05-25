# agent-skill-contract-surface-move

## Goal / Outcome

- Move these medium-residue contract surfaces into `skills/`:
  - `agent-skill-creator`
  - `agent-skill-reviewer`
  - `agent-skill-template`
- Preserve transition-era `.github/skills/` compatibility semantics while the
  move is implemented.
- Leave one repo-visible migration artifact that records move completion,
  preserved compatibility boundaries, and deferred follow-up work.

## Scope

- **In scope**:
  - `analysis/agent-skill-contract-surface-move/requirements.md`
  - `plan/agent-skill-contract-surface-move/agent-skill-contract-surface-move.plan.md`
  - `docs/migration/agent-skill-contract-surface-move.md`
  - `skills/agent-skill-creator/`
  - `skills/agent-skill-reviewer/`
  - `skills/agent-skill-template/`

- **Out of scope**:
  - `.github/skills/agent-skill-creator/`
  - `.github/skills/agent-skill-reviewer/`
  - `.github/skills/agent-skill-template/`
  - runtime/tooling blocker surfaces
  - planning-spine skill folders
  - `.codex/*`
  - `README.md`
  - `VERSION`
  - `AGENTS.md`
  - `docs/repo-positioning.md`
  - checklist-wide migration tracker updates

## Locked Decisions

- This topic implements only the three contract-surface candidates selected for
  the next bounded move batch.
- `skills/` receives new target-architecture copies for the three candidates.
- `.github/skills/` remains the transition-era compatibility surface and is not
  demoted or retired by this branch.
- `.codex/skills` routing, provenance, and shared governance artifacts remain
  untouched in this topic.
- README / VERSION / tag work is deferred until after merge and explicit human
  release handling.
- Base branch is `dev` because no verifiable
  `feat/andrew/copilot-to-codex-migration` branch exists locally or on the
  remote snapshot available during bootstrap.

## Boundaries / Exclusions

- Do not edit runtime/tooling blocker surfaces under this topic.
- Do not rewrite planning-spine dependencies in
  `business-intent-alignment` or `business-to-technical-translation`.
- Do not change `AGENTS.md`, `docs/repo-positioning.md`,
  `docs/migration/migration-runway-checklist.md`, `.codex/skills/README.md`, or
  `.codex/skills/provenance.md`.
- If the move requires editing any path outside `Artifact Paths`, stop and
  re-plan instead of improvising.

## Status / Allowed Transitions

- **Current**: `planned`
- **Execution model**: follow the canonical creator -> reviewer -> publish ->
  merge path; this topic implements branch-local move work first and does not
  execute a repository release action
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

- Branch target: `feat/andrew/agent-skill-contract-surface-move`
- Base branch: `dev`
- This topic must not be reclassified into runtime/tooling repair or repo-wide
  cutover without a new plan.
- `analysis/agent-skill-contract-surface-move/technical-spec.md` is
  intentionally absent; this plan is authored from the locked requirements
  baseline only.

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/agent-skill-contract-surface-move/agent-skill-contract-surface-move.plan.md` | Planning actor | Repo-visible execution contract |
| Requirements baseline | `analysis/agent-skill-contract-surface-move/requirements.md` | Planning actor | Locked candidate set, move rules, and stop conditions |
| Migration report | `docs/migration/agent-skill-contract-surface-move.md` | Creator | Repo-visible move result and deferred-boundary evidence |
| Target skill folder | `skills/agent-skill-creator/` | Creator | New target-architecture copy of the creator contract surface |
| Target skill folder | `skills/agent-skill-reviewer/` | Creator | New target-architecture copy of the reviewer contract surface |
| Target skill folder | `skills/agent-skill-template/` | Creator | New target-architecture copy of the template contract surface |
| Compatibility source | `.github/skills/agent-skill-creator/` | Existing repo artifact | Read-only transition-era source to copy from and preserve |
| Compatibility source | `.github/skills/agent-skill-reviewer/` | Existing repo artifact | Read-only transition-era source to copy from and preserve |
| Compatibility source | `.github/skills/agent-skill-template/` | Existing repo artifact | Read-only transition-era source to copy from and preserve |
| Medium-residue evidence | `docs/migration/codex-migration-copilot-residue-medium-report.md` | Existing repo artifact | Evidence for why these candidates belong to the next move batch |
| Runway checklist | `docs/migration/migration-runway-checklist.md` | Existing repo artifact | Read-only runway classification source |

Artifact path notes:

- This topic does not modify `.github/skills/*` compatibility sources.
- This topic does not modify `.codex/*`, `README.md`, `VERSION`,
  `.github/copilot-instructions.md`, `AGENTS.md`, `docs/repo-positioning.md`,
  or checklist-wide migration trackers.
- If execution requires editing any other path, stop and repair this plan
  before continuing.

## Implementation Steps

1. Copy the current transition-era source content from:
   - `.github/skills/agent-skill-creator/`
   - `.github/skills/agent-skill-reviewer/`
   - `.github/skills/agent-skill-template/`
   into new `skills/` target-architecture folders.
2. Preserve current `.github/skills/` compatibility content without edits.
3. Write `docs/migration/agent-skill-contract-surface-move.md` with:
   - candidate set
   - move result
   - preserved compatibility boundary
   - deferred follow-up lanes
4. Stop and re-plan if implementation requires changes to shared migration,
   projection, runtime/tooling, or governance surfaces.

## Validation / Acceptance Checks

- Only the three locked candidates are moved into `skills/`.
- No runtime/tooling blocker, planning-spine, or shared governance path is
  edited.
- `.github/skills/` compatibility semantics remain intact and are not rewritten
  into repo-wide cutover claims.
- The migration report states what moved, what stayed deferred, and which
  shared-file updates were intentionally excluded.

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
- `merged` is terminal for this topic.
- Shared metadata updates, projection switching, and repo-wide path governance
  changes require separate later topics.

## Open Questions / Unresolved Items

- None at topic-bootstrap time.
- If later implementation reveals that moving any of the three contract surfaces
  requires shared governance, projection, or runtime/tooling edits, stop and
  re-plan instead of widening this topic silently.
