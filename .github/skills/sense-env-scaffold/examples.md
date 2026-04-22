# Sense-Env Scaffold Examples

Detailed usage patterns, multi-path decisions, anti-patterns, and error scenarios
for `sense-env-scaffold`.

---

## Discovery mode — collect environment facts

**When to use:** before beginning implementation work; no contract needed.

```bash
python3 .github/skills/sense-env-scaffold/scripts/sense_env.py --mode discovery
```

Expected outcome:
- Exit `0`
- `.github/env-manifest.json` written with all five top-level keys
- Optional tools that are missing produce `null` values, not errors

Resulting manifest shape:

```json
{
  "meta":        { "schema_version": "1", "run_mode": "discovery", ... },
  "fingerprint": { "repo_root_marker": ".git", "python_version": "3.x.y", ... },
  "facts":       { "current_branch": "...", "repo_present": true, ... },
  "assertions":  [],
  "gaps":        []
}
```

---

## Discovery mode — with snapshot export

**When to use:** when the manifest needs to be committed or shared without
machine-local data (absolute paths, usernames).

```bash
python3 .github/skills/sense-env-scaffold/scripts/sense_env.py \
  --mode discovery --snapshot
```

Expected outcome:
- Exit `0`
- `.github/env-manifest.json` written (full, live)
- `.github/env-manifest.snapshot.json` written (filtered, secret-free)

Anti-pattern:

```bash
# Wrong: snapshot flag on a run that will exit non-zero
python3 .github/skills/sense-env-scaffold/scripts/sense_env.py \
  --mode acceptance --snapshot
# Snapshot is NOT written when exit is 20 or 30.
# Do not assume the snapshot file was created after a failed acceptance run.
```

---

## Acceptance mode — explicit contract file

**When to use:** evaluate a specific blueprint or plan file's sensing assertions.

```bash
python3 .github/skills/sense-env-scaffold/scripts/sense_env.py \
  --mode acceptance --contract-file plan/my-blueprint.md
```

The contract file must contain a fenced block tagged `yaml [sensing-assertions]`:

~~~markdown
```yaml [sensing-assertions]
- kind: path_exists
  target: pyproject.toml
  expected: "true"
- kind: command_available
  target: python3
  expected: "true"
```
~~~

Expected outcomes by exit code:

| Exit | Meaning |
|---|---|
| `0` | All assertions passed (or only UNSUPPORTED — no FAIL) |
| `20` | One or more assertions result is FAIL; read `gaps` in manifest |
| `30` | Contract file not readable, or fenced block absent or malformed |

---

## Acceptance mode — implicit contract lookup

**When to use:** the project uses the default contract file name convention.

```bash
python3 .github/skills/sense-env-scaffold/scripts/sense_env.py \
  --mode acceptance
```

Lookup order (first readable file wins):
1. `<repo_root>/retrofit-plan.md`
2. `<repo_root>/blueprint.md`

Anti-pattern:

```bash
# Wrong: running acceptance with no contract and expecting exit 0
python3 .github/skills/sense-env-scaffold/scripts/sense_env.py --mode acceptance
# If neither retrofit-plan.md nor blueprint.md exists, exit is 30.
# Do not assume discovery-style tolerance applies to acceptance mode.
```

---

## Reading acceptance failures

When exit is `20`, the manifest `gaps` array describes what failed:

```json
{
  "gaps": [
    {
      "type": "FAIL",
      "target": "pyproject.toml",
      "detail": "path_exists: expected true, got false"
    }
  ]
}
```

Next action: fix the environment gap, then re-run acceptance.

---

## Unsupported assertion kind

If the contract contains an assertion kind outside the v1 subset
(`path_exists`, `path_type`, `command_available`), the script does **not**
exit `30`. Instead:

```json
{
  "result": "UNSUPPORTED",
  "kind": "config_key_exists"
}
```

A gap entry is added and the run continues. Exit `20` is **not** triggered by
UNSUPPORTED alone; only a `result == "FAIL"` assertion causes exit `20`.

Anti-pattern:

```bash
# Wrong: writing a contract with rich assertion kinds and expecting them to pass
- kind: config_key_exists
  key: tool.poetry.name
  required: true
  expected: true
# This produces result: UNSUPPORTED, not a pass.
# Extend the script in a separate planning topic before using new kinds.
```

---

## Custom output path

**When to use:** CI or tooling writes manifests to a non-default path.

```bash
python3 .github/skills/sense-env-scaffold/scripts/sense_env.py \
  --mode discovery --output /tmp/ci-manifest.json
```

- Parent directory is created unconditionally (`parents=True, exist_ok=True`).

---

## Anti-patterns summary

| Anti-pattern | Why it fails |
|---|---|
| Run `--mode acceptance` with no contract and expect success | Exit `30`; no contract means no assertions can be evaluated |
| Check for snapshot file after a non-zero run | Snapshot is only written on exit `0` |
| Use unsupported assertion kinds and expect `PASS` | Result is `UNSUPPORTED`; required unsupported assertions count as failures |
| Modify `scripts/sense_env.py` as part of skill invocation | The script is a fixed prototype tool; changes require a separate planning topic |
| Invoke from outside the repository directory tree | `find_repo_root` falls back to cwd; the manifest is still written but `repo_root_marker` may be absent |
