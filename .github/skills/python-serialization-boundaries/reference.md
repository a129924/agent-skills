# Python serialization-boundaries reference

Use this reference after `SKILL.md` narrows the task to semantic translation at
an API, database, or message boundary.

## Semantic gatekeeper framing

- A serialization boundary is where transport meaning becomes internal meaning,
  not just where bytes or JSON become Python objects.
- Raw payload shape is evidence of an external contract. It should stop at the
  boundary instead of leaking into business logic as long-lived `dict`/list
  structures.
- If internal logic still has to ask whether a value is a raw transport string,
  row field, or nested JSON fragment, boundary translation is incomplete.

## Hard rules

### 1. Raw shapes stop at the edge

- API bodies, database rows, and queue messages may arrive as `dict`, row
  mappings, strings, bytes, or SDK objects.
- The adapter that first owns that external contract also owns the translation
  point.
- Service and domain code should receive semantic values or named internal
  records, not raw transport containers by default.

### 2. Partial-update intent must survive translation

- PATCH-like input often needs three states: omitted, explicit `null`, and a new
  value.
- "Leave unchanged" is not the same as `None`.
- Prefer a sentinel-style concept for omission when `None` is a real business
  action.
- If the external contract cannot express the difference but business behavior
  depends on it, stop and ask instead of silently guessing.

### 3. Normalize semantic primitives before core logic

| Transport form | Internal meaning |
| --- | --- |
| UUID string | `UUID` |
| ISO timestamp string | timezone-aware `datetime` |
| numeric string / raw DB numeric | `Decimal` or other chosen money type |
| status code / enum-like text | internal symbolic value |

This skill decides **when** normalization must happen: at the boundary. It does
not choose whether the internal record should be a dataclass, enum, protocol, or
another construct family.

### 4. Convert deeply or stay honest about returning raw data

- If a function says it returns an internal object or typed record, nested lists,
  child objects, and embedded maps should be converted too.
- A shallow wrapper around raw nested payloads is still a transport leak.
- Returning a raw mapping can be acceptable, but the boundary should say so
  honestly instead of pretending the conversion is complete.

### 5. Input and output DTOs may be asymmetric

- Input DTOs capture caller intent.
- Output DTOs capture publication or transport contract.
- Responses and emitted messages may rename, redact, flatten, summarize, or omit
  fields.
- Lossy output is legitimate when the external contract requires it; round-trip
  symmetry is not a universal rule.

### 6. Keep schemas local unless contract ownership is truly shared

- Keep a boundary schema local when one adapter or one boundary owns it.
- Promote a schema to shared status only when multiple producers or consumers
  truly share the same wire meaning, versioning, and lifecycle.
- Matching field names or avoiding duplicate code is not enough reason to create
  a shared contract.

## Adjacent-skill handoff map

| Concern | Hand off to |
| --- | --- |
| strict annotation syntax, `Any`, ignore rules | `python-type-hints-strict` |
| dataclass / `Enum` / `ABC` / `Protocol` choice | `python-model-selection` |
| invalid-payload exception hierarchy or translation policy | `python-error-handling` |
| package gateways, `__all__`, import safety, deep imports | `python-module-boundaries` |
| package/distribution structure or retrofit/scaffold execution | `python-package-layout`, `python-project-init-greenfield`, `python-project-retrofit` |
| whole-library dependency direction or architecture slicing | future architecture-scope topics |

## Framework notes stay supplementary

- Framework helpers such as Pydantic unset tracking, ORM row adapters, or queue
  SDK message objects may help implement these rules.
- They do not replace the portable rule that semantics must be preserved at the
  boundary and raw payloads should not leak inward.
- Examples may mention framework mechanisms, but the skill's default guidance
  stays framework-neutral.
