# Python Blueprint Review Examples

Use these examples after `SKILL.md` has already narrowed the task to reviewing an
authored greenfield `blueprint.md`.

## Approved / valid greenfield blueprint

A blueprint can be approved when it:
- uses any heading names or section order, as long as the design dimensions are still clearly covered
- states the project purpose and required capabilities concretely
- names concrete locators such as `package: weather_service` and `entrypoint: src/weather_service/main.py`
- defines toolchain and quality expectations specifically enough to implement
- contains observable acceptance outcomes
- contains no retrofit preservation or migration pressure

Typical verdict:

```json
{
  "verdict": "approved",
  "blocking_issues": []
}
```

## Approved / different section names and order

This blueprint can still be valid:

~~~markdown
## Outcome
- Build a Python CLI weather service for batch forecasts.

## Verification
- Running `python -m weather_service.main --help` prints CLI usage.
- `pytest` passes for the baseline project.

## Delivery Shape
- package: weather_service
- path: src/weather_service
- path: tests
- entrypoint: src/weather_service/main.py

## Dependencies
- pytest for automated tests
- ruff for linting
~~~

Correct review behavior:
- allow the non-template section names
- review whether the six design dimensions are still covered
- return `approved` if no blocking ambiguity remains

## Needs-rework / missing capability requirements

This blueprint is invalid:

~~~markdown
## Requirements
- Include the normal developer tooling.
- Support a standard Python test setup.
~~~

Correct review behavior:
- return `needs-rework`
- identify that the capability requirements are too abstract
- do not guess which tooling or testing surface the author intended

Typical verdict:

```json
{
  "verdict": "needs-rework",
  "blocking_issues": [
    {
      "issue": "Capability requirements are too abstract to determine the intended tooling and dependency surface.",
      "section": "Requirements",
      "fix": "Name the required capabilities concretely, such as the expected test framework, linting tool, packaging approach, or other implementation-critical dependencies."
    }
  ]
}
```

## Needs-rework / abstract or contradictory locators

This blueprint is invalid:

~~~markdown
## Structure
- path: modern src layout
- package: weather_service
- entrypoint: standard CLI
~~~

Correct review behavior:
- return `needs-rework`
- identify the locators as non-locatable
- do not replace them with guessed paths

Typical verdict:

```json
{
  "verdict": "needs-rework",
  "blocking_issues": [
    {
      "issue": "Structural invariants are too abstract to locate the intended filesystem and entrypoint shape.",
      "section": "Structure",
      "fix": "Provide concrete package, path, and entrypoint values such as `package: weather_service`, `path: src/weather_service`, and `entrypoint: src/weather_service/main.py`."
    }
  ]
}
```

## Needs-rework / non-verifiable acceptance

This blueprint is invalid:

~~~markdown
## Acceptance
- The project should feel production-ready.
- The layout should be clean and maintainable.
~~~

Correct review behavior:
- return `needs-rework`
- identify that the acceptance criteria are aspirational rather than observable
- require concrete verification outcomes

Typical verdict:

```json
{
  "verdict": "needs-rework",
  "blocking_issues": [
    {
      "issue": "Acceptance criteria are aspirational and do not define observable or verifiable outcomes.",
      "section": "Acceptance",
      "fix": "Replace subjective goals with concrete checks, commands, files, behaviors, or test outcomes that can be observed and verified."
    }
  ]
}
```

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
      "section": "Project Overview / Structure",
      "fix": "Reroute this work to `python-retrofit-plan-authoring` and author a retrofit contract that records preservation and migration details explicitly."
    }
  ]
}
```

## Anti-pattern summary

| Anti-pattern | Why it fails |
| --- | --- |
| Reject a blueprint only because headings differ from a template | review dimensions matter; fixed heading order does not |
| Infer missing tooling from phrases like `standard test setup` | the reviewer must not guess capability requirements |
| Treat `modern layout` as locatable structure | downstream implementation still needs concrete paths and entrypoints |
| Accept acceptance prose with no observable checks | greenfield review still requires verifiable outcomes |
| Approve legacy-preservation work as greenfield | lane mismatch should fail review and reroute |
