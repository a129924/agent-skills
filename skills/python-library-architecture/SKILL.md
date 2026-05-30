---
name: python-library-architecture
description: Design or review reusable Python library/package architecture with theme isolation, a side-effect-free `core`, and facade/client composition for multi-theme libraries and SDK-style packages.
complexity: medium
risk_profile:
  - ambiguity_sensitive
inputs:
  - consumer-facing capabilities of the reusable library or SDK
  - proposed themes or capability slices inside one package
  - contracts shared across themes or external boundaries
  - adapters or integrations that touch transport, storage, or vendor APIs
  - intended public facade or client entry points
  - current dependency smells such as peer imports or a growing `common/`
outputs:
  - a library-architecture rule set or design recommendation
  - an explicit dependency-direction model for themes, `core`, adapters, and facade/client entry points
  - refactor guidance for cross-theme coupling, `core` misuse, and composition-root cleanup
use_when:
  - designing or reviewing the internal architecture of a reusable Python library or SDK-style package
  - deciding where themes, shared contracts, adapters, and the public facade/client should live
  - refactoring a coupled package that has cross-theme imports, a bloated `common/`, or orchestration in the wrong layer
do_not_use_when:
  - the main task is package/distribution layout, `src/`, or `pyproject.toml`
  - the main task is module export policy, `__all__`, or deep-import rules
  - the main task is type-hint syntax, model-construct choice, serialization translation, or error policy
  - the main task is service/application architecture, framework layering, or plugin design
---

# Purpose
Choose clean internal architecture for reusable Python libraries and SDK-style packages so themes stay isolated, shared contracts live in `core`, and consumers enter through a clear facade/client.

# Trigger / When to use
Use this skill when:
- designing or reviewing the internal architecture of a reusable Python library or SDK-style package
- deciding where themes, shared contracts, adapters, and the public facade/client should live
- refactoring a coupled package that has cross-theme imports, a bloated `common/`, or orchestration in the wrong layer

Do not use this skill when:
- the main task is package/distribution layout, `src/`, or `pyproject.toml`
- the main task is module export policy, `__all__`, or deep-import rules
- the main task is type-hint syntax, model-construct choice, serialization translation, or error policy
- the main task is service/application architecture, framework layering, or plugin design

# Inputs
- consumer-facing capabilities of the reusable library or SDK
- proposed themes or capability slices inside one package
- contracts shared across themes or external boundaries
- adapters or integrations that touch transport, storage, or vendor APIs
- intended public facade or client entry points
- current dependency smells such as peer imports or a growing `common/`

# Process
1. Confirm the task is library/package architecture only. If it is mainly about package layout, module gateways, typing syntax, model choice, serialization rules, error policy, or app/service architecture, hand off instead of widening scope.
2. Slice the library into themes that own one capability family each. Keep collaboration inside a theme by default.
3. Use `core/` as the shared contract center for multi-theme libraries. Allow a semantically explicit alternative such as `kernel/` or `base/` only if it plays the same role; do not use vague substitutes such as `common/` or `utils/`.
4. Enforce a zero-exception cross-theme import ban. If two themes need the same contract, semantic primitive, or boundary-crossing abstraction, promote it into `core` instead of importing peer-to-peer.
5. Keep `core` side-effect-free and non-orchestrating. Put shared contracts, semantic value types, shared base errors, and pure support logic there; keep I/O, retries, auth refresh flows, client bootstrap, and other outward orchestration out of `core`.
6. Make the public facade/client the recommended composition root. Prefer one primary consumer-facing entry point; allow bounded secondary entry points only when they remain orchestration-only and do not become alternate architecture lanes.
7. Keep dependency direction explicit: facade/client and entry points may compose themes and adapters; adapters may depend on their owning theme and `core`; themes may depend on `core`; `core` must not depend outward.

# Outputs
- a library-architecture rule set or design recommendation
- an explicit dependency-direction model for themes, `core`, adapters, and facade/client entry points
- refactor guidance for cross-theme coupling, `core` misuse, and composition-root cleanup

# Validation
Before proceeding, confirm:
- no theme imports another theme, with zero exceptions
- `core` is the shared contract center and stays side-effect-free
- shared contracts that cross themes or external boundaries are promoted into `core`
- facade/client entry points compose themes and adapters instead of pushing orchestration down into `core`

# Boundaries
- Do not define physical package/distribution layout.
- Do not define package gateways, `__all__`, deep-import policy, or internal-module contracts.
- Do not define type-hint syntax or strict-typing escape hatches.
- Do not choose between `Enum`, `dataclass`, `ABC`, or `Protocol`.
- Do not widen into service/application architecture, framework-specific layering, or plugin systems.

# Local references
- `examples.md`: positive and negative theme-isolation, `core`, and facade/client composition scenarios
