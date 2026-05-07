# Tier 7 — Other Low-Risk Skills Migration
## Schema v2 upgrade: 2 lower-priority skills from legacy standard to creator/reviewer-approved

---

## Status / Allowed Transitions

**Workflow entry condition**: this topic plan enters `planned` only after the reviewed file is committed. Until that commit exists, creator work and downstream publish routing must not start.

**Execution model**: follow the canonical creator -> reviewer -> publish -> merge path for this topic; stable-library handling is out of scope here.

| From | To | Condition |
|---|---|---|
| `planned` | `creator-in-progress` | Plan reviewer returns `approved` |
| `creator-in-progress` | `review-ready` | Creator finishes the latest draft set |
| `review-ready` | `reviewer-in-progress` | Reviewer subagents launched |
| `reviewer-in-progress` | `needs-rework` | Any skill receives `needs-rework` |
| `reviewer-in-progress` | `approved` | All 2 skills receive `approved` |
| `needs-rework` | `creator-in-progress` | Creator addresses reviewer blockers |
| `approved` | `creator-in-progress` | Planner-alignment or review feedback requires creator follow-up before publish |
| `approved` | `publish-in-progress` | Planner contract alignment passes and stable-library handling remains out of scope |
| `publish-in-progress` | `pr-open` | PR created targeting `feature/skill-migration-v1` |
| `pr-open` | `needs-rework` | PR feedback requires creator revision |
| `pr-open` | `merged` | Human triggers STOP POINT 2 merge into `feature/skill-migration-v1` |
| `merged` | `terminal` | Post-merge cleanup complete |

---

## Goal / Outcome

Upgrade `business-intent-alignment` and `plan-step-tracker` to schema v2 while preserving their existing baseline-alignment and step-querying behavior contracts. Both skills must reach `agent-skill-reviewer` verdict `approved` before Tier 7 is considered complete.

---

## Boundaries / Exclusions

- Do not redefine either skill's business responsibility.
- Do not change the Socratic alignment contract in `business-intent-alignment`.
- Do not change the CLI behavior or blocking semantics in `plan-step-tracker`.
- Do not modify governance files (`agent-skill-creator/`, `agent-skill-reviewer/`, `agent-skill-template/`).
- Do not update `README.md`, `VERSION`, or `files/migration-tracker.md` in this topic branch.

---

## Scope

### In scope
Both skills are inferred as **Mode A+** unless creator proves a Preservation Map is required.

### Out of scope
See Boundaries / Exclusions.

### Per-Skill Migration Parameters

| # | Skill | Mode | Inferred Complexity | Inferred Risk Profile | Preservation Notes |
|---|---|---|---|---|---|
| 1 | `business-intent-alignment` | A+ | medium | ambiguity_sensitive | Preserve contradiction surfacing, extreme-boundary checks, and no-technical-solutioning boundary |
| 2 | `plan-step-tracker` | A+ | medium | external_tooling | Preserve CLI command contract, exit-code blocking behavior, and read-only boundary |

---

## Locked Decisions

### D1: Execution Model
- Per-skill creator -> reviewer loop.
- Both skills may be drafted and reviewed in parallel.

### D2: Preservation Map Triggers
Creator must emit a Preservation Map before Mode B rewrite if:
- schema v2 supplementation would force contract drift
- `plan-step-tracker` CLI or exit-code semantics cannot be preserved in Mode A+
- `business-intent-alignment` measurability / contradiction logic cannot be preserved cleanly

### D3: Complexity & Risk Profile Inference

| Skill | Complexity | Reasoning | Risk Profile | Rationale |
|---|---|---|---|---|
| `business-intent-alignment` | **medium** | Multi-path questioning flow with contradiction forcing, measurability rewrite, and freeze criteria | ambiguity_sensitive | Missing or vague business context materially changes the frozen requirements baseline |
| `plan-step-tracker` | **medium** | Queries plan step files through a Python CLI and returns blocking signals through exit codes | external_tooling | The skill depends on command execution and correct exit-code interpretation for workflow blocking behavior |

### D4: YAML / Body Consistency Check
Creator must ensure YAML metadata aligns with body behavior for both skills.

---

## Artifact Paths

| Artifact | Path | Owner | Role |
|---|---|---|---|
| tier-7 plan | `plan/tier-7-other-low-risk/tier-7-other-low-risk.plan.md` | Planning actor | Repo-visible execution contract for this topic |
| business-intent-alignment | `.github/skills/business-intent-alignment/SKILL.md` | creator | schema v2 upgrade |
| plan-step-tracker | `.github/skills/plan-step-tracker/SKILL.md` | creator | schema v2 upgrade |
| plan-step-tracker reference | `.github/skills/plan-step-tracker/reference.md` | creator | preserved CLI contract and fallback guidance |

**Artifact path notes**:
- This topic does **not** modify `README.md`, `VERSION`, or `files/migration-tracker.md`.
- Stable-library metadata is intentionally absent because this is not a stable-library topic.
- Any later integration-branch housekeeping outside these paths is outside this topic and must not be folded into this plan.

---

## Public Contract

When this plan is complete:
- Both skills have schema v2 YAML governance metadata.
- Required complexity-gated sections are present and reviewer-approved.
- Existing measurable-baseline and blocking-query semantics remain intact.
- No file outside the two target skill folders and this plan is changed in the topic branch.

---

## Failure Handling

### Missing Context
- If creator cannot infer complexity or risk without guessing, mark the draft INCOMPLETE and list the missing signals.

### Ambiguous Requirement
- If creator finds contradictions that cannot be supplemented safely, stop and emit a Preservation Map before rewriting.

### Reviewer Rejection
- Any `needs-rework` verdict routes the affected skill back to creator without reopening already-approved work unless shared drift is found.

---

## Validation / Acceptance Checks

Validation via creator/reviewer gates only; no new tests added by this topic.

```bash
# Verify YAML metadata fields exist for business-intent-alignment
grep -E '^(complexity|risk_profile|inputs|outputs|use_when|do_not_use_when):' \
  .github/skills/business-intent-alignment/SKILL.md

# Verify required sections for business-intent-alignment
grep -E '^# (Validation|Boundaries|Local references)$' \
  .github/skills/business-intent-alignment/SKILL.md
grep -E '^- (Positive|Negative):' \
  .github/skills/business-intent-alignment/SKILL.md

# Verify YAML metadata fields exist for plan-step-tracker
grep -E '^(complexity|risk_profile|inputs|outputs|use_when|do_not_use_when):' \
  .github/skills/plan-step-tracker/SKILL.md

# Verify required sections for plan-step-tracker
grep -E '^# (Verification|Boundaries|Local references)$' \
  .github/skills/plan-step-tracker/SKILL.md
grep -E '^(\*\*Positive:|\*\*Negative:)' \
  .github/skills/plan-step-tracker/SKILL.md
```

---

## Inputs

- Existing `.github/skills/business-intent-alignment/SKILL.md`
- Existing `.github/skills/plan-step-tracker/SKILL.md`
- `.github/skills/agent-skill-creator/folder-contract.md`
- `.github/skills/agent-skill-reviewer/review-checklist.md`
- This plan

---

## Implementation Steps

1. Plan reviewer approves this plan.
2. Creator drafts both skills in Mode A+ unless a Preservation Map proves rewrite is required.
3. Reviewer subagents evaluate both drafts independently.
4. Creator addresses any `needs-rework` findings.
5. Main Agent performs planner contract alignment against the approved drafts and exact topic artifact paths before publish preparation begins.
6. STOP POINT 1 -> human approves commit + push while work is in `publish-in-progress`.
7. PR opens against `feature/skill-migration-v1`.
8. STOP POINT 2 -> human merges PR.

---

## Post-merge / Release Actions

No release action in this topic.

After merge into `feature/skill-migration-v1`, any branch cleanup or integration-branch follow-up is outside this topic.

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
