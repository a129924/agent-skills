# Examples

## Dry-run first

Use dry-run to inspect the whole-library plan without writing anything:

```bash
# First projection run can use the canonical skills/... entrypoint instead.
uv run .codex/skills/platform-projection-adapter/scripts/platform_projection_adapter.py \
  --platform-root <path>
```

Expected interpretation:

- `result: SAFE_TO_APPLY` means no differing managed target files block apply.
- `result: BLOCKED` means the summary found an issue such as differing managed
  target files that would require `--force`.

## Apply after explicit authorization

Only add `--apply` when the caller explicitly authorizes writes:

```bash
# First projection run can use the canonical skills/... entrypoint instead.
uv run .codex/skills/platform-projection-adapter/scripts/platform_projection_adapter.py \
  --platform-root <path> \
  --apply
```

Use this when dry-run already showed the projection is safe or when the target
surface is known to be empty.

## Force only for differing managed files

When a managed target file already exists with different content, add `--force`
only after explicit overwrite approval:

```bash
# First projection run can use the canonical skills/... entrypoint instead.
uv run .codex/skills/platform-projection-adapter/scripts/platform_projection_adapter.py \
  --platform-root <path> \
  --apply \
  --force
```

This does not authorize deletion of extra target files and does not change the
whole-library source scope.

## Incorrect patterns

- Running without `--platform-root` and expecting the CLI to guess the `.codex/skills/` target surface
- Running the projected skill and then hard-coding a fallback back to `skills/platform-projection-adapter/...` instead of using the local `.codex/skills/...` entrypoint
- Treating dry-run as permission to write
- Writing a second projection procedure in the skill text or in ad-hoc shell
  commands
- Using `--force` to justify deleting target extras or changing canonical
  `skills/`
