# `.codex/skills` Validation Surface

This directory is a Codex-facing projection surface materialized from the
canonical `skills/` library.

It is intentionally not the repository's canonical source of truth.

Current materialization model:

- every canonical `skills/<skill-name>/` directory is projected into
  `.codex/skills/<skill-name>/`
- projected copies may concretize `.<platform>/...` references into
  `.codex/...` paths for local Codex use
- `platform-projection-adapter` is a special runtime exception:
  `.codex/skills/platform-projection-adapter/scripts/platform_projection_adapter.py`
  remains byte-identical to the canonical `skills/...` runtime instead of being
  concretized, because it is the placeholder-replacement engine itself

> **Read-only projection**: this surface is derived from canonical
> `skills/<skill-name>/` sources. Do not edit projected skill content here as if
> it were canonical. If upstream behavior changes, fix `skills/...` first and
> rematerialize `.codex/skills/...`.

## Source Rule

- use `skills/<skill-name>/` as the canonical upstream source for every entry
  listed below
- rematerialize `.codex/skills/<skill-name>/` from `skills/<skill-name>/`
  whenever the upstream canonical source changes
- apply `.codex/...` concretization only inside this projected surface
- concretize projected files under `.codex/skills/...` by default
- preserve the canonical-identical runtime exception for
  `.codex/skills/platform-projection-adapter/scripts/platform_projection_adapter.py`
  during rematerialization

## Current Mapping

| Skill entry | Upstream source | Surface mode |
| --- | --- | --- |
| `agent-skill-creator` | `skills/agent-skill-creator/` | `materialized-copy` |
| `agent-skill-reviewer` | `skills/agent-skill-reviewer/` | `materialized-copy` |
| `agent-skill-template` | `skills/agent-skill-template/` | `materialized-copy` |
| `business-intent-alignment` | `skills/business-intent-alignment/` | `materialized-copy` |
| `business-to-technical-translation` | `skills/business-to-technical-translation/` | `materialized-copy` |
| `context-package-builder` | `skills/context-package-builder/` | `materialized-copy` |
| `copilot-instructions-init` | `skills/copilot-instructions-init/` | `materialized-copy` |
| `git-branch-naming` | `skills/git-branch-naming/` | `materialized-copy` |
| `git-commit-convention` | `skills/git-commit-convention/` | `materialized-copy` |
| `git-post-merge-workflow` | `skills/git-post-merge-workflow/` | `materialized-copy` |
| `git-release-management` | `skills/git-release-management/` | `materialized-copy` |
| `handoff-routing-policy` | `skills/handoff-routing-policy/` | `materialized-copy` |
| `plan-creator` | `skills/plan-creator/` | `materialized-copy` |
| `plan-reviewer` | `skills/plan-reviewer/` | `materialized-copy` |
| `plan-step-tracker` | `skills/plan-step-tracker/` | `materialized-copy` |
| `platform-projection-adapter` | `skills/platform-projection-adapter/` | `materialized-copy+canonical-runtime-exception` |
| `python-api-signature` | `skills/python-api-signature/` | `materialized-copy` |
| `python-async-await` | `skills/python-async-await/` | `materialized-copy` |
| `python-async-planning` | `skills/python-async-planning/` | `materialized-copy` |
| `python-blueprint-authoring` | `skills/python-blueprint-authoring/` | `materialized-copy` |
| `python-blueprint-review` | `skills/python-blueprint-review/` | `materialized-copy` |
| `python-class-design` | `skills/python-class-design/` | `materialized-copy` |
| `python-code-review` | `skills/python-code-review/` | `materialized-copy` |
| `python-comprehensions` | `skills/python-comprehensions/` | `materialized-copy` |
| `python-context-management` | `skills/python-context-management/` | `materialized-copy` |
| `python-control-flow` | `skills/python-control-flow/` | `materialized-copy` |
| `python-data-model-methods` | `skills/python-data-model-methods/` | `materialized-copy` |
| `python-decorators` | `skills/python-decorators/` | `materialized-copy` |
| `python-descriptors-attribute-access` | `skills/python-descriptors-attribute-access/` | `materialized-copy` |
| `python-docstrings` | `skills/python-docstrings/` | `materialized-copy` |
| `python-error-handling` | `skills/python-error-handling/` | `materialized-copy` |
| `python-generators-iterators` | `skills/python-generators-iterators/` | `materialized-copy` |
| `python-implementation-review` | `skills/python-implementation-review/` | `materialized-copy` |
| `python-library-architecture` | `skills/python-library-architecture/` | `materialized-copy` |
| `python-model-selection` | `skills/python-model-selection/` | `materialized-copy` |
| `python-module-boundaries` | `skills/python-module-boundaries/` | `materialized-copy` |
| `python-naming` | `skills/python-naming/` | `materialized-copy` |
| `python-operator-overloading` | `skills/python-operator-overloading/` | `materialized-copy` |
| `python-package-layout` | `skills/python-package-layout/` | `materialized-copy` |
| `python-plan-authoring` | `skills/python-plan-authoring/` | `materialized-copy` |
| `python-plan-review` | `skills/python-plan-review/` | `materialized-copy` |
| `python-pre-commit` | `skills/python-pre-commit/` | `materialized-copy` |
| `python-project-init-greenfield` | `skills/python-project-init-greenfield/` | `materialized-copy` |
| `python-project-retrofit` | `skills/python-project-retrofit/` | `materialized-copy` |
| `python-pyproject-toolconfig` | `skills/python-pyproject-toolconfig/` | `materialized-copy` |
| `python-retrofit-plan-authoring` | `skills/python-retrofit-plan-authoring/` | `materialized-copy` |
| `python-retrofit-plan-review` | `skills/python-retrofit-plan-review/` | `materialized-copy` |
| `python-serialization-boundaries` | `skills/python-serialization-boundaries/` | `materialized-copy` |
| `python-tdd-test-authoring` | `skills/python-tdd-test-authoring/` | `materialized-copy` |
| `python-testing-pytest` | `skills/python-testing-pytest/` | `materialized-copy` |
| `python-type-hints-strict` | `skills/python-type-hints-strict/` | `materialized-copy` |
| `sense-env-scaffold` | `skills/sense-env-scaffold/` | `materialized-copy` |
| `subagent-dispatch-policy` | `skills/subagent-dispatch-policy/` | `materialized-copy` |
| `worktree-manager` | `skills/worktree-manager/` | `materialized-copy` |

## How to rematerialize

1. Make the canonical change in `skills/<skill-name>/`.
2. Run the canonical bootstrap CLI with `--platform-root .codex`.
3. Restore
   `.codex/skills/platform-projection-adapter/scripts/platform_projection_adapter.py`
   from the canonical `skills/...` copy if rematerialization concretized it.
4. Update `.codex/skills/provenance.md` with the revalidated source commit and
   validation basis.

## Provenance requirement

Each projected skill must be traceable to exactly one upstream source path,
one surface mode, and one last-validated source commit. Maintain
`.codex/skills/provenance.md` with at least:

- `skill_name`
- `upstream_path`
- `materialization_mode`
- `source_commit`
- `validation_basis`

If provenance cannot be established for a projected skill, treat it as stale
and revalidate it against the current upstream source before use.

## Boundary

- do not treat this directory as a third authority tree
- do not treat projected content as canonical source
- do not edit projected skill content here as if it were upstream truth
- do not concretize the `platform_projection_adapter.py` runtime exception
- if a projected skill points to the wrong upstream source, fix the mapping or
  rematerialization rule rather than editing around the mismatch
