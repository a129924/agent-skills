# Plan Reviewer Skill Plan

## Goal / Outcome

Create a `plan-reviewer` Agent Skill that independently reviews repo-visible
`plan/<topic>/<topic>.plan.md` files for this repository.

When this topic is complete:

- `.github/skills/plan-reviewer/` exists as a `review-ready` skill draft
- the skill can review topic plans produced by `plan-creator` or equivalent
  planning work
- the skill returns a single machine-consumable JSON verdict with
  `approved|needs-rework`, `blocking_issues`, and
  `ADDRESS` / `DISCUSS` / `SKIP` triage
- the skill is explicitly positioned as a planning-contract gate that runs after
  a repo-visible topic plan exists and before execution proceeds under
  `plan/agent-handoff-workflow.md`

## Scope

- **In scope**:
  - create `.github/skills/plan-reviewer/` as a new higher-risk reviewer skill
  - define the skill's single responsibility, trigger conditions, inputs,
    process, outputs, and boundaries
  - teach independent review of repo-visible topic plans for this repository
  - encode the known topic-plan failure modes this reviewer must catch:
    - missing required sections
    - invalid or non-canonical status transitions
    - vague or drifting `Artifact Paths`
    - mixed or undeclared stable-library intent
    - non-JSON reviewer handoff contracts
    - wrong phase timing
    - role-boundary confusion across planning actor, creator, reviewer, and
      Main Agent
    - placeholder wording such as `TBD`, `later`, or `follow normal process`
      where the workflow requires an explicit contract
  - teach the intended operating sequence:
    - `plan-creator` authors the repo-visible topic plan
    - Main Agent uses `/fleet` to route that plan to an independent reviewer
    - execution proceeds only after the plan is treated as valid
  - stop at a `review-ready` skill draft

- **Out of scope**:
  - do not modify `plan/agent-handoff-workflow.md` in this topic
  - do not modify `.github/guides/MAIN-AGENT-WORKFLOW.md` in this topic
  - do not update `README.md`, `VERSION`, or `.github/copilot-instructions.md`
    in this topic
  - do not create a plan-authoring template; `plan-reviewer` is not an
    authoring skill
  - do not broaden `plan-reviewer` into a generic project-plan reviewer outside
    this repository
  - do not implement branch preparation, creator drafting, publish routing,
    post-merge actions, or release execution
  - do not create the follow-up workflow-spec-alignment topic in this same topic

## Locked Decisions

### 1. Responsibility: topic-plan review only

- `plan-reviewer` reviews repo-visible topic plans only.
- It does **not** author topic plans; that remains `plan-creator` work.
- It does **not** review skill folders or implementation drafts; that remains
  the existing Phase 4 reviewer responsibility.
- It does **not** publish, merge, release, or route execution itself.

### 2. Coverage: all repo-visible topic plans

- The skill applies to all repo-visible topic plans in this repository.
- It is repository-specific and must not become a generic planning reviewer for
  arbitrary application codebases.
- It must be able to review plans for:
  - new skills
  - workflow-spec changes
  - wording-only or guide topics
  - other repo-internal topics that still follow the same handoff workflow

### 3. Operational position: after plan creation, before execution

- The intended sequence is:
  1. `plan-creator` or equivalent planning work creates
     `plan/<topic>/<topic>.plan.md`
  2. Main Agent routes the plan to an independent reviewer via `/fleet`
  3. creator or planning actor addresses required fixes
  4. only then may execution continue under `plan/agent-handoff-workflow.md`
- `plan-reviewer` is therefore a planning-contract gate.
- It is **not** a replacement for the existing implementation-review Phase 4 in
  `plan/agent-handoff-workflow.md`.

### 4. Review basis: shared contract surface, separate reviewer posture

- `plan-reviewer` must review against the same topic-plan contract surface
  defined by:
  - `plan/agent-handoff-workflow.md`
  - `.github/skills/plan-creator/reference.md`
  - `.github/skills/plan-creator/checklist.md`
  - `.github/skills/plan-creator/templates/topic-plan-template.md`
- It must not mirror `plan-creator`'s authoring flow, template-first behavior,
  or writer posture.
- It must use reviewer language, gatekeeping checks, and independent verdicts.

### 5. Output shape: fixed JSON only

- Reviewer output is a single JSON object only.
- The fixed report shape is:
  - `verdict`
  - `blocking_issues`
  - `copilot_feedback_triage`
    - `ADDRESS`
    - `DISCUSS`
    - `SKIP`
- Reviewer rationale must stay inside the structured JSON fields rather than
  trailing prose.

### 6. Validation depth: medium-high, contract-breaking only

- `checklist.md` should gate contract-breaking issues, not wording polish.
- `examples.md` must cover at least:
  - `Approved / non-stable topic`
  - `Approved + ADDRESS / stable topic`
  - `Needs-rework / workflow-breaking`
  - `Needs-rework / scope-or-boundary-breaking`
- The skill should make it difficult to approve a plan whose workflow contract
  is still unsafe.

### 7. First rollout: review-ready only, non-stable

- This topic produces a `review-ready` `plan-reviewer` skill only.
- Stable-library surfaces such as `README.md`, `VERSION`, and release artifacts
  remain untouched in this topic.
- If `plan-reviewer` is later promoted to the stable library, that work belongs
  to a separate follow-up topic.

## Boundaries / Exclusions

- Do not let `plan-reviewer` rewrite plans on behalf of the planning actor.
- Do not let `plan-reviewer` invent a second topic-plan schema separate from
  `plan-creator` and the canonical workflow.
- Do not let `plan-reviewer` silently tolerate path drift, undeclared stable
  intent, or non-JSON reviewer handoff.
- Do not convert `plan-reviewer` into a new numbered workflow phase in this
  topic.
- Do not treat hidden chat context or oral intent as a substitute for the
  repo-visible topic plan contract.
- Do not add local template files or scaffolding paths that belong to plan
  authoring rather than plan review.

## Status / Allowed Transitions

- **Current**: `merged`
- **Execution model**: follow the canonical creator -> reviewer -> publish ->
  merge path, but stop at `merged`; this topic does not declare a release action
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

- This topic itself follows the existing repository execution workflow.
- `approved` does **not** permit skipping directly to publish work.
- After reviewer approval, the creator / Main Agent flow must first apply any
  required reviewer JSON `ADDRESS` feedback before the standard Phase 4.5
  planner contract alignment checkpoint runs.
- If Phase 4.5 finds drift in locked decisions, artifact paths, or other
  plan-level semantics, route the topic back to `creator-in-progress` before
  any publish work continues.
- The skill being created by this topic is intended for use as a pre-Phase-2
  planning gate for later topics, but this topic does **not** add a new
  numbered phase or change the canonical workflow file itself.

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/plan-reviewer/plan-reviewer.plan.md` | Planning actor | Repo-visible execution contract for this topic |
| Skill folder | `.github/skills/plan-reviewer/` | Creator | Root output location for the draft skill |
| Core skill contract | `.github/skills/plan-reviewer/SKILL.md` | Creator | Executable instruction contract for independent topic-plan review |
| Reference guidance | `.github/skills/plan-reviewer/reference.md` | Creator | Stable local rules for review basis, role boundaries, JSON output, and workflow positioning |
| Detailed examples | `.github/skills/plan-reviewer/examples.md` | Creator | Positive and negative topic-plan review scenarios across the required reviewer paths |
| Validation checklist | `.github/skills/plan-reviewer/checklist.md` | Creator | Repeatable contract-breaking checks for this higher-risk reviewer skill |

Artifact path notes:

- This topic does **not** modify `README.md`, `VERSION`,
  `.github/copilot-instructions.md`, `plan/agent-handoff-workflow.md`, or
  `.github/guides/MAIN-AGENT-WORKFLOW.md`.
- `Stable library metadata` is intentionally absent because this topic is not a
  stable-library publish topic.
- The listed paths are an executable contract, not an informational appendix.
- If creator output, reviewer findings, or planner alignment reveals repo-visible
  changes outside these paths, treat that drift as a plan violation and route
  the topic back to `creator-in-progress` before continuing.

## Implementation Steps

### Creator Phase (after plan approval)

1. **Draft `SKILL.md`**
   - Define `plan-reviewer` as a single-purpose skill for independent review of
     repo-visible topic plans.
   - Make `Trigger / When to use` explicit:
     - use after a repo-visible `plan/<topic>/<topic>.plan.md` exists
     - use before branch preparation or creator implementation begins
     - use when an existing topic plan needs contract review or re-review
     - do not use for authoring the plan itself
     - do not use for reviewing a skill folder or implementation draft
     - do not use for generic project-management plans outside this repository
   - In `Process`, require:
     - read the topic plan plus the current workflow contract
     - review against the shared contract surface from `plan-creator` and the
       workflow
     - reject missing required sections, invalid transitions, vague artifact
       paths, undeclared stable intent, wrong timing, non-JSON handoff, role
       confusion, and unsafe placeholders
     - keep the review focused on contract-breaking issues rather than wording
       polish
     - return the fixed JSON verdict shape with no trailing prose
   - Include concise positive and negative examples in `SKILL.md`.

2. **Draft `reference.md`**
   - Explain the repository-specific basis for plan review:
     - required section meanings
     - stable-library intent rules
     - artifact-path exactness
     - role-boundary rules
     - reviewer handoff JSON rules
   - Explain the intended operating position:
     - plan exists first
     - `/fleet` routes it to an independent reviewer
     - execution starts only after the plan is valid
   - Explain that `plan-reviewer` does not redefine the canonical workflow and
     does not replace implementation review.

3. **Draft `examples.md`**
   - Include at least:
     - one `Approved / non-stable topic` example
     - one `Approved + ADDRESS / stable topic` example
     - one `Needs-rework / workflow-breaking` example
     - one `Needs-rework / scope-or-boundary-breaking` example
   - Show the expected JSON verdict shape in representative cases.
   - Keep examples repository-specific and tied to real topic-plan failure modes.

4. **Draft `checklist.md`**
   - Add medium-high contract checks for:
     - exact `plan/<topic>/<topic>.plan.md` path
     - required sections present and named correctly
     - canonical `Status / Allowed Transitions`
     - exact and bounded `Artifact Paths`
     - explicit stable-library intent
     - machine-consumable reviewer handoff JSON
     - correct post-merge / release timing
     - no planning actor / creator / reviewer / Main Agent role mixing
     - no unsafe placeholders such as `TBD` or `later`
   - Keep the checklist focused on contract-breaking issues rather than tone or
     formatting preferences.

### Reviewer Phase (after creator delivers review-ready)

1. Confirm the skill stays single-purpose: independent topic-plan review only.
2. Confirm the skill explicitly reviews against all four contract sources:
   - `plan/agent-handoff-workflow.md`
   - `.github/skills/plan-creator/reference.md`
   - `.github/skills/plan-creator/checklist.md`
   - `.github/skills/plan-creator/templates/topic-plan-template.md`
3. Confirm the skill shares that contract surface without copying authoring
   behavior or local templates into the reviewer role.
4. Confirm the skill clearly positions itself after topic-plan creation and
   before execution proceeds under `plan/agent-handoff-workflow.md`.
5. Confirm the JSON output contract is explicit, fixed, and machine-consumable.
6. Confirm `examples.md` and `checklist.md` match the risk of a planning gate.
7. Confirm no stable-library surfaces or workflow-spec files changed in this
   first topic.

## Validation / Acceptance Checks

- `plan-reviewer` stays clearly separate from `plan-creator`,
  `agent-skill-reviewer`, and Main Agent orchestration roles.
- The skill can reject the known topic-plan contract failures before execution
  reaches branch preparation or creator implementation.
- The skill explicitly describes the intended operating sequence:
  plan first, independent `/fleet` review second, execution third.
- The skill's review basis explicitly names all four contract sources:
  `plan/agent-handoff-workflow.md`,
  `.github/skills/plan-creator/reference.md`,
  `.github/skills/plan-creator/checklist.md`, and
  `.github/skills/plan-creator/templates/topic-plan-template.md`.
- The JSON reviewer output stays a single object with `verdict`,
  `blocking_issues`, and `ADDRESS` / `DISCUSS` / `SKIP` triage.
- `examples.md` covers the required four reviewer paths.
- `checklist.md` gates contract-breaking issues and does not drift into generic
  style review.
- This topic does not modify stable-library surfaces or workflow-spec files.

## Reviewer Handoff

Reviewer should return one JSON object and focus on:

- whether the skill stays topic-plan-review-only
- whether the skill's review basis matches the current topic-plan contract
- whether the skill clearly positions `/fleet` review after plan creation and
  before later execution
- whether the JSON verdict format is explicit and machine-consumable
- whether the checklist and examples are strong enough for a planning gate

```json
{
  "verdict": "approved|needs-rework",
  "blocking_issues": [
    {
      "issue": "Description of the unmet requirement",
      "file": "path/to/file.md",
      "fix": "Concrete change required before re-review"
    }
  ],
  "copilot_feedback_triage": {
    "ADDRESS": [
      {
        "comment": "Text of Copilot comment",
        "location": "path/to/file.md:line",
        "why": "Why this feedback should be applied"
      }
    ],
    "DISCUSS": [
      {
        "comment": "Text of optional feedback",
        "optional": true,
        "why": "Why this is worth discussing but not required"
      }
    ],
    "SKIP": [
      {
        "comment": "Text of inapplicable feedback",
        "why": "Why it should not change the draft"
      }
    ]
  }
}
```

Reviewer output must be a single JSON object with no trailing prose. Keep all
reasoning inside the structured JSON fields so the handoff remains safely
machine-consumable.

## Post-merge / release actions

1. After merge, run the normal post-merge local sync flow for the working
   branch.
2. Do **not** update `README.md`, `VERSION`, `.github/copilot-instructions.md`,
   `plan/agent-handoff-workflow.md`, or release notes in this topic.
3. If the repository later wants canonical workflow wording that formally names
   `plan-reviewer`, create a separate workflow-spec-alignment topic after this
   skill topic is complete.
4. No repository release action exists for this topic.

## Open Questions / Unresolved Items

- None. Workflow-spec alignment is intentionally deferred to a separate
  follow-up topic and does not block this topic.
