# Framework Notes

These notes are supplemental. Start with the core Python decorator rules first,
then use this file only when the codebase clearly sits in one of these
ecosystems.

## Scope of these notes

- only developer-authored custom decorators
- only light framework alignment notes
- not framework-private internals
- not framework-specific lifecycle policy

## FastAPI

- Keep endpoint decorators transparent enough that framework introspection still
  sees the route callable clearly.
- Do not hide dependency/resource lifetime behind a custom decorator when the
  framework already has explicit dependency mechanisms.
- If a custom decorator adds auth, tracing, or narrow validation, keep the
  behavior explicit and preserve caller-visible typing.

## pytest

- Prefer fixtures and explicit pytest hooks for lifetime or environment setup.
- A custom decorator may still be acceptable for narrow test metadata or
  repeated call-time checks, but it should not become a hidden fixture system.
- Keep the decorated test function inspectable and easy to understand during
  review.

## Click

- Be careful not to fight Click's own signature and parameter expectations.
- Custom decorators should preserve readable command behavior and avoid smearing
  framework registration with unrelated hidden work.
- If the decorator mostly exists to register or configure Click behavior, keep
  the note short and do not expand into framework-internal guidance.

## Environment-sensing linkage

If another skill or environment-sensing step identifies FastAPI, pytest, Click,
or a similar framework, use these notes only as an additional constraint layer.
They do not override the core rules about transparent typing, explicit
behavior, or lifetime boundaries.
