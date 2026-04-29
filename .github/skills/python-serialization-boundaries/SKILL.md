---
name: python-serialization-boundaries
description: Design or review Python serialization boundaries as semantic translation gates for API, database, and message payloads.
---

# Purpose
Choose clear semantic translation rules for data crossing API, database, and
message-queue boundaries so raw transport shapes stop early and internal logic
works with normalized meaning instead of leaked payload structure.

# Trigger / When to use
Use this skill when:
- designing or reviewing how API payloads, database rows, or queue messages
  enter Python code
- deciding where raw `dict` / JSON / row / message shapes should become
  internal objects, records, or semantic values
- PATCH-like updates must distinguish omitted, explicit `null`, and unchanged
  intent
- deciding whether input and output DTOs should differ, or whether output may
  be intentionally lossy
- deciding whether a boundary schema should stay local or become a shared
  external contract

Do not use this skill when:
- the task is mainly a `json.dumps` / `json.loads` tutorial or framework/schema
  library selection question
- the task is mainly about choosing dataclass, `Enum`, `ABC`, or `Protocol`;
  use `python-model-selection`
- the task is mainly about exception hierarchy or translation; use
  `python-error-handling`
- the task is mainly about package gateways, imports, or public export policy;
  use `python-module-boundaries`
- the task is mainly about package/distribution layout or scaffold/retrofit
  execution; use `python-package-layout`, `python-project-init-greenfield`, or
  `python-project-retrofit`
- the task is mainly about broad architecture, dependency direction, ORM/query
  design, or infrastructure setup

# Inputs
- the boundary kind: API request/response, database row, queue message, or
  another transport contract
- whether the data is inbound, outbound, or PATCH-like partial input
- which fields must preserve omitted vs explicit `null` vs unchanged meaning
- which primitives need normalization, such as UUID, datetime, decimal, or
  enum-like transport values
- whether nested objects or collections must be converted deeply
- whether the output contract is intentionally lossy or non-round-trip
- whether the schema is local to one boundary or truly shared across callers or
  services

# Process
1. Confirm the task is about semantic boundary translation, not generic format
   conversion or tool selection.
2. Treat raw transport shapes as temporary. Convert them at the boundary before
   business logic, instead of letting services or entities consume raw
   `dict`/list payloads.
3. Separate inbound and outbound semantics. For PATCH-like inputs, preserve
   omitted, explicit `null`, and unchanged intent separately; use a neutral
   sentinel-style framing when `None` is a real business value.
4. Normalize transport primitives to internal semantic values at the boundary,
   such as `str` -> `UUID`, ISO timestamp string -> timezone-aware
   `datetime`, numeric string -> `Decimal`, or transport code -> internal
   symbolic value.
5. If the boundary claims to return an internal object or typed record, convert
   nested collections and child objects deeply; do not hide raw nested payloads
   inside a shallow wrapper.
6. Allow input DTOs and output DTOs to differ when their meanings differ. Do
   not force round-trip symmetry when outbound contracts need summary,
   redaction, or compatibility shaping.
7. Keep boundary schemas local by default. Promote them to a shared external
   contract only when multiple producers/consumers truly share the same wire
   semantics and lifecycle.
8. Stop and hand off when the remaining question is mainly about type-hint
   syntax, model construct choice, exception policy, module/package structure,
   or broader library architecture.

# Examples
- Positive: Parse a PATCH payload into an internal update object that preserves
  omitted versus explicit `None`, normalize `user_id` to `UUID` and
  `expires_at` to timezone-aware `datetime`, and emit a response DTO that omits
  internal audit fields.
- Negative: Pass raw request `dict`s through service methods, let `None` mean
  both "field not sent" and "clear the field", keep nested raw lists of `dict`,
  or insist the response must mirror the input shape because both are JSON.

# Outputs
- a review-ready rule set or design recommendation for semantic serialization
  boundaries
- defaults for inbound/outbound DTO separation, missing/null handling, type
  normalization, deep conversion, and local-vs-shared schema ownership
- local reference and branching examples for common boundary choices and
  anti-patterns

# Boundaries
This skill defines semantic translation rules at API, database, and message
boundaries. It does not cover:

- Type-hint syntax and strict typing rules →
  `python-type-hints-strict`
- Choosing dataclass, `Enum`, `ABC`, or `Protocol` →
  `python-model-selection`
- Exception hierarchy and invalid-payload translation → `python-error-handling`
- Package gateways, `__all__`, and import policy →
  `python-module-boundaries`
- Package/distribution layout and scaffold/retrofit execution →
  `python-package-layout`, `python-project-init-greenfield`,
  `python-project-retrofit`
- Whole-library dependency direction and architecture slicing → future
  architecture-scope topics

# Local references
- `reference.md`: semantic-gatekeeper framing, hard rules, adjacent-skill
  handoff map, and framework notes; also includes verification criteria, red
  flags, and common rationalizations to support review
- `examples.md`: branching examples for PATCH semantics, asymmetric DTOs, type
  normalization, deep conversion, lossy output, and local-vs-shared schema
  choices
