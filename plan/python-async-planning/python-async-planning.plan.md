# python-async-planning topic plan

Analysis-layer mode: STRICT

Prerequisites:
- `analysis/python-async-planning/requirements.md` — frozen business baseline for this topic
- `analysis/python-async-planning/technical-spec.md` — execution-facing technical baseline for this topic
- Traceability base: authored on `feat/andrew/python-async-planning-spec`, based on `dev@77fa194`

## Goal / Outcome

- Add a new repository skill, `python-async-planning`, plus the minimum related planning/review routing changes so async-capable Python topics cannot proceed toward implementation without a frozen async decision baseline.

## Scope

- **In scope**:
  - `analysis/python-async-planning/requirements.md`
  - `analysis/python-async-planning/technical-spec.md`
  - `plan/python-async-planning/python-async-planning.plan.md`
  - `.github/skills/python-async-planning/SKILL.md`
  - `.github/skills/python-async-planning/reference.md`
  - `.github/skills/python-async-planning/examples.md`
  - optional: `.github/skills/python-async-planning/checklist.md`
  - `.github/skills/python-plan-authoring/SKILL.md`
  - `.github/skills/python-plan-authoring/templates/python-plan-template.md`
  - `.github/skills/python-plan-authoring/examples.md`
  - `.github/skills/python-plan-review/SKILL.md`
  - `.github/skills/python-plan-review/checklist.md`
  - `.github/skills/python-plan-review/examples.md`
  - optional only if needed for discoverability: `.github/skills/python-async-await/SKILL.md` or `.github/skills/python-async-await/reference.md`
  - `README.md`
  - `VERSION`

- **Out of scope**:
  - implementing arbitrary application async code
  - redesigning the repository's full Python planning framework
  - turning `python-async-await` into a general planning skill
  - release-tag creation or post-merge release execution

## Locked Decisions

- This topic is a stable-library-affecting topic.
- Stable-library timing is `publish-in-progress`, not `release`.
- The new skill name is `python-async-planning`.
- The skill remains Python-specific and portable across general Python async I/O planning.
- Async-capable trigger evidence and exemption rules are frozen by the analysis layer and must not be reinterpreted downstream.
- Async-capable topics must carry named async-planning sections covering:
  - async boundary decision
  - resource lifecycle decision
  - concurrency model
  - failure model
  - cancellation / timeout policy
  - validation plan
  - handoff notes for the implementer
- Review may not silently override the plan baseline; contradictions must be logged or routed to re-plan.
- Late-discovered async risk requires minimal retrofit rather than silent continuation.

## Boundaries / Exclusions

- Planning actor owns the analysis artifacts and this topic plan.
- Creator owns only the draft implementation inside the listed artifact paths.
- Reviewer owns only the independent verdict and may not author the final implementation directly.
- Main Agent owns publish, PR, merge-follow-up, and any stable-library file changes that occur after approval.
- This topic must not add broader async architecture guidance unrelated to planning-stage risk freezing.
- If later work needs release tagging, commit policy, or post-merge cleanup, that belongs to separate workflow phases and skills.

## Status / Allowed Transitions

- **Current**: `planned`
- **Execution model**: follow the canonical creator -> reviewer -> publish -> merge path; this topic stops at `merged` and does not declare a Phase 10 release action
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

- Phase 4.5 planner-alignment rule applies normally.
- Creator work must happen inside the spec worktree / feature-branch lineage created from `dev`.
- If work appears outside the locked artifact paths, stop and repair the plan before continuing.

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Business baseline | `analysis/python-async-planning/requirements.md` | Planning actor | Frozen business baseline for async-planning intent |
| Technical baseline | `analysis/python-async-planning/technical-spec.md` | Planning actor | Strict-mode execution source for this topic |
| Topic plan | `plan/python-async-planning/python-async-planning.plan.md` | Planning actor | Repo-visible execution contract for this topic |
| New skill contract | `.github/skills/python-async-planning/SKILL.md` | Creator | Main skill contract for planning-stage async risk freezing |
| New skill reference | `.github/skills/python-async-planning/reference.md` | Creator | Stable local knowledge and constraints for the new skill |
| New skill examples | `.github/skills/python-async-planning/examples.md` | Creator | Positive, negative, and edge examples for the new skill |
| Optional new skill checklist | `.github/skills/python-async-planning/checklist.md` | Creator | Additional misuse-prevention guidance only if review shows it is needed |
| Plan-authoring routing | `.github/skills/python-plan-authoring/SKILL.md` | Creator | Route async-capable plan work toward the new skill |
| Plan-authoring template | `.github/skills/python-plan-authoring/templates/python-plan-template.md` | Creator | Ensure named async-planning sections can be required in authoring guidance |
| Plan-authoring examples | `.github/skills/python-plan-authoring/examples.md` | Creator | Show correct and incorrect async-planning routing cases |
| Plan-review routing | `.github/skills/python-plan-review/SKILL.md` | Creator | Block missing async-planning coverage on async-capable topics |
| Plan-review checklist | `.github/skills/python-plan-review/checklist.md` | Creator | Reviewer checks for async trigger evidence, contradictions, and retrofit behavior |
| Plan-review examples | `.github/skills/python-plan-review/examples.md` | Creator | Show approve / needs-rework behavior for async-capable and retrofit cases |
| Optional async-await cross-link | `.github/skills/python-async-await/SKILL.md` | Creator | Small discoverability cross-link only if needed |
| Optional async-await reference cross-link | `.github/skills/python-async-await/reference.md` | Creator | Small discoverability cross-link only if needed |
| Stable skill list | `README.md` | Main Agent | Add the `python-async-planning` row if approved stable promotion is reached |
| Repository version baseline | `VERSION` | Main Agent | Apply the required MINOR bump if approved stable promotion is reached |

Artifact path notes:

- This topic may modify `README.md` and `VERSION` only at `publish-in-progress` after approval.
- This topic does not require `.github/copilot-instructions.md` changes.
- Artifact paths are executable contract paths. Any later work outside these paths is a plan-alignment problem and must stop for plan repair.

## Stable library metadata

- `README row`: `| \`python-async-planning\` | defines planning-stage Python async architecture and risk-freezing rules for trigger evidence, lifecycle decisions, contradictions, retrofit handling, and portability boundaries before implementation |`
- `VERSION bump`: MINOR
- `timing`: `publish-in-progress`
- `rationale`: this topic adds a new stable skill and therefore changes the user-visible skill library surface
- `release-note expectations`: none in this topic; no Phase 10 release action is declared here

## Implementation Steps

1. Draft `.github/skills/python-async-planning/SKILL.md`, `reference.md`, and `examples.md` so the new skill freezes trigger evidence, exemption rules, contradiction handling, retrofit behavior, portability boundaries, required async-planning output sections, and explicit `PASS` / `SOFT FAIL` / `BLOCKED` validation guidance in `SKILL.md`.
2. Add `.github/skills/python-async-planning/checklist.md` only if the draft still needs extra misuse-prevention signals after review of the core files.
3. Update `.github/skills/python-plan-authoring/SKILL.md`, `templates/python-plan-template.md`, and `examples.md` so async-capable planning requests route to `python-async-planning` and use the named async-planning sections.
4. Update `.github/skills/python-plan-review/SKILL.md`, `checklist.md`, and `examples.md` so reviewer logic detects async-capable evidence, blocks missing async-planning coverage, records contradictions, and uses `retrofit required` for late-discovered async risk.
5. Only if discoverability still looks weak after Steps 1-4, add a limited cross-link in `.github/skills/python-async-await/SKILL.md` or `reference.md` without broadening that skill into a planning contract.
6. After independent reviewer approval and only during `publish-in-progress`, update `README.md` and `VERSION` to reflect the new stable skill.

## Validation / Acceptance Checks

- Strict-mode mapping is maintained: creator output stays traceable to `analysis/python-async-planning/technical-spec.md` and does not invent broader scope.
- The new skill remains single-purpose and Python-specific while still portable across general Python async I/O planning.
- `.github/skills/python-async-planning/SKILL.md` explicitly includes `PASS` / `SOFT FAIL` / `BLOCKED` validation guidance that maps to trigger evidence, exemption handling, contradiction surfacing, retrofit-required cases, and portability-boundary ambiguity.
- Trigger evidence, exemption rules, contradiction-log behavior, and minimal retrofit behavior are consistent across the new skill, plan-authoring guidance, and plan-review guidance.
- Reviewer-facing artifacts explicitly prevent silent override of the plan baseline.
- Optional async-await cross-link stays optional and limited to discoverability.
- `README.md` and `VERSION` are touched only if approval is reached and only at `publish-in-progress`.
- Reviewer handoff remains a single machine-consumable JSON object.

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

- After merge, use the repository's post-merge workflow for local sync and cleanup.
- No repository release action is required in this topic.
- This topic reaches terminal state at `merged`.

## Open Questions / Unresolved Items

- If creator output makes the new skill sufficiently discoverable without extra help, the optional cross-link into `python-async-await` should be skipped.
