# Python Project Retrofit Examples

Detailed examples for `python-project-retrofit`.

---

## LOW path: additive Retrofit V2 execution

**Input retrofit plan shape**

~~~markdown
## Survey Summary
- current package: weather_service/
- current entrypoint: weather_service/cli.py
- current config: requirements.txt

## Gap Analysis
- tests/ is missing
- pyproject.toml is missing

## Target Transformation
- retain entrypoint: weather_service/cli.py
- add path: tests/
- add file: pyproject.toml

## Migration Strategy
```yaml [migration-strategy]
risk_level: LOW
destructive_actions: []
backup_required: false
```

## Acceptance Criteria
```yaml [sensing-assertions]
- kind: path_exists
  target: pyproject.toml
  expected: "true"
- kind: path_exists
  target: tests
  expected: "true"
```
~~~

**Observed workspace**
- `weather_service/cli.py` already exists
- `requirements.txt` exists and will remain during the transition
- no destructive move, delete, or overwrite is required

**Correct behavior**
1. parse the V2 headings and both machine-readable blocks
2. pass the Risk Alignment Check because the runtime scan stays non-destructive
3. use the lightweight `LOW` confirmation path
4. add only the missing governed surfaces
5. generate the Sensing Delta Report
6. hand off to `python3 .codex/skills/sense-env-scaffold/scripts/sense_env.py --mode acceptance --contract-file retrofit-plan.md`

---

## HIGH path: destructive preview and explicit authorization

**Input retrofit plan shape**

~~~markdown
## Survey Summary
- current entrypoint: app.py
- current package root: inventory/
- current config files: requirements.txt, setup.cfg

## Gap Analysis
- target entrypoint conflicts semantically with app.py
- target package root requires relocation into src/
- target toolchain consolidates config into pyproject.toml

## Target Transformation
- target path: src/inventory_service/
- target entrypoint: src/inventory_service/main.py
- target config: pyproject.toml
- Migration Direction: staged package relocation with one governed toolchain surface

## Migration Strategy
```yaml [migration-strategy]
risk_level: HIGH
destructive_actions:
  - move app.py -> src/inventory_service/main.py
  - relocate inventory/ -> src/inventory_service/
  - replace requirements.txt + setup.cfg with pyproject.toml
backup_required: true
```

## Acceptance Criteria
```yaml [sensing-assertions]
- kind: path_exists
  target: src/inventory_service/main.py
  expected: "true"
- kind: path_exists
  target: pyproject.toml
  expected: "true"
```
~~~

**Observed workspace**
- root `app.py` exists
- `inventory/` exists at the repository root
- `requirements.txt` and `setup.cfg` exist
- Git working tree is clean

**Correct behavior**
1. parse the V2 contract and read `risk_level: HIGH`
2. run Gate 1 for the `app.py` shadow conflict
3. run Gate 2 for the legacy config remnants
4. generate a destructive preview from `destructive_actions` plus the current scan
5. require explicit human authorization before any destructive step
6. run Gate 3 immediately before the approved move, delete, or overwrite
7. apply only the approved operations
8. generate the Sensing Delta Report and hand off to acceptance

---

## Risk Alignment Check: mislabeled LOW plan must hard-block

**Invalid plan fragment**

~~~markdown
## Migration Strategy
```yaml [migration-strategy]
risk_level: LOW
destructive_actions: []
backup_required: false
```
~~~

**Observed workspace**
- root `app.py` exists
- target transformation requires `src/weather_service/main.py`
- execution would need a move, delete, or coexistence decision

**Correct behavior**
- hard-block before execution continues
- explain that the declared `LOW` risk conflicts with destructive or conflict-bearing runtime facts
- require plan correction instead of silently escalating the risk in place

**Anti-pattern**

```text
Wrong: silently continue with Gate 1 and treat the plan as HIGH without correcting the contract mismatch.
```

---

## Migration Direction is not a runtime shortcut

**Plan note**

```text
Migration Direction: replace root entrypoint with package entrypoint after relocation
```

**Observed workspace**
- `app.py` still exists at runtime

**Correct behavior**
- still present Gate 1 choices: `move | delete | coexist | abort`
- treat the plan note as strategic intent only
- do not skip the human choice because the plan prefers replacement

---

## Dirty Git state remains a hard block for destructive work

**Situation**
- the plan is `HIGH`
- the human already approved the destructive preview
- `git status --short` shows modified files

**Correct behavior**
- stop before the destructive step
- require a human-approved recovery path: commit current changes or create a backup
- rerun the pre-destructive safety check after that recovery path is ready

---

## Acceptance handoff is still mandatory

**Correct behavior**
- once retrofit work and the Sensing Delta Report are complete, run:

```bash
python3 .codex/skills/sense-env-scaffold/scripts/sense_env.py --mode acceptance --contract-file retrofit-plan.md
```

- if the command cannot run, stop and explain the missing prerequisite
- do not mark the retrofit complete on filesystem inspection alone

---

## Anti-pattern summary

| Anti-pattern | Why it fails |
| --- | --- |
| Accept old Retrofit headings or missing `[migration-strategy]` | Executor must consume the locked V2 contract without compatibility mapping |
| Treat `LOW` as a soft hint even when runtime scanning finds destructive actions | Risk Alignment Check is a hard block |
| Skip destructive preview because the plan already implies the result | HIGH-risk execution still needs explicit human authorization |
| Let `Migration Direction` choose Gate 1 or Gate 2 outcomes | Strategy declaration does not replace runtime gates |
| Claim success without the acceptance handoff | The retrofit loop is not closed until `sense_env.py --mode acceptance` runs |
