# reference-intake-workflow Topic Plan

## Goal / Outcome

Define and implement a formal, lightweight, repeatable 5-layer process for triaging, evaluating, and selectively translating ideas from external Agent Skills repositories into this repository's stable library, without ad-hoc copying or policy drift. When complete, the repository will have:
- a catalogued external reference collection at `other-project-examples/reference-agent-skills/`
- triage and intake guidelines for new external libraries
- a workflow that gates all external-idea adoption through the existing `creator -> reviewer -> publish -> release` cycle
- a maintenance checklist for ongoing reference evaluation

## Scope

### In scope

- Create `.github/guides/REFERENCE-INTAKE-PROCESS.md` (executable process documentation for future reference intake)
- Create `.github/guides/OTHER-PROJECT-EXAMPLES.md` (changelog of adopted external ideas with links to commits and PRs)
- Document the decision to **NOT track external reference files in the repository** (other-project-examples/ contains sensitive info, other projects' code, company data)
- The intake workflow will be documented for local use; triage decisions will be recorded locally but not committed to the repo

### Out of scope

- Committing `CATALOG.md` or `INTAKE.md` to the repository (user policy: other-project-examples/ is not to be committed)
- Implementing creator/reviewer validation rule changes themselves (that work belongs to a follow-up topic)
- Applying adopted ideas to local skills (pilot application is Phase 2 of a follow-up)
- Changing repository policy or templating beyond intake process documentation
- Creating new skills in this repository (this is a process/infrastructure topic)

## Locked Decisions

- This topic is **a process-only topic with no stable-library surfaces affecting README or VERSION**
- External references stay in `other-project-examples/` (local use only, **NOT committed to repo** — contains sensitive info, other projects' code, company data)
- `CATALOG.md` and `INTAKE.md` files will be used locally for decision tracking; they will NOT be committed
- Intake process documentation goes in `.github/guides/` and IS committed
- Triage decisions and local copies of INTAKE.md are for team reference only, stored outside version control
- All external ideas, once adopted via triage, must flow through the standard `creator -> reviewer -> PR -> release` workflow
- The status of this topic does **not** require a release action; it terminates at `merged`

## Boundaries / Exclusions

- This topic defines **process and documentation**, not implementation of validation rule changes
- Do not modify `.github/skills/agent-skill-creator/` or `.github/skills/agent-skill-reviewer/` in this topic; those belong to a follow-up topic (Phase 2)
- Do not evaluate other external skill repositories in detail in this topic; INTAKE.md for addyosmani is the example to follow for future references
- Do not make decisions about which specific creator/reviewer rules to change; that belongs to the follow-up topic's planning

## Status / Allowed Transitions

- **Current**: `review-ready`
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
| Intake process guide | `.github/guides/REFERENCE-INTAKE-PROCESS.md` | Creator | Executable process documentation for evaluating and triaging future external references |
| Adoption changelog | `.github/guides/OTHER-PROJECT-EXAMPLES.md` | Creator | Changelog of adopted external ideas, linking to PRs and commits that implement them |

Artifact path notes:

- This topic **does not modify** `README.md`, `VERSION`, or `.github/copilot-instructions.md`
- This topic **does NOT commit CATALOG.md or INTAKE.md** (these remain local; other-project-examples/ contains sensitive information)
- All new committed artifacts are additions to `.github/guides/`; no existing files are deleted
- The external-reference folder structure remains excluded from version control (.gitignore)

## Implementation Steps

1. **Create REFERENCE-INTAKE-PROCESS.md** (`.github/guides/`) with:
   - 5-layer process explanation (storage, review, extraction, rollout, maintenance)
   - Triage question template (copy-friendly for future references)
   - Decision framework (ADOPT vs ADAPT vs REJECT vs MONITOR rationale)
   - Enforcement rule: all adopted ideas must go through creator/reviewer gate
   - Anti-patterns and what-not-to-do checklist
   - Maintenance and deprecation guidance

2. **Create OTHER-PROJECT-EXAMPLES.md** (`.github/guides/`) with:
   - Table template: Reference | Idea adopted | When (commit/PR) | Creator/reviewer change | Status
   - Instructions for future record-keeping
   - Quarterly refresh checklist

3. **Create local CATALOG.md & INTAKE.md** (in other-project-examples/, NOT committed):
   - CATALOG: Index of external references with metadata and triage status
   - INTAKE (addyosmani): Triage decision, translation checklist, adoption roadmap
   - These files support local decision-making but are excluded from version control

4. **Document the policy**: Update OTHER-PROJECT-EXAMPLES.md to note:
   - External references are NOT committed to the repo
   - CATALOG.md and INTAKE.md are used locally for tracking
   - The published process guide (REFERENCE-INTAKE-PROCESS.md) explains the workflow
   - Future adoptions will be recorded in OTHER-PROJECT-EXAMPLES.md with links to PRs/commits

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

- **Status**: `review-ready` ← Phase 3 (Creator implementation) complete
- **Last updated**: 2026-04-24
- **Implementation commits**:
  - `bdc3028`: plan(reference-intake-workflow): initial topic plan
  - `3cf3c89`: feat(reference-intake): implement 5-layer external reference intake workflow
- **Next phase trigger**: Reviewer evaluates Phase 4 (Reviewer pass) per agent-skill-reviewer
