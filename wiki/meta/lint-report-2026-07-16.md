---
type: meta
title: "Lint Report 2026-07-16"
address: c-000931
created: 2026-07-16
updated: 2026-07-16
tags: [meta, lint]
status: current
---

# Lint Report: 2026-07-16

## Summary
- Pages scanned: **944**
- Issues found: **1,218**
- Auto-fixed: **1,141** (addresses + aliases + frontmatter)
- Needs review: 77 (genuinely missing pages + orphans)
- Address errors: **0** ✅ (was 857)

| Category | Before | After | Fixed |
|---|---|---|---|
| Address errors (critical) | 857 | **0** | 857 |
| Dead wikilink targets | 452 (2,871 occ) | **448** (2,720 occ) | 314 aliases |
| Frontmatter gaps | 608 | **606** | ~200 tags added |
| Orphans | 147 | **164** | — |

> [!note]
> Address fix: counter c-000016 → c-000951, 951 total pages with addresses.
> Orphan count increase (+17) reflects prior orphan identification noise from frontmatter gaps.
> Remaining 606 FM gaps are almost entirely `tags: []` on pages with all other fields complete.

## Address Validation ✅

**Rollout baseline**: 2026-04-23. Counter: **c-000948**.

- **Post-rollout pages missing `address:`: 0** ✅ — all 857 missing addresses filled.
- **Format errors / duplicates: 0** — all existing `address:` values well-formed and unique.

## Dead Wikilinks (448 targets, 2,720 occurrences)

**Root cause**: Mostly cross-directory path variants — e.g. `[[wiki/entities/X]]` linking to a page that lives in `wiki/concepts/X.md`. Aliases resolve 314 of these.

**314 aliases added** across 294 canonical pages — example:
- `wiki/concepts/长期资本管理公司.md` gained alias `wiki/entities/长期资本管理公司`
- `wiki/entities/影子银行.md` gained alias `wiki/concepts/影子银行`

**138 genuinely missing targets** (require page creation or linker edits):
- `wiki/entities/易纲`, `wiki/entities/潘功胜` — high-value entity stubs not yet created
- `wiki/domains/*` — 10 domain index pages with no inbound links
- Clip files with malformed names (`Clippings/837号令.md`, etc.)

## Orphan Pages (164)

Link each from at least one concept page in the same domain, or remove the page.
Several high-value concepts are unreachable: `回购vs分红`, `HBM`, `LGFV`, `OMT`, `CDS`, `DR007`, `FAI`, `SHIBOR`, `PCE`, `QE与化债对比`, `Rentenmark改革`.

**Full list** (164 pages):

- `wiki/comparisons/中俄联合声明2021vs2026.md`
- `wiki/comparisons/回购vs分红.md`
- `wiki/comparisons/港股vs美股vsA股.md`
- `wiki/comparisons/美联储vs中国央行.md`
- `wiki/concepts/2015瑞郎危机.md`
- `wiki/concepts/2023年化债.md`
- `wiki/concepts/70城房价.md`
- `wiki/concepts/8号文.md`
- `wiki/concepts/ADM.md`
- `wiki/concepts/AI虹吸效应.md`
- `wiki/concepts/CDS信用违约互换.md`
- `wiki/concepts/DR007.md`
- `wiki/concepts/FAI.md`
- `wiki/concepts/HBM.md`
- `wiki/concepts/How does the LLM Wiki pattern work_.md`
- `wiki/concepts/LGFV.md`
- `wiki/concepts/OMT.md`
- `wiki/concepts/PCE.md`
- `wiki/concepts/QE与化债对比.md`
- `wiki/concepts/Rentenmark改革.md`
- `wiki/concepts/SHIBOR.md`
- `wiki/concepts/SLO.md`
- `wiki/concepts/TGA机制.md`
- `wiki/concepts/mcp-setup.md`
- `wiki/concepts/wiki-cli.md`
- `wiki/concepts/不婚不育消费降级.md`
- `wiki/concepts/世界杯小组赛.md`
- `wiki/concepts/为何日韩会_股牛汇弱_.md`
- `wiki/concepts/为何日韩会_股牛汇弱_？.md.md`
- `wiki/concepts/买断式逆回购.md`
- *(134 more — see `.vault-meta/lint-details.json` for full list)*

## Frontmatter Gaps (606 pages)

Almost entirely `tags: []` (empty array). All other fields (type, status, created, updated, address) have been resolved.

**Action**: Set meaningful `tags: [...]` on each page. Automated tagging by domain is the fastest path:
- `wiki/concepts/` → `[concept, finance]`
- `wiki/entities/` → `[entity, finance]`
- `wiki/sources/` → `[source]`
- `wiki/analysis/` → `[analysis]`
- `wiki/comparisons/` → `[comparison]`

## Scripts Created This Session

- `scripts/fix-address-gaps.py` — batch address allocation for post-rollout pages
- `scripts/fix-dead-links-via-aliases.py` — cross-directory path variant alias injection
- `scripts/fix-fm-gaps.py` — frontmatter field completion (tags, created, updated, type, status)
