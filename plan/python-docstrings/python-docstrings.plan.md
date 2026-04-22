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
- Reason: widely adopted Python industry standard; provides clear contract sections (Args/Returns/Raises/Examples); supports both traditional exceptions and modern business-return types (Raises vs Result[T,E])
- Note: Alignment with vendor-bcp-exporter is incidental; style choice is justified by broad adoption and structure, not by single-project dependency

### 2. Public API definition: Full contract boundary
- **Public** = classes, public methods, dataclass fields, module-level functions
- **Requires full docstring**: one-liner + description + Args (if params) + Returns (always for non-None-returning functions) + Raises/Examples (context-dependent)
- **Private** (prefix `_`) = internal implementation detail
- **Private method docstring rule**:
  - Always write one-liner explaining intent
  - If method is simple (<15 lines, self-evident): one-liner is sufficient
  - If method is complex (>15 lines) or contains business logic: add full docstring with Args/Returns
  - Exception for @property: one-liner or skip if getter is trivial (e.g., `return self._value`)

### 3. Error semantics: Support both traditional and result-typed patterns
- **Traditional**: use `Raises:` section to document exception types and when they occur
- **Business return types** (e.g., Result[T, E], Union[Success, Failure]): document error cases in `Returns:` section, describing both Ok/Err paths
- **Philosophy**: Caller needs to know what can go wrong; capture it explicitly in the return contract

### 4. Semantic intent > implementation how
- Docstring job: explain **why** this exists, **when** to call it, **what contract** it enforces
- Not: explain line-by-line how the code works
- Reason: strong names + types + guards make code self-evident; docstring adds business/design intent

### 5. Dataclass and field-level documentation (in scope: semantic role only)
- **Dataclass class docstring**: semantic role, boundary context, any invariants
- **Dataclass field docstring**: per-attribute semantic intent, optional/required status, domain meaning
- **IN SCOPE**: "user ID field", "optional run-scoped identifier", "must be >0"
- **OUT OF SCOPE** (delegate to other skills):
  - Type choices (int vs float, Optional vs Union) → `python-type-hints-strict`
  - Validation logic (@validator) → `python-model-selection`
  - Serialization strategy (JSONSchema) → framework-specific skills
- Reason: structured data often carries DDD domain semantics; explicit per-field semantic docs make contracts visible without prescribing structure

### 6. Inline comments: Rare; docstring-first
- Use inline comments only for **non-obvious** control flow or subtle algorithms
- Prefer: clear variable names, guard clauses, early returns, strong types
- If you need an inline comment, consider whether a docstring or better naming would be clearer

## Boundaries / Exclusions

- **Not a code formatter**: does not recommend specific linting tools or auto-formatters
- **Type hint alignment (IN scope)**: docstring Args/Returns types must match signature types (consistency check); choosing type shapes (Optional vs Union) is OUT of scope → `python-type-hints-strict`
- **Not a naming guide**: delegates to `python-naming` skill (docstrings should mention clear names, not prescribe them)
- **Not a model/structure guide**: delegates to `python-model-selection` (skill documents semantic intent of fields that exist; doesn't choose ABC vs dataclass or prescribe validation)
- **Not framework-specific**: stays focused on pure Python docstring patterns; framework integrations (FastAPI, Pydantic, SQLAlchemy) are out of scope
- **Error semantics (IN scope)**: supporting both `Raises:` (traditional) and `Returns:` (business-type Result) is about documenting what can go wrong, not about choosing which pattern to use in code design

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
| Reference | `.github/skills/python-docstrings/reference.md` + `references/` (split structure) | Creator | Overview + topic split files (google-style-template, semantic-intent, error-semantics, dataclass-patterns) |
| Examples | `.github/skills/python-docstrings/examples.md` (required: high-complexity skill) | Creator | Multi-path usage patterns, anti-patterns, real-world scenarios |
| Checklist | `.github/skills/python-docstrings/checklist.md` (optional) | Creator | Review/audit checklist for evaluating docstring compliance |

## Implementation Steps

### Creator Phase (after plan approval)

1. **Draft SKILL.md** (concise examples)
   - Sections: YAML frontmatter (name, description)
   - Purpose: explicit contract focus
   - Trigger / When to use: when? (public API, dataclass fields) when not? (private trivial methods, obvious one-liners)
   - Inputs: code context (class/function signature)
   - Process: step-by-step docstring workflow (identify public vs private → check error paths → write one-liner → fill Args/Returns)
   - **Examples section (SKILL.md only)**: 2 positive + 1 negative (brief, concise)
     - Positive: well-documented public class (semantic + contract)
     - Positive: private method with appropriate one-liner (simple vs complex distinction)
     - Negative: missing intent or implicit error (anti-pattern indicator)
   - Outputs: complete Google Style docstring
   - Boundaries: what it doesn't cover (type choice, model design, naming prescription)
   - Local references: list reference.md and examples.md roles

2. **Draft reference materials (clear single-path structure)**
   - **LOCKED: Use Option B (split references/)**
     - Create `reference.md` as focused overview (~300-400 tokens max) listing split files + their roles
     - Create four topic files under `references/`:
       - `references/google-style-template.md` — Google Style structure (one-liner, description, Args/Returns/Raises/Examples format + examples)
       - `references/semantic-intent.md` — Capturing intent and boundary context; DDD patterns
       - `references/error-semantics.md` — Traditional Raises vs business-return patterns (Result[T,E]); documenting error cases
       - `references/dataclass-patterns.md` — Field-level documentation; semantic role capture; what NOT to document (validation, type choice)
     - List all split files explicitly in SKILL.md Local references with role labels
   - Do NOT use Option A (single file). Commit to split structure to avoid >1000 token consolidation later.

3. **Draft examples.md** (REQUIRED — high complexity skill)
   - Contains 4 positive + 2 negative representative scenarios with detailed explanations
   - Scenarios to cover:
     - a. Public class with semantic intent + method docstring (e.g., DTO, use case)
     - b. Private helper method: simple (<15 lines) vs complex (>15 lines) with one-liner vs full docs
     - c. Dataclass with field-level semantic documentation (per-field intent)
     - d. Function returning traditional exception type vs Result[T,E] business type
     - e. Over-documented trivial code (anti-pattern)
     - f. Missing intent / implicit error handling (anti-pattern)
   - Each example: code snippet + explanation of correctness or why pattern is wrong

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
- [ ] **SKILL.md Examples section**: 2 positive + 1 negative (brief, concise guidance)
- [ ] **examples.md present (REQUIRED for high-complexity skill)**: 4 positive + 2 negative detailed scenarios
  - [ ] Scenario a: Public class with semantic intent + method docstring
  - [ ] Scenario b: Private method complexity tiers (simple <15 lines vs complex >15 lines; documentation expectations)
  - [ ] Scenario c: Dataclass with field-level semantic documentation (per-field intent)
  - [ ] Scenario d: Function with traditional exception vs Result[T,E] business-return pattern
  - [ ] Anti-pattern e: Over-documented trivial code
  - [ ] Anti-pattern f: Missing intent / implicit error handling
- [ ] **reference.md + references/ (split structure)**:
  - [ ] reference.md (~300-400 tokens): overview listing all split files + roles
  - [ ] references/google-style-template.md: format and structure
  - [ ] references/semantic-intent.md: intent capture, DDD context
  - [ ] references/error-semantics.md: exception and Result[T,E] patterns
  - [ ] references/dataclass-patterns.md: field-level semantic docs + scope boundaries
  - [ ] All split files listed in SKILL.md Local references with role labels
- [ ] All examples use real-world code patterns (vendor-bcp-exporter-inspired or generic)
- [ ] No hidden project-specific context; skill is portable
- [ ] Manually tested: skill can guide someone on unfamiliar codebase (not vendor-specific)

### Reviewer approval criteria
- [ ] Required core present: SKILL.md + reference.md + references/ (all 4 split files) + examples.md
- [ ] SKILL.md structure complete (9 sections + frontmatter)
- [ ] SKILL.md Examples: 2 positive + 1 negative (concise)
- [ ] examples.md Examples: 4 positive + 2 negative (detailed), covering all scenarios
- [ ] Examples sufficient for 80%+ of routine docstring tasks
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

1. **Checklist.md priority**: optional for this skill; reviewer may request if additional audit tools prove valuable
2. **Async docstring patterns**: out of scope for first draft, but if Creator discovers repeated async patterns during implementation, can add concise anti-pattern example to examples.md as polish (non-blocking follow-up)
3. **Deprecation and versioning**: out of scope for first draft; future skill if demand arises
4. **Framework integration expectations**: out of scope; stays focused on pure Python patterns (SQLAlchemy, FastAPI, Pydantic specifics belong in framework-focused skills or extensions)

---

## Summary for Creator

**Responsibility**: Implement `python-docstrings` skill teaching Google Style, public API contracts, semantic intent capture, and explicit error semantics with clear boundaries.

**Key decisions LOCKED** (non-negotiable):
- **Google Style format**: one-liner + description + Args/Returns/Raises/Examples sections (industry standard; supports traditional + business-return patterns)
- **Public API contract**: full docstring required for public classes, methods, fields, functions
- **Private method rule**: simple (<15 lines) = one-liner; complex (>15 lines, business logic) = full docstring
- **Error semantics**: support both `Raises:` (traditional) and `Returns:` (Result[T,E] business-type)
- **Semantic intent > implementation how**: docstring captures why/when/what-contract, not line-by-line code
- **Dataclass field docs (semantic role only)**: IN scope; type choice/validation OUT of scope
- **Type hint alignment**: Args/Returns types must match signature (consistency); type shape choice OUT of scope
- **Reference structure (split)**: LOCKED to Option B (reference.md overview + references/ split by topic); no single-file fallback
- **Inline comments**: rare; docstring-first philosophy
- **Boundaries**: no naming guidance, no type-hint shape decisions, no model/validator design, no framework specifics

**Deliverables**:
- SKILL.md (9 sections): 2 positive + 1 negative examples (concise)
- examples.md (REQUIRED): 4 positive + 2 negative detailed scenarios
- reference.md (overview ~300-400 tokens)
- references/ (4 split files):
  - google-style-template.md
  - semantic-intent.md
  - error-semantics.md
  - dataclass-patterns.md
- Optional checklist.md for review audit

**Success criteria**:
- SKILL.md Examples clear and brief; examples.md Examples comprehensive and multi-scenario
- Skill is portable (no vendor-bcp-exporter specific context; inspired by real patterns, but generic application)
- Clear boundaries (doesn't encroach on naming, type choices, model design, framework specifics)
- All local files have explicit roles in SKILL.md Local references
- Private method rule is executable (not "judgment call"—simple <15 lines vs complex >15 lines criterion is objective)
