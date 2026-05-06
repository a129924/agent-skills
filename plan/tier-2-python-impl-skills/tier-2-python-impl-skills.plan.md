# Tier 2 — Python Implementation / Code-modification Skills Migration
## Schema v2 upgrade: 4 skills from legacy standard to creator/reviewer-approved

---

## Goal

Upgrade 4 Python implementation/code-modification skills to schema v2 standard (with `complexity`, `risk_profile`, `Validation`, `Failure Handling` sections) while preserving all existing responsibility, trigger, and process behavior. All 4 skills must reach `reviewer-approved` status before Tier 2 completion.

**Target skills**:
1. `python-project-init-greenfield` — greenfield Python project scaffolding (complexity: **high**)
2. `python-project-retrofit` — existing Python project migration (complexity: **high**)
3. `python-pre-commit` — pre-commit hook configuration (complexity: **medium**)
4. `python-pyproject-toolconfig` — pyproject.toml tool config append (complexity: **medium**)

---

## Non-goals

- Do not redefine any skill's business responsibility or primary trigger.
- Do not change the existing Process / Boundaries / Inputs / Outputs behavior contracts.
- Do not merge to `feature/skill-migration-v1` until all 4 skills are reviewer-approved.
- Do not bump VERSION during this phase; defer to final integration PR.
- Do not modify `agent-skill-creator/`, `agent-skill-reviewer/`, or `agent-skill-template/` (governance files are frozen during migration).
- Do not upgrade Tier 3–7 skills in this plan.

---

## Skills in Scope

All 4 skills are inferred as **upgrade mode (Mode A+)** — preserve existing content, supplement with schema v2 sections only. Rewrite (Mode B) only if creator detects structural contradictions or mixed responsibilities.

### Per-Skill Migration Parameters

| # | Skill | Mode | Inferred Complexity | Inferred Risk Profile | Preservation Notes |
|---|---|---|---|---|---|
| 1 | `python-project-init-greenfield` | A+ | high | destructive_action, multi_agent_handoff | Freeze blueprint v1 parsing logic; keep `sense-env-scaffold` handoff explicit |
| 2 | `python-project-retrofit` | A+ | high | destructive_action, multi_agent_handoff, code_modification | Freeze retrofit v2 section order; keep risk gates + human authorization explicit |
| 3 | `python-pre-commit` | A+ | medium | code_modification, external_tooling | Freeze canonical hook set; keep ruff/pytest/pyright separation clear |
| 4 | `python-pyproject-toolconfig` | A+ | medium | code_modification | Freeze non-destructive append semantics; keep "no overwrite" guarantee |

---

## Decisions

### D1: Execution Model
- **Per-skill creator → reviewer loop**, not batch.
- Each skill produces review-ready draft independently.
- Reviewer approves or returns needs-rework for that skill only.
- Sequential dependency: **none** — all 4 skills can be reviewed in parallel once creator work completes per skill.

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

| Skill | Complexity | Reasoning | Risk Profile | Rationale |
|---|---|---|---|---|
| `python-project-init-greenfield` | **high** | Multi-section output, creates entrypoints, multi-agent handoff to `sense-env-scaffold` | destructive_action, multi_agent_handoff | Creates new files, directories, and scaffolding; hands off to acceptance engine |
| `python-project-retrofit` | **high** | Multi-section input parsing, destructive file moves/merges, risk gates, human authorization required, multi-agent handoff | destructive_action, multi_agent_handoff, code_modification | Migrates existing projects with preview gates and HIGH-risk blocking |
| `python-pre-commit` | **medium** | Single-file output, calls external tool (`pre-commit-config.yaml` creation), optional merge logic | code_modification, external_tooling | Modifies config but non-destructive merge strategy; pre-commit is external tooling |
| `python-pyproject-toolconfig` | **medium** | Single-file append, no destructive overwrites, scripted append semantics | code_modification | Appends config sections only; guarantees no existing section overwrites |

- High-complexity skills **require** `Validation` + `Failure Handling` sections. Medium-complexity skills **should include** both when ambiguity would materially change output. Low-complexity skills may omit both unless risk signals warrant them.
- High-complexity skills **recommend** `Workflow State Contract` (multi-agent handoff is inherent to greenfield + retrofit).

### D4: YAML / Body Consistency Check

Creator must ensure:
- YAML `complexity`, `risk_profile`, `use_when`, `do_not_use_when` **align** with markdown body.
- No contradiction between YAML and body content.
- Contradiction = creator marks as needs-rework and explains.

---

## Affected Files

| Artifact | Path | Owner | Role |
|---|---|---|---|
| python-project-init-greenfield | `.github/skills/python-project-init-greenfield/SKILL.md` | creator | schema v2 upgrade |
| python-project-retrofit | `.github/skills/python-project-retrofit/SKILL.md` | creator | schema v2 upgrade |
| python-pre-commit | `.github/skills/python-pre-commit/SKILL.md` | creator | schema v2 upgrade |
| python-pyproject-toolconfig | `.github/skills/python-pyproject-toolconfig/SKILL.md` | creator | schema v2 upgrade |
| migration tracker | `files/migration-tracker.md` | main-agent | updated per skill after reviewer approval |

**Stable-library surfaces not touched**: `README.md`, `VERSION`, release notes, `.github/copilot-instructions.md`, and all governance files (`agent-skill-creator/`, `agent-skill-reviewer/`, `agent-skill-template/`) are explicitly out of scope for this topic.

---

## Public Contract

When this plan is complete:
- All 4 skills have `complexity`, `risk_profile`, `Validation`, `Failure Handling` sections.
- All maintain their original responsibility, trigger, process, and boundary semantics.
- All pass `agent-skill-reviewer` with verdict `approved`.
- Migration tracker records Mode (A+), complexity, risk_profile, and any rewrite notes.
- No breaking changes to existing workflow contracts for downstream skills or users.

---

## Failure Handling

### Missing Context
- Creator cannot infer a skill's complexity or risk profile → mark as INCOMPLETE, list missing signals.

### Ambiguous Requirement
- If creator judges a skill is "too tangled to supplement" → output **Preservation Map** explaining the structural issue, human decides: retry with clearer input or approve the rewrite risk.

### Reviewer Rejection
- Reviewer returns needs-rework → creator revises and resubmits to same reviewer.
- If revision requires **rewriting** beyond initial Mode A+ scope → creator outputs new Preservation Map, human approves before proceeding.

### Execution Limitation
- Creator subagent is tasked with all 4 skills; if it encounters a blocker on skill N, it must record that and continue with skills N+1..4 rather than stopping all work.

### Risk Gate Failures
- If High-risk skill (`python-project-init-greenfield`, `python-project-retrofit`) cannot pass risk alignment validation:
  - Mark as BLOCKED.
  - Output detailed risk assessment + human decision request.
  - Do not retry without explicit human approval to proceed or escalate.

---

## Test Plan

No new tests. Validation via:
1. **Creator dry-run**: each skill outputs review-ready SKILL.md with all schema v2 sections present.
2. **Reviewer gates**: each skill passes agent-skill-reviewer checklist (YAML/body alignment, complexity match, examples sufficiency, risk gates respected).
3. **Human sign-off**: PR description includes Preservation Map for any Mode B rewrites; human approves skill list and verdict.

---

## Validation Commands

For each upgraded skill, verify schema v2 compliance:

```bash
# Verify YAML metadata fields exist
cd .github/skills/<skill-name>
cat SKILL.md | grep -E '^(complexity|risk_profile|inputs|outputs|use_when|do_not_use_when):'

# Verify Validation section present (required for high complexity)
grep -A 20 '^# Validation' SKILL.md | head -25

# Verify Failure Handling section present (required for high complexity)
grep -A 20 '^# Failure Handling' SKILL.md | head -25

# Verify YAML examples consistency (at least one positive, one negative)
grep -E '^- \*\*(Positive|Negative)\*\*:' SKILL.md | wc -l

# Verify risk_profile tags match risk_profile declared in YAML
grep 'risk_profile:' SKILL.md
grep -E '(destructive|multi_agent|code_modification|external_tooling|ambiguity_sensitive)' SKILL.md | head -10
```

---

## Inputs

- This plan document (`tier-2-python-impl-skills.plan.md`)
- Current state of all 4 skills in `.github/skills/`
- Creator agent role (via `agent-skill-creator` skill)
- Reviewer agent role (via `agent-skill-reviewer` skill)
- Human sign-off at each skill's completion gate
- Reference: `plan/tier-1-python-plan-skills/tier-1-python-plan-skills.plan.md` (parallel Tier 1 model)
- Reference: `.github/skills/agent-skill-creator/folder-contract.md` (schema v2 policy)

---

## Execution Sequence

### Phase 1: Skill 1–4 Creator Loop (Parallelizable after each skill finishes)

For each skill **in order** (greenfield → retrofit → pre-commit → toolconfig):
1. **Creator subagent** reads current SKILL.md + local references.
2. Creator judges Mode (A+/B); if B, outputs Preservation Map for human review before proceeding.
3. Creator produces review-ready SKILL.md:
   - Adds YAML metadata: `complexity`, `risk_profile`, `inputs`, `outputs`, `use_when`, `do_not_use_when`
   - Adds `# Validation` section (brief for medium, detailed for high)
   - Adds `# Failure Handling` section with recoverable/non-recoverable outcomes
   - For high-complexity multi-agent skills, includes `# Workflow State Contract` (recommended)
   - Preserves all existing sections (Purpose, Trigger, Process, Examples, Outputs, Boundaries, Local references)
4. Creator outputs: Preservation Map (if B), YAML/body consistency check, and ready-for-review signal.

### Phase 2: Skill 1–4 Reviewer Loop

For each skill (ordered):
1. **Reviewer subagent** receives creator draft + Preservation Map (if any).
2. Reviewer runs agent-skill-reviewer checklist:
   - YAML metadata present and non-contradictory
   - Complexity level matches required sections (Validation + Failure Handling for high/medium)
   - Risk profile tags match actual skill behavior
   - Examples sufficient for the complexity level
   - Boundaries and trigger remain clear
3. Reviewer outputs: `approved` or `needs-rework` verdict + detailed feedback.

### Phase 3: Revision (if needed)

If reviewer returns needs-rework:
1. Creator revises based on feedback.
2. Resubmit to reviewer.
3. Repeat until `approved`.

### Phase 4: Human Sign-Off (STOP POINT 1)

Once all 4 skills are reviewer-approved:
1. Collect all Preservation Maps + reviewer verdicts.
2. Human reviews the complete Tier 2 summary.
3. **STOP POINT 1**: Explicit human approval before commit.

### Phase 5: Commit & PR

1. Commit all 4 updated SKILL.md files + migration tracker update.
2. Message: `chore(skills): upgrade tier-2 python-impl skills to schema v2`
3. Push to `migrate/tier-2-python-impl-skills`.
4. Open PR to `feature/skill-migration-v1`.
5. PR description includes all Preservation Maps + reviewer verdict summary.

### Phase 6: Merge to Integration Branch (STOP POINT 2)

1. Human reviews PR on GitHub.
2. **STOP POINT 2**: Human merges to `feature/skill-migration-v1`.
3. Once merged, Tier 2 is complete; Tier 3 can begin (uses rebased feature/skill-migration-v1).

---

## Blockers

None identified at plan authoring. All 4 skills have existing `SKILL.md` files and supporting documentation. No upstream dependencies on other tiers.

---

## Open Questions / Unresolved Items

### Q1: Multi-agent handoff contract for pre-commit and toolconfig
**Context**: Both `python-pre-commit` and `python-pyproject-toolconfig` are lower-complexity code-modification skills. Neither explicitly hands off to another agent in their Process.

**Question**: Should these skills include a `# Workflow State Contract` section, or is it optional per the folder-contract.md "recommended" language for high-complexity only?

**Resolution**: Per folder-contract.md § Complexity Policy, Workflow State Contract is **optional** for medium complexity. Only **recommend** it for high-complexity multi-agent handoff. For `python-pre-commit` (medium) and `python-pyproject-toolconfig` (medium), include if the creator detects consumer-agent patterns; otherwise, mark as not-required.

### Q2: python-pyproject-toolconfig Chinese-language Process
**Context**: The existing SKILL.md for `python-pyproject-toolconfig` contains mixed English (frontmatter, headings) and Traditional Chinese (Purpose, Process, Trigger).

**Question**: Should schema v2 upgrade normalize this to English, or preserve the bilingual intent?

**Resolution**: **Preserve bilingual** — this is not a rewrite trigger. Upgrade is Mode A+: add schema v2 sections in English; existing bilingual content remains as-is. Document in Preservation Map: "Existing Traditional Chinese sections preserved; new schema v2 sections in English."

---

## Post-merge / Release Actions

This topic does **not** trigger a repository release. No actions on `VERSION`, `README.md`, release notes, or CHANGELOG are required when Tier 2 merges to `feature/skill-migration-v1`.

The merge to `feature/skill-migration-v1` is the terminal action for this topic. Tier 3 begins by rebasing from the updated integration branch.

---

## Status / Allowed Transitions

```
planned → in_progress → review → approved → merged
```

| Status | Meaning |
|---|---|
| `planned` | Plan authored, awaiting plan-reviewer approval |
| `in_progress` | Creator/reviewer loops active for ≥1 skill |
| `review` | All 4 skills reviewer-approved, awaiting human STOP POINT 1 sign-off |
| `approved` | Human signed off, PR open on GitHub |
| `merged` | PR merged to `feature/skill-migration-v1` |

**Current status**: `planned`

This topic does not advance to `released` — no release action is scoped here.

---

## Reviewer Handoff

```json
{
  "verdict": "approved",
  "plan_path": "plan/tier-2-python-impl-skills/tier-2-python-impl-skills.plan.md",
  "reviewer_agent": "plan-reviewer",
  "round": 1,
  "blocking_issues": [],
  "non_blocking_observations": [],
  "checklist_summary": {
    "goal_non_goals": "clear and non-contradictory",
    "scope": "4 skills with complexity",
    "decisions": "D1-D4 concrete, no placeholders",
    "affected_files": "complete with Owner/Role",
    "public_contract": "no breaking changes",
    "failure_handling": "recovery paths defined",
    "test_plan": "creator+reviewer per skill",
    "validation": "runnable bash commands",
    "execution": "6 phases with dependencies",
    "blockers": "none identified",
    "open_q": "resolved (Q1, Q2)",
    "post_merge": "defined, no release action",
    "transitions": "explicit status map",
    "json_form": "well-formed",
    "rollback": "concrete options A/B/C",
    "success": "8 measurable criteria"
  }
}
```

---

## Rollback Plan

If reviewer rejects multiple skills with the same structural issue:
- Pause Tier 2 execution.
- Human and creator discuss: is this a creator bug, schema v2 ambiguity, or skill design issue?
- Option A: fix creator logic, restart Tier 2 from the rejected skill.
- Option B: adjust schema v2 policy (requires governance file change, out of scope for Tier 2).
- Option C: mark skills as needing manual hand-editing by human reviewer (escalation).

If a single skill cannot be upgraded due to missing inputs or ambiguity:
- Creator outputs detailed Preservation Map explaining blocker.
- Human decides: retry with clearer input, approve rewrite risk, or defer skill to later audit.
- Continue with remaining 3 skills rather than stopping all work.

---

## Success Criteria

✓ All 4 skills have YAML `complexity` and `risk_profile` fields.
✓ All 4 skills have `Validation` section (concise for medium/low, detailed for high).
✓ All 4 skills have `Failure Handling` section with recoverable/non-recoverable outcomes defined.
✓ All 4 skills pass agent-skill-reviewer `approved` status.
✓ No changes to governance files or VERSION.
✓ Migration tracker updated with Mode, complexity, risk_profile, and reviewer verdict for each skill.
✓ PR merged to `feature/skill-migration-v1`.
✓ No breaking changes to existing behavior contracts or downstream consumer skills.

---

## Non-Blocking Follow-Ups (for future tiers or post-Tier-2)

- If creator discovers schema v2 ambiguities affecting lower tiers → record in migration notes, defer to post-migration governance review.
- If any rewrite revealed obsolete local references → mark for cleanup in later audit.
- If pre-commit or toolconfig skills are later discovered to require Workflow State Contract → defer to post-migration refinement (not blocking Tier 2).
- If multi-agent consumer patterns emerge for pre-commit or toolconfig → document in post-migration analysis for future upgrade consideration.
