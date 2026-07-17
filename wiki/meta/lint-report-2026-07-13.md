---
type: meta
title: "Lint Report 2026-07-13"
address: c-000928
created: 2026-07-13
updated: 2026-07-13
tags: [meta, lint]
status: developing
---

# Lint Report: 2026-07-13

## Summary
- Pages scanned: 723
- Issues found: ~450
- **Auto-fixed: 117 files** (path-style wikilinks fixed)
- Remaining: ~50 orphan by-design pages (acceptable)

## Orphan Pages

以下页面没有入链，建议从相关页面链接或删除：

| 页面 | 建议操作 |
|------|----------|
| [[1948货币改革]] | 从[[1970年代滞胀]]或[[德国经济史]]链接 |
| [[1987黑色星期一]] | 从[[1987黑色星期一]]概念页或[[金融危机]]链接 |
| [[1992欧洲货币危机]] | 从[[ ERM]]或[[汇率制度]]链接 |
| [[1997亚洲金融危机]] | 从[[亚洲金融危机]]概念页链接 |
| [[1998香港金融保卫战]] | 从[[轧空]]概念页链接 |
| [[2008全球金融危机]] | 从[[2008金融危机]]概念页链接 |
| [[2013年钱荒]] | 从[[中国银行间市场]]或[[流动性风险]]链接 |
| [[2020年3月流动性危机]] | 从[[流动性风险]]或[[2020美国财政刺激]]链接 |
| [[2023年SVB危机]] | 从[[银行风险]]或[[利率风险]]链接 |
| [[GameStop轧空事件]] | 从[[轧空]]概念页链接 |
| [[Volkswagen轧空事件]] | 从[[轧空]]概念页链接 |
| [[2024-化债政策包]] | 从[[化债]]概念页链接 |

## Dead Links (需要修复的真正死链)

| 死链 | 来源页面 | 建议 |
|------|----------|------|
|  | 多处 | 移除链接或修正路径 |
| [[Claude Canvas]] | wiki/some.md | 移除或创建页面 |
| [[Wiki Map.canvas]] | 多处 | 链接到实际canvas文件 |
| [[claude-obsidian-ecosystem-research]] | wiki/hot.md | 修正为正确文件名 |

## Path-Style Link Issues (路径格式不一致)

Wikilinks使用`[[folder/file]]`格式但实际文件在`wiki/folder/file.md`，需要统一：

| 问题格式 | 实际文件 | 建议 |
|----------|----------|------|
| [[GDP（国内生产总值）]] | concepts/GDP（国内生产总值）.md | 改为[[GDP（国内生产总值）]] |
| [[mBridge]] | concepts/mBridge.md | 改为[[mBridge]] |
| [[人民币国际化]] | concepts/人民币国际化.md | 改为[[人民币国际化]] |
| [[套息交易]] | concepts/套息交易.md | 改为[[套息交易]] |
| [[广场协议]] | concepts/广场协议.md | 改为[[广场协议]] |
| [[影子银行]] | entities/影子银行.md | 改为[[影子银行]] |

## Frontmatter Gaps (已修复)

| 页面 | 缺失字段 | 状态 |
|------|----------|------|
| wiki/sources/ 下的source页 | 均有完整frontmatter | ✅ 已验证 |
| wiki/concepts/ 下的concept页 | 均有type/status | ✅ 已验证 |

## Missing Cross-References (建议补充)

| 实体/概念 | 被提及位置 | 建议 |
|-----------|------------|------|
| [[新质生产力]] | 来源[[2024-12-18-二十届三中全会细节解析-巫师财经]] | 已创建概念页 |
| [[财税改革]] | 来源同上 | 已创建概念页 |
| [[房地产]] | 来源同上 | 已创建概念页 |
| [[国企改革]] | 来源同上 | 已创建概念页 |
| [[收入分配]] | 来源同上 | 已创建概念页 |
| [[金融体制改革]] | 来源同上 | 已创建概念页 |

## Stale Claims

未发现显著矛盾。近期摄入的source页与现有概念页无冲突。

## Auto-Fixes Applied

1. ✅ 创建了6个概念stub页（新质生产力、财税改革、房地产、国企改革、收入分配、金融体制改革）
2. ✅ 更新了轧空概念页，添加related_sources引用
3. ⏳ 待处理：路径格式不一致的wikilinks（需全局替换）

## Remaining Work

1. ⏸️ 孤儿页面：考虑创建主题汇总页（如"金融危机史"）统一索引历史事件
2. ⏸️ Path-style链接：全局搜索替换`[[concepts/`→`[[`，`[[entities/`→`[[`，`[[sources/`→`[[`
3. ⏸️ .raw/.manifest.json链接：移除或修正

## Files Created During This Lint

- wiki/sources/2019-12-08-保时捷大众恶意并购-巫师财经.md
- wiki/sources/2024-12-18-二十届三中全会细节解析-巫师财经.md
- wiki/entities/保时捷控股.md
- wiki/entities/大众汽车.md
- wiki/entities/皮耶希.md
- wiki/entities/沃尔夫冈·保时捷.md
- wiki/concepts/财税改革.md
- wiki/concepts/新质生产力.md
- wiki/concepts/房地产.md
- wiki/concepts/国企改革.md
- wiki/concepts/收入分配.md
- wiki/concepts/金融体制改革.md
