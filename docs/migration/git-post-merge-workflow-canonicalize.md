# git-post-merge-workflow-canonicalize

## Candidate

- `git-post-merge-workflow`

## Verdict

- bounded canonical copy: completed
- branch-policy / active-path repair: deferred

## Source And Target

- source root: `.github/skills/git-post-merge-workflow/`
- target root: `skills/git-post-merge-workflow/`

## Copied File Set

- `SKILL.md`
- `examples.md`
- `references/stop-point-2-checklist.md`

## Compatibility Boundary

- `.github/skills/git-post-merge-workflow/` remains present and unchanged
- compatibility layer preserved: yes
- active path changed: no
- STOP POINT 2 semantics changed: no

## Deferred Lanes

- active-path switching
- branch-policy redesign
- release-surface changes

## Validation Notes

- `diff -rq .github/skills/git-post-merge-workflow skills/git-post-merge-workflow`
  should return no differences after the copy
- no `.github/skills/git-post-merge-workflow/` content should be modified in this topic
