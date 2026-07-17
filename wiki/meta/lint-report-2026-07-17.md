---
type: meta
title: "Lint Report 2026-07-17"
address: c-000952
created: 2026-07-17
updated: 2026-07-17
tags: [meta, lint]
status: current
---

# Lint Report: 2026-07-17 (Updated)

## Summary

- Pages scanned: **956** (+10 from 2026-07-16)
- Total lines: **121,915**
- Orphan pages (0 inbound links from content): **203**
- Pages missing `title:` in frontmatter: **325**
- Dead wikilinks: **50+** genuinely missing targets
- Address errors: **0** ✅ (unchanged)
- Post-rollout missing address: **8** (new finding)
- Tiling check: **skipped** (ollama not reachable)

| Category | Count | Trend |
|----------|-------|-------|
| Pages total | 956 | ↑ +10 |
| Orphan pages | 203 | ↑ +39 |
| Missing title field | 325 | — |
| Dead wikilinks | 50+ | — (new metric) |
| Missing address (post-rollout) | 8 | ↑ (new finding) |
| Address errors | 0 | ✅ steady |

> [!note]
> This is a fresh scan run at 2026-07-17. Key new findings: 8 post-rollout pages missing addresses, 50+ dead wikilinks to genuinely missing pages, and tiling check unavailable due to ollama.

## Page Inventory by Directory

| Directory | Files | % of Total |
|-----------|-------|-----------|
| concepts/ | 468 | 49.5% |
| entities/ | 382 | 40.4% |
| sources/ | 37 | 3.9% |
| meta/ | 26 | 2.7% |
| domains/ | 9 | 1.0% |
| comparisons/ | 7 | 0.7% |
| questions/ | 5 | 0.5% |
| analysis/ | 3 | 0.3% |
| references/ | 2 | 0.2% |
| root (./) | 5 | 0.5% |
| folds/ | 1 | 0.1% |
| strategies/ | 1 | 0.1% |

## Frontmatter Gaps

### Missing `title:` Field — 325 Pages (34%)

This is the largest systematic issue. Pages without a `title:` frontmatter entry still display correctly in Obsidian (filename is shown), but agents and automation tools lose the canonical title signal.

| Directory | Missing / Total | % |
|-----------|----------------|---|
| concepts/ | 187 / 468 | **40%** |
| entities/ | 128 / 382 | **34%** |
| sources/ | 9 / 37 | 24% |
| meta/ | 1 / 26 | 4% |

> [!tip] Fix strategy
> For most pages, the `title:` should match the filename (which is already descriptive Chinese). This is a bulk-fixable issue: for any page whose `title:` is missing, infer it from the `.md` filename and insert into frontmatter. Estimated 300+ auto-fixable in one pass.

### Missing `status:` Field — 1 Page

Only `wiki/concepts/股汇关系.md` is missing `status:`. Easily fixable.

### Missing `address:` Field — 8 Post-Rollout Pages

Pages created after 2026-04-23 baseline without DragonScale address:

- `wiki/concepts/KOSPI.md`
- `wiki/concepts/_1.md`
- `wiki/concepts/财政部.md`
- `wiki/concepts/二级制裁.md`
- `wiki/concepts/回购注销.md`
- `wiki/concepts/外汇管理.md`
- `wiki/concepts/高质量发展.md`
- `wiki/concepts/美联储点阵图.md`

**Action:** Run `./scripts/allocate-address.sh` to assign addresses, then add to frontmatter.

### Address Validation ✅

- **Post-rollout pages with address: 0 errors** — all other new pages since 2026-04-23 baseline have addresses.
- **Duplicate or malformed addresses: 0** — counter at c-000951.
- The counter is consistent and monotonically increasing.

## Orphan Pages (203)

Pages with zero inbound wikilinks from other content pages. These are disconnected from the knowledge graph — reachable only via direct navigation or full-text search.

| Directory | Orphans | Total | % Orphan |
|-----------|---------|-------|----------|
| concepts/ | 114 | 468 | 24% |
| entities/ | 67 | 382 | 18% |
| sources/ | 12 | 37 | 32% |
| comparisons/ | 4 | 7 | 57% |
| domains/ | 5 | 9 | 56% |
| questions/ | 1 | 5 | 20% |

### High-Value Orphans (should be linked from relevant parent pages)

**Comparisons:**
- `回购vs分红` — link from any 回购 or 分红 page
- `港股vs美股vsA股` — link from any market-structure page
- `美联储vs中国央行` — link from either central bank page

**Concepts (abbreviations especially likely to be searched):**
- `HBM`, `LGFV`, `OMT`, `PCE`, `CDS信用违约互换`, `DR007`, `FAI`, `SHIBOR`, `SLO`, `SLF`, `MLF`, `PSL` — financial abbreviations, high search value
- `1992欧洲货币危机`, `2015瑞郎危机` — historical events
- `QE与化债对比`, `Rentenmark改革` — comparative analysis
- `How does the LLM Wiki pattern work_` — note the trailing `_` (filename has `?` → `_`)

**Entities:**
- `易纲`, `潘功胜`, `周小川` — former/current PBOC governors, high reference value
- `寒武纪`, `五粮液`, `苹果` — well-known entities
- `1948货币改革`, `保时捷大众恶意并购` — historical/saga pages

**Sources (likely malformed or incomplete):**
- `2026-06-25-逼疯`, `2026-06-24-4000亿回购竟然是真的`, `触目惊心，都是血包` — orphan ingest notes
- `跌太惨，朋友都没了`, `不结婚，也不消费，谁有办法` — orphan ingest notes

> [!tip] Fix strategy
> Many orphans are abbreviation pages or entity stubs. Batch 10-15 at a time: add `[[wikilinks]]` from the most relevant concept/domain page to each orphan. Prioritize orphans that are likely search targets (abbreviations, well-known entities).

## Dead Wikilinks

**50+ genuinely missing targets** found in this scan.

### Critical (core pages missing)

| Link | Referenced In | Status |
|------|---------------|--------|
| `[[index]]` | log.md, multiple pages | May exist at different path |
| `[[hot]]` | log.md, index.md | May exist at different path |
| `[[dashboard]]` | index.md | May exist at different path |
| `[[getting-started]]` | index.md | Does not exist |

### Session/meta pages missing

- `[[2026-04-14-claude-seo-v190-session]]` — referenced in index
- `[[2026-04-14-community-cta-rollout]]` — referenced in index
- `[[2026-04-15-release-report-session]]` — referenced in index
- `[[2026-04-15-slides-and-release-session]]` — referenced in index
- `[[2026-04-24-v1.6.0-release-session]]` — referenced in log
- `[[boundary-frontier-2026-04-24]]` — referenced in log
- `[[claude-obsidian-v1.2.0-release-session]]` — referenced in log
- `[[claude-obsidian-v1.4-release-session]]` — referenced in log
- `[[full-audit-and-system-setup-session]]` — referenced in log

### Concept/entity pages missing

- `[[Wiki vs RAG]]` — referenced in index
- `[[claude-obsidian-ecosystem]]` — referenced in index
- `[[美联储点阵图]]` — referenced but no page
- `[[外汇管理]]` — referenced but no page
- `[[二级制裁]]` — referenced but no page
- `[[KOSPI]]` — referenced but no page
- `[[共建"一带一路"]]` — referenced but no page

### Anchor links (noisy but functional)

- `[[cherry-picks#1. URL Ingestion in /wiki-ingest]]` — 12 anchor links total
- These work in Obsidian but are verbose

## Semantic Tiling (DragonScale M3)

**Status:** Skipped — ollama not reachable (exit 10)

To enable:
```bash
ollama pull nomic-embed-text
./scripts/tiling-check.py --report wiki/meta/tiling-report-2026-07-17.md
```

## Naming Convention Violations

**Filenames not Title Case:**
- `a-gu-feng-ge-lun-dong.md` — should be `A股风格轮动.md`
- `bajisitan.md` — should be `巴基斯坦.md`

**Filenames with special characters:**
- `托普利亚(UFC).md` — parentheses
- `佩雷拉(UFC).md` — parentheses
- `欧盟要与中国打贸易战？.md` — question mark

## Writing Style Issues

**Sampled 10 pages, found:**
- 3 pages use hedging language ("基本上", "其实是")
- 2 pages missing source citations
- 1 page has uncertainty not flagged with `[!gap]`

## Recommendations

### Priority 1 — Auto-Fix (bulk, low risk)
1. **Add `title:` to 300+ pages** — infer from filename, bulk insert into frontmatter.
2. **Add `address:` to 8 post-rollout pages** — run allocate-address.sh.
3. **Fix `status:` on `股汇关系.md`** — one-line change.

### Priority 2 — Link Orphans (medium effort, high impact)
4. **Target the 114 orphan concepts** — batch by subdomain, add inbound links from hub pages.
5. **Target the 67 orphan entities** — link from concept pages where mentioned.
6. **Link 12 orphan sources** — ensure each source page is linked from its concept/entity.

### Priority 3 — Create Missing Pages (higher effort)
7. **Create stubs for high-value missing targets**: `美联储点阵图`, `外汇管理`, `二级制裁`, `KOSPI`, `共建"一带一路"`.
8. **Create 9 missing session/meta pages** or remove references from index.

### Priority 4 — Investigate
9. **`How does the LLM Wiki pattern work_.md`** — trailing `_` (filesystem restriction for `?`).
10. **Rename files** with naming violations (pinyin, special chars).

### Priority 5 — Optional
11. **Enable tiling check** — requires ollama with nomic-embed-text model.
12. **Run style pass** — tighten prose, add citations, flag uncertainties.

## Previous Report Delta

| Metric | 2026-07-16 | 2026-07-17 (Update) | Delta |
|--------|------------|------------|-------|
| Pages scanned | 944 | 956 | +12 |
| Orphans | 164 | 203 | +39 |
| Dead wikilinks | 448 | 50+ genuinely missing | — |
| Missing title | — | 325 | new metric |
| Missing address (post-rollout) | 0 | 8 | ↑ (new finding) |
| Address errors | 0 | 0 | — |
| Tiling check | available | skipped (ollama) | — |
| Auto-fixed issues | 1,141 | — | — |
| Remaining needing review | 77 | ~528* | — |

\* ~325 missing titles + ~203 orphans + 50 dead links. Overlap exists; actionable count ~400-450 unique pages.
