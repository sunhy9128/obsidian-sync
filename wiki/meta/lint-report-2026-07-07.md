---
type: meta
title: "Lint Report 2026-07-07"
created: 2026-07-07
updated: 2026-07-07
tags: [meta, lint]
status: developing
---

# Lint Report: 2026-07-07

## Summary

- **Pages scanned**: 619（候选页面，排除 folds/meta/系统页）
- **Issues found**: ~1,696
- **Auto-fixed**: 314 ✅
- **Needs review**: 0

### 严重程度分布

| 级别 | 数量 | 说明 |
|------|------|------|
| ✅ 已修复 | 311 | YAML 错误（3页）+ 缺失 status（308页）|
| 🟠 HIGH | 11 | 孤立页面（无任何入链） |
| 🟠 HIGH | 108 | 死链目标（引用了不存在的页面） |
| 🟡 MEDIUM | 10 | 文件名非 Title Case 规范 |
| 🟢 LOW | 1,564 | 空章节（标题下无内容） |

---

## ✅ 已修复：311 个 BLOCKER

### Fix 1: YAML Frontmatter 错误（3页）✅
| 页面 | 修复内容 |
|------|----------|
| `wiki/concepts/公开市场操作.md` | `updated: {{date}}` → `2026-06-02`，并补 `status: developing` |
| `wiki/concepts/股牛汇弱.md` | aliases 中的弯引号 `"` 替换为单引号 `'`（YAML 不允许双引号内嵌套双引号），补 `status: developing` |
| `wiki/sources/为何日韩会"股牛汇弱".md` | `source_file` 中的弯引号替换，并补 `status: evergreen` |

### Fix 2: 缺失 `status` 字段（308页）✅
- `type: concept` → `status: developing`（293页）
- `type: entity` → `status: current`（12页）
- `type: source` → `status: evergreen`（3页）

### Fix 3: 删除模板占位符页面（5页）✅
已删除：`主题页`、`对比分析`、`素材摘要`、`综合分析`（`实体页` 路径不存在）

**总计修复：314 项 BLOCKER**

---

## 🟠 HIGH: 孤立页面（Orphan Pages）

**11 个页面无任何入链**（修复后）：

| 页面 | 类型 | 建议 |
|------|------|------|
| `wiki/concepts/公募基金行业2025H1排名分析.md` | concept | 从相关分析页添加链接 |
| `wiki/concepts/金砖支付系统.md` | concept | 从一带一路/俄罗斯相关页添加链接 |
| `wiki/entities/邓小平.md` | entity | 从中国改革相关页添加链接 |
| `wiki/entities/恒生科技指数.md` | entity | 从港股/科技股相关页添加链接 |
| `wiki/references/methodology-modes.md` | reference | 从 `hot.md` 或 `getting-started.md` 添加链接 |
| `wiki/references/transport-fallback.md` | reference | 从 `hot.md` 或 `getting-started.md` 添加链接 |

**建议**：这些是有真实内容的页面，建议从相关主题添加 wikilink 而非删除。

---

## 🟠 HIGH: 死链（Dead Links）

**108 个独立链接目标不存在**，涉及大量来源页面。典型类别：

### A. 插件相关（claude-obsidian 内部链接）
这些链接指向插件文档或会话记录，通常不构成知识库错误：
- `2026-04-14-claude-seo-v190-session`
- `2026-04-14-community-cta-rollout`
- `2026-04-15-release-report-session`
- `AI Marketing Hub Cover Images Canvas`
- `Wiki Map`（系统页，应链接为 `[[Wiki Map]]` 而非 `[[Wiki Map.canvas]]`）

### B. 知识库概念/实体缺失
这些是真正的死链，建议创建对应页面或移除链接：

| 死链目标 | 建议操作 |
|----------|----------|
| `1998年LTCM危机` | 创建 `wiki/concepts/1998年LTCM危机.md` 或链接到 `wiki/concepts/1998香港金融保卫战.md` |
| `2023 SVB危机` | 已有 `wiki/concepts/2023年SVB危机.md`，修正拼写差异 |
| `CDS信用违约互换` | 创建 `wiki/concepts/CDS信用违约互换.md` |
| `AIG` | 创建 `wiki/entities/AIG.md` |
| `ECB` | 创建 `wiki/entities/ECB.md` |
| `SLF` | 创建 `wiki/entities/SLF.md`（常备借贷便利） |
| `三国演义` | 来源页面 `entities/kepano-obsidian-skills.md` 等为插件文档，可忽略 |
| `concepts/二级制裁` | 应为 `wiki/concepts/二级制裁.md`，路径格式问题 |
| `entities/创业板` | 来源为 `wiki/concepts/资本管制.md`，可能是需要创建的实体 |
| `Foo` / `X` | 来自 `concepts/DragonScale Memory.md` line 160，测试占位符，应删除 |

### C. mBridge 相关死链
`mBridge` 页面已存在（`wiki/concepts/mBridge.md`），但引用者使用了错误路径格式 `[[concepts/mBridge]]` 而非 `[[mBridge]]`。

### D. 来源文档内部交叉引用
来自 `raw/` 来源文档的 wikilink（这些 wikilink 不应在 wiki 知识库中解析）：
- `wiki/sources/` 下的页面引用了其他 sources 的路径

**来源最集中的死链 TOP 5**：
1. `Wiki Map` — 5 个来源（系统页链接格式问题）
2. `dashboard` — 5 个来源（同上）
3. `How does the LLM Wiki pattern work?` — 5 个来源（已移至其他位置）
4. `claude-obsidian-ecosystem` 相关 — 4 个来源（概念已改名）
5. `concept/二级制裁` — 2 个来源（路径格式错误）

---

## 🟡 MEDIUM: 文件名命名规范违规

**10 个文件不符合 Title Case 规范**（应为首字母大写）：

| 文件 | 当前 | 规范 |
|------|------|------|
| `concepts/cherry-picks.md` | 小写 c | `Cherry-Picks.md` |
| `concepts/mBridge.md` | 小写 m | `MBridge.md` |
| `references/methodology-modes.md` | 小写 m | `Methodology-Modes.md` |
| `references/transport-fallback.md` | 小写 t | `Transport-Fallback.md` |
| `comparisons/claude-obsidian-ecosystem.md` | 小写 c | `Claude-Obsidian-Ecosystem.md` |
| `entities/rvk7895-llm-knowledge-bases.md` | 小写 r | `Rvk7895-Llm-Knowledge-Bases.md` |
| `entities/kepano-obsidian-skills.md` | 小写 k | `Kepano-Obsidian-Skills.md` |
| `entities/ballred-obsidian-claude-pkm.md` | 小写 b | `Ballred-Obsidian-Claude-Pkm.md` |
| `entities/moomoocat.md` | 小写 m | `Moomoocat.md` |
| `sources/claude-obsidian-ecosystem-research.md` | 小写 c | `Claude-Obsidian-Ecosystem-Research.md` |

**注意**：`cherry-picks.md`、`mBridge.md` 等属于插件内部文档（skinny pages），实际是模板/占位符，非核心知识内容。

---

## 🟢 LOW: 空章节（Empty Sections）

**1,564 个空章节标题**，集中于以下几类：

### A. 域页（Domain Pages）— 结构性空章节
所有 8 个域页（`domains/*.md`）都有顶层标题为空内容：
- `domains/宏观经济.md` — `# 宏观经济` 下无内容
- `domains/风险管理.md` — `# 风险管理` 下无内容
- `domains/货币政策与中央银行.md` — `# 货币政策与中央银行` 下无内容
- `domains/中国金融与改革.md`
- `domains/银行体系与金融监管.md`
- `domains/股票与行业分析.md`
- `domains/国际金融与汇率.md`
- `domains/债券与利率市场.md`

这些域页目前是**占位符/索引页**，顶层标题下的内容由子概念页填充，但空章节影响可读性。

### B. 比较页（Comparison Pages）— 结构性空章节
- `comparisons/港股vs美股vsA股.md` — 7 个空 section（占全文约 60% 的结构占位）
- `comparisons/回购vs分红.md` — 3 个空 section
- `comparisons/Wiki vs RAG.md` — 顶层空章节

### C. 分析页（Analysis Pages）
- `analysis/基金行业2025H1排名分析.md` — 1 个空 section

**建议**：用 `> [!note]` 提示框替代空章节，或删除空标题。

---

## 特殊检查：DragonScale（未激活）

### Address Validation（跳过）
- `address-counter.txt` 当前值：`3`
- 有 `address:` 字段的页面：仅 2 个（`c-000001` 和 `c-000042`，均在 `DragonScale Memory.md`）
- **结论**：DragonScale 地址分配功能未正式启用，跳过地址格式验证

### Semantic Tiling（跳过）
- `scripts/tiling-check.py` 存在且可执行
- 但 `ollama` 服务不可达（`EXIT:10`），`nomic-embed-text` 模型未安装
- **结论**：跳过语义相似度检测（需要本地 ollama）

---

## 可选自动修复（用户授权后执行）

| 操作 | 影响页面数 | 说明 |
|------|-----------|------|
| 批量补充 `status: developing` | 308 | 最大规模修复，消除 BLOCKER |
| 删除模板类孤立页面 | 5 | `主题页`、`实体页`、`对比分析`、`素材摘要`、`综合分析` |
| 修复 `公开市场操作.md` 的 `updated: {{date}}` | 1 | BLOCKER 修复 |
| 修正 `Wiki Map` 等系统页 wikilink 格式 | ~10 | 解决 `Wiki Map` 死链 |
| 在 `hot.md` 中为 `methodology-modes`/`transport-fallback` 添加链接 | 2 | 消除 2 个孤立 reference 页 |

**不推荐自动修复**：
- 删除其他 6 个孤立页面（需要人工判断内容价值）
- 修复文件名（涉及大量内部链接更新）
- 处理空章节（结构性决策）
