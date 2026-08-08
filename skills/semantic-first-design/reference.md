# Semantic-first decision reference

Use this reference to expose a material distinction, not to require a specific
design pattern. Start with the smallest representation that gives each
caller-visible meaning one clear interpretation.

## Decision prompts

| Area | Ask locally | Make visible when material | Route concrete choices to |
| --- | --- | --- | --- |
| Contract | What does success guarantee? | A return type or documented result that the implementation actually establishes | `python-api-signature`, `python-type-hints-strict` |
| Type and state | What guarantee did this operation add? | Distinct states such as parsed, validated, or prepared only when callers must rely on them | `python-model-selection`, `python-type-hints-strict` |
| Absence | Does absence have exactly one normal meaning? | A separate result or error path when missing, invalid, skipped, unavailable, and failed differ | `python-api-signature`, `python-error-handling` |
| Boolean and policy | Is this naturally yes/no? | A named policy or operation when a flag hides behavior choices or a third choice is credible | `python-api-signature`, `python-model-selection` |
| Boundary | Which external semantics are leaking inward? | A translation that exposes the application's stable contract, rather than vendor flags or weak results | `python-error-handling`, `python-library-architecture` |
| Composition | What implementation is selected and where? | Important components and choices at a visible composition point | `python-library-architecture` |
| Abstraction | What independent variation or invalid state does it remove? | An abstraction only for a real boundary, variation axis, or guarantee | `python-model-selection`, `python-library-architecture` |
| Failure | Could failure be mistaken for valid absence or success? | An explicit failure representation that preserves the relevant cause and contract | `python-error-handling` |

## Resolution rules

1. Name the ambiguity before proposing a remedy. “Use an enum” is not a
   diagnosis; “the flag currently selects three delivery behaviors” is.
2. Preserve a simple primitive, boolean, or optional value when it has one
   natural, local meaning. Semantic-first design is not type maximalism.
3. A successful operation may earn a stronger state guarantee. Reveal it only
   if callers need to distinguish that guarantee from the prior state.
4. Treat normal absence and operational failure as different unless their
   equivalence is intentional, stable, and apparent from the contract.
5. Translate an external system at the boundary. Higher-level code should not
   need vendor-specific conventions to understand normal behavior.
6. Keep composition and orchestration visible when they answer “what is used?”
   and “what happens next?” Do not hide meaningful choices behind magic
   discovery merely to reduce wiring.
7. Extract an abstraction only for an independently varying behavior or a real
   boundary. Do not add fake workflow steps, generic dependency bags, or an
   interface per function to make shapes look uniform.

## Review result format

Return the smallest useful statement:

```text
Ambiguity: <one material ambiguity>
Distinction: <the explicit name/type/result/policy/boundary to introduce>
Guarantee: <what a caller can now know locally>
Route: <specialised skill, or none when this is only cross-cutting guidance>
```

If the relevant meanings cannot be determined, use `INCOMPLETE`. If choosing
between plausible meanings would alter a public contract, valid state, failure
semantics, or architecture boundary, use `BLOCKED` rather than guessing.

## Non-goals

- Do not reopen a locked architecture, path, or contract decision.
- Do not duplicate specialised-skill instructions; this reference only routes
  to their existing ownership.
- Do not trade local reasoning for more classes, configuration, or indirection.
