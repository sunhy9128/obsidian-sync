---
type: meta
title: "Lint Report 2026-08-03"
created: 2026-08-03
updated: 2026-08-03
tags: [meta, lint]
status: developing
---

# Lint Report: 2026-08-03

## Summary

| 指标 | 数值 |
|------|------|
| 扫描文件 | 1019 |
| wikilink 引用 | ~8400 |
| 断链目标 | 37（含误报类，真问题见下） |
| 孤儿页 | 22（14 内容页 + 8 meta/folds） |
| frontmatter 缺口 | 6（1 内容页 + 5 meta） |
| 地址错误 | 0 |
| 空段落 | 0 |
| 语义 tiling | 跳过（ollama 不可达，exit 10） |

> 工具说明：`scripts/find_dead_links.py` 硬编码日期生成 `lint-report-2026-07-14.md`（已删除，内容并入本报告）；其"真实缺失"清单未处理 `#锚点` 与 `路径/前缀` 链接，本报告已过滤。

---

## 一、Dead Links（按优先级）

### HIGH：韩国系重命名断链（13 处引用）

页面实际文件名带日期前缀，但 8 处链接用裸名：

- `[[韩国股灾简史]]`（8 处）← [[韩国历史股灾谱系]]、[[韩国折价（Korea Discount）]]、[[SK海力士]]、[[三星电子]]、[[韩国综合指数(KOSPI)]]、hot、log、[[2026-06-24-韩国需要冷静冷静]]。实际文件：`sources/2026-07-21-韩国股灾简史.md`
- `[[韩国需要冷静冷静]]`（5 处）← [[韩国历史股灾谱系]]、[[韩国综合指数(KOSPI)]]、hot、log、[[2026-07-21-韩国股灾简史]]。实际文件：`sources/2026-06-24-韩国需要冷静冷静.md`

**建议**：两方案二选一——(a) 给两个 source 页加 `aliases: 韩国股灾简史 / 韩国需要冷静冷静`；(b) 把引用改指带日期全名。

### MEDIUM：空格/命名不匹配（15 处引用）

| 断链 | 引用处 | 实际文件 |
|------|--------|---------|
| `[[1997 亚洲金融危机]]` | 9 处（美元潮汐系列等） | `1997亚洲金融危机.md`（无空格） |
| `[[1992 欧洲货币危机]]` | 3 处 | `1992欧洲货币危机.md` |
| `[[meta/lint-report-2026-05-21]]` | 3 处（金融稳定/银行监管/风险加权资产） | 已删除的历史报告 |
| `[[meta/lint-report-2026-06-24]]` | 3 处（同上） | 已删除的历史报告 |
| `[[1998 香港金融保卫战]]` | 1 处（美元潮汐历史案例） | `1998香港金融保卫战.md` |
| `[[2001 阿根廷债务违约]]` | 1 处（美元收割全球的机制） | `2001 阿根廷违约.md` |
| `[[2023 SVB危机]]` | 1 处（沃尔克规则） | `2023年SVB危机.md` |
| `[[研究：美元如何收割新兴市场（增强版）]]` | 2 处（**index.md、hot.md**） | `questions/研究：美元如何收割新兴市场.md` |

### LOW：导航/历史/大小写（10 处引用）

- `[[Concepts]]`/`[[Entities]]`/`[[Sources]]`（各 2 处）← `_index.md` 系列导航链接，指向不存在的裸名页
- `[[How does the LLM Wiki pattern work?]]`（2 处，hot/log）→ 实际 `How does the LLM Wiki pattern work_.md`（问号转下划线）
- `[[lint-report-2026-07-30]]`（1 处，meta/dashboard）→ 引用不存在的未来报告
- `[[Ludwig Erhard]]`（1 处，德国马克）→ 实际 `entities/LudwigErhard.md`
- `[[DDX/DDY/DDZ 指标]]`（1 处，道氏理论）→ 实际 `DDXDDYDDZ-指标.md`
- `[[Wiki链接]]`/`[[wiki链接]]`（1 处，concepts/wikilinks.md 自引用）→ 实际 `wikilinks.md`
- `[[美元收割全球的机制什么]]`（1 处，log 历史条目笔误）

---

## 二、Missing Pages（建议建 stub 或改链）

| 概念 | 引用处 |
|------|--------|
| 有效需求 | [[凯恩斯主义]] |
| 一带一路 / 共建"一带一路" | [[世界银行]]、[[欧盟]]、2026-04-15 外贸数据 |
| 美联储点阵图 | domains/货币政策与中央银行、触目惊心 source |
| 微盘股指数 | 2026-06-24-4000亿回购 source |
| BRICS Pay | [[武器化相互依存]] |
| 中华人民共和国国务院 / 中央人民政府 | [[商务部]]、[[国务院]] |
| 《环球时报》 | [[中欧经贸关系]]、[[官方媒体]] |
| 《欧盟要与中国打贸易战？》 | [[欧盟]] |
| 《综合整治非法跨境证券期货基金经营活动实施方案》 | 837号令 source |
| Claude Canvas | meta/2026-04-10-backlink-empire-session |

---

## 三、Orphan Pages（22：14 内容 + 8 meta/folds）

**内容页（无入链，多为刻意保留的独立主题）**：

- concepts：1970年代滞胀、2008金融危机、How does the LLM Wiki pattern work_、**X（疑似测试文件）**、亚洲金融危机、汇率制度、货币政策策略、金融危机、银行风险
- entities：LudwigErhard、中国银行间市场、德国经济史、易纲、港股

**meta/folds（预期内，无需处理）**：folds/fold-k3-…、meta/2026-04-10-backlink-empire-session、meta/2026-04-14-community-cta-rollout、meta/2026-04-15-slides-and-release-session、meta/retrieval-benchmark-v1.7、meta/tiling-report-2026-04-24、sources/2026-07-21-韩国股灾简史（仅被断链引用）

> 孤儿不自动删除（可能刻意隔离）。`concepts/X.md`、`concepts/Foo.md` 疑似测试残留，建议人工确认。

---

## 四、Duplicate Candidates（tiling 不可用，人工相似性排查）

- `concepts/2008金融危机.md` vs `concepts/2008全球金融危机.md`
- `concepts/亚洲金融危机.md` vs `concepts/1997亚洲金融危机.md`
- `concepts/How does the LLM Wiki pattern work_.md` vs `concepts/LLM Wiki Pattern.md` vs `concepts/Karpathy LLM Wiki Pattern.md`
- `entities/LudwigErhard.md` vs `entities/德国经济史.md`（[[德国马克]] 同时提及 Ludwig Erhard）

---

## 五、Frontmatter Gaps（6）

- **[[安倍经济学]]：缺 `status`**（内容页，需补）
- meta/2026-04-15-release-report-session：缺 created
- meta/2026-04-15-slides-and-release-session：缺 created
- meta/boundary-frontier-2026-04-24：缺 created
- meta/retrieval-benchmark-v1.7：缺 created、tags
- meta/tiling-report-2026-04-24：全缺（脚本生成，可豁免）

---

## 六、Address Validation（DragonScale M2）

- Counter peek：`1083`；最高观测 c-001082 ✓
- 格式错误：0；地址重复：0；counter drift：0
- Post-rollout 缺地址：0（meta 文件豁免）
- 本次会话规避撞号一次（c-001081 重复 → rebuild 取 c-001082），counter 已自愈

## 七、Semantic Tiling（DragonScale M3）

跳过：`tiling-check.py --peek` exit 10（ollama `http://127.0.0.1:11434` 不可达，模型 nomic-embed-text 未加载）。需 `ollama serve` 后重跑 `--report wiki/meta/tiling-report-2026-08-03.md`。

---

## 八、Stale Index（index.md）

- `[[研究：美元如何收割新兴市场（增强版）]]` 指向不存在页面（真实文件为 questions/研究：美元如何收割新兴市场.md）
- **主目录未收录近期新增页**：[[安倍经济学]]、[[桥本行政改革]]、[[厚生劳动省]]、[[日本95年体制]]、韩国系 5 页（韩国股灾简史/历史股灾谱系/韩国折价/KOSPI/韩国需要冷静冷静）、东欧转型系列等——index 收录 57 页 vs 全库 1019 文件，明显滞后

---

## 建议的自动修复（等你确认）

**安全可自动修**：
1. [[安倍经济学]] frontmatter 补 `status: current`
2. 韩国系 13 处引用改为带日期全名（或加 alias）
3. 空格/命名类 15 处引用改指实际文件名（1997亚洲金融危机/1992欧洲货币危机/1998香港金融保卫战/2001阿根廷违约/2023年SVB危机/研究：美元如何收割新兴市场）
4. index.md 修复死链 + 补录近期新增页
5. 建 stub：有效需求、一带一路、美联储点阵图

**需人工判断**：
- 删除/合并重复页（2008金融危机 vs 2008全球金融危机、亚洲金融危机 vs 1997亚洲金融危机、X.md/Foo.md 测试残留）
- 孤儿页去留
- 历史 lint 报告引用（金融稳定/银行监管/风险加权资产）改链或忽略
