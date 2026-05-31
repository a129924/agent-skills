# Review Verdict Contract

Use this reference to keep `python-blueprint-review` output machine-consumable and
review-only.

## Required output shape

Return exactly one JSON object:

```json
{
  "verdict": "approved|needs-rework",
  "blocking_issues": [
    {
      "issue": "string",
      "section": "string",
      "fix": "string"
    }
  ]
}
```

Rules:
- emit no prose before or after the JSON object
- use `approved` only when no blocking design defects remain
- use `needs-rework` when any missing-dimension, capability, locatability, acceptance, or lane-fit defect exists
- keep `blocking_issues` empty only when the verdict is `approved`

## Blocking issue expectations

Each blocking issue should:
- name the real design defect
- point to the failing section or review dimension
- state the repair needed to make the blueprint reviewable again

Good blocking fixes:
- `Name the required test framework and linting tool explicitly.`
- `Replace abstract structure terms with concrete package, path, and entrypoint values.`
- `Reroute this contract to python-retrofit-plan-authoring because it describes legacy-preservation work.`

Weak blocking fixes to avoid:
- `Improve this section.`
- `Make it clearer.`
- `Probably use the standard layout.`

## Review-only boundary

The verdict must not:
- rewrite the blueprint inline
- start execution steps
- claim that implementation is now authorized
- replace authoring or retrofit skills by doing their job directly
