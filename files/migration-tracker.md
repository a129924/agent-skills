# Agent Skill Migration Tracker
## Schema v2 Migration: legacy skills → new creator/reviewer standard

**Integration branch**: `feature/skill-migration-v1`
**Started**: 2026-05-06
**Target**: 45 skills to reviewer-approved status

---

## Progress Summary

| Tier | Description | Skills | Done | Status |
|---|---|---|---|---|
| 1 | Python Planning / Review | 9 | 9 | ✅ complete |
| 2 | Python Implementation / Code-modification | 5 | 4 | ✅ complete (4/5; python-testing-pytest deferred) |
| 3 | Python Helper / Reference | 20 | 20 | ✅ complete |
| 4 | Git Workflow / Review / Commit | 3 | 3 | ✅ complete |
| 5 | Git Helper | 1 | 1 | ✅ complete |
| 6 | Other 高風險 | 5 | 5 | ✅ complete |
| 7 | Other 低風險 | 2 | 2 | ✅ complete |
| **Total** | | **45** | **44** | 🔄 In Progress (44/45; `python-testing-pytest` deferred) |

---

## Tier 1 — Python Planning / Review

Branch: `migrate/tier-1-python-plan-skills`
PR target: `feature/skill-migration-v1`

| Skill | Mode | Complexity | Risk Profile | Reviewer Verdict | Status | Notes |
|---|---|---|---|---|---|---|
| `python-plan-authoring` | A+ | high | ambiguity_sensitive, multi_agent_handoff | ✅ approved | ✅ done | warnings fixed |
| `python-plan-review` | A+ | high | ambiguity_sensitive, multi_agent_handoff | ✅ approved | ✅ done | Workflow State Contract gap noted (non-blocking) |
| `python-code-review` | A+ | high | ambiguity_sensitive, multi_agent_handoff | ✅ approved | ✅ done | YAML do_not_use_when aligned to 6 body entries |
| `python-implementation-review` | A+ | high | ambiguity_sensitive, multi_agent_handoff | ✅ approved | ✅ done | Workflow State Contract gap noted (non-blocking) |
| `python-blueprint-authoring` | A+ | high | ambiguity_sensitive, multi_agent_handoff, destructive_action | ✅ approved | ✅ done | YAML do_not_use_when aligned; Workflow State Contract gap noted |
| `python-blueprint-review` | A+ | high | ambiguity_sensitive, multi_agent_handoff, destructive_action | ✅ approved | ✅ done | Workflow State Contract gap noted (non-blocking) |
| `python-retrofit-plan-authoring` | A+ | high | ambiguity_sensitive, multi_agent_handoff, destructive_action | ✅ approved | ✅ done | Workflow State Contract gap noted (non-blocking) |
| `python-retrofit-plan-review` | A+ | high | ambiguity_sensitive, multi_agent_handoff, destructive_action | ✅ approved | ✅ done | severity marker added to Ambiguous Requirement handler |
| `python-tdd-test-authoring` | A+ | high | ambiguity_sensitive, multi_agent_handoff, code_modification | ✅ approved | ✅ done | negative example clarified |

---

## Tier 2 — Python Implementation / Code-modification

Branch: `migrate/tier-2-python-impl-skills`
PR target: `feature/skill-migration-v1`

| Skill | Mode | Complexity | Risk Profile | Reviewer Verdict | Status | Notes |
|---|---|---|---|---|---|---|
| `python-project-init-greenfield` | A+ | high | destructive_action, multi_agent_handoff | ✅ approved | ✅ done | |
| `python-project-retrofit` | A+ | high | destructive_action, multi_agent_handoff, code_modification | ✅ approved | ✅ done | |
| `python-pre-commit` | A+ | medium | code_modification, external_tooling | ✅ approved | ✅ done | |
| `python-pyproject-toolconfig` | A+ | medium | code_modification | ✅ approved | ✅ done | complexity raised low → medium (code_modification requires medium+) |
| `python-testing-pytest` | — | — | — | — | 🔲 deferred | not in Tier 2 scope |

---

## Tier 3 — Python Helper / Reference

Branch: `migrate/tier-3-python-helper-skills`
PR target: `feature/skill-migration-v1`

| Skill | Mode | Complexity | Risk Profile | Reviewer Verdict | Status | Notes |
|---|---|---|---|---|---|---|
| `python-naming` | A+ | low | — | ✅ approved | ✅ done | |
| `python-docstrings` | A+ | medium | ambiguity_sensitive | ✅ approved | ✅ done | PR #59 reviewed; 7 BLOCKERs fixed |
| `python-type-hints-strict` | A+ | low | — | ✅ approved | ✅ done | |
| `python-control-flow` | A+ | low | — | ✅ approved | ✅ done | |
| `python-comprehensions` | A+ | low | — | ✅ approved | ✅ done | |
| `python-generators-iterators` | A+ | low | — | ✅ approved | ✅ done | |
| `python-context-management` | A+ | medium | — | ✅ approved | ✅ done | |
| `python-async-await` | A+ | medium | — | ✅ approved | ✅ done | |
| `python-decorators` | A+ | low | — | ✅ approved | ✅ done | |
| `python-descriptors-attribute-access` | A+ | medium | — | ✅ approved | ✅ done | |
| `python-data-model-methods` | A+ | low | — | ✅ approved | ✅ done | |
| `python-operator-overloading` | A+ | low | — | ✅ approved | ✅ done | |
| `python-class-design` | A+ | low | — | ✅ approved | ✅ done | |
| `python-api-signature` | A+ | medium | — | ✅ approved | ✅ done | |
| `python-module-boundaries` | A+ | medium | — | ✅ approved | ✅ done | |
| `python-library-architecture` | A+ | medium | ambiguity_sensitive | ✅ approved | ✅ done | |
| `python-package-layout` | A+ | low | — | ✅ approved | ✅ done | |
| `python-error-handling` | A+ | low | — | ✅ approved | ✅ done | |
| `python-serialization-boundaries` | A+ | medium | ambiguity_sensitive | ✅ approved | ✅ done | |
| `python-model-selection` | A+ | low | — | ✅ approved | ✅ done | |

---

## Tier 4 — Git Workflow / Review / Commit

Branch: `migrate/tier-4-git-workflow-skills`
PR target: `feature/skill-migration-v1`

| Skill | Mode | Complexity | Risk Profile | Reviewer Verdict | Status | Notes |
|---|---|---|---|---|---|---|
| `git-commit-convention` | A+ | medium | ambiguity_sensitive | ✅ approved | ✅ done | |
| `git-post-merge-workflow` | A+ | medium | destructive_action, multi_agent_handoff, external_tooling | ✅ approved | ✅ done | |
| `git-release-management` | A+ | high | destructive_action, ambiguity_sensitive, external_tooling | ✅ approved | ✅ done | PR #58 reviewed; 5 fixes applied (C1-C5) |

---

## Tier 5 — Git Helper

Branch: `migrate/tier-5-git-helper-skills`
PR target: `feature/skill-migration-v1`

| Skill | Mode | Complexity | Risk Profile | Reviewer Verdict | Status | Notes |
|---|---|---|---|---|---|---|
| `git-branch-naming` | A+ | medium | ambiguity_sensitive | ✅ approved | ✅ done | PR #60 merged |

---

## Tier 6 — Other 高風險

Branch: `migrate/tier-6-other-high-risk`
PR target: `feature/skill-migration-v1`

| Skill | Mode | Complexity | Risk Profile | Reviewer Verdict | Status | Notes |
|---|---|---|---|---|---|---|
| `plan-creator` | A+ | high | ambiguity_sensitive, multi_agent_handoff | ✅ approved | ✅ done | `reference.md` split into focused overview + `references/`; PR #61 feedback clarified Workflow State Contract does not alter fixed JSON verdict schema |
| `plan-reviewer` | A+ | high | ambiguity_sensitive, multi_agent_handoff | ✅ approved | ✅ done | fixed-schema JSON verdict contract preserved through PR #61 follow-up |
| `sense-env-scaffold` | A+ | medium | external_tooling | ✅ approved | ✅ done | non-blocking warning: Validation lacks a Quality Checks tier |
| `copilot-instructions-init` | A+ | high | ambiguity_sensitive, code_modification | ✅ approved | ✅ done | non-blocking note: recoverable gates could rename `HARD STOP` to `BLOCKED` for consistency |
| `business-to-technical-translation` | A+ | medium | ambiguity_sensitive | ✅ approved | ✅ done | reviewer noted migration was effectively a no-op because the skill already matched the required contract shape |

---

## Tier 7 — Other 低風險

Branch: `migrate/tier-7-other-low-risk`
PR target: `feature/skill-migration-v1`

| Skill | Mode | Complexity | Risk Profile | Reviewer Verdict | Status | Notes |
|---|---|---|---|---|---|---|
| `business-intent-alignment` | A+ | medium | ambiguity_sensitive | ✅ approved | ✅ done | contradiction forcing and measurability baseline contract preserved; PR #62 merged |
| `plan-step-tracker` | A+ | medium | external_tooling | ✅ approved | ✅ done | CLI command contract and blocking semantics preserved; `reference.md` retained as focused companion file; PR #62 merged with follow-up wording fixes |

---

## Migration Notes

Any governance rule adjustments discovered during migration should be recorded here
(not directly patched in creator/reviewer/template during migration).

- Tier 6 surfaced one governance correction worth preserving: `plan-creator/reference.md` had to be split once it exceeded the "more than 3 logical topics" threshold, while `reference.md` remained the focused companion overview.
- PR #61 also clarified that `plan-reviewer` workflow-state fields are internal coordination metadata only and must not widen the fixed JSON verdict schema consumed downstream.
