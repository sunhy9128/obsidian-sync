---
type: meta
title: "Lint Report 2026-07-14"
created: 2026-07-14
updated: 2026-07-14
tags: [meta, lint]
status: developing
---

# Lint Report: 2026-07-14

## Summary

- Pages scanned: 734 (wiki/, concepts/, entities/, excluding wiki/meta/)
- Issues found: ~1,460
- Auto-fixed (this session): 15 stub pages created for `2013年钱荒` dead links
- Needs review: ~1,445

> [!info]
> 本次lint并行启动了4个检查agent（orphans、dead links、frontmatter、empty sections），以及DragonScale和semantic tiling两项专项检查。

### Issue Breakdown

| 类别 | 数量 | 优先级 |
|------|------|--------|
| 孤儿页 (orphans) | 635 | MEDIUM |
| 死链 (dead links) | 75 unique targets, 200+ refs | HIGH |
| Frontmatter 缺口 | 20 | LOW |
| 空章节 (empty sections) | 1,530 instances in 275 files | HIGH |
| DragonScale address | 660 post-rollout pages missing address | BLOCKER |
| Semantic tiling | skipped (ollama unreachable) | LOW |

---

## 1. Orphan Pages (635 / 83.9%)

> [!warning]
> 孤儿页比例极高(83.9%)，但多数是source导入页面天然缺乏内部交叉引用，非结构错误。

### 完全孤立 (0 inbound + 0 outbound) — 3 pages
- `meta/retrieval-benchmark-v1.7`
- `meta/tiling-report-2026-04-24`
- `strategies/_index`

### 分布
| 目录 | 孤儿数 |
|------|--------|
| concepts/ | 287 |
| entities/ | 282 |
| sources/ | 24 |
| meta/ | 23 |
| comparisons/ | 4 |
| analysis/ | 3 |
| references/ | 2 |
| questions/ | 2 |
| strategies/ | 1 |

**建议:** 优先处理 crisis history (1992欧洲货币危机、1997亚洲金融危机、2008全球金融危机等) → monetary policy (利率走廊、SHIBOR、DR007等) → regulatory reform (资管新规、8号文等) 的交叉链接。

---

## 2. Dead Links (75 unique targets)

### 高优先级 — 真实缺失页面 (stub未创建)

| 死链 | 被引用页面 (部分) |
|------|-----------------|
| `1998年LTCM危机` | 2023年SVB危机, 最后贷款人 |
| `2015瑞郎危机` | 瑞士央行 |
| `2023 SVB危机` | 沃尔克规则 |
| `CDS信用违约互换` | 影子银行 |
| `CIPS` | 国债逆回购, 美元霸权 |
| `SDR` | 巴塞尔协议III, IMF |
| `TARGET2` | (multiple lint-reports) |
| `AIG` | 影子银行 |
| `Bundesbank` | 法国1983年转向 |
| `Ludwig Erhard` | 德国马克 |
| `Volkswagen轧空事件` | 轧空, 卖空机制 |
| `三元悖论` | 1992欧洲货币危机, 欧洲货币体系 |
| `土地财政` | 化债, 地方政府隐性债务 |
| `城投公司` | 化债核心命题 |
| `量化紧缩` | 扩表与缩表, 美联储 |
| `直升机撒钱` | 美联储独立性, 扩表与缩表 |
| `巴塞尔协议` | 逆周期资本缓冲, 沃尔克规则 |
| `累计期权` | 期权 |
| `做空机制` | 保时捷大众恶意并购, 影子银行 |
| `做空CDS` | 影子银行 |
| `买断式逆回购` | 国债逆回购 |
| `人民币国际化` | 国债逆回购 |
| `货币乘数` | 银行扩表与流动性 |
| `雷曼兄弟` | 影子银行 |
| `沃尔克` | 逆周期资本缓冲, 存款保险 |
| `伯南克` | 最后贷款人 |
| `欧元区` | 负利率, OMT |
| `欧洲央行` | 欧猪五国 |
| `次级制裁` | 霸权稳定论, 美元霸权 |
| `次贷危机` | (multiple) |

### 高优先级 — 畸形链接 (数据损坏)

| 死链 | 疑似来源 |
|------|---------|
| `MLFconcepts/OMT` | 源码中链接拼接损坏 |
| `PSLconcepts/QE与化债对比` | 源码中链接拼接损坏 |
| `X` | 测试残留或损坏 |
| `...` | 测试残留或损坏 |

### 中优先级 — 路径型链接 (basename-only)

以下链接仅用文件名但Vault中有多个同名文件或路径不完整：
`[[SLF]]`、`[[SLF]]`、`[[MLF]]`、`[[PSL]]` 等指向 `[[wiki/concepts/SLF]]` 但实际应为 `[[wiki/concepts/SLF|SLF]]`

---

## 3. Frontmatter Gaps (20 files)

| 缺失模式 | 数量 | 文件 |
|----------|------|------|
| `created` + `updated` | 5 | CBOT, 大豆战争, 战略储备, 中储粮, 五神 |
| `created` | 4 | getting-started, hot, index, log (meta页) |
| `updated` | 11 | 万科宝能之争, 中国特色企业治理, 恶意收购, 杠杆收购, 白衣骑士, 华润, 姚振华, 安邦, 宝能系, 庄炳昌, 王石 |

**观察:** 11个`updated`缺失全是entity页面(宝能系相关群)，可能是同一批导入但漏填。5个同时缺`created`+`updated`是最早期页面，需时间回填。

---

## 4. Empty Sections (1,530 instances in 275 files)

> [!alert]
> 275个文件有1,530个空章节。其中15个文件各有13-15个空章节，是重大内容缺口。

### Top offenders (13+ empty sections each)

| 文件 | 空章节数 |
|------|----------|
| concepts/交易成本与科斯定理 | 15 |
| concepts/巴塞尔协议III | 14 |
| concepts/沃尔克规则 | 14 |
| entities/索罗斯 | 13 |
| concepts/长期资本管理公司 | 13 |
| concepts/最后贷款人 | 13 |
| concepts/希腊字母 | 13 |
| concepts/套期保值 | 13 |
| concepts/基差风险 | 13 |
| concepts/动态对冲 | 13 |
| concepts/期权 | 13 |
| concepts/2020年3月流动性危机 | 13 |
| concepts/2008全球金融危机 | 13 |
| concepts/1997亚洲金融危机 | 13 |
| concepts/1992欧洲货币危机 | 13 |

**模式:** 使用"一、二、三..."或"第X节"结构但章节内容完全缺失。这些页面需要大量内容填充，不是简单的模板残留。

---

## 5. DragonScale Address Validation

- **DragonScale: enabled**
- Counter state: `16` (next available: `c-000016`)
- Highest c- address: `c-000015` (12 pages total)

### BLOCKER — 660 post-rollout pages without address

> [!danger]
> 2026-04-23之后创建的660个页面全部缺少address字段。这是`wiki-ingest`未启用`allocate-address.sh`的系统性问题。
>
> **修复:** 需要在`wiki-ingest`流程中集成`./scripts/allocate-address.sh`，或手动批量分配。**Lint不自动修复address缺失**（按设计仅观察）。

### Legacy pages pending backfill: 34
(created < 2026-04-23, informational only)

---

## 6. Semantic Tiling

- **Status:** skipped — ollama not reachable (exit 10)
- **Fix:** `ollama pull nomic-embed-text` then re-run lint

---

## Recommended Fix Priority

| 优先级 | 任务 | 数量 | 操作 |
|--------|------|------|------|
| **BLOCKER** | 启用DragonScale address分配系统 | 660 | 修改wiki-ingest流程 |
| **P0** | 修复畸形链接 (`MLFconcepts/OMT`等) | 4 | 找到源文件修正 |
| **P0** | 填充top-15空章节文件 | 15文件×13+节 | 人工内容填充 |
| **P1** | 创建高频缺失页stub | ~30 | wiki-ingest批量创建 |
| **P2** | 补充frontmatter缺口 | 20 | 手动补字段 |
| **P3** | 系统性孤儿页交叉链接 | 635 | 分批次添加入站链接 |
| **P4** | 删除测试残留 (`[[Foo]]`, `[[X]]`) | 2 | 手动删除 |

---

## Auto-Fix Log (This Session)

| 时间 | 操作 | 结果 |
|------|------|------|
| 2026-07-14 | 为`2013年钱荒.md`创建15个stub页面 | ✅ 完成 |

创建的stub页面：
- concepts: 2023年化债, 8号文, DR007, SHIBOR, SLF, SLO, 货币基金, 资管新规, 金融脱媒, 利率市场化
- entities: 周小川, 银监会, 光大银行, 天弘基金, 阿里巴巴

---

*Report generated: 2026-07-14*
*Scanner: parallel 4-agent (orphans/dead-links/frontmatter/empty-sections) + DragonScale + tiling-check*
