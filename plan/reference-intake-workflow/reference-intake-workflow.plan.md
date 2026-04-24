# reference-intake-workflow Topic Plan

## Goal / Outcome

Define and implement a formal, lightweight, repeatable 5-layer process for triaging, evaluating, and selectively translating ideas from external Agent Skills repositories into this repository's stable library, without ad-hoc copying or policy drift. When complete, the repository will have:
- a catalogued external reference collection at `other-project-examples/reference-agent-skills/`
- triage and intake guidelines for new external libraries
- a workflow that gates all external-idea adoption through the existing `creator -> reviewer -> publish -> release` cycle
- a maintenance checklist for ongoing reference evaluation

## Scope

### In scope

- Create `other-project-examples/reference-agent-skills/CATALOG.md` (registry of external references with metadata and triage status)
- Create `other-project-examples/reference-agent-skills/addyosmani/INTAKE.md` (triage decision for the existing addyosmani/agent-skills reference)
- Create `.github/guides/REFERENCE-INTAKE-PROCESS.md` (executable process documentation for future reference intake)
- Create `.github/guides/OTHER-PROJECT-EXAMPLES.md` (changelog of adopted external ideas with links to commits and PRs)
- Document the triage and translation decisions for addyosmani in the INTAKE.md (no implementation of creator/reviewer changes yet)

### Out of scope

- Implementing creator/reviewer validation rule changes themselves (that work belongs to a follow-up topic)
- Applying adopted ideas to local skills (pilot application is Phase 2 of a follow-up)
- Changing repository policy or templating beyond intake process documentation
- Creating new skills in this repository (this is a process/infrastructure topic)

## Locked Decisions

- This topic is **a process-only topic with no stable-library surfaces affecting README or VERSION**
- External references stay in `other-project-examples/` with sibling `INTAKE.md` decision files; they do not become merged into `.github/skills/`
- Triage decisions must be traceable (stored in `INTAKE.md`), not left in session context
- All external ideas, once adopted via triage, must flow through the standard `creator -> reviewer -> PR -> release` workflow, not be imported ad-hoc
- The intake process itself is documented in `.github/guides/`, where it can be referenced by future creators and reviewers
- The status of this topic does **not** require a release action; it terminates at `merged`

## Boundaries / Exclusions

- This topic defines **process and documentation**, not implementation of validation rule changes
- Do not modify `.github/skills/agent-skill-creator/` or `.github/skills/agent-skill-reviewer/` in this topic; those belong to a follow-up topic (Phase 2)
- Do not evaluate other external skill repositories in detail in this topic; INTAKE.md for addyosmani is the example to follow for future references
- Do not make decisions about which specific creator/reviewer rules to change; that belongs to the follow-up topic's planning

## Status / Allowed Transitions

- **Current**: `planned`
- **Execution model**: Follow the canonical `creator -> reviewer -> publish -> merge` path; this topic does not require a release action.
- **Allowed transitions**:
  - `planned` -> `creator-in-progress`
  - `creator-in-progress` -> `review-ready`
  - `review-ready` -> `reviewer-in-progress`
  - `reviewer-in-progress` -> `approved` or `needs-rework`
  - `needs-rework` -> `creator-in-progress`
  - `approved` -> `publish-in-progress`
  - `publish-in-progress` -> `pr-open`
  - `pr-open` -> `merged` or `needs-rework`
  - `merged` -> terminal (no release action)

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/reference-intake-workflow/reference-intake-workflow.plan.md` | Planning actor | Repo-visible execution contract for this topic |
| CATALOG | `other-project-examples/reference-agent-skills/CATALOG.md` | Creator | Index and registry of all external references with triage status |
| addyosmani INTAKE | `other-project-examples/reference-agent-skills/addyosmani/INTAKE.md` | Creator | Triage decision, translation checklist, and adoption roadmap for the addyosmani reference |
| Intake process guide | `.github/guides/REFERENCE-INTAKE-PROCESS.md` | Creator | Executable process documentation for evaluating and triaging future external references |
| Adoption changelog | `.github/guides/OTHER-PROJECT-EXAMPLES.md` | Creator | Changelog of adopted external ideas, linking to PRs and commits that implement them |

Artifact path notes:

- This topic **does not modify** `README.md`, `VERSION`, or `.github/copilot-instructions.md`
- All new artifacts are additions to the repository; no existing files are deleted
- The external-reference folder structure is preserved as-is; INTAKE.md is added as a sibling

## Implementation Steps

1. **Create CATALOG.md** with:
   - Index of external reference repositories (starting with addyosmani)
   - Metadata: author, source URL, license, discovery date, primary domain
   - Triage status for each (adopt, adapt, reject, monitor)
   - Quick lookup for future reference reviewers

2. **Create INTAKE.md for addyosmani** with:
   - Metadata section (author, source, license, focus area)
   - Triage questions (gaps addressed, pattern portability, license compatibility, improvement suggestions)
   - Decision: **ADOPT + ADAPT** (adopt the rigor of validation/lifecycle/red-flags; adapt format to local split-model)
   - Specific ideas to adopt (validation checklist richness, lifecycle framing, error-pattern focus, example quality enforcement)
   - Ideas to reject (monolithic SKILL.md model, single-file-only structure)
   - Translation tasks (linked to follow-up topic for creator/reviewer updates)

3. **Create REFERENCE-INTAKE-PROCESS.md** with:
   - 5-layer process explanation (storage, review, extraction, rollout, maintenance)
   - Triage question template (copy-friendly for future references)
   - Decision framework (ADOPT vs ADAPT vs REJECT vs MONITOR rationale)
   - Enforcement rule: all adopted ideas must go through creator/reviewer gate
   - Anti-patterns and what-not-to-do checklist
   - Maintenance and deprecation guidance

4. **Create OTHER-PROJECT-EXAMPLES.md** with:
   - Table template: Reference | Idea adopted | When (commit/PR) | Creator/reviewer change | Status
   - Instructions for future record-keeping
   - Quarterly refresh checklist

## Validation / Acceptance Checks

- [ ] All required artifact paths exist and are exact (not vague labels)
- [ ] CATALOG.md indexes the addyosmani reference with correct metadata and triage status
- [ ] INTAKE.md follows the triage template and includes adoption rationale
- [ ] REFERENCE-INTAKE-PROCESS.md is copy-friendly and can serve future external references
- [ ] OTHER-PROJECT-EXAMPLES.md is ready to receive the first adoption record (after follow-up topic merges)
- [ ] No artifacts contradict `.github/copilot-instructions.md` or `README.md` policy
- [ ] Reviewer can use INTAKE.md and REFERENCE-INTAKE-PROCESS.md to understand how future external references will be evaluated

## Reviewer Handoff

```json
{
  "verdict": "approved|needs-rework",
  "blocking_issues": [],
  "copilot_feedback_triage": {
    "ADDRESS": [
      "Are all artifact paths exact and role-labeled?",
      "Does INTAKE.md provide clear adoption rationale?",
      "Is REFERENCE-INTAKE-PROCESS.md reusable for future references?"
    ],
    "DISCUSS": [
      "Should we schedule quarterly reviews of MONITOR-status references?",
      "Does the triage template strike the right balance of structure vs. flexibility?"
    ],
    "SKIP": []
  }
}
```

## Post-merge / release actions

- **No repository release action is required** for this topic.
- After merge, the intake process is documented and ready for use by creator/reviewer roles.
- The follow-up topic (Phase 2) will implement creator/reviewer changes linked from INTAKE.md and will use the process defined here.

## Open Questions / Unresolved Items

- None blocking this plan. The triage decision for addyosmani is locked: **ADOPT + ADAPT** with specific ideas listed for follow-up.

---

## Topic Status Marker

- **Status**: `planned`
- **Last updated**: 2026-04-24
- **Next phase trigger**: Creator begins Phase 3 (implementation) when this plan is committed and approved.
