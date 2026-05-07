# Tier 5 — Git Helper Skills Migration
## Schema v2 upgrade: 1 git helper skill from legacy standard to creator/reviewer-approved

---

## Status / Allowed Transitions

**Current status**: `pr-open`

| From | To | Condition |
|---|---|---|
| `planned` | `creator-in-progress` | Plan reviewer returns `approved` |
| `creator-in-progress` | `review-ready` | Creator finishes the latest draft |
| `review-ready` | `reviewer-in-progress` | Reviewer subagent launched |
| `reviewer-in-progress` | `needs-rework` | agent-skill-reviewer returns `needs-rework` |
| `reviewer-in-progress` | `approved` | agent-skill-reviewer returns `approved` |
| `needs-rework` | `creator-in-progress` | Creator addresses reviewer blockers |
| `approved` | `creator-in-progress` | Planner contract alignment detects drift and routes back for correction |
| `approved` | `publish-in-progress` | Planner contract alignment passes and publish work may begin |
| `publish-in-progress` | `pr-open` | PR created targeting `feature/skill-migration-v1` |
| `pr-open` | `needs-rework` | PR feedback requires creator revision |
| `pr-open` | `merged` | A new explicit human resume message confirms the merge completed after STOP POINT 2 handoff |
| `merged` | `terminal` | No release action applies; post-merge cleanup runs only after explicit resume via `git-post-merge-workflow` |

---

## Goal / Outcome

Upgrade `git-branch-naming` to schema v2 while preserving its existing branch-naming responsibility, trigger rules, repair guidance, and non-automation boundary. The skill must reach `agent-skill-reviewer` verdict `approved` before Tier 5 is considered complete.

---

## Boundaries / Exclusions

- Do not redefine the skill's business responsibility or naming convention.
- Do not change the existing Process / Boundaries / Inputs / Outputs behavior contract.
- Do not modify governance files (`agent-skill-creator/`, `agent-skill-reviewer/`, `agent-skill-template/`).
- Do not update `README.md`, `VERSION`, or `files/migration-tracker.md` in this topic branch.
- Do not upgrade Tier 6 or Tier 7 skills in this plan.

---

## Scope

### In scope
`git-branch-naming` is inferred as **Mode A+**: preserve existing content and supplement only the schema v2 gaps.

### Out of scope
See Boundaries / Exclusions.

### Per-Skill Migration Parameters

| # | Skill | Mode | Inferred Complexity | Inferred Risk Profile | Preservation Notes |
|---|---|---|---|---|---|
| 1 | `git-branch-naming` | A+ | medium | ambiguity_sensitive | Preserve `<type>/<username>/<short-description>` contract, wrong-branch rescue paths, and non-automation boundary |

---

## Locked Decisions

### D1: Execution Model
- Single-skill creator -> reviewer loop.
- No intra-tier dependency exists beyond reviewer approval for this one skill.

### D2: Preservation Map Triggers
Creator must output a Preservation Map if Mode B rewrite is needed because:
- trigger / boundaries / process contradict each other
- schema v2 supplementation would require guessing missing behavior
- branch-repair guidance is too tangled to preserve safely in Mode A+

### D3: Complexity & Risk Profile Inference

| Skill | Complexity | Reasoning | Risk Profile | Rationale |
|---|---|---|---|---|
| `git-branch-naming` | **medium** | Multi-path decisions: new branch naming, existing-branch conflict, wrong-branch rescue path, and split-versus-broaden advice | ambiguity_sensitive | Missing context such as task type, namespace token, or existing branch state materially changes the recommended branch name and repair path |

### D4: YAML / Body Consistency Check
Creator must ensure YAML `complexity`, `risk_profile`, `use_when`, `do_not_use_when`, `inputs`, and `outputs` match the body without contradiction.

---

## Artifact Paths

| Artifact | Path | Owner | Role |
|---|---|---|---|
| tier-5 plan | `plan/tier-5-git-helper-skills/tier-5-git-helper-skills.plan.md` | Planning actor | Repo-visible execution contract for this topic |
| git-branch-naming | `.github/skills/git-branch-naming/SKILL.md` | creator | schema v2 upgrade |

**Stable-library surfaces not touched in this topic**: `README.md`, `VERSION`, and `files/migration-tracker.md` remain out of scope for this topic plan.

---

## Public Contract

When this plan is complete:
- `git-branch-naming` has schema v2 YAML governance metadata.
- The skill includes schema v2-required sections for its inferred complexity.
- Existing naming semantics, repair guidance, and non-automation boundary remain intact.
- The skill passes `agent-skill-reviewer` with verdict `approved`.

---

## Failure Handling

### Missing Context
- If creator cannot infer complexity or risk without guessing, mark the draft INCOMPLETE and list the exact missing signals.

### Ambiguous Requirement
- If creator detects internal contradictions that force Mode B, stop and output a Preservation Map before rewriting.

### Reviewer Rejection
- If reviewer returns `needs-rework`, creator revises only the flagged areas and resubmits.

---

## Validation / Acceptance Checks

Validation via creator/reviewer gates only; no new tests.

```bash
# Verify YAML metadata fields exist
cd .github/skills/git-branch-naming
grep -E '^(complexity|risk_profile|inputs|outputs|use_when|do_not_use_when):' SKILL.md

# Verify Validation and Failure Handling sections exist
grep -E '^# (Validation|Failure Handling)$' SKILL.md

# Verify at least one positive and one negative example
grep -E '^- \*\*(Positive|Negative)\*\*:' SKILL.md
```

---

## Inputs

- Existing `.github/skills/git-branch-naming/SKILL.md`
- `.github/skills/agent-skill-creator/folder-contract.md`
- `.github/skills/agent-skill-reviewer/review-checklist.md`
- This plan

---

## Implementation Steps

1. Plan reviewer approves this plan.
2. Creator upgrades `git-branch-naming` in Mode A+ unless a Preservation Map proves rewrite is required.
3. Reviewer returns `approved` or `needs-rework`.
4. If reviewer returns `needs-rework`, creator addresses only the flagged blockers and resubmits for independent reviewer re-check.
5. After reviewer `approved`, Main Agent performs planner contract alignment against this topic plan; any drift routes the topic back to `creator-in-progress` before publish.
6. If planner alignment passes, topic enters `publish-in-progress` and Main Agent prepares only the allowed artifact set for commit / push / PR creation.
7. STOP POINT 1: no commit, push, or PR creation until explicit human approval is given for the staged publish set.
8. After STOP POINT 1 approval, Main Agent may commit, push, and open the PR against `feature/skill-migration-v1`.
9. If PR feedback changes trigger logic, examples, process, boundaries, scope, or other reviewer-owned semantics, route back through creator -> reviewer rather than direct self-approval.
10. STOP POINT 2: after merge handoff, the current execution must fully stop; do not poll or continue until a new explicit human message confirms merge completion and requests post-merge follow-up.

---

## Post-merge / Release Actions

No release action in this topic.

After human merge handoff, this execution stops at STOP POINT 2.

Only after a new explicit human resume message that confirms the merge is complete:
- route post-merge cleanup and local sync through `git-post-merge-workflow`
- delete remote and local branch `migrate/tier-5-git-helper-skills` if that workflow confirms cleanup preconditions
- fast-forward sync the integration branch if that workflow confirms the merge state

`README.md`, `VERSION`, and `files/migration-tracker.md` are out of scope for this topic and remain untouched here.

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
