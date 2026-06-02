# Skills Canonical Positioning Plan

## Goal / Outcome

Produce a bounded positioning correction that makes the repository's current
truth explicit without widening into skill-contract, workflow-contract, or
runtime/tooling migration.

When this topic is complete:

- `AGENTS.md` states that `skills/` is the current canonical truth
- `docs/repo-positioning.md` presents one current authority model rather than a
  transition-only split
- `.github/copilot-instructions.md` is clearly GitHub/Copilot compatibility
  guidance rather than a repo-wide policy owner
- `README.md` summarizes the same current-truth model and frames old migration
  notes as historical context only

## Scope

- **In scope**:
  - update `AGENTS.md`
  - update `docs/repo-positioning.md`
  - update `.github/copilot-instructions.md`
  - update `README.md`
  - create topic-local planning artifacts for this topic

- **Out of scope**:
  - editing `.github/skills/**`
  - editing `.codex/skills/**`
  - editing `skills/**`
  - editing `.github/guides/MAIN-AGENT-WORKFLOW.md`
  - editing any `agent-skill-*` contract surface
  - runtime/tooling/install/sync/projection automation changes
  - directory moves, copies, deletes, or path cutover work
  - VERSION, release, or stable-library publish work

## Locked Decisions

### 1. Topic type: positioning-only correction

- This topic corrects repository positioning only.
- It does not perform skill-contract migration, workflow-guide repair, or
  runtime follow-up.

### 2. Editable scope is fixed

Only these repo files may be modified by creator work:

- `AGENTS.md`
- `docs/repo-positioning.md`
- `.github/copilot-instructions.md`
- `README.md`

### 3. Forbidden scope is fixed

The following paths are forbidden in this topic even if they contain wording
that looks outdated after the four-file correction:

- `.github/skills/**`
- `.codex/skills/**`
- `skills/**`
- `.github/guides/MAIN-AGENT-WORKFLOW.md`
- any `agent-skill-*`
- runtime/tooling/install/sync/projection automation surfaces

If later work appears to require changes in those paths, stop and create a
separate topic instead of widening this one.

### 4. Analysis-layer priority is fixed

This topic uses strict-mode analysis inputs:

- `analysis/skills-canonical-positioning/requirements.md`
  - SHA-256: `20fa6d1f6f68466888bc5e814f2df9fe5af852fac6073028426d01c1ad3993b6`
- `analysis/skills-canonical-positioning/technical-spec.md`
  - SHA-256: `0c3341f2f8ef1cb32f78a332d84375c4aa2ad3522eb3eff441bdd0f92968ebbf`

The plan must map 100% to those analysis artifacts. Chat-time convenience must
not override them without an explicit human `override`.

### 5. Stable-library and release intent are absent

- This topic is not a stable-library publish topic.
- `VERSION` stays unchanged.
- No tag, release, or release-note action exists in this topic.

## Boundaries / Exclusions

- Do not rewrite `.github/skills/**` or `.codex/skills/**` descriptions to make
  the repository feel globally consistent.
- Do not treat the four-file correction as authorization to align creator,
  reviewer, template, or workflow contracts.
- Do not add new files outside the topic-local planning artifacts and the four
  editable documents.
- Do not infer README/VERSION release behavior from other topics.
- If scope drifts outside the exact editable paths, stop and repair the plan
  before implementation continues.

## Status / Allowed Transitions

- **Current**: `planned`
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

- Use the standard Phase 4.5 planner contract alignment rule from
  `plan/agent-handoff-workflow.md`.
- Any attempt to widen editable scope beyond the four locked files is plan drift
  and must route back to plan repair before execution continues.
- Reviewer findings about `.github/skills/**`, `.codex/skills/**`, or
  `skills/**` consistency are follow-up only unless one of the four editable
  files becomes impossible to update honestly.

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/skills-canonical-positioning/skills-canonical-positioning.plan.md` | Planning actor | Repo-visible execution contract for this topic |
| Topic progression artifact | `plan/skills-canonical-positioning/skills-canonical-positioning.step.md` | Planning actor | Current-truth workflow progression status for this topic |
| Requirements baseline | `analysis/skills-canonical-positioning/requirements.md` | Planning actor | Frozen business baseline for scope and authority rules |
| Technical baseline | `analysis/skills-canonical-positioning/technical-spec.md` | Planning actor | Frozen technical translation and forbidden-scope rules |
| Governance source | `AGENTS.md` | Creator | Canonical governance wording to correct |
| Positioning contract | `docs/repo-positioning.md` | Creator | Repository positioning wording to correct |
| Copilot compatibility guidance | `.github/copilot-instructions.md` | Creator | GitHub/Copilot-specific compatibility wording to correct |
| Human summary | `README.md` | Creator | Human-facing summary wording to correct |

Artifact path notes:

- This topic modifies `README.md`.
- This topic does **not** modify `VERSION`.
- This topic does **not** modify `.github/skills/**`, `.codex/skills/**`,
  `skills/**`, or `.github/guides/MAIN-AGENT-WORKFLOW.md`.
- Treat the listed editable paths as an executable contract.
- If later work drifts outside these paths, stop and repair the plan rather
  than staging extra files.

## Implementation Steps

### Creator Phase

1. Read the locked analysis artifacts before changing any repo file.
2. Update `AGENTS.md` so `skills/` is described as current canonical truth and
   the topic boundary stays positioning-only.
3. Update `docs/repo-positioning.md` so the file presents one current authority
   model and frames platform paths as compatibility/projection only.
4. Update `.github/copilot-instructions.md` so it clearly defers authority to
   `AGENTS.md` and `docs/repo-positioning.md`.
5. Update `README.md` so its summary and historical notes no longer imply that
   Copilot-era surfaces define current truth.
6. Do not edit any file outside the four locked editable paths.

### Reviewer Phase

1. Verify all file changes stay inside the four editable paths.
2. Verify `skills/` is described consistently as current canonical truth in all
   four files.
3. Verify `.github/copilot-instructions.md` is bounded to compatibility
   guidance and does not read as repo-wide authority.
4. Verify `README.md` historical notes remain historical and do not override the
   current authority model.
5. Verify no forbidden path was modified or implied to be modified.

### Main Agent publish flow

1. After reviewer approval and Phase 4.5 alignment, move the topic to
   `publish-in-progress`.
2. Stage only:
   - `AGENTS.md`
   - `docs/repo-positioning.md`
   - `.github/copilot-instructions.md`
   - `README.md`
   - topic-local planning artifacts if the workflow requires them in the same
     commit
3. Do not stage any forbidden-scope path.
4. Commit, push, and open the PR against `dev`.
5. No release action follows merge.

## Validation / Acceptance Checks

- all four editable files present one consistent authority model
- `skills/` is described as current canonical truth in all four files
- `.github/copilot-instructions.md` is explicitly compatibility guidance only
- `README.md` no longer implies `.github/skills/...` is current repository truth
- no file outside the four editable paths is modified
- `.github/skills/**`, `.codex/skills/**`, and `skills/**` remain untouched
- reviewer handoff stays a single JSON object
- no VERSION or release action is introduced

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

- Run normal post-merge local sync if the topic is merged.
- No repository release action is required.
- No VERSION bump or tag creation is allowed in this topic.

## Open Questions / Unresolved Items

- None. Editable scope, forbidden scope, authority model, and non-release intent
  are locked for this topic.
