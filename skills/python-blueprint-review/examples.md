# Python Blueprint Review Examples

Use these examples after `SKILL.md` has already narrowed the task to reviewing an
authored greenfield `blueprint.md`.

## Approved / valid greenfield blueprint

A blueprint that:
- uses the locked six-section blueprint v1 order
- starts `## Acceptance Criteria` with `yaml [sensing-assertions]`
- lists exact library skill names such as `sense-env-scaffold`
- names concrete locators such as `package: weather_service` and `entrypoint: src/weather_service/main.py`
- contains no retrofit preservation or migration pressure

Typical verdict:

```json
{
  "verdict": "approved",
  "blocking_issues": []
}
```

---

## Needs-rework / wrong section order

This blueprint is invalid:

~~~markdown
## Project Overview
...

## Toolchain Expectation
...

## Required Skills
...
~~~

Correct review behavior:
- return `needs-rework`
- cite the locked order mismatch as a blocking issue
- do not rewrite the blueprint inline

Typical verdict:

```json
{
  "verdict": "needs-rework",
  "blocking_issues": [
    {
      "issue": "Blueprint headings are out of the locked v1 order.",
      "section": "Toolchain Expectation / Required Skills",
      "fix": "Reorder the blueprint to Project Overview -> Required Skills -> Toolchain Expectation -> Structural Invariants -> Quality Thresholds -> Acceptance Criteria."
    }
  ]
}
```

---

## Needs-rework / missing or malformed `yaml [sensing-assertions]`

This blueprint is invalid:

~~~markdown
## Acceptance Criteria
- Explain the acceptance goals first.

```yaml
- kind: path_exists
  target: pyproject.toml
```
~~~

Correct review behavior:
- fail the review because the fenced block is not tagged `yaml [sensing-assertions]`
- fail the review because prose appears before the machine-readable block
- fail the review because the assertion is missing `expected`

Typical verdict:

```json
{
  "verdict": "needs-rework",
  "blocking_issues": [
    {
      "issue": "Acceptance criteria do not start with a valid `yaml [sensing-assertions]` block.",
      "section": "Acceptance Criteria",
      "fix": "Place a parseable fenced `yaml [sensing-assertions]` block immediately under `## Acceptance Criteria` and include `kind`, `target`, and `expected` in every assertion."
    }
  ]
}
```

---

## Needs-rework / missing skill or abstract structural invariants

This blueprint is invalid:

~~~markdown
## Required Skills
- python_testing_pytest: Test baseline

## Structural Invariants
- path: modern src layout
- entrypoint: standard CLI
~~~

Correct review behavior:
- return `needs-rework`
- identify `python_testing_pytest` as an exact-name validation failure
- identify the structural items as non-locatable
- do not normalize the skill name or guess replacement paths

Typical verdict:

```json
{
  "verdict": "needs-rework",
  "blocking_issues": [
    {
      "issue": "Required skill name does not match a current-library directory exactly.",
      "section": "Required Skills",
      "fix": "Replace `python_testing_pytest` with an exact existing skill name such as `python-testing-pytest` if that is the intended dependency."
    },
    {
      "issue": "Structural invariants are too abstract for executor consumption.",
      "section": "Structural Invariants",
      "fix": "Provide concrete package, path, and entrypoint values such as `package: weather_service` and `entrypoint: src/weather_service/main.py`."
    }
  ]
}
```

---

## Needs-rework / lane mismatch should reroute to retrofit

Request surface:

```text
Preserve the current app.py behavior, move legacy package code under src/, and replace requirements.txt with pyproject.toml.
```

Correct review behavior:
- return `needs-rework`
- identify that the blueprint is not truly greenfield
- tell the author to reroute the contract to `python-retrofit-plan-authoring`
- do not approve the blueprint just because the target state resembles a baseline

Typical verdict:

```json
{
  "verdict": "needs-rework",
  "blocking_issues": [
    {
      "issue": "The contract describes retrofit work rather than a greenfield baseline.",
      "section": "Project Overview / Structural Invariants",
      "fix": "Reroute this work to `python-retrofit-plan-authoring` and author a retrofit contract that records current-state preservation and migration details."
    }
  ]
}
```

---

## Anti-pattern summary

| Anti-pattern | Why it fails |
| --- | --- |
| Approve a blueprint with reordered headings | `python-project-init-greenfield` consumes the locked section order |
| Accept prose before the fenced sensing block | v1 requires the machine-readable block immediately under `## Acceptance Criteria` |
| Normalize `_` to `-` in skill names | `Required Skills` validation is exact-name only |
| Treat “modern layout” as locatable structure | executor-facing structure must be concrete |
| Approve legacy-preservation work as greenfield | lane mismatch should fail review and reroute |
