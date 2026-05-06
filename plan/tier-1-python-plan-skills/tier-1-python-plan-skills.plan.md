# Tier 1 — Python Planning / Review Skills Migration
## Schema v2 upgrade: 9 skills from legacy standard to creator/reviewer-approved

---

## Goal

Upgrade 9 Python planning/review/testing skills to schema v2 standard (with `complexity`, `risk_profile`, `Validation`, `Failure Handling` sections) while preserving all existing responsibility, trigger, and process behavior. All 9 skills must reach `reviewer-approved` status before Tier 1 completion.

---

## Non-goals

- Do not redefine any skill's business responsibility or primary trigger.
- Do not change the existing Process / Boundaries / Inputs / Outputs behavior contracts.
- Do not merge to `feature/skill-migration-v1` until all 9 skills are reviewer-approved.
- Do not bump VERSION during this phase; defer to final integration PR.
- Do not modify `agent-skill-creator/`, `agent-skill-reviewer/`, or `agent-skill-template/` (governance files are frozen during migration).

---

## Skills in Scope

All 9 skills are inferred as **upgrade mode (Mode A)** — preserve existing content, supplement with schema v2 sections only. Rewrite (Mode B) only if creator detects structural contradictions or mixed responsibilities.

### Per-Skill Migration Parameters

| # | Skill | Mode | Inferred Complexity | Inferred Risk Profile | Preservation Notes |
|---|---|---|---|---|---|
| 1 | `python-plan-authoring` | A | high | ambiguity_sensitive, multi_agent_handoff | Freeze 13-section plan structure; keep decision points explicit |
| 2 | `python-plan-review` | A | high | ambiguity_sensitive, multi_agent_handoff | Freeze boundary between "plan review" vs "implementation review" |
| 3 | `python-code-review` | A | high | ambiguity_sensitive, multi_agent_handoff, code_modification | Freeze review signal types; keep anti-patterns stable |
| 4 | `python-implementation-review` | A | high | ambiguity_sensitive, multi_agent_handoff, code_modification | Freeze distinction from `python-code-review` |
| 5 | `python-blueprint-authoring` | A | high | ambiguity_sensitive, multi_agent_handoff, destructive_action | Freeze blueprint schema v1 lock; keep examples stable |
| 6 | `python-blueprint-review` | A | high | ambiguity_sensitive, multi_agent_handoff, destructive_action | Freeze review contract against v1 schema |
| 7 | `python-retrofit-plan-authoring` | A | high | ambiguity_sensitive, multi_agent_handoff, destructive_action | Freeze retrofit v2 section order; keep risk metadata structure |
| 8 | `python-retrofit-plan-review` | A | high | ambiguity_sensitive, multi_agent_handoff, destructive_action | Freeze risk gates; keep sensing assertion kinds locked |
| 9 | `python-tdd-test-authoring` | A | high | ambiguity_sensitive, multi_agent_handoff, code_modification | Freeze TDD red→green→refactor flow; preserve examples |

---

## Decisions

### D1: Execution Model
- **Per-skill creator → reviewer loop**, not batch.
- Each skill produces review-ready draft independently.
- Reviewer approves or returns needs-rework for that skill only.
- Sequential dependency: later skills may depend on early ones if they reference each other.

### D2: Preservation Map Triggers
For each skill, creator must output a **Preservation Map** (in PR description or commit message) showing:
- **Preserve**: sections kept as-is with their role explained
- **Rewrite**: sections restructured; reason given
- **Remove**: sections deleted; reason given
- **Add**: new sections required by schema v2
- **Risk**: any lost behavior or implicit context that downstream users should be aware of

**Rewrite trigger**: creator encounters any of:
- Multiple responsibilities tangled together
- trigger / do_not_use_when / boundaries mutually contradictory
- Process steps already obsolete relative to local references
- Content gap too large to supplement without guessing

### D3: Complexity & Risk Profile Inference

All 9 skills are classified as **complexity: high**. Risk profiles vary per skill — see per-skill table above for authoritative values.

- All **require** `Validation` + `Failure Handling` sections.
- All **recommend** `Workflow State Contract` (multi-agent handoff is inherent to these skills).

### D4: YAML / Body Consistency Check

Creator must ensure:
- YAML `complexity`, `risk_profile`, `use_when`, `do_not_use_when` **align** with markdown body.
- No contradiction between YAML and body content.
- Contradiction = creator marks as needs-rework and explains.

### D5: Testing & Validation

No new tests are required. Validation is structural (YAML/body alignment, completeness of sections per complexity level).

---

## Affected Files

| Artifact | Path | Owner | Role |
|---|---|---|---|
| python-plan-authoring | `.github/skills/python-plan-authoring/SKILL.md` | creator | schema v2 upgrade |
| python-plan-review | `.github/skills/python-plan-review/SKILL.md` | creator | schema v2 upgrade |
| python-code-review | `.github/skills/python-code-review/SKILL.md` | creator | schema v2 upgrade |
| python-implementation-review | `.github/skills/python-implementation-review/SKILL.md` | creator | schema v2 upgrade |
| python-blueprint-authoring | `.github/skills/python-blueprint-authoring/SKILL.md` | creator | schema v2 upgrade |
| python-blueprint-review | `.github/skills/python-blueprint-review/SKILL.md` | creator | schema v2 upgrade |
| python-retrofit-plan-authoring | `.github/skills/python-retrofit-plan-authoring/SKILL.md` | creator | schema v2 upgrade |
| python-retrofit-plan-review | `.github/skills/python-retrofit-plan-review/SKILL.md` | creator | schema v2 upgrade |
| python-tdd-test-authoring | `.github/skills/python-tdd-test-authoring/SKILL.md` | creator | schema v2 upgrade |
| migration tracker | `files/migration-tracker.md` | main-agent | updated per skill after reviewer approval |

**Stable-library surfaces not touched**: `README.md`, `VERSION`, release notes, `.github/copilot-instructions.md`, and all governance files (`agent-skill-creator/`, `agent-skill-reviewer/`, `agent-skill-template/`) are explicitly out of scope for this topic.

---

## Public Contract

When this plan is complete:
- All 9 skills have `complexity`, `risk_profile`, `Validation`, `Failure Handling` sections.
- All maintain their original responsibility, trigger, process, and boundary semantics.
- All pass `agent-skill-reviewer` with verdict `approved`.
- Migration tracker records Mode (A/B), complexity, risk_profile, and any rewrite notes.

---

## Failure Handling

### Missing Context
- Creator cannot infer a skill's complexity → mark as INCOMPLETE, list missing signals.

### Ambiguous Requirement
- If creator judges a skill is "too tangled to supplement" → output **Preservation Map** explaining the structural issue, human decides: retry with clearer input or approve the rewrite risk.

### Reviewer Rejection
- Reviewer returns needs-rework → creator revises and resubmits to same reviewer.
- If revision requires **rewriting** beyond initial Mode A scope → creator outputs new Preservation Map, human approves before proceeding.

### Execution Limitation
- Creator subagent is tasked with all 9 skills; if it encounters a blocker on skill N, it must record that and continue with skills N+1..9 rather than stopping all work.

---

## Test Plan

No new tests. Validation via:
1. **Creator dry-run**: each skill outputs review-ready SKILL.md with all schema v2 sections present.
2. **Reviewer gates**: each skill passes agent-skill-reviewer checklist (YAML/body alignment, complexity match, examples sufficiency).
3. **Human sign-off**: PR description includes Preservation Map for any Mode B rewrites; human approves skill list and verdict.

---

## Validation Commands

None (no code changes). Structural validation is manual review + agent-skill-reviewer tool.

---

## Inputs

- This plan document (`tier-1-python-plan-skills.plan.md`)
- Current state of all 9 skills in `.github/skills/`
- Creator agent role (via `agent-skill-creator` skill)
- Reviewer agent role (via `agent-skill-reviewer` skill)
- Human sign-off at each skill's completion gate

---

## Execution Sequence

### Phase 1: Skill 1–9 Creator Loop (Parallelizable but Per-Skill Approved)

For each skill in order:
1. **Creator subagent** reads current SKILL.md + local references.
2. Creator judges Mode (A/B); if B, outputs Preservation Map for human review before proceeding.
3. Creator produces review-ready SKILL.md (schema v2 compliant, all sections filled per complexity).
4. Creator outputs: Preservation Map (if B), YAML/body consistency check, and ready-for-review signal.

### Phase 2: Skill 1–9 Reviewer Loop

For each skill (ordered):
1. **Reviewer subagent** receives creator draft + Preservation Map (if any).
2. Reviewer runs agent-skill-reviewer checklist.
3. Reviewer outputs: `approved` or `needs-rework` verdict + detailed feedback.

### Phase 3: Revision (if needed)

If reviewer returns needs-rework:
1. Creator revises based on feedback.
2. Resubmit to reviewer.
3. Repeat until `approved`.

### Phase 4: Human Sign-Off (STOP POINT 1)

Once all 9 skills are reviewer-approved:
1. Collect all Preservation Maps + reviewer verdicts.
2. Human reviews the complete Tier 1 summary.
3. **STOP POINT 1**: Explicit human approval before commit.

### Phase 5: Commit & PR

1. Commit all 9 updated SKILL.md files + migration tracker update.
2. Message: `chore(skills): upgrade tier-1 python-plan skills to schema v2`
3. Push to `migrate/tier-1-python-plan-skills`.
4. Open PR to `feature/skill-migration-v1`.
5. PR description includes all Preservation Maps + reviewer verdict summary.

### Phase 6: Merge to Integration Branch (STOP POINT 2)

1. Human reviews PR on GitHub.
2. **STOP POINT 2**: Human merges to `feature/skill-migration-v1`.
3. Once merged, Tier 1 is complete; Tier 2 can begin (uses rebased feature/skill-migration-v1).

---

## Blockers

None identified. All 9 skills have existing `SKILL.md` files and local references; no missing upstream dependencies.

---

## Open Questions / Unresolved Items

None at plan authoring time.

---

## Post-merge / Release Actions

This topic does **not** trigger a repository release. No actions on `VERSION`, `README.md`, release notes, or CHANGELOG are required when Tier 1 merges to `feature/skill-migration-v1`.

The merge to `feature/skill-migration-v1` is the terminal action for this topic. Tier 2 begins by rebasing from the updated integration branch.

---

## Status / Allowed Transitions

```
planned → in_progress → review → approved → merged
```

| Status | Meaning |
|---|---|
| `planned` | Plan authored, awaiting plan-reviewer approval |
| `in_progress` | Creator/reviewer loops active for ≥1 skill |
| `review` | All 9 skills reviewer-approved, awaiting human STOP POINT 1 sign-off |
| `approved` | Human signed off, PR open on GitHub |
| `merged` | PR merged to `feature/skill-migration-v1` |

**Current status**: `planned`

This topic does not advance to `released` — no release action is scoped here.

---

## Reviewer Handoff

```json
{
  "verdict": "approved",
  "plan_path": "plan/tier-1-python-plan-skills/tier-1-python-plan-skills.plan.md",
  "reviewer_agent": "plan-reviewer",
  "round": 2,
  "blocking_issues": [],
  "copilot_feedback_triage": {
    "ADDRESS": [],
    "DISCUSS": [],
    "SKIP": ["Reviewer Handoff JSON contains extra plan_path field — harmless"]
  }
}
```

---

## Rollback Plan

If reviewer rejects multiple skills with the same structural issue:
- Pause Tier 1 execution.
- Human and creator discuss: is this a creator bug, schema v2 ambiguity, or skill design issue?
- Option A: fix creator logic, restart Tier 1.
- Option B: adjust schema v2 policy (requires governance file change, out of scope for Tier 1).
- Option C: mark skills as needing manual hand-editing by human reviewer (escalation).

---

## Success Criteria

✓ All 9 skills have YAML `complexity` and `risk_profile` fields.
✓ All 9 skills have `Validation` and `Failure Handling` sections (per high complexity).
✓ All 9 skills pass agent-skill-reviewer `approved` status.
✓ No changes to governance files or VERSION.
✓ Migration tracker updated with Mode, complexity, risk_profile, and reviewer verdict for each skill.
✓ PR merged to `feature/skill-migration-v1`.

---

## Non-Blocking Follow-Ups (for future tiers or post-Tier-1)

- If creator discovers schema v2 ambiguities affecting all tiers → record in migration notes, defer to post-migration governance review.
- If any rewrite revealed obsolete local references → mark for cleanup in later audit.
- If high-risk skill verdicts suggest creator/reviewer feedback loop needs tuning → record, defer to workflow-gate analysis.
