# git-release-management-canonicalize

## Candidate

- `git-release-management`

## Verdict

- bounded canonical copy: completed
- release-policy / active-path repair: deferred

## Source And Target

- source root: `.github/skills/git-release-management/`
- target root: `skills/git-release-management/`

## Copied File Set

- `SKILL.md`
- `examples.md`
- `references/gate-contract.md`
- `references/version-sources.md`
- `references/version-bump-guidance.md`
- `references/emergency-path.md`

## Compatibility Boundary

- `.github/skills/git-release-management/` remains present and unchanged
- compatibility layer preserved: yes
- active path changed: no
- release gate semantics changed: no

## Deferred Lanes

- active-path switching
- release-policy redesign
- tag/version-policy changes

## Validation Notes

- `diff -rq .github/skills/git-release-management skills/git-release-management`
  should return no differences after the copy
- no `.github/skills/git-release-management/` content should be modified in this topic
