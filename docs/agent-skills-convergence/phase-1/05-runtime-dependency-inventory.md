# Runtime Dependency Inventory
## agent-skill-creator

### Runtime mode
projection_required

### Detected dependencies
- scripts: no
- hooks: no
- templates: no
- hard-coded paths: yes
- custom agent references: no
- subAgent references: no
- platform commands: no
- external CLI assumptions: no

### Hard-coded path evidence
- .github/skills/...

### Projection requirement
projection_required: true

### Future platform targets
Potential targets:
- .codex/skills/
- human_review_required

### Notes
skills/ and .github/ differ on authoring target path

## agent-skill-reviewer

### Runtime mode
portable

### Detected dependencies
- scripts: no
- hooks: no
- templates: no
- hard-coded paths: yes
- custom agent references: no
- subAgent references: yes
- platform commands: no
- external CLI assumptions: no

### Hard-coded path evidence
- .github/skills/...

### Projection requirement
projection_required: false

### Future platform targets
Potential targets:
- none

### Notes
no additional runtime note

## agent-skill-template

### Runtime mode
projection_required

### Detected dependencies
- scripts: no
- hooks: no
- templates: no
- hard-coded paths: yes
- custom agent references: no
- subAgent references: no
- platform commands: no
- external CLI assumptions: no

### Hard-coded path evidence
- .github/skills/...

### Projection requirement
projection_required: true

### Future platform targets
Potential targets:
- .codex/skills/
- human_review_required

### Notes
template and folder-contract differ on active authoring path

## business-intent-alignment

### Runtime mode
portable

### Detected dependencies
- scripts: no
- hooks: no
- templates: no
- hard-coded paths: no
- custom agent references: no
- subAgent references: no
- platform commands: no
- external CLI assumptions: no

### Hard-coded path evidence
- none detected

### Projection requirement
projection_required: false

### Future platform targets
Potential targets:
- none

### Notes
no additional runtime note

## business-to-technical-translation

### Runtime mode
portable

### Detected dependencies
- scripts: no
- hooks: no
- templates: no
- hard-coded paths: no
- custom agent references: no
- subAgent references: no
- platform commands: no
- external CLI assumptions: no

### Hard-coded path evidence
- none detected

### Projection requirement
projection_required: false

### Future platform targets
Potential targets:
- none

### Notes
no additional runtime note

## copilot-instructions-init

### Runtime mode
platform_native

### Detected dependencies
- scripts: no
- hooks: no
- templates: no
- hard-coded paths: yes
- custom agent references: no
- subAgent references: no
- platform commands: no
- external CLI assumptions: no

### Hard-coded path evidence
- .github/skills/...

### Projection requirement
projection_required: uncertain

### Future platform targets
Potential targets:
- .github/skills/
- human_review_required

### Notes
writes .github/copilot-instructions.md and consumes .github skill inventory

## git-branch-naming

### Runtime mode
portable

### Detected dependencies
- scripts: no
- hooks: no
- templates: no
- hard-coded paths: no
- custom agent references: no
- subAgent references: no
- platform commands: no
- external CLI assumptions: yes

### Hard-coded path evidence
- none detected

### Projection requirement
projection_required: false

### Future platform targets
Potential targets:
- none

### Notes
no additional runtime note

## git-commit-convention

### Runtime mode
portable

### Detected dependencies
- scripts: no
- hooks: no
- templates: no
- hard-coded paths: no
- custom agent references: no
- subAgent references: no
- platform commands: no
- external CLI assumptions: yes

### Hard-coded path evidence
- none detected

### Projection requirement
projection_required: false

### Future platform targets
Potential targets:
- none

### Notes
no additional runtime note

## git-post-merge-workflow

### Runtime mode
portable

### Detected dependencies
- scripts: no
- hooks: no
- templates: no
- hard-coded paths: no
- custom agent references: no
- subAgent references: no
- platform commands: no
- external CLI assumptions: yes

### Hard-coded path evidence
- none detected

### Projection requirement
projection_required: false

### Future platform targets
Potential targets:
- none

### Notes
no additional runtime note

## git-release-management

### Runtime mode
portable

### Detected dependencies
- scripts: no
- hooks: no
- templates: no
- hard-coded paths: no
- custom agent references: no
- subAgent references: no
- platform commands: no
- external CLI assumptions: yes

### Hard-coded path evidence
- none detected

### Projection requirement
projection_required: false

### Future platform targets
Potential targets:
- none

### Notes
no additional runtime note

## plan-creator

### Runtime mode
projection_required

### Detected dependencies
- scripts: no
- hooks: no
- templates: yes
- hard-coded paths: yes
- custom agent references: no
- subAgent references: no
- platform commands: no
- external CLI assumptions: no

### Hard-coded path evidence
- .github/skills/...

### Projection requirement
projection_required: true

### Future platform targets
Potential targets:
- .codex/skills/
- human_review_required

### Notes
fallback contract source differs between surfaces

## plan-reviewer

### Runtime mode
projection_required

### Detected dependencies
- scripts: no
- hooks: no
- templates: no
- hard-coded paths: yes
- custom agent references: no
- subAgent references: yes
- platform commands: no
- external CLI assumptions: no

### Hard-coded path evidence
- .github/skills/...

### Projection requirement
projection_required: true

### Future platform targets
Potential targets:
- .codex/skills/
- human_review_required

### Notes
review basis path and blocked behavior differ between surfaces

## plan-step-tracker

### Runtime mode
projection_required

### Detected dependencies
- scripts: yes
- hooks: no
- templates: no
- hard-coded paths: yes
- custom agent references: no
- subAgent references: no
- platform commands: yes
- external CLI assumptions: yes

### Hard-coded path evidence
- .github/skills/...
- scripts/...

### Projection requirement
projection_required: true

### Future platform targets
Potential targets:
- .codex/skills/
- human_review_required

### Notes
CLI path and supported operation set differ between surfaces

## python-api-signature

### Runtime mode
portable

### Detected dependencies
- scripts: no
- hooks: no
- templates: no
- hard-coded paths: no
- custom agent references: no
- subAgent references: no
- platform commands: no
- external CLI assumptions: no

### Hard-coded path evidence
- none detected

### Projection requirement
projection_required: false

### Future platform targets
Potential targets:
- none

### Notes
no additional runtime note

## python-async-await

### Runtime mode
portable

### Detected dependencies
- scripts: no
- hooks: no
- templates: no
- hard-coded paths: no
- custom agent references: no
- subAgent references: no
- platform commands: no
- external CLI assumptions: no

### Hard-coded path evidence
- none detected

### Projection requirement
projection_required: false

### Future platform targets
Potential targets:
- none

### Notes
no additional runtime note

## python-async-planning

### Runtime mode
portable

### Detected dependencies
- scripts: no
- hooks: no
- templates: no
- hard-coded paths: no
- custom agent references: no
- subAgent references: no
- platform commands: no
- external CLI assumptions: no

### Hard-coded path evidence
- none detected

### Projection requirement
projection_required: false

### Future platform targets
Potential targets:
- none

### Notes
no additional runtime note

## python-blueprint-authoring

### Runtime mode
projection_required

### Detected dependencies
- scripts: no
- hooks: no
- templates: no
- hard-coded paths: yes
- custom agent references: no
- subAgent references: no
- platform commands: no
- external CLI assumptions: no

### Hard-coded path evidence
- .github/skills/...

### Projection requirement
projection_required: true

### Future platform targets
Potential targets:
- .codex/skills/
- human_review_required

### Notes
github surface adds checklist and reference set

## python-blueprint-review

### Runtime mode
projection_required

### Detected dependencies
- scripts: no
- hooks: no
- templates: no
- hard-coded paths: yes
- custom agent references: no
- subAgent references: no
- platform commands: no
- external CLI assumptions: no

### Hard-coded path evidence
- .github/skills/...

### Projection requirement
projection_required: true

### Future platform targets
Potential targets:
- .codex/skills/
- human_review_required

### Notes
missing canonical counterpart under skills/; validates exact current library root via .github/skills path

## python-class-design

### Runtime mode
portable

### Detected dependencies
- scripts: no
- hooks: no
- templates: no
- hard-coded paths: no
- custom agent references: no
- subAgent references: no
- platform commands: no
- external CLI assumptions: no

### Hard-coded path evidence
- none detected

### Projection requirement
projection_required: false

### Future platform targets
Potential targets:
- none

### Notes
no additional runtime note

## python-code-review

### Runtime mode
portable

### Detected dependencies
- scripts: no
- hooks: no
- templates: no
- hard-coded paths: no
- custom agent references: no
- subAgent references: no
- platform commands: no
- external CLI assumptions: no

### Hard-coded path evidence
- none detected

### Projection requirement
projection_required: false

### Future platform targets
Potential targets:
- none

### Notes
no additional runtime note

## python-comprehensions

### Runtime mode
portable

### Detected dependencies
- scripts: no
- hooks: no
- templates: no
- hard-coded paths: no
- custom agent references: no
- subAgent references: no
- platform commands: no
- external CLI assumptions: no

### Hard-coded path evidence
- none detected

### Projection requirement
projection_required: false

### Future platform targets
Potential targets:
- none

### Notes
no additional runtime note

## python-context-management

### Runtime mode
portable

### Detected dependencies
- scripts: no
- hooks: no
- templates: no
- hard-coded paths: no
- custom agent references: no
- subAgent references: no
- platform commands: no
- external CLI assumptions: no

### Hard-coded path evidence
- none detected

### Projection requirement
projection_required: false

### Future platform targets
Potential targets:
- none

### Notes
no additional runtime note

## python-control-flow

### Runtime mode
portable

### Detected dependencies
- scripts: no
- hooks: no
- templates: no
- hard-coded paths: no
- custom agent references: no
- subAgent references: no
- platform commands: no
- external CLI assumptions: no

### Hard-coded path evidence
- none detected

### Projection requirement
projection_required: false

### Future platform targets
Potential targets:
- none

### Notes
no additional runtime note

## python-data-model-methods

### Runtime mode
portable

### Detected dependencies
- scripts: no
- hooks: no
- templates: no
- hard-coded paths: no
- custom agent references: no
- subAgent references: no
- platform commands: no
- external CLI assumptions: no

### Hard-coded path evidence
- none detected

### Projection requirement
projection_required: false

### Future platform targets
Potential targets:
- none

### Notes
no additional runtime note

## python-decorators

### Runtime mode
portable

### Detected dependencies
- scripts: no
- hooks: no
- templates: no
- hard-coded paths: no
- custom agent references: no
- subAgent references: no
- platform commands: no
- external CLI assumptions: no

### Hard-coded path evidence
- none detected

### Projection requirement
projection_required: false

### Future platform targets
Potential targets:
- none

### Notes
no additional runtime note

## python-descriptors-attribute-access

### Runtime mode
portable

### Detected dependencies
- scripts: no
- hooks: no
- templates: no
- hard-coded paths: no
- custom agent references: no
- subAgent references: no
- platform commands: no
- external CLI assumptions: no

### Hard-coded path evidence
- none detected

### Projection requirement
projection_required: false

### Future platform targets
Potential targets:
- none

### Notes
no additional runtime note

## python-docstrings

### Runtime mode
portable

### Detected dependencies
- scripts: no
- hooks: no
- templates: no
- hard-coded paths: no
- custom agent references: no
- subAgent references: no
- platform commands: no
- external CLI assumptions: no

### Hard-coded path evidence
- none detected

### Projection requirement
projection_required: false

### Future platform targets
Potential targets:
- none

### Notes
no additional runtime note

## python-error-handling

### Runtime mode
portable

### Detected dependencies
- scripts: no
- hooks: no
- templates: no
- hard-coded paths: no
- custom agent references: no
- subAgent references: no
- platform commands: no
- external CLI assumptions: no

### Hard-coded path evidence
- none detected

### Projection requirement
projection_required: false

### Future platform targets
Potential targets:
- none

### Notes
no additional runtime note

## python-generators-iterators

### Runtime mode
portable

### Detected dependencies
- scripts: no
- hooks: no
- templates: no
- hard-coded paths: no
- custom agent references: no
- subAgent references: no
- platform commands: no
- external CLI assumptions: no

### Hard-coded path evidence
- none detected

### Projection requirement
projection_required: false

### Future platform targets
Potential targets:
- none

### Notes
no additional runtime note

## python-implementation-review

### Runtime mode
portable

### Detected dependencies
- scripts: no
- hooks: no
- templates: no
- hard-coded paths: yes
- custom agent references: no
- subAgent references: no
- platform commands: no
- external CLI assumptions: no

### Hard-coded path evidence
- .github/skills/...

### Projection requirement
projection_required: false

### Future platform targets
Potential targets:
- none

### Notes
no additional runtime note

## python-library-architecture

### Runtime mode
portable

### Detected dependencies
- scripts: no
- hooks: no
- templates: no
- hard-coded paths: no
- custom agent references: no
- subAgent references: no
- platform commands: no
- external CLI assumptions: no

### Hard-coded path evidence
- none detected

### Projection requirement
projection_required: false

### Future platform targets
Potential targets:
- none

### Notes
github surface adds reference.md and broader validation wording

## python-model-selection

### Runtime mode
portable

### Detected dependencies
- scripts: no
- hooks: no
- templates: no
- hard-coded paths: no
- custom agent references: no
- subAgent references: no
- platform commands: no
- external CLI assumptions: no

### Hard-coded path evidence
- none detected

### Projection requirement
projection_required: false

### Future platform targets
Potential targets:
- none

### Notes
no additional runtime note

## python-module-boundaries

### Runtime mode
portable

### Detected dependencies
- scripts: no
- hooks: no
- templates: no
- hard-coded paths: no
- custom agent references: no
- subAgent references: no
- platform commands: no
- external CLI assumptions: no

### Hard-coded path evidence
- none detected

### Projection requirement
projection_required: false

### Future platform targets
Potential targets:
- none

### Notes
no additional runtime note

## python-naming

### Runtime mode
portable

### Detected dependencies
- scripts: no
- hooks: no
- templates: no
- hard-coded paths: no
- custom agent references: no
- subAgent references: no
- platform commands: no
- external CLI assumptions: no

### Hard-coded path evidence
- none detected

### Projection requirement
projection_required: false

### Future platform targets
Potential targets:
- none

### Notes
no additional runtime note

## python-operator-overloading

### Runtime mode
portable

### Detected dependencies
- scripts: no
- hooks: no
- templates: no
- hard-coded paths: no
- custom agent references: no
- subAgent references: no
- platform commands: no
- external CLI assumptions: no

### Hard-coded path evidence
- none detected

### Projection requirement
projection_required: false

### Future platform targets
Potential targets:
- none

### Notes
no additional runtime note

## python-package-layout

### Runtime mode
portable

### Detected dependencies
- scripts: no
- hooks: no
- templates: no
- hard-coded paths: yes
- custom agent references: no
- subAgent references: no
- platform commands: no
- external CLI assumptions: no

### Hard-coded path evidence
- none detected

### Projection requirement
projection_required: false

### Future platform targets
Potential targets:
- none

### Notes
github surface adds reference.md and broader routing wording

## python-plan-authoring

### Runtime mode
projection_required

### Detected dependencies
- scripts: no
- hooks: no
- templates: yes
- hard-coded paths: no
- custom agent references: no
- subAgent references: no
- platform commands: no
- external CLI assumptions: no

### Hard-coded path evidence
- none detected

### Projection requirement
projection_required: true

### Future platform targets
Potential targets:
- .codex/skills/
- human_review_required

### Notes
github surface adds templates and expanded plan contract

## python-plan-review

### Runtime mode
portable

### Detected dependencies
- scripts: no
- hooks: no
- templates: no
- hard-coded paths: no
- custom agent references: no
- subAgent references: no
- platform commands: no
- external CLI assumptions: no

### Hard-coded path evidence
- none detected

### Projection requirement
projection_required: false

### Future platform targets
Potential targets:
- none

### Notes
no additional runtime note

## python-pre-commit

### Runtime mode
projection_required

### Detected dependencies
- scripts: yes
- hooks: no
- templates: yes
- hard-coded paths: yes
- custom agent references: no
- subAgent references: no
- platform commands: yes
- external CLI assumptions: yes

### Hard-coded path evidence
- scripts/...

### Projection requirement
projection_required: true

### Future platform targets
Potential targets:
- .codex/skills/
- human_review_required

### Notes
github surface adds script, templates, references, and tests

## python-project-init-greenfield

### Runtime mode
projection_required

### Detected dependencies
- scripts: no
- hooks: no
- templates: no
- hard-coded paths: yes
- custom agent references: no
- subAgent references: no
- platform commands: no
- external CLI assumptions: yes

### Hard-coded path evidence
- .github/skills/...

### Projection requirement
projection_required: true

### Future platform targets
Potential targets:
- .codex/skills/
- human_review_required

### Notes
no additional runtime note

## python-project-retrofit

### Runtime mode
projection_required

### Detected dependencies
- scripts: no
- hooks: no
- templates: no
- hard-coded paths: yes
- custom agent references: no
- subAgent references: no
- platform commands: no
- external CLI assumptions: yes

### Hard-coded path evidence
- .github/skills/...

### Projection requirement
projection_required: true

### Future platform targets
Potential targets:
- .codex/skills/
- human_review_required

### Notes
no additional runtime note

## python-pyproject-toolconfig

### Runtime mode
projection_required

### Detected dependencies
- scripts: yes
- hooks: no
- templates: yes
- hard-coded paths: yes
- custom agent references: no
- subAgent references: no
- platform commands: yes
- external CLI assumptions: yes

### Hard-coded path evidence
- .github/skills/...
- scripts/...

### Projection requirement
projection_required: true

### Future platform targets
Potential targets:
- .codex/skills/
- human_review_required

### Notes
github surface adds script, templates, references, and tests

## python-retrofit-plan-authoring

### Runtime mode
portable

### Detected dependencies
- scripts: no
- hooks: no
- templates: no
- hard-coded paths: no
- custom agent references: no
- subAgent references: no
- platform commands: no
- external CLI assumptions: no

### Hard-coded path evidence
- none detected

### Projection requirement
projection_required: false

### Future platform targets
Potential targets:
- none

### Notes
no additional runtime note

## python-retrofit-plan-review

### Runtime mode
portable

### Detected dependencies
- scripts: no
- hooks: no
- templates: no
- hard-coded paths: no
- custom agent references: no
- subAgent references: no
- platform commands: no
- external CLI assumptions: no

### Hard-coded path evidence
- none detected

### Projection requirement
projection_required: false

### Future platform targets
Potential targets:
- none

### Notes
no additional runtime note

## python-serialization-boundaries

### Runtime mode
portable

### Detected dependencies
- scripts: no
- hooks: no
- templates: no
- hard-coded paths: no
- custom agent references: no
- subAgent references: no
- platform commands: no
- external CLI assumptions: no

### Hard-coded path evidence
- none detected

### Projection requirement
projection_required: false

### Future platform targets
Potential targets:
- none

### Notes
only REVIEW.md differs

## python-tdd-test-authoring

### Runtime mode
projection_required

### Detected dependencies
- scripts: no
- hooks: no
- templates: no
- hard-coded paths: no
- custom agent references: no
- subAgent references: no
- platform commands: no
- external CLI assumptions: no

### Hard-coded path evidence
- none detected

### Projection requirement
projection_required: true

### Future platform targets
Potential targets:
- .codex/skills/
- human_review_required

### Notes
github surface adds checklist and verdict-oriented references

## python-testing-pytest

### Runtime mode
portable

### Detected dependencies
- scripts: no
- hooks: no
- templates: no
- hard-coded paths: no
- custom agent references: no
- subAgent references: no
- platform commands: no
- external CLI assumptions: no

### Hard-coded path evidence
- none detected

### Projection requirement
projection_required: false

### Future platform targets
Potential targets:
- none

### Notes
no additional runtime note

## python-type-hints-strict

### Runtime mode
portable

### Detected dependencies
- scripts: no
- hooks: no
- templates: no
- hard-coded paths: no
- custom agent references: no
- subAgent references: no
- platform commands: no
- external CLI assumptions: no

### Hard-coded path evidence
- none detected

### Projection requirement
projection_required: false

### Future platform targets
Potential targets:
- none

### Notes
no additional runtime note

## sense-env-scaffold

### Runtime mode
projection_required

### Detected dependencies
- scripts: yes
- hooks: no
- templates: no
- hard-coded paths: yes
- custom agent references: no
- subAgent references: no
- platform commands: yes
- external CLI assumptions: yes

### Hard-coded path evidence
- .github/skills/...
- scripts/...

### Projection requirement
projection_required: true

### Future platform targets
Potential targets:
- .codex/skills/
- human_review_required

### Notes
runtime assertion handling differs in script implementation

## worktree-manager

### Runtime mode
portable

### Detected dependencies
- scripts: no
- hooks: no
- templates: no
- hard-coded paths: no
- custom agent references: no
- subAgent references: no
- platform commands: no
- external CLI assumptions: yes

### Hard-coded path evidence
- none detected

### Projection requirement
projection_required: false

### Future platform targets
Potential targets:
- none

### Notes
no additional runtime note
