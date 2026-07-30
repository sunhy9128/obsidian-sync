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

> [!important] 老王的话——这次体检纠偏 + 根治一起干了
> 昨天报告把"24 目标/48 处死链"列为 P1 待修。今天老王把 Obsidian 的 **alias 解析逻辑**补进判定后，真死链只剩个位数——而**根治 `lint-scan.py` 后，真死链归零**。韩国股灾简史、1997 亚洲金融危机、1992 欧洲货币危机、美联储点阵图、微盘股指数、2023 SVB 危机……这些在 Obsidian 里**全部能正常跳转**，根本不用修。破扫描器不认 alias/路径/大小写，虚报狼来了，这次一起治了。

## Summary
- Pages scanned: **1019**（concepts 522 / entities 394 / sources 38 / domains 9 / comparisons 7 / questions 6 / analysis 3 / meta 33 / folds 1）
- Transport: `cli` + `filesystem` 兜底（`.vault-meta/transport.json`）
- DragonScale: 特性全开（address-counter @ 1066，tiling-thresholds 已配置）

| 维度 | 修复前 | 修复后 | 状态 |
|------|------|------|------|
| 孤儿页 | 0 | 0 | ✅ 优秀 |
| 地址冲突 | 0 | 0（985 地址全唯一） | ✅ 保持 |
| 地址格式错误 | 0 | 0 | ✅ |
| **真实内容死链** | 23 目标/57 处（含误报） | **0** 🎉 | ✅→✅ |
| lint-scan 报告死链 | 103 目标 | 65（全为 meta/噪音） | ✅ 根治 |
| 伪死链（alias 误报） | 27 目标 | 0（扫描器已认 alias） | ✅ 根治 |
| 核心内容页缺 tags | 610 | 603 | 🟡 MEDIUM |
| Semantic tiling | 跳过 | 跳过（ollama 未装） | ⚪ |

## 🔧 本轮修复清单（全部完成 ✅）

| # | 动作 | 结果 |
|---|------|------|
| 1 | `comparisons/_index.md` 两处去路径前缀（`[[wiki/comparisons/xxx]]`→`[[xxx]]`） | ✅ |
| 2 | 建 `wiki/concepts/中国经济.md` concept stub（address c-001065，seed 状态） | ✅ |
| 3 | 根治 `lint-scan.py`：解析 frontmatter 多行列表 + alias/路径/大小写加入索引 | ✅ |
| 4 | 修 `lint-analyze.py`：死链判定对齐 Obsidian 大小写不敏感 + 日期动态化 | ✅ |

**未修（核实后确认非死链）**：
- `[[2023 SVB危机]]`：alias `2023 svb危机` 大小写不敏感能命中，Obsidian 可跳转，无需补 alias
- `[[研究：美元如何收割新兴市场（增强版）]]`：实际页有同名 alias，可跳转，无需改链

## 🔍 核心纠偏：alias 误报问题（已根治）

### 问题根源
`.vault-meta/lint-scan.py` 旧版构建 `name_to_paths` 索引时**只按文件名 stem，不读 frontmatter `aliases`**，也不认路径前缀写法，也不做大小写折叠。Obsidian 的 wikilink 解析逻辑是 **stem + alias + 路径 + 大小写不敏感**四重命中，于是大量能正常跳转的链接被误报成死链。

本 vault 有 **206 个文件声明了 aliases，共 859 个 alias 条目**——这是一张庞大的"隐藏路由表"，旧扫描器完全无视。

### 根治方案
重写 `lint-scan.py` 的 `parse_frontmatter`：正确处理多行 YAML 列表块（`aliases:`、`tags:`、`related:`、`sources:`）。`name_to_paths` 索引扩充为 6 路：① stem ② stem 小写 ③ 完整相对路径 ④ 完整路径小写 ⑤ alias 原文 ⑥ alias 小写。`lint-analyze.py` 死链判定对齐 Obsidian 大小写不敏感。

### 效果
- lint-scan 报告死链：103 → 65（剩余 65 全为 `meta/lint-report-*`、`Entities/Sources/Concepts`、`raw/*` 等噪音/历史记录，非内容死链）
- **真实内容页死链：23 → 0** 🎉
- tags 统计也更准：610 → 603（多行 tags 列表现在能正确识别）

### 被 alias/大小写/路径救活的「伪死链」（均已根治，无需任何修复）

| 伪死链 | 实际解析到 |
|--------|-----------|
| `[[1997 亚洲金融危机]]` | `wiki/concepts/1997亚洲金融危机.md` |
| `[[韩国股灾简史]]` | `wiki/concepts/韩国历史股灾谱系.md` |
| `[[韩国需要冷静冷静]]` | `wiki/sources/2026-06-24-韩国需要冷静冷静.md` |
| `[[1992 欧洲货币危机]]` | `wiki/concepts/1992欧洲货币危机.md` |
| `[[美联储点阵图]]` | `wiki/entities/点阵图.md` |
| `[[微盘股指数]]` | `wiki/concepts/微盘股.md` |
| `[[2023 SVB危机]]` | `wiki/concepts/2023年SVB危机.md`（alias 大小写不敏感） |
| `[[共建"一带一路"]]` / `[[一带一路]]` | `wiki/concepts/共建一带一路.md` |
| `[[中华人民共和国国务院]]` / `[[中华人民共和国中央人民政府]]` | `wiki/entities/国务院.md` |
| `[[BRICS Pay]]` | `wiki/concepts/金砖支付系统.md` |
| `[[Ludwig Erhard]]` | `wiki/entities/LudwigErhard.md` |
| `[[《环球时报》]]` | `wiki/entities/环球时报.md` |
| `[[研究：美元如何收割新兴市场（增强版）]]` | `wiki/questions/研究：美元如何收割新兴市场.md`（alias） |
| `[[为何日韩会"股牛汇弱"]]` | `wiki/concepts/股牛汇弱.md` |

## Dead Links — ✅ 真死链归零

经「alias + 路径前缀 + 大小写不敏感」三重解析对齐 Obsidian 行为后，**全部内容页 wikilink 均可正常跳转**。lint-scan 报告的 65 个"死链"全部来自：
- `meta/lint-report-*` 之间的历史自引用（lint 报告记录过往死链）
- `meta/dashboard`、`Entities/Sources/Concepts`（_index 大写标题互链）
- `raw/wechat/*`、`Clippings/*`（.raw 原始区，非 wiki 内容）
- `[[MLF\]]`、`[[PSL\]]` 等 log.md 里的转义示例文本

这些非真实内容死链，无需处理。

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
| P1 HIGH | 修 `lint-scan.py`：解析 aliases + 路径 + 大小写加入索引 | 1 处脚本重写 | ✅ 完成 |
| P1 HIGH | 修 `lint-analyze.py`：死链判定大小写不敏感 + 日期动态 | 2 处 | ✅ 完成 |
| P2 MEDIUM | 改 `comparisons/_index.md` 两处去路径前缀 | 2 处 | ✅ 完成 |
| P2 MEDIUM | 建 `中国经济` concept stub（c-001065） | 1 页 | ✅ 完成 |
| ~~P2~~ | ~~补 `2023年SVB危机.md` alias~~ | — | ✅ 无需修（大小写不敏感能命中） |
| ~~P2~~ | ~~index.md 研究页改链~~ | — | ✅ 无需修（alias 能命中） |
| P3 LOW | 补 603 核心页 tags（批量） | 大 | ⏳ 待处理 |
| P3 LOW | Semantic tiling 启用（装 ollama + pull 模型） | 环境配置 | ⏳ 待处理 |
| P3 LOW | `index.md` 4 处 `meta/*` 路径前缀规范化 | 4 处 | ⏳ 可选 |

---

> [!note] 老王的话
> 体检 + 根治一起收工。真死链归零——内容页 wikilink 全部能跳转。破 `lint-scan.py` 不认 alias/路径/大小写的毛病治好了，以后报告死链数从虚报 103 直接掉到真实值（65，还全是 meta 噪音）。地址体系保持干净（985 地址零冲突），新建中国经济 stub 拿了 c-001065。昨天的 P0 修复今天复核没回潮。剩 603 核心页缺 tags 是老问题，批量补得慢慢来。git 那些破事老王没你话没碰，改动都落盘了，你瞅着满意再说提交。
