# Python Retrofit Plan Review Examples

Use these examples after `SKILL.md` has already narrowed the task to reviewing an
authored Retrofit V2 `retrofit-plan.md`.

## Approved / valid Retrofit V2 contract

A plan that:
- uses the locked five-section Retrofit V2 order
- includes a parseable `yaml [migration-strategy]` block with supported values
- includes a parseable `yaml [sensing-assertions]` block using only supported kinds
- names concrete locators such as `app.py`, `src/weather_service/main.py`, and `pyproject.toml`
- keeps strategy prose separate from runtime gate answers

Typical verdict:

```json
{
  "verdict": "approved",
  "blocking_issues": []
}
```

---

## Needs-rework / wrong section order or old headings

This plan is invalid:

~~~markdown
## Survey Summary
...

## Target Transformation
...

## Migration Strategy
...
~~~

Correct review behavior:
- return `needs-rework`
- cite the locked order mismatch as a blocking issue
- do not rewrite the contract inline

Typical verdict:

```json
{
  "verdict": "needs-rework",
  "blocking_issues": [
    {
      "issue": "Retrofit headings are missing or out of the locked V2 order.",
      "section": "Survey Summary / Target Transformation / Migration Strategy",
      "fix": "Restore the exact heading order: Survey Summary -> Gap Analysis -> Target Transformation -> Migration Strategy -> Acceptance Criteria, without old-heading aliases."
    }
  ]
}
```

---

## Needs-rework / malformed `yaml [migration-strategy]` or unsupported `risk_level`

This plan is invalid:

~~~markdown
## Migration Strategy
```yaml [migration-strategy]
risk_level: MEDIUM
destructive_actions: move app.py -> src/weather_service/main.py
backup_required: maybe
```
~~~

Correct review behavior:
- fail the review because `MEDIUM` is unsupported
- fail the review because `destructive_actions` is not a YAML sequence
- fail the review because `backup_required` is not the YAML boolean `true` or `false`

Typical verdict:

```json
{
  "verdict": "needs-rework",
  "blocking_issues": [
    {
      "issue": "`risk_level` is unsupported for the current Retrofit V2 execution contract.",
      "section": "Migration Strategy",
      "fix": "Use only `LOW` or `HIGH` in `yaml [migration-strategy]`; `MEDIUM` must not appear in current reviewable contracts."
    },
    {
      "issue": "`destructive_actions` must be a YAML sequence and `backup_required` must be a YAML boolean.",
      "section": "Migration Strategy",
      "fix": "Rewrite `destructive_actions` as a YAML list and set `backup_required` to `true` or `false` so the block stays parseable and executable."
    }
  ]
}
```

---

## Needs-rework / malformed or unsupported `yaml [sensing-assertions]`

This plan is invalid:

~~~markdown
## Acceptance Criteria
```yaml [sensing-assertions]
- kind: config_key_exists
  target: pyproject.toml
- kind: path_exists
  target: src/weather_service/main.py
  expected: "true"
```
~~~

Correct review behavior:
- fail the review because `config_key_exists` is unsupported
- fail the review because the first assertion is missing `expected`
- do not widen the supported assertion-kind set during review

Typical verdict:

```json
{
  "verdict": "needs-rework",
  "blocking_issues": [
    {
      "issue": "Acceptance assertions include unsupported or incomplete records.",
      "section": "Acceptance Criteria",
      "fix": "Keep every assertion inside the supported subset (`path_exists`, `path_type`, `command_available`) and include `kind`, `target`, and `expected` in every record."
    }
  ]
}
```

---

## Needs-rework / `LOW` risk contradicted by destructive reality

This plan is invalid:

~~~markdown
## Target Transformation
- target entrypoint: src/weather_service/main.py
- replace requirements.txt with pyproject.toml

## Migration Strategy
```yaml [migration-strategy]
risk_level: LOW
destructive_actions: []
backup_required: false
```
~~~

Correct review behavior:
- return `needs-rework`
- identify that moves or replacements make the written plan destructive
- require the contract to align the risk metadata instead of letting execution discover the lie

Typical verdict:

```json
{
  "verdict": "needs-rework",
  "blocking_issues": [
    {
      "issue": "Declared `LOW` risk contradicts the destructive retrofit described elsewhere in the contract.",
      "section": "Target Transformation / Migration Strategy",
      "fix": "Align the contract to the real destructive scope by using supported HIGH-risk metadata and listing the concrete destructive actions, or rewrite the plan to stay purely additive."
    }
  ]
}
```

---

## Needs-rework / authoring-versus-executor boundary violation

This plan is invalid:

~~~markdown
## Target Transformation
- Migration Direction: automatically delete app.py and overwrite setup.cfg if conflicts appear
~~~

Correct review behavior:
- return `needs-rework`
- identify that planning prose is pre-authorizing runtime gate answers
- keep the repair focused on boundary correction rather than execution advice

Typical verdict:

```json
{
  "verdict": "needs-rework",
  "blocking_issues": [
    {
      "issue": "Planning prose tries to pre-decide runtime conflict or destructive outcomes owned by the executor.",
      "section": "Target Transformation",
      "fix": "Limit strategy text to intent and remove pre-authorized outcomes such as automatic delete, overwrite, move, coexist, or preserve decisions."
    }
  ]
}
```

---

## Needs-rework / abstract locatability or wrong-lane request

Request surface:

```text
Modernize the project layout, clean up old files, and create the first governed Python structure for this mostly empty repository.
```

Correct review behavior:
- return `needs-rework`
- identify that the contract is too abstract and also greenfield-shaped rather than retrofit-shaped
- reroute to the correct upstream lane instead of approving or repairing inline

Typical verdict:

```json
{
  "verdict": "needs-rework",
  "blocking_issues": [
    {
      "issue": "The contract is not concrete enough for retrofit execution and appears to belong in the greenfield lane instead.",
      "section": "Survey Summary / Target Transformation",
      "fix": "Provide concrete current-state and target locators for real retrofit work, or reroute this request to `python-blueprint-authoring` because it describes first-structure baseline work rather than retrofit migration."
    }
  ]
}
```

---

## Anti-pattern summary

| Anti-pattern | Why it fails |
| --- | --- |
| Approve old or reordered headings | `python-project-retrofit` consumes the locked Retrofit V2 order |
| Accept `MEDIUM` as “close enough” | current execution supports only `LOW` or `HIGH` |
| Allow unsupported sensing assertion kinds | `sense_env.py` acceptance still supports only the v1 subset |
| Let strategy prose choose delete or move outcomes | runtime gates stay executor-owned |
| Treat “modernize the layout” as locatable | executor-facing contracts must name concrete paths, files, and tools |
| Review a greenfield or skill-folder task here | this skill owns authored Retrofit V2 contract review only |
