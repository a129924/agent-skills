# Scope Draft Plan Skill — PR #119 Correction Steps

## Correction workflow

- [X] Planner classified PR #119 inventory drift as `medium` and froze
  `PLANNER_REPLAN` direction.
- [X] Planner updated parent truth: exact correction artifacts and generated
  inventory snapshot are declared in `Artifact Paths`; obsolete exact-11
  feature-write-set wording is removed.
- [ ] Implementer makes exactly four bounded PR-comment repairs:
  1. output template allows only a BC Mission or explicitly marks Cross-BC /
     Spike as `BLOCKED`;
  2. step artifact removes or corrects stale `uncommitted by design` wording;
  3. summary artifact removes or corrects the same stale wording; and
  4. review log records `approved` as the skill-review gate verdict, using
     `PASS` only as explanatory prose if retained.
- [ ] Implementer runs `uv run scripts/build_skills_inventory.py --repo-root .`
  after the final skill fixes to regenerate `artifacts/skills-inventory.jsonl`.
- [ ] Implementer verifies: exactly 57 JSONL records; exactly one record whose
  `canonical_path` equals `skills/scope-draft-plan` (no trailing slash); and
  no inventory-record change other than that one new canonical-skill record.
- [ ] Separate Reviewer reviews the bounded correction diff and returns an
  explicit verdict.
- [ ] After approval, Main Agent commits and pushes the bounded correction to
  the existing PR #119 branch; no new PR or release route is created.

## Handoff constraints

- This is one correction loop inside the existing `pr-open` topic state; it is
  not a new Human Gate or a new feature scope.
- The Implementer must not change parent planning intent, the inventory builder
  contract, or deferred release timing.
- A failed inventory count, a duplicate/missing exact `canonical_path`, an
  unexpected inventory-record diff, an incomplete one of the four repairs, or
  scope/path drift returns to Planner before commit.
