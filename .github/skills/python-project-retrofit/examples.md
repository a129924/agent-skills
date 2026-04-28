# Python Project Retrofit Examples

Detailed examples for `python-project-retrofit`.

---

## Happy path: clean retrofit with explicit human confirmations

**Input retrofit plan shape**

~~~markdown
## Project Overview
- Current entrypoint: app.py
- Current package: none

## Target Structure
- path: src/weather_service
- path: tests
- entrypoint: src/weather_service/main.py

## Acceptance Criteria
```yaml [sensing-assertions]
- kind: path_exists
  target: src/weather_service/main.py
  expected: "true"
- kind: path_exists
  target: pyproject.toml
  expected: "true"
```
~~~

**Observed workspace**
- root `app.py` exists
- `requirements.txt` exists
- Git working tree is clean

**Correct behavior**
1. detect Gate 1 because `app.py` overlaps the planned entrypoint intent
2. ask the human to choose `move`, `delete`, `coexist`, or `abort`
3. detect Gate 2 because `requirements.txt` is an implicit config remnant
4. ask the human to choose `migrate`, `delete`, `preserve`, or `abort`
5. run Gate 3 immediately before the approved file move or overwrite
6. apply only the approved actions
7. generate the Sensing Delta Report
8. hand off to `python3 .github/skills/sense-env-scaffold/scripts/sense_env.py --mode acceptance --contract-file retrofit-plan.md`

**Expected result**
- the project is restructured without silent guesses
- the gate decisions are explicit and human-owned
- acceptance either passes or returns concrete gaps

---

## Gate 1: Shadow File Detection must offer all four outcomes

### Option A: `move`

**Situation**
- current file: `app.py`
- target file: `src/inventory/main.py`
- both represent the primary CLI entrypoint

**Correct behavior**
- explain the semantic overlap
- ask whether to move `app.py` into `src/inventory/main.py`
- wait for confirmation before touching either path

### Option B: `delete`

**Situation**
- current file: `legacy_runner.py`
- target file: `src/inventory/main.py`
- the human confirms the target file should replace the legacy runner entirely

**Correct behavior**
- state that deletion is destructive
- run the Git safety gate first
- delete only after the human explicitly chooses `delete`

### Option C: `coexist`

**Situation**
- `app.py` remains as a compatibility shim while the new package entrypoint lives at `src/inventory/main.py`

**Correct behavior**
- keep both files intentionally
- record coexistence as a deliberate design choice, not as unresolved drift
- include the resulting file-state change in the Delta Report

### Option D: `abort`

**Situation**
- the human is not ready to decide whether the root script and package entrypoint should coexist

**Correct behavior**
- stop the retrofit cleanly
- summarize the unresolved shadow conflict
- do not proceed to Gate 2 or any filesystem change

**Anti-pattern**

```text
Wrong: auto-move the root file because the target path looks more modern.
```

---

## Gate 2: Implicit Config Mining must stay explicit

### Migration path

**Observed remnants**
- `poetry.lock`
- `pyproject.toml`

**Correct behavior**
- explain that the existing toolchain appears Poetry-based
- ask whether to `migrate` that configuration to the target toolchain
- stop until the human confirms the migration scope

### Deletion path

**Observed remnants**
- `.venv`
- `Pipfile`

**Correct behavior**
- explain that deletion will remove local-environment or legacy package-manager traces
- require the Git safety check before any destructive cleanup
- delete only after the human chooses `delete`

### Preservation path

**Observed remnants**
- `requirements.txt`
- `setup.cfg`

**Correct behavior**
- allow the files to remain when the human chooses `preserve`
- avoid rewriting them into the target config automatically
- document the preserved remnants in the Delta Report as unchanged or intentionally retained context

### Abort path

**Correct behavior**
- if the human chooses `abort`, stop the retrofit rather than guessing which toolchain should win

**Anti-pattern**

```text
Wrong: merge `setup.cfg`, `requirements.txt`, and `pyproject.toml` into one synthesized config without asking.
```

---

## Gate ordering when multiple gates trigger together

**Situation**
- root `app.py` conflicts with planned `src/service/main.py`
- `poetry.lock` and `.venv` are present
- no file operations have run yet

**Correct behavior**
1. handle Shadow File Detection first
2. after the human resolves Gate 1, handle Implicit Config Mining
3. only then run Git safety immediately before the destructive operation

**Why this matters**
- the human should not be asked about config migration until the file-layout conflict is understood
- Git safety is a pre-destructive gate, not a substitute for semantic conflict resolution

---

## Gate 3: dirty Git state is a hard block

**Situation**
- the human chose `move`
- `git status --short` shows modified files

**Correct behavior**
- stop before moving, deleting, or overwriting anything
- state that the working tree is dirty
- require one of these human-approved paths:
  - commit the existing changes first
  - produce a backup first
- do not offer a bypass option

**Anti-pattern**

```text
Wrong: continue because the move is small and Git probably has enough history.
```

---

## Pre-destructive backup path

**Situation**
- the working tree is dirty
- the human cannot commit yet but wants a backup before continuing

**Correct behavior**
- create the approved backup artifact or location before destructive work resumes
- confirm the backup exists and is understandable to the human
- rerun the Git safety check after the backup step and before the destructive operation

**Important**
- backup is an allowed recovery path
- backup is not permission to skip explicit gate answers

---

## Sensing Delta Report example

**Expected JSON shape**

```json
{
  "delta_summary": {
    "timestamp": "2026-04-28T12:00:00Z",
    "pre_retrofit_state": {
      "entrypoints": ["app.py"],
      "config_files": ["requirements.txt"]
    },
    "post_retrofit_state": {
      "entrypoints": ["src/weather_service/main.py"],
      "config_files": ["pyproject.toml"]
    },
    "changes": [
      {
        "fact_key": "primary_entrypoint",
        "before": "app.py",
        "after": "src/weather_service/main.py",
        "operation": "MOVED"
      },
      {
        "fact_key": "dependency_config",
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

**Correct behavior**
- keep `before` and `after` human-readable
- use only `MOVED`, `CREATED`, `MODIFIED`, or `DELETED`
- make the report understandable as a single-view summary of the retrofit “surgery”

---

## Acceptance handoff is mandatory

**Correct behavior**
- once retrofit work and the Delta Report are complete, run:

```bash
python3 .github/skills/sense-env-scaffold/scripts/sense_env.py --mode acceptance --contract-file retrofit-plan.md
```

- if the command cannot run, stop and explain the missing prerequisite
- do not mark the retrofit complete on filesystem inspection alone

---

## Anti-pattern summary

| Anti-pattern | Why it fails |
| --- | --- |
| Start moving files before Gate 1 is resolved | Shadow conflicts require an explicit human decision |
| Auto-merge multiple config surfaces into one guessed toolchain | Conflicting config policy belongs to the human |
| Treat a dirty working tree as a warning only | Gate 3 is a hard block before destructive work |
| Skip the Delta Report because the diff is visible in Git | The skill requires a single-view before/after artifact |
| Claim success without the acceptance handoff | The retrofit loop is not closed until `sense_env.py --mode acceptance` runs |
