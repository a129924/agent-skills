# Blueprint Review Checks

Use this reference when reviewing an authored greenfield `blueprint.md`.

This reviewer is `blueprint-text first`. It does not enforce a locked heading
schema. It enforces whether the authored design baseline is concrete,
internally consistent, and verifiable enough to execute without downstream
guessing.

## Required review dimensions

The blueprint must cover these dimensions clearly, regardless of section names
or ordering:

1. purpose or project overview
2. capability requirements
3. toolchain expectation
4. structure, locators, or invariants
5. quality thresholds
6. acceptance or verification shape

Review should fail when:
- a required dimension is missing
- a dimension exists only as vague prose or placeholders
- the blueprint relies on template headings while omitting implementation-critical details

## Acceptance and verification rules

- acceptance criteria are mandatory
- observable or verifiable outcomes are required
- prose, lists, tables, or machine-readable blocks are all acceptable if they are concrete
- subjective goals such as `clean`, `production-ready`, or `good defaults` are not enough by themselves
- malformed verification language is blocking when the downstream implementer would need to invent the real acceptance criteria

## Human-readable section interpretation

Preferred forms include:

- `- Key: Value`
- `- Capability: concrete requirement`
- `- Verification: observable outcome`

Review notes:
- explanatory prose is allowed when it adds clarity
- authors may organize the blueprint differently from the common template
- headings or formatting style are not the contract; concrete design content is the contract

## Contract-breaking review outcomes

Return `needs-rework` when the blueprint:
- omits one of the required design dimensions
- leaves capability requirements too abstract to implement safely
- uses contradictory or non-locatable structure claims
- defines acceptance only as aspiration or taste
- includes retrofit or migration work while claiming to be greenfield
