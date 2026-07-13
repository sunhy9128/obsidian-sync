---
type: meta
title: "Lint Report 2026-06-24 (Batch 2)"
created: 2026-06-25
updated: 2026-06-25
tags: [meta, lint, incremental, batch2]
status: developing
related:
  - "[[Wiki Map.canvas]]"
  - "[[index]]"
  - "[[log]]"
  - "[[lint-report-2026-06-24]]"
  - "[[lint-report-2026-06-24-incremental]]"
---

# Lint Report: 2026-06-24 (Batch 2)

> **本次扫描范围**:2026-06-24 第二批摄取 / 修改的 13 个页面
> **上游报告**:`[[lint-report-2026-06-24]]`(全量 497 页扫描)+ `[[lint-report-2026-06-24-incremental]]`(第一批 11 页)

## 增量摘要

| Metric | Count |
|---|---|
| 新增 source 页 | 2(三星回购 + 任庄主韩国) |
| 新增 concept 页 | 9(TGA机制 / 美联储独立性 / 2020美国财政刺激 / 国债缓冲机制 / 扩表与缩表 / 通胀目标制 / 单股杠杆ETF / 浮盈计税 / 重分红轻回购) |
| 新增 entity 页 | 2(韩国央行 + 韩国金融监督院) |
| 修改已有页 | 5(moomoocat / 三星电子 / AI虹吸效应 / 微盘股 / 韩国 / 任庄主 / 美联储) |
| 新增 wikilink 数 | ~120 |
| **死链** | **4**(MEDIUM) |
| Frontmatter 完整度 | **100%** |
| Orphan | 0 |
| Stale claims | 0 |

---

## 新增页面清单(13)

### Source(2)
- `wiki/sources/2026-06-24-韩国需要冷静冷静.md`
- `wiki/sources/2026-06-24-4000亿回购竟然是真的.md`

### Concepts(9)
- `wiki/concepts/TGA机制.md`
- `wiki/concepts/美联储独立性.md`
- `wiki/concepts/2020美国财政刺激.md`
- `wiki/concepts/国债缓冲机制.md`
- `wiki/concepts/扩表与缩表.md`
- `wiki/concepts/通胀目标制.md`
- `wiki/concepts/单股杠杆ETF.md`
- `wiki/concepts/浮盈计税.md`
- `wiki/concepts/重分红轻回购.md`

### Entities(2)
- `wiki/entities/韩国央行.md`
- `wiki/entities/韩国金融监督院.md`

---

## MEDIUM Findings

### M1. 死链:`[[entities/劳资协议]]`

**位置**:`wiki/entities/三星电子.md:47`
- `[[entities/劳资协议|劳资协议]] — 回购资金的制度源头`

**说明**:本概念引用描述了三星回购的制度源头(10 年劳资协议),但未创建独立页面。

**修复建议**(二选一):
- 选项 A:创建 `wiki/entities/三星劳资协议.md` stub(若后续多文引用)
- 选项 B:删除 wikilink,改为纯文本"三星 10 年劳资协议"

**优先级**:MEDIUM — 单点引用,概念独立性待评估。

### M2. 死链:`[[entities/创业板]]`

**位置**:
- `wiki/entities/三星电子.md:48`
- `wiki/sources/2026-06-24-4000亿回购竟然是真的.md:268`

**说明**:A 股创业板指未作为独立实体页存在;相关讨论在 `wiki/concepts/A股市场结构.md` 中(创业板部分已涵盖交易制度、定位、流动性)。

**修复建议**:
- 选项 A:创建 `wiki/entities/创业板指.md` stub(简单)
- 选项 B:删除 wikilink,改为纯文本"创业板"
- 选项 C:保留 wikilink 但用别名(如 `[[A股市场结构|创业板]]`)间接链接

**优先级**:MEDIUM — 涉及 2 处引用。

### M3. 死链:`[[entities/科创板]]`

**位置**:
- `wiki/entities/三星电子.md:49`
- `wiki/sources/2026-06-24-4000亿回购竟然是真的.md:269`

**说明**:同 M2,科创板作为独立实体未建。

**修复建议**:同 M2 模式。

**优先级**:MEDIUM — 涉及 2 处引用。

### M4. 死链:`[[wiki/entities/微盘股指数]]`

**位置**:`wiki/sources/2026-06-24-4000亿回购竟然是真的.md:270`
- `[[wiki/entities/微盘股指数|微盘股指数]] — 1 月回撤 20%`

**说明**:`wiki/concepts/微盘股.md` 已存在(2026-06-24 创建),引用了正确的概念页路径,但本链接用了 `wiki/entities/` 前缀而非 `wiki/concepts/`(微盘股是概念而非实体)。

**修复建议**:将 `[[wiki/entities/微盘股指数]]` 改为 `[[wiki/concepts/微盘股|微盘股指数]]` 即可。

**优先级**:MEDIUM — 路径错误(前缀不对),单点引用。

---

## LOW Findings

### L1. frontmatter:`source_file` 前向引用

**位置**:
- `wiki/sources/2026-06-24-韩国需要冷静冷静.md:6`
- `wiki/sources/2026-06-24-4000亿回购竟然是真的.md:6`

**说明**:与上游报告 L1 同类问题,原文未先存到 `raw/` 即摄取。建议后续补归档。

**优先级**:LOW — 已通过本批次 `Write` 创建对应 `raw/wechat/2026-06-24-*.md`,引用实际可用。

### L2. wikilink 路径格式不一致(继承)

**说明**:沿用 vault 既有 `[[wiki/X|X]]` 格式,与上游报告 L3 同问题。

**优先级**:LOW — 不影响功能,与 vault 风格一致。

---

## Frontmatter 审计

### 通过项(13/13)

| 页面 | type | created | updated | tags | aliases | status |
|---|---|---|---|---|---|---|
| 2026-06-24-韩国需要冷静冷静 | ✓ source | ✓ | ✓ | ✓ (12 tags) | ✓ (3) | — |
| 2026-06-24-4000亿回购竟然是真的 | ✓ source | ✓ | ✓ | ✓ (13 tags) | ✓ (4) | — |
| TGA机制 | ✓ concept | ✓ | ✓ | ✓ (5) | ✓ (5) | ✓ developing |
| 美联储独立性 | ✓ concept | ✓ | ✓ | ✓ (5) | ✓ (5) | ✓ developing |
| 2020美国财政刺激 | ✓ concept | ✓ | ✓ | ✓ (5) | ✓ (6) | ✓ developing |
| 国债缓冲机制 | ✓ concept | ✓ | ✓ | ✓ (5) | ✓ (5) | ✓ developing |
| 扩表与缩表 | ✓ concept | ✓ | ✓ | ✓ (6) | ✓ (6) | ✓ developing |
| 通胀目标制 | ✓ concept | ✓ | ✓ | ✓ (5) | ✓ (5) | ✓ developing |
| 单股杠杆ETF | ✓ concept | ✓ | ✓ | ✓ (5) | ✓ (5) | ✓ developing |
| 浮盈计税 | ✓ concept | ✓ | ✓ | ✓ (4) | ✓ (4) | ✓ developing |
| 重分红轻回购 | ✓ concept | ✓ | ✓ | ✓ (5) | ✓ (5) | ✓ developing |
| 韩国央行 | ✓ entity | ✓ | ✓ | ✓ (3) | ✓ (4) | — |
| 韩国金融监督院 | ✓ entity | ✓ | ✓ | ✓ (4) | ✓ (4) | — |

**结果**:所有新页面符合 vault frontmatter 规范。

---

## Cross-Reference Verification

### 入站链接密度(本次新增页面被引用次数)

| 新页面 | 入站来源数 |
|---|---|
| `TGA机制` | 3(美联储/扩表与缩表/2020美国财政刺激) |
| `美联储独立性` | 4(美联储/扩表与缩表/TGA机制/2020美国财政刺激/国债缓冲机制) |
| `2020美国财政刺激` | 3(TGA机制/扩表与缩表/国债缓冲机制) |
| `国债缓冲机制` | 5(美联储/扩表与缩表/TGA机制/2020美国财政刺激) |
| `扩表与缩表` | 3(美联储/2020美国财政刺激/TGA机制) |
| `重分红轻回购` | 2(三星电子/4000亿回购 source) |
| `通胀目标制` | 4(韩国央行/韩国.md/任庄主.md/韩国需要冷静冷静 source) |
| `单股杠杆ETF` | 3(韩国金融监督院/三星回购 source/韩国需要冷静冷静 source) |
| `浮盈计税` | 3(韩国.md/三星回购 source/韩国需要冷静冷静 source) |
| `韩国央行` | 5(任庄主.md/韩国.md/韩国金融监督院/韩国需要冷静冷静 source/moomoocat.md) |
| `韩国金融监督院` | 4(任庄主.md/韩国.md/韩国央行/韩国需要冷静冷静 source) |
| `三星回购 source` | 1(三星电子.md) |
| `韩国需要冷静冷静 source` | 3(任庄主.md/韩国.md/三星电子.md) |

**结果**:全部 13 个新页面均被 ≥1 个其他页面引用,**无 orphan**。

### 出站链接验证

| 引用目标 | 验证状态 |
|---|---|
| `wiki/entities/moomoocat` | ✓ |
| `wiki/entities/任庄主` | ✓ |
| `wiki/entities/三星电子` | ✓ |
| `wiki/entities/SK海力士` | ✓ |
| `wiki/entities/韩国综合指数` | ✓ |
| `wiki/entities/韩国` | ✓ |
| `wiki/entities/特朗普` | ✓ |
| `wiki/entities/美联储` | ✓ |
| `wiki/entities/直升机撒钱` | ✓ |
| `wiki/entities/财政货币化` | ✓ |
| `wiki/entities/量化紧缩` | ✓ |
| `wiki/entities/货币政策工具` | ✓ |
| `wiki/entities/梧桐树智库` | ✓ |
| `wiki/concepts/股牛汇弱` | ✓ |
| `wiki/concepts/通胀目标制` | ✓ |
| `wiki/concepts/单股杠杆ETF` | ✓ |
| `wiki/concepts/浮盈计税` | ✓ |
| `wiki/concepts/加息预期` | ✓ |
| `wiki/concepts/输入型通胀` | ✓ |
| `wiki/concepts/出口导向型经济体` | ✓ |
| `wiki/concepts/ICT出口` | ✓ |
| `wiki/concepts/AI虹吸效应` | ✓ |
| `wiki/concepts/微盘股` | ✓ |
| `wiki/concepts/重分红轻回购` | ✓ |
| `wiki/concepts/回购注销` | ✓ |
| `wiki/concepts/A股市场结构` | ✓ |
| `wiki/concepts/股息与分红` | ✓ |
| `wiki/concepts/TGA机制` | ✓ |
| `wiki/concepts/美联储独立性` | ✓ |
| `wiki/concepts/2020美国财政刺激` | ✓ |
| `wiki/concepts/国债缓冲机制` | ✓ |
| `wiki/concepts/扩表与缩表` | ✓ |
| `wiki/concepts/公开市场操作` | ✓ |
| `wiki/concepts/量化宽松` | ✓ |
| `wiki/concepts/美元加息周期` | ✓ |
| `wiki/concepts/输入型通胀` | ✓ |
| `wiki/concepts/老登板块` | ✓ |
| `wiki/concepts/抗通胀资产` | ✓ |
| `wiki/sources/2026-06-15-美伊MoU签署与全球狂欢` | ✓ |
| `wiki/sources/2026-06-24-韩国需要冷静冷静` | ✓ |
| `wiki/sources/2026-06-24-4000亿回购竟然是真的` | ✓ |
| `wiki/sources/为何日韩会股牛汇弱` | ✓ |
| `wiki/sources/崩溃的信徒` | ✓ |
| `wiki/sources/跌太惨，朋友都没了` | ✓ |
| `wiki/sources/触目惊心，都是血包` | ✓ |
| `wiki/concepts/国债缓冲机制` | ✓ |
| **`[[entities/劳资协议]]`** | **✗ DEAD LINK**(M1) |
| **`[[entities/创业板]]`** | **✗ DEAD LINK**(M2) |
| **`[[entities/科创板]]`** | **✗ DEAD LINK**(M3) |
| **`[[wiki/entities/微盘股指数]]`** | **✗ DEAD LINK**(M4,前缀错误) |

**总计**:48 个出站链接,**44 个有效**,4 个死链。健康度:**92%**(略低于第一批的 95%,主要是 M2/M3 多处引用累积)。

---

## Stale Claims 检查

### 数据一致性验证

| 断言 | 出处 | 一致性 |
|---|---|---|
| 三星 90 万亿韩元 ≈ 4000 亿人民币 | 三星回购 source / 三星电子 | ✓ 双向一致 |
| 三星 vs A 股回购 3 倍 | 三星回购 source / 重分红轻回购 | ✓ |
| A 股年回购 1400 亿 | 重分红轻回购 / 三星回购 source / A股市场结构 | ✓ |
| A 股现金分红 2.6 万亿 | 重分红轻回购 / 三星回购 source | ✓ |
| 美股回购 = A 股 56 倍 | 重分红轻回购 / 三星回购 source | ✓ |
| 微盘股 1 月回撤 20% | 三星回购 source / 微盘股 / AI虹吸效应 | ✓ 三向一致 |
| 微盘股年内 +15% → -5% | 三星回购 source / 微盘股 | ✓ |
| BOK 维持 2.5% 不变 | 韩国需要冷静冷静 source / 韩国央行 | ✓ |
| BOK 2 位支持加息 + 3 位后续加息 | 韩国需要冷静冷静 source / 韩国央行 | ✓ |
| 韩国 CPI 3.14% / 核心 2.53% | 韩国需要冷静冷静 source / 韩国央行 | ✓ |
| KOSPI 2026 +94.67% | 韩国需要冷静冷静 source / 韩国综合指数 | ✓ |
| 韩元 2026 -6.5% | 韩国需要冷静冷静 source / 韩国.md | ✓ |
| FSS 6-18 提示单股杠杆 ETF | 韩国需要冷静冷静 source / 韩国金融监督院 | ✓ |
| 单股杠杆 ETF 最大跌幅 36.9% | 韩国金融监督院 / 单股杠杆ETF | ✓ |
| KOSPI 单日 -10%(6-23) | 浮盈计税 / 韩国.md / 单股杠杆ETF | ✓ |
| 布油 $73 / 白银 $60 / 黄金 $4000 | 三星回购 source / moomoocat | ✓ |
| TGA ≈ $7000 亿 | TGA机制 | ✓ 单源 |
| 美联储资产负债表 ≈ $6.7 万亿(2026) | 扩表与缩表 | ✓ 单源 |

**结论**:**0 stale claims**。所有断言跨页面一致。

---

## 当日摄取总览(汇总)

| 批次 | 时间 | 新增 | 修改 | 死链 | 健康度 |
|---|---|---|---|---|---|
| 第一批(增量) | 2026-06-24 早 | 10 | 7 | 2(M1/M2) | 95% |
| **第二批(本次)** | 2026-06-24 中晚 | **13** | **5** | **4**(M1-M4) | **92%** |
| **当日累计** | — | **23** | **12** | **4** | — |

---

## 修复建议(立即可执行)

### 高效修复(M1-M3 概念未建)

```
1. 创建 wiki/entities/创业板指.md(简单 stub,5 行内容)
2. 创建 wiki/entities/科创50.md(同上)
3. 删除 [[entities/劳资协议]] 引用或创建 stub
```

### 简单修复(M4 路径错误)

将 `[[wiki/entities/微盘股指数]]` 改为 `[[wiki/concepts/微盘股|微盘股指数]]`。

---

## 设计观察

### 本批次概念高度网络化

4 个美联储/TGA 概念页形成强闭合网络:

```
TGA机制 ←→ 美联储独立性 ←→ 国债缓冲机制 ←→ 2020美国财政刺激
       ↓              ↓                  ↓
              扩表与缩表
```

每个概念都被 3-5 个其他新概念引用,**网络密度高**,无 orphan,符合知识图谱的健康标准。

### 任庄主韩国文章也形成完整闭环

```
韩国央行 → 通胀目标制 → 加息预期
    ↓
韩国金融监督院 → 单股杠杆ETF → 浮盈计税
    ↓
韩国综合指数(KOSPI) ← 三星电子 ← SK海力士
```

6 个新页面全部互联,**结构紧凑**。

### 三星回购文章相对松散

由于涉及 A 股市场结构,跨域引用较多(`创业板`、`科创板`、`微盘股指数` 死链),反映**A股细分领域**在 vault 中**尚未充分索引**,是后续可补的方向。

---

## 本次零问题项

- ✓ 无 BLOCKER
- ✓ 无 HIGH(只有 4 个 MEDIUM 死链)
- ✓ 无安全/隐私问题
- ✓ 无数据冲突
- ✓ 无 frontmatter 严重缺失
- ✓ 无 orphan
- ✓ 所有数据跨页面一致

---

## 与上游报告整合

- 上游报告 1:`[[lint-report-2026-06-24]]`(全量 497 页,BLOCKER B1 flock)
- 上游报告 2:`[[lint-report-2026-06-24-incremental]]`(第一批 11 页,2 死链已修复)
- 本报告:`[[lint-report-2026-06-24-batch2]]`(本批次)

**死链累计统计**:
- 全量报告:36
- 第一批修复后:34
- 本批次新增:4(M1-M4)
- **当前累计**:38(待修复)

---

## Methodology

- 增量扫描范围:13 个页面(9 concept + 2 entity + 2 source)
- Wikilink 验证:basename + `wiki/` 前缀回退
- 入站链接统计:grep 全 vault `files_with_matches`
- Stale claims:跨 5+ 页面同一断言的语义对齐
- Frontmatter 审计:type / created / updated / tags / aliases / status 六维检查
- 不覆盖:早上全量 497 页 BLOCKER / HIGH(详见 `lint-report-2026-06-24.md`)