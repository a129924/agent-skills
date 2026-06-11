# Codex Skills Canonical Retarget Plan

Analysis-layer routing: **incomplete layer**.

Semantic warning:

- `analysis/codex-skills-canonical-retarget/requirements.md` is absent.
- `analysis/codex-skills-canonical-retarget/technical-spec.md` is absent.
- This plan is authored from locked human decisions plus repo-visible contract
  sources only.
- The missing optional analysis layer does not authorize scope widening.

## Goal / Outcome

- Replace the first-wave `.codex/skills/*` compatibility surface for 11 named
  skills with `.codex`-local materialized directories copied from canonical
  `skills/<skill-name>/`.
- Concretize any copied `.<platform>/skills/...` references inside those
  materialized `.codex/skills/**` files to `.codex/skills/...` only within the
  `.codex` surface.
- Align `.codex/skills/README.md` and `.codex/skills/provenance.md` to the
  materialized-copy model, canonical upstream mapping, and validation basis.

When this topic is complete:

- the 11 selected `.codex/skills/*` entries are directories, not symlinks
- their copied content originates from same-name `skills/*` canonical sources
- `.codex/skills/README.md` and `.codex/skills/provenance.md` describe those
  entries as `.codex`-local `materialized-copy` surfaces
- `skills/**` and `.github/skills/**` remain unchanged

## Scope

- **In scope**:
  - `plan/codex-skills-canonical-retarget/codex-skills-canonical-retarget.plan.md`
  - `plan/codex-skills-canonical-retarget/codex-skills-canonical-retarget.step.md`
  - `plan/codex-skills-canonical-retarget/codex-skills-canonical-retarget.review-log.md`
  - `.codex/skills/README.md`
  - `.codex/skills/provenance.md`
  - `.codex/skills/business-intent-alignment/`
  - `.codex/skills/business-to-technical-translation/`
  - `.codex/skills/plan-creator/`
  - `.codex/skills/plan-reviewer/`
  - `.codex/skills/agent-skill-creator/`
  - `.codex/skills/agent-skill-reviewer/`
  - `.codex/skills/agent-skill-template/`
  - `.codex/skills/git-branch-naming/`
  - `.codex/skills/git-commit-convention/`
  - `.codex/skills/git-post-merge-workflow/`
  - `.codex/skills/worktree-manager/`

- **Out of scope**:
  - any edit under `skills/**`
  - any edit under `.github/skills/**`
  - hash stamping, JSONL inventory, or any other skill-versioning work
  - platform-wide residue cleanup outside the 11 materialized `.codex` skill
    surfaces
  - projection automation, generator work, or runtime loader changes
  - README, VERSION, release, or tag updates

## Locked Decisions

- Feature branch is frozen to
  `feat/andrew/codex-skills-canonical-retarget`.
- PR target branch is frozen to `dev`.
- Implementation write set is frozen to these 13 exact `.codex/skills/**`
  paths only:
  - `.codex/skills/README.md`
  - `.codex/skills/provenance.md`
  - `.codex/skills/business-intent-alignment/`
  - `.codex/skills/business-to-technical-translation/`
  - `.codex/skills/plan-creator/`
  - `.codex/skills/plan-reviewer/`
  - `.codex/skills/agent-skill-creator/`
  - `.codex/skills/agent-skill-reviewer/`
  - `.codex/skills/agent-skill-template/`
  - `.codex/skills/git-branch-naming/`
  - `.codex/skills/git-commit-convention/`
  - `.codex/skills/git-post-merge-workflow/`
  - `.codex/skills/worktree-manager/`
- `skills/**` and `.github/skills/**` are read-only for this topic.
- `skills/<skill-name>/` remains the canonical source of truth for all 11
  selected skills.
- `.codex/skills/<skill-name>/` for those 11 entries must be a materialized
  copy, not a symlink retarget.
- `.<platform>/skills/...` concretization applies only inside copied
  `.codex/skills/**` content and must become `.codex/skills/...`.
- This topic is not a stable-library topic.
- `README.md` stays unchanged.
- `VERSION` stays unchanged.
- No release or tagging action exists in this topic.
- Independent plan review was required before branch preparation and
  implementation. Implementation review must complete before publish routing.

## Boundaries / Exclusions

- Planning actor owns this topic plan and step truth for the planning /
  progression phase.
- Reviewer owns review verdicts and must not author the final implementation
  directly.
- Creator owns only the bounded `.codex/skills/**` materialization work after
  plan review approval.
- Main Agent owns commit, push, PR, and merge routing after review acceptance
  and required human approval.
- Do not retroactively widen this topic into canonical-content alignment for
  `skills/**` or `.github/skills/**`.
- Do not treat `.codex/skills/` as a third authority tree or cutover proof.
- If execution requires any path outside the listed topic artifacts and frozen
  `.codex/skills/**` write set, stop and repair the plan before continuing.

## Status / Allowed Transitions

- **Current**: `publish-in-progress`
- **Execution model**: follow the canonical creator -> reviewer -> publish ->
  merge path, with no release action
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

- Plan review has already approved this topic contract.
- Implementation review has accepted the staged 11-item materialized `.codex`
  surface and the current topic truth artifacts.
- If later review feedback returns `needs-rework`, corrections must stay inside
  this topic's plan/step/review-log artifacts or the frozen `.codex/skills/**`
  implementation write set only.
- Reviewer findings that control routing or multi-round rework must be recorded
  in the topic-local review log instead of hidden chat history.

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/codex-skills-canonical-retarget/codex-skills-canonical-retarget.plan.md` | Planning actor | Repo-visible execution contract for this topic |
| Topic progression artifact | `plan/codex-skills-canonical-retarget/codex-skills-canonical-retarget.step.md` | Planning actor | Current-truth workflow progression status for this topic |
| Review routing log | `plan/codex-skills-canonical-retarget/codex-skills-canonical-retarget.review-log.md` | Reviewer / Planning actor | Repo-visible verdict history when reviewer feedback controls routing |
| Projection surface note | `.codex/skills/README.md` | Creator | First-wave mapping table and source-rule text for the materialized `.codex` surface |
| Projection provenance table | `.codex/skills/provenance.md` | Creator | Provenance rows for the 11 materialized first-wave `.codex` skill entries |
| Materialized skill surface | `.codex/skills/business-intent-alignment/` | Creator | `.codex`-local copy of canonical `skills/business-intent-alignment/` |
| Materialized skill surface | `.codex/skills/business-to-technical-translation/` | Creator | `.codex`-local copy of canonical `skills/business-to-technical-translation/` |
| Materialized skill surface | `.codex/skills/plan-creator/` | Creator | `.codex`-local copy of canonical `skills/plan-creator/` |
| Materialized skill surface | `.codex/skills/plan-reviewer/` | Creator | `.codex`-local copy of canonical `skills/plan-reviewer/` |
| Materialized skill surface | `.codex/skills/agent-skill-creator/` | Creator | `.codex`-local copy of canonical `skills/agent-skill-creator/` with `.codex` concretization where required |
| Materialized skill surface | `.codex/skills/agent-skill-reviewer/` | Creator | `.codex`-local copy of canonical `skills/agent-skill-reviewer/` with `.codex` concretization where required |
| Materialized skill surface | `.codex/skills/agent-skill-template/` | Creator | `.codex`-local copy of canonical `skills/agent-skill-template/` with `.codex` concretization where required |
| Materialized skill surface | `.codex/skills/git-branch-naming/` | Creator | `.codex`-local copy of canonical `skills/git-branch-naming/` |
| Materialized skill surface | `.codex/skills/git-commit-convention/` | Creator | `.codex`-local copy of canonical `skills/git-commit-convention/` |
| Materialized skill surface | `.codex/skills/git-post-merge-workflow/` | Creator | `.codex`-local copy of canonical `skills/git-post-merge-workflow/` |
| Materialized skill surface | `.codex/skills/worktree-manager/` | Creator | `.codex`-local copy of canonical `skills/worktree-manager/` |

Artifact path notes:

- This topic does **not** modify `README.md`.
- This topic does **not** modify `VERSION`.
- This topic does **not** modify `.github/skills/**` or `skills/**`.
- Treat the listed paths as an executable contract.
- If later work appears outside these paths, stop and repair the topic plan
  before continuing.

## Implementation Steps

1. After plan review approval, re-read this topic plan, the current
   `.codex/skills/README.md`, the current `.codex/skills/provenance.md`, and
   the 11 named `.codex/skills/*` surfaces before editing the projection
   surface.
2. Remove the 11 top-level `.codex/skills/*` symlink surfaces named in this
   topic and materialize directories copied from same-name canonical
   `skills/<skill-name>/` folders.
3. Within those copied `.codex/skills/**` files only, concretize any copied
   `.<platform>/skills/...` literals to `.codex/skills/...`.
4. Update `.codex/skills/README.md` so the source-rule wording and first-wave
   mapping table match the materialized-copy model.
5. Update `.codex/skills/provenance.md` so all 11 first-wave rows record the
   canonical upstream path, `materialization_mode = materialized-copy`, and the
   relevant validation basis.
6. Keep `skills/**` and `.github/skills/**` read-only throughout the topic.
7. Stop and route back to plan repair if implementation requires any additional
   file, any canonical-source edit under `skills/**`, or any platform-wide
   cleanup outside the frozen write set.

## Validation / Acceptance Checks

- the plan and step artifacts exist at the exact topic-local paths above
- the implementation write set stays limited to the 13 frozen
  `.codex/skills/**` entries
- all 11 targeted `.codex/skills/*` entries are directories and are not
  symlinks
- the 11 materialized `.codex/skills/*` surfaces originate from same-name
  canonical `skills/*` content
- copied content differences versus canonical `skills/*` are limited to
  required `.codex/skills/...` concretization inside the `.codex` surface
- `.codex/skills/README.md` and `.codex/skills/provenance.md` both reflect
  `materialized-copy` provenance for those 11 entries
- no file under `skills/**` or `.github/skills/**` is modified
- no hash/JSONL/versioning work is introduced
- no platform-wide residue cleanup is introduced
- reviewer handoff remains one JSON object

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

- Run normal post-merge local sync only if the topic later reaches merge.
- No repository release action is required.
- No `README.md` or `VERSION` update is allowed in this topic.

## Open Questions / Unresolved Items

- None. The feature branch, PR target, materialization mode, implementation
  write set, read-only surfaces, and forbidden scope are all frozen for this
  topic.
