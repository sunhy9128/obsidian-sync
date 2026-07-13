---
type: meta
title: "Lint Report 2026-06-24"
created: 2026-06-24
updated: 2026-06-24
tags: [meta, lint]
status: developing
related:
  - "[[Wiki Map.canvas]]"
  - "[[index]]"
  - "[[log]]"
  - "[[hot]]"
---

# Lint Report: 2026-06-24

## Summary

| Metric | Count |
|---|---|
| Pages scanned (excluding folds/meta) | 497 |
| Frontmatter coverage | 100% (497/497) |
| Orphan pages (no inbound link, >3d old) | 0 |
| Dead links | 36 |
| Pages missing tags | 111 |
| Pages missing created | 9 |
| Pages missing updated | 1 |
| Address validation issues | 0 |
| Tiling check | SKIPPED (ollama not installed) |
| Issues found (BLOCKER + HIGH + MEDIUM + LOW) | 1 BLOCKER + 3 HIGH + 4 MEDIUM + 3 LOW |
| Auto-fixed | 0 |

---

## Type Distribution

| Type | Count |
|---|---|
| entity | 235 |
| concept | 215 |
| source | 17 |
| meta | 11 |
| domain | 8 |
| comparison | 5 |
| analysis | 2 |
| reference | 2 |
| overview | 1 |
| question | 1 |

## Status Distribution

| Status | Count |
|---|---|
| developing | 162 |
| evergreen | 17 |
| current | 9 |
| mature | 5 |
| seed | 4 |
| seedling | 3 |
| extracted | 3 |
| proposed | 1 |
| (none set) | 293 |

> Note: 293 pages without `status` field is mostly sources + concept notes using tag-based maturity instead. Not a blocker, but flagged for completeness.

---

## BLOCKER Findings

### B1. `flock` command not available on this system

The DragonScale `allocate-address.sh` and `wiki-lock.sh` scripts both depend on `flock(1)` for atomic file locking. macOS does not ship `flock` by default and it is not installed via Homebrew (`/usr/local/bin/flock` and `/opt/homebrew/bin/flock` both missing).

**Impact**: Every DragonScale-backed operation fails at lock acquisition:

```
$ bash scripts/allocate-address.sh --peek
scripts/allocate-address.sh: line 36: flock: command not found
ERR: could not acquire address allocator lock within 5s
```

This breaks:
- `wiki-ingest` address assignment (Mechanism 2)
- `wiki-lock` advisory locks for multi-writer safety (v1.7 mechanism)
- Address counter consistency checks
- PostToolUse hook deferral on lock-held state

**Recommended fix**:
```bash
brew install flock
# OR replace flock with shlock-compatible fallback
# OR install util-linux via MacPorts
```

Status of DragonScale mechanisms in this vault: **effectively dormant**. Only 1 page (`wiki/concepts/DragonScale Memory.md` → `c-000001`) has an address assigned out of 497 pages. Counter at 3 is manual. Decide whether to enable or formally retire.

---

## HIGH Findings

### H1. 36 dead wikilinks — 3 root causes

#### H1.a — Placeholder references inherited from template (7 links, 16+ references)

These reference pages that were promised by the claude-obsidian template but were never created in this vault:

| Target | References | First-seen source |
|---|---|---|
| `[\[Wiki Map\]]` | 6 | `wiki/hot.md`, `wiki/getting-started.md` |
| `[\[dashboard\]]` | 6 | `wiki/overview.md` |
| `[\[How does the LLM Wiki pattern work?\]]` | 5 | `wiki/hot.md`, `wiki/log.md` |
| `[\[claude-obsidian-presentation\]]` | 1 | `wiki/overview.md` |
| `[\[AI Marketing Hub Cover Images Canvas\]]` | 1 | `wiki/overview.md` |
| `[\[notes/Foo\]]` | 2 | `wiki/log.md` (placeholder) |

**Fix**: Either create stub pages, or replace with descriptive text. `wiki/Wiki Map.canvas` exists and could resolve `[\[Wiki Map\]]` if Obsidian resolves canvas files (it does not by default).

#### H1.b — Stale `Clippings/...` paths in source citations (~34 references)

Frontmatter `sources:` fields across many concept pages reference `[\[Clippings/...\]]` paths that no longer exist. Example:

```yaml
# wiki/concepts/反外国不当域外管辖条例.md
sources: ["[[Clippings/837号令.md]]"]
# wiki/concepts/征兵困境.md
sources: ["[[Clippings/太不团结了.md]]"]
```

`raw/Clippings/` directory does not exist in this vault. These files were either renamed, moved to `raw/articles/`, or never migrated.

**Fix**: Map each `Clippings/X.md` reference to its actual current path. The filenames correspond to entries in `raw/articles/` or `wiki/sources/`.

#### H1.c — `raw/wechat/...` wikilinks point to ingested sources (~11 references)

The wiki uses `[\[raw/wechat/2026-04-15-2026年1-3月中国外贸数据.md\]]` in citations, but that file was ingested and lives at `wiki/sources/2026-04-15-2026年1-3月中国外贸数据.md`. The `raw/wechat/` path is the pre-ingest location.

**Fix**: Replace with basename `[\[2026-04-15-2026年1-3月中国外贸数据\]]` or `[\[wiki/sources/2026-04-15-2026年1-3月中国外贸数据\]]`.

### H2. 4 references-to-non-existent guides in `wiki/references/`

`wiki/references/methodology-modes.md` and `wiki/references/transport-fallback.md` link to guides that don't exist as files:

| Missing guide | Referenced from |
|---|---|
| `[\[methodology-modes-guide\]]` | `wiki/references/methodology-modes.md` (×2) |
| `[\[wiki-mode\]]` | `wiki/references/methodology-modes.md` (×2) |
| `[\[wiki-cli\]]` | `wiki/references/transport-fallback.md` |
| `[\[mcp-setup\]]` | `wiki/references/transport-fallback.md` |

**Fix**: Either write the referenced docs as full pages, or rewrite the references to point at existing skills (`skills/wiki-mode/SKILL.md`, `skills/wiki-cli/SKILL.md`, `skills/wiki/references/mcp-setup.md`).

### H3. Path-prefix mismatch on `冲销式干预` (4 dead-link false negatives)

`[\[wiki/concepts/冲销式干预.md\]]` is referenced 4 times. The page **does exist** at `wiki/concepts/冲销式干预.md` but the `wiki/` prefix in the wikilink prevents Obsidian from resolving by basename.

**Fix**: Strip the `wiki/` prefix from these wikilinks to use `[\[冲销式干预\]]` form, matching Obsidian's basename resolution.

---

## MEDIUM Findings

### M1. 111 pages missing `tags` field

Distribution:
- ~85 in `wiki/sources/` (sources typically don't need tags, but convention in this vault has them)
- ~15 in `wiki/concepts/` (notable for cross-domain linkage)
- 2 in `wiki/references/` (`methodology-modes.md`, `transport-fallback.md`)
- ~9 scattered in `wiki/entities/`

**Fix**: Batch-add `tags: [entity]` (or `[concept]`, `[source]`) by type. Sources could use tags reflecting topic (e.g., `tags: [source, finance, china]`).

### M2. 9 pages missing `created` field — all are infrastructure

| Page | Why expected exempt |
|---|---|
| `wiki/hot.md` | meta, manually maintained |
| `wiki/getting-started.md` | meta |
| `wiki/log.md` | meta |
| `wiki/index.md` | meta |
| `wiki/references/methodology-modes.md` | reference |
| `wiki/references/transport-fallback.md` | reference |
| `wiki/concepts/_index.md` | _index |
| `wiki/sources/_index.md` | _index |
| `wiki/entities/_index.md` | _index |

**Fix**: Add `created` to the 2 reference pages and 3 _index pages. Leave meta files (hot, log, overview, index, getting-started) as expected-exempt.

### M3. 1 page missing `updated` — `wiki/references/methodology-modes.md`

**Fix**: Add `updated: 2026-06-24`.

### M4. Index freshness — `wiki/index.md` last updated 2026-04-07

`wiki/index.md` is dated 2026-04-07 but the vault has grown from 34 pages (then) to 497 (now). It references entities (Andrej Karpathy, Claude SEO) that are clearly not the financial-vault's main domain anymore.

**Fix**: Rewrite `wiki/index.md` as a domain-organized index for the financial knowledge base, OR explicitly mark it as "plugin template artifact" and supersede with a new `wiki/overview.md` navigation page.

---

## LOW Findings

### L1. Shadow banking page has many unlinked concept mentions

User is currently viewing `wiki/entities/影子银行.md`. Cross-reference check found 30+ financial terms (次贷危机, 资产证券化, MBS, CDO, 资管新规, 灰犀牛, etc.) mentioned in the body without `[\[wikilink\]]` markup. Related-links section at the bottom covers the major ones.

**Fix** (optional, readability improvement): Add wikilinks inline where useful. Low priority because the related-links section already provides navigation.

### L2. 293 pages without explicit `status`

Most are sources or concepts that mature via tag/folder rather than frontmatter status. Not blocking, but Dataview dashboards rely on `status` for filtering.

**Fix**: Decide on a vault-wide convention. Options:
- Add `status: developing` to all missing pages (cheap, dashboard-ready)
- Drop `status` from Dataview queries and use `tags` + `type` instead
- Use Obsidian Bases (newer plugin) which has its own status field

### L3. `wiki/concepts/主题页.md` is orphan by strict definition but new (<3d)

Auto-excluded from orphan list because recently modified. Watch list — if no inbound links appear within 2 weeks, mark for either linking or deletion.

---

## Cross-Reference Density (sample)

Top 10 pages by inbound link count (resolves link hygiene):

| Page | Inbound links |
|---|---|
| `wiki/sources/2026-04-15-2026年1-3月中国外贸数据.md` | high (raw imports + references) |
| `wiki/concepts/冲销式干预.md` | high |
| (many shadow-banking-related concepts) | moderate |

Note: actual counts available in `/tmp/lint_full.json` for further analysis.

---

## Address Validation

- Counter state: `3` (`.vault-meta/address-counter.txt`)
- Highest c- address observed: `c-000001`
- Pages with address: 1
- Post-rollout pages checked: N/A (only 1 page has address; rollout effectively dormant)
- Legacy pages pending backfill: N/A
- Address format errors: 0
- Address collisions: 0

**DragonScale is dormant in this vault.** See BLOCKER B1 — the underlying `flock` issue means address allocation cannot run anyway. Recommendation: explicitly retire DragonScale mechanisms OR install `flock` and run a backfill ingest pass.

---

## Semantic Tiling

**Skipped** — `ollama` not installed on this system. `scripts/tiling-check.py --peek` would exit 10 (`ollama unreachable`).

Recommendation: install ollama + `nomic-embed-text` model if duplicate-page detection is desired:

```bash
brew install ollama
ollama pull nomic-embed-text
# then:
bash scripts/tiling-check.py --report wiki/meta/tiling-report-2026-06-24.md
```

---

## Safe-to-Auto-Fix Summary

| Fix | Safe? | Notes |
|---|---|---|
| Add missing `tags` placeholder | Yes | type-based default tags |
| Add missing `created` to non-meta files | Yes | use file mtime |
| Add missing `updated` | Yes | today |
| Strip `wiki/` prefix from `冲销式干预` wikilinks | Yes | targeted replace |
| Replace `raw/wechat/X` with basename | Yes | files exist at sources/X |
| Replace `Clippings/X` with correct path | Review | need mapping table |
| Create stub pages for `[\[Wiki Map\]]`, `[\[dashboard\]]`, etc. | Review | decide on meaning first |
| Resolve `[\[notes/Foo\]]` placeholder | Yes | remove |

**Not auto-fixed**: dead links from template inheritance need a decision (create stub vs delete ref).

---

## Recommended Action Plan

1. **Fix `flock`** (BLOCKER): `brew install flock`. Required for any DragonScale work.
2. **Batch frontmatter patches** (1 hour): add tags/created/updated across the 121 affected pages.
3. **Path correction sweep** (30 min): fix `raw/wechat/...` and `wiki/concepts/X` prefix issues via grep+replace.
4. **Decide on Clippings mapping** (1 hour + judgment): for each `Clippings/X` reference, find the corresponding file in `raw/articles/` or `wiki/sources/` and rewrite. If unresolvable, remove the citation.
5. **Decide on DragonScale posture** (decision): either install flock + run backfill, or formally mark as not-in-use.
6. **Rewrite `wiki/index.md`** (1 hour): financial-vault specific, drop template-era references.
7. **Optional: cross-reference pass on `影子银行.md`** (15 min, educational benefit only).

---

## Methodology

- Frontmatter parser: strict YAML subset (top-level scalars + single-level lists)
- Wikilink extractor: `\[\[target(#anchor)?(|display)?\]\]`
- Orphan check: `>3 days old` to absorb recent ingest churn
- Dead link check: basename fallback + `wiki/` prefix resolution
- Tiling: skipped per ollama absence
- DragonScale counter: read directly from `.vault-meta/address-counter.txt` (lock-free)
- Full data dump: `/tmp/lint_full.json`
