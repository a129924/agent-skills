# Tier 3 — Python Helper / Reference Skills Migration
## Schema v2 upgrade: 20 skills from legacy standard to creator/reviewer-approved

---

## Goal / Outcome

Upgrade 20 Python helper/reference skills to schema v2 standard (with `complexity`, `risk_profile`, `Validation`, `Failure Handling` sections where required by complexity) while preserving all existing responsibility, trigger, and process behavior. All 20 skills must reach `reviewer-approved` status before Tier 3 completion.

**Target skills**:
1. `python-naming` — Python naming conventions (complexity: **low**)
2. `python-docstrings` — Google Style docstring contract writing (complexity: **low**)
3. `python-control-flow` — if/elif/match/case/guard patterns (complexity: **low**)
4. `python-comprehensions` — list/dict/set comprehension readability rules (complexity: **low**)
5. `python-type-hints-strict` — strict pyright type-hint rules (complexity: **medium**)
6. `python-generators-iterators` — generator vs collection choice (complexity: **medium**)
7. `python-context-management` — context manager design (complexity: **medium**)
8. `python-async-await` — async boundary and concurrency rules (complexity: **medium**)
9. `python-decorators` — decorator use and transparency rules (complexity: **medium**)
10. `python-descriptors-attribute-access` — attribute access ladder (complexity: **medium**)
11. `python-data-model-methods` — dunder method selection rules (complexity: **medium**)
12. `python-operator-overloading` — operator contract rules (complexity: **medium**)
13. `python-class-design` — public surface and instance state rules (complexity: **medium**)
14. `python-api-signature` — function/method signature rules (complexity: **medium**)
15. `python-module-boundaries` — package/module boundary rules (complexity: **medium**)
16. `python-library-architecture` — library/package architecture rules (complexity: **medium**)
17. `python-package-layout` — package layout with src/ and pyproject.toml (complexity: **medium**)
18. `python-error-handling` — exception handling rules (complexity: **medium**)
19. `python-serialization-boundaries` — serialization boundary rules (complexity: **medium**)
20. `python-model-selection` — Enum/dataclass/ABC/Protocol selection rules (complexity: **medium**)

---

## Scope

**In scope**:
- All 20 Python helper/reference skills listed below, each upgraded to schema v2.
- All 20 skills use **upgrade mode (Mode A+)** — preserve existing content, supplement with schema v2 YAML fields and sections only. Rewrite (Mode B) only if creator detects structural contradictions or mixed responsibilities.

**Out of scope**:
- Do not redefine any skill's business responsibility or primary trigger.
- Do not change the existing Process / Boundaries / Inputs / Outputs behavior contracts.
- Do not bump VERSION during this phase; defer to final integration PR.
- Do not modify `agent-skill-creator/`, `agent-skill-reviewer/`, or `agent-skill-template/` (governance files are frozen during migration).
- Do not upgrade Tier 4–7 skills in this plan.

### Per-Skill Migration Parameters

| # | Skill | Mode | Inferred Complexity | Inferred Risk Profile | Preservation Notes |
|---|---|---|---|---|---|
| 1 | `python-naming` | A+ | low | — | Preserve all naming rules verbatim; no decisions |
| 2 | `python-docstrings` | A+ | low | — | Preserve Google Style format rules |
| 3 | `python-control-flow` | A+ | low | — | Preserve truthiness/guard/match rules |
| 4 | `python-comprehensions` | A+ | low | — | Preserve readability thresholds |
| 5 | `python-type-hints-strict` | A+ | medium | ambiguity_sensitive | Preserve strict-mode constraints; branching for type categories |
| 6 | `python-generators-iterators` | A+ | medium | ambiguity_sensitive | Preserve generator vs collection decision ladder |
| 7 | `python-context-management` | A+ | medium | ambiguity_sensitive | Preserve @contextmanager vs class-based choice rules |
| 8 | `python-async-await` | A+ | medium | ambiguity_sensitive | Preserve async boundary and cancellation rules |
| 9 | `python-decorators` | A+ | medium | ambiguity_sensitive | Preserve transparency and signature-preservation rules |
| 10 | `python-descriptors-attribute-access` | A+ | medium | ambiguity_sensitive | Preserve the least-powerful-sufficient ladder |
| 11 | `python-data-model-methods` | A+ | medium | ambiguity_sensitive | Preserve dunder method selection rules and dataclass boundary |
| 12 | `python-operator-overloading` | A+ | medium | ambiguity_sensitive | Preserve NotImplemented dispatch and reflected-operator pairing |
| 13 | `python-class-design` | A+ | medium | ambiguity_sensitive | Preserve public surface, thin constructor, and name-mangling rules |
| 14 | `python-api-signature` | A+ | medium | ambiguity_sensitive | Preserve parameter ordering and keyword-only rules |
| 15 | `python-module-boundaries` | A+ | medium | ambiguity_sensitive | Preserve public surface and re-export rules |
| 16 | `python-library-architecture` | A+ | medium | ambiguity_sensitive | Preserve theme isolation and core contract rules |
| 17 | `python-package-layout` | A+ | medium | ambiguity_sensitive | Preserve src/ layout and packaged-data rules |
| 18 | `python-error-handling` | A+ | medium | ambiguity_sensitive | Preserve translation boundary and propagation rules |
| 19 | `python-serialization-boundaries` | A+ | medium | ambiguity_sensitive | Preserve semantic translation gate and null-intent rules |
| 20 | `python-model-selection` | A+ | medium | ambiguity_sensitive | Preserve selection ladder across all 4 construct types |

---

## Locked Decisions

### D1: Execution Model
- **Per-skill creator → reviewer loop**, not batch.
- Each skill produces review-ready draft independently.
- Reviewer approves or returns needs-rework for that skill only.
- Sequential dependency: **none** — all 20 skills can be processed in parallel.

### D2: Preservation Map Triggers
For each skill, creator must output a **Preservation Map** showing:
- **Preserve**: sections kept as-is
- **Rewrite**: sections restructured; reason given
- **Remove**: sections deleted; reason given
- **Add**: new sections required by schema v2
- **Risk**: any lost behavior or implicit context

**Rewrite trigger** (Mode B):
- Multiple responsibilities tangled together
- Trigger / do_not_use_when / boundaries mutually contradictory
- Process steps already obsolete relative to local references
- Content gap too large to supplement without guessing

### D3: Complexity & Risk Profile Inference

**Low complexity skills** (4 skills): `python-naming`, `python-docstrings`, `python-control-flow`, `python-comprehensions`
- These are pure reference/guidance with no branching decisions
- `risk_profile`: empty (no execution risk)
- `Validation` and `Failure Handling`: optional; include only if risk signals exist
- No `Workflow State Contract` needed

**Medium complexity skills** (16 skills): all remaining
- These involve branching decisions where missing context changes the guidance materially
- `risk_profile`: `[ambiguity_sensitive]`
- `Validation`: recommended; include when ambiguity would change output
- `Failure Handling`: include when ambiguity would materially change output
- No `Workflow State Contract` needed (no multi-agent handoff)

### D4: YAML / Body Consistency Check
Creator must ensure:
- YAML `complexity`, `risk_profile`, `use_when`, `do_not_use_when` align with markdown body.
- No contradiction between YAML and body content.
- Contradiction = creator marks as needs-rework and explains.

### D5: Batch Execution Strategy
- Due to volume (20 skills), creator subagents run in groups of 4 (max concurrency limit).
- Groups: [1–4], [5–8], [9–12], [13–16], [17–20]
- Each group is reviewed independently before next group starts.
- Reviewer subagents run in parallel within each group.

---

## Boundaries / Exclusions

Role boundaries:
- Creator must not self-review; each skill requires an independent reviewer subagent.
- Reviewer may not author the skill implementation; reviewer role is verdict-only.
- Main Agent must not merge the PR; STOP POINT 2 requires explicit human approval.
- Governance files (`agent-skill-creator/`, `agent-skill-reviewer/`, `agent-skill-template/`) are frozen during this migration.

Scope boundaries:
- Do not merge to `feature/skill-migration-v1` until all 20 skills pass `agent-skill-reviewer`.
- VERSION bump, README update, and release notes belong to the final integration PR topic.
- Tier 4–7 skill upgrades belong to separate topics.

---

## Status / Allowed Transitions

- **Current**: `planned`
- **Execution model**: per-skill creator → reviewer loop; all 20 skills must reach `reviewer-approved` before publish begins; topic stops at `pr-open` pending human merge (STOP POINT 2); no release action at merge time.
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
  - `pr-open` → `needs-rework`
  - `pr-open` → `merged`
  - `merged` → terminal

Routing notes:
- This topic does not trigger a repository release; `merged` is the terminal state.
- Phase 4.5 rule applies: plan-reviewer approval required before creator work begins.
- STOP POINT 1: no commit or push until explicit human approval.
- STOP POINT 2: no self-merge; PR waits for explicit human merge into `feature/skill-migration-v1`.

---

## Artifact Paths

| Artifact | Path | Owner | Role |
|---|---|---|---|
| Topic plan | `plan/tier-3-python-helper-skills/tier-3-python-helper-skills.plan.md` | Planning actor | Repo-visible execution contract for this topic |
| python-naming | `.github/skills/python-naming/SKILL.md` | creator | schema v2 upgrade |
| python-docstrings | `.github/skills/python-docstrings/SKILL.md` | creator | schema v2 upgrade |
| python-control-flow | `.github/skills/python-control-flow/SKILL.md` | creator | schema v2 upgrade |
| python-comprehensions | `.github/skills/python-comprehensions/SKILL.md` | creator | schema v2 upgrade |
| python-type-hints-strict | `.github/skills/python-type-hints-strict/SKILL.md` | creator | schema v2 upgrade |
| python-generators-iterators | `.github/skills/python-generators-iterators/SKILL.md` | creator | schema v2 upgrade |
| python-context-management | `.github/skills/python-context-management/SKILL.md` | creator | schema v2 upgrade |
| python-async-await | `.github/skills/python-async-await/SKILL.md` | creator | schema v2 upgrade |
| python-decorators | `.github/skills/python-decorators/SKILL.md` | creator | schema v2 upgrade |
| python-descriptors-attribute-access | `.github/skills/python-descriptors-attribute-access/SKILL.md` | creator | schema v2 upgrade |
| python-data-model-methods | `.github/skills/python-data-model-methods/SKILL.md` | creator | schema v2 upgrade |
| python-operator-overloading | `.github/skills/python-operator-overloading/SKILL.md` | creator | schema v2 upgrade |
| python-class-design | `.github/skills/python-class-design/SKILL.md` | creator | schema v2 upgrade |
| python-api-signature | `.github/skills/python-api-signature/SKILL.md` | creator | schema v2 upgrade |
| python-module-boundaries | `.github/skills/python-module-boundaries/SKILL.md` | creator | schema v2 upgrade |
| python-library-architecture | `.github/skills/python-library-architecture/SKILL.md` | creator | schema v2 upgrade |
| python-package-layout | `.github/skills/python-package-layout/SKILL.md` | creator | schema v2 upgrade |
| python-error-handling | `.github/skills/python-error-handling/SKILL.md` | creator | schema v2 upgrade |
| python-serialization-boundaries | `.github/skills/python-serialization-boundaries/SKILL.md` | creator | schema v2 upgrade |
| python-model-selection | `.github/skills/python-model-selection/SKILL.md` | creator | schema v2 upgrade |
| migration tracker | `files/migration-tracker.md` | main-agent | updated per skill after reviewer approval |

**Stable-library surfaces not touched**: `README.md`, `VERSION`, release notes, `.github/copilot-instructions.md`, and all governance files (`agent-skill-creator/`, `agent-skill-reviewer/`, `agent-skill-template/`) are explicitly out of scope for this topic.

---

## Implementation Steps

For each batch of skills (groups of up to 4, run as parallel creator subagents):

1. **Creator subagent** reads the existing `SKILL.md` for each skill in the group and produces:
   - A Preservation Map (Preserve / Rewrite / Remove / Add / Risk per section).
   - Updated `SKILL.md` with schema v2 YAML fields (`complexity`, `risk_profile`, `use_when`, `do_not_use_when`) plus required body sections (`Validation`, `Failure Handling` where warranted by complexity).
   - YAML / body consistency verified: no contradiction between YAML fields and markdown body.
2. **Low-complexity skills** (python-naming, python-docstrings, python-control-flow, python-comprehensions): add `complexity: low`, `risk_profile: []`; `Validation` and `Failure Handling` are optional.
3. **Medium-complexity skills** (all remaining 16): add `complexity: medium`, `risk_profile: [ambiguity_sensitive]`; include `Validation` and `Failure Handling` sections.
4. If **Mode B** is triggered: creator outputs Preservation Map explaining the structural issue; halts and awaits human decision before proceeding with that skill.
5. After all skills in a group are review-ready, **reviewer subagents** run in parallel to issue independent verdicts.
6. After each group's reviewers approve all skills, **Main Agent** updates `files/migration-tracker.md` with Mode, complexity, risk_profile, and rewrite notes.

---

## Failure Handling

### Missing Context
- Creator cannot infer a skill's complexity or risk profile → mark as INCOMPLETE, list missing signals.

### Ambiguous Requirement
- If creator judges a skill is "too tangled to supplement" → output Preservation Map explaining the structural issue; human decides whether to retry or approve rewrite.

### Reviewer Rejection
- Reviewer returns needs-rework → creator revises and resubmits to same reviewer.
- If revision requires rewriting beyond initial Mode A+ scope → creator outputs new Preservation Map; human approves before proceeding.

### Execution Limitation
- If creator encounters a blocker on skill N within a group, record that and continue with remaining skills in the group rather than stopping all work.

---

## Validation / Acceptance Checks

Acceptance signals:
1. All 20 skills reach `reviewer-approved` status (confirmed by reviewer subagent JSON verdicts).
2. Migration tracker (`files/migration-tracker.md`) records Mode, complexity, risk_profile, and rewrite notes for every skill.
3. PR description includes Preservation Map for any Mode B rewrites.
4. Plan status is `pr-open` before merge; no `TBD` placeholders remain in any upgraded skill's YAML.
5. Each skill passes `agent-skill-reviewer` checklist: YAML/body alignment, complexity match, examples sufficiency, risk gates respected.

Verification commands per upgraded skill:

```bash
# Verify YAML metadata fields exist
cd .github/skills/<skill-name>
cat SKILL.md | grep -E '^(complexity|risk_profile|inputs|outputs|use_when|do_not_use_when):'

# Verify Validation section (required for high; recommended for medium)
grep -A 10 '^# Validation' SKILL.md | head -12

# Verify Failure Handling section (required for high; recommended for medium)
grep -A 10 '^# Failure Handling' SKILL.md | head -12

# Verify at least one positive and one negative example
grep -E '^- \*\*(Positive|Negative|Correct|Incorrect)\*\*' SKILL.md | wc -l

# Verify risk_profile declared in YAML
grep 'risk_profile:' SKILL.md
```

---

## Inputs

- All 20 existing `SKILL.md` files (legacy format, no schema v2 fields)
- `agent-skill-creator/folder-contract.md` (schema v2 authority)
- `agent-skill-reviewer/review-checklist.md` (reviewer gate authority)
- This plan (execution contract)

---

## Execution Sequence

1. Plan reviewer approves this plan → branch `migrate/tier-3-python-helper-skills` ready
2. Creator group 1 (skills 1–4: low complexity) → reviewer group 1 in parallel
3. Creator group 2 (skills 5–8) → reviewer group 2 in parallel
4. Creator group 3 (skills 9–12) → reviewer group 3 in parallel
5. Creator group 4 (skills 13–16) → reviewer group 4 in parallel
6. Creator group 5 (skills 17–20) → reviewer group 5 in parallel
7. Migration tracker updated after each group's reviewers approve
8. STOP POINT 1 → human approves commit + push
9. PR opened → Copilot review → feedback addressed if needed
10. STOP POINT 2 → human merges PR into `feature/skill-migration-v1`

---

## Reviewer Handoff

```json
{
  "verdict": "approved|needs-rework",
  "blocking_issues": [],
  "copilot_feedback_triage": {
    "ADDRESS": [],
    "DISCUSS": [],
    "SKIP": []
  }
}
```

---

## Post-merge / release actions

No repository release action is required at merge time. This topic merges into `feature/skill-migration-v1`, an integration branch — not `dev` or `main`. VERSION bump, README update, and release notes are deferred to the final integration PR that consolidates all Tier migrations. No action required by Main Agent after merge is complete.

---

## Open Questions / Unresolved Items

None — all decisions locked. If a skill's creator detects a structural issue requiring Mode B rewrite, the human decision gate is defined in `Failure Handling`.
