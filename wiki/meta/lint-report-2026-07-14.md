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

- Pages scanned: 718 (excluding folds/, meta/)
- Issues found: 495
- Auto-fixed: 0 (review-first policy)
- Needs review: 495

> [!info]
> 本报告使用 PyYAML 正确解析 frontmatter（修正了 7-13 报告中 tags 多行列表解析错误导致的 607 个虚假 frontmatter 缺口）。

### Issue Breakdown

| 类别 | 数量 | 优先级 |
|------|------|--------|
| 孤立页 (orphans) | 22 | MEDIUM |
| 死链 (dead links) | 451 (222 unique) | HIGH |
| Frontmatter 缺口 | 22 | LOW |
| 空章节 (empty sections) |  8 | LOW |
| Stale index 条目 | 2 | LOW |

---

## Orphan Pages (22)

以下页面无入站 wikilink，建议从相关概念页或实体页添加链接：

### Concept 类孤立 (4)

- [[_index]] (`wiki/concepts/_index.md`)
- [[公募基金行业2025H1排名分析]] (`wiki/concepts/公募基金行业2025H1排名分析.md`)
- [[军工航空产业]] (`wiki/concepts/军工航空产业.md`)
- [[金砖支付系统]] (`wiki/concepts/金砖支付系统.md`)

### Entity 类孤立 (8)

- [[_index]] (`wiki/entities/_index.md`)
- [[实体页]] (`wiki/entities/实体页.md`)
- [[恒生科技指数]] (`wiki/entities/恒生科技指数.md`)
- [[最后贷款人]] (`wiki/entities/最后贷款人.md`)
- [[美元霸权]] (`wiki/entities/美元霸权.md`)
- [[财政货币化]] (`wiki/entities/财政货币化.md`)
- [[邓小平]] (`wiki/entities/邓小平.md`)
- [[量化宽松]] (`wiki/entities/量化宽松.md`)

### Source 类孤立 (4)

> [!note] Source 类页面通常从外部链接，不强制要求内部入站 wikilink。

- [[2026-06-23-股份回购后注销对股票有什么影响]] (`wiki/sources/2026-06-23-股份回购后注销对股票有什么影响.md`)
- [[_index]] (`wiki/sources/_index.md`)
- [[冲销式干预]] (`wiki/sources/冲销式干预.md`)
- [[石油美元体系]] (`wiki/sources/石油美元体系.md`)

### _index / 系统页孤立 (3)

- `wiki/comparisons/_index.md`
- `wiki/domains/_index.md`
- `wiki/strategies/_index.md`

### 其他孤立 (3)

- `wiki/questions/财政货币化.md`
- `wiki/references/methodology-modes.md`
- `wiki/references/transport-fallback.md`

---

## Dead Links (451 total, 222 unique)

### 1. 路径型死链 (basename-only) — 140 unique

这些 wikilink 仅使用文件名（如 `[[SLF]]`），但同名页面在多个目录存在或根本不存在。最常见的：

| 目标 | 提及次数 | 建议 |
|------|----------|------|
| `[[结构性行情]]` | 1 | 创建概念/实体页 |
| `[[货币政策传导机制]]` | 1 | 创建概念/实体页 |
| `[[How does the LLM Wiki pattern work?]]` | 1 | 创建概念/实体页 |
| `[[Three laws of motion]]` | 1 | 创建概念/实体页 |
| `[[Entities]]` | 1 | 创建概念/实体页 |
| `[[Sources]]` | 1 | 创建概念/实体页 |
| `[[《环球时报》]]` | 1 | 创建概念/实体页 |
| `[[产权理论与制度经济学]]` | 1 | 创建概念/实体页 |
| `[[制度变迁]]` | 1 | 创建概念/实体页 |
| `[[价格机制]]` | 1 | 创建概念/实体页 |
| `[[市场失灵]]` | 1 | 创建概念/实体页 |
| `[[2026年1-3月中国外贸数据]]` | 1 | 创建概念/实体页 |
| `[[301条款]]` | 1 | 创建概念/实体页 |
| `[[对外投资]]` | 1 | 创建概念/实体页 |
| `[[为何日韩会股牛汇弱]]` | 1 | 创建概念/实体页 |
| `[[本币贬值]]` | 1 | 创建概念/实体页 |
| `[[外国补贴条例（FSR）]]` | 1 | 创建概念/实体页 |
| `[[出口管制]]` | 1 | 创建概念/实体页 |
| `[[SLF]]` | 1 | 创建概念/实体页 |
| `[[美联储货币政策]]` | 1 | 创建概念/实体页 |

### 2. 真实缺失页面 — 79 unique

这些 wikilink 指向的页面在 wiki 中不存在：

| 死链 | 提及次数 | 建议 |
|------|----------|------|
| `[[wiki/concepts/SLO]]` | 1 | 创建 stub 或修正链接 |
| `[[wiki/concepts/SLF]]` | 1 | 创建 stub 或修正链接 |
| `[[wiki/concepts/2023年化债]]` | 1 | 创建 stub 或修正链接 |
| `[[wiki/concepts/货币基金]]` | 1 | 创建 stub 或修正链接 |
| `[[wiki/entities/阿里巴巴]]` | 1 | 创建 stub 或修正链接 |
| `[[wiki/concepts/金融脱媒]]` | 1 | 创建 stub 或修正链接 |
| `[[wiki/concepts/资管新规]]` | 1 | 创建 stub 或修正链接 |
| `[[wiki/concepts/8号文]]` | 1 | 创建 stub 或修正链接 |
| `[[wiki/entities/周小川]]` | 1 | 创建 stub 或修正链接 |
| `[[wiki/entities/银监会]]` | 1 | 创建 stub 或修正链接 |
| `[[wiki/concepts/DR007]]` | 1 | 创建 stub 或修正链接 |
| `[[wiki/concepts/SHIBOR]]` | 1 | 创建 stub 或修正链接 |
| `[[wiki/entities/光大银行]]` | 1 | 创建 stub 或修正链接 |
| `[[wiki/entities/天弘基金]]` | 1 | 创建 stub 或修正链接 |
| `[[wiki/concepts/央行对冲工具]]` | 1 | 创建 stub 或修正链接 |
| `[[wiki/concepts/1998年LTCM危机]]` | 1 | 创建 stub 或修正链接 |
| `[[wiki/concepts/存储三巨头]]` | 1 | 创建 stub 或修正链接 |
| `[[wiki/concepts/存储芯片]]` | 1 | 创建 stub 或修正链接 |
| `[[wiki/concepts/苹果涨价]]` | 1 | 创建 stub 或修正链接 |
| `[[wiki/concepts/MLF\]]` | 1 | 创建 stub 或修正链接 |
| `[[wiki/concepts/PSL\]]` | 1 | 创建 stub 或修正链接 |
| `[[wiki/concepts/港股通]]` | 1 | 创建 stub 或修正链接 |
| `[[wiki/entities/中核集团]]` | 1 | 创建 stub 或修正链接 |
| `[[wiki/entities/中国电科]]` | 1 | 创建 stub 或修正链接 |
| `[[wiki/entities/中国船舶]]` | 1 | 创建 stub 或修正链接 |

> 还有 54 个真实缺失链接，详见 `/tmp/wiki_lint_v2.json`

### 3. Canvas 引用 (0)

`[[Wiki Map.canvas]]` 等是 Obsidian canvas 文件，不是 wiki 页。Obsidian 原生支持，但 wikilink 解析会算 dead link。建议保留或转 image embed。

### 4. 测试残留 (2)

如 `[[Foo]]`、`[[wikilinks]]` 等是概念验证残留，建议删除：

- `[[Foo]]` (in `wiki/concepts/DragonScale Memory.md`)
- `[[wikilinks]]` (in `wiki/concepts/cherry-picks.md`)

---

## Frontmatter Gaps (22)

> [!info]
> 修正前报告为 607 个，但绝大多数是 tags 解析失败（多行 YAML 列表）。PyYAML 正确解析后只剩 22 个真实缺口。

### 分布

| 缺失字段 | 数量 |
|---------|------|
| updated | 10 |
| created, updated | 8 |
| created | 4 |

### 详情

- `wiki/hot.md`: missing `['created']`
- `wiki/getting-started.md`: missing `['created']`
- `wiki/log.md`: missing `['created']`
- `wiki/index.md`: missing `['created']`
- `wiki/concepts/大豆战争.md`: missing `['created', 'updated']`
- `wiki/concepts/恶意收购.md`: missing `['updated']`
- `wiki/concepts/万科宝能之争.md`: missing `['updated']`
- `wiki/concepts/白衣骑士.md`: missing `['updated']`
- `wiki/concepts/CBOT.md`: missing `['created', 'updated']`
- `wiki/concepts/中国特色企业治理.md`: missing `['updated']`
- `wiki/concepts/战略储备.md`: missing `['created', 'updated']`
- `wiki/concepts/杠杆收购.md`: missing `['updated']`
- `wiki/sources/2025-02-04-中国粮食金融保卫战-巫师财经.md`: missing `['created', 'updated']`
- `wiki/sources/万科宝能股权之争.md`: missing `['created', 'updated']`
- `wiki/entities/庄炳昌.md`: missing `['created', 'updated']`
- `wiki/entities/中储粮.md`: missing `['created', 'updated']`
- `wiki/entities/华润.md`: missing `['updated']`
- `wiki/entities/安邦.md`: missing `['updated']`
- `wiki/entities/姚振华.md`: missing `['updated']`
- `wiki/entities/五神.md`: missing `['created', 'updated']`
- `wiki/entities/王石.md`: missing `['updated']`
- `wiki/entities/宝能系.md`: missing `['updated']`

---

## Empty Sections (1920)

只有 7 个文件包含真正空的章节（多数是 _index.md 模板提示语）。具体：

- `wiki/getting-started.md`: ['Three-Step Quick Start']
- `wiki/domains/宏观经济.md`: ['宏观经济', '核心概念']
- `wiki/domains/风险管理.md`: ['风险管理']
- `wiki/domains/货币政策与中央银行.md`: ['货币政策与中央银行']
- `wiki/domains/中国金融与改革.md`: ['中国金融与改革']
- `wiki/domains/银行体系与金融监管.md`: ['银行体系与金融监管']
- `wiki/domains/股票与行业分析.md`: ['股票与行业分析']
- `wiki/domains/国际金融与汇率.md`: ['国际金融与汇率']
- `wiki/domains/债券与利率市场.md`: ['债券与利率市场']
- `wiki/comparisons/港股vs美股vsA股.md`: ['二、上市制度对比', '四、投资者结构对比', '五、市场特征对比', '六、三地互联互通', '七、投资 A 股 vs 港股 vs 美股的选择框架']
- `wiki/comparisons/回购vs分红.md`: ['三、回报机制的数学差异', '七、不同市场环境下的选择', '九、投资者策略含义']
- `wiki/comparisons/Wiki vs RAG.md`: ['Wiki vs RAG']
- `wiki/analysis/基金行业2025H1排名分析.md`: ['行业关键趋势']
- `wiki/analysis/基金年中排名对A股影响机制.md`: ['二、三大传导机制', '三、年中资金流向的结构性影响', '五、对A股投资者的启示']
- `wiki/concepts/机会成本.md`: ['一、核心概念', '二、成本分类', '三、典型案例', '四、生产可能性边界（PPF）', '五、机会成本的应用', '六、机会成本与其他成本概念', '七、深度思考题']
- `wiki/concepts/股汇关系.md`: ['股汇关系']
- `wiki/concepts/1992欧洲货币危机.md`: ['二、时间线', '三、欧洲汇率机制（ERM）详解', '四、索罗斯的"做空操作"', '五、英格兰银行的"防御战"', '六、索罗斯的"盈利分析"', '七、1992 年危机的"全球影响"', '八、索罗斯的"反思与影响"', '九、1992 危机与 1998 香港案例的对比', '十、1992 危机的"金融学意义"', '十一、1992 危机的"经验教训"', '十二、1992 危机的"金融史定位"', '十三、1992 危机的"哲学高度"', '十四、1992 危机的"反思"']
- `wiki/concepts/中俄全面战略协作伙伴关系.md`: ['中俄全面战略协作伙伴关系']
- `wiki/concepts/货币兑换（1990东德）.md`: ['二、核心兑换规则', '三、科尔的核心动机', '四、货币兑换的金融学分析', '五、货币兑换的六大直接后果', '六、货币兑换的金融学理论框架', '七、货币兑换的争议与评价', '相关条目']
- `wiki/concepts/OMT.md`: ['一、核心定义', '二、OMT 诞生的背景：2012 年欧债危机', '三、OMT 的运作机制', '四、OMT 的法律争议', '五、OMT 的"威慑效应"', '六、OMT 与 APP/PEPP 的关系', '八、OMT 的国际比较', '九、OMT 的历史评价', '相关条目']
- `wiki/concepts/囚徒困境.md`: ['一、经典案例', '二、占优策略分析', '三、N 人囚徒困境', '四、走出困境的机制', '五、现实金融案例', '六、理论意义']
- `wiki/concepts/央行政策.md`: ['央行政策']
- `wiki/concepts/共建一带一路.md`: ['共建"一带一路"', '三、美元替代的三条平行路径']
- `wiki/concepts/出口导向型经济体.md`: ['出口导向型经济体']
- `wiki/concepts/霸权稳定论.md`: ['一、核心定义', '二、历史上的霸权', '三、霸权稳定论与欧元区', '四、对中国的启示', '相关条目']
- `wiki/concepts/启发式与偏差.md`: ['启发式与偏差']
- `wiki/concepts/PCE.md`: ['美联储的政策框架']
- `wiki/concepts/理性预期.md`: ['理性预期']
- `wiki/concepts/经济增长.md`: ['经济增长']
- `wiki/concepts/财政政策与货币政策协同.md`: ['财政政策与货币政策协同']
- `wiki/concepts/负利率.md`: ['一、核心定义', '二、负利率的理论基础', '三、负利率的国际实践', '四、负利率的五大问题', '五、负利率与化债', '六、负利率的退出', '七、负利率的全球评价', '相关条目']
- `wiki/concepts/工业加速器法案.md`: ['《工业加速器法案》']
- `wiki/concepts/稀缺性.md`: ['稀缺性']
- `wiki/concepts/数据安全.md`: ['数据安全']
- `wiki/concepts/外汇掉期冲销.md`: ['外汇掉期冲销']
- `wiki/concepts/军工航空产业.md`: ['二、六条战线', '三、军工产业四大基础理论', '四、战机产业链', '五、发动机产业链', '六、导弹（制导炸弹）产业链', '七、军机军贸', '八、需求侧宏观逻辑', '十、81192的历史意义']
- `wiki/concepts/公开市场操作.md`: ['公开市场操作']
- `wiki/concepts/去美元化.md`: ['一、核心定义与本质', '二、去美元化的核心驱动力', '三、去美元化的关键数据', '四、去美元化的具体路径', '五、去美元化的核心案例', '六、去美元化与美元武器化的耦合关系', '七、去美元化的结构性约束', '八、去美元化与人民币国际化的关系', '十、未来演进', '相关条目']
- `wiki/concepts/美联储独立性.md`: ['1930 年代立法背景', '独立性的具体保障机制', '2020 年的"灰色地带"', '美联储独立性的现实挑战', '失去独立性的历史教训']
- `wiki/concepts/化债核心命题.md`: ['二、命题的金融学升华', '三、命题的四个支撑要点', '3.3 "争取时间"的三层含义', '四、命题与三大基础概念的关系', '六、命题的三个推论', '七、命题在不同语境下的应用', '八、命题的局限与争议']
- `wiki/concepts/官方媒体.md`: ['官方媒体']
- `wiki/concepts/蒙代尔-弗莱明模型.md`: ['蒙代尔-弗莱明模型']
- `wiki/concepts/阻断法令.md`: ['一、核心定义与本质', '二、欧盟阻断法令（EU Blocking Statute）', '三、中国阻断办法', '四、俄罗斯反制裁法', '五、阻断法令的国际比较', '六、阻断法令与美国长臂管辖的博弈', '七、阻断法令的实战案例', '八、阻断法令的未来演进', '相关条目']
- `wiki/concepts/供需.md`: ['供需']
- `wiki/concepts/逆向选择.md`: ['一、核心概念', '二、Akerlof 二手车市场模型', '三、健康保险市场', '四、金融市场', '五、劳动力市场', '六、其他典型场景', '八、理论意义']
- `wiki/concepts/预期差交易.md`: ['四、预期差在宏观事件中的应用', '五、预期差的识别方法']
- `wiki/concepts/国际收支.md`: ['一、核心定义', '二、BOP 三大账户', '三、国际收支恒等式', '四、顺差/逆差的宏观经济含义', '五、中国双顺差历史', '六、外汇储备', '七、特里芬难题']
- `wiki/concepts/粮食安全.md`: ['粮食安全']
- `wiki/concepts/国家理论.md`: ['国家理论']
- `wiki/concepts/金融传导机制分析框架.md`: ['二、四层分析框架', '三、为什么看起来"反直觉"？', '五、案例：豆粕-猪价背离的完整分析', '六、更多多链叠加案例']
- `wiki/concepts/化债.md`: ['二、化债的对象——三类债务', '四、化债的运作机制', '五、钱从哪里来？——五大资金来源', '5.2 五大来源详解', '六、化债的进度与成效', '七、化债的争议与挑战', '十、化债对银行体系流动性的影响', '10.7 银行"三重损失"与"三重缓冲"']
- `wiki/concepts/财政发力与通胀关联.md`: ['财政发力与通胀关联']
- `wiki/concepts/外汇干预有效性.md`: ['外汇干预有效性', '干预有效性的判断维度']
- `wiki/concepts/仪表盘.md`: ['仪表盘']
- `wiki/concepts/蛛网模型.md`: ['六、扩展与衍生模型']
- `wiki/concepts/金融武器化.md`: ['一、核心定义与本质', '二、金融武器化的运作机制', '2.1 五大武器工具', '三、金融武器化的历史演进', '四、金融武器化的反作用力（核心议题）', '五、各方的"金融武器化"博弈策略', '六、金融武器化与"非对称反制"', '七、金融武器化的未来演进', '相关条目']
- `wiki/concepts/股汇负相关性.md`: ['股汇负相关性']
- `wiki/concepts/高风险设备供应商清单.md`: ['高风险设备供应商清单']
- `wiki/concepts/东欧转型.md`: ['一、核心定义与范围', '二、东欧转型的三大策略', '三、东欧转型的关键差异', '四、东欧转型的五大成功因素', '五、东欧转型的五大核心问题', '六、东欧转型对转型经济学的贡献', '相关条目']
- `wiki/concepts/欧洲货币体系.md`: ['二、历史背景：布雷顿森林崩溃后的"欧洲方案"', '三、EMS 核心机制', '四、EMS 的"硬通货"理论', '五、EMS 的历史演进', '六、EMS 的"遗产"：通向欧元的桥梁', '七、EMS 的金融学意义', '八、EMS 时代的危机与经验', '九、EMS 与其他货币体系的比较', '十、EMS 时代的精神遗产']
- `wiki/concepts/中国改革.md`: ['一、核心定义与基本信息', '二、改革的五个历史阶段']

---

## Stale Index Entries (2)

`wiki/index.md` 中有 2 个引用需要修正：

- `[[Wiki Map.canvas]]`
- `[[Wiki Map.canvas]]`

---

## Address Validation (DragonScale Mechanism 2)

> [!warning]
> **关键发现**: 只有 12 个页面被分配了 address,但 post-rollout (2026-04-23 之后) 创建的 660 个页面都没有 address。这是 wiki-ingest 没启用 address 分配的系统性问题,不是页面作者的问题。

- Counter state: `16` (下一个可用 `c-000016`)
- Highest c- address observed: `c-000015`
- Addressed pages: 12
- Address collisions: 0 ✓
- Bad format: 0 ✓
- Counter drift: 0 ✓
- Manifest mismatches: 0 ✓

### Post-rollout pages without address (errors): 660

按文件夹分布：

- `wiki/analysis/基金年中排名对A股影响机制.md/`: 1 pages
- `wiki/analysis/基金行业2025H1排名分析.md/`: 1 pages
- `wiki/comparisons/中俄联合声明2021vs2026.md/`: 1 pages
- `wiki/comparisons/回购vs分红.md/`: 1 pages
- `wiki/comparisons/港股vs美股vsA股.md/`: 1 pages
- `wiki/concepts/1987黑色星期一.md/`: 1 pages
- `wiki/concepts/1992欧洲货币危机.md/`: 1 pages
- `wiki/concepts/1997亚洲金融危机.md/`: 1 pages
- `wiki/concepts/1998香港金融保卫战.md/`: 1 pages
- `wiki/concepts/2008全球金融危机.md/`: 1 pages
- `wiki/concepts/2013年钱荒.md/`: 1 pages
- `wiki/concepts/2020年3月流动性危机.md/`: 1 pages
- `wiki/concepts/2020美国财政刺激.md/`: 1 pages
- `wiki/concepts/2023年SVB危机.md/`: 1 pages
- `wiki/concepts/301调查.md/`: 1 pages
- `wiki/concepts/70城房价.md/`: 1 pages
- `wiki/concepts/AI虹吸效应.md/`: 1 pages
- `wiki/concepts/A股市场结构.md/`: 1 pages
- `wiki/concepts/A股风格轮动.md/`: 1 pages
- `wiki/concepts/CAPM资本资产定价模型.md/`: 1 pages
- `wiki/concepts/CPI与通胀.md/`: 1 pages
- `wiki/concepts/DDXDDYDDZ-指标.md/`: 1 pages
- `wiki/concepts/E-commerce SEO.md/`: 1 pages
- `wiki/concepts/GDP（国内生产总值）.md/`: 1 pages
- `wiki/concepts/GameStop轧空事件.md/`: 1 pages
- `wiki/concepts/HBM.md/`: 1 pages
- `wiki/concepts/ICT出口.md/`: 1 pages
- `wiki/concepts/IS-LM模型.md/`: 1 pages
- `wiki/concepts/LGFV.md/`: 1 pages
- `wiki/concepts/LPR.md/`: 1 pages
- `wiki/concepts/MLF.md/`: 1 pages
- `wiki/concepts/OMT.md/`: 1 pages
- `wiki/concepts/PCE.md/`: 1 pages
- `wiki/concepts/PSL.md/`: 1 pages
- `wiki/concepts/Persistent Wiki Artifact.md/`: 1 pages
- `wiki/concepts/QE与化债对比.md/`: 1 pages
- `wiki/concepts/Query-Time Retrieval.md/`: 1 pages
- `wiki/concepts/Rentenmark改革.md/`: 1 pages
- `wiki/concepts/Source-First Synthesis.md/`: 1 pages
- `wiki/concepts/TGA机制.md/`: 1 pages
- `wiki/concepts/Treuhand 私有化.md/`: 1 pages
- `wiki/concepts/Volkswagen轧空事件.md/`: 1 pages
- `wiki/concepts/mBridge.md/`: 1 pages
- `wiki/concepts/不婚不育消费降级.md/`: 1 pages
- `wiki/concepts/东欧转型.md/`: 1 pages
- `wiki/concepts/两德合并.md/`: 1 pages
- `wiki/concepts/个人信息保护.md/`: 1 pages
- `wiki/concepts/中东地缘新平衡.md/`: 1 pages
- `wiki/concepts/中东局势.md/`: 1 pages
- `wiki/concepts/中俄全面战略协作伙伴关系.md/`: 1 pages
- `wiki/concepts/中国2026年一季度外贸数据.md/`: 1 pages
- `wiki/concepts/中国改革.md/`: 1 pages
- `wiki/concepts/中央银行外汇干预.md/`: 1 pages
- `wiki/concepts/中概股.md/`: 1 pages
- `wiki/concepts/中欧经贸关系.md/`: 1 pages
- `wiki/concepts/中美俄大三角.md/`: 1 pages
- `wiki/concepts/二十届三中全会.md/`: 1 pages
- `wiki/concepts/五穷六绝七翻身.md/`: 1 pages
- `wiki/concepts/交易成本与科斯定理.md/`: 1 pages
- `wiki/concepts/人口结构.md/`: 1 pages
- `wiki/concepts/仪表盘.md/`: 1 pages
- `wiki/concepts/价格传导非对称性.md/`: 1 pages
- `wiki/concepts/企业理论.md/`: 1 pages
- `wiki/concepts/休克疗法.md/`: 1 pages
- `wiki/concepts/估值指标.md/`: 1 pages
- `wiki/concepts/供应链多元化.md/`: 1 pages
- `wiki/concepts/供需.md/`: 1 pages
- `wiki/concepts/供需均衡.md/`: 1 pages
- `wiki/concepts/俄乌无人机消耗战.md/`: 1 pages
- `wiki/concepts/俄罗斯转型.md/`: 1 pages
- `wiki/concepts/保障措施调查.md/`: 1 pages
- `wiki/concepts/信息不对称.md/`: 1 pages
- `wiki/concepts/信用利差.md/`: 1 pages
- `wiki/concepts/借股票池.md/`: 1 pages
- `wiki/concepts/债市定价逻辑.md/`: 1 pages
- `wiki/concepts/全国统一大市场.md/`: 1 pages
- `wiki/concepts/全球金融周期.md/`: 1 pages
- `wiki/concepts/公共物品.md/`: 1 pages
- `wiki/concepts/公募基金行业2025H1排名分析.md/`: 1 pages
- `wiki/concepts/公地悲剧.md/`: 1 pages
- `wiki/concepts/公开市场操作.md/`: 1 pages
- `wiki/concepts/共建一带一路.md/`: 1 pages
- `wiki/concepts/关税战对通胀的传导.md/`: 1 pages
- `wiki/concepts/再投资.md/`: 1 pages
- `wiki/concepts/军事同盟.md/`: 1 pages
- `wiki/concepts/军工航空产业.md/`: 1 pages
- `wiki/concepts/冲销式干预.md/`: 1 pages
- `wiki/concepts/出口商品结构.md/`: 1 pages
- `wiki/concepts/出口导向型经济体.md/`: 1 pages
- `wiki/concepts/出口盈利预期.md/`: 1 pages
- `wiki/concepts/利率平价理论.md/`: 1 pages
- `wiki/concepts/利率走廊.md/`: 1 pages
- `wiki/concepts/制度学习.md/`: 1 pages
- `wiki/concepts/制裁武器.md/`: 1 pages
- `wiki/concepts/前景理论.md/`: 1 pages
- `wiki/concepts/加息预期.md/`: 1 pages
- `wiki/concepts/动态对冲.md/`: 1 pages
- `wiki/concepts/化债.md/`: 1 pages
- `wiki/concepts/化债核心命题.md/`: 1 pages
- `wiki/concepts/化债的成本转嫁与道德风险.md/`: 1 pages
- `wiki/concepts/北约亚太扩张.md/`: 1 pages
- `wiki/concepts/半冲销.md/`: 1 pages
- `wiki/concepts/华盛顿共识.md/`: 1 pages
- `wiki/concepts/单股杠杆ETF.md/`: 1 pages
- `wiki/concepts/卖空机制.md/`: 1 pages
- `wiki/concepts/占优策略与重复博弈.md/`: 1 pages
- `wiki/concepts/去美元化.md/`: 1 pages
- `wiki/concepts/双顺差.md/`: 1 pages
- `wiki/concepts/反倾销税.md/`: 1 pages
- `wiki/concepts/反垄断法.md/`: 1 pages
- `wiki/concepts/反外国不当域外管辖条例.md/`: 1 pages
- `wiki/concepts/反外国制裁法.md/`: 1 pages
- `wiki/concepts/反补贴.md/`: 1 pages
- `wiki/concepts/启发式与偏差.md/`: 1 pages
- `wiki/concepts/囚徒困境.md/`: 1 pages
- `wiki/concepts/回购市场.md/`: 1 pages
- `wiki/concepts/团结税.md/`: 1 pages
- `wiki/concepts/国企改革.md/`: 1 pages
- `wiki/concepts/国债缓冲机制.md/`: 1 pages
- `wiki/concepts/国债逆回购.md/`: 1 pages
- `wiki/concepts/国务院关于产业链供应链安全的规定.md/`: 1 pages
- `wiki/concepts/国务院关于对外投资的规定.md/`: 1 pages
- `wiki/concepts/国家安全法.md/`: 1 pages
- `wiki/concepts/国家理论.md/`: 1 pages
- `wiki/concepts/国家秘密.md/`: 1 pages
- `wiki/concepts/国际收支.md/`: 1 pages
- `wiki/concepts/地方政府隐性债务.md/`: 1 pages
- `wiki/concepts/地缘政治.md/`: 1 pages
- `wiki/concepts/域外管辖权.md/`: 1 pages
- `wiki/concepts/基差风险.md/`: 1 pages
- `wiki/concepts/处置效应.md/`: 1 pages
- `wiki/concepts/外国补贴条例FSR.md/`: 1 pages
- `wiki/concepts/外汇占款.md/`: 1 pages
- `wiki/concepts/外汇干预有效性.md/`: 1 pages
- `wiki/concepts/外汇掉期冲销.md/`: 1 pages
- `wiki/concepts/外汇管制.md/`: 1 pages
- `wiki/concepts/多德弗兰克法案.md/`: 1 pages
- `wiki/concepts/大小盘轮动.md/`: 1 pages
- `wiki/concepts/大欧亚伙伴关系.md/`: 1 pages
- `wiki/concepts/央票.md/`: 1 pages
- `wiki/concepts/央行入市干预.md/`: 1 pages
- `wiki/concepts/央行对冲工具（化债背景）.md/`: 1 pages
- `wiki/concepts/央行政策.md/`: 1 pages
- `wiki/concepts/央行数字货币.md/`: 1 pages
- `wiki/concepts/套利资金.md/`: 1 pages
- `wiki/concepts/套息交易.md/`: 1 pages
- `wiki/concepts/套期保值.md/`: 1 pages
- `wiki/concepts/奥肯定律与潜在产出.md/`: 1 pages
- `wiki/concepts/存款保险.md/`: 1 pages
- `wiki/concepts/存款准备金率.md/`: 1 pages
- `wiki/concepts/官方媒体.md/`: 1 pages
- `wiki/concepts/定向调控.md/`: 1 pages
- `wiki/concepts/实际利率框架.md/`: 1 pages
- `wiki/concepts/实际有效汇率.md/`: 1 pages
- `wiki/concepts/对外关系法.md/`: 1 pages
- `wiki/concepts/对外投资安全审查.md/`: 1 pages
- `wiki/concepts/对外贸易法.md/`: 1 pages
- `wiki/concepts/居民个人对外投资.md/`: 1 pages
- `wiki/concepts/工业加速器法案.md/`: 1 pages
- `wiki/concepts/巴塞尔协议III.md/`: 1 pages
- `wiki/concepts/巴拉萨-萨缪尔森效应.md/`: 1 pages
- `wiki/concepts/市场失灵与外部性.md/`: 1 pages
- `wiki/concepts/市场微观结构.md/`: 1 pages
- `wiki/concepts/市场风险与VaR模型.md/`: 1 pages
- `wiki/concepts/希腊字母.md/`: 1 pages
- `wiki/concepts/广场协议.md/`: 1 pages
- `wiki/concepts/库存周期.md/`: 1 pages
- `wiki/concepts/开正门堵偏门.md/`: 1 pages
- `wiki/concepts/弹性.md/`: 1 pages
- `wiki/concepts/征兵困境.md/`: 1 pages
- `wiki/concepts/微盘股.md/`: 1 pages
- `wiki/concepts/心理账户.md/`: 1 pages
- `wiki/concepts/恶性通胀.md/`: 1 pages
- `wiki/concepts/战损比.md/`: 1 pages
- `wiki/concepts/房地产.md/`: 1 pages
- `wiki/concepts/扩表与缩表.md/`: 1 pages
- `wiki/concepts/技术出口管理.md/`: 1 pages
- `wiki/concepts/技术分析.md/`: 1 pages
- `wiki/concepts/技术分析指标.md/`: 1 pages
- `wiki/concepts/投资组合理论.md/`: 1 pages
- `wiki/concepts/抗通胀资产.md/`: 1 pages
- `wiki/concepts/抵抗轴心.md/`: 1 pages
- `wiki/concepts/损失厌恶.md/`: 1 pages
- `wiki/concepts/收入分配.md/`: 1 pages
- `wiki/concepts/数字服务法DSA.md/`: 1 pages
- `wiki/concepts/数字货币桥.md/`: 1 pages
- `wiki/concepts/数据安全.md/`: 1 pages
- `wiki/concepts/新一轮加息周期.md/`: 1 pages
- `wiki/concepts/新质生产力.md/`: 1 pages
- `wiki/concepts/日元升值.md/`: 1 pages
- `wiki/concepts/日元国际化与外储.md/`: 1 pages
- `wiki/concepts/日本财政扩张担忧.md/`: 1 pages
- `wiki/concepts/最后贷款人.md/`: 1 pages
- `wiki/concepts/有效市场假说.md/`: 1 pages
- `wiki/concepts/期望效用理论.md/`: 1 pages
- `wiki/concepts/期权.md/`: 1 pages
- `wiki/concepts/期货对冲.md/`: 1 pages
- `wiki/concepts/本币升值.md/`: 1 pages
- `wiki/concepts/机会成本.md/`: 1 pages
- `wiki/concepts/杠杆.md/`: 1 pages
- `wiki/concepts/核准备案.md/`: 1 pages
- `wiki/concepts/次级制裁.md/`: 1 pages
- `wiki/concepts/欧债危机.md/`: 1 pages
- `wiki/concepts/欧元区主权债务危机.md/`: 1 pages
- `wiki/concepts/欧洲货币体系.md/`: 1 pages
- `wiki/concepts/欧猪五国.md/`: 1 pages
- `wiki/concepts/正回购.md/`: 1 pages
- `wiki/concepts/汇率传导机制.md/`: 1 pages
- `wiki/concepts/汇率损失.md/`: 1 pages
- `wiki/concepts/汇率超调模型.md/`: 1 pages
- `wiki/concepts/汇率非市场化.md/`: 1 pages
- `wiki/concepts/沃什政策组合.md/`: 1 pages
- `wiki/concepts/沃尔克规则.md/`: 1 pages
- `wiki/concepts/沉没成本.md/`: 1 pages
- `wiki/concepts/法国1983年转向.md/`: 1 pages
- `wiki/concepts/法经济学.md/`: 1 pages
- `wiki/concepts/泡沫经济.md/`: 1 pages
- `wiki/concepts/流动性幻觉.md/`: 1 pages
- `wiki/concepts/流动性消失术.md/`: 1 pages
- `wiki/concepts/流动性虹吸.md/`: 1 pages
- `wiki/concepts/流动性风险.md/`: 1 pages
- `wiki/concepts/浮盈计税.md/`: 1 pages
- `wiki/concepts/海外投行预测偏差.md/`: 1 pages
- `wiki/concepts/消费者剩余与生产者剩余.md/`: 1 pages
- `wiki/concepts/渐进主义.md/`: 1 pages
- `wiki/concepts/热钱.md/`: 1 pages
- `wiki/concepts/特殊再融资债券.md/`: 1 pages
- `wiki/concepts/猪周期.md/`: 1 pages
- `wiki/concepts/现代货币理论 (MMT).md/`: 1 pages
- `wiki/concepts/现状偏见.md/`: 1 pages
- `wiki/concepts/理性预期.md/`: 1 pages
- `wiki/concepts/社会消费品零售.md/`: 1 pages
- `wiki/concepts/离岸央票.md/`: 1 pages
- `wiki/concepts/秩序自由主义.md/`: 1 pages
- `wiki/concepts/稀缺性.md/`: 1 pages
- `wiki/concepts/税收归宿.md/`: 1 pages
- `wiki/concepts/稳定文化.md/`: 1 pages
- `wiki/concepts/窗口指导.md/`: 1 pages
- `wiki/concepts/竞争政策.md/`: 1 pages
- `wiki/concepts/粮食安全.md/`: 1 pages
- `wiki/concepts/纳什均衡.md/`: 1 pages
- `wiki/concepts/经济增长.md/`: 1 pages
- `wiki/concepts/经营者集中审查.md/`: 1 pages
- `wiki/concepts/结构性工具.md/`: 1 pages
- `wiki/concepts/综合整治非法跨境证券期货基金经营活动实施方案.md/`: 1 pages
- `wiki/concepts/网络安全监管.md/`: 1 pages
- `wiki/concepts/美伊备忘录.md/`: 1 pages
- `wiki/concepts/美元加息周期.md/`: 1 pages
- `wiki/concepts/美元流动性.md/`: 1 pages
- `wiki/concepts/美元霸权.md/`: 1 pages
- `wiki/concepts/美联储独立性.md/`: 1 pages
- `wiki/concepts/老登板块.md/`: 1 pages
- `wiki/concepts/联系汇率制度.md/`: 1 pages
- `wiki/concepts/股份回购与注销.md/`: 1 pages
- `wiki/concepts/股债跷跷板效应.md/`: 1 pages
- `wiki/concepts/股息与分红.md/`: 1 pages
- `wiki/concepts/股指期货.md/`: 1 pages
- `wiki/concepts/股汇关系.md/`: 1 pages
- `wiki/concepts/股汇负相关性.md/`: 1 pages
- `wiki/concepts/股牛汇弱.md/`: 1 pages
- `wiki/concepts/自杀式加息.md/`: 1 pages
- `wiki/concepts/舆论战.md/`: 1 pages
- `wiki/concepts/莱茵资本主义.md/`: 1 pages
- `wiki/concepts/菲利普斯曲线.md/`: 1 pages
- `wiki/concepts/蒙代尔-弗莱明模型.md/`: 1 pages
- `wiki/concepts/蛛网模型.md/`: 1 pages
- `wiki/concepts/融资融券.md/`: 1 pages
- `wiki/concepts/行业分析框架.md/`: 1 pages
- `wiki/concepts/行为助推.md/`: 1 pages
- `wiki/concepts/行为金融学.md/`: 1 pages
- `wiki/concepts/规模不经济.md/`: 1 pages
- `wiki/concepts/规模经济与范围经济.md/`: 1 pages
- `wiki/concepts/计划经济转型.md/`: 1 pages
- `wiki/concepts/诱多.md/`: 1 pages
- `wiki/concepts/豆粕.md/`: 1 pages
- `wiki/concepts/负利率.md/`: 1 pages
- `wiki/concepts/财务分析框架.md/`: 1 pages
- `wiki/concepts/财政发力与通胀关联.md/`: 1 pages
- `wiki/concepts/财政政策与货币政策协同.md/`: 1 pages
- `wiki/concepts/财政政策乘数.md/`: 1 pages
- `wiki/concepts/财政货币化.md/`: 1 pages
- `wiki/concepts/财税改革.md/`: 1 pages
- `wiki/concepts/货币兑换（1990东德）.md/`: 1 pages
- `wiki/concepts/货币贬值.md/`: 1 pages
- `wiki/concepts/购买力平价理论.md/`: 1 pages
- `wiki/concepts/贸易战.md/`: 1 pages
- `wiki/concepts/资本管制.md/`: 1 pages
- `wiki/concepts/资源配置.md/`: 1 pages
- `wiki/concepts/赎罪性质回购.md/`: 1 pages
- `wiki/concepts/跨境数据流动.md/`: 1 pages
- `wiki/concepts/跨境资金登记.md/`: 1 pages
- `wiki/concepts/跷跷板效应.md/`: 1 pages
- `wiki/concepts/轧空.md/`: 1 pages
- `wiki/concepts/输入型通胀.md/`: 1 pages
- `wiki/concepts/过度自信.md/`: 1 pages
- `wiki/concepts/进口商品结构.md/`: 1 pages
- `wiki/concepts/进口配额.md/`: 1 pages
- `wiki/concepts/逆向选择.md/`: 1 pages
- `wiki/concepts/逆周期资本缓冲.md/`: 1 pages
- `wiki/concepts/通胀多因素推动论.md/`: 1 pages
- `wiki/concepts/通胀目标制.md/`: 1 pages
- `wiki/concepts/道德风险与委托代理.md/`: 1 pages
- `wiki/concepts/重分红轻回购.md/`: 1 pages
- `wiki/concepts/量价关系.md/`: 1 pages
- `wiki/concepts/量化宽松.md/`: 1 pages
- `wiki/concepts/量比.md/`: 1 pages
- `wiki/concepts/金砖支付系统.md/`: 1 pages
- `wiki/concepts/金穹系统.md/`: 1 pages
- `wiki/concepts/金融传导机制分析框架.md/`: 1 pages
- `wiki/concepts/金融体制改革.md/`: 1 pages
- `wiki/concepts/金融制裁.md/`: 1 pages
- `wiki/concepts/金融投资知识库概览.md/`: 1 pages
- `wiki/concepts/金融武器化.md/`: 1 pages
- `wiki/concepts/金融自由化.md/`: 1 pages
- `wiki/concepts/钢铁进口保护法案.md/`: 1 pages
- `wiki/concepts/铆钉德国马克.md/`: 1 pages
- `wiki/concepts/银行扩表与流动性.md/`: 1 pages
- `wiki/concepts/锚定效应.md/`: 1 pages
- `wiki/concepts/长期资本管理公司.md/`: 1 pages
- `wiki/concepts/长臂管辖.md/`: 1 pages
- `wiki/concepts/阵营化趋势.md/`: 1 pages
- `wiki/concepts/阻断外国法律与措施不当域外适用办法.md/`: 1 pages
- `wiki/concepts/阻断法令.md/`: 1 pages
- `wiki/concepts/降息周期.md/`: 1 pages
- `wiki/concepts/隐性刚兑.md/`: 1 pages
- `wiki/concepts/霸权稳定论.md/`: 1 pages
- `wiki/concepts/静态点火测试.md/`: 1 pages
- `wiki/concepts/非冲销式干预.md/`: 1 pages
- `wiki/concepts/韩国ICT产业集中度.md/`: 1 pages
- `wiki/concepts/预期差交易.md/`: 1 pages
- `wiki/concepts/风险溢价与无风险利率.md/`: 1 pages
- `wiki/concepts/马斯特里赫特条约.md/`: 1 pages
- `wiki/concepts/高通胀保值效应.md/`: 1 pages
- `wiki/concepts/高风险设备供应商清单.md/`: 1 pages
- `wiki/concepts/魏玛恶性通胀.md/`: 1 pages
- `wiki/domains/中国金融与改革.md/`: 1 pages
- `wiki/domains/债券与利率市场.md/`: 1 pages
- `wiki/domains/国际金融与汇率.md/`: 1 pages
- `wiki/domains/宏观经济.md/`: 1 pages
- `wiki/domains/股票与行业分析.md/`: 1 pages
- `wiki/domains/货币政策与中央银行.md/`: 1 pages
- `wiki/domains/银行体系与金融监管.md/`: 1 pages
- `wiki/domains/风险管理.md/`: 1 pages
- `wiki/entities/1948货币改革.md/`: 1 pages
- `wiki/entities/2022年加息周期.md/`: 1 pages
- `wiki/entities/2026年世界杯.md/`: 1 pages
- `wiki/entities/8-11汇改.md/`: 1 pages
- `wiki/entities/AFS会计处理.md/`: 1 pages
- `wiki/entities/BIS.md/`: 1 pages
- `wiki/entities/BTFP.md/`: 1 pages
- `wiki/entities/CHIPS.md/`: 1 pages
- `wiki/entities/CIPS.md/`: 1 pages
- `wiki/entities/Ceconomy.md/`: 1 pages
- `wiki/entities/Christine Lagarde.md/`: 1 pages
- `wiki/entities/DCF模型.md/`: 1 pages
- `wiki/entities/DeepSeek.md/`: 1 pages
- `wiki/entities/ECB.md/`: 1 pages
- `wiki/entities/ESM.md/`: 1 pages
- `wiki/entities/EU理事会.md/`: 1 pages
- `wiki/entities/FDIC.md/`: 1 pages
- `wiki/entities/FOMC会议.md/`: 1 pages
- `wiki/entities/G7.md/`: 1 pages
- `wiki/entities/G7领导人峰会.md/`: 1 pages
- `wiki/entities/HTM会计处理.md/`: 1 pages
- `wiki/entities/Hans Luther.md/`: 1 pages
- `wiki/entities/IMF.md/`: 1 pages
- `wiki/entities/INSTEX.md/`: 1 pages
- `wiki/entities/IRB内部评级法.md/`: 1 pages
- `wiki/entities/Jean-Claude Trichet.md/`: 1 pages
- `wiki/entities/Kweb.md/`: 1 pages
- `wiki/entities/LCR流动性覆盖率.md/`: 1 pages
- `wiki/entities/LDI策略.md/`: 1 pages
- `wiki/entities/LTCM危机.md/`: 1 pages
- `wiki/entities/Manu.md/`: 1 pages
- `wiki/entities/Mario Draghi.md/`: 1 pages
- `wiki/entities/Meta.md/`: 1 pages
- `wiki/entities/Meta收购Manu审查.md/`: 1 pages
- `wiki/entities/NASA.md/`: 1 pages
- `wiki/entities/OPEC.md/`: 1 pages
- `wiki/entities/RCEP.md/`: 1 pages
- `wiki/entities/RSI-指标.md/`: 1 pages
- `wiki/entities/SDR.md/`: 1 pages
- `wiki/entities/SK海力士.md/`: 1 pages
- `wiki/entities/SPFS.md/`: 1 pages
- `wiki/entities/SWIFT.md/`: 1 pages
- `wiki/entities/SpaceX.md/`: 1 pages
- `wiki/entities/Temu.md/`: 1 pages
- `wiki/entities/UFC白宫站.md/`: 1 pages
- `wiki/entities/Wim Duisenberg.md/`: 1 pages
- `wiki/entities/moomoocat.md/`: 1 pages
- `wiki/entities/万科.md/`: 1 pages
- `wiki/entities/三元悖论.md/`: 1 pages
- `wiki/entities/三星电子.md/`: 1 pages
- `wiki/entities/三菱集团.md/`: 1 pages
- `wiki/entities/世界银行.md/`: 1 pages
- `wiki/entities/东德.md/`: 1 pages
- `wiki/entities/东盟.md/`: 1 pages
- `wiki/entities/中东五股力量博弈.md/`: 1 pages
- `wiki/entities/中东地缘格局.md/`: 1 pages
- `wiki/entities/中东局势对全球金融市场的影响.md/`: 1 pages
- `wiki/entities/中华人民共和国财政部.md/`: 1 pages
- `wiki/entities/中国.md/`: 1 pages
- `wiki/entities/中国中免.md/`: 1 pages
- `wiki/entities/中国共产党.md/`: 1 pages
- `wiki/entities/中国台湾.md/`: 1 pages
- `wiki/entities/中国外交部.md/`: 1 pages
- `wiki/entities/中国外贸数据.md/`: 1 pages
- `wiki/entities/中国央行.md/`: 1 pages
- `wiki/entities/中芯国际.md/`: 1 pages
- `wiki/entities/久期.md/`: 1 pages
- `wiki/entities/乌克兰.md/`: 1 pages
- `wiki/entities/也门胡塞武装.md/`: 1 pages
- `wiki/entities/五粮液.md/`: 1 pages
- `wiki/entities/亚洲金融危机传导机制.md/`: 1 pages
- `wiki/entities/亚马逊.md/`: 1 pages
- `wiki/entities/京东.md/`: 1 pages
- `wiki/entities/人民币国际化.md/`: 1 pages
- `wiki/entities/人民币汇率形成机制.md/`: 1 pages
- `wiki/entities/人民日报.md/`: 1 pages
- `wiki/entities/以色列.md/`: 1 pages
- `wiki/entities/价格双轨制.md/`: 1 pages
- `wiki/entities/价格改革时机.md/`: 1 pages
- `wiki/entities/任博宏观论道.md/`: 1 pages
- `wiki/entities/任庄主.md/`: 1 pages
- `wiki/entities/伊拉克亲伊朗武装.md/`: 1 pages
- `wiki/entities/伊朗.md/`: 1 pages
- `wiki/entities/伊朗石油欧元计价.md/`: 1 pages
- `wiki/entities/佩雷拉(UFC).md/`: 1 pages
- `wiki/entities/俄罗斯.md/`: 1 pages
- `wiki/entities/俄罗斯人民币结算.md/`: 1 pages
- `wiki/entities/保时捷控股.md/`: 1 pages
- `wiki/entities/信用风险.md/`: 1 pages
- `wiki/entities/修正久期.md/`: 1 pages
- `wiki/entities/债券价格敏感性.md/`: 1 pages
- `wiki/entities/债务陷阱.md/`: 1 pages
- `wiki/entities/免疫策略.md/`: 1 pages
- `wiki/entities/全球流动性危机.md/`: 1 pages
- `wiki/entities/八部门.md/`: 1 pages
- `wiki/entities/农业农村部.md/`: 1 pages
- `wiki/entities/净稳定资金比率.md/`: 1 pages
- `wiki/entities/凸性.md/`: 1 pages
- `wiki/entities/分税制.md/`: 1 pages
- `wiki/entities/利率市场化.md/`: 1 pages
- `wiki/entities/利率风险.md/`: 1 pages
- `wiki/entities/到期收益率.md/`: 1 pages
- `wiki/entities/前瞻指引.md/`: 1 pages
- `wiki/entities/华夏基金.md/`: 1 pages
- `wiki/entities/压力测试.md/`: 1 pages
- `wiki/entities/原油.md/`: 1 pages
- `wiki/entities/原油价格.md/`: 1 pages
- `wiki/entities/可转债.md/`: 1 pages
- `wiki/entities/商务部.md/`: 1 pages
- `wiki/entities/国债收益率曲线.md/`: 1 pages
- `wiki/entities/国务院.md/`: 1 pages
- `wiki/entities/国家发改委.md/`: 1 pages
- `wiki/entities/国家外汇管理局.md/`: 1 pages
- `wiki/entities/国证有色指数.md/`: 1 pages
- `wiki/entities/国足.md/`: 1 pages
- `wiki/entities/土地财政.md/`: 1 pages
- `wiki/entities/土耳其.md/`: 1 pages
- `wiki/entities/埃及.md/`: 1 pages
- `wiki/entities/城投公司.md/`: 1 pages
- `wiki/entities/外汇储备.md/`: 1 pages
- `wiki/entities/大众汽车.md/`: 1 pages
- `wiki/entities/大商所.md/`: 1 pages
- `wiki/entities/天然气.md/`: 1 pages
- `wiki/entities/央行独立性.md/`: 1 pages
- `wiki/entities/存款保险上限.md/`: 1 pages
- `wiki/entities/存款保险制度.md/`: 1 pages
- `wiki/entities/实体页.md/`: 1 pages
- `wiki/entities/密特朗.md/`: 1 pages
- `wiki/entities/寒武纪.md/`: 1 pages
- `wiki/entities/尼日利亚.md/`: 1 pages
- `wiki/entities/巴勒斯坦哈马斯.md/`: 1 pages
- `wiki/entities/巴基斯坦.md/`: 1 pages
- `wiki/entities/巴塞尔协议.md/`: 1 pages
- `wiki/entities/巴林.md/`: 1 pages
- `wiki/entities/市场风险.md/`: 1 pages
- `wiki/entities/布雷顿森林体系.md/`: 1 pages
- `wiki/entities/布雷顿森林体系瓦解.md/`: 1 pages
- `wiki/entities/库拉索.md/`: 1 pages
- `wiki/entities/彭博.md/`: 1 pages
- `wiki/entities/影子银行.md/`: 1 pages
- `wiki/entities/德国.md/`: 1 pages
- `wiki/entities/德国马克.md/`: 1 pages
- `wiki/entities/恒生科技指数.md/`: 1 pages
- `wiki/entities/意大利.md/`: 1 pages
- `wiki/entities/成交量分析.md/`: 1 pages
- `wiki/entities/成长股vs价值股.md/`: 1 pages
- `wiki/entities/托普利亚(UFC).md/`: 1 pages
- `wiki/entities/折现率.md/`: 1 pages
- `wiki/entities/抢收行为.md/`: 1 pages
- `wiki/entities/拼多多.md/`: 1 pages
- `wiki/entities/操作风险.md/`: 1 pages
- `wiki/entities/收益率曲线.md/`: 1 pages
- `wiki/entities/新兴市场.md/`: 1 pages
- `wiki/entities/新兴市场危机.md/`: 1 pages
- `wiki/entities/新格伦火箭.md/`: 1 pages
- `wiki/entities/日元套利交易.md/`: 1 pages
- `wiki/entities/日本.md/`: 1 pages
- `wiki/entities/日本银行.md/`: 1 pages
- `wiki/entities/日经225.md/`: 1 pages
- `wiki/entities/普京.md/`: 1 pages
- `wiki/entities/最后贷款人.md/`: 1 pages
- `wiki/entities/有效久期.md/`: 1 pages
- `wiki/entities/期限错配.md/`: 1 pages
- `wiki/entities/机床.md/`: 1 pages
- `wiki/entities/梧桐树智库.md/`: 1 pages
- `wiki/entities/次贷危机.md/`: 1 pages
- `wiki/entities/欧元.md/`: 1 pages
- `wiki/entities/欧央行执行委员会.md/`: 1 pages
- `wiki/entities/欧委会.md/`: 1 pages
- `wiki/entities/欧洲议会.md/`: 1 pages
- `wiki/entities/欧盟.md/`: 1 pages
- `wiki/entities/欧盟委员会.md/`: 1 pages
- `wiki/entities/欧盟对华贸易战.md/`: 1 pages
- `wiki/entities/汇率.md/`: 1 pages
- `wiki/entities/汇率风险.md/`: 1 pages
- `wiki/entities/汽车.md/`: 1 pages
- `wiki/entities/沃尔夫冈·保时捷.md/`: 1 pages
- `wiki/entities/沙特.md/`: 1 pages
- `wiki/entities/沙特协议.md/`: 1 pages
- `wiki/entities/流动性陷阱.md/`: 1 pages
- `wiki/entities/海天味业.md/`: 1 pages
- `wiki/entities/渐进式改革.md/`: 1 pages
- `wiki/entities/港股-vs-美股-vs-A股.md/`: 1 pages
- `wiki/entities/滞胀.md/`: 1 pages
- `wiki/entities/点阵图.md/`: 1 pages
- `wiki/entities/牧原股份.md/`: 1 pages
- `wiki/entities/物价闯关.md/`: 1 pages
- `wiki/entities/特朗普.md/`: 1 pages
- `wiki/entities/特里芬难题.md/`: 1 pages
- `wiki/entities/环球时报.md/`: 1 pages
- `wiki/entities/瑞典央行.md/`: 1 pages
- `wiki/entities/瑞士央行.md/`: 1 pages
- `wiki/entities/皮耶希.md/`: 1 pages
- `wiki/entities/监管升级机制.md/`: 1 pages
- `wiki/entities/监管套利.md/`: 1 pages
- `wiki/entities/直升机撒钱.md/`: 1 pages
- `wiki/entities/石油美元体系.md/`: 1 pages
- `wiki/entities/离岸人民币.md/`: 1 pages
- `wiki/entities/科威特.md/`: 1 pages
- `wiki/entities/科尔.md/`: 1 pages
- `wiki/entities/稀土.md/`: 1 pages
- `wiki/entities/税收套利.md/`: 1 pages
- `wiki/entities/税收返还.md/`: 1 pages
- `wiki/entities/立陶宛.md/`: 1 pages
- `wiki/entities/第一次石油危机.md/`: 1 pages
- `wiki/entities/粮食.md/`: 1 pages
- `wiki/entities/系统性风险.md/`: 1 pages
- `wiki/entities/索尼.md/`: 1 pages
- `wiki/entities/索罗斯.md/`: 1 pages
- `wiki/entities/经济预测摘要.md/`: 1 pages
- `wiki/entities/美以伊战争.md/`: 1 pages
- `wiki/entities/美债收益率.md/`: 1 pages
- `wiki/entities/美元周期.md/`: 1 pages
- `wiki/entities/美元微笑理论.md/`: 1 pages
- `wiki/entities/美元指数.md/`: 1 pages
- `wiki/entities/美元霸权.md/`: 1 pages
- `wiki/entities/美光科技.md/`: 1 pages
- `wiki/entities/美国.md/`: 1 pages
- `wiki/entities/美联储.md/`: 1 pages
- `wiki/entities/美联储利率决策.md/`: 1 pages
- `wiki/entities/美联储资产负债表.md/`: 1 pages
- `wiki/entities/美联储银行业监管.md/`: 1 pages
- `wiki/entities/联邦储备系统架构.md/`: 1 pages
- `wiki/entities/联邦基金利率.md/`: 1 pages
- `wiki/entities/股债汇联动.md/`: 1 pages
- `wiki/entities/肥料.md/`: 1 pages
- `wiki/entities/能繁母猪.md/`: 1 pages
- `wiki/entities/船舶.md/`: 1 pages
- `wiki/entities/艾略特波浪理论.md/`: 1 pages
- `wiki/entities/花旗.md/`: 1 pages
- `wiki/entities/英国养老金制度.md/`: 1 pages
- `wiki/entities/英国养老金危机.md/`: 1 pages
- `wiki/entities/英格兰银行.md/`: 1 pages
- `wiki/entities/荷兰.md/`: 1 pages
- `wiki/entities/蓝色起源.md/`: 1 pages
- `wiki/entities/虚收虚报.md/`: 1 pages
- `wiki/entities/行业轮动.md/`: 1 pages
- `wiki/entities/西班牙.md/`: 1 pages
- `wiki/entities/贝佐斯.md/`: 1 pages
- `wiki/entities/财政包干制.md/`: 1 pages
- `wiki/entities/财政货币化.md/`: 1 pages
- `wiki/entities/货币传导机制.md/`: 1 pages
- `wiki/entities/货币信用.md/`: 1 pages
- `wiki/entities/货币创造.md/`: 1 pages
- `wiki/entities/货币层级.md/`: 1 pages
- `wiki/entities/货币政策工具.md/`: 1 pages
- `wiki/entities/货币政策正常化.md/`: 1 pages
- `wiki/entities/货币本质.md/`: 1 pages
- `wiki/entities/贸易顺差.md/`: 1 pages
- `wiki/entities/资产价格渠道.md/`: 1 pages
- `wiki/entities/资产证券化.md/`: 1 pages
- `wiki/entities/资产负债表衰退.md/`: 1 pages
- `wiki/entities/资本充足率.md/`: 1 pages
- `wiki/entities/资本流动.md/`: 1 pages
- `wiki/entities/资本缓冲.md/`: 1 pages
- `wiki/entities/超额准备金.md/`: 1 pages
- `wiki/entities/越南.md/`: 1 pages
- `wiki/entities/转移支付.md/`: 1 pages
- `wiki/entities/通胀预期与美债收益率.md/`: 1 pages
- `wiki/entities/通胀预期管理.md/`: 1 pages
- `wiki/entities/道氏理论.md/`: 1 pages
- `wiki/entities/邓小平.md/`: 1 pages
- `wiki/entities/部分准备金制度.md/`: 1 pages
- `wiki/entities/量化紧缩.md/`: 1 pages
- `wiki/entities/金融创新.md/`: 1 pages
- `wiki/entities/金融稳定.md/`: 1 pages
- `wiki/entities/银行挤兑.md/`: 1 pages
- `wiki/entities/银行监管.md/`: 1 pages
- `wiki/entities/长江存储.md/`: 1 pages
- `wiki/entities/长鑫存储.md/`: 1 pages
- `wiki/entities/阿曼.md/`: 1 pages
- `wiki/entities/阿根廷.md/`: 1 pages
- `wiki/entities/阿联酋.md/`: 1 pages
- `wiki/entities/集中度风险.md/`: 1 pages
- `wiki/entities/集成电路.md/`: 1 pages
- `wiki/entities/霍尔木兹海峡.md/`: 1 pages
- `wiki/entities/非洲猪瘟.md/`: 1 pages
- `wiki/entities/韩国.md/`: 1 pages
- `wiki/entities/韩国KOSPI.md/`: 1 pages
- `wiki/entities/韩国央行.md/`: 1 pages
- `wiki/entities/韩国综合指数.md/`: 1 pages
- `wiki/entities/韩国金融监督院.md/`: 1 pages
- `wiki/entities/风险加权资产.md/`: 1 pages
- `wiki/entities/香港金管局.md/`: 1 pages
- `wiki/entities/马克龙.md/`: 1 pages
- `wiki/entities/高新技术产品.md/`: 1 pages
- `wiki/entities/高盛.md/`: 1 pages
- `wiki/entities/鲍威尔.md/`: 1 pages
- `wiki/entities/麦考利久期.md/`: 1 pages
- `wiki/entities/黎巴嫩真主党.md/`: 1 pages
- `wiki/entities/黑田东彦.md/`: 1 pages
- `wiki/questions/财政货币化.md/`: 1 pages
- `wiki/references/methodology-modes.md/`: 1 pages
- `wiki/references/transport-fallback.md/`: 1 pages
- `wiki/sources/2024-化债政策包.md/`: 1 pages
- `wiki/sources/2026-04-15-2026年1-3月中国外贸数据.md/`: 1 pages
- `wiki/sources/2026-04-29-巴塞尔协议.md/`: 1 pages
- `wiki/sources/2026-05-09-basel-iv-credit-risk.md/`: 1 pages
- `wiki/sources/2026-05-13-日元保卫战-日本央行11万亿干预.md/`: 1 pages
- `wiki/sources/2026-05-22-没人关心普京访华.md/`: 1 pages
- `wiki/sources/2026-06-04-日本史上最大规模汇率保卫战.md/`: 1 pages
- `wiki/sources/2026-06-15-美伊MoU签署与全球狂欢.md/`: 1 pages
- `wiki/sources/2026-06-23-股份回购后注销对股票有什么影响.md/`: 1 pages
- `wiki/sources/2026-06-24-4000亿回购竟然是真的.md/`: 1 pages
- `wiki/sources/2026-06-24-韩国需要冷静冷静.md/`: 1 pages
- `wiki/sources/2026-06-25-逼疯.md/`: 1 pages
- `wiki/sources/837号令.md/`: 1 pages
- `wiki/sources/不结婚，也不消费，谁有办法.md/`: 1 pages
- `wiki/sources/为何日韩会“股牛汇弱”.md/`: 1 pages
- `wiki/sources/冲销式干预.md/`: 1 pages
- `wiki/sources/太不团结了.md/`: 1 pages
- `wiki/sources/崩溃的信徒.md/`: 1 pages
- `wiki/sources/我们已经处于新一轮加息周期中或前夜.md/`: 1 pages
- `wiki/sources/欧盟要与中国打贸易战.md/`: 1 pages
- `wiki/sources/石油美元体系.md/`: 1 pages
- `wiki/sources/触目惊心，都是血包.md/`: 1 pages
- `wiki/sources/跌太惨，朋友都没了.md/`: 1 pages

> [!danger]
> 按 DragonScale 策略,post-rollout 页面必须有 address。这些页面创建时间 >= 2026-04-23,但分配系统未运行。
>
> **修复方案**: 需要重新运行 `wiki-ingest` 时启用 `./scripts/allocate-address.sh`,或手动批量分配。Lint 不会自动修复。

### Pending backfill (informational): 34

34 个 legacy 页面（created < 2026-04-23）尚无 address,按策略暂不需要修复。

---

## Semantic Tiling (DragonScale Mechanism 3)

- 状态: **skipped** (ollama 不可达)
- 启用方法: 运行 `ollama serve` + `ollama pull nomic-embed-text`,然后重新 lint

---

## Duplicate Filenames (6 组)

> [!danger]
> 同一文件夹内不能有重复文件名,但跨文件夹可以。跨文件夹的重复 wikilink 只用 basename 匹配会导致链接歧义。

| 文件名 | 出现位置 |
|--------|----------|
| `冲销式干预` | concepts, sources |
| `最后贷款人` | concepts, entities |
| `美元霸权` | concepts, entities |
| `财政货币化` | concepts, entities, questions |
| `量化宽松` | concepts, entities |
| `石油美元体系` | sources, entities |

---

## Recommended Fix Priority

| 优先级 | 任务 | 数量 | 操作建议 |
|--------|------|------|----------|
| P0 | 创建高频提及的真实缺失页 | ~39 | wiki-ingest 或手动创建 stub |
| P0 | 启用 DragonScale address 分配 | 660 | 修改 wiki-ingest 调用 `./scripts/allocate-address.sh` |
| P1 | 修正路径型 dead link | 70 | 批量补全路径或重命名 |
| P2 | 添加 orphan 页面入站 link | 22 | 从相关概念页/实体页添加 wikilink |
| P3 | 补充 frontmatter 缺口 | 22 | 手动补 type/created/updated |
| P4 | 删除测试残留 | 2 | 删除 `[[Foo]]`、`[[X]]` 等 |
| P5 | 解决重复文件名歧义 | 6 组 | 重命名后批量更新引用 |

---

## How to Apply Fixes

### Safe to auto-fix (review first):
- 添加缺失 frontmatter 字段 (created/updated/tags placeholder)
- 创建高频缺失页面的 stub
- 把 basename-only links 改写为 path-prefix 形式

### Needs human review:
- 删除 orphan 页面 (可能是 intentional)
- 合并重复页 (需要内容比对)
- 解决冲突的 frontmatter 值
- 启用 address 分配系统 (架构决策)

---

## Related Reports

- 7-13 报告 (前次): [[lint-report-2026-07-13]] — 已批量修复 117 个 path-style wikilink
- 历史报告: [[lint-report-2026-07-08]] / [[lint-report-2026-07-07]] / [[lint-report-2026-07-06]]
