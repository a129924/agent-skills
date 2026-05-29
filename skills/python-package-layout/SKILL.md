---
name: python-package-layout
description: Design or review conservative Python package layouts with `src/`, `pyproject.toml`, clear library-vs-CLI placement, and tests that exercise packaged code rather than local-path accidents.
complexity: medium
risk_profile:
  - ambiguity_sensitive
inputs:
  - package shape: library-only, CLI-enabled, or both
  - import package name and any differing distribution name
  - package-data or optional-extra requirements
  - preferred test location relative to packaged code
  - whether the repository currently relies on flat-root execution or ad-hoc scripts
outputs:
  - a package-layout rule set or design recommendation
  - placement rules for `src/`, tests, CLI entrypoints, package data, and extras
use_when:
  - designing or reviewing the directory layout of a reusable Python package
  - deciding whether code belongs under `src/<package_name>/`, `tests/`, a CLI module, or a non-package script
  - deciding how `pyproject.toml` should anchor package metadata, entry points, package data, and extras
  - repairing a package layout that works only because local execution happens from the repo root
do_not_use_when:
  - the main question is public export policy, `__all__`, or deep-import rules
  - the main question is internal architecture slicing, dependency direction, or shared-contract placement
  - the task is end-to-end project bootstrap or retrofit execution
  - the preferred path is a namespace-package or no-`__init__.py` design
---

# Purpose
Choose a clear, distributable layout for an ordinary Python package without drifting into architecture policy or project-bootstrap workflow.

# Trigger / When to use
Use this skill when:
- designing or reviewing the directory layout of a reusable Python package
- deciding whether code belongs under `src/<package_name>/`, `tests/`, a CLI module, or a non-package script
- deciding how `pyproject.toml` should anchor package metadata, entry points, package data, and extras
- repairing a package layout that works only because local execution happens from the repo root

Do not use this skill when:
- the main question is public export policy, `__all__`, or deep-import rules
- the main question is internal architecture slicing, dependency direction, or shared-contract placement
- the task is end-to-end project bootstrap or retrofit execution
- the preferred path is a namespace-package or no-`__init__.py` design

# Inputs
- package shape: library-only, CLI-enabled, or both
- import package name and any differing distribution name
- package-data or optional-extra requirements
- preferred test location relative to packaged code
- whether the repository currently relies on flat-root execution or ad-hoc scripts

# Process
1. Confirm the task is about package/distribution structure for a regular package, not about architecture, modeling, or workflow execution.
2. Default to a `src/` layout for reusable or distributable packages, and put importable code under `src/<package_name>/` with `__init__.py`.
3. Use `pyproject.toml` as the packaging anchor for project metadata, dependencies, extras, entry points, and package-data settings.
4. Keep reusable library logic inside the package. Keep CLI launchers and ad-hoc scripts thin consumers; if the package exposes a CLI, route it through a console script and/or `__main__.py` that delegates to package code.
5. Put tests outside `src/`, usually under `tests/`, and make them import the packaged code through normal package paths instead of relying on repo-root import accidents.
6. Treat package data and extras as packaging decisions. Keep shipped data near the package and declare it from `pyproject.toml`; keep extras for optional install-time capabilities rather than as a substitute for package structure.
7. If the question shifts to public import gateways, API composition, or repository transformation workflow, hand off instead of widening this skill.

# Outputs
- a package-layout rule set or design recommendation
- default placement rules for source packages, tests, CLI entrypoints, package data, and extras
- branching guidance for library-only, CLI-enabled, and mixed packages

# Validation
Before proceeding, confirm:
- importable code lives under `src/<package_name>/` for the ordinary-package default
- `pyproject.toml` is the single packaging anchor for metadata, entry points, extras, and package-data declarations
- reusable logic is not trapped in scripts or `__main__.py`
- tests do not depend on repo-root import accidents

# Boundaries
- Do not define public export policy, `__all__`, or deep-import rules.
- Do not define architecture slicing, bounded contexts, or facade/client composition.
- Do not choose `Enum`, `dataclass`, `ABC`, or `Protocol`.
- Do not define exception hierarchy or translation rules.
- Do not turn this into a scaffold or retrofit workflow.

