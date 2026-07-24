---
type: meta
title: "Lint Report 2026-07-24"
created: 2026-07-24
updated: 2026-07-24
tags: [meta, lint]
status: developing
---

# Lint Report: 2026-07-24

## Summary
- Pages scanned: 944
- Transport: cli (obsidian-cli v0.2.3)
- DragonScale: active (counter @ 959)
- Issues found: ~100+
- Auto-fixed: 0
- Needs review: YES

---

## 1. Address Validation (DragonScale) — ERROR

- Counter state: `959` (next available)
- Highest c- address observed: `c-001006`
- Post-rollout pages checked: all pass
- Legacy pages pending backfill: 0 (legacy manifest empty)

### Errors

| Page | Address | Issue |
|------|---------|-------|
| [[武器化相互依存]] | c-001002 | > counter peek (959) — counter drift |
| [[美元潮汐量化实证]] | c-001004 | > counter peek (959) — counter drift |
| [[韩国历史股灾谱系]] | c-001006 | > counter peek (959) — counter drift |

**Fix**: run `./scripts/allocate-address.sh --rebuild` to resync counter.

No invalid format, no duplicates, no post-rollout missing addresses ✅

---

## 2. Dead Links — 73 total

> [!gap] 以下链接指向不存在的页面。列出高频引用源。

### Historical Crisis Series
| 死链 | 引用自 |
|------|--------|
| [[1982 拉美债务危机]] | [[美元周期]] |
| [[1992 欧洲货币危机]] | [[log]] |
| [[1994 龙舌兰危机]] | [[美元潮汐]] |
| [[1997 亚洲金融危机]] | [[log]] |
| [[1998 俄罗斯卢布危机]] | [[美元收割全球的机制]] |
| [[1998 香港金融保卫战]] | [[美元潮汐历史案例]] |
| [[2001 阿根廷违约]] | [[Original Sin（原罪）]] |
| [[2001 阿根廷债务违约]] | [[美元收割全球的机制]] |
| [[2014-2015 俄罗斯卢布危机]] | [[美元收割全球的机制]] |
| [[2018-2019 土耳其阿根廷货币危机]] | [[美元收割全球的机制]] |
| [[2022 俄罗斯制裁]] | [[武器化相互依存]] |
| [[2022 斯里兰卡违约]] | [[美元潮汐量化实证]] |
| [[2022-2024 美联储紧缩周期]] | [[美元收割全球的机制]] |
| [[2023 svb危机]] | (多处) |
| [[2026 新一轮美元紧缩周期与新兴市场]] | [[美元周期]] |

### Missing Entity Pages
| 死链 | 说明 |
|------|------|
| [[微软]] | 多处引用，无实体页 |
| [[港元]] / [[港股]] | 多处引用，无实体页 |
| [[港交所]] / [[证监会]] / [[中证登]] | 监管/机构实体缺失 |
| [[中国电科]] / [[中国船舶]] / [[中核集团]] | 央企实体缺失 |
| [[中央银行]] | 多处引用，无概念页 |
| [[一带一路]] / [[共建"一带一路"]] | 多处引用 |
| [[中华人民共和国国务院]] / [[中华人民共和国中央人民政府]] | 政府实体缺失 |

### Missing Concept Pages
| 死链 | 引用自 |
|------|--------|
| [[ludwig erhard]] | (多处) |
| [[santiago principle]] | 主权财富基金相关 |
| [[brics pay]] / [[金砖支付]] | 金砖相关 |
| [[target2]] | ECB/欧元区相关 |
| [[wiki-mode]] | wiki 技能相关 |
| [[wikilinks]] | wiki 语法相关 |
| [[claude canvas]] | Claude 集成 |
| [[esg 投资]] | ESG 缺概念页 |
| [[how does the llm wiki pattern work?]] | (多处) |
| [[卡脖子技术]] | (多处) |
| [[存储三巨头]] | 半导体相关 |
| [[微盘股指数]] | A股相关 |
| [[金融安全]] | 宏观概念 |
| [[长期主义]] / [[估值修复]] / [[被动投资]] / [[积极股东]] | 投资概念 |
| [[期权策略]] | 衍生品概念 |
| [[天量成交]] / [[财富转移效应]] / [[产业升级]] / [[城镇化]] | 宏观经济 |
| [[伊朗制裁]] | 地缘政治 |
| [[主权基金透明度]] | 主权基金相关 |
| [[美联储点阵图]] / [[货币政策策略]] | 央行相关 |

### Stub / Article References (可能不应作为页面创建)
- 《我们已经处于新一轮加息周期中或前夜》
- 《欧盟要与中国打贸易战？》
- 《环球时报》
- 《综合整治非法跨境证券期货基金经营活动实施方案》
- 韩国股灾简史 (已有 source 页 [[2026-07-21-韩国股灾简史]])
- 韩国需要冷静冷静 (已有 source 页)
- 中国化债政策包-2024 (已有)
- 为何日韩会"股牛汇弱" / 为何日韩会股牛汇弱 (已有 concept 页)

> 建议：创建 stub 实体/概念页，或删除无效 wikilink。

---

## 3. Orphan Pages — 14

无入链的页面：

| 页面 | 类型 | 建议 |
|------|------|------|
| [[2026-07-21-韩国股灾简史]] | source | 新 ingest，等关联 |
| [[中粮]] | entity | 无入链，从相关国资/粮食页加链接 |
| [[傅育宁]] | entity | 同上 |
| [[孟山都]] | entity | 从农业/粮食页加链接 |
| [[宁高宁]] | entity | 从国资相关页加链接 |
| [[庄炳昌]] | entity | 同上 |
| [[柏林墙]] | entity | 从德国/冷战相关页加链接 |
| [[钜盛华]] | entity | 从宝能/万科相关加链接 |
| [[前海人寿]] | entity | 从宝能/险资页加链接 |
| [[国产替代]] | concept | 从半导体/科技页加链接 |
| [[国防军工]] | concept | 从军工相关加链接 |
| [[为何日韩会_股牛汇弱_]] | concept | 命名异常，underscore 包围 |
| [[为何日韩会_股牛汇弱_？.md]] | concept | **双后缀名 + 问号，严重命名问题** |
| [[How does the LLM Wiki pattern work_]] | concept | 尾随 underscore |

---

## 4. Broken Filenames

| 文件 | 问题 |
|------|------|
| `wiki/concepts/_1.md` | stub 页 `\1`，regex 遗物。地址 c-000952，建议删除 |
| `wiki/concepts/为何日韩会_股牛汇弱_？.md.md` | **双 `.md` 后缀**（×2 个同名文件） |
| `wiki/concepts/为何日韩会_股牛汇弱_.md` | filenames 含多余 underscore |
| `wiki/comparisons/Wiki vs RAG.md` | 空格，但不违规（仅不一致） |
| 30+ 概念页含空格 | 虽不违规但降低 wikilink 可靠性 |

**命名一致性问题** (大量英文概念页含空格 vs 中文页一般无空格)：
- `E-commerce SEO.md`, `Search Experience Optimization.md` 等 30+ 英文名含空格
- 与中文概念页命名风格不一致（建议统一为 Title Case with spaces 或 kebab-case）

---

## 5. Frontmatter Gaps

### Missing `type`
- `wiki/questions/为什么索罗斯做空英镑而非法郎.md` — 唯一的问题页缺 type

### Missing `tags` — 约 15 页
主要在 `wiki/concepts/` 和 `wiki/entities/`：
- `PSL.md`, `QE与化债对比.md`, `化债.md`, `点阵图.md`, `美联储.md`, `特里芬难题.md`, `财政货币化.md`, `化债核心命题.md`, `布雷顿森林体系.md`, `特殊再融资债券.md`, `地方政府隐性债务.md`, `银行扩表与流动性.md`, `化债的成本转嫁与道德风险.md`, `央行对冲工具（化债背景）.md`

### Missing `status` — 约 30 页
含多条 source 文件、概念页：
- 巫师财经系列 sources（4 条）
- `2026年世界杯.md`, `301调查.md`, `8-11汇改.md`, `837号令.md`, `Andrej Karpathy.md`, `Compounding Knowledge.md` 等

### Missing `created` — 8 页
- `_index.md`, `getting-started.md`, `hot.md`, `index.md`, `log.md`（系统页可豁免）
- `2025-02-04-中国粮食金融保卫战-巫师财经.md` — 缺 created
- `万科宝能股权之争.md` — 缺 created

---

## 6. Semantic Tiling

**Skipped** — ollama 不可达 (exit 10)。本地未运行 `ollama` 或未安装 `nomic-embed-text`。

```
ollama_reachable: false
model_present: false
cache_entries: 0
thresholds_calibrated: false
```

要启用：安装 ollama → `ollama pull nomic-embed-text` → 重跑 lint。

---

## 7. Style / Naming Conventions

### Status 字段引号不一致
- `"developing"` (345) vs `developing` (57)
- `"current"` (180) vs `current` (63)
- `"stub"` (177) vs `stub` (23)
- `"evergreen"` (26) vs `evergreen` (12)
- `"extracted"` (5) vs `extracted` (3)

YAML 引号不一致不影响解析但不利于维护，建议统一无引号。

### Type 字段引号不一致
- `"entity"` (284) vs `entity` (93)
- `"concept"` (254) vs `concept` (199)
- `"source"` (29) vs `source` (7)

---

## Priority Actions

| 优先级 | 事项 | 操作 |
|--------|------|------|
| 🔴 HIGH | 地址计数器漂移 | `./scripts/allocate-address.sh --rebuild` |
| 🔴 HIGH | `_1.md` 文件 | 确认后删除（regex 遗物） |
| 🔴 HIGH | 双后缀名文件 | 删除 `为何日韩会_股牛汇弱_？.md.md`，保留或重命名正确文件 |
| 🟡 MEDIUM | 实体页孤儿 | 为 8 个无入链 entity 页加链接 |
| 🟡 MEDIUM | Dead links 清理 | 为高频死链接（危机系列、实体、概念）创建 stub 或移除引用 |
| 🟢 LOW | Frontmatter 补全 | 补 tags/status/created 空白 |
| 🟢 LOW | 引号统一 | status/type 字段去引号 |
