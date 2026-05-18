# Python Type Hints Object Boundary Plan

> Analysis-layer mode: **STRICT**
> Execution-facing source of truth:
> `analysis/python-type-hints-object-boundary/technical-spec.md`
> Business guardrail:
> `analysis/python-type-hints-object-boundary/requirements.md`
> No human `override` instruction was provided, so analysis artifacts outrank
> chat-time paraphrases.

## Goal / Outcome

Create a repo-visible execution contract for tightening
`.github/skills/python-type-hints-strict/` so it no longer permits a known
repo-owned/domain type to be weakened to `object` except at true untrusted
boundaries or narrowing-helper inputs, while keeping the topic inside strict
typing policy rather than runtime model selection.

## Scope

- **In scope**:
  - update `.github/skills/python-type-hints-strict/SKILL.md`
  - update `.github/skills/python-type-hints-strict/reference.md`
  - update `.github/skills/python-type-hints-strict/examples.md`
  - preserve explicit signposting to `python-model-selection`
  - preserve the active skill path under `.github/skills/`

- **Out of scope**:
  - any change to `.github/copilot-instructions.md`
  - any new test harness, checklist file, or skill-path migration
  - choosing runtime models such as `Enum`, `dataclass`, `ABC`, or `Protocol`
  - implementation work outside the target skill folder

## Locked Decisions

- Topic slug is `python-type-hints-object-boundary`.
- `python-type-hints-strict` is an **existing stable skill** listed in `README.md`
  under Current skills; this topic updates it with a new hard `object`-boundary rule.
- **Stable-library SemVer impact**: adding a new constraint rule to an existing stable
  skill is a backward-compatible capability addition → **MINOR bump** (e.g. `0.57.0`).
- `README.md` and `VERSION` must be updated post-merge as part of the standard
  release step; they are deferred, not excluded.
- Base branch is `dev`.
- Execution branch is `feat/andrew/python-type-hints-object-boundary`.
- Managed worktree path is
  `../agent-skills.worktrees/agent-20260515-python-type-hints-object-boundary`.
- The hard rule is locked: when a repo-owned/domain type already exists,
  changing it to `object` is invalid unless the position is a true untrusted
  boundary or narrowing-helper input.
- Every accepted `object` usage must include a short justification naming the
  boundary or narrowing role it serves.
- The topic must not broaden into model selection; runtime model-shape choices
  remain delegated to `python-model-selection`.
- The plan maps 100% to
  `analysis/python-type-hints-object-boundary/technical-spec.md`.

## Boundaries / Exclusions

- Creator owns drafting the target skill files only; creator must not approve
  its own work.
- Reviewer owns verdict only; reviewer must not author the final implementation
  directly.
- Main Agent may manage plan, branch, publish, and PR workflow later, but must
  not change locked intent without updating repo-visible artifacts.
- If implementation drifts outside the listed artifact paths, treat that as plan
  violation and route back to `creator-in-progress` or plan repair before
  publish work.
- This topic does not authorize commit, push, PR, merge, release, or stable
  promotion work by itself.

## Status / Allowed Transitions

- **Current**: `pr-open`
- **Execution model**: PR #77 is already open, so live routing resumes at
  `pr-open` and continues through the canonical review-fix -> merge path; this
  topic does not declare a release action
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

- Live resume point is `pr-open` for PR #77; do not restart this topic from
  `planned` unless the plan is explicitly reset.
- Phase 4.5 planner contract alignment is required after reviewer approval and
  before publish work.
- If reviewer approval reveals drift in the locked invalid/valid `object`
  contract, artifact paths, or non-stable intent, route back to
  `creator-in-progress`.
- Human STOP POINT 1 has already been passed for this topic because the PR is
  open; use PR feedback / merge routing from here.
- This planning topic itself stops after the repo-visible plan is produced and
  human review is complete.

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/python-type-hints-object-boundary/python-type-hints-object-boundary.plan.md` | Planning actor | Repo-visible execution contract for this topic |
| Requirements baseline | `analysis/python-type-hints-object-boundary/requirements.md` | Planning actor | Frozen business baseline that defines the valid/invalid `object` policy |
| Technical spec | `analysis/python-type-hints-object-boundary/technical-spec.md` | Planning actor | Execution-facing technical source of truth for this topic |
| Skill contract | `.github/skills/python-type-hints-strict/SKILL.md` | Creator | Top-level rule set, process, validation, and concise examples |
| Reference rules | `.github/skills/python-type-hints-strict/reference.md` | Creator | Detailed `object` boundary rules, justification requirement, and preference order |
| Examples | `.github/skills/python-type-hints-strict/examples.md` | Creator | Positive and negative scenarios for allowed and invalid `object` use |

Artifact path notes:

- `README.md` and `VERSION` are **deferred** to the post-merge release step, not
  permanently excluded; a MINOR bump is required before or at merge into the
  stable branch.
- `.github/copilot-instructions.md` remains out of scope.
- The listed paths are an executable contract.
- If later work proposes any repo-visible change outside these paths, stop and
  repair the topic plan before execution continues.

## Implementation Steps

1. **Creator updates `SKILL.md`**
   - add the hard invalid rule for weakening known repo-owned/domain types to
     `object`
   - add boundary-only allowance for true untrusted boundaries and
     narrowing-helper inputs
   - add validation wording that asks whether a repo-owned type already exists
   - strengthen concise positive and negative examples to mention `object`

2. **Creator updates `reference.md`**
   - add an `object`-specific rule section
   - define the allowed boundary list narrowly: decoder output, validator input,
     type-guard input, and similar narrowing-helper entry points
   - require short justification for each surviving `object` usage
   - encode the preference order:
     `repo-owned type -> explicit refinement / alias -> boundary-only object`

3. **Creator updates `examples.md`**
   - add one valid example showing `object` at a narrowing/helper boundary with
     immediate narrowing back to a precise type
   - add one invalid example showing a known alias/value type/model weakened to
     `object`
   - keep examples inside strict-typing guidance and avoid model-selection drift

4. **Creator self-check before reviewer handoff**
   - verify all three files describe the same invalid/valid line for `object`
   - verify `python-model-selection` redirect remains intact
   - verify no new files, stable-surface edits, or path drift were introduced

5. **Reviewer pass**
   - evaluate the revised skill against this topic plan
   - return machine-consumable JSON only
   - use `needs-rework` if any file permits `object` more broadly than the
     locked contract

## Validation / Acceptance Checks

- [ ] `analysis/python-type-hints-object-boundary/requirements.md` and
  `analysis/python-type-hints-object-boundary/technical-spec.md` remain the
  governing inputs for this topic
- [ ] `SKILL.md` explicitly says weakening an existing repo-owned/domain type to
  `object` is invalid outside true untrusted boundaries or narrowing-helper
  inputs
- [ ] `reference.md` names the allowed `object` boundary list and requires
  justification for every remaining `object` site
- [ ] `examples.md` includes at least one valid and one invalid `object`
  scenario that match the contract and reference wording
- [ ] `python-model-selection` redirect is preserved
- [ ] no files outside the declared artifact paths are modified
- [ ] reviewer handoff remains exactly one JSON object
- [ ] `README.md` and `VERSION` are scheduled for MINOR bump in post-merge release step

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

- After merge, bump `VERSION` to the next MINOR version (e.g. `0.57.0`) and
  update `README.md` if the skill description requires amendment.
- Local sync follows the normal post-merge workflow.
- The `README.md` description for `python-type-hints-strict` should note the
  `object`-boundary rule if it changes the advertised capability summary.

## Open Questions / Unresolved Items

- None at planning time. The analysis layer is complete and this plan is ready
  for creator execution after human review.
