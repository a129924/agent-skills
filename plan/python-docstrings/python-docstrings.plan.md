# Python Docstrings Skill Plan

## Goal / Outcome
Design a `python-docstrings` Agent Skill that teaches when and how to write clear, contract-first docstrings using Google Style format. The skill emphasizes **explicit over implicit** — docstrings should capture intent, boundaries, and semantic contracts so code is self-documenting and business contracts are visible. The skill must never invent hidden business rationale: when intent cannot be inferred from explicit signals in code and nearby context, it falls back to documenting the callable contract clearly.

## Scope
- **In scope**:
  - Google Style docstring format (one-liner + description + Args/Returns/Raises/Examples)
  - Public API docstring requirements (classes, public methods, dataclass fields)
  - Private/internal method docstring guidelines (one-liner vs full documentation)
  - Semantic intent capture from explicit signals: "why and when" vs "what the code does"
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
- Note: Alignment with surveyed real-world code is incidental; style choice is justified by broad adoption and structure, not by single-project dependency

### 2. Public API definition: Full contract boundary
- **Public** = classes, public methods, dataclass fields, module-level functions
- **Requires full docstring**: one-liner + description + Args (if params) + Returns (always for non-None-returning functions) + Raises/Examples (context-dependent)
- **Private** (prefix `_`) = internal implementation detail
- **Private method docstring rule**:
  - Always write one-liner explaining intent
  - One-liner is sufficient when the method is a local implementation helper with no independent caller-facing contract
  - Add a full docstring only when the private method has its own non-obvious contract, shown by one or more explicit signals:
    - it mutates object or external state
    - it translates, suppresses, or raises domain-specific errors
    - it returns a structured/domain value whose meaning is not obvious from name + type
    - it is reused from multiple call sites and its preconditions/postconditions matter
  - Exception for @property: one-liner or skip if getter is trivial (e.g., `return self._value`)

### 3. Error semantics: Support both traditional and result-typed patterns
- **Traditional**: use `Raises:` section to document exception types and when they occur
- **Business return types** (e.g., Result[T, E], Union[Success, Failure]): document error cases in `Returns:` section, describing both Ok/Err paths
- **Philosophy**: Caller needs to know what can go wrong; capture it explicitly in the return contract

### 4. Semantic intent > implementation how
- Docstring job: explain **why** this exists, **when** to call it, **what contract** it enforces
- Not: explain line-by-line how the code works
- **Method for deriving semantic intent**:
  - infer from explicit signals only: symbol name, module/class role, parameter names, return type, named errors, surrounding public API, and explicit constraints already stated in code-adjacent context
  - if those signals reveal a boundary or domain role, document that role briefly
  - if those signals do **not** reveal a trustworthy "why", do not invent one; write a contract-focused docstring instead
  - use "why" only when it is explicit from code-adjacent context; otherwise prefer "what contract / when to use"
- Reason: strong names + types + guards make code mechanics self-evident; docstring adds the missing contract or boundary meaning when that meaning is explicit

### 5. Dataclass and field-level documentation (in scope: semantic role only)
- **Dataclass class docstring**: semantic role, boundary context, any invariants
- **Dataclass field docstring**: per-attribute semantic intent, optional/required status, domain meaning
- **IN SCOPE**:
  - "user ID field"
  - "optional run-scoped identifier"
  - domain constraints only when they are already explicit in the public contract and matter to callers
- **OUT OF SCOPE** (delegate to other skills):
  - Type choices (int vs float, Optional vs Union) → `python-type-hints-strict`
  - Validation logic (@validator) → `python-model-selection`
  - Serialization strategy (JSONSchema) → framework-specific skills
- **How to phrase boundary cases**:
  - acceptable: "Positive quantity expected by downstream pricing rules" when that constraint is already explicit in public API or validation contract
  - not acceptable: implementation-level validation advice such as "validated by @field_validator" or speculative constraints not stated elsewhere
- Reason: structured data often carries DDD domain semantics; explicit per-field semantic docs make contracts visible without prescribing structure

### 6. Inline comments: Rare; docstring-first
- Use inline comments only for **non-obvious** control flow or subtle algorithms
- Prefer: clear variable names, guard clauses, early returns, strong types
- If you need an inline comment, consider whether a docstring or better naming would be clearer

### 7. Publication boundary: review-ready topic only
- This topic does **not** publish `python-docstrings` into the stable library.
- `README.md`, `VERSION`, release notes, and `.github/copilot-instructions.md`
  remain untouched in this topic.
- Stable-library promotion, release timing, and version bump decisions are
  deferred to a future dedicated publish topic once the skill content is proven
  review-ready.

## Boundaries / Exclusions

- **Not a code formatter**: does not recommend specific linting tools or auto-formatters
- **Type hint alignment (IN scope)**: when a docstring mentions a type, it must not contradict the signature; docstrings do not need to restate every type annotation verbatim. Choosing type shapes (Optional vs Union) is OUT of scope → `python-type-hints-strict`
- **Not a naming guide**: delegates to `python-naming` skill (docstrings should mention clear names, not prescribe them)
- **Not a model/structure guide**: delegates to `python-model-selection` (skill documents semantic intent of fields that exist; doesn't choose ABC vs dataclass or prescribe validation)
- **Not framework-specific**: stays focused on pure Python docstring patterns; framework integrations (FastAPI, Pydantic, SQLAlchemy) are out of scope
- **Error semantics (IN scope)**: supporting both `Raises:` (traditional) and `Returns:` (business-type Result) is about documenting what can go wrong, not about choosing which pattern to use in code design
- **Not a stable-library publish topic**: this plan does not update `README.md`,
  `VERSION`, `.github/copilot-instructions.md`, or release notes; those belong
  to a later publish-focused topic if the skill graduates to stable library

## Status / Allowed Transitions

- **Current**: `planned`
- **Execution model**: follow the canonical creator → reviewer → publish → merge
  path, but stop at `merged`; this topic does not declare a release action
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
- `approved` does **not** mean the topic may skip directly to publish work.
- After reviewer approval, Main Agent must run the Phase 4.5 planner contract
  alignment checkpoint defined by `plan/agent-handoff-workflow.md`.
- If Phase 4.5 finds drift in locked decisions, artifact paths, or other
  plan-level contract semantics, route the topic back to
  `creator-in-progress` before any publish work continues.
- Only when Phase 4.5 passes may Main Agent move the topic to
  `publish-in-progress`.

## Artifact Paths

| Artifact | Path | Owner | Role |
|----------|------|-------|------|
| Topic plan | `plan/python-docstrings/python-docstrings.plan.md` | Planning actor / Main Agent | Repo-visible execution contract for this topic |
| Skill folder | `.github/skills/python-docstrings/` | Creator | Root output location for the draft skill |
| Core SKILL.md | `.github/skills/python-docstrings/SKILL.md` | Creator | Executable instruction contract |
| Reference overview | `.github/skills/python-docstrings/reference.md` | Creator | Navigation overview for the split reference set |
| Split references | `.github/skills/python-docstrings/references/` | Creator | Topic-specific reference files listed in `SKILL.md` |
| Examples | `.github/skills/python-docstrings/examples.md` | Creator | Detailed positive and negative scenarios for the skill |
| Checklist | `.github/skills/python-docstrings/checklist.md` (optional) | Creator | Optional audit checklist if the creator includes it |

Artifact path notes:
- This topic does **not** modify `README.md`, `VERSION`, or
  `.github/copilot-instructions.md`.
- `Stable library metadata` is intentionally absent because this topic is not a
  stable-library publish topic.
- The listed paths are an executable contract, not an informational appendix.
- If creator output, reviewer findings, or planner alignment reveals repo-visible
  changes outside these paths, treat that drift as a plan violation and route
  the topic back to `creator-in-progress` before continuing.

## Implementation Steps

### Creator Phase (after plan approval)

1. **Draft SKILL.md** (concise examples)
   - Sections: YAML frontmatter (name, description)
   - Purpose: explicit contract focus
   - Trigger / When to use: when? (public API, dataclass fields) when not? (private trivial methods, obvious one-liners)
   - Inputs: code context (class/function signature)
   - Process: step-by-step docstring workflow (identify public vs private → inspect explicit intent signals → choose contract-only or semantic-intent wording → check error paths → fill Args/Returns/Raises)
   - **Examples section (SKILL.md only)**: 3 positive + 1 negative (brief, concise)
     - Positive: public callable where semantic role is explicit from name + boundary context
     - Positive: public callable where "why" is not explicit, so the docstring stays contract-focused
     - Positive: private helper with appropriate one-liner because it has no independent contract
     - Negative: invented rationale, contradictory type wording, or implicit error contract
   - Outputs: complete Google Style docstring
   - Boundaries: what it doesn't cover (type choice, model design, naming prescription)
   - Local references: list reference.md and examples.md roles

2. **Draft reference materials (clear single-path structure)**
   - **LOCKED: Use Option B (split references/)**
     - Treat `reference.md` + `references/` as one reference responsibility with split storage
     - Create `reference.md` as focused overview (~300-400 tokens max) listing split files + their roles and serving as navigation only
     - Create four topic files under `references/`:
       - `references/google-style-template.md` — Google Style structure (one-liner, description, Args/Returns/Raises/Examples format + examples)
       - `references/semantic-intent.md` — How to derive semantic intent from explicit signals; when to fall back to contract-only wording; 5-7 concrete examples including one bad invented-why example
       - `references/error-semantics.md` — Traditional Raises vs business-return patterns (Result[T,E]); documenting error cases without choosing the design pattern
       - `references/dataclass-patterns.md` — Field-level documentation; semantic role capture; contract-vs-validation boundary and examples
     - List all split files explicitly in SKILL.md Local references with role labels
   - Do NOT use Option A (single file). Commit to split structure to avoid >1000 token consolidation later.

3. **Draft examples.md** (REQUIRED — high complexity skill)
   - Contains 5 positive + 3 negative representative scenarios with detailed explanations
   - Scenarios to cover:
     - a. Public class/function where semantic intent is explicit from boundary context
     - b. Public class/function where intent is not explicit, so the docstring stays contract-focused and does not invent rationale
     - c. Private helper with no independent contract → one-liner only
     - d. Private helper with independent contract (side effect / error translation / reused preconditions) → full docstring
     - e. Dataclass with field-level semantic documentation, including contract-vs-validation boundary
     - f. Function returning traditional exception type vs Result[T,E] business type
     - g. Anti-pattern: invented "why" not supported by code or nearby context
     - h. Anti-pattern: docstring contradicts signature types or error behavior
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
3. **Validate examples**: confirm the required scenario set is present in both concise and detailed form (semantic-intent derivation, contract-only fallback, private helper rules, dataclass boundary, error patterns, anti-patterns)
4. **Check single responsibility**: is scope pure docstring guidance? (not naming, not types, not model choice)
5. **Verify portability**: confirm all guidance is generic after removing repo-specific names; no step should rely on project-specific architecture knowledge
6. **Use reviewer inputs explicitly**:
   - SKILL folder: `.github/skills/python-docstrings/`
   - Topic plan: `plan/python-docstrings/python-docstrings.plan.md`
   - Copilot feedback collected by Main Agent in Phase 4b, used as context for
     `ADDRESS` / `DISCUSS` / `SKIP` triage
7. **Structured findings**: record concrete findings as blocking issues and
   feedback triage rationale in the reviewer JSON output
8. **Verdict**: approved or needs-rework with specific guidance

## Validation / Acceptance Checks

### Creator readiness (before handoff to reviewer)
- [ ] SKILL.md complete with all 9 required sections
- [ ] **SKILL.md Examples section**: 3 positive + 1 negative (brief, concise guidance)
  - [ ] semantic-intent-from-explicit-context example
  - [ ] contract-only-when-why-is-not-explicit example
  - [ ] private-helper-one-liner example
  - [ ] negative invented-rationale / contradictory-contract example
- [ ] **examples.md present (REQUIRED for high-complexity skill)**: 5 positive + 3 negative detailed scenarios
  - [ ] Scenario a: semantic intent derived from explicit boundary context
  - [ ] Scenario b: contract-only fallback when rationale is not explicit
  - [ ] Scenario c: private helper with no independent contract
  - [ ] Scenario d: private helper with independent contract (state mutation / error translation / reused preconditions)
  - [ ] Scenario e: dataclass field documentation with contract-vs-validation boundary
  - [ ] Scenario f: traditional exception vs Result[T,E] documentation pattern
  - [ ] Anti-pattern g: invented "why" unsupported by code/context
  - [ ] Anti-pattern h: type or error contract contradiction
- [ ] **reference.md + references/ (split structure)**:
  - [ ] reference.md (~300-400 tokens): navigation overview listing all split files + roles
  - [ ] references/google-style-template.md: format and structure
  - [ ] references/semantic-intent.md: intent derivation method, fallback rules, bad-example coverage
  - [ ] references/error-semantics.md: exception and Result[T,E] patterns
  - [ ] references/dataclass-patterns.md: field-level semantic docs + contract-vs-validation boundary
  - [ ] All split files listed in SKILL.md Local references with role labels
- [ ] All examples use real-world code patterns expressed with generic or clearly generalized names
- [ ] No hidden project-specific context:
  - [ ] no repo-specific paths, proprietary type names, or architecture-only assumptions in core guidance
  - [ ] examples use generic names or clearly generalized variants
  - [ ] semantic-intent guidance never requires knowledge unavailable from explicit code-adjacent context
- [ ] Creator portability spot-check:
  - [ ] at least one example is authored directly with generic names, or rewritten from a real-world pattern into generic names, and still follows the same rules
  - [ ] the rewritten example does not depend on project-specific architecture knowledge

### Reviewer approval criteria
- [ ] Required core present: SKILL.md + reference.md + references/ (all 4 split files) + examples.md
- [ ] SKILL.md structure complete (9 sections + frontmatter)
- [ ] SKILL.md Examples: 3 positive + 1 negative (concise)
- [ ] examples.md Examples: 5 positive + 3 negative (detailed), covering all required scenarios a-h
- [ ] Single responsibility: pure docstring guidance (no scope creep into naming, types, models)
- [ ] Portability: reference and examples are generic, reusable outside the surveyed source project
- [ ] Portability spot-check: reviewer can remove any remaining project nouns from the chosen rewritten example without changing the guidance
- [ ] Boundaries are clear; no ambiguity about what is/isn't covered
- [ ] Local file roles explicitly named in Local references
- [ ] Reviewer records specific findings in JSON `blocking_issues` and feedback
      triage entries
- [ ] Reviewer handoff output follows the workflow JSON contract
- [ ] Reviewer input includes Copilot feedback context and triages it through
      `ADDRESS` / `DISCUSS` / `SKIP`
- [ ] No stable-library surfaces are included in this topic (`README.md`,
      `VERSION`, `.github/copilot-instructions.md`, release notes)
- [ ] Any repo-visible path drift outside listed `Artifact Paths` is treated as
      a plan violation and routed back before publish

## Reviewer Handoff

**Fixed report format** (from `plan/agent-handoff-workflow.md` schema):

```json
{
  "verdict": "approved|needs-rework",
  "blocking_issues": [
    {
      "issue": "Description of the unmet requirement",
      "file": "path/to/file.md",
      "fix": "Concrete change required before re-review"
    }
  ],
  "copilot_feedback_triage": {
    "ADDRESS": [
      {
        "comment": "Text of Copilot comment",
        "location": "path/to/file.md:line",
        "why": "Why this feedback should be applied"
      }
    ],
    "DISCUSS": [
      {
        "comment": "Text of optional feedback",
        "optional": true,
        "why": "Why this is worth discussing but not required"
      }
    ],
    "SKIP": [
      {
        "comment": "Text of inapplicable feedback",
        "why": "Why it should not change the draft"
      }
    ]
  }
}
```

Reviewer may append short prose notes after the JSON object, but the JSON object
is the fixed machine-consumable handoff contract.

## Post-merge / release actions

1. After merge, run the normal post-merge local sync flow for the working branch.
2. Do **not** update `README.md`, `VERSION`, `.github/copilot-instructions.md`, or
   release notes in this topic.
3. No repository release action is required for this topic.
4. Stable-library publication for `python-docstrings` is deferred to a later
   publish-focused topic once the skill is proven review-ready.
5. This topic is terminal at `merged`.

## Open Questions / Unresolved Items

1. **Checklist.md priority**: optional for this skill; reviewer may request if additional audit tools prove valuable
2. **Async docstring patterns**: explicitly deferred; do not add async-specific guidance or examples in this draft
3. **Deprecation and versioning**: explicitly deferred; future skill if demand arises
4. **Framework integration expectations**: explicitly deferred; stays focused on pure Python patterns (SQLAlchemy, FastAPI, Pydantic specifics belong in framework-focused skills or extensions)
5. **Stable-library promotion**: explicitly deferred; if `python-docstrings`
   later enters the stable library, create a separate publish-focused topic with
   `Stable library metadata`

---

## Summary for Creator

**Responsibility**: Implement `python-docstrings` skill teaching Google Style, public API contracts, semantic intent capture, and explicit error semantics with clear boundaries.

**Key decisions LOCKED** (non-negotiable):
- **Google Style format**: one-liner + description + Args/Returns/Raises/Examples sections (industry standard; supports traditional + business-return patterns)
- **Public API contract**: full docstring required for public classes, methods, fields, functions
- **Private method rule**: one-liner by default; full docstring only when the private method has an explicit independent contract (state mutation, error translation, structured/domain return, or reused pre/postconditions)
- **Error semantics**: support both `Raises:` (traditional) and `Returns:` (Result[T,E] business-type)
- **Semantic intent method**: derive only from explicit code-adjacent signals; if rationale is not explicit, use contract-only wording and do not invent "why"
- **Dataclass field docs (semantic role only)**: IN scope; validation mechanics and type choice OUT of scope
- **Type hint alignment**: docstrings may omit type syntax, but any stated type must not contradict the signature
- **Reference structure (split)**: one reference responsibility implemented as `reference.md` navigation + `references/` topic splits
- **Inline comments**: rare; docstring-first philosophy
- **Boundaries**: no naming guidance, no type-hint shape decisions, no model/validator design, no framework specifics
- **Publication boundary**: this topic does not touch `README.md`, `VERSION`,
  `.github/copilot-instructions.md`, or release notes; stable-library publish is
  deferred to a later topic

**Deliverables**:
- SKILL.md (9 sections): 3 positive + 1 negative concise examples
- examples.md (REQUIRED): 5 positive + 3 negative detailed scenarios
- reference.md (overview ~300-400 tokens)
- references/ (4 split files):
  - google-style-template.md
  - semantic-intent.md
  - error-semantics.md
  - dataclass-patterns.md
- Optional checklist.md for review audit

**Success criteria**:
- SKILL.md Examples stand on their own for standard usage; examples.md covers edge cases and anti-patterns in depth
- Skill is portable (no repo-specific context; grounded in real patterns but written generically)
- Clear boundaries (doesn't encroach on naming, type choices, model design, framework specifics)
- All local files have explicit roles in SKILL.md Local references
- Semantic-intent guidance is executable because it names explicit sources and a contract-only fallback
- Private method rule is executable because it depends on explicit contract signals, not line-count guesswork
- The topic plan remains workflow-compatible without declaring stable-library
  publish or release work
