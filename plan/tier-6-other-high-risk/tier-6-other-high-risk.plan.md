# Tier 6 — Other High-Risk Skills Migration
## Schema v2 upgrade: 5 high-risk skills from legacy standard to creator/reviewer-approved

---

## Status / Allowed Transitions

**Current status**: `planned`

| From | To | Condition |
|---|---|---|
| `planned` | `creator-in-progress` | Plan reviewer returns `approved` |
| `creator-in-progress` | `review-ready` | Creator finishes the latest draft set |
| `review-ready` | `reviewer-in-progress` | Reviewer subagents launched |
| `reviewer-in-progress` | `needs-rework` | Any skill receives `needs-rework` |
| `reviewer-in-progress` | `approved` | All 5 skills receive `approved` |
| `needs-rework` | `creator-in-progress` | Creator addresses reviewer blockers |
| `approved` | `creator-in-progress` | Phase 4.5 planner contract alignment routes the topic back to creator if any approved draft drifts from locked contract |
| `approved` | `publish-in-progress` | Human approves commit + push (STOP POINT 1) |
| `publish-in-progress` | `pr-open` | PR created targeting `feature/skill-migration-v1` |
| `pr-open` | `needs-rework` | PR feedback requires creator revision |
| `pr-open` | `merged` | Human triggers STOP POINT 2 merge into `feature/skill-migration-v1` |
| `merged` | `terminal` | Post-merge cleanup complete |

---

## Goal / Outcome

Upgrade 5 high-risk non-Python/non-Git-workflow skills to schema v2 while preserving their existing responsibility, gating behavior, and downstream handoff contracts. All 5 skills must reach `agent-skill-reviewer` verdict `approved` before Tier 6 is considered complete.

**Target skills**:
1. `plan-creator`
2. `plan-reviewer`
3. `sense-env-scaffold`
4. `copilot-instructions-init`
5. `business-to-technical-translation`

---

## Boundaries / Exclusions

- Do not change the business responsibility of any target skill.
- Do not change repo workflow semantics or governance rules during this migration.
- Do not modify governance files outside the target skills themselves.
- Do not update `README.md`, `VERSION`, or `files/migration-tracker.md` in this topic branch.
- Do not upgrade Tier 5 or Tier 7 skills in this plan.

---

## Scope

### In scope
All 5 skills are inferred as **Mode A+** unless creator proves a Preservation Map is required.

### Out of scope
See Boundaries / Exclusions.

### Per-Skill Migration Parameters

| # | Skill | Mode | Inferred Complexity | Inferred Risk Profile | Preservation Notes |
|---|---|---|---|---|---|
| 1 | `plan-creator` | A+ | high | ambiguity_sensitive, multi_agent_handoff | Preserve canonical topic-plan contract, analysis-layer routing, and stable-library timing rules |
| 2 | `plan-reviewer` | A+ | high | ambiguity_sensitive, multi_agent_handoff | Preserve JSON-only verdict contract, contract-breaking focus, and review-basis requirements |
| 3 | `sense-env-scaffold` | A+ | medium | external_tooling | Preserve fixed CLI contract, exit-code meanings, manifest schema, and prototype-tooling boundary |
| 4 | `copilot-instructions-init` | A+ | high | ambiguity_sensitive, code_modification | Preserve hard-stop stale-fact gate, overwrite-choice gate, and target-file-only boundary |
| 5 | `business-to-technical-translation` | A+ | medium | ambiguity_sensitive | Preserve pessimistic translator posture, rollback-to-alignment rule, and no-implementation boundary |

---

## Locked Decisions

### D1: Execution Model
- Use per-skill creator -> reviewer loops.
- Review may run in parallel after drafts are ready.
- No strict runtime dependency exists between the five migrations; the coupling is conceptual, not file-level.

### D2: Preservation Map Triggers
Creator must emit a Preservation Map before Mode B rewrite if:
- workflow or output contracts are internally contradictory
- schema v2 supplementation would require silent redefinition of gates
- JSON-only, CLI, or overwrite-choice behavior cannot be preserved in Mode A+

### D3: Complexity & Risk Profile Inference

| Skill | Complexity | Reasoning | Risk Profile | Rationale |
|---|---|---|---|---|
| `plan-creator` | **high** | Writes repo-visible execution contracts with analysis-layer priority and stable-library timing decisions | ambiguity_sensitive, multi_agent_handoff | Small wording changes can misroute planning authority and downstream execution handoff |
| `plan-reviewer` | **high** | Returns machine-consumable plan verdicts that gate all later execution | ambiguity_sensitive, multi_agent_handoff | Wrong approval or malformed JSON can unblock invalid downstream execution |
| `sense-env-scaffold` | **medium** | Executes a fixed CLI contract with multi-exit-code behavior and manifest outputs | external_tooling | Tool invocation, exit-code interpretation, and manifest path handling depend on external runtime behavior |
| `copilot-instructions-init` | **high** | Generates or refreshes a governed file through stale-fact and overwrite gates | ambiguity_sensitive, code_modification | Wrong synthesis or missed hard stop can overwrite instructions or encode false project truth |
| `business-to-technical-translation` | **medium** | Multi-path translation with feasibility conflicts, rollback triggers, and architecture-compliance checks | ambiguity_sensitive | Missing or vague baseline interpretation materially changes the technical spec and rollback recommendation |

### D4: YAML / Body Consistency Check
Creator must ensure YAML metadata and body contracts stay aligned for all five skills.

### D5: High-Risk Guardrails
For `plan-creator`, `plan-reviewer`, and `copilot-instructions-init`, creator must preserve:
- explicit hard-stop conditions
- output-shape contracts
- boundary rules that prevent silent fallback or silent merge

If any of those cannot be preserved in Mode A+, creator must stop and emit a Preservation Map before rewriting.

---

## Artifact Paths

| Artifact | Path | Owner | Role |
|---|---|---|---|
| tier-6 plan | `plan/tier-6-other-high-risk/tier-6-other-high-risk.plan.md` | Planning actor | Repo-visible execution contract for this topic |
| plan-creator | `.github/skills/plan-creator/SKILL.md` | creator | schema v2 upgrade |
| plan-creator reference overview | `.github/skills/plan-creator/reference.md` | creator | focused overview retained as the required companion file after split-reference repair |
| plan-creator section reference | `.github/skills/plan-creator/references/required-section-meaning.md` | creator | split reference for required topic-plan section semantics |
| plan-creator stable-library reference | `.github/skills/plan-creator/references/stable-library-rule.md` | creator | split reference for stable-library metadata and timing rules |
| plan-creator artifact-path reference | `.github/skills/plan-creator/references/artifact-path-rule.md` | creator | split reference for exact artifact-path contract rules |
| plan-creator role-boundary reference | `.github/skills/plan-creator/references/role-boundary-rule.md` | creator | split reference for planning / creator / reviewer / Main Agent ownership rules |
| plan-creator stop-and-ask reference | `.github/skills/plan-creator/references/stop-and-ask-triggers.md` | creator | split reference for stop-and-ask routing triggers |
| plan-creator template reference | `.github/skills/plan-creator/references/template-usage-rule.md` | creator | split reference for canonical template usage rules |
| plan-reviewer | `.github/skills/plan-reviewer/SKILL.md` | creator | schema v2 upgrade |
| sense-env-scaffold | `.github/skills/sense-env-scaffold/SKILL.md` | creator | schema v2 upgrade |
| copilot-instructions-init | `.github/skills/copilot-instructions-init/SKILL.md` | creator | schema v2 upgrade |
| business-to-technical-translation | `.github/skills/business-to-technical-translation/SKILL.md` | creator | schema v2 upgrade |

**Stable-library surfaces not touched in this topic**: `README.md`, `VERSION`, and `files/migration-tracker.md` are deferred until merge-complete follow-up on the integration branch.

**Artifact-path guardrail**: this topic remains locked to `SKILL.md`-only edits for `plan-reviewer`, `sense-env-scaffold`, `copilot-instructions-init`, and `business-to-technical-translation`. `plan-creator` alone may also edit the exact companion-file paths listed above to repair the split-reference blocker raised by independent review. No other target skill may broaden beyond its listed paths without another plan repair.

---

## Public Contract

When this plan is complete:
- All 5 skills have schema v2 YAML governance metadata.
- Required complexity-gated sections are present and reviewer-approved.
- Existing hard stops, output-shape contracts, and no-fallback boundaries remain intact.
- No governance-file edits outside the target skill folders are introduced.

---

## Stable library metadata

- Stable-library entry in this topic: **no**
- `README.md` update in this topic: **no**
- `VERSION` update in this topic: **no**
- `files/migration-tracker.md` update in this topic: **no**
- Timing: not applicable in this topic; any later stable-library or integration-branch maintenance happens outside this plan
- Release action in this topic: none

---

## Failure Handling

### Missing Context
- If creator cannot infer complexity or risk without guessing, mark the draft INCOMPLETE and list the missing signals.

### Ambiguous Requirement
- If creator detects contradiction between YAML inference and body behavior, stop and emit a Preservation Map rather than smoothing over the conflict.

### Reviewer Rejection
- Any `needs-rework` verdict routes the affected skill back to creator without reopening already-approved skills unless shared contract drift is discovered.
- If the required rework would edit a path outside the currently locked `Artifact Paths`, repair this plan first, re-run independent plan review, and only then return the affected skill to creator.

### Risk Gate Failures
- If a high-risk contract (JSON-only verdict, stale-fact hard stop, overwrite-choice gate, or canonical plan contract) cannot be preserved in Mode A+, mark the skill BLOCKED and require human decision before rewriting.

---

## Validation / Acceptance Checks

Validation via creator/reviewer gates only; no new tests added by this topic.

```bash
# Verify YAML metadata fields exist
cd .github/skills/<skill-name>
grep -E '^(complexity|risk_profile|inputs|outputs|use_when|do_not_use_when):' SKILL.md

# Verify Validation and Failure Handling sections exist
grep -E '^# (Validation|Failure Handling)$' SKILL.md

# Verify at least one positive and one negative example
grep -E '^- \*\*(Positive|Negative)\*\*:' SKILL.md

# For plan-reviewer: verify JSON-only output contract remains explicit
grep -E 'JSON|machine-consumable|approved|needs-rework' .github/skills/plan-reviewer/SKILL.md | head -10
```

---

## Inputs

- Existing `SKILL.md` files for all 5 target skills
- `agent-skill-creator/folder-contract.md`
- `agent-skill-reviewer/review-checklist.md`
- This plan

---

## Implementation Steps

1. Plan reviewer approves this plan.
2. Creator drafts `plan-creator` and `plan-reviewer`.
   - If reviewer rejects `plan-creator` for oversized multi-topic `reference.md`, creator may split that file into the exact `references/*.md` paths locked above while keeping `reference.md` as the focused companion overview.
3. Creator drafts `sense-env-scaffold`, `copilot-instructions-init`, and `business-to-technical-translation`.
4. Reviewer subagents evaluate each draft independently.
5. Creator addresses any `needs-rework` findings.
6. STOP POINT 1 -> human approves commit + push.
7. PR opens against `feature/skill-migration-v1`.
8. STOP POINT 2 -> human merges PR.

---

## Post-merge / Release Actions

No release action in this topic.

After merge into `feature/skill-migration-v1`:
- delete remote and local branch `migrate/tier-6-other-high-risk`
- fast-forward sync the integration branch
- update `files/migration-tracker.md` on the integration branch

`README.md` and `VERSION` remain deferred to the later maintainer-controlled release step.

---

## Open Questions / Unresolved Items

None.

---

## Reviewer Handoff

```json
{
  "verdict": "approved|needs-rework",
  "blocking_issues": [],
  "copilot_feedback_triage": { "ADDRESS": [], "DISCUSS": [], "SKIP": [] }
}
```
