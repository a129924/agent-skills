# Risk, Boundary, and Locatability Checks

Use this reference when reviewing whether an authored Retrofit V2 contract is
safe to hand off to `python-project-retrofit`.

## Risk-alignment review rule

Review the written target state, strategy prose, and `yaml [migration-strategy]`
block as one contract.

Current execution-facing expectations:
- `LOW` means additive or non-destructive work only
- `HIGH` means destructive work is explicit and reviewable
- `LOW` normally pairs with `destructive_actions: []` and `backup_required: false`
- `HIGH` normally pairs with concrete `destructive_actions` and `backup_required: true`

Return `needs-rework` when:
- the contract says `LOW` but the written work implies move, delete, overwrite, directory relocation, entrypoint replacement, or core-toolchain replacement
- the plan describes destructive work but `destructive_actions` is empty or too partial to represent that scope
- `backup_required` conflicts with the destructive reality described in the plan
- the reviewer would need to infer destructive steps that the contract did not declare concretely

## Destructive-scope signals

Treat these as destructive signals that must align with the risk metadata:
- moving files or directories so the source path disappears
- deleting legacy files, directories, or environments
- overwriting config files such as `pyproject.toml`, `setup.cfg`, or `requirements.txt`
- replacing entrypoints or package roots
- collapsing multiple config surfaces into one survivor file
- reshaping a repository into `src/` layout from a materially different current structure

## Authoring-versus-executor boundary

Planning text may describe intent, but it must not pre-decide runtime answers
owned by `python-project-retrofit`.

Review should fail when the plan treats strategy prose as if it already grants:
- `move`, `delete`, `coexist`, or `abort` answers for shadow conflicts
- `migrate`, `delete`, `preserve`, or `abort` answers for config-remnant handling
- destructive authorization that should still require executor-time human approval
- conflict-resolution outcomes that depend on runtime scans

Allowed planning language:
- “staged package relocation with compatibility shim retained during transition”
- “target state replaces legacy config with one governed surface”

Blocking boundary language:
- “delete the old root script automatically”
- “overwrite setup.cfg if conflicts appear”
- “runtime should preserve both paths by default”

## Locatability rule

The contract must be concrete enough for executor handoff without guesswork.

At minimum, review should expect:
- real current-state paths when the survey summary claims live surfaces exist
- real target paths
- real entrypoint file paths when execution depends on them
- real config filenames or surfaces when toolchain change is part of the plan
- real tool names when the target state depends on them
- mutually consistent locators across sections

### Acceptable

```markdown
## Survey Summary
- current entrypoint: app.py
- current config: requirements.txt

## Target Transformation
- target package: src/weather_service/
- target entrypoint: src/weather_service/main.py
- target config: pyproject.toml
```

### Blocking

```markdown
## Survey Summary
- current layout: legacy app

## Target Transformation
- modernize the layout
- clean up old files
- switch to a better toolchain
```

These blocking examples fail because the reviewer would have to invent the real
paths, files, and tools.

## Contradiction checks

Return `needs-rework` when locators disagree, for example:

```text
- current entrypoint: app.py
- retain entrypoint: src/weather_service/main.py
```

```text
- target package: src/weather_service/
- target config: keep requirements.txt only
- destructive_actions:
  - replace requirements.txt with pyproject.toml
```

The review should not guess which statement is authoritative.

## Review response pattern

When these checks fail:
1. identify the exact risk mismatch, boundary violation, or non-locatable item
2. explain why safe executor handoff is blocked
3. return `needs-rework`
4. describe the required contract repair without rewriting the plan inline
