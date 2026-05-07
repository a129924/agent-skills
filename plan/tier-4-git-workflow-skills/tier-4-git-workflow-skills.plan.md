# Tier 4 — Git Workflow / Review / Commit Skills Migration
## Schema v2 upgrade: 3 skills from legacy standard to creator/reviewer-approved

---

## Status / Allowed Transitions

**Current status**: `pr-open`

| From | To | Condition |
|---|---|---|
| `planned` | `creator-in-progress` | Plan reviewer returns `approved` |
| `creator-in-progress` | `review-ready` | All 3 skills drafted by agent-skill-creator |
| `review-ready` | `reviewer-in-progress` | Reviewer subagent launched |
| `reviewer-in-progress` | `needs-rework` | agent-skill-reviewer returns `needs-rework` |
| `reviewer-in-progress` | `approved` | All 3 skills pass agent-skill-reviewer with `approved` |
| `needs-rework` | `creator-in-progress` | Creator addresses reviewer blockers |
| `approved` | `publish-in-progress` | Human approves commit + push (STOP POINT 1) |
| `publish-in-progress` | `pr-open` | PR created targeting `feature/skill-migration-v1` |
| `pr-open` | `needs-rework` | Copilot review returns blocking feedback |
| `pr-open` | `merged` | Human triggers STOP POINT 2 merge into `feature/skill-migration-v1` |
| `merged` | `terminal` | Post-merge cleanup complete |

---

## Goal / Outcome

Upgrade 3 Git workflow/review/commit skills to schema v2 standard (with `complexity`, `risk_profile`, `Validation`, `Failure Handling` sections) while preserving all existing responsibility, trigger, and process behavior. All 3 skills must reach `reviewer-approved` status before Tier 4 completion.

**Target skills**:
1. `git-commit-convention` — semantic commit message drafting and review (complexity: **medium**)
2. `git-post-merge-workflow` — post-merge cleanup and sync (complexity: **medium**)
3. `git-release-management` — strict release gate enforcement (complexity: **high**)

---

## Boundaries / Exclusions

- Do not redefine any skill's business responsibility or primary trigger.
- Do not change the existing Process / Boundaries / Inputs / Outputs behavior contracts.
- Do not merge to `feature/skill-migration-v1` until all 3 skills are reviewer-approved.
- Do not bump VERSION during this phase; defer to final integration PR.
- Do not modify `agent-skill-creator/`, `agent-skill-reviewer/`, or `agent-skill-template/` (governance files are frozen during migration).
- Do not upgrade Tier 3, 5, 6, or 7 skills in this plan.

---

## Scope

### In scope
All 3 skills are inferred as **upgrade mode (Mode A+)** — preserve existing content, supplement with schema v2 YAML fields and required sections. Rewrite (Mode B) only if creator detects structural contradictions or mixed responsibilities.

### Out of scope
See Boundaries / Exclusions.

### Per-Skill Migration Parameters

| # | Skill | Mode | Inferred Complexity | Inferred Risk Profile | Preservation Notes |
|---|---|---|---|---|---|
| 1 | `git-commit-convention` | A+ | medium | ambiguity_sensitive | Preserve split-signal logic, repair commands, and breaking-change marker rules |
| 2 | `git-post-merge-workflow` | A+ | medium | destructive_action, multi_agent_handoff, external_tooling | Preserve STOP POINT 2 gate, FF-only sync, and branch deletion defaults |
| 3 | `git-release-management` | A+ | high | destructive_action, ambiguity_sensitive, external_tooling | Preserve all release gates, emergency exception path, tagging safety, and repair guidance |

---

## Locked Decisions

### D1: Execution Model
- **Per-skill creator → reviewer loop**.
- Each skill produces review-ready draft independently.
- Reviewer approves or returns needs-rework for that skill only.
- Sequential dependency: **none** — all 3 skills can be reviewed in parallel once creator completes.

### D2: Preservation Map Triggers
For each skill, creator must output a **Preservation Map** showing:
- **Preserve**: sections kept as-is with role explained
- **Rewrite**: sections restructured; reason given
- **Remove**: sections deleted; reason given
- **Add**: new sections required by schema v2
- **Risk**: any lost behavior or implicit context downstream users should be aware of

**Rewrite trigger** (Mode B):
- Multiple responsibilities tangled together
- Trigger / do_not_use_when / boundaries mutually contradictory
- Process steps already obsolete relative to local references
- Content gap too large to supplement without guessing

### D3: Complexity & Risk Profile Inference

| Skill | Complexity | Reasoning | Risk Profile | Rationale |
|---|---|---|---|---|
| `git-commit-convention` | **medium** | Multi-path decisions: single vs split commit, repair paths (`--amend`, `git add -p`), breaking-change markers; branching on staged change set | ambiguity_sensitive | Missing context (e.g., which files are staged) materially changes the output — different commits, different subjects, different footers |
| `git-post-merge-workflow` | **medium** | Single-path cleanup with hard gate checks (STOP POINT 2, FF-only sync, branch deletion); limited branching but destructive consequence if wrong | destructive_action, multi_agent_handoff, external_tooling | Branch deletion is irreversible; FF-only sync can fail if upstream diverges; wrong branch deletion would lose commits; STOP POINT 2 is an explicit multi-agent handoff gate; git CLI is required for sync and branch operations |
| `git-release-management` | **high** | Complex multi-path: normal release gate, emergency exception path, tagging safety, version-source sync, repair guidance; gatekeeping skill with downstream release consequences | destructive_action, ambiguity_sensitive, external_tooling | Tagging and releasing wrong commits is irreversible; ambiguous PR/branch state can lead to releasing unreviewed code; emergency exceptions are high-stakes decisions; relies on external tooling (gh CLI, CI APIs) for gate-signal retrieval and tagging commands |

**Policy implications**:
- `git-commit-convention` (medium): `Validation` recommended; `Failure Handling` recommended.
- `git-post-merge-workflow` (medium): `Validation` required (destructive_action triggers conditional requirement); `Failure Handling` required.
- `git-release-management` (high): `Validation` required; `Failure Handling` required; `Workflow State Contract` recommended (gatekeeping skill that blocks or permits downstream work).

### D4: YAML / Body Consistency Check
Creator must ensure:
- YAML `complexity`, `risk_profile`, `use_when`, `do_not_use_when` align with markdown body.
- No contradiction between YAML and body content.
- For `git-release-management`: YAML `do_not_use_when` must match the explicit bypass-prevention rules in `Boundaries`.
- Contradiction = creator marks as needs-rework and explains.

### D5: git-release-management Risk Gate
`git-release-management` is a **gatekeeping skill** — its primary function is to block unsafe releases. Creator must preserve:
- All blocking conditions (must not soften or make optional)
- Emergency exception path (must stay explicit with human-approval gate)
- Tagging safety rules (must not allow unilateral tagging)
- Version-source synchronization checks

If any of these cannot be preserved in Mode A+, creator must flag as BLOCKED and output a detailed Preservation Map before proceeding.

---

## Artifact Paths

| Artifact | Path | Owner | Role |
|---|---|---|---|
| tier-4 plan | `plan/tier-4-git-workflow-skills/tier-4-git-workflow-skills.plan.md` | Planning actor | Repo-visible execution contract for this topic |
| git-commit-convention | `.github/skills/git-commit-convention/SKILL.md` | creator | schema v2 upgrade |
| git-post-merge-workflow | `.github/skills/git-post-merge-workflow/SKILL.md` | creator | schema v2 upgrade |
| git-release-management | `.github/skills/git-release-management/SKILL.md` | creator | schema v2 upgrade |
| migration tracker | `files/migration-tracker.md` | main-agent | updated per skill after reviewer approval |

**Stable-library surfaces not touched**: `README.md`, `VERSION`, release notes, `.github/copilot-instructions.md`, and all governance files (`agent-skill-creator/`, `agent-skill-reviewer/`, `agent-skill-template/`) are explicitly out of scope for this topic.

---

## Public Contract

When this plan is complete:
- All 3 skills have `complexity`, `risk_profile`, and required schema v2 sections.
- All maintain their original responsibility, trigger, process, and boundary semantics.
- `git-release-management` preserves all blocking conditions and emergency exception gates unchanged.
- All pass `agent-skill-reviewer` with verdict `approved`.
- Migration tracker records Mode (A+), complexity, risk_profile, and any rewrite notes per skill.
- No breaking changes to existing workflow contracts.

---

## Failure Handling

### Missing Context
- Creator cannot infer a skill's complexity or risk profile → mark as INCOMPLETE, list missing signals.

### Ambiguous Requirement
- If creator judges a skill is "too tangled to supplement" → output Preservation Map; human decides whether to retry with clearer input or approve the rewrite risk.

### Reviewer Rejection
- Reviewer returns needs-rework → creator revises and resubmits to same reviewer.
- If revision requires rewriting beyond initial Mode A+ scope → creator outputs new Preservation Map; human approves before proceeding.

### Risk Gate Failures
- `git-release-management` cannot preserve its blocking conditions in Mode A+ → mark as BLOCKED, output detailed Preservation Map, require human decision before proceeding.

---

## Validation / Acceptance Checks

No new tests. Validation via:
1. **Creator dry-run**: each skill outputs review-ready SKILL.md with all required schema v2 sections present.
2. **Reviewer gates**: each skill passes agent-skill-reviewer checklist (YAML/body alignment, complexity match, examples sufficiency, risk gates respected).
3. **Special gate for git-release-management**: reviewer must explicitly confirm all blocking conditions are preserved and no release gate was softened.
4. **Human sign-off**: PR description includes Preservation Map for any Mode B rewrites.

```bash
# Verify YAML metadata fields exist
cd .github/skills/<skill-name>
cat SKILL.md | grep -E '^(complexity|risk_profile|inputs|outputs|use_when|do_not_use_when):'

# Verify Validation section (required for high; recommended for medium)
grep -A 15 '^# Validation' SKILL.md | head -18

# Verify Failure Handling section (required for high; required for medium with destructive_action)
grep -A 15 '^# Failure Handling' SKILL.md | head -18

# Verify at least one positive and one negative example
grep -E '^- \*\*(Positive|Negative)\*\*:' SKILL.md | wc -l

# For git-release-management only: verify blocking conditions preserved
grep -E '(BLOCK|block|gate|must not|forbidden|prevent)' SKILL.md | head -15
```

---

## Inputs

- All 3 existing `SKILL.md` files (legacy format, no schema v2 fields)
- `agent-skill-creator/folder-contract.md` (schema v2 authority)
- `agent-skill-reviewer/review-checklist.md` (reviewer gate authority)
- This plan (execution contract)

---

## Implementation Steps

1. Plan reviewer approves this plan → branch `migrate/tier-4-git-workflow-skills` ready
2. Creator subagents launched in parallel: git-commit-convention, git-post-merge-workflow
3. Creator subagent for git-release-management (separate due to higher risk — run after D5 gate confirmed)
4. Reviewer subagents launched in parallel for all 3 once creator completes
5. Migration tracker updated after all 3 reviewers approve
6. STOP POINT 1 → human approves commit + push
7. PR opened → Copilot review → feedback addressed if needed
8. STOP POINT 2 → human merges PR into `feature/skill-migration-v1`

**Note**: git-release-management may be processed after git-commit-convention and git-post-merge-workflow if the creator detects structural risks requiring human pre-approval (per D5 risk gate).

---

## Post-merge / Release Actions

No release action required at this stage. VERSION bump and README update are deferred to the final integration PR (`feature/skill-migration-v1 → dev/main`).

After merge into `feature/skill-migration-v1`:
- Delete remote and local branch `migrate/tier-4-git-workflow-skills`
- Fast-forward sync `feature/skill-migration-v1`
- Update `files/migration-tracker.md` Tier 4 summary row

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
