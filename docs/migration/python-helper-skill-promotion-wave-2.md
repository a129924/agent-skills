# python-helper-skill-promotion-wave-2

## Wave boundary

This migration wave is locked to exactly these 18 Python helper skills:

1. `python-api-signature`
2. `python-async-await`
3. `python-class-design`
4. `python-comprehensions`
5. `python-context-management`
6. `python-control-flow`
7. `python-data-model-methods`
8. `python-decorators`
9. `python-descriptors-attribute-access`
10. `python-docstrings`
11. `python-error-handling`
12. `python-generators-iterators`
13. `python-model-selection`
14. `python-module-boundaries`
15. `python-naming`
16. `python-operator-overloading`
17. `python-testing-pytest`
18. `python-type-hints-strict`

No additional skill is promoted by this wave.

## Transition boundary

- `.github/skills/` remains the current active authored/reviewed workflow path during transition.
- `skills/` is the target-architecture promotion result for this wave only.
- This wave does not authorize repo-wide active-path cutover.

## Source-authority rule

Source authority for this wave is one-way and bounded:

- `.github/skills/<skill-name>/` remains the preserved transition-era source input.
- `skills/<skill-name>/` is the copied target-architecture promotion result for the selected skill.
- This wave does not declare `.github/skills/` and `skills/` to be dual canonical sources.

## Promotion results

| Skill | Result | Source path | Target path | Notes |
| --- | --- | --- | --- | --- |
| `python-api-signature` | `copied` | `.github/skills/python-api-signature/` | `skills/python-api-signature/` | Folder-level direct copy completed; source preserved unchanged |
| `python-async-await` | `copied` | `.github/skills/python-async-await/` | `skills/python-async-await/` | Folder-level direct copy completed; source preserved unchanged |
| `python-class-design` | `copied` | `.github/skills/python-class-design/` | `skills/python-class-design/` | Folder-level direct copy completed; source preserved unchanged |
| `python-comprehensions` | `copied` | `.github/skills/python-comprehensions/` | `skills/python-comprehensions/` | Folder-level direct copy completed; source preserved unchanged |
| `python-context-management` | `copied` | `.github/skills/python-context-management/` | `skills/python-context-management/` | Folder-level direct copy completed; source preserved unchanged |
| `python-control-flow` | `copied` | `.github/skills/python-control-flow/` | `skills/python-control-flow/` | Folder-level direct copy completed; source preserved unchanged |
| `python-data-model-methods` | `copied` | `.github/skills/python-data-model-methods/` | `skills/python-data-model-methods/` | Folder-level direct copy completed; source preserved unchanged |
| `python-decorators` | `copied` | `.github/skills/python-decorators/` | `skills/python-decorators/` | Folder-level direct copy completed; source preserved unchanged |
| `python-descriptors-attribute-access` | `copied` | `.github/skills/python-descriptors-attribute-access/` | `skills/python-descriptors-attribute-access/` | Folder-level direct copy completed; source preserved unchanged |
| `python-docstrings` | `copied` | `.github/skills/python-docstrings/` | `skills/python-docstrings/` | Folder-level direct copy completed; source preserved unchanged |
| `python-error-handling` | `copied` | `.github/skills/python-error-handling/` | `skills/python-error-handling/` | Folder-level direct copy completed; source preserved unchanged |
| `python-generators-iterators` | `copied` | `.github/skills/python-generators-iterators/` | `skills/python-generators-iterators/` | Folder-level direct copy completed; source preserved unchanged |
| `python-model-selection` | `copied` | `.github/skills/python-model-selection/` | `skills/python-model-selection/` | Folder-level direct copy completed; source preserved unchanged |
| `python-module-boundaries` | `copied` | `.github/skills/python-module-boundaries/` | `skills/python-module-boundaries/` | Folder-level direct copy completed; source preserved unchanged |
| `python-naming` | `copied` | `.github/skills/python-naming/` | `skills/python-naming/` | Folder-level direct copy completed; source preserved unchanged |
| `python-operator-overloading` | `copied` | `.github/skills/python-operator-overloading/` | `skills/python-operator-overloading/` | Folder-level direct copy completed; source preserved unchanged |
| `python-testing-pytest` | `copied` | `.github/skills/python-testing-pytest/` | `skills/python-testing-pytest/` | Folder-level direct copy completed; source preserved unchanged |
| `python-type-hints-strict` | `copied` | `.github/skills/python-type-hints-strict/` | `skills/python-type-hints-strict/` | Folder-level direct copy completed; source preserved unchanged |

## Deferred follow-up lanes

- Any repo-wide active-path cutover from `.github/skills/` to `skills/`
- Any migration of `agent-skill-creator`, `agent-skill-reviewer`, or `agent-skill-template`
- Any runtime/tooling blocker repair or path-retargeting
- Any installer, projection, or platform-adapter switching work
- Any governance, positioning, README, VERSION, or release-surface updates
