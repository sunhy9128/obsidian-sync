---
type: meta
title: "Lint Report 2026-07-14"
created: 2026-07-14
updated: 2026-07-14
tags: [meta, lint, dead-links]
status: developing
---

# Lint Report: 2026-07-14 — Wiki 断链专项

## 摘要

| 指标 | 数值 |
|------|------|
| 扫描页面 | 998 |
| 扫描文件 | 1015 |
| 别名总数 | 848 |
| wikilink 引用总数 | 8442 |
| **断链目标数** | **91** |
| **断链引用处数** | **172** |

> **说明**：本报告已包含 Obsidian aliases 匹配——如果 wikilink 目标在某页面的 aliases 中，则视为有效链接。

## 分类概览

| 分类 | 数量 | 处理建议 |
|------|------|---------|
| 误报 | 27 | 无需处理（canvas、反斜杠、代码块误读） |
| 历史 | 2 | 无需处理（历史 lint 报告） |
| 路径错误 | 3 | 建议修正（去掉路径前缀或 .md） |
| 格式错误 | 7 | 建议修正（引号、大小写、标点、空格） |
| 缺失 | 52 | 需新建 stub 页面或修正为已存在的概念 |

---

## 📋 详细断链清单

### 🚨 真实缺失（需新建）（52 个）

- `[[meta/dashboard]]` (4 处) — 真实缺失，需新建
- `[[Claude Canvas]]` (3 处) — 真实缺失，需新建
- `[[cherry-picks#1. URL Ingestion in /wiki-ingest]]` (3 处) — 真实缺失，需新建
- `[[raw/wechat/2026-06-15-美伊MoU签署与全球狂欢]]` (3 处) — 真实缺失，需新建
- `[[Entities]]` (3 处) — 真实缺失，需新建
- `[[Sources]]` (3 处) — 真实缺失，需新建
- `[[Concepts]]` (3 处) — 真实缺失，需新建
- `[[美元收割全球的机制什么]]` (2 处) — 真实缺失，需新建
- `[[meta/2026-04-14-community-cta-rollout]]` (2 处) — 真实缺失，需新建
- `[[meta/2026-04-15-slides-and-release-session]]` (2 处) — 真实缺失，需新建
- `[[meta/2026-04-15-release-report-session]]` (2 处) — 真实缺失，需新建
- `[[meta/2026-04-14-claude-seo-v190-session]]` (2 处) — 真实缺失，需新建
- `[[folder/file]]` (2 处) — 真实缺失，需新建
- `[[...]]` (2 处) — 真实缺失，需新建
- `[[TARGET2]]` (2 处) — 真实缺失，需新建
- `[[\1]]` (2 处) — 真实缺失，需新建
- `[[为何日韩会"股牛汇弱"]]` (2 处) — 真实缺失，需新建
- `[[金砖支付]]` (2 处) — 真实缺失，需新建
- `[[target2]]` (2 处) — 真实缺失，需新建
- `[[claude canvas]]` (2 处) — 真实缺失，需新建
- `[[为何日韩会_股牛汇弱_]]` (2 处) — 真实缺失，需新建
- `[[为何日韩会_股牛汇弱_？.md]]` (2 处) — 真实缺失，需新建
- `[[cherry-picks#10. Marp Presentation Output]]` (2 处) — 真实缺失，需新建
- `[[cherry-picks#11. obsidian-memory-mcp Integration]]` (2 处) — 真实缺失，需新建
- `[[cherry-picks#12. obsidian-bases Skill (from kepano)]]` (2 处) — 真实缺失，需新建
- `[[cherry-picks#13. Schema-Emergent Vault Mode]]` (2 处) — 真实缺失，需新建
- `[[cherry-picks#2. Auto-Commit PostToolUse Hook]]` (2 处) — 真实缺失，需新建
- `[[cherry-picks#3. defuddle Web Cleaning Skill]]` (2 处) — 真实缺失，需新建
- `[[cherry-picks#4. Delta Tracking Manifest]]` (2 处) — 真实缺失，需新建
- `[[cherry-picks#5. Multi-Depth Query Modes]]` (2 处) — 真实缺失，需新建
- `[[cherry-picks#6. /wiki-ingest Vision Support]]` (2 处) — 真实缺失，需新建
- `[[cherry-picks#7. /adopt — Import Existing Vault]]` (2 处) — 真实缺失，需新建
- `[[cherry-picks#8. Productivity Wrapper (Daily/Weekly Reviews)]]` (2 处) — 真实缺失，需新建
- `[[cherry-picks#9. Multi-Agent Compatibility]]` (2 处) — 真实缺失，需新建
- `[[cherry-picks#9. Multi-Agent Compatibility (Cursor, Windsurf, Codex)]]` (2 处) — 真实缺失，需新建
- `[[raw/wechat/2026-06-24-4000亿回购竟然是真的]]` (2 处) — 真实缺失，需新建
- `[[raw/wechat/2026-06-24-韩国需要冷静冷静]]` (2 处) — 真实缺失，需新建
- `[[raw/wechat/2026-06-25-逼疯]]` (2 处) — 真实缺失，需新建
- `[[raw/wechat/不结婚，也不消费，谁有办法]]` (2 处) — 真实缺失，需新建
- `[[raw/wechat/崩溃的信徒]]` (2 处) — 真实缺失，需新建
- `[[raw/wechat/触目惊心，都是血包]]` (2 处) — 真实缺失，需新建
- `[[raw/wechat/跌太惨，朋友都没了]]` (2 处) — 真实缺失，需新建
- `[[raw/zhihu/日元保卫战：日本央行11万亿干预，为何挡不住160？]]` (2 处) — 真实缺失，需新建
- `[[wiki/domains/中国经济]]` (2 处) — 真实缺失，需新建
- `[[三元悖论#三个自我实现的均衡]]` (2 处) — 真实缺失，需新建
- `[[人民币国际化#CIPS 的战略意义]]` (2 处) — 真实缺失，需新建
- `[[人民币国际化#三条腿框架]]` (2 处) — 真实缺失，需新建
- `[[人民币汇率形成机制#CNY-CNH 价差的意义]]` (2 处) — 真实缺失，需新建
- `[[央行数字货币#mBridge]]` (2 处) — 真实缺失，需新建
- `[[奥肯定律与潜在产出#七、潜在产出与政策评估]]` (2 处) — 真实缺失，需新建
- ... 还有 2 个

### 🔧 路径错误（建议修正）（3 个）

- `[[Clippings/837号令.md]]` (2 处) — 应为 [[837号令]]（去掉路径和 .md）
- `[[Clippings/太不团结了.md]]` (2 处) — 应为 [[太不团结了]]（去掉路径和 .md）
- `[[wiki/X]]` (2 处) — 应为 [[X]]（去掉路径前缀）

### ✏️ 格式错误（建议修正）（7 个）

- `[[How does the LLM Wiki pattern work?]]` (4 处) — 应为 [[how does the LLM wiki pattern work?]]（大小写）
- `[[ludwig erhard]]` (2 处) — 应为 [[Ludwig Erhard]]（大小写）
- `[[santiago principle]]` (2 处) — 应为 [[Santiago Principle]]（大小写）
- `[[brics pay]]` (2 处) — 应为 [[BRICS Pay]]（大小写）
- `[[esg 投资]]` (2 处) — 应为 [[ESG 投资]]（大小写）
- `[[2023 SVB危机]]` (2 处) — 应为 [[2023 svb危机]]（大小写）
- `[[Wiki链接]]` (2 处) — 应为 [[wiki链接]]（大小写）

### ℹ️ 误报（无需处理）（27 个）

- `[[wiki/meta/化债机制图谱.canvas]]` (2 处) — canvas 文件，不是 markdown 页面
- `[[wiki/X` → `[[X` 跨全 vault(本次继承问题,本次未引入新错误)。

---

## Cross-Reference Verification

### 入站链接(谁引用了新页面)]]` (2 处) — 包含反引号（代码块误读）
- `[[wiki/` 路径格式的 wikilinks，发现以下潜在问题：]]` (2 处) — 包含反引号（代码块误读）
- `[[MLF\]]` (1 处) — 反斜杠结尾（markdown 转义错误）
- `[[PSL\]]` (1 处) — 反斜杠结尾（markdown 转义错误）
- `[[美联储\]]` (1 处) — 反斜杠结尾（markdown 转义错误）
- `[[中国央行\]]` (1 处) — 反斜杠结尾（markdown 转义错误）
- `[[美联储独立性\]]` (1 处) — 反斜杠结尾（markdown 转义错误）
- `[[鲍威尔\]]` (1 处) — 反斜杠结尾（markdown 转义错误）
- `[[LPR\]]` (1 处) — 反斜杠结尾（markdown 转义错误）
- `[[存款准备金率\]]` (1 处) — 反斜杠结尾（markdown 转义错误）
- `[[窗口指导\]]` (1 处) — 反斜杠结尾（markdown 转义错误）
- `[[扩表与缩表\]]` (1 处) — 反斜杠结尾（markdown 转义错误）
- `[[央行政策\]]` (1 处) — 反斜杠结尾（markdown 转义错误）
- `[[化债核心命题\]]` (1 处) — 反斜杠结尾（markdown 转义错误）
- `[[QE与化债对比\]]` (1 处) — 反斜杠结尾（markdown 转义错误）
- `[[mBridge\]]` (1 处) — 反斜杠结尾（markdown 转义错误）
- `[[冲销式干预\]]` (1 处) — 反斜杠结尾（markdown 转义错误）
- `[[欧洲央行\]]` (1 处) — 反斜杠结尾（markdown 转义错误）
- `[[央行对冲工具（化债背景）\]]` (1 处) — 反斜杠结尾（markdown 转义错误）
- `[[周小川\]]` (1 处) — 反斜杠结尾（markdown 转义错误）
- `[[特朗普\]]` (1 处) — 反斜杠结尾（markdown 转义错误）
- `[[2013年钱荒\]]` (1 处) — 反斜杠结尾（markdown 转义错误）
- `[[2020美国财政刺激\]]` (1 处) — 反斜杠结尾（markdown 转义错误）
- `[[2008全球金融危机\]]` (1 处) — 反斜杠结尾（markdown 转义错误）
- `[[长鑫存储\]]` (1 处) — 反斜杠结尾（markdown 转义错误）
- `[[回购注销\]]` (1 处) — 反斜杠结尾（markdown 转义错误）

### 📚 历史引用（无需处理）（2 个）

- `[[meta/lint-report-2026-05-21]]` (4 处) — 历史 lint 报告，引用属正常
- `[[meta/lint-report-2026-06-24]]` (4 处) — 历史 lint 报告，引用属正常

---

## 🎯 修复优先级（HIGH ≥ 3 处引用）

### HIGH 优先级（缺失，引用 ≥ 3 次）：7 个

- `[[meta/dashboard]]` (4 处)
- `[[Claude Canvas]]` (3 处)
- `[[cherry-picks#1. URL Ingestion in /wiki-ingest]]` (3 处)
- `[[raw/wechat/2026-06-15-美伊MoU签署与全球狂欢]]` (3 处)
- `[[Entities]]` (3 处)
- `[[Sources]]` (3 处)
- `[[Concepts]]` (3 处)

### MEDIUM 优先级（缺失，引用 2 次）：45 个

- `[[...]]`
- `[[TARGET2]]`
- `[[\1]]`
- `[[cherry-picks#10. Marp Presentation Output]]`
- `[[cherry-picks#11. obsidian-memory-mcp Integration]]`
- `[[cherry-picks#12. obsidian-bases Skill (from kepano)]]`
- `[[cherry-picks#13. Schema-Emergent Vault Mode]]`
- `[[cherry-picks#2. Auto-Commit PostToolUse Hook]]`
- `[[cherry-picks#3. defuddle Web Cleaning Skill]]`
- `[[cherry-picks#4. Delta Tracking Manifest]]`
- `[[cherry-picks#5. Multi-Depth Query Modes]]`
- `[[cherry-picks#6. /wiki-ingest Vision Support]]`
- `[[cherry-picks#7. /adopt — Import Existing Vault]]`
- `[[cherry-picks#8. Productivity Wrapper (Daily/Weekly Reviews)]]`
- `[[cherry-picks#9. Multi-Agent Compatibility]]`
- `[[cherry-picks#9. Multi-Agent Compatibility (Cursor, Windsurf, Codex)]]`
- `[[claude canvas]]`
- `[[folder/file]]`
- `[[meta/2026-04-14-claude-seo-v190-session]]`
- `[[meta/2026-04-14-community-cta-rollout]]`
- `[[meta/2026-04-15-release-report-session]]`
- `[[meta/2026-04-15-slides-and-release-session]]`
- `[[raw/wechat/2026-06-24-4000亿回购竟然是真的]]`
- `[[raw/wechat/2026-06-24-韩国需要冷静冷静]]`
- `[[raw/wechat/2026-06-25-逼疯]]`
- `[[raw/wechat/2026-07-21-韩国股灾简史]]`
- `[[raw/wechat/不结婚，也不消费，谁有办法]]`
- `[[raw/wechat/崩溃的信徒]]`
- `[[raw/wechat/触目惊心，都是血包]]`
- `[[raw/wechat/跌太惨，朋友都没了]]`
- `[[raw/zhihu/日元保卫战：日本央行11万亿干预，为何挡不住160？]]`
- `[[target2]]`
- `[[wiki/domains/中国经济]]`
- `[[三元悖论#三个自我实现的均衡]]`
- `[[为何日韩会"股牛汇弱"]]`
- `[[为何日韩会_股牛汇弱_]]`
- `[[为何日韩会_股牛汇弱_？.md]]`
- `[[人民币国际化#CIPS 的战略意义]]`
- `[[人民币国际化#三条腿框架]]`
- `[[人民币汇率形成机制#CNY-CNH 价差的意义]]`
- `[[央行数字货币#mBridge]]`
- `[[奥肯定律与潜在产出#七、潜在产出与政策评估]]`
- `[[汇率传导机制#3. 资产负债表渠道 (Balance Sheet Channel)]]`
- `[[美元收割全球的机制什么]]`
- `[[金砖支付]]`

### LOW 优先级（缺失，引用 1 次）：0 个


---

## 🔧 路径错误批量修正

这些链接的目标页面**已存在**，只是路径前缀错误。可用批量脚本修正。

| 错误链接 | 应改为 | 次数 |
|---------|--------|------|
| `[[Clippings/837号令.md]]` | `[[837号令]]` | 2 |
| `[[Clippings/太不团结了.md]]` | `[[太不团结了]]` | 2 |
| `[[wiki/X]]` | `[[X]]` | 2 |

---

## ✏️ 格式错误批量修正

| 错误链接 | 应改为 | 次数 |
|---------|--------|------|
| `[[How does the LLM Wiki pattern work?]]` | `[[how does the LLM wiki pattern work?]]` | 4 |
| `[[ludwig erhard]]` | `[[Ludwig Erhard]]` | 2 |
| `[[santiago principle]]` | `[[Santiago Principle]]` | 2 |
| `[[brics pay]]` | `[[BRICS Pay]]` | 2 |
| `[[esg 投资]]` | `[[ESG 投资]]` | 2 |
| `[[2023 SVB危机]]` | `[[2023 svb危机]]` | 2 |
| `[[Wiki链接]]` | `[[wiki链接]]` | 2 |

---

## 📌 修复建议

### 缺失页面处理流程

1. **检查来源**：阅读引用此链接的所有源页面，理解上下文
2. **如是真实概念**：新建 stub 页面
   ```yaml
   ---
   type: concept  # 或 entity
   title: "页面名"
   status: stub
   created: 2026-07-14
   updated: 2026-07-14
   tags: [待完善]
   ---
   ```
3. **如是错误引用**：将 `[[target]]` 改为已存在的 `[[existing]]`

### 路径/格式错误批量修正

建议使用 sed 批量替换：
```bash
# 示例：修正 wiki/concepts/ 路径
grep -rl 'wiki/concepts/' wiki/ | xargs sed -i '' 's|\[\[wiki/concepts/\([^]]*\)\]\]|[[\1]]|g'
```
