# Skills audit findings and dispositions

Baseline: `c96eeb8b886d5e7885effbf2d56c7b9e337def8a`. Evidence below is from that exact revision, not guessed line numbers.

All 17 issues are confirmed static/runtime defects. Bounded model-decision observations are recorded in validation.md; they do not establish general speed or model-quality improvement.

## F01 — 投影引擎改壞自己

- 確認證據：`skills/platform-projection-adapter/scripts/platform_projection_adapter.py:157` — return content.replace(PLACEHOLDER_PREFIX, platform_prefix)
- 影響：投影產物無法正確重跑其他platform。
- 修正：renderer保留自身bytes；真正生成的引擎重新投影。
- 驗證界線：runtime tests及真實投影重跑。

## F02 — merge與整份覆寫混淆

- 確認證據：`skills/python-pre-commit/SKILL.md:71` — uv run scripts/apply_precommit.py --force
- 影響：更新既有設定可能丟失custom hooks。
- 修正：新建沿用generator；merge手工加入缺項並保留rev/args；整份替換需明確批准及備份。
- 驗證界線：文件獨立review；generator既有保留/覆寫測試。

## F03 — 空或錯誤完成證據可成功

- 確認證據：`skills/python-implementation-review/SKILL.md:90` — No matches → all Implementation Steps are complete → continue to step 2.
- 影響：既有gate可能忽略未知marker或缺漏section。
- 修正：完成檢查fail-closed；query介面不變；grep僅供列出。
- 驗證界線：64 runtime tests及24個獨立格式反例。

## F04 — 不可執行的驗證與pull語法

- 確認證據：`skills/python-pyproject-toolconfig/SKILL.md:70` — uv run -c "import tomllib; tomllib.load(open('pyproject.toml','rb')); print('TOML valid')"
- 影響：TOML驗證失敗；explicit remote/branch pull被解析成錯誤repository。
- 修正：uv run python -c並明確Python3.11+執行前提；git pull --ff-only remote branch。
- 驗證界線：CLI help/本機fixture；未對遠端執行post-merge pull。

## F05 — Pyright設定與tool detection錯誤

- 確認證據：`skills/python-code-review/SKILL.md:78` — Record detected tools in the output as `tooling_detected`. Use detected configuration to frame judgment — for example, if `[tool.pyright]` has `strict = true`, then `Any` usage is flagged as blocking.
- 影響：漏掉分散設定，strict severity可能錯配。
- 修正：使用typeCheckingMode或strict path array；累積各tool證據，尊重pyrightconfig precedence。
- 驗證界線：官方Pyright文件對照及獨立文件review；未跑Pyright模型比較。

## F06 — approved範例記錄PII

- 確認證據：`skills/python-code-review/examples.md:44` — logger.info("User created", extra={"email": email})
- 影響：few-shot示例與PII blocking政策矛盾。
- 修正：正例只記錄固定事件碼，不記email/任意exception文字；保留PII限制。
- 驗證界線：逐行檢查及獨立文件review。

## F07 — standalone review被formal gate阻斷

- 確認證據：`skills/python-code-review/SKILL.md:62` — ## Step 0 — Sequencing gate (MUST execute first)
- 影響：正常diff品質審查被迫先寫approved plan。
- 修正：獨立品質review直接做；正式workflow仍保留implementation gate。
- 驗證界線：獨立文件review；三模型before/after決策案例，見validation.md。

## F08 — 可查明事實也要求使用者填答

- 確認證據：`skills/python-plan-authoring/SKILL.md:74` — 1. **No Decisions content** — the user has not answered all required decision points:
- 影響：規劃工作退回使用者，額外數量門檻增加無關內容。
- 修正：先查code/config，提出有據decision；保留13sections，N/A有理由、Non-goals無配額。
- 驗證界線：模板/reviewer/示例一致性review；三模型before/after決策案例，見validation.md。

## F09 — safe default與ask同時生效

- 確認證據：`skills/python-decorators/SKILL.md:154` — - **Ambiguous requirement**: if stacking order or signature transparency requirement is undecided, apply the safe default (preserve signature with `functools.wraps` + `ParamSpec`) and note it may need revision.
- 影響：相同缺口可停可走，尤其auth/cache order不能靠wraps解決。
- 修正：只对material semantics詢問；one-shot/plainattribute安全預設與failure handling一致。
- 驗證界線：全庫description/default slice獨立review。

## F10 — handoff接收者排除該工作

- 確認證據：`skills/semantic-first-design/SKILL.md:184` — - Do not define exception hierarchy, translation, retry, or logging policy;
- 影響：retry/logging、classdecorator、asyncplugin是假handoff。
- 修正：承認coverage gap，查projectpolicy/verifieddocs；只轉交實際受理範圍。
- 驗證界線：對照caller/receiver及獨立review。

## F11 — 基準修訂要求magic word

- 確認證據：`skills/plan-creator/SKILL.md:72` — - analysis-layer artifacts outrank conversation-time instructions unless a human explicitly says `override`
- 影響：清楚的使用者修訂也被analysis舊稿阻擋。
- 修正：清楚修訂更新受影響baseline；只有歧義才問；同步workflow。
- 驗證界線：獨立文件review。

## F12 — draft PR套用release全gate

- 確認證據：`skills/git-release-management/SKILL.md:61` — 5. For the normal path, require the full gate: reviewer approval, CI green, base tests passing, strict type checks passing, lint passing, documentation updated where contracts changed, versions synchronized, a clean workspace, and no tag conflict.
- 影響：CI/review尚待PR才啟動時無法建立draft；非Python也被套strictPython。
- 修正：入口依draft/merge/release分流；release細節按需讀；必要安全與emergency限制保留。
- 驗證界線：獨立文件review；未宣稱PR已建立。

## F13 — public change等於breaking且amend無路

- 確認證據：`skills/git-commit-convention/SKILL.md:77` — 4. **Breaking change check** — if any public interface changes, require `!` marker and body explanation.
- 影響：相容新增誤標breaking，訊息amend無staging可能被拒。
- 修正：評估相容性；policy/newcommit/message-only分流；amend --only保留tree/index。
- 驗證界線：獨立文件review；未改寫真實commit history。

## F14 — 風險升級与review severity矛盾

- 確認證據：`skills/agent-skill-reviewer/review-checklist.md:176` — - escalate `medium → high` if the skill modifies code, creates plans used by
- 影響：一般local edit自動high，heading/count代替實質安全證據。
- 修正：依影響/可恢復性判斷，實質completion/failure必要、heading可等價；保留portablecompanion。
- 驗證界線：三份authoringcontract與59descriptions獨立review。

## F15 — 全新tests都必須RED

- 確認證據：`skills/python-tdd-test-authoring/SKILL.md:104` — - Tests are genuinely RED — they fail before any production code is written (verify by running `pytest --no-header -rN <test_file>` and confirming all new tests fail).
- 影響：與pass_existing/明示skip/xfail矛盾且可能以importerror充數。
- 修正：必須實跑並比較各test初始state；RED限目標行為缺失；cannot-run不得ready。
- 驗證界線：checklist/atomicorder/正文獨立review。

## F16 — 固定blueprint引用不存在section

- 確認證據：`skills/python-blueprint-authoring/SKILL.md:133` — - note the assumption explicitly as a sub-bullet under an existing section of the blueprint (e.g., under `## Implementation Notes`)
- 影響：consumer固定6section，作者卻引入未定義章節。
- 修正：assumption放既有Project Overview或相關schema section。
- 驗證界線：6section契約與修改位置對照。

## F17 — Codex來源metadata缺3筆

- 確認證據：`.codex/skills/README.md:36` — ## Current Mapping
- 影響：59skills只有56mapping/provenance，來源追蹤不完整。
- 修正：mapping/provenance59筆，baseline+exactsourcehash；不編造未存在的sourcecommit。
- 驗證界線：inventory/來源bytes/真實零差異projection檢查。

## Bounded evidence and remaining limitations

- Explicit content/destination authorization was received. All 72 planned observations, 6 affected-case reruns, the complete 36-record final-catalog rerun, and 3 current selected-family reruns completed; raw records and interpretation limits are in model-results.jsonl and validation.md.
- No latency, token-efficiency, task-success-rate, or cross-model improvement claim is made.
- All 59 descriptions were compared with triggers; issue-related companion families were deeply reviewed. This is not a claim that every existing example in all companions was executed.
- GitHub skill copies remain inspection-only: baseline comparison found 43 absent files and 32 differing files. This historical compatibility drift was not silently migrated.
- README existing rows were refreshed only, as planned. Its historical table omits platform-projection-adapter, scope-draft-plan, and spec-docs-mvp-generator and lists python-implementation-workflow outside the canonical 59. The inventory and Codex mapping enumerate the canonical set; row additions/removal remain a documented follow-up.
- Independent review suggested a generated-engine subprocess CLI auto-root regression. It is now implemented and passes. Running the projected tests also exposed premature replacement of fixture placeholders (4 failures); runtime fixture construction fixed that, and all 64 projected runtime tests now pass.
