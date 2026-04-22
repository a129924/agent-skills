# Env Manifest Schema

Defines the structure of `.github/env-manifest.json` and
`.github/env-manifest.snapshot.json` produced by `.github/skills/sense-env-scaffold/scripts/sense_env.py`.

## Purpose

The manifest is the single structured record of the repository's environment state
at the time of a `sense_env.py` run. It is designed to be:

- human-readable (stable JSON indentation)
- machine-parseable (fixed top-level keys, `snake_case` throughout)
- safe to commit (snapshot variant strips machine-local and secret-shaped data)

---

## Top-level schema

All five keys are required on every successful run. Their values may be empty
collections but the keys must be present.

```json
{
  "meta": { ... },
  "fingerprint": { ... },
  "facts": { ... },
  "assertions": [ ... ],
  "gaps": [ ... ]
}
```

| Key | Type | Description |
|---|---|---|
| `meta` | object | Run metadata: mode, timestamp, script version |
| `fingerprint` | object | Stable identity signals for the run environment |
| `facts` | object | Collected environment facts (tool versions, file presence, Git state) |
| `assertions` | array | Per-assertion evaluation records (acceptance mode only; empty in discovery) |
| `gaps` | array | Unmet items that require remediation |

---

## `meta` module

```json
"meta": {
  "schema_version": "1",
  "run_mode": "discovery",
  "timestamp_utc": "2026-04-22T06:00:00Z",
  "script_version": "1.0.0"
}
```

| Field | Type | Notes |
|---|---|---|
| `schema_version` | string | Fixed `"1"` for v1 |
| `run_mode` | string | `"discovery"` or `"acceptance"` |
| `timestamp_utc` | string | ISO 8601 UTC |
| `script_version` | string | Semver string from inside the script |

---

## `fingerprint` module

```json
"fingerprint": {
  "repo_root_marker": ".git",
  "python_version": "3.11.9",
  "platform": "darwin"
}
```

| Field | Type | Notes |
|---|---|---|
| `repo_root_marker` | string | `".git"` (directory or file); `null` when not in a repo |
| `python_version` | string | `sys.version_info` formatted as `"major.minor.patch"` |
| `platform` | string | `sys.platform` value |

Snapshot shaping replaces or removes any field that exposes machine-specific detail
beyond what is listed here.

---

## `facts` module

```json
"facts": {
  "repo_present": true,
  "git_available": true,
  "current_branch": "feat/andrew/sense-env-scaffold",
  "workspace_clean": false,
  "key_paths": {
    "README.md": true,
    ".github/": true,
    "pyproject.toml": false,
    "tests/": false,
    "scripts/": true,
    ".github/copilot-instructions.md": true
  }
}
```

| Field | Type | Notes |
|---|---|---|
| `repo_present` | boolean | `true` when `.git` marker found |
| `git_available` | boolean | `true` when `git` command runs without error |
| `current_branch` | string or null | Branch name; `null` when Git unavailable or detached HEAD |
| `workspace_clean` | boolean or null | `true` when `git status --porcelain` returns empty; `null` when Git unavailable |
| `key_paths` | object | Map of well-known relative paths to boolean presence values |

`key_paths` values are repo-relative. The v1 set is fixed; do not add arbitrary paths
without a separate planning topic.

---

## `assertions` module

Populated in acceptance mode only. Empty array `[]` in discovery mode.

Each assertion record:

```json
{
  "kind": "path_exists",
  "target": "scripts/sense_env.py",
  "expected": true,
  "actual": true,
  "result": "PASS"
}
```

| Field | Type | Notes |
|---|---|---|
| `kind` | string | One of the v1 supported kinds (see below) |
| `target` | string | The subject of the assertion |
| `expected` | any | Expected value as parsed from the contract |
| `actual` | any | Observed value at run time |
| `result` | string | `"PASS"`, `"FAIL"`, or `"UNSUPPORTED"` |

### V1 supported assertion kinds

| Kind | Target meaning | Expected value |
|---|---|---|
| `path_exists` | Repo-relative path | `true` / `false` |
| `path_type` | Repo-relative path | `"file"` / `"directory"` |
| `command_available` | Executable name | `true` / `false` |

Any assertion kind outside this list is recorded as `"UNSUPPORTED"` and placed in
`gaps` with type `MISSING`. The script does not claim general YAML support; only a
narrow documented subset is parsed.

---

## `gaps` module

Records items that failed assertion, were unsupported, or represent missing optional
components discovered in discovery mode.

```json
{
  "type": "MISSING",
  "target": "pyproject.toml",
  "detail": "path_exists assertion failed: path not found"
}
```

| Field | Type | Notes |
|---|---|---|
| `type` | string | `"MISSING"`, `"MISMATCH"`, or `"DEPRECATED"` |
| `target` | string | The subject that has the gap |
| `detail` | string | Human-readable explanation |

| Gap type | Meaning |
|---|---|
| `MISSING` | Expected item is absent |
| `MISMATCH` | Item exists but value or type does not match expectation |
| `DEPRECATED` | Item is present but marked as no longer valid by the contract |

---

## Example: discovery-mode manifest

```json
{
  "meta": {
    "schema_version": "1",
    "run_mode": "discovery",
    "timestamp_utc": "2026-04-22T06:00:00Z",
    "script_version": "1.0.0"
  },
  "fingerprint": {
    "repo_root_marker": ".git",
    "python_version": "3.11.9",
    "platform": "darwin"
  },
  "facts": {
    "repo_present": true,
    "git_available": true,
    "current_branch": "feat/andrew/sense-env-scaffold",
    "workspace_clean": false,
    "key_paths": {
      "README.md": true,
      ".github/": true,
      "pyproject.toml": false,
      "tests/": false,
      "scripts/": true,
      ".github/copilot-instructions.md": true
    }
  },
  "assertions": [],
  "gaps": []
}
```

---

## Example: acceptance-mode manifest (one failure)

```json
{
  "meta": {
    "schema_version": "1",
    "run_mode": "acceptance",
    "timestamp_utc": "2026-04-22T06:01:00Z",
    "script_version": "1.0.0"
  },
  "fingerprint": {
    "repo_root_marker": ".git",
    "python_version": "3.11.9",
    "platform": "darwin"
  },
  "facts": {
    "repo_present": true,
    "git_available": true,
    "current_branch": "feat/andrew/sense-env-scaffold",
    "workspace_clean": false,
    "key_paths": {
      "README.md": true,
      ".github/": true,
      "pyproject.toml": false,
      "tests/": false,
      "scripts/": true,
      ".github/copilot-instructions.md": true
    }
  },
  "assertions": [
    {
      "kind": "path_exists",
      "target": "pyproject.toml",
      "expected": true,
      "actual": false,
      "result": "FAIL"
    },
    {
      "kind": "command_available",
      "target": "python3",
      "expected": true,
      "actual": true,
      "result": "PASS"
    }
  ],
  "gaps": [
    {
      "type": "MISSING",
      "target": "pyproject.toml",
      "detail": "path_exists assertion failed: path not found"
    }
  ]
}
```

---

## Snapshot filtering and promotion

When `--snapshot` is used, the script writes a second file:
`.github/env-manifest.snapshot.json`

Snapshot shaping rules in v1 (applied before writing):

| Data category | Treatment in v1 |
|---|---|
| Selected fingerprint fields that are machine-local | Removed (only `repo_root_marker`, `python_version`, `platform` are kept) |
| Facts fields whose keys match secret-related patterns | Removed |
| Absolute local paths inside `key_paths` | Replaced with `null` |
| Usernames in paths | Not specifically scrubbed in v1 |
| Machine-specific identifiers (hostname, UID) | Not broadly guaranteed to be removed in v1 |
| Secret-shaped values (tokens, keys, passwords) | Not inspected by value in v1; only key-pattern matching is applied |
| Branch names | Kept |
| Platform string | Kept |
| Python version | Kept |

The v1 snapshot is only partially sanitized. It should not be treated as a complete
scrub of usernames, host identifiers, or secret-like values based on their content.

The snapshot is written only when the run exits `0`. If the run exits `10`, `20`, or
`30`, no snapshot is written. This is enforced by the script; callers should not
attempt to promote partial or error-state manifests.

Snapshot promotion to a permanent record (for example, committing to the repo) is
a workflow-level human decision outside the script's responsibility.
