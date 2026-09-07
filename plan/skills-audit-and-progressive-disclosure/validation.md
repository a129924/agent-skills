# Validation evidence

## Local checks

| Check | Observed result |
| --- | --- |
| Canonical inventory, projection, tracker, pre-commit and toolconfig suites | 94 passed |
| Generated Codex projection and tracker suites | 64 passed |
| Independent runtime checks | 64 suite tests plus 24 malformed-input probes passed |
| Generated-engine subprocess CLI auto-root | Passed; independently reviewed |
| Actual projected CLI dry-run against `.codex` | 287 noop, 0 create, 0 update, 0 conflicts; exit 0 |
| Canonical inventory | 59 records; exact deterministic builder output |
| Codex mapping and provenance | Exactly the 59 canonical names |
| Engine exception | Canonical and projected runtime byte-identical |
| Skill frontmatter | Ruby YAML safe-load accepted all 59; names match directories |
| Local-reference scan | 221 candidates; 218 actual local/repo paths resolve; 3 are illustrative/output names, not missing dependencies |
| Python syntax | Both changed runtimes and evaluator parse with Python AST |
| Topic JSON | Parseable; source hashes recorded per skill |
| Change boundary | All 219 final changed paths in the 828-entry approved manifest |
| Whitespace | Tracked and staged checks passed after removing a new reference's trailing blank line |
| Original checkout | `dev` worktree remains clean |
| Recovery archive | SHA-256 matched; all 580 matching manifest baseline files verified from readable archive members |

Executed canonical test command (using existing local tooling, no install):

```bash
env PYTHONDONTWRITEBYTECODE=1 PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
  PYTHONPATH=/Users/andrew/.cache/uv/archive-v0/-Vwipp48jy8pUdMUEO3NT/lib/python3.9/site-packages \
  UV_CACHE_DIR=/private/tmp/skills-audit-uv-cache UV_OFFLINE=1 \
  UV_PYTHON=/opt/homebrew/bin/python3 \
  python3 -m pytest -q -p no:cacheprovider \
  skills/platform-projection-adapter/tests skills/plan-step-tracker/tests \
  skills/python-pre-commit/tests skills/python-pyproject-toolconfig/tests tests
```

The host interpreter is Python 3.14; the existing cached pytest package is reused
via PYTHONPATH. This is the actual machine-specific command, not a portable
installation prescription. Tests use disposable fixtures, not real user config.

The projected suite command uses the same read-only Python/pytest environment
with `.codex/skills/platform-projection-adapter/tests` and
`.codex/skills/plan-step-tracker/tests` as targets.

Projection/inventory reuse existing CLIs:

```bash
python3 skills/platform-projection-adapter/scripts/platform_projection_adapter.py --platform-root .codex
python3 skills/platform-projection-adapter/scripts/platform_projection_adapter.py --platform-root .codex --apply --force
python3 scripts/build_skills_inventory.py
python3 .codex/skills/platform-projection-adapter/scripts/platform_projection_adapter.py --platform-root .codex
```

The first dry-run intentionally reported differences. `--apply --force` was used
only after the exact target was previewed and the recoverable backup existed.
Later review corrections were regenerated and the final projected CLI returned
zero drift. No `.github/skills` files were changed.

## Failure history retained

- Initial new runtime regression selection: 4 failed, 4 passed, 43 deselected,
  reproducing generated-engine and missing/empty/malformed completion failures.
- First complete run with a cached Python 3.9 interpreter: collection failed on
  existing `tomllib` imports. Switched to installed Python 3.14; no product code
  was weakened to accommodate the wrong test interpreter.
- First Python 3.14 run: 12 failed, 69 passed because uv could not access its
  default cache under sandbox permissions. An isolated offline cache resolved
  this execution limit; original affected tests then passed.
- Independent review found additional malformed completion inputs not covered by
  the initial tests. Added 13 regression cases; all canonical tests now pass.
- Executing generated tests exposed 4 failures and 60 passes: their literal
  placeholder fixtures had been prematurely concretized. Runtime construction
  of test data fixed the issue without widening the renderer exception. The
  regenerated suites now pass all 64 tests.
- A final combined invocation of canonical and projected suites failed collection
  because mirrored test files share module names. Re-ran the suites in separate
  processes using the documented commands: 94 canonical and 64 projected passed.
  No product changes or deletion of caches were needed.

## Model comparison — observed

On 2026-09-07 the user explicitly authorized transmitting evaluation-required
Skills content, including unpublished edits, to Codex Astra / Sol / Luna.
Auto-review then accepted the commands; the earlier rejection was not bypassed.
The earlier content-free Luna availability probe is not part of these results.

Executed `evaluate_models.py before` and `evaluate_models.py after`, each with
`--output plan/skills-audit-and-progressive-disclosure/model-results.jsonl`.
After correcting a stale release-procedure cross-reference, executed
`evaluate_models.py after --case draft-pr` with the same output. A later staged
whitespace check removed a trailing blank line in that reference; repeated the
same three cases to match final content hashes. All 78 raw records are retained:
36 before, 36 initial after and 6 affected-case reruns.
All were observed, with no execution-limited result or unexpected tool event.

| Model (medium effort) | Before action matches | Final after action matches |
| --- | --- | --- |
| gpt-6-astra | 8/12 | 12/12 |
| gpt-5.6-sol | 8/12 | 12/12 |
| gpt-5.6-luna | 7/12 | 12/12 |

These counts measure agreement with predefined next-action labels, not complete
workflow success. Manual inspection of all answers found a before-Luna PII case
with the correct `block` label but an incorrect additional claim that workflow
approval was absent. The after answer recognizes sequencing is satisfied and
blocks specifically on PII. The before count is not a semantic pass rate.
All final after reasons are consistent with their supplied scenario and expected
next action; selected-skill arrays are not independently scored.

All three models now proceed on standalone review and discoverable facts, block
on missing-plan, invalid-step and PII gates, and ask about unresolved auth/cache
order. Before Astra/Sol blocked draft creation; before Luna unnecessarily asked
about explicit changed intent and blocked a documented routing gap. No final
after action mismatches were observed in this fixed sample.

The runner exports only discovery descriptions and selected-family Markdown,
using fresh ephemeral read-only Codex calls. The CLI method was checked against
local help and the official
[non-interactive documentation](https://learn.chatgpt.com/docs/non-interactive-mode).
Expected labels are not supplied in prompts. References are preloaded: this is
not an on-demand retrieval, tool-using implementation, latency or token-efficiency
test. One observation per phase/case is not a repeated reliability study.
Prompt hashes identify content; use the latest after record per model/case for
the delivered snapshot, retaining superseded records for traceability.

Independent evaluation-method review: approved with these interpretation limits.
Timeout handling preserves an error summary rather than partial stdout/stderr;
no timeout occurred, so this unexercised path remains a documented limitation.

## Remaining limitations

- Required model observations are complete. Final independent topic acceptance
  and publishing are tracked in the topic review log and summary; no merge or
  release is authorized.
- The README's existing rows were refreshed without adding/removing rows, per
  the plan. Its historical missing canonical entries and extra noncanonical
  workflow row are recorded in findings.md for a separate indexing decision.
- All descriptions and issue-related documents were reviewed, not every code
  example in every companion. No improvement in speed or model quality is claimed.

## Publication verification

Three implementation/evidence topic commits were pushed normally. PR #126 was
initially created as a draft and read back as OPEN/draft, base dev, intended feature head:
https://github.com/a129924/agent-skills/pull/126

At that check, `statusCheckRollup=[]` and `reviewDecision` was empty. The user
subsequently authorized Ready-for-review status; GitHub then reported
`isDraft=false` with the same base/head. Neither state is a green-CI or
human-approval signal. Human review is the next handoff; merge, release, tags
and worktree cleanup are outside this delivery.
