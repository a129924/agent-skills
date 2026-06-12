# Review Verdict Contract

Use this reference to keep `python-retrofit-plan-review` output
machine-consumable and review-only.

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
- use `approved` only when no blocking contract defects remain
- use `needs-rework` when any schema, risk, boundary, locatability, or lane-fit defect exists
- keep `blocking_issues` empty only when the verdict is `approved`

## Blocking issue expectations

Each blocking issue should:
- name the real contract defect
- point to the failing section or section pair
- state the repair needed to make the plan reviewable again
- stay specific enough that the author can repair the contract without guessing what failed

Good blocking fixes:
- “Restore the locked Retrofit V2 heading order and remove old-heading aliases.”
- “Replace unsupported `MEDIUM` risk metadata with a supported `LOW` or `HIGH` contract that matches the real destructive scope.”
- “Rewrite the sensing assertions so every record uses only `path_exists`, `path_type`, or `command_available` and includes `kind`, `target`, and `expected`.”
- “Reroute this request to `python-blueprint-authoring` because it describes greenfield baseline work rather than retrofit migration.”

Weak blocking fixes to avoid:
- “Improve this section.”
- “Make it clearer.”
- “Probably use the standard layout.”
- “Execution can decide later.”

## Review-only boundary

The verdict must not:
- rewrite the retrofit plan inline
- start executor steps
- claim that retrofit execution is now authorized
- replace authoring or greenfield lanes by doing their job directly
- widen the supported risk or assertion-kind contract while reviewing
