# Reference

## CLI Contract

Run the local CLI from the active projected skill surface:

```bash
uv run .<platform>/skills/platform-projection-adapter/scripts/platform_projection_adapter.py \
  --platform-root <path>
```

Add `--apply` only for explicit writes:

```bash
uv run .<platform>/skills/platform-projection-adapter/scripts/platform_projection_adapter.py \
  --platform-root <path> \
  --apply
```

Add `--force` only when differing managed target files may be overwritten:

```bash
uv run .<platform>/skills/platform-projection-adapter/scripts/platform_projection_adapter.py \
  --platform-root <path> \
  --apply \
  --force
```

## Behavior Notes

- Source of truth is always the canonical `skills/` library under the repo root.
- The projected script must remain runnable from `.<platform>/skills/...` without
  requiring callers to swap back to `skills/...`.
- Target paths always land under `<platform-root>/skills/` while preserving the
  canonical relative path.
- Dry-run is the default and performs no writes.
- `--apply` without `--force` is blocked when an existing managed target file
  differs from the rendered projection.
- `--force` removes only the overwrite block for managed target files. It does
  not widen source scope and does not delete extra target files.
- Placeholder text that starts with `.<platform>/` is rewritten in target
  content to `<platform-root>/`.
- Canonical wording that already refers to `skills/...` remains unchanged.
- When the skill text describes a projection surface abstractly, prefer
  `.<platform>/...` wording over naming one concrete platform path.
- The script locates the repository root by walking upward until it finds
  `AGENTS.md` and the canonical `skills/` directory, so both canonical and
  projected script paths stay valid runtime entrypoints.

## Summary Fields

Every run should be read through these fields:

- `mode`
- `platform_root`
- `source_count`
- `create`
- `update`
- `noop`
- `conflicts`
- `result`
- `error` when present

`create_paths`, `update_paths`, and `conflict_paths` explain which managed
target files would change.

## Failure Interpretation

- `result: SAFE_TO_APPLY` means dry-run found no differing managed target files.
- `result: APPLIED` means the CLI completed its write phase successfully.
- `result: BLOCKED` means the run did not finish in a state that should be
  treated as successful. Re-read the `error` line and rerun dry-run if needed.

If apply fails partway through, trust the next dry-run summary instead of the
previous plan.
