# Topic Plan — `python-descriptors-attribute-access`

## Analysis Layer Routing

> ⚡ **STRICT MODE ACTIVE**
>
> Both analysis artifacts exist and are frozen:
> - `analysis/python-descriptors-attribute-access/requirements.md` (R1–R10, frozen 2026-05-04)
> - `analysis/python-descriptors-attribute-access/technical-spec.md` (T1–T5, frozen 2026-05-04)
>
> This plan maps 100% to `technical-spec.md`. Analysis artifacts outrank all
> chat-time instructions. Any deviation from the technical spec requires an
> explicit human `override` statement before the change takes effect.

---

## Goal / Outcome

A stable, repo-visible Agent Skill at `.github/skills/python-descriptors-attribute-access/` that:

- teaches Python developers to choose the **least powerful attribute access mechanism** that correctly expresses the intended attribute semantics (R1 mechanism ladder)
- covers `@property`, `@cached_property`, custom descriptor protocol, and attribute hook methods (`__getattr__`, `__setattr__`, `__getattribute__`)
- frames `__getattr__` / `__setattr__` / `__getattribute__` as **discouraged with strict escape hatch conditions** (not forbidden, not freely allowed)
- ships with mandatory `examples.md` covering six branching-decision scenarios and two high-risk anti-patterns
- is approved by an independent reviewer subagent and published with README row and VERSION bump to `0.37.0`

---

## Scope

**In scope** (mapped from requirements R1–R10 and technical-spec artifact list):

- `@property` / getter / setter / deleter discipline (R2)
- `@cached_property` for lazy computed attributes (R3) — Python 3.8+
- Custom descriptor protocol: `__get__`, `__set__`, `__delete__` (R4)
- `__set_name__` for descriptor reusability (R5)
- Data descriptor vs non-data descriptor lookup priority (R6)
- `__getattr__` — discouraged, 5-condition escape hatch (R7)
- `__setattr__` / `__delattr__` — discouraged, same 5-condition escape hatch (R8)
- `__getattribute__` — highest-risk, near-absolute discouragement (R9)
- `__init__` initialization pitfall for `__getattr__` / `__setattr__` (R10)
- Mechanism selection ladder (R1): plain → `@property` → `@cached_property` → custom descriptor → `__getattr__` → `__setattr__` → `__getattribute__`

**Out of scope** (from requirements non-goals):

- `__slots__` memory optimization → `python-class-design`
- Metaclass attribute handling → out of repo skill scope
- `__new__` / object lifecycle → `python-class-design`
- ORM-specific descriptor patterns (Django models, SQLAlchemy)
- Framework-grade instrumentation
- Schema validation frameworks
- Cross-field domain validation → `python-error-handling`
- `functools` beyond `@cached_property`
- `@property` decorator-protocol mechanics (how decorators wrap functions) → `python-decorators`
- `__init__` ownership and general object construction rules → `python-data-model-methods` (R10 pitfall context: pitfall is covered here, but `__init__` design belongs there)

---

## Locked Decisions

These decisions are frozen from the analysis layer and must not be rediscovered during creator work:

| Decision | Value | Source |
| --- | --- | --- |
| `__getattr__`/`__setattr__` framing | Discouraged with strict escape hatch (not forbidden) | requirements.md R7, R8 |
| Escape hatch condition count | 5 conditions — must appear as checklist, not prose | requirements.md R7, technical-spec T4.2 |
| `__getattribute__` framing | Highest-risk, near-absolute discouragement | requirements.md R9 |
| `examples.md` | Required (not optional) — 6 sections | technical-spec T5 |
| `reference.md` + `references/` split | Required — 4 logical topics exceed 1,000-token threshold | technical-spec Artifact Paths |
| Python version floor | 3.6+ for descriptor protocol; 3.8+ for `@cached_property` | requirements.md Assumptions |
| `@cached_property` ownership | This skill owns it; future `python-functools-patterns` will signpost here | technical-spec Conflict Detection |
| Setter validation boundary | Single-attribute invariant only; cross-field → `python-error-handling` | requirements.md R2 |
| `python-decorators` | `@property` is syntactically a decorator; decorator-protocol mechanics are not this skill's domain → signpost | requirements.md R2 |
| `python-data-model-methods` | `__init__` construction rules; R10 pitfall is covered here (safe internal state access) but general `__init__` design policy belongs there | requirements.md R10 |
| Topic affects stable library | Yes — README row + VERSION bump | technical-spec Plan Contract Anchors |

---

## Boundaries / Exclusions

**Role boundaries**:
- Creator owns all 7 new skill files
- Main Agent owns README row addition and VERSION bump
- Reviewer subagent provides independent verdict; Main Agent does not self-approve

**Scope boundaries**:
- Any `__slots__` content → rollback trigger RT-1
- Any ORM/framework-specific descriptor content → rollback trigger RT-2
- R7 escape hatch in prose instead of checklist → rollback trigger RT-3
- Cross-field validation in `@property` setter section → rollback trigger RT-4
- Metaclass attribute content → rollback trigger RT-5
- `__getattribute__` without strong discouragement → rollback trigger RT-6
- `@property` decorator-protocol mechanics → signpost to `python-decorators`, do not author here
- `__init__` design rules beyond R10 pitfall → signpost to `python-data-model-methods`, do not author here

---

## Status / Allowed Transitions

- **Current**: `planned`
- **Execution model**: canonical creator → reviewer → publish → merge path with stable-library release action
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
  - `publish-in-progress` → `merged`
  - `pr-open` → `needs-rework`
  - `pr-open` → `merged`
  - `merged` → `released`

**Routing notes**:

- Phase 4.5 rule applies: README row and VERSION bump occur at `publish-in-progress`, before PR creation, not after merge.
- STOP POINT 1 is required before any commit or push.
- STOP POINT 2 is required after merge handoff; only an explicit human resume message activates post-merge release actions.

---

## Artifact Paths

| Artifact | Path | Owner | Role |
| --- | --- | --- | --- |
| Topic plan | `plan/python-descriptors-attribute-access/python-descriptors-attribute-access.plan.md` | Planning actor | Repo-visible execution contract |
| Requirements baseline | `analysis/python-descriptors-attribute-access/requirements.md` | Analysis layer | Frozen business baseline (R1–R10) |
| Technical spec | `analysis/python-descriptors-attribute-access/technical-spec.md` | Analysis layer | Frozen technical baseline (T1–T5) |
| Skill contract | `.github/skills/python-descriptors-attribute-access/SKILL.md` | Creator | Primary skill instruction contract |
| Reference overview | `.github/skills/python-descriptors-attribute-access/reference.md` | Creator | Short navigation index to `references/` |
| Mechanism ladder | `.github/skills/python-descriptors-attribute-access/references/mechanism-ladder.md` | Creator | R1 — 7-rung decision criteria (T1.2) |
| Property & cached_property | `.github/skills/python-descriptors-attribute-access/references/property-and-cached-property.md` | Creator | R2, R3 — property discipline and lazy attributes (T2) |
| Custom descriptors | `.github/skills/python-descriptors-attribute-access/references/custom-descriptors.md` | Creator | R4, R5, R6 — custom descriptor protocol (T3) |
| Attribute hooks | `.github/skills/python-descriptors-attribute-access/references/attribute-hooks.md` | Creator | R7, R8, R9, R10 — discouraged hooks and pitfalls (T4) |
| Examples | `.github/skills/python-descriptors-attribute-access/examples.md` | Creator | Required — 6 branching scenarios (T5) |
| README row | `README.md` | Main Agent | New row: `python-descriptors-attribute-access` |
| VERSION | `VERSION` | Main Agent | Bump `0.36.0` → `0.37.0` |

**Artifact path notes**:

- `README.md` must receive a new table row for this skill before PR creation (`publish-in-progress` timing).
- `VERSION` must be bumped from `0.36.0` to `0.37.0` before PR creation.
- `.github/copilot-instructions.md` is **not modified** by this topic.
- Any work outside the listed paths constitutes scope drift and must be stopped.

---

## Stable Library Metadata

- **README row**: new row in the Python skills table — `python-descriptors-attribute-access`
- **VERSION bump**: `0.36.0` → `0.37.0` (MINOR — new stable skill added)
- **Timing**: `publish-in-progress` — both `README.md` and `VERSION` changes are committed before PR creation, not deferred to post-merge
- **Rationale**: this skill adds a new stable skill to the repo's Python library; MINOR bump is required per repo SemVer convention
- **Tag**: `v0.37.0` created and pushed at post-merge release step

---

## Implementation Steps

Steps are sequenced per technical-spec dependency order (T3 before T4):

1. **Author `SKILL.md`** — include 9 required sections (frontmatter, Purpose, Trigger, Inputs, Process, Examples, Outputs, Boundaries, Local references). Process section must reference the R1 mechanism ladder. Python 3.8+ boundary for `@cached_property` must appear in Boundaries. Local references must list all 4 `references/` files with their roles. SKILL.md must include cross-skill signposts to: `python-decorators` (decorator mechanics boundary), `python-class-design` (`__slots__`, `__new__`), `python-error-handling` (cross-field validation), `python-data-model-methods` (`__init__` construction rules).

2. **Author `reference.md`** — short navigation overview only. Points readers to the four topic-specific reference files. Must not duplicate content from `references/`.

3. **Author `references/mechanism-ladder.md`** — R1 ladder with 7 rungs, upgrade criteria for each rung, and "unjustified skip" signal (T1.2).

4. **Author `references/property-and-cached-property.md`** — `@property` discipline (R2), `@cached_property` comparison (R3), setter validation boundary rule, Python 3.8+ gate, signpost to `python-error-handling` for cross-field validation (T2.1–T2.3).

5. **Author `references/custom-descriptors.md`** — upgrade criteria from `@property` (R4), `__set_name__` with before/after example (R5), data vs non-data lookup priority table (R6) (T3.1–T3.3).

6. **Author `references/attribute-hooks.md`** — `__getattr__` discouraged framing with 5-condition escape hatch checklist (R7; conditions are items 1–5 of requirements.md R7), `__setattr__`/`__delattr__` (R8), `__getattribute__` near-absolute discouragement (R9), `__init__` pitfall with `object.__getattribute__` fix (R10). For R10, signpost to `python-data-model-methods` for general `__init__` design; this file covers only the attribute-hook-specific initialization hazard. (T4.1–T4.4)

7. **Author `examples.md`** — required 6 sections:
   - S1: Ladder selection walkthrough
   - S2: `@property` setter validation — in-scope vs out-of-scope
   - S3: Custom descriptor with `__set_name__` (before/after)
   - S4: Data vs non-data lookup priority gotcha
   - S5: `__getattr__` escape hatch — compliant proxy vs non-compliant convenience
   - S6: `__init__` pitfall — `Broken` vs `Safe` (also referenced from `references/attribute-hooks.md`) (T5.1–T5.2)

---

## Validation / Acceptance Checks

- [ ] `SKILL.md` contains all 9 required sections including YAML frontmatter
- [ ] `SKILL.md` Local references lists all 4 `references/` files with their roles
- [ ] `SKILL.md` Boundaries states Python 3.8+ requirement for `@cached_property`
- [ ] `references/mechanism-ladder.md` presents the 7-rung ladder with upgrade criteria
- [ ] `references/attribute-hooks.md` R7 escape hatch is a 5-item checklist, not prose
- [ ] `references/attribute-hooks.md` `__getattribute__` uses near-absolute discouragement language
- [ ] `examples.md` contains all 6 required sections with correct/incorrect code pairs
- [ ] `examples.md` S6 `Broken`/`Safe` pair matches the `object.__getattribute__` fix in `references/attribute-hooks.md`
- [ ] Rollback triggers RT-1 through RT-6 were checked and none triggered
- [ ] `README.md` has the new `python-descriptors-attribute-access` row
- [ ] `VERSION` reads `0.37.0`
- [ ] No content from the excluded scope list (`__slots__`, ORM, metaclass, cross-field validation) appears

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

This topic declares a release action. After the user confirms merge:

1. Sync local `dev` branch with `git pull --ff-only origin dev`
2. Delete remote branch: `git push origin --delete feat/andrew/python-descriptors-attribute-access`
3. Delete local branch: `git branch -d feat/andrew/python-descriptors-attribute-access`
4. Verify `VERSION` reads `0.37.0` and `README.md` contains the `python-descriptors-attribute-access` row
5. Create annotated tag: `git tag -a v0.37.0 -m "release: python-descriptors-attribute-access stable skill"`
6. Push tag: `git push origin v0.37.0`

---

## Open Questions / Unresolved Items

None. All scope, boundary, artifact path, stable-library timing, analysis-layer routing, and release decisions are resolved.
