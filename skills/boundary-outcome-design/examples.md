# Boundary Outcome Design Examples

## 1. Adapter translation with selective preservation

**Situation:** An external client raises timeout, service-unavailable, and
rate-limit errors. The UseCase retries timeout and service-unavailable in the
same way, but schedules rate-limited work from server-provided retry metadata.

```text
Observed boundary:
Adapter implementing an Application-owned outbound Port.

Potential vocabulary leak:
SdkTimeoutError and HTTP 503 would leak client/transport vocabulary through the Port.

Decision-relevant distinctions:
- timeout/service unavailable: same retry decision
- rate limited: retry scheduling needs retry metadata

Suggested translation point:
Adapter, while mapping the external client response/error.

Suggested outcome granularity:
DependencyUnavailable; RateLimited(retry metadata); successful capability result.

Boundary action:
Translate; compress timeout/service-unavailable; preserve rate-limit distinction.
```

Do not infer that every HTTP status needs its own Port outcome. The examples are
semantic roles, not required type names.

## 2. UseCase compression after a detailed Port contract

**Situation:** A shared Port distinguishes `DependencyTimeout` from
`DependencyUnavailable` for one consumer. A checkout UseCase has the same
temporary-unavailable handling for both.

```text
Observed boundary:
Checkout UseCase operation result.

Potential vocabulary leak:
None; both Port outcomes are capability vocabulary, but they exceed this operation's needs.

Decision-relevant distinctions:
- timeout/unavailable: identical fallback and user message

Suggested translation point:
Checkout UseCase when interpreting the Port result.

Suggested outcome granularity:
TemporarilyUnavailable; operation success; other operation-specific results.

Boundary action:
Compress.
```

The Port and UseCase do not need the same type or number of alternatives.

## 3. Optional Domain state becomes an operation failure

**Situation:** A `Subject` may legally have no `optional_value`; an export
operation requires one.

```text
Observed boundary:
Application operation interpreting valid Domain state.

Potential vocabulary leak:
None.

Decision-relevant distinctions:
- value absent: export must reject with an operation-specific result
- value present: proceed with export

Suggested translation point:
UseCase after obtaining Subject state, not Adapter retrieval.

Suggested outcome granularity:
Exported; ValueRequired.

Boundary action:
Preserve valid Domain state; translate it to an operation result only for export.
```

**Incorrect reasoning:** `optional_value: Value | None` means `Subject` is
invalid, so the Adapter must return an error whenever it sees `None`.

## 4. Repository and Unit of Work

**Situation:** `find()` can have a normal lookup miss; `commit()` can report a
write conflict. The ORM may also raise an unexpected driver failure during
either operation.

```text
Observed boundary:
Repository lookup and Unit of Work transaction completion are separate boundaries.

Potential vocabulary leak:
Leaking the ORM's concrete conflict or driver exception into Application.

Decision-relevant distinctions:
- lookup miss: normal application absence path
- write conflict: caller may refresh, retry, or report conflict
- unexpected driver failure: no defined local recovery decision

Suggested translation point:
Repository for lookup capability; Unit of Work for transaction completion.

Suggested outcome granularity:
Entity | absence at lookup; Committed | Conflict at commit; unexpected failure stays controlled propagation.

Boundary action:
Preserve normal absence and transaction conflict; leave unexpected driver failure as unexpected exception.
```

**Incorrect reasoning:** All database failures must be `CommitOutcome`, or a
`Session(Protocol)` return signature means the ORM cannot fail at runtime.

## 5. Over-compression and exception mirroring

**Over-compression:** Replacing `NotFound`, `Conflict`, and
`TemporarilyUnavailable` with `Failed` is wrong when callers respectively show
absence, ask for conflict resolution, and retry.

**One-to-one mirroring:** Replacing `Sdk429Error`, `Sdk503Error`, and
`SdkTimeoutError` with identically named Outcome classes is not translation if
the caller still sees only SDK facts and no new semantic decision is described.

**Appropriate promotion:** If a corrupted invariant reaches an Application
boundary, do not add `CorruptedInvariant` to every normal result union merely
for completeness. Recommend the controlled application-safe exception/global
handler path and identify it as unexpected.
