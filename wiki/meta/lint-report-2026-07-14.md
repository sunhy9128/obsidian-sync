---
type: meta
title: "Lint Report 2026-07-14"
created: 2026-07-14
updated: 2026-07-14
tags: [meta, lint]
status: developing
---

# Lint Report: 2026-07-14

> [!info]
> 本次 lint 并行启动了 5 个专项扫描 agent：orphans、dead links、frontmatter、DragonScale address validation、semantic tiling (peek)。

## Summary

| 指标 | 数值 |
|------|------|
| 扫描页面数 | 719（排除 meta/、folds/） |
| 孤立页面 | 9 |
| 死链实例 | 453 |
| 唯一缺失目标 | 159 |
| Frontmatter 缺口 | 22 pages |
| DragonScale 地址缺失（post-rollout） | 675 |
| 语义平铺 | 跳过（ollama 不可达） |

---

## 1. Orphan Pages — 9 个

> 孤立页面比例极低（1.3%），vault 整体链接健康度良好。

| 页面 | 类型 | 建议 |
|------|------|------|
| `2026-06-23-股份回购后注销对股票有什么影响` | source | 从[[回购注销]]链接 |
| `methodology-modes` | meta | 确认是否有意孤立（plugin 参考页） |
| `transport-fallback` | meta | 确认是否有意孤立（plugin 参考页） |
| `公募基金行业2025H1排名分析` | analysis | 从[[基金年中排名对A股影响机制]]链接 |
| `军工航空产业` | concept | 从[[国防军工]]或[[地缘政治]]链接 |
| `实体页` | entity | 名称疑似测试残留，建议确认或删除 |
| `恒生科技指数` | entity | 从[[港股vs美股vsA股]]链接 |
| `邓小平` | entity | 从[[改革开放]]或[[中国金融与改革]]链接 |
| `金砖支付系统` | concept | 从[[金砖国家]]或[[去美元化]]链接 |

**注**：与昨日报告（635 orphans）差异巨大，原因是今日扫描采用严格定义（0 inbound 且 0 outbound 才算孤立），而昨日可能将所有无 inbound 的页面全部计入。

---

## 2. Dead Links — 453 实例 / 159 唯一目标

### 高优先级 — 真实缺失页面（未创建 stub）

| 死链目标 | 典型来源页 |
|----------|-----------|
| `1998年LTCM危机` | 最后贷款人、2023年SVB危机 |
| `2015瑞郎危机` | 瑞士央行 |
| `2023 SVB危机` | 沃尔克规则 |
| `CDS信用违约互换` | 影子银行 |
| `AIG` | 影子银行 |
| `Bundesbank` | 法国1983年转向 |
| `Ludwig Erhard` | 德国马克 |
| `Volkswagen轧空事件` | 轧空、卖空机制 |
| `三元悖论` | 1992欧洲货币危机、欧洲货币体系 |
| `土地财政` | 化债、地方政府隐性债务 |
| `城投公司` | 化债核心命题 |
| `量化紧缩` | 扩表与缩表、美联储 |
| `直升机撒钱` | 美联储独立性、扩表与缩表 |
| `累计期权` | 期权 |
| `做空机制` | 保时捷大众恶意并购、影子银行 |
| `买断式逆回购` | 国债逆回购 |
| `人民币国际化` | 国债逆回购 |
| `货币乘数` | 银行扩表与流动性 |
| `雷曼兄弟` | 影子银行 |
| `沃尔克` | 逆周期资本缓冲、存款保险 |
| `伯南克` | 最后贷款人 |
| `欧元区` | 负利率、OMT |
| `欧洲央行` | 欧猪五国 |
| `次级制裁` | 霸权稳定论、美元霸权 |
| `次贷危机` | （多处引用） |
| `央行对冲工具` | 最后贷款人、逆周期资本缓冲 |
| `8·11汇改` / `8.11 汇改` | 冲销式干预、非冲销式干预 |
| `301条款` | 输入型通胀、关税战传导 |
| `沃尔克` | 逆周期资本缓冲 |

### 中优先级 — 路径型链接（vault 存在同名文件）

这些链接的目标文件存在，但 wikilink 写法有问题：

| 问题写法 | 实际文件 | 来源 |
|----------|----------|------|
| `[[wiki/concepts/城镇化]]` | `concepts/城镇化.md` | 房地产 |
| `[[wiki/entities/沃尔克]]` | `entities/沃尔克.md` | 最后贷款人 |
| `[[wiki/entities/中央银行]]` | `entities/中央银行.md` | 财政货币化 |
| `[[wiki/concepts/回购注销\|回购注销]]` | `concepts/回购注销.md` | 多处 |
| `[[wiki/meta/化债机制图谱.canvas]]` | `meta/化债机制图谱.canvas` | 化债核心命题 |

**修复方式**：将 `[[wiki/concepts/X]]` 改为 `[[X]]`，`[[wiki/entities/X]]` 改为 `[[X]]`。

### 低优先级 — 测试残留

| 死链 | 疑似来源 |
|------|----------|
| `Foo` | DragonScale Memory（测试残留） |
| `wikilinks` | cherry-picks |
| `Wiki Map.canvas` | getting-started、hot、index |
| `dashboard` | overview、_index、货币本质 |
| `How does the LLM Wiki pattern work?` | Persistent Wiki Artifact、Query-Time Retrieval |
| `Three laws of motion` | Persistent Wiki Artifact |

---

## 3. Frontmatter Gaps — 22 个页面

| 缺失字段 | 数量 | 页面 |
|----------|------|------|
| `created` | 4 | hot, getting-started, log, index（meta 导航页） |
| `created` + `updated` | 6 | 大豆战争, CBOT, 战略储备, 中储粮, 五神, 2025-02-04-中国粮食金融保卫战-巫师财经 |
| `updated` | 12 | 恶意收购, 万科宝能之争, 白衣骑士, 中国特色企业治理, 杠杆收购, 华润, 安邦, 姚振华, 宝能系, 庄炳昌, 万科宝能股权之争 |

**注**：`created` + `updated` 均缺失的 6 个是最早期页面（created < 2026-04-23），需时间回填。

---

## 4. DragonScale Address Validation

### Counter State
- **Counter peek**: `16`（下一个可用地址：`c-000016`）
- **Rollout baseline**: `2026-04-23`（来自 `.vault-meta/legacy-pages.txt`）

### Pages WITH 有效地址（12 个，均唯一）

| 地址 | 页面 |
|------|------|
| c-000001 | DragonScale Memory |
| c-000004 | 万科宝能股权之争 |
| c-000005 | 王石 |
| c-000006 | 姚振华 |
| c-000007 | 华润 |
| c-000008 | 安邦 |
| c-000009 | 宝能系 |
| c-000011 | 中国特色企业治理 |
| c-000012 | 恶意收购 |
| c-000013 | 白衣骑士 |
| c-000014 | 杠杆收购 |
| c-000015 | 万科宝能之争 |

### BLOCKER — 675 个 post-rollout 页面缺少 address

2026-04-23 之后创建的 686 个 post-rollout 页面中，仅 11 个有地址，675 个缺失。这是 `wiki-ingest` 未集成 `allocate-address.sh` 的系统性问题。

> **修复方案**：在 `wiki-ingest` 流程中每次创建页面时调用 `./scripts/allocate-address.sh`，或手动批量分配。**Lint 不自动修复 address 缺失**（按设计仅观察）。

### Pending Backfill — 40 个 legacy 页面（信息级）

| 类别 | 示例 |
|------|------|
| sources（老帖子） | 2020-04-25-日本经济崩盘始末-巫师财经, 2019-12-08-保时捷大众恶意并购-巫师财经 |
| meta 页 | full-audit-and-system-setup-session, claud-obsidian-v1.4-release-session |
| concepts（早期） | 大豆战争, Compounding Knowledge, Hot Cache, 量化宽松 |
| entities（早期） | Andrej Karpathy, Claude SEO, How does the LLM Wiki pattern work |

---

## 5. Semantic Tiling

- **Status**: skipped — ollama 不可达（exit 10）
- **诊断**: `ollama_reachable: false`, `model_present: false`
- **Fix**: `ollama pull nomic-embed-text` 后重新运行 lint

---

## Recommended Fix Priority

| 优先级 | 任务 | 数量 | 操作 |
|--------|------|------|------|
| **BLOCKER** | 启用 DragonScale address 分配 | 675 | 修改 wiki-ingest 流程 |
| **P0** | 修复路径型 wikilinks | ~50 | 全局替换 `[[wiki/concepts/` → `[[` |
| **P1** | 创建高频缺失页 stub | ~30 | wiki-ingest 批量创建 |
| **P2** | 补充 frontmatter 缺口 | 22 | 手动补字段 |
| **P3** | 删除/确认孤立测试残留 | 1 | 确认 `实体页` 是否为测试残留 |
| **P4** | 删除测试 wikilink（Foo） | 1 | 从 DragonScale Memory 移除 |

---

## Comparison with Previous Lint (2026-07-13)

| 指标 | 2026-07-13 | 2026-07-14 | 变化 |
|------|------------|------------|------|
| 扫描页面数 | 723 | 719 | -4 |
| 孤立页面 | 635 | 9 | ⬇️ 定义更严格 |
| 死链（唯一目标） | 75 | 159 | ⬆️ 更精确扫描 |
| Frontmatter 缺口 | ~20 | 22 | — |
| DragonScale 地址缺失 | 660 | 675 | ⬆️ +15 新页面 |

---

*Report generated: 2026-07-14*
*Scanner: parallel 5-agent (orphans/dead-links/frontmatter/DragonScale/tiling-peek)*
