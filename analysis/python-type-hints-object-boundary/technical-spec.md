# Technical Specification: python-type-hints-object-boundary

> Translated from:
> `analysis/python-type-hints-object-boundary/requirements.md`
> Status: **READY FOR PLAN CREATION**
> Posture: pessimistic implementer — hidden scope, review cost, and rollback
> triggers are stated explicitly.

---

## Baseline Gating Check

- `requirements.md` exists and is marked FROZEN: ✅
- All 6 requirements name actor, condition, observable result, and decision
  rule: ✅
- Contradictions are resolved: ✅
- Topic boundaries are explicit: ✅
- No unresolved ambiguity requires rollback to `business-intent-alignment`: ✅

Translation proceeds.

---

## Requirement-to-Technical Mapping

### R1 — Hard prohibition on weakening known domain contracts to `object`

**Technical tasks:**
- `SKILL.md`: add an explicit rule in Process and Examples that changing a
  repo-owned/domain type to `object` is invalid outside true untrusted
  boundaries or narrowing-helper inputs
- `SKILL.md`: add validation language that asks whether a repo-owned type
  already exists before accepting `object`
- `examples.md`: include a negative example where a known alias/value type/model
  is incorrectly weakened to `object`

**Artifacts:** `.github/skills/python-type-hints-strict/SKILL.md`,
`.github/skills/python-type-hints-strict/examples.md`

**Dependency note:** The rule must stay within strict-typing policy and not
invent new model-selection guidance.

---

### R2 — Narrow definition of allowed `object` positions

**Technical tasks:**
- `reference.md`: add an `object`-specific subsection that names the allowed
  entry positions: decoder output, validator input, type-guard input, and
  similar narrowing helpers
- `SKILL.md`: add process wording that `object` is boundary-only and must be
  narrowed quickly
- `examples.md`: add a positive example showing `object` at a narrowing/helper
  input that returns or recovers a precise domain type

**Artifacts:** `.github/skills/python-type-hints-strict/SKILL.md`,
`.github/skills/python-type-hints-strict/reference.md`,
`.github/skills/python-type-hints-strict/examples.md`

**Feasibility note:** This is straightforward authoring work, but the allowed
boundary list must stay narrow enough that future agents cannot reinterpret it
as permission for ordinary API types.

---

### R3 — Justification requirement for every remaining `object` usage

**Technical tasks:**
- `reference.md`: require a short justification for each accepted `object` site,
  naming the boundary or narrowing role it serves
- `SKILL.md`: treat missing justification as a validation failure, not optional
  guidance
- `examples.md`: show that "easier type checking" or "not sure of the type" is
  not an acceptable justification

**Artifacts:** `.github/skills/python-type-hints-strict/SKILL.md`,
`.github/skills/python-type-hints-strict/reference.md`,
`.github/skills/python-type-hints-strict/examples.md`

**Operational burden:** Reviewer must now evaluate justification quality, not
only syntax. That is acceptable because the topic is medium complexity and the
review burden is localized to one skill folder.

---

### R4 — Preference order must favor repo-owned or refined explicit types

**Technical tasks:**
- `reference.md`: encode the preference ladder explicitly:
  `repo-owned type -> explicit refinement / alias -> boundary-only object`
- `SKILL.md`: reinforce that `object` must not be used to avoid understanding
  the domain model
- `examples.md`: show the correct alternative when an existing alias/value type
  should be reused instead of collapsing to `object`

**Artifacts:** `.github/skills/python-type-hints-strict/SKILL.md`,
`.github/skills/python-type-hints-strict/reference.md`,
`.github/skills/python-type-hints-strict/examples.md`

**Cost note:** Low-to-medium writing effort. The main risk is over-specifying how
to create new runtime models; the wording must stay on typing-contract
refinement, not object-model selection.

---

### R5 — Scope must remain strict-typing guidance, not model selection

**Technical tasks:**
- Preserve the existing `python-model-selection` redirect in `SKILL.md`
- Ensure any new `object` guidance does not choose `Enum`, `dataclass`, `ABC`,
  or `Protocol` on behalf of the user
- Keep `reference.md` focused on type-hint policy, not runtime model mechanics

**Artifacts:** `.github/skills/python-type-hints-strict/SKILL.md`,
`.github/skills/python-type-hints-strict/reference.md`

**Architecture note:** This topic fits the repository's single-responsibility
skill model as long as the redirect remains explicit.

---

### R6 — Positive and negative examples must make the rule executable

**Technical tasks:**
- `SKILL.md`: strengthen top-level positive/negative examples to mention `object`
  explicitly
- `examples.md`: add one concise valid example and one concise invalid example
  for the `object` boundary rule without drifting into unrelated typing topics
- Keep all three files semantically aligned so the same valid/invalid line is
  visible in contract, reference, and examples

**Artifacts:** `.github/skills/python-type-hints-strict/SKILL.md`,
`.github/skills/python-type-hints-strict/examples.md`,
`.github/skills/python-type-hints-strict/reference.md`

**Risk flag:** Cross-file inconsistency is the most likely failure mode. If one
file permits a broader use of `object` than another, reviewer should return
`needs-rework`.

---

## Artifact Plan

| Artifact | Path | Authoring notes |
| --- | --- | --- |
| Requirements baseline | `analysis/python-type-hints-object-boundary/requirements.md` | Frozen business baseline for the topic |
| Technical specification | `analysis/python-type-hints-object-boundary/technical-spec.md` | Execution-facing source of truth for the topic plan |
| Topic plan | `plan/python-type-hints-object-boundary/python-type-hints-object-boundary.plan.md` | Repo-visible execution contract; must map 100% to this technical spec |
| Skill contract | `.github/skills/python-type-hints-strict/SKILL.md` | Add hard invalid rule, tightened validation, and concise examples |
| Reference rules | `.github/skills/python-type-hints-strict/reference.md` | Add object-specific boundary rules, preference order, and justification requirement |
| Example scenarios | `.github/skills/python-type-hints-strict/examples.md` | Add allowed-boundary and invalid-weakening scenarios |

**Explicit no-change paths:** `README.md`, `VERSION`,
`.github/copilot-instructions.md`, and any new test harness are outside this
topic unless a later publish topic chooses otherwise.

---

## Architecture Compliance Self-Check

| Check | Result | Notes |
| --- | --- | --- |
| Existing skill path remains `.github/skills/` | ✅ FIT | Matches current active workflow path during transition |
| Single responsibility | ✅ FIT | Topic tightens strict-typing policy only |
| Required local files remain the same | ✅ FIT | `SKILL.md`, `reference.md`, `examples.md`; no new companion file required |
| Stable-library surfaces touched now | ✅ NO | No `README.md`/`VERSION` change planned in this topic |
| Creator/reviewer role separation preserved | ✅ FIT | Plan stops before implementation approval; later execution still uses creator and reviewer separately |
| Analysis-layer compatibility | ✅ FIT | Both analysis artifacts exist, so downstream plan can run in strict mode |

No architecture waiver is required.

---

## Feasibility Assessment

### Cost-of-realization

| Workstream | Complexity | Notes |
| --- | --- | --- |
| `SKILL.md` update | Medium | Needs careful wording in Process, Examples, and Validation |
| `reference.md` update | Medium | Must distinguish allowed boundary use from forbidden convenience fallback |
| `examples.md` update | Low-Medium | Short new scenarios, but they must be semantically sharp |
| Cross-file alignment review | Medium | Highest risk is contradictory wording between contract/reference/examples |

### Sequencing constraint

1. Freeze requirements baseline first
2. Create technical spec
3. Create topic plan in strict mode
4. Only then begin creator drafting of the skill files

### Operational burden

- Reviewer must check semantic alignment across three files, not only local line
  edits
- No migration, release, or stable-library burden is introduced in this topic

---

## Material Conflicts and Rollback Triggers

No material conflict currently blocks planning. Roll back to alignment if any of
these conditions appear during implementation:

1. A new requirement tries to make `python-type-hints-strict` choose concrete
   runtime model forms (`Enum`, `dataclass`, `ABC`, `Protocol`) instead of only
   typing policy
2. A proposed implementation requires `README.md` or `VERSION` changes even
   though this topic is declared non-stable
3. The allowed `object` boundary list grows beyond untrusted-boundary /
   narrowing-helper entry points without a new frozen requirement baseline

If any rollback trigger fires, stop creator work and return to
`business-intent-alignment` or plan repair instead of stretching the topic
silently.

---

## Planning Handoff Summary

The downstream topic plan must:

- operate in **strict mode** because both analysis artifacts exist
- map its implementation steps 100% to the three target skill files named above
- declare explicit non-stable intent
- stop after repo-visible planning until a human resumes creator execution
