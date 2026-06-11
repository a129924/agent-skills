# Sensing Delta Contract

Use this reference when `python-project-retrofit` produces the post-retrofit
summary artifact.

## Purpose

The Sensing Delta Report is the single-view record of what the retrofit changed.
It should make the before/after state understandable without reading the full Git
history.

## Required top-level shape

The artifact is a JSON object with a top-level `delta_summary` key.

```json
{
  "delta_summary": {
    "timestamp": "2026-04-28T12:00:00Z",
    "pre_retrofit_state": {},
    "post_retrofit_state": {},
    "changes": [],
    "new_files": [],
    "deleted_files": [],
    "modified_files": []
  }
}
```

## Required fields

`delta_summary` must contain:

- `timestamp` — ISO-8601 time for the finished retrofit state capture
- `pre_retrofit_state` — summarized facts sensed before changes
- `post_retrofit_state` — summarized facts sensed after changes
- `changes` — ordered change records
- `new_files` — paths created by the retrofit
- `deleted_files` — paths removed by the retrofit
- `modified_files` — paths changed in place

## Change-record schema

Each entry in `changes` must contain:

- `fact_key` — the fact or surface being described
- `before` — human-readable prior state
- `after` — human-readable resulting state
- `operation` — one of:
  - `MOVED`
  - `CREATED`
  - `MODIFIED`
  - `DELETED`

Do not invent extra operation names.

## Interpretation rules

- use `MOVED` when the same logical artifact changed path
- use `CREATED` when the artifact did not exist before retrofit
- use `MODIFIED` when the path survived but its contents or governing role changed
- use `DELETED` when the artifact was intentionally removed

If multiple facts changed for one file, prefer multiple `changes` entries over a
single ambiguous record.

## Example

```json
{
  "delta_summary": {
    "timestamp": "2026-04-28T12:00:00Z",
    "pre_retrofit_state": {
      "entrypoints": ["app.py"],
      "toolchain": ["requirements.txt"]
    },
    "post_retrofit_state": {
      "entrypoints": ["src/weather_service/main.py"],
      "toolchain": ["pyproject.toml"]
    },
    "changes": [
      {
        "fact_key": "primary_entrypoint",
        "before": "app.py",
        "after": "src/weather_service/main.py",
        "operation": "MOVED"
      },
      {
        "fact_key": "dependency_configuration",
        "before": "requirements.txt",
        "after": "pyproject.toml",
        "operation": "MODIFIED"
      }
    ],
    "new_files": ["src/weather_service/main.py", "pyproject.toml"],
    "deleted_files": [],
    "modified_files": ["pyproject.toml"]
  }
}
```

## Human-reading guidance

A good Delta Report lets a reviewer answer these questions quickly:

- what existed before the retrofit?
- what exists now?
- which facts moved, appeared, changed, or disappeared?
- which paths were created, deleted, or modified?

## Provenance linkage

Record the Delta Report reference alongside provenance so the retrofit has both:

- a governance record in `.<platform>/skills-provenance.json`
- a runtime artifact reference describing the before/after surgery

## Acceptance relationship

The Delta Report summarizes the retrofit. It does not replace acceptance.
After the report exists, hand off to:

```bash
python3 .<platform>/skills/sense-env-scaffold/scripts/sense_env.py --mode acceptance --contract-file retrofit-plan.md
```

If acceptance fails, keep the Delta Report; it still documents what changed.
