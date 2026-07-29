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

> 老王暴躁体检报告。1017 页全量扫描，DragonScale 特性全开。**P0 BLOCKER 已全部修复**（地址冲突清零 + 特里芬合并 + c-000910/911 重分配）。剩余 P1-P3 待后续处理。

## Summary
- Pages scanned: **1017**（删特里芬 entities 旧版 -1，新建本报告 +1，净持平）
- Issues found: **708**（含噪音；精筛后真实内容死链仅 24 目标/48 处）
- **P0 Auto-fixed: 4 项** ✅
  - 清除 29 个 meta/fold 页误分配的 address 字段
  - 合并特里芬难题重复页（删 entities 旧版，concepts 版保留 c-000718）
  - 淡马锡重分配 c-001063（解 c-000910 冲突）
  - 研究页重分配 c-001064（解 c-000911 冲突）
- Needs review: P1-P3 待人工确认

| 维度 | 修复前 | 修复后 | 严重度 |
|------|------|------|--------|
| 孤儿页 | 0 | 0 | ✅ 优秀 |
| 地址冲突 | 9 组 | **0** ✅ | 🔴→✅ |
| 真实内容死链 | 24 目标 | 24 目标（P0未涉及） | 🟡 HIGH |
| Frontmatter 缺 tags | 200 核心页 | 200（P0未涉及） | 🟡 MEDIUM |
| 页面类型 | concept 518 / entity 394 / source 37 / meta 33 | 同上 | — |

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

## Address Validation（DragonScale Mechanism 2）—— ✅ 已修复

- Counter state: `1065`（修复后 `./scripts/allocate-address.sh --peek`，分配了 c-001063/c-001064 两次）
- 最高 c- 地址观测: c-001064
- Post-rollout pages checked: 1017 中绝大部分有地址 ✅
- Legacy pages pending backfill: 0
- **地址冲突: 0 组** ✅（修复前 9 组）

### 修复记录

| 地址 | 处理动作 | 结果 |
|------|---------|------|
| c-000907 | 删 `hot.md` address | 美元潮汐独占 ✅ |
| c-000908 | 删 `index.md` address | 美元周期独占 ✅ |
| c-000909 | 删 `log.md` address | 脆弱五国独占 ✅ |
| c-000910 | 淡马锡重分配 → c-001063 | 美元潮汐历史案例独占 c-000910 ✅ |
| c-000911 | 研究页重分配 → c-001064 | 主权财富基金独占 c-000911 ✅ |
| c-000912 | 删 `meta/2026-04-14-community-cta-rollout.md` address | GIC 独占 ✅ |
| c-000913 | 删 `meta/2026-04-15-release-report-session.md` address | 中投独占 ✅ |
| c-000914 | 删 `meta/2026-04-15-slides-and-release-session.md` address | 挪威主权基金独占 ✅ |
| c-000718 | 删 `entities/特里芬难题.md` 旧版 | concepts 版独占 ✅ |
| c-000915~930 段 | 批量删 25 个 meta 页 address | meta 页回归无地址状态 ✅ |

### 特里芬难题合并详情（c-000718）

- 删除：`wiki/entities/特里芬难题.md`（2026-05-21 旧 stub，developing，0 独有入链）
- 保留：`wiki/concepts/特里芬难题.md`（2026-07-17 完整版，current，5 个学术 source，10+ 入链）
- 所有 `[[特里芬难题]]` 简化名链接现正确解析到 concepts 版，零破坏。

## Frontmatter Gaps

- **606 页缺字段，全部是缺 `tags`**（200 页是核心内容页，其余 406 为 meta/session 类本可不强求）。
- 核心 200 页缺 tags 影响 Dataview 聚类与检索，**MEDIUM 级**。
- 其余必填字段（type/status/created/updated）全部齐全 ✅。

## Missing Cross-References / Stale Claims

本次未发现明显陈旧论断。近期页（美元潮汐系列、韩国股灾系列、化债系列）交叉引用密集，时序闭环良好（预警→兑现链清晰）。

## 修复优先级建议

| 优先级 | 动作 | 状态 |
|--------|------|------|
| P0 BLOCKER | 清除 25 个 meta 页 + hot/index/log 的 address 字段 | ✅ 已完成（29个文件） |
| P0 BLOCKER | 合并特里芬难题（删 entities 旧版） | ✅ 已完成 |
| P0 BLOCKER | c-000910 淡马锡重分配 c-001063 | ✅ 已完成 |
| P0 BLOCKER | c-000911 研究页重分配 c-001064 | ✅ 已完成 |
| P1 HIGH | 修韩国股灾/冷静冷静链接写法（改全 vault 引用） | ⏳ 待处理（~13 处） |
| P1 HIGH | 建 1997 亚洲金融危机、1992 欧洲货币危机 stub | ⏳ 待处理 |
| P2 MEDIUM | 补 200 核心页 tags | ⏳ 待处理 |
| P3 LOW | 清理低价值历史死链 / 改链同义页 | ⏳ 待处理 |

## Semantic Tiling

- 本轮 ollama tiling-check 未跑（需 `ollama pull nomic-embed-text`，本次跳过）。
- 手动识别并已处理 1 组语义重复：[[特里芬难题]] concepts vs entities（已合并）。

---

> [!note] 老王的话
> P0 全清！地址体系回归干净——9 组冲突归零，25 个 meta 页不再抢号，特里芬难题合并到唯一正本，淡马锡和研究页挪了新号。链接网络零孤儿、零新增死链。剩下的 P1（韩国链接写法 + 亚洲金融危机 stub）、P2（补 tags）你啥时候要治，喊老王一声接着干。
