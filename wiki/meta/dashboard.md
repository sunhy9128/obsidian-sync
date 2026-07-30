---
type: meta
title: "Dashboard"
updated: 2026-07-30
tags:
  - meta
  - dashboard
status: evergreen
related:
  - "[[index]]"
  - "[[overview]]"
  - "[[log]]"
  - "[[_index]]"
  - "[[Compounding Knowledge]]"
---

# Wiki Dashboard

Navigation: [[index]] | [[overview]] | [[log]] | [[hot]]

The dashboard uses **Obsidian Bases**. A core Obsidian feature shipped in v1.9.10 (August 2025). No plugin install required.

> [!tip] Embedded Bases view
> The interactive dashboard lives in [[dashboard.base]]. Open that file directly, or use the embed below.

![[dashboard.base]]

---

## Legacy Dataview Dashboard (Optional)

If you are on Obsidian < 1.9.10 or prefer Dataview, the queries below still work. Just install the Dataview community plugin.

### Recent Activity

```dataview
TABLE type, status, updated FROM "wiki" SORT updated DESC LIMIT 15
```

### Seed Pages (Need Development)

```dataview
LIST FROM "wiki" WHERE status = "seed" SORT updated ASC
```

### Entities Missing Sources

```dataview
LIST FROM "wiki/entities" WHERE !sources OR length(sources) = 0
```

### Open Questions

```dataview
LIST FROM "wiki/questions" WHERE status = "developing" OR status = "seed" SORT updated DESC
```

### Comparisons

```dataview
TABLE verdict FROM "wiki/comparisons" SORT updated DESC
```

### Sources

```dataview
TABLE author, date_published, updated FROM "wiki/sources" WHERE type = "source" SORT updated DESC LIMIT 10
```

### Pages Missing Status（2026-07-30 Lint: 0 pages ✅）

```dataview
LIST FROM "wiki" WHERE !status AND type != "meta" LIMIT 50
```

### Orphan Pages（2026-07-30 Lint: 0 pages ✅）

```dataview
LIST FROM "wiki" WHERE length(filter(file.inlinks, (l) => true)) = 0 AND type != "meta" SORT updated DESC
```

### Pages Missing Tags（2026-07-30 Lint: 610 核心内容页 🟡 MEDIUM）

```dataview
LIST FROM "wiki" WHERE (!tags OR length(tags) = 0) AND type != "meta" AND type != "fold" SORT updated DESC LIMIT 50
```

### YAML-Error Pages（2026-07-30 Lint: 0 ✅）

```dataview
LIST FROM "wiki" WHERE string(file.ctime) = "" OR file.mtime = null
```

> [!note] Lint 状态（2026-07-30）
> 地址体系干净（985 地址零冲突）｜ 零孤儿 ｜ 真死链仅 4 处（详见 [[lint-report-2026-07-30]]）｜ 610 核心页缺 tags 待补。注：历史 lint-scan.py 不认 alias，死链数含大量误报，已在新报告中纠偏。
