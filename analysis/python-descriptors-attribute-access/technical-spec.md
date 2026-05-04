# Technical Specification — `python-descriptors-attribute-access`

**Status**: FROZEN  
**Source baseline**: `analysis/python-descriptors-attribute-access/requirements.md` (all R1–R10 resolved)  
**Produced at**: 2026-05-04  
**Posture**: pessimistic implementer — hidden coupling, operational cost, and migration burden assumed until disproven

---

## Requirement-to-Technical Mapping

### R1 — Mechanism Selection Ladder → SKILL.md + `references/mechanism-ladder.md`

**Minimum realization**:
- `SKILL.md` Process section must state the 7-rung ladder as the primary decision entry point
- `references/mechanism-ladder.md` expands the decision criteria per rung: when each rung is sufficient, what forces an upgrade, and what constitutes an unjustified skip
- The ladder must be renderable as a readable ordered list, not hidden in prose

**Technical tasks**:
- T1.1: author `SKILL.md` Process section with ladder reference
- T1.2: author `references/mechanism-ladder.md` with rung-by-rung upgrade criteria

**Cost**: low. Purely documentation; no runtime or integration dependencies.

---

### R2 + R3 — `@property` and `@cached_property` → `references/property-and-cached-property.md`

**Minimum realization**:
- One reference file covering both mechanisms: when to use `@property` vs `@cached_property`, the setter validation boundary rule (single-attribute invariant only), and the computed-once vs always-recomputed distinction
- Python version gate: `@cached_property` requires **3.8+** — must be stated explicitly in this file and in `SKILL.md` Boundaries

**Technical tasks**:
- T2.1: author `references/property-and-cached-property.md` with property/cached_property comparison table
- T2.2: document setter validation boundary (single-attribute invariant only; cross-field validation is out of scope — signpost to `python-error-handling`)
- T2.3: state Python 3.8+ version requirement for `@cached_property` in `SKILL.md`

**Cost**: low-medium. Setter validation boundary needs careful wording to prevent scope drift.

**Cross-skill dependency**: `python-error-handling` owns cross-field validation. Signpost required. Future `python-functools-patterns` skill may also reference `cached_property`; current skill takes ownership, future skill will signpost here.

---

### R4 + R5 + R6 — Custom Descriptor Protocol → `references/custom-descriptors.md`

**Minimum realization**:
- One reference file covering: upgrade criteria from `@property` to custom descriptor (R4), `__set_name__` for reusability (R5), and data vs non-data descriptor lookup priority (R6)
- Data descriptor vs non-data descriptor distinction must include a lookup priority table (data descriptor > instance `__dict__` > non-data descriptor > class `__dict__`)
- `__set_name__` must include a before/after example showing hardcoded vs dynamic private name

**Technical tasks**:
- T3.1: author `references/custom-descriptors.md` with upgrade criteria
- T3.2: document `__set_name__` with before/after example
- T3.3: document data vs non-data lookup priority with a table and at least one gotcha example

**Cost**: medium. The data/non-data distinction is conceptually subtle and easily over-explained into academic territory. Requires editorial discipline to stay practical.

**Risk**: R6 can drift into descriptor-internals-for-its-own-sake. Constraint: every explanation must connect to an observable developer mistake or design decision, not abstract CPython theory.

---

### R7 + R8 + R9 + R10 — Attribute Hook Mechanisms → `references/attribute-hooks.md`

**Minimum realization**:
- One reference file covering: `__getattr__` (R7), `__setattr__`/`__delattr__` (R8), `__getattribute__` (R9), and the `__init__` pitfall (R10)
- R7 escape hatch must enumerate all 5 conditions as a checklist, not prose. Compression to a footnote triggers rollback.
- R9 must name `__getattribute__` as the highest-risk mechanism with near-absolute discouragement
- R10 `__init__` pitfall must appear in the **anti-pattern section of `references/attribute-hooks.md`** and also in `examples.md` as a concrete code example

**Technical tasks**:
- T4.1: author `references/attribute-hooks.md` with discouraged-hierarchy framing
- T4.2: document R7 escape hatch as 5-item checklist (not prose)
- T4.3: document R9 `__getattribute__` with near-absolute discouragement and architectural justification requirement
- T4.4: document R10 `__init__` pitfall with `object.__getattribute__` / `object.__setattr__` solution pattern

**Cost**: high. This is the highest-risk section. Incorrect framing could normalize dangerous patterns. Requires strong discouragement signals, not just soft guidance.

---

### examples.md — Required (Branching + High-Risk Patterns)

**Minimum realization**:
- `examples.md` is **mandatory** for this skill because:
  - R1 ladder has 7 branching paths — SKILL.md examples alone cannot cover 80% of routine usage
  - R7 escape hatch has complex multi-condition decisions
  - R10 pitfall is a non-obvious failure mode requiring a concrete runnable counter-example
- Required sections in `examples.md`:
  1. Ladder selection walkthrough (choosing between `@property`, `@cached_property`, custom descriptor)
  2. `@property` setter validation — in-scope vs out-of-scope invariants
  3. Custom descriptor with `__set_name__` (before/after)
  4. Data descriptor vs non-data descriptor lookup priority gotcha
  5. `__getattr__` escape hatch — compliant proxy vs non-compliant convenience use
  6. `__init__` pitfall — `Broken` class vs `Safe` class

**Technical tasks**:
- T5.1: author all 6 `examples.md` sections
- T5.2: ensure R10 pitfall `Broken`/`Safe` pair appears in both `examples.md` and `references/attribute-hooks.md`

**Cost**: high. Six distinct sections with code examples. Most examples require showing both a wrong and a correct approach.

---

## Artifact Paths

| Artifact | Path | Owner | Status |
| --- | --- | --- | --- |
| SKILL.md | `.github/skills/python-descriptors-attribute-access/SKILL.md` | Creator | New |
| reference.md (overview) | `.github/skills/python-descriptors-attribute-access/reference.md` | Creator | New |
| Mechanism ladder | `.github/skills/python-descriptors-attribute-access/references/mechanism-ladder.md` | Creator | New |
| Property & cached_property | `.github/skills/python-descriptors-attribute-access/references/property-and-cached-property.md` | Creator | New |
| Custom descriptors | `.github/skills/python-descriptors-attribute-access/references/custom-descriptors.md` | Creator | New |
| Attribute hooks | `.github/skills/python-descriptors-attribute-access/references/attribute-hooks.md` | Creator | New |
| Examples | `.github/skills/python-descriptors-attribute-access/examples.md` | Creator | New |
| README row | `README.md` | Main Agent | Append row |
| VERSION bump | `VERSION` | Main Agent | 0.36.0 → 0.37.0 |

**Total new files**: 7 (SKILL.md + reference.md + 4 references/ files + examples.md)

**Artifact count rationale**: `reference.md` alone would exceed ~1,000 tokens covering 10 requirements across 4 logical topics. Split into 4 topic-specific reference files under `references/` is required by repo reference policy (>1,000 tokens or >3 logical topics triggers split).

---

## Architecture Compliance Self-Check

| Check | Result | Notes |
| --- | --- | --- |
| Single responsibility | ✅ Compliant | All content is attribute access control; no overlap claimed |
| Portability | ✅ Compliant | Python built-ins only; no framework, library, or OS dependencies |
| Independence | ✅ Compliant | Cross-skill signposts declared; no hidden imports from other skills |
| examples.md required | ✅ Required | Branching decisions + escape hatch + pitfall exceed SKILL.md example capacity |
| reference.md split required | ✅ Required | 4 logical topics, estimated >1,000 tokens total |
| Python 3.6+ floor | ✅ Compliant | `__set_name__` and descriptor protocol are 3.6+; `@cached_property` is 3.8+ |
| Cross-skill signpost: `python-class-design` | ✅ Required | `__slots__`, `__new__`, immutability decisions — all signposted |
| Cross-skill signpost: `python-error-handling` | ✅ Required | Cross-field validation, DTO-level contracts — signposted from R2 boundary |
| Cross-skill signpost: `python-decorators` | ✅ Required | `@property` is a decorator; mechanics of decorator protocol are not this skill's domain |
| Cross-skill signpost: `python-data-model-methods` | ✅ Required | `__init__` ownership (R10 pitfall context), `__eq__` / `__hash__` — signposted |

---

## Feasibility Assessment

| Workstream | Complexity | Risk |
| --- | --- | --- |
| SKILL.md + mechanism ladder | Low | Low |
| `@property` / `@cached_property` reference | Low-Medium | Low |
| Custom descriptor reference | Medium | Medium — data/non-data distinction requires editorial control |
| Attribute hooks reference | Medium-High | High — normalization risk for dangerous patterns |
| examples.md (6 sections) | High | Medium — correct/incorrect pairs require accuracy |

**Sequencing constraint**: `references/attribute-hooks.md` (T4) should be authored after `references/custom-descriptors.md` (T3) because the hook mechanisms sit at the top of the ladder and must reference the descriptor protocol sections correctly.

**No external integration dependencies.** No runtime validation, API calls, or system dependencies exist. All work is authoring and structural.

---

## Conflict Detection

| Conflict | Severity | Resolution |
| --- | --- | --- |
| `@cached_property` overlaps future `python-functools-patterns` skill | Low | Current skill takes ownership. Future skill will signpost here. No renegotiation needed. |
| Setter validation boundary (R2) overlaps `python-error-handling` | Low | Boundary is explicit: single-attribute invariant only. Cross-field validation out of scope. Signpost required. |
| `__set_name__` conceptually adjacent to `python-class-design` | Low | Usage context (descriptor reusability) is clearly within scope. `python-class-design` owns class structure decisions, not descriptor protocol usage. |

**No material conflicts detected.** No rollback to alignment required. All conflicts are boundary-labelling issues resolvable by explicit signposts.

---

## Rollback Triggers

The following conditions trigger rollback to alignment and must halt creator work pending renegotiation:

| Trigger | Condition | Action |
| --- | --- | --- |
| RT-1 | `__slots__` implementation appears in skill content | Stop. `__slots__` belongs to `python-class-design`. Remove and signpost. |
| RT-2 | ORM-specific patterns (Django models, SQLAlchemy Column, etc.) appear | Stop. Framework-specific descriptor usage is out of scope. Remove. |
| RT-3 | R7 5-condition escape hatch compressed to prose footnote | Stop. Must appear as an explicit 5-item checklist. Revert and reauthor. |
| RT-4 | Cross-field or DTO-level validation appears in `@property` setter guidance | Stop. Scope breach into `python-error-handling` territory. Remove and signpost. |
| RT-5 | Metaclass attribute handling appears | Stop. Out of scope. Remove. |
| RT-6 | `__getattribute__` framed as a normal tool without strong discouragement | Stop. Must be highest-risk framing with near-absolute discouragement. Revert. |

---

## Plan Contract Anchors

These fields are intended to make `plan-creator` operation deterministic in Strict Mode:

- **Topic**: `python-descriptors-attribute-access`
- **Feature branch**: `feat/andrew/python-descriptors-attribute-access`
- **Base branch**: `dev`
- **VERSION bump**: `0.36.0` → `0.37.0` (MINOR — new stable skill)
- **README row**: new row in the Python skills table, entry: `python-descriptors-attribute-access`
- **Stable library timing**: `publish-in-progress` (README + VERSION updated before PR, not after)
- **examples.md**: required (not optional)
- **Total new files**: 7
- **Cross-skill signposts required**: `python-class-design`, `python-error-handling`, `python-decorators`, `python-data-model-methods`
