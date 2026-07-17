---
type: concept
title: "E-commerce SEO"
address: c-000053
created: 2026-06-24
updated: 2026-06-24
tags: [concept]
status: developing
aliases:
  - "电商SEO"
  - "电商搜索优化"
---

# E-commerce SEO

> 针对在线零售网站的搜索引擎优化方法

**E-commerce SEO** 是 SEO 在电商场景下的专项应用,聚焦于产品页、品类页、购物体验的搜索可见性提升。

## 与通用 SEO 的差异

| 维度 | 通用 SEO | E-commerce SEO |
|---|---|---|
| 内容主体 | 信息型(博客、指南) | 产品型(PDP、PLP) |
| 关键词类型 | 信息查询(how、what) | 交易查询(buy、price、review) |
| 核心指标 | 流量、停留时间 | 转化率、客单价、GMV |
| 技术重点 | 内容质量、外链 | 结构化数据(Schema Product)、分面导航 |
| 内容策略 | 长文、教程 | 产品描述、用户评测 |

## 核心优化点

- **产品页 Schema 标记**:Product、Offer、AggregateRating 结构化数据
- **分面导航(Faceted Navigation)**:按品牌、价格、属性筛选的可索引 URL
- **长尾产品关键词**:型号、SKU、变体的精确匹配
- **用户生成内容(UGC)**:评测、问答对长尾关键词覆盖
- **重复内容管理**:同一产品的多 SKU、多 URL canonical 化
- **季节性页面**:节日、促销专题页的时效性优化

## Claude SEO 中的实现

Claude SEO 包含 E-commerce SEO 专项模块,自动检测产品页结构、提取分面导航建议、生成 Schema 标记模板。

## 相关条目

- [[wiki/entities/Claude SEO]] — Tier 4 Claude Code skill,包含 E-commerce SEO 模块
- [[wiki/concepts/Semantic Topic Clustering]] — 适用于 E-commerce 产品聚类
