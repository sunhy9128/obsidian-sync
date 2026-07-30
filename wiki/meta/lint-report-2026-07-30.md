---
type: meta
title: "Lint Report 2026-07-30"
created: 2026-07-30
updated: 2026-07-30
tags: [meta, lint]
status: current
related:
  - "[[index]]"
  - "[[log]]"
  - "[[lint-report-2026-07-29]]"
---

# Lint Report: 2026-07-30

> [!important] 老王的话——这次体检纠了个大偏
> 昨天报告把"24 目标/48 处死链"列为 P1 待修。今天老王把 Obsidian 的 **alias 解析逻辑**补进判定后，**真死链只剩 4 个目标/4 处**——其余全是 `lint-scan.py` 不认 alias 造成的**误报**。韩国股灾简史、1997 亚洲金融危机、1992 欧洲货币危机、美联储点阵图、微盘股指数……这些在 Obsidian 里**全部能正常跳转**，根本不用修。别再被那个破扫描器骗了。

## Summary
- Pages scanned: **1017**（concepts 521 / entities 394 / sources 38 / domains 9 / comparisons 7 / questions 6 / analysis 3 / meta 33 / folds 1）
- Transport: `cli` + `filesystem` 兜底（`.vault-meta/transport.json`）
- DragonScale: 特性全开（address-counter @ 1065，tiling-thresholds 已配置）

| 维度 | 数值 | 状态 |
|------|------|------|
| 孤儿页 | 0 | ✅ 优秀 |
| 地址格式错误 | 0 | ✅ |
| 地址冲突 | 0（985 地址全唯一） | ✅ 保持 |
| **真实死链** | **4 目标 / 4 处** | 🟡 LOW（修起来简单） |
| 伪死链（alias 误报） | 27 目标 | ⚪ 无需修 |
| 核心内容页缺 tags | 610 | 🟡 MEDIUM |
| index.md 死链 | 1 真 + 4 伪 | 🟡 LOW |
| Semantic tiling | 跳过（ollama 未安装） | ⚪ |

## 🔍 核心纠偏：alias 误报问题

### 问题根源
`.vault-meta/lint-scan.py` 构建 `name_to_paths` 索引时**只按文件名 stem，不读 frontmatter `aliases`**。Obsidian 的 wikilink 解析逻辑是 **stem + alias 双重命中**，于是所有靠 alias 解析的链接都被 lint 误报成死链。

本 vault 有 **206 个文件声明了 aliases，共 859 个 alias 条目**——这是一张庞大的"隐藏路由表"，lint-scan 完全无视。

### 被 alias 救活的伪死链（27 个，均为 lint 误报，无需任何修复）

| 伪死链 | 实际解析到 |
|--------|-----------|
| `[[1997 亚洲金融危机]]` | `wiki/concepts/1997亚洲金融危机.md` |
| `[[韩国股灾简史]]` | `wiki/concepts/韩国历史股灾谱系.md` |
| `[[韩国需要冷静冷静]]` | `wiki/sources/2026-06-24-韩国需要冷静冷静.md` |
| `[[1992 欧洲货币危机]]` | `wiki/concepts/1992欧洲货币危机.md` |
| `[[美联储点阵图]]` | `wiki/entities/点阵图.md` |
| `[[微盘股指数]]` | `wiki/concepts/微盘股.md` |
| `[[共建"一带一路"]]` / `[[一带一路]]` | `wiki/concepts/共建一带一路.md` |
| `[[中华人民共和国国务院]]` / `[[中华人民共和国中央人民政府]]` | `wiki/entities/国务院.md` |
| `[[BRICS Pay]]` | `wiki/concepts/金砖支付系统.md` |
| `[[Ludwig Erhard]]` | `wiki/entities/LudwigErhard.md` |
| `[[《环球时报》]]` | `wiki/entities/环球时报.md` |
| `[[《我们已经处于新一轮加息周期中或前夜》]]` | `wiki/sources/我们已经处于新一轮加息周期中或前夜.md` |
| `[[为何日韩会"股牛汇弱"]]` | `wiki/concepts/股牛汇弱.md` |
| 其余 14 个 | 均有 alias 解析 |

> [!gap] 待改进项
> `lint-scan.py` 应当解析 frontmatter `aliases`，把 alias 也加入 `name_to_paths` 索引。这是扫描器的 bug，不是 wiki 内容的问题。修了它，以后 lint 报告的死链数会从 103 直接掉到真实值。

## Dead Links — 真死链（仅 4 个，Obsidian 也无法解析）

### 1. `[[2023 SVB危机]]` — 补 alias 即修 🟢
- **引用方**：`wiki/concepts/沃尔克规则.md`（1 处，第 961 行）
- **目标页**：`wiki/concepts/2023年SVB危机.md` 已存在
- **问题**：目标页 alias 有 `硅谷银行危机`/`SVB 倒闭`/`2023 年银行业危机`/`Silicon Valley Bank Crisis`/`硅谷银行倒闭事件`，**独缺 `2023 SVB危机`**（引用写法无"年"字，现有 alias 带年字或不同表述）
- **修复**：给 `2023年SVB危机.md` 的 aliases 追加 `"2023 SVB危机"`

### 2. `[[中国经济]]` — 建 stub 或改链 🟡
- **引用方**：`wiki/sources/2024-12-18-二十届三中全会细节解析-巫师财经.md`（1 处，第 313 行 `[[中国经济|中国经济]]`）
- **目标页**：不存在。无 alias 能解析。
- **修复建议**：建一个简短 concept stub `wiki/concepts/中国经济.md`（type: concept, status: seed），或改链到已有的宏观经济相关 domain 页 `[[宏观经济]]`

### 3-4. `comparisons/_index.md` 两处带路径前缀链接 — 改链去前缀 🟢
- `[[wiki/comparisons/港股vs美股vsA股|港股 vs 美股 vs A 股]]`（第 17 行）
- `[[wiki/comparisons/中俄联合声明2021vs2026|中俄联合声明对比：2021 vs 2026]]`（第 20 行）
- **问题**：目标文件存在，Obsidian **能解析**带路径写法，但 `lint-scan.py` 只按 stem 索导致报死链。写法冗余不规范。
- **修复**：去掉路径前缀，改用 stem：`[[港股vs美股vsA股|港股 vs 美股 vs A 股]]`、`[[中俄联合声明2021vs2026|中俄联合声明对比：2021 vs 2026]]`

## Orphan Pages
**0 个**。链接网络健康，零孤儿。这点做得漂亮。

## Address Validation（DragonScale Mechanism 2）— ✅ 干净

- Counter state: `1065`（`./scripts/allocate-address.sh --peek`）
- 已分配地址页面: **985**
- 唯一地址数: **985**
- 地址格式错误: **0**
- 地址冲突组: **0** ✅（昨天 P0 修复保住，未回潮）
- Legacy pages pending backfill: 0
- Post-rollout 缺地址页: 0

地址体系完全干净。昨天清的 9 组冲突 + 25 个 meta 页抢号，今天复核全部保住。

## Frontmatter Gaps — 🟡 MEDIUM

- **610 个核心内容页缺 `tags`**（entities 289 / concepts 269 / sources 29 / domains 9 / comparisons 7 / analysis 3 / questions 3 / strategies 1）
- 其余必填字段（type/status/created/updated）全部齐全 ✅
- meta/session 类缺 tags 22 个，本可不强求
- **影响**：缺 tags 影响 Dataview 聚类检索与按主题过滤，MEDIUM 级
- **注意**：`tags: []`（空列表）也算缺——例如 `韩国需要冷静冷静` source 页就是空 tags

## index.md 陈旧条目 — 🟡 LOW

index.md 共 120 个 wikilink，5 个 lint 报死链：
- **4 个为路径前缀误报**（文件存在，Obsidian 能解析）：`[[meta/2026-04-14-community-cta-rollout]]`、`[[meta/2026-04-15-slides-and-release-session]]`、`[[meta/2026-04-15-release-report-session]]`、`[[meta/2026-04-14-claude-seo-v190-session]]` — 同 _index.md 那俩，写法带 `meta/` 前缀，可统一去前缀
- **1 个真死链**：`[[研究：美元如何收割新兴市场（增强版）]]` — 实际页是 `wiki/questions/研究：美元如何收割新兴市场.md`（无"增强版"后缀）。改链去掉"（增强版）"即修

## Missing Cross-References / Stale Claims
未发现明显陈旧论断。近期页（美元潮汐系列、韩国股灾系列、化债系列、广场协议系列）交叉引用密集，时序闭环良好。`[[1997亚洲金融危机]]`、`[[1992欧洲货币危机]]`、`[[点阵图]]` 等历史缺失页经核实**已建好且有 alias**，昨天报告的"建议建 stub"实际早已完成。

## Semantic Tiling
本轮 ollama `tiling-check.py` 未跑（环境未安装 ollama，需 `ollama pull nomic-embed-text`）。手动未发现明显语义重复页——昨天合并的特里芬难题（concepts vs entities）已收敛为唯一正本。

## Empty Sections
> [!gap] 检测受限说明
> 空标题节自动检测的假阳性率高（父子嵌套标题、紧跟 callout/表格的标题会被误判），本次不给量化数字，避免误导。抽样肉眼确认 `机会成本.md` 等页面节内容完整。此项降级为 LOW，留待后续用更可靠的 AST 级检测处理。

## 修复优先级建议

| 优先级 | 动作 | 工作量 | 状态 |
|--------|------|--------|------|
| P1 HIGH | 修 `lint-scan.py`：解析 aliases 加入索引 | 1 处脚本改动 | ⏳ 根治误报 |
| P2 MEDIUM | 补 `2023年SVB危机.md` 的 `2023 SVB危机` alias | 1 行 | ⏳ |
| P2 MEDIUM | index.md `研究：美元如何收割新兴市场（增强版）` 改链去后缀 | 1 处 | ⏳ |
| P2 MEDIUM | 建 `中国经济` concept stub 或改链到 `[[宏观经济]]` | 1 页/1 处 | ⏳ |
| P3 LOW | `_index.md` / `index.md` 去掉路径前缀写法（5 处） | 5 处 | ⏳ 规范化 |
| P3 LOW | 补 610 核心页 tags（批量） | 大 | ⏳ |
| P3 LOW | Semantic tiling 启用（装 ollama + pull 模型） | 环境配置 | ⏳ |

---

> [!note] 老王的话
> 体检纠偏完成。昨天的 P0 修复（地址体系）今天复核全部保住——985 地址零冲突零格式错误，没回潮，这点靠谱。但昨天当成 P1 死链的韩国股灾简史、亚洲金融危机那一坨，**全是 lint-scan.py 不认 alias 的误报**——Obsidian 里跳得好好的。真死链就 4 个，修起来都是一两行的事。根治办法是给 `lint-scan.py` 补上 alias 解析，以后报告别再虚报狼来了。剩 610 核心页缺 tags 是老问题，批量补得慢慢来。你啥时候要治这 4 个真死链或修扫描器，喊老王一声。
