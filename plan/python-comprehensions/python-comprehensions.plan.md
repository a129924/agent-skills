# Python Comprehensions Skill Plan

## Goal / Outcome

Create a repo-visible execution plan for a new stable skill at
`.github/skills/python-comprehensions/` that teaches when to use list/dict/set
comprehensions for readability and performance, when comprehensions become
unreadable and should be replaced with explicit loops or functional tools, and
how to balance functional vs imperative style choices in Python. The completed
topic should produce a review-ready skill that covers comprehension readability
boundaries, nested structures, filter/map trade-offs, and anti-patterns.

## Scope

- **In scope**:
  - create `.github/skills/python-comprehensions/SKILL.md`
  - create `.github/skills/python-comprehensions/reference.md` as the focused
    overview and navigation file
  - create `.github/skills/python-comprehensions/examples.md` for layered
    examples, anti-patterns, and split signals
  - define first-draft rules for:
    - single-level comprehensions (list, dict, set) as standard practice
    - readability boundaries: when nested comprehensions become opaque
    - filter/map vs comprehension trade-offs
    - generator expressions as lazy variants
    - when explicit loops are clearer than comprehensions
    - performance implications (memory, execution order)
    - comprehension scoping rules (variable leakage in Python 2 vs 3)
  - declare stable-library promotion timing for `README.md` and `VERSION`
  - declare the post-merge tag action for this new stable skill topic

- **Out of scope**:
  - general functional programming patterns (owned by potential
    `python-functional-style` skill)
  - iterator protocol or generator design strategy (owned by
    `python-generators-iterators`)
  - performance optimization at scale or Big-O analysis
  - NumPy/pandas array operations or specialized comprehension variants
  - walrus operator (`:=`) inside comprehensions (too narrow; 3.8+ only)

## Locked Decisions

- This topic is a **stable-library-affecting topic** with declared publish and
  release timing.
- The skill's primary scope is **readability-first comprehension guidance** for
  ordinary Python code, not specialized libraries or advanced functional patterns.
- **Scope breadth is locked to `comprehension-readability-and-boundaries`**,
  meaning:
  - single-level list/dict/set comprehensions are mainline topics
  - nested comprehensions and readability limits are mainline topics
  - generator expressions as lazy variants are in scope
  - filter/map vs comprehension trade-offs are in scope
  - the topic should prioritize readability heuristics over functional purity
- **Readability emphasis is locked**, meaning:
  - the skill should prioritize "is this code clear to a maintainer?" over
    "is this the shortest way to write it?"
  - nested comprehensions that exceed 2 levels or mix multiple conditions
    should be flagged as candidates for refactoring
  - comprehension complexity should be assessed by cognitive load, not token count
- **Stable-library timing is locked to `stable-library-affecting-now`**, meaning:
  - this topic should update `README.md` and `VERSION` at
    `publish-in-progress`
  - a post-merge tag action is expected if the topic reaches stable library
- **Version baseline**:
  - implementation guidance should work on **Python 3.10+** to match the
    repository's existing Python typing baseline
  - examples may use modern syntax without 3.7 compatibility concerns
  - walrus operator (`:=`) is not a main topic; if mentioned, should be
    version-gated as 3.8+ optional

## Boundaries / Exclusions

- `python-functional-style` (future skill, if created)
  - owns currying, partial application, function composition, and functional
    style patterns
  - this topic only decides when comprehensions are readable vs when to switch
    to loops or map/filter

- `python-generators-iterators`
  - owns iterator protocol, custom iterators, lazy evaluation design, and
    generator functions
  - this topic treats generator expressions as comprehension equivalents, not
    as design patterns

- `python-control-flow`
  - owns `if/elif`, guard clauses, and truthiness rules in general
  - this topic only applies control-flow guidance to comprehension filters

- `python-error-handling`
  - owns exception handling strategy
  - this topic may note that try/except inside comprehensions is usually a
    design smell

## Status / Allowed Transitions

**Current status**: `pr-open`

Canonical allowed transitions:
- `planned` → `creator-in-progress` (when this plan is committed and ready)
- `creator-in-progress` → `review-ready` (when creator finishes draft)
- `review-ready` → `reviewer-in-progress` (when handed to reviewer)
- `reviewer-in-progress` → `approved` | `needs-rework` (reviewer verdict)
- `needs-rework` → `creator-in-progress` (if rework required)
- `approved` → `publish-in-progress` (if stable-library update approved)
- `publish-in-progress` → `pr-open` (when PR is created)
- `pr-open` → `merged` (when PR is merged)
- `merged` → `released` (when version and tag actions complete)
- `released` → terminal

## Implementation Steps

1. **Draft phase** (via `agent-skill-creator`):
   - create `.github/skills/python-comprehensions/SKILL.md` with:
     - explicit trigger: when to use this skill
     - process: decision tree for comprehension readability
     - concise positive/negative examples
     - clear boundaries vs related skills
   - create `.github/skills/python-comprehensions/reference.md` as overview
   - create `.github/skills/python-comprehensions/examples.md` for 5–8 layered
     scenarios
   - all files must follow repository skill folder contract
   - update topic plan status to `review-ready`

2. **Review phase** (via independent `agent-skill-reviewer`):
   - verify required files present (SKILL.md, reference.md, examples.md)
   - verify examples cover readability boundary cases
   - verify boundaries are explicit vs related skills
   - verify no hidden repo context is assumed
   - return `approved` or `needs-rework`
   - update topic plan status to reviewer verdict

3. **Publish phase** (if `approved`):
   - commit skill files to dev branch
   - add row to `README.md` (alphabetically after `python-class-design`)
   - update `VERSION` (MINOR bump, e.g., X.Y.Z → X.(Y+1).0)
   - create annotated git tag matching the version
   - push tag and commit
   - update topic plan status to `released`

## Artifact Paths

```
.github/skills/python-comprehensions/
  ├── SKILL.md                    # skill contract: trigger, process, examples, boundaries
  ├── reference.md                # overview, readability heuristics, scoping rules
  └── examples.md                 # 5–8 scenarios: simple, nested, edge cases, anti-patterns

README.md                          # add row at stable-library-affecting-now
VERSION                            # update to next MINOR version
plan/python-comprehensions/
  └── python-comprehensions.plan.md # this file; repo-visible execution contract
```

## Validation / Acceptance Checks

**Draft must pass**:
- [ ] SKILL.md includes explicit trigger (when to use)
- [ ] SKILL.md includes concise positive and negative examples
- [ ] reference.md explains readability boundaries with heuristics
- [ ] examples.md covers ≥5 scenarios: simple, nested, generator, filter/map,
      anti-pattern
- [ ] no file assumes hidden repo context or project-specific conventions
- [ ] skill is clearly independent of `python-functional-style` and
      `python-generators-iterators`

**Review phase verdict**: `approved` or `needs-rework`

**Publish phase success**:
- [ ] committed to dev
- [ ] README.md updated with alphabetical row
- [ ] VERSION bumped to next MINOR version
- [ ] git tag created and pushed matching the version
- [ ] status verified as released

## Reviewer Handoff

```json
{
  "phase": 2,
  "input_artifact": ".github/skills/python-comprehensions/",
  "input_format": "skill folder with SKILL.md, reference.md, examples.md",
  "reviewer_role": "agent-skill-reviewer",
  "decision_rule": "approved if all required files present, examples sufficient, boundaries explicit; needs-rework if gaps found",
  "output_format": "approved | needs-rework",
  "required_checks": [
    "required_core_files_present",
    "examples_cover_readability_boundaries",
    "boundaries_vs_related_skills_explicit",
    "no_hidden_repo_context"
  ],
  "next_actor": "main-agent-publisher"
}
```

## Post-merge / Release Actions

When `approved` and merged to dev:

1. **Stable-library promotion** (stable-library-affecting-now):
   - README.md row added (alphabetically after `python-class-design`)
   - VERSION bumped: X.Y.Z → X.(Y+1).0
   - plan status updated to `publish-in-progress`

2. **Release tagging** (post-merge):
   - Create annotated tag matching the version: `git tag -a v<VERSION> -m "Release v<VERSION>: add python-comprehensions skill"`
   - Push tag: `git push origin v<VERSION>`
   - plan status updated to `released`

3. **Verification**:
   - Confirm tag exists on remote
   - Confirm README includes new skill row
   - Confirm VERSION file matches the new version

## Open Questions / Unresolved Items

- None at plan review time.

All locked decisions are explicit. All workflow phases are defined. All transition rules match canonical handoff-workflow semantics.
