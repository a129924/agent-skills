# Reference Overview — `python-descriptors-attribute-access`

This skill's reference material is split across four topic-specific files.
Each file covers one logical cluster of requirements.
Read the file for the topic you are working on; do not read all four
unless you need the full picture.

## Reference files

| File | Topic | Requirements |
| --- | --- | --- |
| [`references/mechanism-ladder.md`](references/mechanism-ladder.md) | 7-rung decision ladder — per-rung upgrade criteria and unjustified-skip signal | R1 |
| [`references/property-and-cached-property.md`](references/property-and-cached-property.md) | `@property` discipline, `@cached_property` lazy attributes, setter validation boundary, Python 3.8+ gate | R2, R3 |
| [`references/custom-descriptors.md`](references/custom-descriptors.md) | Upgrade criteria from `@property`, `__set_name__` for reusability, data vs non-data lookup priority table | R4, R5, R6 |
| [`references/attribute-hooks.md`](references/attribute-hooks.md) | `__getattr__` / `__setattr__` escape hatch checklist, `__getattribute__` near-absolute discouragement, `__init__` pitfall and fix | R7, R8, R9, R10 |

Start with `references/mechanism-ladder.md` if you are unsure which mechanism to choose.
Start with `references/attribute-hooks.md` if you are reviewing code that already uses hook methods.
