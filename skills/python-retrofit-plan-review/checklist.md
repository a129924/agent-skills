# Python Retrofit Plan Review Checklist

Use this checklist before returning a verdict for an authored Retrofit V2
`retrofit-plan.md`.

- [ ] The task is really Retrofit V2 contract review, not authoring, execution, greenfield blueprint review, skill-folder review, topic-plan review, or implementation-diff review.
- [ ] The review stays inside the existing Retrofit V2 contract already consumed by `python-project-retrofit`.
- [ ] The section order is exactly:
  - [ ] `## Survey Summary`
  - [ ] `## Gap Analysis`
  - [ ] `## Target Transformation`
  - [ ] `## Migration Strategy`
  - [ ] `## Acceptance Criteria`
- [ ] No required heading is missing, reordered, renamed, mixed with old headings, or replaced by a compatibility alias.
- [ ] `## Migration Strategy` contains a parseable fenced `yaml [migration-strategy]` block.
- [ ] `risk_level` is present and is only `LOW` or `HIGH`; unsupported values such as `MEDIUM` were treated as blocking issues.
- [ ] `destructive_actions` is present and is a YAML sequence, even when empty.
- [ ] `backup_required` is present and is the YAML boolean `true` or `false`.
- [ ] `## Acceptance Criteria` contains a parseable fenced `yaml [sensing-assertions]` block.
- [ ] Every sensing assertion includes `kind`, `target`, and `expected`.
- [ ] Every sensing assertion `kind` is one of: `path_exists`, `path_type`, `command_available`; unsupported kinds were treated as blocking issues.
- [ ] Risk-alignment contradictions were checked across `Target Transformation`, `Migration Strategy`, and surrounding prose.
- [ ] A written destructive path does not hide behind `risk_level: LOW` or an empty / partial `destructive_actions` list.
- [ ] Planning prose was not allowed to pre-authorize runtime outcomes such as `move`, `delete`, `coexist`, `migrate`, `preserve`, or destructive approval.
- [ ] Current-state facts, target paths, entrypoints, config surfaces, and tool names are concrete and locatable enough for executor handoff without guessing.
- [ ] Greenfield-shaped or otherwise wrong-lane requests were rejected or rerouted instead of absorbed.
- [ ] The verdict reports blocking issues instead of rewriting the plan on the reviewer's behalf.
- [ ] The final output is exactly one JSON object using the local verdict contract.
