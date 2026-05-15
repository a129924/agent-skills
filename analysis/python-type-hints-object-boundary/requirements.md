# Requirements Baseline: python-type-hints-object-boundary

> Status: **FROZEN** — ready for `business-to-technical-translation`.
> Frozen by: business-intent-alignment session (2026-05-15).
> All named contradictions have been resolved into explicit rules.

---

## Problem Statement (Business Terms)

The existing `python-type-hints-strict` skill already restricts `Any`,
`cast(...)`, and ignore comments, but it does not directly guard against a
different failure mode: an authoring agent weakens an already-known domain
contract to `object` because `object` feels safer than preserving or refining
the real type.

This weakens repository-owned APIs, hides domain meaning from maintainers, and
turns strict typing guidance into a conservative escape hatch instead of a
contract-preserving rule set.

A refined baseline is needed so the skill clearly distinguishes:

- `object` as a narrowly valid entry type at true untrusted boundaries, and
- `object` as an invalid replacement for a known repo-owned alias, value type,
  model, protocol, or other concrete domain contract.

---

## Actors and Permission Boundaries

| Actor | Role |
| --- | --- |
| Python developer | Uses the skill to decide whether a type annotation is acceptable under `pyright --strict` |
| Creator agent | Drafts or revises `.github/skills/python-type-hints-strict/` |
| Reviewer / maintainer | Verifies the skill preserves domain contracts and does not permit convenience-driven weakening to `object` |
| Copilot / implementation agent | Applies the skill during code generation or review and must follow the stricter `object` decision rules |

---

## In-Scope Requirements

### R1 — Hard prohibition on weakening known domain contracts to `object`

- **Actor**: Copilot / implementation agent or Python developer applying strict
  typing guidance
- **Condition**: A repo-owned alias, value type, model, protocol, or other
  concrete domain type already exists for the position being annotated
- **Observable result**: The skill treats changing that position to `object` as
  invalid unless the position is a true untrusted boundary or a
  narrowing-helper input
- **Metric / decision rule**: Reviewer can verify from `SKILL.md`,
  `reference.md`, and `examples.md` that `object` is rejected for ordinary
  parameters, returns, service-layer APIs, and repo-owned contracts when a
  stronger type already exists
- **Failure meaning**: Existing domain guarantees disappear from the code
  contract, making review harder and future refinement less likely

### R2 — Narrow definition of allowed `object` positions

- **Actor**: Python developer or Copilot using the skill at dynamic entry points
- **Condition**: A value enters from a true untrusted boundary such as decoder
  output, validator input, or a type-guard / narrowing helper input
- **Observable result**: The skill permits `object` only at that boundary and
  requires immediate narrowing back to a precise type before normal business use
- **Metric / decision rule**: The allowed examples are explicitly named and stay
  limited to untrusted-boundary or narrowing-helper entry points; the rule does
  not expand to ordinary public API signatures or return types
- **Failure meaning**: `object` spreads into normal application contracts and
  becomes indistinguishable from a convenience fallback

### R3 — Justification requirement for every remaining `object` usage

- **Actor**: Creator agent or Python developer authoring strict typing guidance
- **Condition**: A surviving `object` annotation remains after applying the rule
  set
- **Observable result**: The usage includes a short justification that names the
  boundary or narrowing role it serves
- **Metric / decision rule**: Reviewer can reject any remaining `object` usage
  whose only rationale is convenience, uncertainty, or avoiding domain-model
  understanding
- **Failure meaning**: The skill preserves `object` without a reviewable reason,
  recreating the same conservative collapse in a less explicit form

### R4 — Preference order must favor repo-owned or refined explicit types

- **Actor**: Copilot / implementation agent choosing a type annotation
- **Condition**: The codebase already has a reusable alias/value type, or the
  contract can be represented by a clearer explicit type instead of `object`
- **Observable result**: The skill tells the agent to reuse the repo-owned type
  first, or create/refine an explicit type when needed, before considering
  `object`
- **Metric / decision rule**: The skill's decision path is reviewable as
  `repo-owned type -> explicit refinement -> boundary-only object`, never
  `object first`
- **Failure meaning**: Repo-owned domain modeling erodes over time because `object`
  is easier than preserving the real contract

### R5 — Scope must remain strict-typing guidance, not model selection

- **Actor**: Creator agent revising `python-type-hints-strict`
- **Condition**: The `object` problem suggests introducing or changing concrete
  runtime models such as `Enum`, `dataclass`, `ABC`, or `Protocol`
- **Observable result**: The skill keeps its existing boundary and redirects such
  model-shape decisions to `python-model-selection`
- **Metric / decision rule**: The updated skill strengthens type-hint policy
  without taking ownership of runtime model selection
- **Failure meaning**: The skill becomes broader and less reliable because it
  mixes syntax/policy guidance with separate modeling decisions

### R6 — Positive and negative examples must make the rule executable

- **Actor**: Reviewer / maintainer validating the revised skill
- **Condition**: The skill draft claims to distinguish valid and invalid `object`
  usage
- **Observable result**: The artifact set includes at least one concise positive
  example where `object` is allowed at a narrowing/helper boundary and at least
  one negative example where a known domain type is incorrectly weakened to
  `object`
- **Metric / decision rule**: A reviewer can verify the valid/invalid line
  without guessing from prose alone
- **Failure meaning**: The rule stays abstract, leaving future authoring agents
  to reinterpret it inconsistently

---

## Explicit Non-Goals

| Item | Reason excluded |
| --- | --- |
| Choosing between `Enum`, `dataclass`, `ABC`, or `Protocol` | Owned by `python-model-selection` |
| General naming or control-flow style | Owned by `python-naming` / `python-control-flow` |
| Relaxing `pyright --strict` escape-hatch policy | Opposite of the topic goal |
| Changing skill path architecture or stable-library workflow | Outside this topic; repository positioning is already frozen |
| Introducing new test infrastructure or publish workflow | Topic is limited to analysis + plan for a focused skill refinement |

---

## Acceptance Criteria (Success Signals)

**AC-1 (Contract preservation)** — A reviewer can reject a proposed change from a
repo-owned type to `object` by pointing to one explicit rule in the revised
skill artifacts.

**AC-2 (Boundary clarity)** — A developer can tell in one read whether a given
`object` annotation is valid because it is at a decoder/validator/type-guard
boundary, or invalid because it weakens a normal domain contract.

**AC-3 (No convenience escape hatch)** — A remaining `object` usage is accepted
only when the artifact explicitly names the narrowing or untrusted-boundary role
it serves; "easier type checking" is never sufficient.

---

## Explicit Assumptions

- The target skill remains `.github/skills/python-type-hints-strict/`.
- Scope is limited to `SKILL.md`, `reference.md`, and `examples.md`.
- The repository's strict typing baseline still assumes `pyright --strict`.
- The policy should be hard-line by default: if a repo-owned/domain type exists,
  replacing it with `object` is invalid unless the position is a true untrusted
  boundary or narrowing-helper input.

---

## Extreme-Boundary Checks Applied

| Boundary probe | Resulting requirement implication |
| --- | --- |
| External decoder returns unknown shape | `object` may be acceptable only at the decoder/output-entry boundary before narrowing (R2) |
| Validator receives malformed external payload | `object` may be acceptable only as validator input if the next step narrows or rejects it (R2) |
| Repo-owned alias already exists | Replacing it with `object` is invalid (R1, R4) |
| One helper site vs many repeated API sites | Rule does not loosen at scale; repeated use makes the need for explicit types stronger, not weaker (R4) |
| Public return type vs type-guard input | Return types must stay precise; type-guard inputs may use `object` only for narrowing (R2) |

---

## Contradiction Log

No contradictions survived review. The main potential conflict was resolved
explicitly:

| Potential conflict | Resolution |
| --- | --- |
| "`object` is safer than guessing, so it should be broadly allowed" vs "strict typing must preserve known domain contracts" | Resolve in favor of contract preservation: `object` is allowed only at true untrusted boundaries or narrowing-helper inputs, never as a convenience fallback |

---

## Blockers

None. The baseline is frozen and ready for technical translation.
