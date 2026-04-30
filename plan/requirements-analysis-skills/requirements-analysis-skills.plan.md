---
name: requirements-analysis-skills
status: planned
---

# Requirements Analysis Skills

Create two complementary Agent Skills to strengthen requirement analysis discipline across the repository: `business-intent-alignment` (Socratic interviewer perspective) and `business-to-technical-translation` (pessimistic implementer perspective), plus integrate the `analysis/` fact layer into `plan-creator` workflow.

## Goal / Outcome

- Two new stable Agent Skills that enforce measurability in requirements and feasibility in technical translation
- `analysis/<topic>/requirements.md` and `analysis/<topic>/technical-spec.md` become recognizable input artifacts in the repository
- `plan-creator` Skill updated to consume, validate, and route on these analysis artifacts with tiered validation and soft-gate semantics
- Both new Skills pass `agent-skill-reviewer` with `approved` verdict
- README and VERSION updated; no blocking issues remain

## Scope

- **In scope**:
  - `.github/skills/business-intent-alignment/` — Skill folder with SKILL.md, reference.md, examples.md, checklist.md
  - `.github/skills/business-to-technical-translation/` — Skill folder with SKILL.md, reference.md, examples.md, checklist.md
  - `.github/skills/plan-creator/SKILL.md` — update to add analysis layer consumption rules, tiered validation, and soft-gate semantics
  - `README.md` — add two new Skill rows to "Current skills" table
  - `VERSION` — bump MINOR (two stable Skills added)

- **Out of scope**:
  - Creating or populating `analysis/<topic>/` files in this topic
  - Creating sample `analysis/example-topic/` with real content (guidance only)
  - Changing the `plan/agent-handoff-workflow.md` canonical workflow
  - Creating additional Skills beyond the two required
  - Retrofitting existing topics into the analysis layer

## Locked Decisions

1. **Topic is stable-library-affecting**: Both new Skills are intended for the stable library immediately, not as review-ready-only drafts. They will be added to README and VERSION on approval.

2. **Single topic plan**: This work is one topic covering requirement definition, creator drafting, independent review, plan-creator integration, README/VERSION updates, and final verification under the canonical repository workflow.

3. **Perspective constraints are hard contracts**:
   - `business-intent-alignment` must embody "Socratic interviewer" and extreme-boundary checking; output must be measurement-capable
   - `business-to-technical-translation` must embody "pessimist implementer" and feasibility self-check; must detect and signal architectural conflicts
   - Both must maintain rational, structure-heavy, emotionless-logic tone
   - These are not optional style suggestions; they must appear in examples.md and checklist.md

4. **Analysis layer is soft-gated fact layer**:
   - `plan-creator` does not hard-block on missing `analysis/` files, but must emit explicit semantic warnings
   - When `analysis/<topic>/requirements.md` and `analysis/<topic>/technical-spec.md` are both present, `plan-creator` enters "strict mode" and maps output plan 100% to technical-spec
   - Analysis file content has priority over conversation-time instructions unless Human explicitly says `override`

5. **Review-ready first, then approve**:
   - Creator drafts both Skills using `agent-skill-creator`
   - Independent reviewer must review each using `agent-skill-reviewer`
   - Rework cycle continues until both return `approved`

## Boundaries / Exclusions

- Do not implement user-facing applications or example projects in `analysis/`
- Do not change the `plan/` folder's execution-contract semantics; `analysis/` is a parallel fact layer, not part of plan schemas
- Do not modify existing Skill folder structures outside of `plan-creator`
- Do not approve either new Skill if examples or checklists do not concretely demonstrate the Socratic and pessimist perspectives, not just mention them
- Creator role cannot self-approve; reviewer role cannot generate final implementation

## Status / Allowed Transitions

- **Current**: `planned`
- **Execution model**: Standard creator → reviewer → publish → merge path per `plan/agent-handoff-workflow.md` phases 1–10
- **Allowed transitions**:
  - `planned` → `creator-in-progress`
  - `creator-in-progress` → `review-ready`
  - `review-ready` → `reviewer-in-progress`
  - `reviewer-in-progress` → `approved`
  - `reviewer-in-progress` → `needs-rework`
  - `needs-rework` → `creator-in-progress`
  - `approved` → `creator-in-progress`
  - `approved` → `publish-in-progress`
  - `publish-in-progress` → `pr-open`
  - `publish-in-progress` → `merged`
  - `pr-open` → `needs-rework`
  - `pr-open` → `merged`
  - `merged` → terminal

- **Routing notes**:
  - Use the standard Phase 4.5 planner-contract-alignment rule explicitly: creator may apply required reviewer fixes, then Main Agent runs planner contract alignment and decides whether the topic returns to `creator-in-progress` or moves to `publish-in-progress`.
  - Publish staging includes only the exact artifact paths listed below.
  - Do not use broad staging like `git add -A` or `git add .`; stage only allowed artifact paths
  - After manual merge at STOP POINT 2, stop completely and resume only on explicit human message

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/requirements-analysis-skills/requirements-analysis-skills.plan.md` | Planning actor | Repo-visible execution contract for this topic |
| First Skill contract | `.github/skills/business-intent-alignment/SKILL.md` | Creator | Socratic interviewer Skill; active requirement baseline construction |
| First Skill reference | `.github/skills/business-intent-alignment/reference.md` | Creator | Stable guidance for requirements baseline, challenge patterns, and boundaries |
| First Skill examples | `.github/skills/business-intent-alignment/examples.md` | Creator | Positive and negative examples showing questioning and extreme-boundary checks |
| First Skill checklist | `.github/skills/business-intent-alignment/checklist.md` | Creator | Repeatable validation for measurability, contradiction detection, and trigger clarity |
| Second Skill contract | `.github/skills/business-to-technical-translation/SKILL.md` | Creator | Pessimist implementer Skill; technical feasibility gating |
| Second Skill reference | `.github/skills/business-to-technical-translation/reference.md` | Creator | Stable guidance for feasibility checks, architecture compliance, and rollback triggers |
| Second Skill examples | `.github/skills/business-to-technical-translation/examples.md` | Creator | Positive and negative examples showing cost-of-realization analysis and rollback cases |
| Second Skill checklist | `.github/skills/business-to-technical-translation/checklist.md` | Creator | Repeatable validation for feasibility, architecture fit, and contradiction handling |
| plan-creator integration | `.github/skills/plan-creator/SKILL.md` | Creator | Add analysis-layer consumption rules, tiered validation, soft-gate semantics, and strict-mode mapping contract |
| README update | `README.md` | Main Agent | Add two new Skills to "Current skills" table with descriptions |
| Version update | `VERSION` | Main Agent | Bump MINOR version (SemVer: two stable Skills added) |

Artifact path notes:

- This topic modifies `README.md` and `VERSION`.
- This topic does not modify `.github/copilot-instructions.md`.
- Treat the listed paths as an executable contract; if later work drifts outside them, stop and revise the topic plan before continuing.

## Stable library metadata

- **README row**: Add two rows to the "Current skills" table:
  - insert `business-intent-alignment` before `copilot-instructions-init`
  - insert `business-to-technical-translation` immediately after `business-intent-alignment`
  - `business-intent-alignment` | Collects and aligns business requirements, applying Socratic questioning and extreme-boundary checking to ensure measurable, contradiction-free intent baseline
  - `business-to-technical-translation` | Translates requirements to technical specification, conducting feasibility checks and architecture compliance verification; surfaces conflicts and cost-of-realization warnings

- **VERSION bump**: MINOR (SemVer: two new stable Skills + plan-creator enhancement = backward-compatible capability expansion)
  - Example: if current version is `1.2.3`, bump to `1.3.0`

- **Timing**: Changes happen at `publish-in-progress` phase
  - README and VERSION are included in PR and merged together with Skill folders

- **Rationale**: Both new Skills immediately improve requirement discipline and should be discoverable in README upon release

## Implementation Steps

1. **Requirement definition**
   - Draft complete requirement specification for `business-intent-alignment` (perspective: Socratic interviewer, extreme-boundary checks, measurability contract)
   - Draft complete requirement specification for `business-to-technical-translation` (perspective: pessimist implementer, feasibility checks, architecture compliance contract)

2. **Skill drafting**
   - Use `agent-skill-creator` to produce `.github/skills/business-intent-alignment/` with SKILL.md, reference.md, examples.md, checklist.md
   - Use `agent-skill-creator` to produce `.github/skills/business-to-technical-translation/` with SKILL.md, reference.md, examples.md, checklist.md
   - Ensure examples and checklists concretely demonstrate Socratic questioning and pessimist feasibility checks, not just describe them
   - Mark both drafts as "review-ready"

3. **Independent review and rework**
   - Use `agent-skill-reviewer` to review each Skill against repository rules
   - Verify: single responsibility, portability, independence, explicit trigger clarity, adequate examples (including success and failure paths), medium-risk validation present
   - Verify: examples show Socratic interviewer / pessimist implementer perspectives in action, not as flavor text
   - If `needs-rework` returned, apply feedback and resubmit; iterate until both return `approved`

4. **plan-creator integration**
   - Update `.github/skills/plan-creator/SKILL.md`:
     - Add "Pre-check" or "Inputs" section describing analysis-layer consumption
     - Document tiered validation: strict mode when both `analysis/<topic>/requirements.md` and `analysis/<topic>/technical-spec.md` exist
     - Document semantic warnings if files missing
     - Document override semantics (analysis files have priority unless Human explicitly says override)

5. **Creator completion boundary**
   - Verify all Skill files present and complete
   - Verify `plan-creator/SKILL.md` changes do not break existing functionality
   - Stop creator-side implementation at the review-ready / approved artifact boundary
   - Leave README/VERSION handling, staging, and PR preparation to Main Agent during `publish-in-progress` per `Stable library metadata`

## Validation / Acceptance Checks

1. ✅ Both Skills pass `agent-skill-reviewer` with `approved` verdict
2. ✅ Each Skill folder contains SKILL.md, reference.md, examples.md, checklist.md (or explicit statement of why optional file is omitted)
3. ✅ Examples in both Skills concretely demonstrate Socratic questioning (business-intent-alignment) and feasibility checking (business-to-technical-translation), not just describe them
4. ✅ `business-intent-alignment` examples include extreme-boundary scenarios (offline, wrong user role, process interruption, etc.)
5. ✅ `business-to-technical-translation` examples include architecture-conflict detection, cost-of-realization warnings, and rollback-to-alignment scenarios
6. ✅ Both Skills maintain rational, structure-heavy, emotionless-logic tone throughout
7. ✅ `plan-creator/SKILL.md` section on analysis layer is present, clear, and includes all three new rules: tiered validation, semantic warnings, override semantics
8. ✅ README.md "Current skills" table includes two new rows with correct descriptions
9. ✅ VERSION file bumped to next MINOR version (e.g., 1.2.3 → 1.3.0)
10. ✅ All artifact paths match the listed table exactly; no stray edits outside allowed paths
11. ✅ Reviewer handoff JSON is present and valid (see below)

## Reviewer Handoff

```json
{
  "verdict": "approved|needs-rework",
  "blocking_issues": [
    {
      "issue": "Description of a contract-breaking problem",
      "file": "Exact path where the issue exists",
      "fix": "Specific action required to resolve"
    }
  ],
  "copilot_feedback_triage": {
    "ADDRESS": [
      {
        "comment": "Required change or missing element",
        "location": "Exact path or section reference",
        "why": "Rationale for why this must be addressed"
      }
    ],
    "DISCUSS": [
      {
        "comment": "Optional improvement or discussion point",
        "optional": true,
        "why": "Rationale for why this is worth discussing"
      }
    ],
    "SKIP": [
      {
        "comment": "Feedback item that is not applicable",
        "why": "Explanation of why it does not apply to this topic"
      }
    ]
  }
}
```

## Post-merge / release actions

- After merge, use the standard post-merge local sync flow when a human explicitly resumes after STOP POINT 2.
- No separate repository release action is required for this topic because stable-library files are updated at `publish-in-progress`, not deferred to Phase 10.
- Both Skills are available in the stable library once the merged changes land on the main branch.

## Open Questions / Unresolved Items

None. Scope, boundaries, artifact paths, stable-library intent, and role ownership are all locked and explicit.
