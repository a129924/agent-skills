# Semantic Drift Report
## agent-skill-creator

### Compared locations
- skills/: present
- .github/skills/: present
- .codex/skills/: present

### Textual differences
skills/ and .github/ differ on authoring target path

### Semantic differences
Observed drift changes expected output path, validation source, supported commands, or executable helper behavior.

### Behavioral impact
- high

### Examples of behavior-changing differences
- different authoring target path (`skills/` vs `.github/skills/`)
- different declared output folder

### Recommended canonical candidate
- skills/

### Reason
skills/ and .github/ differ on authoring target path

## agent-skill-template

### Compared locations
- skills/: present
- .github/skills/: present
- .codex/skills/: present

### Textual differences
template and folder-contract differ on active authoring path

### Semantic differences
Observed drift changes expected output path, validation source, supported commands, or executable helper behavior.

### Behavioral impact
- high

### Examples of behavior-changing differences
- template tree points at different root path
- folder contract differs on current active authoring path

### Recommended canonical candidate
- skills/

### Reason
template and folder-contract differ on active authoring path

## copilot-instructions-init

### Compared locations
- skills/: present
- .github/skills/: present
- .codex/skills/: missing

### Textual differences
same-name content is aligned across `skills/` and `.github/skills/`; `.codex/skills/` counterpart is missing in this worktree

### Semantic differences
No same-name semantic drift was evidenced between `skills/` and `.github/skills/`. Phase 1 evidence instead shows a platform-native Copilot contract that should not be auto-canonicalized into a generic surface.

### Behavioral impact
- low

### Examples of behavior-changing differences
- missing counterpart on at least one inspected surface
- writes `.github/copilot-instructions.md` and depends on GitHub-oriented skill inventory

### Recommended canonical candidate
- human_review_required

### Reason
`copilot_only` and `platform_native` evidence conflicts with generic canonicalization; missing `.codex/skills/` presence alone is insufficient to pick `skills/`

## git-release-management

### Compared locations
- skills/: present
- .github/skills/: present
- .codex/skills/: missing

### Textual differences
missing counterpart only

### Semantic differences
Surface presence differs; no semantic merge was attempted in Phase 1.

### Behavioral impact
- low

### Examples of behavior-changing differences
- missing counterpart on at least one inspected surface

### Recommended canonical candidate
- skills/

### Reason
counterpart missing on at least one inspected surface; no content rewrite occurred in Phase 1

## plan-creator

### Compared locations
- skills/: present
- .github/skills/: present
- .codex/skills/: present

### Textual differences
fallback contract source differs between surfaces

### Semantic differences
Observed drift changes expected output path, validation source, supported commands, or executable helper behavior.

### Behavioral impact
- high

### Examples of behavior-changing differences
- different fallback contract source
- different failure-path guidance when template is absent

### Recommended canonical candidate
- human_review_required

### Reason
fallback contract source differs between surfaces

## plan-reviewer

### Compared locations
- skills/: present
- .github/skills/: present
- .codex/skills/: present

### Textual differences
review basis path and blocked behavior differ between surfaces

### Semantic differences
Observed drift changes expected output path, validation source, supported commands, or executable helper behavior.

### Behavioral impact
- high

### Examples of behavior-changing differences
- different review-basis paths
- different blocking behavior when plan or contract sources are missing

### Recommended canonical candidate
- human_review_required

### Reason
review basis path and blocked behavior differ between surfaces

## plan-step-tracker

### Compared locations
- skills/: present
- .github/skills/: present
- .codex/skills/: missing

### Textual differences
CLI path and supported operation set differ between surfaces

### Semantic differences
Observed drift changes expected output path, validation source, supported commands, or executable helper behavior.

### Behavioral impact
- high

### Examples of behavior-changing differences
- different script path
- different supported operation set

### Recommended canonical candidate
- merge_required

### Reason
CLI path and supported operation set differ between surfaces

## python-api-signature

### Compared locations
- skills/: present
- .github/skills/: present
- .codex/skills/: missing

### Textual differences
missing counterpart only

### Semantic differences
Surface presence differs; no semantic merge was attempted in Phase 1.

### Behavioral impact
- low

### Examples of behavior-changing differences
- missing counterpart on at least one inspected surface

### Recommended canonical candidate
- skills/

### Reason
counterpart missing on at least one inspected surface; no content rewrite occurred in Phase 1

## python-async-await

### Compared locations
- skills/: present
- .github/skills/: present
- .codex/skills/: missing

### Textual differences
missing counterpart only

### Semantic differences
Surface presence differs; no semantic merge was attempted in Phase 1.

### Behavioral impact
- low

### Examples of behavior-changing differences
- missing counterpart on at least one inspected surface

### Recommended canonical candidate
- skills/

### Reason
counterpart missing on at least one inspected surface; no content rewrite occurred in Phase 1

## python-async-planning

### Compared locations
- skills/: present
- .github/skills/: present
- .codex/skills/: missing

### Textual differences
missing counterpart only

### Semantic differences
Surface presence differs; no semantic merge was attempted in Phase 1.

### Behavioral impact
- low

### Examples of behavior-changing differences
- missing counterpart on at least one inspected surface

### Recommended canonical candidate
- skills/

### Reason
counterpart missing on at least one inspected surface; no content rewrite occurred in Phase 1

## python-blueprint-authoring

### Compared locations
- skills/: present
- .github/skills/: present
- .codex/skills/: missing

### Textual differences
github surface adds checklist and reference set

### Semantic differences
Observed drift changes expected output path, validation source, supported commands, or executable helper behavior.

### Behavioral impact
- medium

### Examples of behavior-changing differences
- different required companion files
- different executor-facing blueprint contract assumptions

### Recommended canonical candidate
- merge_required

### Reason
github surface adds checklist and reference set

## python-blueprint-review

### Compared locations
- skills/: missing
- .github/skills/: present
- .codex/skills/: missing

### Textual differences
missing canonical counterpart under skills/; validates exact current library root via .github/skills path

### Semantic differences
Surface presence differs; no semantic merge was attempted in Phase 1.

### Behavioral impact
- medium

### Examples of behavior-changing differences
- skill missing from skills/ canonical tree candidate set

### Recommended canonical candidate
- .github/skills/

### Reason
counterpart missing on at least one inspected surface; no content rewrite occurred in Phase 1

## python-class-design

### Compared locations
- skills/: present
- .github/skills/: present
- .codex/skills/: missing

### Textual differences
missing counterpart only

### Semantic differences
Surface presence differs; no semantic merge was attempted in Phase 1.

### Behavioral impact
- low

### Examples of behavior-changing differences
- missing counterpart on at least one inspected surface

### Recommended canonical candidate
- skills/

### Reason
counterpart missing on at least one inspected surface; no content rewrite occurred in Phase 1

## python-code-review

### Compared locations
- skills/: present
- .github/skills/: present
- .codex/skills/: missing

### Textual differences
missing counterpart only

### Semantic differences
Surface presence differs; no semantic merge was attempted in Phase 1.

### Behavioral impact
- low

### Examples of behavior-changing differences
- missing counterpart on at least one inspected surface

### Recommended canonical candidate
- skills/

### Reason
counterpart missing on at least one inspected surface; no content rewrite occurred in Phase 1

## python-comprehensions

### Compared locations
- skills/: present
- .github/skills/: present
- .codex/skills/: missing

### Textual differences
missing counterpart only

### Semantic differences
Surface presence differs; no semantic merge was attempted in Phase 1.

### Behavioral impact
- low

### Examples of behavior-changing differences
- missing counterpart on at least one inspected surface

### Recommended canonical candidate
- skills/

### Reason
counterpart missing on at least one inspected surface; no content rewrite occurred in Phase 1

## python-context-management

### Compared locations
- skills/: present
- .github/skills/: present
- .codex/skills/: missing

### Textual differences
missing counterpart only

### Semantic differences
Surface presence differs; no semantic merge was attempted in Phase 1.

### Behavioral impact
- low

### Examples of behavior-changing differences
- missing counterpart on at least one inspected surface

### Recommended canonical candidate
- skills/

### Reason
counterpart missing on at least one inspected surface; no content rewrite occurred in Phase 1

## python-control-flow

### Compared locations
- skills/: present
- .github/skills/: present
- .codex/skills/: missing

### Textual differences
missing counterpart only

### Semantic differences
Surface presence differs; no semantic merge was attempted in Phase 1.

### Behavioral impact
- low

### Examples of behavior-changing differences
- missing counterpart on at least one inspected surface

### Recommended canonical candidate
- skills/

### Reason
counterpart missing on at least one inspected surface; no content rewrite occurred in Phase 1

## python-data-model-methods

### Compared locations
- skills/: present
- .github/skills/: present
- .codex/skills/: missing

### Textual differences
missing counterpart only

### Semantic differences
Surface presence differs; no semantic merge was attempted in Phase 1.

### Behavioral impact
- low

### Examples of behavior-changing differences
- missing counterpart on at least one inspected surface

### Recommended canonical candidate
- skills/

### Reason
counterpart missing on at least one inspected surface; no content rewrite occurred in Phase 1

## python-decorators

### Compared locations
- skills/: present
- .github/skills/: present
- .codex/skills/: missing

### Textual differences
missing counterpart only

### Semantic differences
Surface presence differs; no semantic merge was attempted in Phase 1.

### Behavioral impact
- low

### Examples of behavior-changing differences
- missing counterpart on at least one inspected surface

### Recommended canonical candidate
- skills/

### Reason
counterpart missing on at least one inspected surface; no content rewrite occurred in Phase 1

## python-descriptors-attribute-access

### Compared locations
- skills/: present
- .github/skills/: present
- .codex/skills/: missing

### Textual differences
missing counterpart only

### Semantic differences
Surface presence differs; no semantic merge was attempted in Phase 1.

### Behavioral impact
- low

### Examples of behavior-changing differences
- missing counterpart on at least one inspected surface

### Recommended canonical candidate
- skills/

### Reason
counterpart missing on at least one inspected surface; no content rewrite occurred in Phase 1

## python-docstrings

### Compared locations
- skills/: present
- .github/skills/: present
- .codex/skills/: missing

### Textual differences
missing counterpart only

### Semantic differences
Surface presence differs; no semantic merge was attempted in Phase 1.

### Behavioral impact
- low

### Examples of behavior-changing differences
- missing counterpart on at least one inspected surface

### Recommended canonical candidate
- skills/

### Reason
counterpart missing on at least one inspected surface; no content rewrite occurred in Phase 1

## python-error-handling

### Compared locations
- skills/: present
- .github/skills/: present
- .codex/skills/: missing

### Textual differences
missing counterpart only

### Semantic differences
Surface presence differs; no semantic merge was attempted in Phase 1.

### Behavioral impact
- low

### Examples of behavior-changing differences
- missing counterpart on at least one inspected surface

### Recommended canonical candidate
- skills/

### Reason
counterpart missing on at least one inspected surface; no content rewrite occurred in Phase 1

## python-generators-iterators

### Compared locations
- skills/: present
- .github/skills/: present
- .codex/skills/: missing

### Textual differences
missing counterpart only

### Semantic differences
Surface presence differs; no semantic merge was attempted in Phase 1.

### Behavioral impact
- low

### Examples of behavior-changing differences
- missing counterpart on at least one inspected surface

### Recommended canonical candidate
- skills/

### Reason
counterpart missing on at least one inspected surface; no content rewrite occurred in Phase 1

## python-implementation-review

### Compared locations
- skills/: present
- .github/skills/: present
- .codex/skills/: missing

### Textual differences
missing counterpart only

### Semantic differences
Surface presence differs; no semantic merge was attempted in Phase 1.

### Behavioral impact
- low

### Examples of behavior-changing differences
- missing counterpart on at least one inspected surface

### Recommended canonical candidate
- skills/

### Reason
counterpart missing on at least one inspected surface; no content rewrite occurred in Phase 1

## python-library-architecture

### Compared locations
- skills/: present
- .github/skills/: present
- .codex/skills/: missing

### Textual differences
github surface adds reference.md and broader validation wording

### Semantic differences
Guidance and supporting material differ enough to change interpretation, but direct execution behavior was not proven universally.

### Behavioral impact
- medium

### Examples of behavior-changing differences
- GitHub surface adds reference-driven review baseline

### Recommended canonical candidate
- merge_required

### Reason
meaning or guidance differs, but direct runtime impact is not fully proven from text alone

## python-model-selection

### Compared locations
- skills/: present
- .github/skills/: present
- .codex/skills/: missing

### Textual differences
missing counterpart only

### Semantic differences
Surface presence differs; no semantic merge was attempted in Phase 1.

### Behavioral impact
- low

### Examples of behavior-changing differences
- missing counterpart on at least one inspected surface

### Recommended canonical candidate
- skills/

### Reason
counterpart missing on at least one inspected surface; no content rewrite occurred in Phase 1

## python-module-boundaries

### Compared locations
- skills/: present
- .github/skills/: present
- .codex/skills/: missing

### Textual differences
missing counterpart only

### Semantic differences
Surface presence differs; no semantic merge was attempted in Phase 1.

### Behavioral impact
- low

### Examples of behavior-changing differences
- missing counterpart on at least one inspected surface

### Recommended canonical candidate
- skills/

### Reason
counterpart missing on at least one inspected surface; no content rewrite occurred in Phase 1

## python-naming

### Compared locations
- skills/: present
- .github/skills/: present
- .codex/skills/: missing

### Textual differences
missing counterpart only

### Semantic differences
Surface presence differs; no semantic merge was attempted in Phase 1.

### Behavioral impact
- low

### Examples of behavior-changing differences
- missing counterpart on at least one inspected surface

### Recommended canonical candidate
- skills/

### Reason
counterpart missing on at least one inspected surface; no content rewrite occurred in Phase 1

## python-operator-overloading

### Compared locations
- skills/: present
- .github/skills/: present
- .codex/skills/: missing

### Textual differences
missing counterpart only

### Semantic differences
Surface presence differs; no semantic merge was attempted in Phase 1.

### Behavioral impact
- low

### Examples of behavior-changing differences
- missing counterpart on at least one inspected surface

### Recommended canonical candidate
- skills/

### Reason
counterpart missing on at least one inspected surface; no content rewrite occurred in Phase 1

## python-package-layout

### Compared locations
- skills/: present
- .github/skills/: present
- .codex/skills/: missing

### Textual differences
github surface adds reference.md and broader routing wording

### Semantic differences
Guidance and supporting material differ enough to change interpretation, but direct execution behavior was not proven universally.

### Behavioral impact
- medium

### Examples of behavior-changing differences
- GitHub surface adds stronger redirect and validation language

### Recommended canonical candidate
- merge_required

### Reason
meaning or guidance differs, but direct runtime impact is not fully proven from text alone

## python-plan-authoring

### Compared locations
- skills/: present
- .github/skills/: present
- .codex/skills/: missing

### Textual differences
github surface adds templates and expanded plan contract

### Semantic differences
Observed drift changes expected output path, validation source, supported commands, or executable helper behavior.

### Behavioral impact
- medium

### Examples of behavior-changing differences
- different required artifact set
- different template surface and plan-shape expectations

### Recommended canonical candidate
- merge_required

### Reason
github surface adds templates and expanded plan contract

## python-plan-review

### Compared locations
- skills/: present
- .github/skills/: present
- .codex/skills/: missing

### Textual differences
missing counterpart only

### Semantic differences
Surface presence differs; no semantic merge was attempted in Phase 1.

### Behavioral impact
- low

### Examples of behavior-changing differences
- missing counterpart on at least one inspected surface

### Recommended canonical candidate
- skills/

### Reason
counterpart missing on at least one inspected surface; no content rewrite occurred in Phase 1

## python-pre-commit

### Compared locations
- skills/: present
- .github/skills/: present
- .codex/skills/: missing

### Textual differences
github surface adds script, templates, references, and tests

### Semantic differences
Observed drift changes expected output path, validation source, supported commands, or executable helper behavior.

### Behavioral impact
- high

### Examples of behavior-changing differences
- script-driven config write exists only on GitHub surface
- extra references, template, and tests alter expected usage

### Recommended canonical candidate
- merge_required

### Reason
github surface adds script, templates, references, and tests

## python-project-init-greenfield

### Compared locations
- skills/: present
- .github/skills/: present
- .codex/skills/: missing

### Textual differences
same-name content is identical across `skills/` and `.github/skills/`; `.codex/skills/` counterpart is missing in this worktree

### Semantic differences
No same-name semantic drift was evidenced. The remaining gap is projection presence, not content divergence.

### Behavioral impact
- none

### Examples of behavior-changing differences
- missing counterpart on at least one inspected surface

### Recommended canonical candidate
- skills/

### Reason
same-name content is identical between `skills/` and `.github/skills/`; the remaining gap is missing `.codex/skills/` projection only

## python-project-retrofit

### Compared locations
- skills/: present
- .github/skills/: present
- .codex/skills/: missing

### Textual differences
same-name content is identical across `skills/` and `.github/skills/`; `.codex/skills/` counterpart is missing in this worktree

### Semantic differences
No same-name semantic drift was evidenced. The remaining gap is projection presence, not content divergence.

### Behavioral impact
- none

### Examples of behavior-changing differences
- missing counterpart on at least one inspected surface

### Recommended canonical candidate
- skills/

### Reason
same-name content is identical between `skills/` and `.github/skills/`; the remaining gap is missing `.codex/skills/` projection only

## python-pyproject-toolconfig

### Compared locations
- skills/: present
- .github/skills/: present
- .codex/skills/: missing

### Textual differences
github surface adds script, templates, references, and tests

### Semantic differences
Observed drift changes expected output path, validation source, supported commands, or executable helper behavior.

### Behavioral impact
- high

### Examples of behavior-changing differences
- append script exists only on GitHub surface
- template/test set changes expected execution path

### Recommended canonical candidate
- merge_required

### Reason
github surface adds script, templates, references, and tests

## python-retrofit-plan-authoring

### Compared locations
- skills/: present
- .github/skills/: present
- .codex/skills/: missing

### Textual differences
missing counterpart only

### Semantic differences
Surface presence differs; no semantic merge was attempted in Phase 1.

### Behavioral impact
- low

### Examples of behavior-changing differences
- missing counterpart on at least one inspected surface

### Recommended canonical candidate
- skills/

### Reason
counterpart missing on at least one inspected surface; no content rewrite occurred in Phase 1

## python-retrofit-plan-review

### Compared locations
- skills/: present
- .github/skills/: present
- .codex/skills/: missing

### Textual differences
missing counterpart only

### Semantic differences
Surface presence differs; no semantic merge was attempted in Phase 1.

### Behavioral impact
- low

### Examples of behavior-changing differences
- missing counterpart on at least one inspected surface

### Recommended canonical candidate
- skills/

### Reason
counterpart missing on at least one inspected surface; no content rewrite occurred in Phase 1

## python-serialization-boundaries

### Compared locations
- skills/: present
- .github/skills/: present
- .codex/skills/: missing

### Textual differences
only REVIEW.md differs

### Semantic differences
Meaning appears unchanged; observed drift is limited to report/review metadata wording.

### Behavioral impact
- none

### Examples of behavior-changing differences
- review metadata date placeholder differs

### Recommended canonical candidate
- skills/

### Reason
content drift is limited to review metadata wording

## python-tdd-test-authoring

### Compared locations
- skills/: present
- .github/skills/: present
- .codex/skills/: missing

### Textual differences
github surface adds checklist and verdict-oriented references

### Semantic differences
Observed drift changes expected output path, validation source, supported commands, or executable helper behavior.

### Behavioral impact
- medium

### Examples of behavior-changing differences
- GitHub surface adds checklist and verdict-oriented references
- output expectations become workflow-gated rather than purely advisory

### Recommended canonical candidate
- merge_required

### Reason
github surface adds checklist and verdict-oriented references

## python-testing-pytest

### Compared locations
- skills/: present
- .github/skills/: present
- .codex/skills/: missing

### Textual differences
missing counterpart only

### Semantic differences
Surface presence differs; no semantic merge was attempted in Phase 1.

### Behavioral impact
- low

### Examples of behavior-changing differences
- missing counterpart on at least one inspected surface

### Recommended canonical candidate
- skills/

### Reason
counterpart missing on at least one inspected surface; no content rewrite occurred in Phase 1

## python-type-hints-strict

### Compared locations
- skills/: present
- .github/skills/: present
- .codex/skills/: missing

### Textual differences
missing counterpart only

### Semantic differences
Surface presence differs; no semantic merge was attempted in Phase 1.

### Behavioral impact
- low

### Examples of behavior-changing differences
- missing counterpart on at least one inspected surface

### Recommended canonical candidate
- skills/

### Reason
counterpart missing on at least one inspected surface; no content rewrite occurred in Phase 1

## sense-env-scaffold

### Compared locations
- skills/: present
- .github/skills/: present
- .codex/skills/: missing

### Textual differences
runtime assertion handling differs in script implementation

### Semantic differences
Observed drift changes expected output path, validation source, supported commands, or executable helper behavior.

### Behavioral impact
- high

### Examples of behavior-changing differences
- different malformed-assertion handling
- different contract-error path in runtime script

### Recommended canonical candidate
- merge_required

### Reason
runtime assertion handling differs in script implementation
