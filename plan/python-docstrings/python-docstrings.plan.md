# Python Docstrings Skill Plan

## Goal / Outcome
Design a `python-docstrings` Agent Skill that teaches when and how to write clear, contract-first docstrings using Google Style format. The skill emphasizes **explicit over implicit** — docstrings should capture intent, boundaries, and semantic contracts so code is self-documenting and business contracts are visible.

## Scope
- **In scope**:
  - Google Style docstring format (one-liner + description + Args/Returns/Raises/Examples)
  - Public API docstring requirements (classes, public methods, dataclass fields)
  - Private/internal method docstring guidelines (one-liner vs full documentation)
  - Semantic intent capture: "why and when" vs "what the code does"
  - Boundary and DDD context documentation
  - Error semantics (traditional Raises, also business-type returns like Result[T, E])
  - Dataclass and structured data field-level documentation
  - Inline comment policy (when docstring is better)
  - Type hint and docstring alignment
  
- **Out of scope**:
  - Async/await specific conventions
  - Framework-specific docstrings (FastAPI, Pydantic, SQLAlchemy auto-docs)
  - Sphinx roles, reStructuredText markup
  - Multi-language or i18n documentation
  - Deprecation warnings or version-history tracking

## Locked Decisions

### 1. Docstring style: Google Style (non-negotiable)
- Format: one-liner → extended description → Args/Returns/Raises/Examples/Yields
- Reason: matches vendor-bcp-exporter production codebase; widely adopted in Python; clear contract sections
- Exception: Do not mandate docstring on trivial/one-line internal utilities (judgment call by reviewer context)

### 2. Public API definition: Full contract boundary
- **Public** = classes, public methods, dataclass fields, module-level functions
- **Requires full docstring**: one-liner + description + Args (if params) + Returns (always for non-None-returning functions) + Raises/Examples (context-dependent)
- **Private** (prefix `_`) = internal implementation detail
- **Minimal docstring for private**: one-liner explaining intent (optional for tiny helpers or @property with obvious behavior)

### 3. Error semantics: Support both traditional and result-typed patterns
- **Traditional**: use `Raises:` section to document exception types and when they occur
- **Business return types** (e.g., Result[T, E], Union[Success, Failure]): document error cases in `Returns:` section, describing both Ok/Err paths
- **Philosophy**: Caller needs to know what can go wrong; capture it explicitly in the return contract

### 4. Semantic intent > implementation how
- Docstring job: explain **why** this exists, **when** to call it, **what contract** it enforces
- Not: explain line-by-line how the code works
- Reason: strong names + types + guards make code self-evident; docstring adds business/design intent

### 5. Dataclass and field-level documentation
- Dataclass *class* docstring: semantic role, boundary context, any invariants
- Dataclass *field* docstring: per-attribute intent, optional/required status, semantic meaning
- Reason: structured data often carries DDD domain semantics; explicit per-field docs make contracts visible

### 6. Inline comments: Rare; docstring-first
- Use inline comments only for **non-obvious** control flow or subtle algorithms
- Prefer: clear variable names, guard clauses, early returns, strong types
- If you need an inline comment, consider whether a docstring or better naming would be clearer

## Boundaries / Exclusions

- **Not a code formatter**: does not recommend specific linting tools or auto-formatters
- **Not type-hint guidance**: delegates to `python-type-hints-strict` skill (docstrings may reference types, but signature hints are separate)
- **Not a naming guide**: delegates to `python-naming` skill (docstrings should mention clear names, not prescribe them)
- **Not a model/structure guide**: delegates to `python-model-selection` (skill documents models that exist; doesn't choose ABC vs dataclass)

## Status / Allowed Transitions

- **Current**: `planned`
- **Workflow target**: `creator-in-progress` → `review-ready` → reviewer approval
- **Allowed transitions from `planned`**:
  - `planned` → `creator-in-progress` (when creator picks up implementation)
  - `planned` → `review-ready` (when plan is locked and creator is ready to implement in next step)

## Artifact Paths

| Artifact | Path | Owner | Role |
|----------|------|-------|------|
| Topic plan | `plan/python-docstrings/python-docstrings.plan.md` | Main Agent (planning phase) | Handoff contract between planning and creator |
| Skill folder | `.github/skills/python-docstrings/` | Creator Agent | Implementation delivery |
| Core SKILL.md | `.github/skills/python-docstrings/SKILL.md` | Creator | Executable instruction contract |
| Reference | `.github/skills/python-docstrings/reference.md` (or `references/` if >1000 tokens) | Creator | Stable local knowledge, patterns, edge cases |
| Examples | `.github/skills/python-docstrings/examples.md` (required: high-complexity skill) | Creator | Multi-path usage patterns, anti-patterns, real-world scenarios |
| Checklist | `.github/skills/python-docstrings/checklist.md` (optional) | Creator | Review/audit checklist for evaluating docstring compliance |

## Implementation Steps

### Creator Phase (after plan approval)

1. **Draft SKILL.md**
   - Sections: YAML frontmatter (name, description)
   - Purpose: explicit contract focus
   - Trigger / When to use: when? (on public API, dataclass fields) when not? (private trivial methods, obvious one-liners)
   - Inputs: code context (class/function signature)
   - Process: step-by-step docstring-writing workflow (intent → contract → signature mapping → args/returns)
   - Examples: 2-3 positive (well-documented public API, dataclass with field docs, error semantics), 2-3 negative (missing intent, over-documented trivial code, implicit error handling)
   - Outputs: complete Google Style docstring
   - Boundaries: what it doesn't cover (types, naming, model choice)
   - Local references: list reference.md and examples.md roles

2. **Draft reference.md or references/**
   - **Recommended: Option B (split into references/)**
     - Six topics (Google Style, public API, private methods, semantic intent, error semantics, dataclass patterns) will likely exceed 1,000 tokens in a single file
     - Split structure (per repo policy):
       - `references/google-style-template.md` — Google Style structure and format rules
       - `references/semantic-intent.md` — Capturing intent, boundary, and DDD context
       - `references/error-semantics.md` — Documenting exceptions, Result types, error paths
       - `references/dataclass-patterns.md` — Field-level documentation and invariant capture
     - Create `reference.md` as focused overview (max ~300 tokens) listing split files + their roles
     - List all split files and roles explicitly in SKILL.md Local references
   - **Option A (single reference.md)**: Only if content confirmed to be <800 tokens; not recommended at start

3. **Draft examples.md** (REQUIRED — high complexity skill)
   - Minimum 4-5 representative scenarios:
     a. Public class with semantic intent (e.g., DTO, use case) + field/method docs
     b. Private helper method with one-liner intent
     c. Function returning traditional exception type vs Result[T, E] business type
     d. Dataclass with field-level semantic documentation
     e. Over-documented trivial code (anti-pattern) vs minimal acceptable docs
   - Each example: code snippet + explanation of why this is correct/incorrect

4. **Optional: checklist.md**
   - Review checklist for auditing docstring compliance:
     - [ ] Every public class has docstring with semantic intent?
     - [ ] Every public method has Returns documented?
     - [ ] Error semantics (Raises or Result) explicitly stated?
     - [ ] Dataclass fields have per-field docstring?
     - [ ] No inline comments that could be replaced by docstring + clear naming?

### Reviewer Phase (after creator delivers review-ready)

1. **Verify required core** (SKILL.md + reference/examples present)
2. **Check structure**: YAML, Purpose, Trigger, Inputs, Process, Examples, Outputs, Boundaries, Local references
3. **Validate examples**: 2+ positive, 2+ negative; cover public/private/dataclass/error patterns
4. **Check single responsibility**: is scope pure docstring guidance? (not naming, not types, not model choice)
5. **Verify portability**: can skill be used outside vendor-bcp-exporter? (reference material generic, not project-specific)
6. **Evidence table**: collect findings (structure ok, examples sufficient, boundaries clear, local reference roles explicit)
7. **Verdict**: approved or needs-rework with specific guidance

## Validation / Acceptance Checks

### Creator readiness (before handoff to reviewer)
- [ ] SKILL.md complete with all 9 required sections
- [ ] **examples.md present (REQUIRED for high-complexity skill)**
- [ ] **At least 4 positive and 2 negative examples total**, covering all patterns:
  - [ ] Positive: well-documented public class/method (semantic intent + Args/Returns)
  - [ ] Positive: dataclass with field-level documentation
  - [ ] Positive: private method with one-liner intent
  - [ ] Positive: error semantics (Raises or Result[T,E] pattern)
  - [ ] Negative: over-documented trivial code (anti-pattern)
  - [ ] Negative: missing intent / implicit error handling (anti-pattern)
- [ ] reference.md (overview only) or references/ (split by topic) with all roles labeled in SKILL.md Local references
- [ ] All examples use real-world code patterns or vendor-bcp-exporter-inspired scenarios
- [ ] No hidden project-specific context; skill is portable
- [ ] Manually tested: skill description is clear enough for agent to apply to unfamiliar codebase

### Reviewer approval criteria
- [ ] Required core present: SKILL.md + reference.md (or references/) + examples.md
- [ ] SKILL.md structure complete (9 sections + frontmatter)
- [ ] **Examples coverage: at least 4 positive + 2 negative scenarios** covering public/private/dataclass/error-semantics/anti-patterns
- [ ] Examples sufficient for 80%+ of routine usage
- [ ] Single responsibility: pure docstring guidance (no scope creep into naming, types, models)
- [ ] Portability: reference and examples are generic, reusable outside vendor-bcp-exporter context
- [ ] Boundaries are clear; no ambiguity about what is/isn't covered
- [ ] Local file roles explicitly named in Local references
- [ ] Evidence: reviewer fills in table with specific findings

## Reviewer Handoff

**Fixed report format** (from `plan/agent-handoff-workflow.md` schema):

```
Skill: python-docstrings
Verdict: [approved | needs-rework]
Blocking issues: [none | list specific unmet criteria]

Evidence:
| Criterion | Finding | Status |
|-----------|---------|--------|
| Required core (SKILL.md + reference + examples) | [present/missing] | [ok/fail] |
| Structure (9 sections + frontmatter) | [complete/incomplete] | [ok/fail] |
| Examples coverage | [covers public/private/dataclass/error] | [ok/fail] |
| Single responsibility | [pure docstring guidance] | [ok/fail] |
| Portability | [generic, reusable] | [ok/fail] |
| Boundaries clarity | [explicit, unambiguous] | [ok/fail] |
| Local references roles | [explicit labels] | [ok/fail] |

Review notes: [summary of key findings, any polish suggestions]
```

## Post-Approval Actions (Publisher / Release)

1. Add `python-docstrings` entry to README.md Stable Skills list (after reviewer approval)
2. Update `.github/copilot-instructions.md` to reflect new skill availability (if instructions mention available skills)
3. Tag skill in release notes when published
4. Optional: link from python-naming, python-type-hints-strict in README cross-references

## Open Questions / Unresolved Items

1. **Checklist.md priority**: should be optional or required for high-complexity skills? (Current assumption: optional, but reviewer may request)
2. **Async docstring specifics**: confirmed out of scope, but if Creator encounters repeated async docstring patterns during implementation, consider adding a concise anti-pattern example to examples.md (e.g., "missing await in docstring description" or "unclear if coroutine has side effects"). Leave as follow-up polish, not blocking.
3. **Deprecation warnings**: out of scope for first draft, but should examples.md have an anti-pattern entry (e.g., "don't forget @deprecated" or is that separate)?
4. **Framework integration**: vendor-bcp-exporter uses SQLAlchemy and uses-case patterns; should reference.md have a section on "framework-specific docstring expectations" or stay focused on pure Python?

---

## Summary for Creator

**Responsibility**: Implement `python-docstrings` skill teaching Google Style, public API contracts, semantic intent capture, and explicit error semantics.

**Key decisions locked**:
- Google Style format (non-negotiable)
- Public API definition (full docstring) vs private (one-liner or skip)
- Support both Raises and Result[T, E] business-type error patterns
- Semantic intent > implementation details
- Dataclass field-level documentation is in scope
- Inline comments rare; docstring-first philosophy

**Deliverables**:
- SKILL.md with 9 required sections, 2+ positive + 2+ negative examples
- reference.md (or references/) with template, patterns, semantic intent guidance
- examples.md (required) with 4-5 representative scenarios
- Optional checklist.md for review audit

**Success criteria**:
- Examples cover public/private/dataclass/error-semantics patterns
- Skill is portable (no vendor-bcp-exporter specific context)
- Clear boundaries (doesn't encroach on naming, types, model selection)
- All local files have explicit roles in SKILL.md Local references
