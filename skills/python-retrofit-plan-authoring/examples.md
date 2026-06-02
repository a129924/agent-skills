# Python Retrofit Plan Authoring Examples

Detailed examples for `python-retrofit-plan-authoring`.

---

## Happy path: LOW-risk additive retrofit contract

**Input facts**
- current package: `weather_service/`
- current entrypoint: `weather_service/cli.py`
- current config: `requirements.txt`
- requested additions: `pyproject.toml`, `tests/`, and explicit acceptance checks

**Correct Retrofit V2 contract shape**

~~~markdown
## Survey Summary
- current package: weather_service/
- current entrypoint: weather_service/cli.py
- current config: requirements.txt

## Gap Analysis
- missing path: tests/
- missing config: pyproject.toml
- current requirements.txt should remain as legacy context during transition

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
- Migration Direction: additive baseline reinforcement

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

**Why this is correct**
- the plan uses the locked V2 section order
- `LOW` is justified because the contract is additive and non-destructive
- `Migration Direction` declares strategy only; it does not choose runtime gates

---

## High-risk contract with concrete destructive preview data

**Input facts**
- current entrypoint: `app.py`
- current package root: `inventory/`
- current config: `requirements.txt`, `setup.cfg`
- requested target: `src/inventory_service/main.py` with `pyproject.toml`

**Correct Retrofit V2 contract shape**

~~~markdown
## Survey Summary
- current entrypoint: app.py
- current package root: inventory/
- current config files: requirements.txt, setup.cfg

## Gap Analysis
- current code is not under src/
- target entrypoint conflicts semantically with app.py
- config will change from legacy files to pyproject.toml

## Target Transformation
- target path: src/inventory_service/
- target entrypoint: src/inventory_service/main.py
- target config: pyproject.toml
- Migration Direction: restructure into src package with one governed toolchain surface

## Migration Strategy
```yaml [migration-strategy]
risk_level: HIGH
destructive_actions:
  - move app.py -> src/inventory_service/main.py
  - relocate inventory/ -> src/inventory_service/
  - replace requirements.txt + setup.cfg with pyproject.toml
backup_required: true
```
- runtime gate outcomes remain human-owned during execution

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

**Why this is correct**
- the destructive surfaces are concrete and previewable
- `HIGH` matches observable directory reshaping and toolchain replacement
- the plan does not pre-authorize delete, move, or overwrite at runtime

---

## Stop-and-ask: target transformation is too abstract

This request is not authorable yet:

```text
Modernize the project layout, clean up old files, and switch to a better toolchain.
```

**Correct behavior**
- stop before drafting `retrofit-plan.md`
- ask for concrete paths, concrete surviving files, named toolchain targets, and verifiable acceptance outcomes
- avoid filling `destructive_actions` with guesses such as “probably move app.py somewhere under src/”

**Anti-pattern**

```text
Wrong: invent `src/app/main.py`, mark the risk `LOW`, and assume the executor can work out the rest.
```

---

## Stop-and-fix: risk-level mismatch during authoring

This draft is invalid:

~~~markdown
## Migration Strategy
```yaml [migration-strategy]
risk_level: LOW
destructive_actions:
  - move app.py -> src/weather_service/main.py
backup_required: false
```
~~~

**Correct behavior**
- correct the contract before handoff
- use `HIGH` because the plan includes code relocation
- make `backup_required` align with the destructive strategy
- do not leave the mismatch for the executor to discover first

---

## Lane mismatch: greenfield request should not become retrofit authoring

**Request**

```text
Create the first Python project structure for this empty repository and include acceptance checks.
```

**Correct behavior**
- stop retrofit authoring
- route to `python-project-init-greenfield`
- do not fabricate a retrofit `Survey Summary` for a repository with no meaningful current state

---

## Anti-pattern summary

| Anti-pattern | Why it fails |
| --- | --- |
| Use old headings such as `## Project Overview` | Retrofit V2 has a locked section order with no compatibility layer |
| Leave `destructive_actions` vague | Executor cannot produce a reliable destructive preview or alignment check |
| Treat `Migration Direction` as runtime consent | Runtime gate outcomes stay human-owned during execution |
| Mark directory reshaping as `LOW` | Risk must follow observable physical traits |
| Draft a plan without concrete paths or tool names | `contract 太抽象` is a stop-and-ask condition |
