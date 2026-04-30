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
- use `approved` only when no blocking contract defects remain
- use `needs-rework` when any locked-schema, required-skill, locatability, or lane-fit defect exists
- keep `blocking_issues` empty only when the verdict is `approved`

## Blocking issue expectations

Each blocking issue should:
- name the real contract defect
- point to the failing section or section pair
- state the repair needed to make the blueprint reviewable again

Good blocking fixes:
- “Replace the guessed skill alias with an exact current-library skill name.”
- “Move the fenced `yaml [sensing-assertions]` block immediately under `## Acceptance Criteria`.”
- “Reroute this contract to `python-retrofit-plan-authoring` because it describes legacy-preservation work.”

Weak blocking fixes to avoid:
- “Improve this section.”
- “Make it clearer.”
- “Probably use the standard layout.”

## Review-only boundary

The verdict must not:
- rewrite the blueprint inline
- start executor steps
- claim that initialization is now authorized
- replace authoring or retrofit skills by doing their job directly
