# Strict typing reference

## Baseline
- Treat `pyright --strict` as the default compatibility target.
- Annotate public function and method parameters and return values.
- Use PEP 604 unions such as `User | None`.
- Use built-in generics such as `list[str]` and `dict[str, int]`.
- Introduce `TypeAlias` for repeated or complex types.
- Annotate empty collections and mutable attributes when inference would be ambiguous.

## Preferred patterns
- Use `Literal` for small closed string choices.
- Narrow types with explicit checks before branching.
- Keep return types stable; prefer one clear output shape per function.

## Restricted escape hatches
- `Any`: only at dynamic boundaries or third-party edges; convert to precise types quickly.
- `cast(...)`: only after a runtime guarantee or trusted narrowing step.
- Ignore comments: only for isolated tool limitations, with the smallest possible scope and a justification note.
- Avoid file-wide suppression when a local fix is possible.

## Avoid
- Untyped public APIs.
- Legacy spellings like `Optional[X]`, `Union[A, B]`, `List[X]`, or `Dict[K, V]` when modern syntax works.
- Routine `cast` or ignore comments as a replacement for modeling the type correctly.
- Return signatures that bounce between unrelated types.
