# Plan Creator Skill Plan

## Goal / Outcome

Create a `plan-creator` Agent Skill that produces valid, repo-visible
`plan/<topic>/<topic>.plan.md` files for this repository.

The skill should make Phase 1 planning reliable before creator, reviewer, and
main-agent execution begins. Its output must be consumable by the existing
workflow without relying on hidden chat context, session summaries, or implied
intent.

## Scope

- **In scope**:
  - Create `.github/skills/plan-creator/` as a new higher-risk planning skill.
  - Define the skill's single responsibility, trigger conditions, inputs,
    process, outputs, and boundaries.
  - Teach canonical topic-plan authoring for this repository's workflow.
  - Include a local canonical template for `plan/<topic>/<topic>.plan.md`.
  - Encode the known failure modes this skill must prevent:
    - invalid status model or transitions
    - non-JSON reviewer handoff contracts
    - mixed or undeclared stable-library intent
    - incomplete or drifting `Artifact paths`
    - wrong section names or phase timing
    - mixed role ownership between planning actor, creator, reviewer, and
      main agent
  - Stop at a `review-ready` skill draft.

- **Out of scope**:
  - Do not implement a validator or scaffold script in this topic.
  - Do not update `README.md`, `VERSION`, or `.github/copilot-instructions.md`
    in this topic.
  - Do not modify `plan/agent-handoff-workflow.md` unless a tiny wording repair
    is strictly required for direct consistency.
  - Do not broaden `plan-creator` into a general project planner outside this
    repository.
  - Do not author downstream topic plans as part of this topic beyond the local
    examples and template needed by the skill itself.

## Locked Decisions

### 1. Responsibility: topic-plan authoring only

- `plan-creator` owns only Phase 1 planning output.
- It does **not** perform creator drafting, review verdicts, publish routing,
  post-merge actions, or release execution.
- Its stop condition is: a repo-visible topic plan exists and is ready to hand
  to the normal creator / reviewer / main-agent workflow.

### 2. Coverage: all repo topics, not only skill topics

- The skill applies to all topic plans in this repository.
- It remains repository-specific: it is not a generic planner for arbitrary
  application codebases.
- The skill must be able to author plans for:
  - new skills
  - workflow-spec changes
  - guide or wording-only topics
  - other repo-internal topics that still follow the same handoff workflow

### 3. Authoring mode: strict-stop-and-ask

- If scope, artifact paths, role ownership, stable-library timing, or release
  intent is unclear, `plan-creator` must stop and ask for clarification.
- It must not fill placeholder wording merely to complete the template.
- It must not guess whether a topic belongs in the stable library.

### 4. Delivery shape: template-first, validator later

- The primary authoring aid is a local canonical template:
  - `.github/skills/plan-creator/templates/topic-plan-template.md`
- The template lives inside the skill folder so it evolves with the skill.
- A validator may exist later in a separate follow-up topic, but no validator
  script is part of this first topic.

### 5. First rollout: review-ready only

- This topic produces a `review-ready` `plan-creator` skill only.
- Stable-library surfaces such as `README.md` and `VERSION` remain untouched in
  this topic.
- If `plan-creator` is later promoted into the stable library, that publish work
  belongs to a separate topic.

### 6. Required topic-plan contract content

`plan-creator` must require topic plans to include, at minimum:

- `Goal / Outcome`
- `Scope`
- `Locked Decisions`
- `Boundaries / Exclusions`
- `Status / Allowed Transitions`
- `Artifact Paths`
- `Implementation Steps`
- `Validation / Acceptance Checks`
- `Reviewer Handoff`
- `Post-merge / release actions`
- `Open questions / unresolved items`

Conditional rule:

- `Stable library metadata` appears only when the topic explicitly affects
  stable-library surfaces or declares deferred release timing.
- When the topic does **not** affect stable-library surfaces, the plan must say
  so explicitly rather than leaving the intent ambiguous.

## Boundaries / Exclusions

- Do not collapse planning responsibilities into creator or reviewer
  responsibilities.
- Do not treat `Artifact paths` as an informational appendix; they must remain
  an executable contract.
- Do not permit reviewer handoff to degrade into free-form Markdown when the
  workflow requires a machine-consumable JSON object.
- Do not bundle stable-library publish timing into an otherwise review-ready-only
  topic unless the topic explicitly exists to handle that publish work.
- Do not add repo-global helper files for planning when the skill-local template
  or references are sufficient.

## Status / Allowed Transitions

- **Current**: `pr-open`
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

- `approved` does **not** mean the topic may skip directly to publish work.
- After reviewer approval, the creator / main flow must first apply any
  required reviewer JSON `ADDRESS` feedback and complete the necessary
  revisions before Main Agent runs the Phase 4.5 planner contract alignment
  checkpoint defined by `plan/agent-handoff-workflow.md`.
- If Phase 4.5 finds drift in locked decisions, artifact paths, or other
  plan-level contract semantics, route the topic back to
  `creator-in-progress` before any publish work continues.
- Only after reviewer approval, required feedback application, and a passing
  Phase 4.5 checkpoint may Main Agent move the topic to `publish-in-progress`.

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/plan-creator/plan-creator.plan.md` | Planning actor | Repo-visible execution contract for this topic |
| Skill folder | `.github/skills/plan-creator/` | Creator | Root output location for the draft skill |
| Core skill contract | `.github/skills/plan-creator/SKILL.md` | Creator | Executable instruction contract |
| Detailed examples | `.github/skills/plan-creator/examples.md` | Creator | Positive and negative topic-plan authoring scenarios |
| Reference guidance | `.github/skills/plan-creator/reference.md` | Creator | Stable local rules for plan contracts, role boundaries, and stable-library branching |
| Validation checklist | `.github/skills/plan-creator/checklist.md` | Creator | Repeatable review and misuse-prevention checks for a higher-risk planning skill |
| Local template | `.github/skills/plan-creator/templates/topic-plan-template.md` | Creator | Canonical starting shape for repo topic plans |

Artifact path notes:

- This topic does **not** modify `README.md`, `VERSION`, or
  `.github/copilot-instructions.md`.
- `Stable library metadata` is intentionally absent because this topic is not a
  stable-library publish topic.
- The listed paths are an executable contract, not an informational appendix.
- If creator output, reviewer findings, or planner alignment reveals repo-visible
  changes outside these paths, treat that drift as a plan violation and route
  the topic back to `creator-in-progress` before continuing.

## Implementation Steps

### Creator Phase (after plan approval)

1. **Draft `SKILL.md`**
   - Define `plan-creator` as a single-purpose skill for repo-visible topic-plan
     authoring.
   - Make `Trigger / When to use` explicit:
     - use when a new repo topic needs a valid `plan/<topic>/<topic>.plan.md`
     - do not use when editing a finished plan in a tiny localized way
     - do not use for creator drafting, review, publish, or release execution
   - In `Process`, require:
     - identify whether the topic is review-ready-only or stable-library-affecting
     - lock scope and boundaries before drafting
     - enumerate exact artifact paths
     - use canonical transitions only
     - choose strict-stop-and-ask whenever required information is missing
   - Include concise positive and negative examples in `SKILL.md`.

2. **Draft `templates/topic-plan-template.md`**
   - Provide canonical section order for topic plans.
   - Mark which sections are always required and which are conditional.
   - Include explicit prompts for:
     - stable-library vs non-stable intent
     - role ownership
     - artifact-path exactness
     - reviewer JSON handoff
     - post-merge / release timing
   - Keep the template focused on structure and prompts; do not fill it with
     fake defaults or speculative content.

3. **Draft `reference.md`**
   - Explain the repository-specific meaning of each required topic-plan section.
   - Explain when `Stable library metadata` is required versus intentionally
     omitted.
   - Explain how to author `Artifact paths` as an executable contract.
   - Explain role boundaries among planning actor, creator, reviewer, and
     main agent.
   - Explain the strict-stop-and-ask policy and common failure signals.

4. **Draft `examples.md`**
   - Include at least:
     - one non-stable skill topic
     - one stable-library publish topic
     - one workflow-spec topic
     - one wording-only small topic
     - multiple anti-patterns
   - Anti-patterns must cover:
     - invalid transitions
     - mixed stable-library intent
     - missing or drifting artifact paths
     - wrong reviewer handoff format
     - wrong phase naming or timing
     - role-boundary confusion

5. **Draft `checklist.md`**
   - Add review-oriented checks for:
     - required sections present
     - stable / non-stable intent clearly declared
     - artifact paths exact and bounded
     - reviewer handoff machine-consumable
     - post-merge / release actions not mistimed
     - no creator / reviewer / main-agent responsibility mixing
   - Keep the checklist local to this higher-risk skill; do not generalize it
     into repo-global policy by itself.

### Reviewer Phase (after creator delivers review-ready)

1. Confirm the skill stays single-purpose: topic-plan authoring only.
2. Confirm the template and examples are strong enough to prevent the known
   workflow failure modes.
3. Confirm the checklist and reference guidance match the risk of a
   gate-shaping skill.
4. Confirm the skill remains repository-specific without becoming a generic
   project-planning assistant.
5. Confirm no stable-library surfaces were included in this first topic.

## Validation / Acceptance Checks

- `plan-creator` stays clearly separate from `agent-skill-creator`,
  `agent-skill-reviewer`, and Main Agent orchestration roles.
- The skill can prevent the known topic-plan failure modes before execution
  reaches creator / reviewer / publish phases.
- The template enforces canonical section order and conditional branching
  without generating fake content.
- The guidance explicitly distinguishes stable-library topics from non-stable
  topics.
- `Artifact paths` are treated as an executable contract, not a loose list.
- The reviewer handoff guidance remains machine-consumable JSON.
- The skill uses stronger validation material appropriate for a higher-risk
  planning / gate-shaping skill.
- This topic does not modify stable-library surfaces or introduce a validator
  script prematurely.

## Reviewer Handoff

**Fixed report format** (from `plan/agent-handoff-workflow.md` schema):

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
rationale inside the structured JSON fields so the handoff remains safely
machine-consumable.

## Post-merge / release actions

1. After merge, run the normal post-merge local sync flow for the working
   branch.
2. Do **not** update `README.md`, `VERSION`, `.github/copilot-instructions.md`,
   or release notes in this topic.
3. No repository release action is required for this topic.
4. Stable-library promotion for `plan-creator`, if desired later, is deferred to
   a separate publish-focused topic once this skill is proven review-ready.
5. This topic is terminal at `merged`.

## Open Questions / Unresolved Items

- None of the remaining questions block the first `review-ready` implementation.
- If `reference.md` later becomes too broad, decide whether to split it into
  `references/` under normal repo policy.
- If a validator is later justified, create it in a separate follow-up topic and
  keep it limited to structural / contract validation rather than substantive
  content generation.
