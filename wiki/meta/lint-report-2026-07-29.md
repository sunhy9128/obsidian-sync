---
type: meta
title: "Lint Report 2026-07-29"
created: 2026-07-29
updated: 2026-07-29
tags: [meta, lint]
status: current
related:
  - "[[index]]"
  - "[[log]]"
---

# Lint Report: 2026-07-29

> 老王暴躁体检报告。1017 页全量扫描，DragonScale 特性全开。本次重灾区：地址冲突 + 真实死链。

## Summary
- Pages scanned: **1017**
- Issues found: **716**（含噪音后真实约 **305**）
- Auto-fixed: 0（等批准）
- Needs review: 全部待人工确认

| 维度 | 数量 | 严重度 |
|------|------|--------|
| 孤儿页 | 0 | ✅ 优秀 |
| 死链目标 | 101（真实死链 100，噪音 11） | 🔴 HIGH |
| Frontmatter 缺字段 | 606（全部缺 tags） | 🟡 MEDIUM |
| 地址冲突 | 9 组 | 🔴 BLOCKER |
| 页面类型分布 | concept 518 / entity 395 / source 37 / meta 33 | — |
| 状态分布 | developing 417 / stub 258 / current 256 / evergreen 50 | — |

## Orphan Pages
无。链接网络健康，零孤儿。这点做得漂亮，没让老王骂街。

## Dead Links

### 真实死链 TOP（需处理）

**A. 链接写法不规范（source 页带日期前缀，引用却用简化名）—— 改链即修**
- `[[韩国股灾简史]]`（8 处）：实际文件 `wiki/sources/2026-07-21-韩国股灾简史.md`。引用方：`韩国历史股灾谱系`、`韩国折价（Korea Discount）`、`SK海力士`、`hot.md`、`log.md` 等。**建议**：要么全 vault 改用 `[[2026-07-21-韩国股灾简史]]`，要么给 source 页建 alias / 或重命名去前缀。
- `[[韩国需要冷静冷静]]`（5 处）：实际文件 `wiki/sources/2026-06-24-韩国需要冷静冷静.md`。同上。

**B. 高价值缺失页（多页引用，该建 stub）**
- `[[1997 亚洲金融危机]]`（9 处真实引用）：被 `Original Sin（原罪）`、`美元周期`、`美元收割全球的机制`、`美元潮汐历史案例` 等核心页引用。**建议建 concept 页**——这是美元潮汐史的核心案例。
- `[[1992 欧洲货币危机]]`（3 处真实）：被 `美元潮汐历史案例`、`log.md` 引用。**建议建 concept 页**。
- `[[美联储点阵图]]`（2 处真实）：被 `货币政策与中央银行` domain 页引用。**建议建 concept stub**。
- `[[微盘股指数]]`（1 处真实 + meta 噪音）：被 `2026-06-24-4000亿回购竟然是真的` 引用。建议建 stub 或改链到已有 A 股指数页。

**C. 历史遗留死链（低优先级）**
- `[[中国经济]]`、`[[BRICS Pay]]`、`[[2023 SVB危机]]`、`[[《环球时报》]]`、`[[共建"一带一路"]]`、`[[一带一路]]`、`[[中华人民共和国国务院]]`、`[[中华人民共和国中央人民政府]]`、`[[Ludwig Erhard]]`、`[[TARGET2]]` 等：各 1-2 处引用，部分有同义页可改链（如 `一带一路`→已有相关页）。

### 噪音死链（不需处理）

- `[[meta/dashboard]]`、`[[meta/lint-report-*]]`、`[[Entities]]`/`[[Sources]]`/`[[Concepts]]`（_index 互链用大写标题）、`[[Claude Canvas]]`、`[[How does the LLM Wiki pattern work?]]` 等：均为 meta 页之间的自引用或 lint 报告历史记录，**非真实内容死链**，本次忽略。
- `[[raw/wechat/*]]`：指向 `.raw/` 原始区的链接，按 vault 规则 `.raw/` 不属 wiki 内容，忽略。

## Address Validation（DragonScale Mechanism 2）—— 🔴 BLOCKER

- Counter state: `1063`（`./scripts/allocate-address.sh --peek`）
- 最高 c- 地址观测: c-000940（本报告）
- Post-rollout pages checked: 1017 中绝大部分有地址 ✅
- Legacy pages pending backfill: 0

### 9 组重复地址（核心问题）

**根因**：8 个号段（c-000907~c-000914）被 meta 页 / fold 页 / 实体页 / 概念页**双重占用**。按 DragonScale 规则，meta 页和 fold 页（index/hot/log）**本就不该有 address 字段**，是历史误分配。

| 地址 | 不该有的一方（建议删 address） | 合法保留方 |
|------|------------------------------|-----------|
| c-000907 | `wiki/hot.md`（fold 页） | `wiki/concepts/美元潮汐.md` |
| c-000908 | `wiki/index.md`（fold 页） | `wiki/concepts/美元周期.md` |
| c-000909 | `wiki/log.md`（fold 页） | `wiki/concepts/脆弱五国（Fragile Five）.md` |
| c-000910 | `wiki/meta/2026-04-10-backlink-empire-session.md` + `wiki/entities/淡马锡.md` 之一 | `wiki/concepts/美元潮汐历史案例.md`（或淡马锡） |
| c-000911 | `wiki/meta/2026-04-14-claude-seo-v190-session.md` | `wiki/concepts/主权财富基金.md` 或 `wiki/questions/研究：美元如何收割新兴市场.md` 二选一 |
| c-000912 | `wiki/meta/2026-04-14-community-cta-rollout.md` | `wiki/entities/GIC.md` |
| c-000913 | `wiki/meta/2026-04-15-release-report-session.md` | `wiki/entities/中投.md` |
| c-000914 | `wiki/meta/2026-04-15-slides-and-release-session.md` | `wiki/entities/挪威主权基金.md` |

**另有 25 个 meta 页带了 address 字段**（c-000910~c-000930 段），全部违反"meta 页排除"规则，建议批量清除 address 字段。

### 特里芬难题重复页（c-000718）—— 语义重复需合并

- `wiki/concepts/特里芬难题.md`：2026-07-17 更新，current，5 个学术 source，内容完整。**入链 10+**（hot、domains、美元潮汐系列、研究页等均指向它）。
- `wiki/entities/特里芬难题.md`：2026-05-21 旧版，developing，内容是早期 stub。
- **建议**：删除 entities 旧版，concepts 版为唯一正本。两者同 type=entity 同地址，是纯重复。

## Frontmatter Gaps

- **606 页缺字段，全部是缺 `tags`**（200 页是核心内容页，其余 406 为 meta/session 类本可不强求）。
- 核心 200 页缺 tags 影响 Dataview 聚类与检索，**MEDIUM 级**。
- 其余必填字段（type/status/created/updated）全部齐全 ✅。

## Missing Cross-References / Stale Claims

本次未发现明显陈旧论断。近期页（美元潮汐系列、韩国股灾系列、化债系列）交叉引用密集，时序闭环良好（预警→兑现链清晰）。

## 修复优先级建议

| 优先级 | 动作 | 影响页数 | 风险 |
|--------|------|---------|------|
| P0 BLOCKER | 清除 25 个 meta 页 + hot/index/log 的 address 字段 | ~28 | 低（meta 页本不该有） |
| P0 BLOCKER | 合并特里芬难题（删 entities 旧版） | 1 删 | 低（入链全指向 concepts 版） |
| P0 BLOCKER | c-000911 二选一：主权财富基金 vs 研究页 | 1 | 需判断 |
| P1 HIGH | 修韩国股灾/冷静冷静链接写法（改全 vault 引用） | ~13 处 | 低 |
| P1 HIGH | 建 1997 亚洲金融危机、1992 欧洲货币危机 stub | 2 建 | 低 |
| P2 MEDIUM | 补 200 核心页 tags | 200 | 低但量大 |
| P3 LOW | 清理低价值历史死链 / 改链同义页 | ~15 | 低 |

## Semantic Tiling

- 本轮 ollama tiling-check 未跑（需 `ollama pull nomic-embed-text`，本次跳过）。
- 但已手动识别 1 组语义重复：[[特里芬难题]] concepts vs entities（见上）。

---

> [!note] 老王的话
> 链接网络零孤儿、frontmatter 必填字段齐全，底子不错。但地址体系串号了——meta 页不该抢号却抢了 25 个，还和实体页撞车 8 处。死链里韩国那俩是写法不规范，1997/1992 亚洲金融危机是真该补的核心案例页。要修哪几档，你拍板。
