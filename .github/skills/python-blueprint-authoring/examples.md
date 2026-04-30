# Python Blueprint Authoring Examples

Detailed examples for `python-blueprint-authoring`.

---

## Happy path: review-ready greenfield blueprint

**Input facts**
- repository state: empty or baseline-only
- repository name: `weather-service`
- required skills already in library: `sense-env-scaffold`, `python-testing-pytest`, `python-type-hints-strict`
- desired package: `weather_service`
- desired entrypoint: `src/weather_service/main.py`

**Correct blueprint shape**

~~~markdown
## Project Overview
- Name: Weather Service
- Purpose: Provide a governed Python baseline for weather data collection and reporting.

## Required Skills
- sense-env-scaffold: Acceptance verification runner
- python-testing-pytest: Pytest unit-testing baseline
- python-type-hints-strict: Strict typing baseline

## Toolchain Expectation
- python @ 3.12: Runtime baseline
- package_manager @ uv: Dependency and lock workflow
- linter @ ruff: Linting and formatting surface
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
- Acceptance should pass after greenfield init completes.
~~~

**Why this is correct**
- the section order matches the locked blueprint v1 contract exactly
- every required skill uses an exact current-library directory name
- structural invariants are concrete enough for `python-project-init-greenfield` to scaffold without guesswork
- the `yaml [sensing-assertions]` block appears immediately under `## Acceptance Criteria`

---

## Stop-and-ask: required skill is missing from the current library

**Requested line**

```markdown
## Required Skills
- python-linting-baseline: Shared lint policy
```

**Correct behavior**
- stop authoring before producing a review-ready blueprint
- report that `.github/skills/python-linting-baseline/` is not present in the active library
- ask the human to choose an existing exact skill name or install/add the missing skill first
- do not silently rewrite the line to a “close enough” skill such as `python-testing-pytest`

**Anti-pattern**

```text
Wrong: normalize the request to another skill, keep the unknown name as a placeholder, or defer the error to greenfield execution.
```

---

## Stop-and-ask: `Structural Invariants` are too abstract to locate

**Request**

```text
Use a modern src layout, sensible packages, and whatever entrypoint looks standard.
```

**Correct behavior**
- stop before drafting the final blueprint
- ask for a concrete package name, concrete paths, and an exact entrypoint path
- explain that `python-project-init-greenfield` consumes locatable invariants and should not infer them from style words

**Anti-pattern**

```text
Wrong: invent `src/app/main.py`, call the package `app_core`, and assume the executor can refine it later.
```

---

## Lane mismatch: request is really retrofit planning

**Request**

```text
The repository already has app.py, requirements.txt, and a legacy package. Plan the move into src/, preserve current behavior, and add acceptance checks.
```

**Correct behavior**
- stop blueprint authoring
- route to `python-retrofit-plan-authoring`
- explain that existing files, migration pressure, and preservation requirements make this a retrofit lane, not greenfield blueprint authoring

**Anti-pattern**

```text
Wrong: write a greenfield blueprint that pretends the legacy files do not matter.
```

---

## Anti-pattern summary

| Anti-pattern | Why it fails |
| --- | --- |
| Guess a near-match skill name | Exact-name validation is authoring-time blocking |
| Put prose before `yaml [sensing-assertions]` | The executor expects the block immediately under `## Acceptance Criteria` |
| Describe structure as “clean” or “modern” | The executor needs locatable package, path, and entrypoint facts |
| Use blueprint authoring for an existing repository migration | Lane mismatch should reroute to retrofit authoring |
| Add new headings or schema aliases | The skill must reuse the existing blueprint v1 contract exactly |
