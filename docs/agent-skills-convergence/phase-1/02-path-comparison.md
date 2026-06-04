# Path Comparison
## agent-skill-creator
### Presence
- skills/: yes
- .github/skills/: yes
- .codex/skills/: yes

### File set comparison
| File | skills/ | .github/skills/ | .codex/skills/ | Status |
| --- | ---: | ---: | ---: | --- |
| SKILL.md | 1 | 1 | 1 | all-present |
| blueprint.md | 1 | 1 | 1 | all-present |
| examples.md | 1 | 1 | 1 | all-present |
| folder-contract.md | 1 | 1 | 1 | all-present |

### Normalized comparison result

difference_level: behavior_diff

### Notes
- skills/ and .github/ differ on authoring target path; matches `.github/skills/` projection

## agent-skill-reviewer
### Presence
- skills/: yes
- .github/skills/: yes
- .codex/skills/: yes

### File set comparison
| File | skills/ | .github/skills/ | .codex/skills/ | Status |
| --- | ---: | ---: | ---: | --- |
| SKILL.md | 1 | 1 | 1 | all-present |
| examples.md | 1 | 1 | 1 | all-present |
| review-checklist.md | 1 | 1 | 1 | all-present |

### Normalized comparison result

difference_level: identical

### Notes
- matches `.github/skills/` projection

## agent-skill-template
### Presence
- skills/: yes
- .github/skills/: yes
- .codex/skills/: yes

### File set comparison
| File | skills/ | .github/skills/ | .codex/skills/ | Status |
| --- | ---: | ---: | ---: | --- |
| SKILL.md | 1 | 1 | 1 | all-present |
| folder-contract.md | 1 | 1 | 1 | all-present |
| reference.md | 1 | 1 | 1 | all-present |
| template.md | 1 | 1 | 1 | all-present |

### Normalized comparison result

difference_level: behavior_diff

### Notes
- template and folder-contract differ on active authoring path; matches `.github/skills/` projection

## business-intent-alignment
### Presence
- skills/: yes
- .github/skills/: yes
- .codex/skills/: yes

### File set comparison
| File | skills/ | .github/skills/ | .codex/skills/ | Status |
| --- | ---: | ---: | ---: | --- |
| SKILL.md | 1 | 1 | 1 | all-present |
| checklist.md | 1 | 1 | 1 | all-present |
| examples.md | 1 | 1 | 1 | all-present |
| reference.md | 1 | 1 | 1 | all-present |

### Normalized comparison result

difference_level: identical

### Notes
- matches `skills/` projection

## business-to-technical-translation
### Presence
- skills/: yes
- .github/skills/: yes
- .codex/skills/: yes

### File set comparison
| File | skills/ | .github/skills/ | .codex/skills/ | Status |
| --- | ---: | ---: | ---: | --- |
| SKILL.md | 1 | 1 | 1 | all-present |
| checklist.md | 1 | 1 | 1 | all-present |
| examples.md | 1 | 1 | 1 | all-present |
| reference.md | 1 | 1 | 1 | all-present |

### Normalized comparison result

difference_level: identical

### Notes
- matches `skills/` projection

## copilot-instructions-init
### Presence
- skills/: yes
- .github/skills/: yes
- .codex/skills/: no

### File set comparison
| File | skills/ | .github/skills/ | .codex/skills/ | Status |
| --- | ---: | ---: | ---: | --- |
| SKILL.md | 1 | 1 | 0 | missing-in-one-surface |
| checklist.md | 1 | 1 | 0 | missing-in-one-surface |
| examples.md | 1 | 1 | 0 | missing-in-one-surface |
| references/input-sources-and-priority.md | 1 | 1 | 0 | missing-in-one-surface |
| references/instruction-layering.md | 1 | 1 | 0 | missing-in-one-surface |
| references/merge-and-conflict-policy.md | 1 | 1 | 0 | missing-in-one-surface |

### Normalized comparison result

difference_level: missing_counterpart

### Notes
- writes .github/copilot-instructions.md and consumes .github skill inventory

## git-branch-naming
### Presence
- skills/: yes
- .github/skills/: yes
- .codex/skills/: yes

### File set comparison
| File | skills/ | .github/skills/ | .codex/skills/ | Status |
| --- | ---: | ---: | ---: | --- |
| SKILL.md | 1 | 1 | 1 | all-present |
| examples.md | 1 | 1 | 1 | all-present |
| references/conflict-and-fallbacks.md | 1 | 1 | 1 | all-present |
| references/migration-playbooks.md | 1 | 1 | 1 | all-present |
| references/naming-patterns.md | 1 | 1 | 1 | all-present |

### Normalized comparison result

difference_level: identical

### Notes
- matches `.github/skills/` projection

## git-commit-convention
### Presence
- skills/: yes
- .github/skills/: yes
- .codex/skills/: yes

### File set comparison
| File | skills/ | .github/skills/ | .codex/skills/ | Status |
| --- | ---: | ---: | ---: | --- |
| SKILL.md | 1 | 1 | 1 | all-present |
| examples.md | 1 | 1 | 1 | all-present |
| references/scope-alignment.md | 1 | 1 | 1 | all-present |
| references/split-and-repair.md | 1 | 1 | 1 | all-present |
| references/type-selection.md | 1 | 1 | 1 | all-present |

### Normalized comparison result

difference_level: identical

### Notes
- matches `.github/skills/` projection

## git-post-merge-workflow
### Presence
- skills/: yes
- .github/skills/: yes
- .codex/skills/: yes

### File set comparison
| File | skills/ | .github/skills/ | .codex/skills/ | Status |
| --- | ---: | ---: | ---: | --- |
| SKILL.md | 1 | 1 | 1 | all-present |
| examples.md | 1 | 1 | 1 | all-present |
| references/stop-point-2-checklist.md | 1 | 1 | 1 | all-present |

### Normalized comparison result

difference_level: identical

### Notes
- matches `.github/skills/` projection

## git-release-management
### Presence
- skills/: yes
- .github/skills/: yes
- .codex/skills/: no

### File set comparison
| File | skills/ | .github/skills/ | .codex/skills/ | Status |
| --- | ---: | ---: | ---: | --- |
| SKILL.md | 1 | 1 | 0 | missing-in-one-surface |
| examples.md | 1 | 1 | 0 | missing-in-one-surface |
| references/emergency-path.md | 1 | 1 | 0 | missing-in-one-surface |
| references/gate-contract.md | 1 | 1 | 0 | missing-in-one-surface |
| references/version-bump-guidance.md | 1 | 1 | 0 | missing-in-one-surface |
| references/version-sources.md | 1 | 1 | 0 | missing-in-one-surface |

### Normalized comparison result

difference_level: missing_counterpart

### Notes
- no additional note

## plan-creator
### Presence
- skills/: yes
- .github/skills/: yes
- .codex/skills/: yes

### File set comparison
| File | skills/ | .github/skills/ | .codex/skills/ | Status |
| --- | ---: | ---: | ---: | --- |
| SKILL.md | 1 | 1 | 1 | all-present |
| checklist.md | 1 | 1 | 1 | all-present |
| examples.md | 1 | 1 | 1 | all-present |
| reference.md | 1 | 1 | 1 | all-present |
| references/artifact-path-rule.md | 1 | 1 | 1 | all-present |
| references/required-section-meaning.md | 1 | 1 | 1 | all-present |
| references/role-boundary-rule.md | 1 | 1 | 1 | all-present |
| references/stable-library-rule.md | 1 | 1 | 1 | all-present |
| references/stop-and-ask-triggers.md | 1 | 1 | 1 | all-present |
| references/template-usage-rule.md | 1 | 1 | 1 | all-present |
| templates/topic-plan-template.md | 1 | 1 | 1 | all-present |

### Normalized comparison result

difference_level: behavior_diff

### Notes
- fallback contract source differs between surfaces; matches `skills/` projection

## plan-reviewer
### Presence
- skills/: yes
- .github/skills/: yes
- .codex/skills/: yes

### File set comparison
| File | skills/ | .github/skills/ | .codex/skills/ | Status |
| --- | ---: | ---: | ---: | --- |
| SKILL.md | 1 | 1 | 1 | all-present |
| checklist.md | 1 | 1 | 1 | all-present |
| examples.md | 1 | 1 | 1 | all-present |
| reference.md | 1 | 1 | 1 | all-present |

### Normalized comparison result

difference_level: behavior_diff

### Notes
- review basis path and blocked behavior differ between surfaces; matches `skills/` projection

## plan-step-tracker
### Presence
- skills/: yes
- .github/skills/: yes
- .codex/skills/: no

### File set comparison
| File | skills/ | .github/skills/ | .codex/skills/ | Status |
| --- | ---: | ---: | ---: | --- |
| SKILL.md | 1 | 1 | 0 | missing-in-one-surface |
| examples.md | 1 | 1 | 0 | missing-in-one-surface |
| reference.md | 1 | 1 | 0 | missing-in-one-surface |
| scripts/step_tracker.py | 1 | 1 | 0 | missing-in-one-surface |
| tests/test_step_tracker.py | 1 | 1 | 0 | missing-in-one-surface |

### Normalized comparison result

difference_level: behavior_diff

### Notes
- CLI path and supported operation set differ between surfaces

## python-api-signature
### Presence
- skills/: yes
- .github/skills/: yes
- .codex/skills/: no

### File set comparison
| File | skills/ | .github/skills/ | .codex/skills/ | Status |
| --- | ---: | ---: | ---: | --- |
| SKILL.md | 1 | 1 | 0 | missing-in-one-surface |
| examples.md | 1 | 1 | 0 | missing-in-one-surface |

### Normalized comparison result

difference_level: missing_counterpart

### Notes
- no additional note

## python-async-await
### Presence
- skills/: yes
- .github/skills/: yes
- .codex/skills/: no

### File set comparison
| File | skills/ | .github/skills/ | .codex/skills/ | Status |
| --- | ---: | ---: | ---: | --- |
| SKILL.md | 1 | 1 | 0 | missing-in-one-surface |
| examples.md | 1 | 1 | 0 | missing-in-one-surface |
| reference.md | 1 | 1 | 0 | missing-in-one-surface |
| references/async-protocols.md | 1 | 1 | 0 | missing-in-one-surface |
| references/cancellation-and-failure.md | 1 | 1 | 0 | missing-in-one-surface |
| references/structured-concurrency.md | 1 | 1 | 0 | missing-in-one-surface |

### Normalized comparison result

difference_level: missing_counterpart

### Notes
- no additional note

## python-async-planning
### Presence
- skills/: yes
- .github/skills/: yes
- .codex/skills/: no

### File set comparison
| File | skills/ | .github/skills/ | .codex/skills/ | Status |
| --- | ---: | ---: | ---: | --- |
| SKILL.md | 1 | 1 | 0 | missing-in-one-surface |
| examples.md | 1 | 1 | 0 | missing-in-one-surface |
| reference.md | 1 | 1 | 0 | missing-in-one-surface |

### Normalized comparison result

difference_level: missing_counterpart

### Notes
- no additional note

## python-blueprint-authoring
### Presence
- skills/: yes
- .github/skills/: yes
- .codex/skills/: no

### File set comparison
| File | skills/ | .github/skills/ | .codex/skills/ | Status |
| --- | ---: | ---: | ---: | --- |
| SKILL.md | 1 | 1 | 0 | missing-in-one-surface |
| checklist.md | 0 | 1 | 0 | single-surface-only |
| examples.md | 1 | 1 | 0 | missing-in-one-surface |
| references/blueprint-contract.md | 0 | 1 | 0 | single-surface-only |
| references/greenfield-lane-boundaries.md | 0 | 1 | 0 | single-surface-only |
| references/required-skills-validation.md | 0 | 1 | 0 | single-surface-only |
| references/structural-invariants-locatability.md | 0 | 1 | 0 | single-surface-only |

### Normalized comparison result

difference_level: behavior_diff

### Notes
- github surface adds checklist and reference set

## python-blueprint-review
### Presence
- skills/: no
- .github/skills/: yes
- .codex/skills/: no

### File set comparison
| File | skills/ | .github/skills/ | .codex/skills/ | Status |
| --- | ---: | ---: | ---: | --- |
| SKILL.md | 0 | 1 | 0 | single-surface-only |
| checklist.md | 0 | 1 | 0 | single-surface-only |
| examples.md | 0 | 1 | 0 | single-surface-only |
| references/blueprint-v1-review-checks.md | 0 | 1 | 0 | single-surface-only |
| references/greenfield-fit-and-reroute.md | 0 | 1 | 0 | single-surface-only |
| references/required-skills-and-locatability-checks.md | 0 | 1 | 0 | single-surface-only |
| references/review-verdict-contract.md | 0 | 1 | 0 | single-surface-only |

### Normalized comparison result

difference_level: missing_counterpart

### Notes
- missing canonical counterpart under skills/; validates exact current library root via .github/skills path

## python-class-design
### Presence
- skills/: yes
- .github/skills/: yes
- .codex/skills/: no

### File set comparison
| File | skills/ | .github/skills/ | .codex/skills/ | Status |
| --- | ---: | ---: | ---: | --- |
| SKILL.md | 1 | 1 | 0 | missing-in-one-surface |
| examples.md | 1 | 1 | 0 | missing-in-one-surface |

### Normalized comparison result

difference_level: missing_counterpart

### Notes
- no additional note

## python-code-review
### Presence
- skills/: yes
- .github/skills/: yes
- .codex/skills/: no

### File set comparison
| File | skills/ | .github/skills/ | .codex/skills/ | Status |
| --- | ---: | ---: | ---: | --- |
| SKILL.md | 1 | 1 | 0 | missing-in-one-surface |
| examples.md | 1 | 1 | 0 | missing-in-one-surface |
| reference.md | 1 | 1 | 0 | missing-in-one-surface |
| references/anti-patterns.md | 1 | 1 | 0 | missing-in-one-surface |
| references/cross-skill-signposts.md | 1 | 1 | 0 | missing-in-one-surface |
| references/observability.md | 1 | 1 | 0 | missing-in-one-surface |
| references/test-quality.md | 1 | 1 | 0 | missing-in-one-surface |
| references/tooling-detection.md | 1 | 1 | 0 | missing-in-one-surface |

### Normalized comparison result

difference_level: missing_counterpart

### Notes
- no additional note

## python-comprehensions
### Presence
- skills/: yes
- .github/skills/: yes
- .codex/skills/: no

### File set comparison
| File | skills/ | .github/skills/ | .codex/skills/ | Status |
| --- | ---: | ---: | ---: | --- |
| SKILL.md | 1 | 1 | 0 | missing-in-one-surface |
| examples.md | 1 | 1 | 0 | missing-in-one-surface |
| reference.md | 1 | 1 | 0 | missing-in-one-surface |

### Normalized comparison result

difference_level: missing_counterpart

### Notes
- no additional note

## python-context-management
### Presence
- skills/: yes
- .github/skills/: yes
- .codex/skills/: no

### File set comparison
| File | skills/ | .github/skills/ | .codex/skills/ | Status |
| --- | ---: | ---: | ---: | --- |
| SKILL.md | 1 | 1 | 0 | missing-in-one-surface |
| examples.md | 1 | 1 | 0 | missing-in-one-surface |

### Normalized comparison result

difference_level: missing_counterpart

### Notes
- no additional note

## python-control-flow
### Presence
- skills/: yes
- .github/skills/: yes
- .codex/skills/: no

### File set comparison
| File | skills/ | .github/skills/ | .codex/skills/ | Status |
| --- | ---: | ---: | ---: | --- |
| SKILL.md | 1 | 1 | 0 | missing-in-one-surface |
| examples.md | 1 | 1 | 0 | missing-in-one-surface |

### Normalized comparison result

difference_level: missing_counterpart

### Notes
- no additional note

## python-data-model-methods
### Presence
- skills/: yes
- .github/skills/: yes
- .codex/skills/: no

### File set comparison
| File | skills/ | .github/skills/ | .codex/skills/ | Status |
| --- | ---: | ---: | ---: | --- |
| SKILL.md | 1 | 1 | 0 | missing-in-one-surface |
| examples.md | 1 | 1 | 0 | missing-in-one-surface |
| reference.md | 1 | 1 | 0 | missing-in-one-surface |
| references/construction-and-representation.md | 1 | 1 | 0 | missing-in-one-surface |
| references/container-protocols.md | 1 | 1 | 0 | missing-in-one-surface |
| references/equality-hash-and-dataclass.md | 1 | 1 | 0 | missing-in-one-surface |

### Normalized comparison result

difference_level: missing_counterpart

### Notes
- no additional note

## python-decorators
### Presence
- skills/: yes
- .github/skills/: yes
- .codex/skills/: no

### File set comparison
| File | skills/ | .github/skills/ | .codex/skills/ | Status |
| --- | ---: | ---: | ---: | --- |
| SKILL.md | 1 | 1 | 0 | missing-in-one-surface |
| examples.md | 1 | 1 | 0 | missing-in-one-surface |
| reference.md | 1 | 1 | 0 | missing-in-one-surface |
| references/behavior-visibility.md | 1 | 1 | 0 | missing-in-one-surface |
| references/framework-notes.md | 1 | 1 | 0 | missing-in-one-surface |
| references/signature-integrity.md | 1 | 1 | 0 | missing-in-one-surface |

### Normalized comparison result

difference_level: missing_counterpart

### Notes
- no additional note

## python-descriptors-attribute-access
### Presence
- skills/: yes
- .github/skills/: yes
- .codex/skills/: no

### File set comparison
| File | skills/ | .github/skills/ | .codex/skills/ | Status |
| --- | ---: | ---: | ---: | --- |
| SKILL.md | 1 | 1 | 0 | missing-in-one-surface |
| examples.md | 1 | 1 | 0 | missing-in-one-surface |
| reference.md | 1 | 1 | 0 | missing-in-one-surface |
| references/attribute-hooks.md | 1 | 1 | 0 | missing-in-one-surface |
| references/custom-descriptors.md | 1 | 1 | 0 | missing-in-one-surface |
| references/mechanism-ladder.md | 1 | 1 | 0 | missing-in-one-surface |
| references/property-and-cached-property.md | 1 | 1 | 0 | missing-in-one-surface |

### Normalized comparison result

difference_level: missing_counterpart

### Notes
- no additional note

## python-docstrings
### Presence
- skills/: yes
- .github/skills/: yes
- .codex/skills/: no

### File set comparison
| File | skills/ | .github/skills/ | .codex/skills/ | Status |
| --- | ---: | ---: | ---: | --- |
| SKILL.md | 1 | 1 | 0 | missing-in-one-surface |
| examples.md | 1 | 1 | 0 | missing-in-one-surface |
| reference.md | 1 | 1 | 0 | missing-in-one-surface |
| references/dataclass-patterns.md | 1 | 1 | 0 | missing-in-one-surface |
| references/error-semantics.md | 1 | 1 | 0 | missing-in-one-surface |
| references/google-style-template.md | 1 | 1 | 0 | missing-in-one-surface |
| references/semantic-intent.md | 1 | 1 | 0 | missing-in-one-surface |

### Normalized comparison result

difference_level: missing_counterpart

### Notes
- no additional note

## python-error-handling
### Presence
- skills/: yes
- .github/skills/: yes
- .codex/skills/: no

### File set comparison
| File | skills/ | .github/skills/ | .codex/skills/ | Status |
| --- | ---: | ---: | ---: | --- |
| SKILL.md | 1 | 1 | 0 | missing-in-one-surface |
| examples.md | 1 | 1 | 0 | missing-in-one-surface |

### Normalized comparison result

difference_level: missing_counterpart

### Notes
- no additional note

## python-generators-iterators
### Presence
- skills/: yes
- .github/skills/: yes
- .codex/skills/: no

### File set comparison
| File | skills/ | .github/skills/ | .codex/skills/ | Status |
| --- | ---: | ---: | ---: | --- |
| SKILL.md | 1 | 1 | 0 | missing-in-one-surface |
| examples.md | 1 | 1 | 0 | missing-in-one-surface |
| reference.md | 1 | 1 | 0 | missing-in-one-surface |

### Normalized comparison result

difference_level: missing_counterpart

### Notes
- no additional note

## python-implementation-review
### Presence
- skills/: yes
- .github/skills/: yes
- .codex/skills/: no

### File set comparison
| File | skills/ | .github/skills/ | .codex/skills/ | Status |
| --- | ---: | ---: | ---: | --- |
| SKILL.md | 1 | 1 | 0 | missing-in-one-surface |
| examples.md | 1 | 1 | 0 | missing-in-one-surface |
| reference.md | 1 | 1 | 0 | missing-in-one-surface |
| references/contract-deviation-rules.md | 1 | 1 | 0 | missing-in-one-surface |
| references/plan-section-structure.md | 1 | 1 | 0 | missing-in-one-surface |
| references/semantic-boundaries.md | 1 | 1 | 0 | missing-in-one-surface |
| references/traceability-status.md | 1 | 1 | 0 | missing-in-one-surface |

### Normalized comparison result

difference_level: missing_counterpart

### Notes
- no additional note

## python-library-architecture
### Presence
- skills/: yes
- .github/skills/: yes
- .codex/skills/: no

### File set comparison
| File | skills/ | .github/skills/ | .codex/skills/ | Status |
| --- | ---: | ---: | ---: | --- |
| SKILL.md | 1 | 1 | 0 | missing-in-one-surface |
| examples.md | 1 | 1 | 0 | missing-in-one-surface |
| reference.md | 0 | 1 | 0 | single-surface-only |

### Normalized comparison result

difference_level: semantic_diff

### Notes
- github surface adds reference.md and broader validation wording

## python-model-selection
### Presence
- skills/: yes
- .github/skills/: yes
- .codex/skills/: no

### File set comparison
| File | skills/ | .github/skills/ | .codex/skills/ | Status |
| --- | ---: | ---: | ---: | --- |
| SKILL.md | 1 | 1 | 0 | missing-in-one-surface |
| examples.md | 1 | 1 | 0 | missing-in-one-surface |

### Normalized comparison result

difference_level: missing_counterpart

### Notes
- no additional note

## python-module-boundaries
### Presence
- skills/: yes
- .github/skills/: yes
- .codex/skills/: no

### File set comparison
| File | skills/ | .github/skills/ | .codex/skills/ | Status |
| --- | ---: | ---: | ---: | --- |
| SKILL.md | 1 | 1 | 0 | missing-in-one-surface |
| examples.md | 1 | 1 | 0 | missing-in-one-surface |

### Normalized comparison result

difference_level: missing_counterpart

### Notes
- no additional note

## python-naming
### Presence
- skills/: yes
- .github/skills/: yes
- .codex/skills/: no

### File set comparison
| File | skills/ | .github/skills/ | .codex/skills/ | Status |
| --- | ---: | ---: | ---: | --- |
| SKILL.md | 1 | 1 | 0 | missing-in-one-surface |
| reference.md | 1 | 1 | 0 | missing-in-one-surface |

### Normalized comparison result

difference_level: missing_counterpart

### Notes
- no additional note

## python-operator-overloading
### Presence
- skills/: yes
- .github/skills/: yes
- .codex/skills/: no

### File set comparison
| File | skills/ | .github/skills/ | .codex/skills/ | Status |
| --- | ---: | ---: | ---: | --- |
| SKILL.md | 1 | 1 | 0 | missing-in-one-surface |
| examples.md | 1 | 1 | 0 | missing-in-one-surface |
| reference.md | 1 | 1 | 0 | missing-in-one-surface |
| references/binary-operators.md | 1 | 1 | 0 | missing-in-one-surface |
| references/comparison-and-ordering.md | 1 | 1 | 0 | missing-in-one-surface |
| references/in-place-and-unary-operators.md | 1 | 1 | 0 | missing-in-one-surface |

### Normalized comparison result

difference_level: missing_counterpart

### Notes
- no additional note

## python-package-layout
### Presence
- skills/: yes
- .github/skills/: yes
- .codex/skills/: no

### File set comparison
| File | skills/ | .github/skills/ | .codex/skills/ | Status |
| --- | ---: | ---: | ---: | --- |
| SKILL.md | 1 | 1 | 0 | missing-in-one-surface |
| examples.md | 1 | 1 | 0 | missing-in-one-surface |
| reference.md | 0 | 1 | 0 | single-surface-only |

### Normalized comparison result

difference_level: semantic_diff

### Notes
- github surface adds reference.md and broader routing wording

## python-plan-authoring
### Presence
- skills/: yes
- .github/skills/: yes
- .codex/skills/: no

### File set comparison
| File | skills/ | .github/skills/ | .codex/skills/ | Status |
| --- | ---: | ---: | ---: | --- |
| SKILL.md | 1 | 1 | 0 | missing-in-one-surface |
| examples.md | 1 | 1 | 0 | missing-in-one-surface |
| templates/python-plan-template.md | 0 | 1 | 0 | single-surface-only |
| templates/spec-template.md | 0 | 1 | 0 | single-surface-only |
| templates/step-template.md | 0 | 1 | 0 | single-surface-only |

### Normalized comparison result

difference_level: behavior_diff

### Notes
- github surface adds templates and expanded plan contract

## python-plan-review
### Presence
- skills/: yes
- .github/skills/: yes
- .codex/skills/: no

### File set comparison
| File | skills/ | .github/skills/ | .codex/skills/ | Status |
| --- | ---: | ---: | ---: | --- |
| SKILL.md | 1 | 1 | 0 | missing-in-one-surface |
| checklist.md | 1 | 1 | 0 | missing-in-one-surface |
| examples.md | 1 | 1 | 0 | missing-in-one-surface |

### Normalized comparison result

difference_level: missing_counterpart

### Notes
- no additional note

## python-pre-commit
### Presence
- skills/: yes
- .github/skills/: yes
- .codex/skills/: no

### File set comparison
| File | skills/ | .github/skills/ | .codex/skills/ | Status |
| --- | ---: | ---: | ---: | --- |
| SKILL.md | 1 | 1 | 0 | missing-in-one-surface |
| examples.md | 1 | 1 | 0 | missing-in-one-surface |
| reference.md | 0 | 1 | 0 | single-surface-only |
| references/hooks-catalog.md | 0 | 1 | 0 | single-surface-only |
| references/stage-matrix.md | 0 | 1 | 0 | single-surface-only |
| references/uv-run-format.md | 0 | 1 | 0 | single-surface-only |
| references/version-pinning.md | 0 | 1 | 0 | single-surface-only |
| scripts/apply_precommit.py | 0 | 1 | 0 | single-surface-only |
| templates/pre-commit-config.yaml | 0 | 1 | 0 | single-surface-only |
| tests/test_apply_precommit.py | 0 | 1 | 0 | single-surface-only |

### Normalized comparison result

difference_level: behavior_diff

### Notes
- github surface adds script, templates, references, and tests

## python-project-init-greenfield
### Presence
- skills/: yes
- .github/skills/: yes
- .codex/skills/: no

### File set comparison
| File | skills/ | .github/skills/ | .codex/skills/ | Status |
| --- | ---: | ---: | ---: | --- |
| SKILL.md | 1 | 1 | 0 | missing-in-one-surface |
| examples.md | 1 | 1 | 0 | missing-in-one-surface |
| references/baseline-generation-rules.md | 1 | 1 | 0 | missing-in-one-surface |
| references/blueprint-parsing-contract.md | 1 | 1 | 0 | missing-in-one-surface |

### Normalized comparison result

difference_level: missing_counterpart

### Notes
- `skills/` and `.github/skills/` are directory-identical in this worktree; only the `.codex/skills/` counterpart is missing

## python-project-retrofit
### Presence
- skills/: yes
- .github/skills/: yes
- .codex/skills/: no

### File set comparison
| File | skills/ | .github/skills/ | .codex/skills/ | Status |
| --- | ---: | ---: | ---: | --- |
| SKILL.md | 1 | 1 | 0 | missing-in-one-surface |
| examples.md | 1 | 1 | 0 | missing-in-one-surface |
| references/retrofit-conflict-resolution.md | 1 | 1 | 0 | missing-in-one-surface |
| references/retrofit-plan-v2-contract.md | 1 | 1 | 0 | missing-in-one-surface |
| references/retrofit-safety-guidelines.md | 1 | 1 | 0 | missing-in-one-surface |
| references/sensing-delta-contract.md | 1 | 1 | 0 | missing-in-one-surface |

### Normalized comparison result

difference_level: missing_counterpart

### Notes
- `skills/` and `.github/skills/` are directory-identical in this worktree; only the `.codex/skills/` counterpart is missing

## python-pyproject-toolconfig
### Presence
- skills/: yes
- .github/skills/: yes
- .codex/skills/: no

### File set comparison
| File | skills/ | .github/skills/ | .codex/skills/ | Status |
| --- | ---: | ---: | ---: | --- |
| SKILL.md | 1 | 1 | 0 | missing-in-one-surface |
| examples.md | 1 | 1 | 0 | missing-in-one-surface |
| reference.md | 0 | 1 | 0 | single-surface-only |
| scripts/apply_toolconfig.py | 0 | 1 | 0 | single-surface-only |
| templates/toolconfig-pyright.toml.tmpl | 0 | 1 | 0 | single-surface-only |
| templates/toolconfig-pytest.toml.tmpl | 0 | 1 | 0 | single-surface-only |
| templates/toolconfig-ruff.toml.tmpl | 0 | 1 | 0 | single-surface-only |
| tests/test_existing_preserved.py | 0 | 1 | 0 | single-surface-only |
| tests/test_idempotent.py | 0 | 1 | 0 | single-surface-only |
| tests/test_input_validation.py | 0 | 1 | 0 | single-surface-only |
| tests/test_section_detection.py | 0 | 1 | 0 | single-surface-only |
| tests/test_substitution.py | 0 | 1 | 0 | single-surface-only |

### Normalized comparison result

difference_level: behavior_diff

### Notes
- github surface adds script, templates, references, and tests

## python-retrofit-plan-authoring
### Presence
- skills/: yes
- .github/skills/: yes
- .codex/skills/: no

### File set comparison
| File | skills/ | .github/skills/ | .codex/skills/ | Status |
| --- | ---: | ---: | ---: | --- |
| SKILL.md | 1 | 1 | 0 | missing-in-one-surface |
| checklist.md | 1 | 1 | 0 | missing-in-one-surface |
| examples.md | 1 | 1 | 0 | missing-in-one-surface |
| references/authoring-vs-executor-boundaries.md | 1 | 1 | 0 | missing-in-one-surface |
| references/migration-strategy-risk-model.md | 1 | 1 | 0 | missing-in-one-surface |
| references/retrofit-v2-contract.md | 1 | 1 | 0 | missing-in-one-surface |

### Normalized comparison result

difference_level: missing_counterpart

### Notes
- no additional note

## python-retrofit-plan-review
### Presence
- skills/: yes
- .github/skills/: yes
- .codex/skills/: no

### File set comparison
| File | skills/ | .github/skills/ | .codex/skills/ | Status |
| --- | ---: | ---: | ---: | --- |
| SKILL.md | 1 | 1 | 0 | missing-in-one-surface |
| checklist.md | 1 | 1 | 0 | missing-in-one-surface |
| examples.md | 1 | 1 | 0 | missing-in-one-surface |
| references/lane-fit-and-reroute.md | 1 | 1 | 0 | missing-in-one-surface |
| references/retrofit-v2-review-checks.md | 1 | 1 | 0 | missing-in-one-surface |
| references/review-verdict-contract.md | 1 | 1 | 0 | missing-in-one-surface |
| references/risk-boundary-and-locatability-checks.md | 1 | 1 | 0 | missing-in-one-surface |

### Normalized comparison result

difference_level: missing_counterpart

### Notes
- no additional note

## python-serialization-boundaries
### Presence
- skills/: yes
- .github/skills/: yes
- .codex/skills/: no

### File set comparison
| File | skills/ | .github/skills/ | .codex/skills/ | Status |
| --- | ---: | ---: | ---: | --- |
| REVIEW.md | 1 | 1 | 0 | missing-in-one-surface |
| SKILL.md | 1 | 1 | 0 | missing-in-one-surface |
| examples.md | 1 | 1 | 0 | missing-in-one-surface |
| reference.md | 1 | 1 | 0 | missing-in-one-surface |

### Normalized comparison result

difference_level: text_diff_only

### Notes
- only REVIEW.md differs

## python-tdd-test-authoring
### Presence
- skills/: yes
- .github/skills/: yes
- .codex/skills/: no

### File set comparison
| File | skills/ | .github/skills/ | .codex/skills/ | Status |
| --- | ---: | ---: | ---: | --- |
| SKILL.md | 1 | 1 | 0 | missing-in-one-surface |
| checklist.md | 0 | 1 | 0 | single-surface-only |
| examples.md | 1 | 1 | 0 | missing-in-one-surface |
| references/atomic-commit-order.md | 0 | 1 | 0 | single-surface-only |
| references/behavior-change-classifier.md | 0 | 1 | 0 | single-surface-only |
| references/codebase-evidence-levels.md | 0 | 1 | 0 | single-surface-only |

### Normalized comparison result

difference_level: behavior_diff

### Notes
- github surface adds checklist and verdict-oriented references

## python-testing-pytest
### Presence
- skills/: yes
- .github/skills/: yes
- .codex/skills/: no

### File set comparison
| File | skills/ | .github/skills/ | .codex/skills/ | Status |
| --- | ---: | ---: | ---: | --- |
| SKILL.md | 1 | 1 | 0 | missing-in-one-surface |
| examples.md | 1 | 1 | 0 | missing-in-one-surface |

### Normalized comparison result

difference_level: missing_counterpart

### Notes
- no additional note

## python-type-hints-strict
### Presence
- skills/: yes
- .github/skills/: yes
- .codex/skills/: no

### File set comparison
| File | skills/ | .github/skills/ | .codex/skills/ | Status |
| --- | ---: | ---: | ---: | --- |
| SKILL.md | 1 | 1 | 0 | missing-in-one-surface |
| examples.md | 1 | 1 | 0 | missing-in-one-surface |
| reference.md | 1 | 1 | 0 | missing-in-one-surface |

### Normalized comparison result

difference_level: missing_counterpart

### Notes
- no additional note

## sense-env-scaffold
### Presence
- skills/: yes
- .github/skills/: yes
- .codex/skills/: no

### File set comparison
| File | skills/ | .github/skills/ | .codex/skills/ | Status |
| --- | ---: | ---: | ---: | --- |
| SKILL.md | 1 | 1 | 0 | missing-in-one-surface |
| examples.md | 1 | 1 | 0 | missing-in-one-surface |
| references/env-manifest-schema.md | 1 | 1 | 0 | missing-in-one-surface |
| references/sense-env-cli-contract.md | 1 | 1 | 0 | missing-in-one-surface |
| scripts/sense_env.py | 1 | 1 | 0 | missing-in-one-surface |
| scripts/sense_env_runtime/__init__.py | 1 | 1 | 0 | missing-in-one-surface |
| scripts/sense_env_runtime/contract.py | 1 | 1 | 0 | missing-in-one-surface |
| scripts/sense_env_runtime/models.py | 1 | 1 | 0 | missing-in-one-surface |
| scripts/sense_env_runtime/runtime.py | 1 | 1 | 0 | missing-in-one-surface |

### Normalized comparison result

difference_level: behavior_diff

### Notes
- runtime assertion handling differs in script implementation

## worktree-manager
### Presence
- skills/: yes
- .github/skills/: yes
- .codex/skills/: yes

### File set comparison
| File | skills/ | .github/skills/ | .codex/skills/ | Status |
| --- | ---: | ---: | ---: | --- |
| SKILL.md | 1 | 1 | 1 | all-present |
| checklist.md | 1 | 1 | 1 | all-present |
| examples.md | 1 | 1 | 1 | all-present |
| reference.md | 1 | 1 | 1 | all-present |

### Normalized comparison result

difference_level: identical

### Notes
- matches `.github/skills/` projection
