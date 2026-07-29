# `.codex/skills` Provenance

This file records the current `.codex/skills` projection provenance for the
whole canonical `skills/` library.

Current implementation note:

- `source_commit` records the upstream canonical commit that was validated
- `materialized-copy` rows are direct projections from `skills/<skill-name>/`
  with `.codex/...` concretization applied where needed
- `materialized-copy+canonical-runtime-exception` indicates the projected copy
  keeps one file byte-identical to canonical after materialization

## Current provenance

| skill_name | upstream_path | materialization_mode | source_commit | validation_basis |
| --- | --- | --- | --- | --- |
| `agent-skill-creator` | `skills/agent-skill-creator/` | `materialized-copy` | `8ce10c2` | `materialized from canonical source by platform-projection-adapter; .codex/skills/... concretized` |
| `agent-skill-reviewer` | `skills/agent-skill-reviewer/` | `materialized-copy` | `8ce10c2` | `materialized from canonical source by platform-projection-adapter; .codex/skills/... concretized` |
| `agent-skill-template` | `skills/agent-skill-template/` | `materialized-copy` | `8ce10c2` | `materialized from canonical source by platform-projection-adapter; .codex/skills/... concretized` |
| `business-intent-alignment` | `skills/business-intent-alignment/` | `materialized-copy` | `8ce10c2` | `materialized from canonical source by platform-projection-adapter; .codex/skills/... concretized` |
| `business-to-technical-translation` | `skills/business-to-technical-translation/` | `materialized-copy` | `8ce10c2` | `materialized from canonical source by platform-projection-adapter; .codex/skills/... concretized` |
| `context-package-builder` | `skills/context-package-builder/` | `materialized-copy` | `8ce10c2` | `materialized from canonical source by platform-projection-adapter; .codex/skills/... concretized` |
| `copilot-instructions-init` | `skills/copilot-instructions-init/` | `materialized-copy` | `8ce10c2` | `materialized from canonical source by platform-projection-adapter; .codex/skills/... concretized` |
| `git-branch-naming` | `skills/git-branch-naming/` | `materialized-copy` | `86184c9` | `materialized from canonical source by platform-projection-adapter; .codex/skills/... concretized; revalidated against canonical hygiene baseline at 86184c9` |
| `git-commit-convention` | `skills/git-commit-convention/` | `materialized-copy` | `86184c9` | `materialized from canonical source by platform-projection-adapter; .codex/skills/... concretized; revalidated against canonical hygiene baseline at 86184c9` |
| `git-post-merge-workflow` | `skills/git-post-merge-workflow/` | `materialized-copy` | `8ce10c2` | `materialized from canonical source by platform-projection-adapter; .codex/skills/... concretized` |
| `git-release-management` | `skills/git-release-management/` | `materialized-copy` | `8ce10c2` | `materialized from canonical source by platform-projection-adapter; .codex/skills/... concretized` |
| `handoff-routing-policy` | `skills/handoff-routing-policy/` | `materialized-copy` | `8ce10c2` | `materialized from canonical source by platform-projection-adapter; .codex/skills/... concretized` |
| `plan-creator` | `skills/plan-creator/` | `materialized-copy` | `8ce10c2` | `materialized from canonical source by platform-projection-adapter; .codex/skills/... concretized` |
| `plan-reviewer` | `skills/plan-reviewer/` | `materialized-copy` | `8ce10c2` | `materialized from canonical source by platform-projection-adapter; .codex/skills/... concretized` |
| `plan-step-tracker` | `skills/plan-step-tracker/` | `materialized-copy` | `86184c9` | `materialized from canonical source by platform-projection-adapter; .codex/skills/... concretized; revalidated against canonical hygiene baseline at 86184c9` |
| `platform-projection-adapter` | `skills/platform-projection-adapter/` | `materialized-copy+canonical-runtime-exception` | `8ce10c2` | `materialized from canonical source; projected docs concretized to .codex/skills/...; scripts/platform_projection_adapter.py preserved byte-identical to canonical runtime` |
| `python-api-signature` | `skills/python-api-signature/` | `materialized-copy` | `8ce10c2` | `materialized from canonical source by platform-projection-adapter; .codex/skills/... concretized` |
| `python-async-await` | `skills/python-async-await/` | `materialized-copy` | `8ce10c2` | `materialized from canonical source by platform-projection-adapter; .codex/skills/... concretized` |
| `python-async-planning` | `skills/python-async-planning/` | `materialized-copy` | `8ce10c2` | `materialized from canonical source by platform-projection-adapter; .codex/skills/... concretized` |
| `python-blueprint-authoring` | `skills/python-blueprint-authoring/` | `materialized-copy` | `8ce10c2` | `materialized from canonical source by platform-projection-adapter; .codex/skills/... concretized` |
| `python-blueprint-review` | `skills/python-blueprint-review/` | `materialized-copy` | `8ce10c2` | `materialized from canonical source by platform-projection-adapter; .codex/skills/... concretized` |
| `python-class-design` | `skills/python-class-design/` | `materialized-copy` | `8ce10c2` | `materialized from canonical source by platform-projection-adapter; .codex/skills/... concretized` |
| `python-code-review` | `skills/python-code-review/` | `materialized-copy` | `8ce10c2` | `materialized from canonical source by platform-projection-adapter; .codex/skills/... concretized` |
| `python-comprehensions` | `skills/python-comprehensions/` | `materialized-copy` | `8ce10c2` | `materialized from canonical source by platform-projection-adapter; .codex/skills/... concretized` |
| `python-context-management` | `skills/python-context-management/` | `materialized-copy` | `8ce10c2` | `materialized from canonical source by platform-projection-adapter; .codex/skills/... concretized` |
| `python-control-flow` | `skills/python-control-flow/` | `materialized-copy` | `8ce10c2` | `materialized from canonical source by platform-projection-adapter; .codex/skills/... concretized` |
| `python-data-model-methods` | `skills/python-data-model-methods/` | `materialized-copy` | `8ce10c2` | `materialized from canonical source by platform-projection-adapter; .codex/skills/... concretized` |
| `python-decorators` | `skills/python-decorators/` | `materialized-copy` | `8ce10c2` | `materialized from canonical source by platform-projection-adapter; .codex/skills/... concretized` |
| `python-descriptors-attribute-access` | `skills/python-descriptors-attribute-access/` | `materialized-copy` | `8ce10c2` | `materialized from canonical source by platform-projection-adapter; .codex/skills/... concretized` |
| `python-docstrings` | `skills/python-docstrings/` | `materialized-copy` | `86184c9` | `materialized from canonical source by platform-projection-adapter; .codex/skills/... concretized; revalidated against canonical hygiene baseline at 86184c9` |
| `python-error-handling` | `skills/python-error-handling/` | `materialized-copy` | `8ce10c2` | `materialized from canonical source by platform-projection-adapter; .codex/skills/... concretized` |
| `python-generators-iterators` | `skills/python-generators-iterators/` | `materialized-copy` | `86184c9` | `materialized from canonical source by platform-projection-adapter; .codex/skills/... concretized; revalidated against canonical hygiene baseline at 86184c9` |
| `python-implementation-review` | `skills/python-implementation-review/` | `materialized-copy` | `8ce10c2` | `materialized from canonical source by platform-projection-adapter; .codex/skills/... concretized` |
| `python-library-architecture` | `skills/python-library-architecture/` | `materialized-copy` | `8ce10c2` | `materialized from canonical source by platform-projection-adapter; .codex/skills/... concretized` |
| `python-model-selection` | `skills/python-model-selection/` | `materialized-copy` | `8ce10c2` | `materialized from canonical source by platform-projection-adapter; .codex/skills/... concretized` |
| `python-module-boundaries` | `skills/python-module-boundaries/` | `materialized-copy` | `8ce10c2` | `materialized from canonical source by platform-projection-adapter; .codex/skills/... concretized` |
| `python-naming` | `skills/python-naming/` | `materialized-copy` | `8ce10c2` | `materialized from canonical source by platform-projection-adapter; .codex/skills/... concretized` |
| `python-operator-overloading` | `skills/python-operator-overloading/` | `materialized-copy` | `8ce10c2` | `materialized from canonical source by platform-projection-adapter; .codex/skills/... concretized` |
| `python-package-layout` | `skills/python-package-layout/` | `materialized-copy` | `8ce10c2` | `materialized from canonical source by platform-projection-adapter; .codex/skills/... concretized` |
| `python-plan-authoring` | `skills/python-plan-authoring/` | `materialized-copy` | `86184c9` | `materialized from canonical source by platform-projection-adapter; .codex/skills/... concretized; revalidated against canonical hygiene baseline at 86184c9` |
| `python-plan-review` | `skills/python-plan-review/` | `materialized-copy` | `8ce10c2` | `materialized from canonical source by platform-projection-adapter; .codex/skills/... concretized` |
| `python-pre-commit` | `skills/python-pre-commit/` | `materialized-copy` | `86184c9` | `materialized from canonical source by platform-projection-adapter; .codex/skills/... concretized; revalidated against canonical hygiene baseline at 86184c9` |
| `python-project-init-greenfield` | `skills/python-project-init-greenfield/` | `materialized-copy` | `8ce10c2` | `materialized from canonical source by platform-projection-adapter; .codex/skills/... concretized` |
| `python-project-retrofit` | `skills/python-project-retrofit/` | `materialized-copy` | `8ce10c2` | `materialized from canonical source by platform-projection-adapter; .codex/skills/... concretized` |
| `python-pyproject-toolconfig` | `skills/python-pyproject-toolconfig/` | `materialized-copy` | `8ce10c2` | `materialized from canonical source by platform-projection-adapter; .codex/skills/... concretized` |
| `python-retrofit-plan-authoring` | `skills/python-retrofit-plan-authoring/` | `materialized-copy` | `8ce10c2` | `materialized from canonical source by platform-projection-adapter; .codex/skills/... concretized` |
| `python-retrofit-plan-review` | `skills/python-retrofit-plan-review/` | `materialized-copy` | `8ce10c2` | `materialized from canonical source by platform-projection-adapter; .codex/skills/... concretized` |
| `python-serialization-boundaries` | `skills/python-serialization-boundaries/` | `materialized-copy` | `8ce10c2` | `materialized from canonical source by platform-projection-adapter; .codex/skills/... concretized` |
| `python-tdd-test-authoring` | `skills/python-tdd-test-authoring/` | `materialized-copy` | `86184c9` | `materialized from canonical source by platform-projection-adapter; .codex/skills/... concretized; revalidated against canonical hygiene baseline at 86184c9` |
| `python-testing-pytest` | `skills/python-testing-pytest/` | `materialized-copy` | `8ce10c2` | `materialized from canonical source by platform-projection-adapter; .codex/skills/... concretized` |
| `python-type-hints-strict` | `skills/python-type-hints-strict/` | `materialized-copy` | `8ce10c2` | `materialized from canonical source by platform-projection-adapter; .codex/skills/... concretized` |
| `sense-env-scaffold` | `skills/sense-env-scaffold/` | `materialized-copy` | `8ce10c2` | `materialized from canonical source by platform-projection-adapter; .codex/skills/... concretized` |
| `scope-draft-plan` | `skills/scope-draft-plan/` | `materialized-copy` | `c45ffb8` | `direct materialization from canonical source; no .<platform>/ placeholders to concretize` |
| `step-creator` | `skills/step-creator/` | `materialized-copy` | `2379e45` | `byte-identical materialization from canonical source; no .<platform>/ placeholders to concretize` |
| `subagent-dispatch-policy` | `skills/subagent-dispatch-policy/` | `materialized-copy` | `8ce10c2` | `materialized from canonical source by platform-projection-adapter; .codex/skills/... concretized` |
| `worktree-manager` | `skills/worktree-manager/` | `materialized-copy` | `8ce10c2` | `materialized from canonical source by platform-projection-adapter; .codex/skills/... concretized` |

## Revalidation rule

When an upstream source changes:

1. verify the entry's `materialization_mode`
2. rematerialize the `.codex` surface from canonical `skills/<skill-name>/`
3. restore the canonical runtime exception for
   `platform-projection-adapter/scripts/platform_projection_adapter.py` when needed
4. confirm `.codex/skills/README.md` still matches the actual surface
5. update the affected row in this file with the revalidated `source_commit`
   and `validation_basis`

If the source mapping cannot be verified, treat the projected surface as stale
and do not use it as validation evidence.
