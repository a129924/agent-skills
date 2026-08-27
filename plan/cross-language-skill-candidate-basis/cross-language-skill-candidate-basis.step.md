---
topic: cross-language-skill-candidate-basis
status: planned
created: 2026-08-27
---

# Cross-Language Skill Candidate Basis — Progression

## Workflow Stages

- [X] planned
- [X] creator-in-progress
- [X] review-ready
- [X] reviewer-in-progress
- [X] approved
- [ ] needs-rework
- [X] publish-in-progress
- [ ] pr-open
- [ ] merged

## Actionable Steps

### planned

- [X] Create the topic plan with explicit non-stable intent, read-only input
  set, exact final write set, no-modify, and no-delete boundaries.
- [X] Create this progression artifact because the topic requires Plan-Creator,
  Plan-Reviewer, Implementer, Reviewer, Main Agent, and human handoffs.
- [X] Lock the four groups and 11 candidates; do not add skills during this
  topic.
- [X] Plan-Reviewer independently verifies this plan and progression artifact
  against `AGENTS.md`, `plan/agent-handoff-workflow.md`, and
  `plan/topic-plan-contract.md`.
- [X] Plan-Reviewer creates the listed review log only to record its routing
  verdict, then returns the canonical JSON handoff. This is a pre-execution
  validation gate within `planned`, not a workflow stage; only an `approved`
  verdict permits `planned` -> `creator-in-progress`.

### creator-in-progress

- [X] Implementer began after the approved Plan-Reviewer verdict.
- [X] Read the locked evidence set and created only
  `docs/agent-skills-convergence/cross-language-candidate-basis.md`.
- [X] Recorded all 11 candidates once, preserving the generic-core plus
  language-appendix model and labelling absent Swift/TypeScript evidence.

### review-ready

- [X] Implementer verified the locked write set and handed the
  candidate-basis document to an independent Reviewer.

### reviewer-in-progress

- [X] Reviewer assessed completeness, evidence discipline, candidate count,
  language-boundary honesty, and path/scope alignment.

### approved

- [X] Main Agent completed Phase 4.5 plan-contract alignment; the approved
  candidate-basis document remains within the locked write boundary.

### publish-in-progress

- [X] Publish handoff is authorized after independent Reviewer approval.
- [ ] Main Agent validates and stages only the exact topic artifact paths, then
  commits, pushes, and opens the draft pull request.
  routing.

### needs-rework

- [ ] Route bounded findings to Implementer; do not change the candidate set,
  create a language appendix, or alter existing topic artifacts.

### publish-in-progress

- [ ] Main Agent validates and stages only the exact topic artifact paths, then
  waits for STOP POINT 1 human authorization before commit, push, and draft PR.

### pr-open

- [ ] Stop at human review after draft PR creation; do not merge, release, tag,
  or poll for merge completion.

### merged

- [ ] STOP POINT 2: only a new explicit human resume may initiate post-merge
  local sync and creation of the topic close summary.

## Handoff / Gate Notes

- Optional analysis inputs are absent. This plan contains the required semantic
  warning; no actor may create, regenerate, or infer an analysis layer in this
  topic.
- Existing Phase 1 artifacts and the current repository positioning topic are
  read-only evidence. They are not part of this topic's write set.
- This is a non-stable documentation/planning topic: `README.md`, `VERSION`,
  `skills/**`, `.github/**`, and `.codex/**` are prohibited writes.
- Current canonical state: `planned`. Plan-Reviewer approval is a required
  independent pre-execution validation gate before Implementer work; it is not
  an additional workflow state. The plan-review result must be recorded in the
  exact review-log path because it controls routing.
- Swift and TypeScript entries are future-validation requirements or blockers,
  never claims of verified target-project behavior.
- Plan-Reviewer approval is recorded in the topic review log; Implementer work
  is complete and the Reviewer verdict is `approved`.
- Current canonical state: `publish-in-progress`.
- Next actor: Main Agent (publisher) to create the approved topic commit,
  push it, and open a draft pull request for human review.
