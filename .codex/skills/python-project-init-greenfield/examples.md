# Python Project Init Greenfield Examples

Detailed examples for `python-project-init-greenfield`.

---

## Happy path: minimal governed greenfield repo

**Input blueprint**

~~~markdown
## Project Overview
- Name: Weather Service

## Required Skills
- sense-env-scaffold: Acceptance verification runner
- python-type-hints-strict: Strict typing baseline
- python-testing-pytest: Pytest testing baseline

## Toolchain Expectation
- python @ 3.12: Runtime and development baseline
- package_manager @ uv: Dependency and lock workflow
- linter @ ruff: Linting
- tester @ pytest: Test execution
- type_checker @ pyright: Strict type checking

## Structural Invariants
- package: weather_service
- path: src/weather_service
- path: tests
- entrypoint: src/weather_service/main.py

## Quality Thresholds
- coverage: >=90
- type_checking: pyright --strict passes
- lint_pass: ruff check passes
- test_pass: pytest passes

## Acceptance Criteria
```yaml [sensing-assertions]
- kind: path_exists
  target: pyproject.toml
  expected: "true"
- kind: path_exists
  target: src/weather_service/main.py
  expected: "true"
- kind: command_available
  target: uv
  expected: "true"
```
~~~

**Expected actions**
- create `src/`, `tests/`, and `scripts/`
- create `src/weather_service/main.py` with typed starter boilerplate
- generate uv-aligned `pyproject.toml` with pytest / ruff / pyright config
- copy the three listed skills into `.codex/skills/`
- write governance provenance into `.codex/skills-provenance.json`
- run `python3 .codex/skills/sense-env-scaffold/scripts/sense_env.py --mode acceptance --contract-file blueprint.md`

**Expected result**
- the repository is baseline-ready without invented business logic
- `README.md` includes `## Governance`, uv quick-start, and acceptance note
- acceptance either passes or returns explicit gaps

---

## Package-name fallback when blueprint does not declare `package:`

If `## Structural Invariants` omits an explicit package name:

```markdown
## Structural Invariants
- path: src
- path: tests
- entrypoint: src/main.py
```

and the repository directory is `weather-service`, the skill should derive:

```text
weather_service
```

**Correct behavior**
- normalize `-` to `_`
- use the derived package name consistently in `src/<package_name>/` surfaces when the blueprint needs a package namespace
- do not invent a stylized CamelCase package name

---

## Optional toolchain or invariant items stay lightweight

**Input lines**

```markdown
## Toolchain Expectation
- formatter @ ruff: Formatting via `ruff format`
- docs_preview @ mkdocs: Optional local docs preview (Optional)
```

**Correct behavior**
- install or configure the required formatter path
- keep optional items as placeholders, comments, or non-installed examples
- do not turn `(Optional)` into a mandatory download or heavyweight baseline dependency

**Anti-pattern**

```text
Wrong: install MkDocs and generate a full docs site just because the blueprint mentioned
an optional preview tool.
```

---

## Divergent required skill already exists in target repo

If the target already contains:

```text
.codex/skills/python-testing-pytest/
```

but its contents materially differ from the source library copy, the skill must stop.

**Correct behavior**
- show the conflict clearly
- ask the human whether to keep existing content, replace it, or reconcile manually
- avoid silent overwrite, merge, or "latest wins" behavior

**Anti-pattern**

```text
Wrong: overwrite the target skill folder because the names match.
```

---

## Missing or malformed acceptance block

This blueprint is invalid:

```markdown
## Acceptance Criteria
- Human note: looks good
```

**Correct behavior**
- stop before file creation
- report that the required ````yaml [sensing-assertions]```` block is missing
- do not fall back to discovery mode or invent assertions

---

## Required skill missing from the source library

If the blueprint lists:

```markdown
## Required Skills
- custom-governance-skill: Internal governance layer
```

but the active source library does not contain:

```text
.codex/skills/custom-governance-skill/SKILL.md
```

the skill must stop with a concrete error.

**Correct behavior**
- point to the missing source skill path
- do not create a partial placeholder skill folder
- do not silently continue with an incomplete governance baseline

---

## Acceptance handoff requires a real sensing implementation

If the blueprint requires acceptance but the target repo does not end up with the
canonical CLI path available locally, the skill must not claim completion.

**Correct behavior**
- ensure `sense-env-scaffold` was copied or an equivalent local install already exists
- run `python3 .codex/skills/sense-env-scaffold/scripts/sense_env.py --mode acceptance --contract-file blueprint.md`
- if acceptance cannot run, stop and explain why the handoff is incomplete

---

## Anti-pattern summary

| Anti-pattern | Why it fails |
| --- | --- |
| Start init before validating the blueprint contract | The skill may create a baseline against an invalid spec |
| Treat prose notes as machine-readable keys | Human notes are intentionally skippable |
| Auto-overwrite divergent config or skill folders | Ambiguous governance changes require human approval |
| Generate business services or concrete secrets | Out of scope for a baseline initializer |
| Skip acceptance because the generated files look reasonable | The workflow requires a closed build-and-acceptance loop |
