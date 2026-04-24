# Reference Overview

This skill uses a split reference layer because decorator guidance spans several
distinct topics: signature integrity, behavior visibility, and light
framework-specific notes.

## Reference Files

| File | Role |
| --- | --- |
| `references/signature-integrity.md` | Transparent wrapper rules for `functools.wraps`, `ParamSpec`, `TypeVar`, `Callable[P, R]`, and signature-preservation anti-patterns |
| `references/behavior-visibility.md` | Explicitness rules for retries, caching, auth, side effects, error translation, and lifetime-boundary warnings |
| `references/framework-notes.md` | Light notes for developer-authored decorators in frameworks such as FastAPI, pytest, and Click |

## Navigation

- Start with `SKILL.md` for the main decision path.
- Use `references/signature-integrity.md` when the main question is whether a
  decorator stays transparent to callers.
- Use `references/behavior-visibility.md` when the decorator may hide side
  effects or lifetime-driven work.
- Use `references/framework-notes.md` only after the core Python rules are
  already satisfied.
- Use `examples.md` for the multi-path worked examples and anti-patterns.
