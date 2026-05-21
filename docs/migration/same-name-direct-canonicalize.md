# Same-Name Direct Canonicalize

## Branch

- `feat/andrew/same-name-direct-canonicalize`

## Topic result

- Branch-local execution mode: canonical-authority decision only
- Candidate set executed: 2
- Skill content edit performed: no
- `.codex/skills` projection change performed: no

## Decision table

| skill | file_set_match | content_status | canonical authority | compatibility role | codex_projection_state | decision |
| --- | --- | --- | --- | --- | --- | --- |
| `business-intent-alignment` | `yes` | `equivalent` | `skills/` | `.github/skills/` remains the transition-era compatibility mirror | `readable-from-skills` | `canonicalize-directly` |
| `business-to-technical-translation` | `yes` | `equivalent` | `skills/` | `.github/skills/` remains the transition-era compatibility mirror | `readable-from-skills` | `canonicalize-directly` |

## Why no merge or overwrite is required

- Both skills already have matching file sets across `skills/` and
  `.github/skills/`.
- No content diff is present for either skill.
- `.codex/skills` already reads both skills from `skills/`, so the canonical
  authority decision does not require projection mutation in this topic.

## Authority decision

- `skills/` is the canonical authority for:
  - `business-intent-alignment`
  - `business-to-technical-translation`
- `.github/skills/` remains a transition-era compatibility mirror for both
  skills.
- This topic does not declare repo-wide active-path cutover complete.

## What did not change

- No file under `skills/` was edited.
- No file under `.github/skills/` was edited.
- No `.codex/skills` symlink, README, or provenance file was edited.
- No planning-spine candidate was touched.

## Deferred items

- Any future repo-wide current-path governance change
- Any `.github/skills/` retirement or projection cutover step
