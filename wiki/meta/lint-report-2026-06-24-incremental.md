---
type: meta
title: "Lint Report 2026-06-24 (Incremental)"
created: 2026-06-24
updated: 2026-06-24
tags: [meta, lint, incremental]
status: developing
related:
  - "[[Wiki Map.canvas]]"
  - "[[index]]"
  - "[[log]]"
  - "[[hot]]"
  - "[[lint-report-2026-06-24]]"
---

# Lint Report: 2026-06-24 (Incremental)

> **本次扫描范围**:2026-06-24 当日摄取 / 修改的 11 个页面(不含早上的全量 497 页报告)
> **上游报告**:`[[lint-report-2026-06-24]]`(全量 497 页扫描,1 BLOCKER + 3 HIGH + 4 MEDIUM + 3 LOW)

## 增量摘要

| Metric | Count |
|---|---|
| 新增 source 页 | 1 |
| 新增 concept 页 | 2 |
| 新增 entity 页 | 8 |
| 修改已有页 | 7(moomoocat / 美以伊战争 / 霍尔木兹海峡 / 伊朗 / 特朗普 / AI虹吸 / 加息预期) |
| 新增 wikilink 数 | ~70 |
| 死链 | **2**(MEDIUM) |
| 前向 source_file 引用 | 1(LOW,raw 文件尚未保存) |
| 跨引用覆盖率 | 95% |
| Frontmatter 完整度 | 100%(10/10 新页面符合规范) |
| Orphan(无入站链接) | 0(全部新页面均被 moomoocat 或 source 页引用) |

---

## 新增页面清单(11)

### Source(1)
- `wiki/sources/2026-06-15-美伊MoU签署与全球狂欢.md`

### Concepts(2)
- `wiki/concepts/美伊备忘录.md` — `status: developing`
- `wiki/concepts/微盘股.md` — `status: developing`

### Entities(8)
- `wiki/entities/2026年世界杯.md`
- `wiki/entities/UFC白宫站.md`
- `wiki/entities/佩雷拉(UFC).md`
- `wiki/entities/托普利亚(UFC).md`
- `wiki/entities/库拉索.md`
- `wiki/entities/国足.md`
- `wiki/entities/华夏基金.md`
- `wiki/entities/国证有色指数.md`

### 已修改(7)
- `wiki/entities/moomoocat.md` — 增加 6-15 文章到描述 / 相关实体 / 相关概念 / 来源提及
- `wiki/entities/美以伊战争.md` — 追加 6-15 MoU 进展 + 时间线 + 9 条新 mentions
- `wiki/entities/霍尔木兹海峡.md` — 60 天免费开放 + 伊朗接管海峡
- `wiki/entities/伊朗.md` — 三大博弈优势
- `wiki/entities/特朗普.md` — 油价涨 40-50% 推动停火的新 mention
- `wiki/concepts/AI虹吸效应.md` — 6-15 行情印证(元件 +8.7% / 半导体 +6%)
- `wiki/concepts/加息预期.md` — 12 月维持利率概率 28.9% → 43.8% 重定价
- `wiki/sources/2026-05-13-日元保卫战-日本央行11万亿干预.md` — 知乎平行版本补充

---

## MEDIUM Findings

### M1. 死链:`[[wiki/entities/德国]]`

**位置**:`wiki/entities/2026年世界杯.md:79`
- `[[德国]] — 暴打卡拉索的传统强队`

**说明**:引用指向 `wiki/entities/德国.md`,该文件**不存在**。其他世界杯相关页面(库拉索、国足)未引用德国,只在本页面出现。

**修复建议**:创建 `wiki/entities/德国.md` stub 页面,或在本页删除德国引用(影响小,因为只有世界杯页面需要它)。

**优先级**:MEDIUM — 单点死链,不影响其他页面。

### M2. 死链:`[[wiki/concepts/世界杯小组赛]]`

**位置**:`wiki/entities/2026年世界杯.md:87`
- `[[wiki/concepts/世界杯小组赛|世界杯小组赛]] — 强弱分化明显的赛制`

**说明**:本概念此前不存在,引用为前瞻性分类。仅 `2026年世界杯.md` 一处使用,概念是否值得独立页面待定。

**修复建议**(二选一):
- 选项 A:创建 `wiki/concepts/世界杯小组赛.md` stub(若预期会有更多世界杯相关页面)
- 选项 B:删除此 wikilink,改为纯文本"世界杯小组赛赛制"

**优先级**:MEDIUM — 单点引用,概念独立性待评估。

---

## LOW Findings

### L1. 前向 `source_file` 引用:`raw/wechat/2026-06-15-美伊MoU签署与全球狂欢`

**位置**:`wiki/sources/2026-06-15-美伊MoU签署与全球狂欢.md:6`
- `source_file: "[[raw/wechat/2026-06-15-美伊MoU签署与全球狂欢]]"`

**说明**:原文是用户**直接在对话中粘贴**,未先保存到 `raw/wechat/` 目录。`raw/wechat/` 路径下确实没有此文件,但 source 页明确标注了 `Original file:`。建议后续将原文保存到 `raw/wechat/2026-06-15-美伊MoU签署与全球狂欢.md` 以让链路完整。

**优先级**:LOW — 前向引用,知识链路未断裂但需补全。

### L2. frontmatter:`source_file` 路径 vs 文件实际存放位置

**说明**:同一 source 页(`2026-06-15-美伊MoU签署与全球狂欢.md`)使用 `raw/wechat/`,而知乎平行版(`2026-05-13-日元保卫战`)使用 `raw/zhihu/`。两路径规范**不一致**:
- `raw/wechat/` 是微信公众号文章的传统存放路径
- `raw/zhihu/` 是知乎专栏文章的新增路径

**修复建议**:建立统一规则 — 微信公众号→`raw/wechat/`,知乎→`raw/zhihu/`,其他来源按平台名建文件夹。**当前实际已遵循此规则**,所以 LOW 而非 MEDIUM。

### L3. wikilink 格式不一致(同 vault 既存问题,本次继承)

**说明**:新增页面使用 `[[wiki/concepts/X|X]]` 全路径形式,而 vault 内其他页面常用 `[[X]]` 简写形式。

**示例**:
- 本次新增: `[[wiki/concepts/美伊备忘录|美伊备忘录]]`
- vault 既有: `[[中东地缘新平衡]]`(类似但少 `wiki/`)

**影响**:Obsidian basename 解析都能找到,但会触发上游报告中的 H1.b 类型问题(路径前缀不统一)。

**修复建议**:批量替换 `[[wiki/X` → `[[X` 跨全 vault(本次继承问题,本次未引入新错误)。

---

## Cross-Reference Verification

### 入站链接(谁引用了新页面)

| 新页面 | 入站来源 |
|---|---|
| `wiki/sources/2026-06-15-美伊MoU签署与全球狂欢` | moomoocat.md, 美以伊战争.md, 霍尔木兹海峡.md, 伊朗.md, 特朗普.md, AI虹吸效应.md, 加息预期.md, 2026年世界杯.md, 库拉索.md, 国足.md, UFC白宫站.md, 佩雷拉(UFC).md, 托普利亚(UFC).md, 国证有色指数.md, 华夏基金.md, 美伊备忘录.md, 微盘股.md(**17 个文件**) |
| `wiki/concepts/美伊备忘录` | moomoocat.md, 美以伊战争.md, 霍尔木兹海峡.md, 伊朗.md, 特朗普.md, 美伊备忘录.md(source) |
| `wiki/concepts/微盘股` | moomoocat.md, AI虹吸效应.md, 微盘股.md(source) |
| `wiki/entities/2026年世界杯` | moomoocat.md, 库拉索.md, 国足.md, source.md |
| `wiki/entities/UFC白宫站` | moomoocat.md, 佩雷拉(UFC).md, 托普利亚(UFC).md, source.md |
| `wiki/entities/佩雷拉(UFC)` | moomoocat.md, UFC白宫站.md, 托普利亚(UFC).md, source.md |
| `wiki/entities/托普利亚(UFC)` | moomoocat.md, UFC白宫站.md, 佩雷拉(UFC).md, source.md |
| `wiki/entities/库拉索` | moomoocat.md, 2026年世界杯.md, 国足.md, source.md |
| `wiki/entities/国足` | moomoocat.md(隐式), 2026年世界杯.md, 库拉索.md, source.md |
| `wiki/entities/华夏基金` | moomoocat.md, source.md |
| `wiki/entities/国证有色指数` | moomoocat.md, source.md |

**结果**:全部 11 个新页面**无 orphan**(≥1 入站引用)。这是 wiki 设计的健康状态 — 新页面通过 moomoocat 实体页和 source 页形成强引用网络。

### 出站链接验证(新页面中的 wikilink 是否有效)

| 引用目标 | 状态 |
|---|---|
| `entities/moomoocat` | ✓ |
| `wiki/concepts/美伊备忘录` | ✓ |
| `wiki/concepts/微盘股` | ✓ |
| `wiki/concepts/AI虹吸效应` | ✓ |
| `wiki/concepts/加息预期` | ✓ |
| `点阵图` | ✓(位于 `wiki/entities/点阵图.md`) |
| `wiki/concepts/中东地缘新平衡` | ✓ |
| `wiki/concepts/新一轮加息周期` | ✓ |
| `wiki/concepts/输入型通胀` | ✓ |
| `wiki/entities/美以伊战争` | ✓ |
| `entities/霍尔木兹海峡` | ✓ |
| `entities/伊朗` | ✓ |
| `entities/特朗普` | ✓ |
| `wiki/entities/华夏基金` | ✓ |
| `韩国KOSPI` | ✓ |
| `日经225` | ✓ |
| `wiki/entities/2026年世界杯` | ✓ |
| `entities/UFC白宫站` | ✓ |
| `entities/佩雷拉(UFC)` | ✓ |
| `entities/托普利亚(UFC)` | ✓ |
| `entities/库拉索` | ✓ |
| `entities/日本` | ✓ |
| `entities/国足` | ✓ |
| `entities/荷兰` | ✓ |
| `entities/美联储` | ✓ |
| `concepts/301调查` | ✓ |
| `concepts/贸易战` | ✓ |
| `entities/鲍威尔` | ✓ |
| `entities/黎巴嫩真主党` | ✓ |
| `entities/OPEC` | ✓ |
| `concepts/粮食安全` | ✓ |
| `wiki/sources/触目惊心，都是血包` | ✓ |
| `wiki/sources/跌太惨，朋友都没了` | ✓ |
| `wiki/sources/崩溃的信徒` | ✓ |
| `wiki/sources/2026-03-24-中东局势对全球金融市场的影响` | ✓ |
| `wiki/sources/我们已经处于新一轮加息周期中或前夜` | ✓ |
| `wiki/concepts/大小盘轮动` | ✓ |
| `wiki/concepts/A股风格轮动` | ✓ |
| `wiki/concepts/跷跷板效应` | ✓ |
| `entities/特朗普` | ✓ |
| **[[entities/德国]]** | **✗ DEAD LINK**(M1) |
| **[[wiki/concepts/世界杯小组赛]]** | **✗ DEAD LINK**(M2) |
| `raw/wechat/2026-06-15-美伊MoU签署与全球狂欢` | **⚠ 前向引用**(L1) |

**总计**:40 个出站链接,**38 个有效**,2 个死链,1 个前向引用。健康度:**95%**。

---

## Frontmatter 审计

### 通过项(10/10)

| 页面 | type | created | updated | tags | aliases | status |
|---|---|---|---|---|---|---|
| 2026-06-15-美伊MoU签署与全球狂欢 | ✓ source | ✓ | ✓ | ✓ (20 tags) | ✓ (4) | — |
| 美伊备忘录 | ✓ concept | ✓ | ✓ | ✓ (6 tags) | ✓ (5) | ✓ developing |
| 微盘股 | ✓ concept | ✓ | ✓ | ✓ (6 tags) | ✓ (4) | ✓ developing |
| 2026年世界杯 | ✓ entity | ✓ | ✓ | ✓ (4 tags) | ✓ (4) | — |
| UFC白宫站 | ✓ entity | ✓ | ✓ | ✓ (4 tags) | ✓ (3) | — |
| 佩雷拉(UFC) | ✓ entity | ✓ | ✓ | ✓ (3 tags) | ✓ (3) | — |
| 托普利亚(UFC) | ✓ entity | ✓ | ✓ | ✓ (3 tags) | ✓ (3) | — |
| 库拉索 | ✓ entity | ✓ | ✓ | ✓ (3 tags) | ✓ (3) | — |
| 国足 | ✓ entity | ✓ | ✓ | ✓ (3 tags) | ✓ (3) | — |
| 华夏基金 | ✓ entity | ✓ | ✓ | ✓ (3 tags) | ✓ (3) | — |
| 国证有色指数 | ✓ entity | ✓ | ✓ | ✓ (3 tags) | ✓ (3) | — |

### 注意事项
- **Entity 页面无 `status` 字段**:与 vault 现有 293 页无 status 的既定模式一致(参见上游报告 L2)。概念页(`美伊备忘录`、`微盘股`)有 `status: developing`,遵循概念页规范。
- **Tags 命名规范**:本次使用 `domain-type` 风格(`mma`,`fifa`),与 vault 既有混合风格(`finance`,`china`)一致。

---

## Stale Claims 检查

### 与上游报告 H1.b(Clippings/... 路径)对比
- 本次新增页面**未引入**新的 `Clippings/` 死链。
- 知乎版本处理选择"合并到现有 source 页",而非新建 source,避免新增死链(决策正确)。

### 与上游报告 H1.c(`raw/wechat/...` 路径)对比
- 本次引入 1 个 `raw/wechat/...` 前向引用(L1),但这是 source_file 字段,语义正当(原文待归档)。
- 既有 `raw/wechat/` 死链问题未受本次操作影响。

### 数据一致性检查
| 断言 | 出处 | 一致性 |
|---|---|---|
| 美伊 MoU 6-15 线上签,6-19 正式签 | 本次 source / moomoocat / 美以伊战争 / 霍尔木兹海峡 / 伊朗 | ✓ 多页面同步 |
| 霍尔木兹海峡免费开放 60 天 | 本次 source / 美伊备忘录 / 霍尔木兹海峡 / 伊朗 | ✓ |
| 维持 3.5-3.75% 概率 28.9% → 43.8% | 本次 source / 加息预期 | ✓ |
| 微盘股年内 -1.55% / 回撤 18% | 本次 source / 微盘股 / moomoocat | ✓ |
| 创业板 +5.3% / 韩股 +5.2% / 日经 +5% | 本次 source / moomoocat | ✓ |
| 布油 83 美元 / -5% | 本次 source / moomoocat / 美伊备忘录 / 霍尔木兹海峡 | ✓ |
| UFC 白宫站佩雷拉 / 托普利亚被 TKO | 本次 source / UFC白宫站 / 佩雷拉(UFC) / 托普利亚(UFC) / moomoocat | ✓ |

**结论**:无 stale claims。所有新增断言在引用页面中保持一致。

---

## 增量结论与建议

### 当日摄取质量评估
- **链接健康度**:95%(40 出站中 38 有效)
- **无 orphan**:0 个新页面是孤儿
- **无 stale claims**:所有断言跨页面一致
- **Frontmatter 完整度**:100%
- **跨引用密度**:高 — 平均每个新页面被 5+ 个其他页面引用

### 立即可执行修复(估时 10 分钟)

1. **修复 M1** — 创建 `wiki/entities/德国.md` stub:
```yaml
---
type: entity
created: 2026-06-24
updated: 2026-06-24
sources: ["[[wiki/sources/2026-06-15-美伊MoU签署与全球狂欢]]"]
tags: [location, europe]
aliases:
  - "Germany"
  - "德意志联邦共和国"
  - "Federal Republic of Germany"
---

# 德国

## 基本信息
- Type: location
- Source: [[wiki/sources/2026-06-15-美伊MoU签署与全球狂欢]]

## 描述
德国(欧洲中部国家)在 2026 年世界杯小组赛以 7:1 暴打库拉索,延续德国"对鱼腩队大开杀戒"的传统风格(参见 [[wiki/entities/2026年世界杯|2026年世界杯]])。
```

2. **修复 M2** — 将 `[[wiki/concepts/世界杯小组赛|世界杯小组赛]]` 改为纯文本"世界杯小组赛赛制"(避免为单点引用创建概念页)。

3. **修复 L1** — 保存原文到 `raw/wechat/2026-06-15-美伊MoU签署与全球狂欢.md`,让 source_file 引用解析为真。

### 中期建议
- **统一 wikilink 前缀**:与上游报告 H1.b 一起处理,跨 vault 批量替换 `[[wiki/X` → `[[X`
- **德国 stub 扩展**:可后续补充 2026 年世界杯其他德国相关数据(参考德甲、奔驰等延伸)
- **概念页面密度管理**:观察 `微盘股`、`美伊备忘录` 是否会被其他文章引用,决定是否提升为 evergreen

### 本次零问题项
- ✓ 无 BLOCKER
- ✓ 无 HIGH
- ✓ 无安全/隐私问题
- ✓ 无数据冲突
- ✓ 无 frontmatter 严重缺失

---

## 与上游报告整合

本次增量报告是 `lint-report-2026-06-24.md` 的**补充**,不替代全量扫描。建议:
- 保留本次报告为 `lint-report-2026-06-24-incremental.md`
- 上游报告的核心问题(B1 flock / H1 死链 36 / M1 tags / L2 status 缺失)**未受本次操作恶化**
- 本次操作**未引入**新的 Clippings/... 或 raw/wechat 死链(除 source_file 前向引用)
- 知乎平行版本的**合并策略**避免了重复 source 页面,节省链接资源

---

## Methodology

- 增量扫描范围:11 个页面(10 新增 + 7 修改中实际触达 11 个唯一文件)
- Wikilink 验证:basename + `wiki/` 前缀回退
- 入站链接统计:grep 全 vault `files_with_matches` 模式
- Stale claims:跨 5+ 页面同一断言的语义对齐
- 不覆盖:早上的全量 497 页 BLOCKER / HIGH(详见 `lint-report-2026-06-24.md`)