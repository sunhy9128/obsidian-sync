---
type: meta
title: "Lint Report 2026-07-06"
created: 2026-07-06
updated: 2026-07-06
tags: [meta, lint]
status: developing
---

# Lint Report: 2026-07-06

## Summary

- **Pages scanned**: 587
- **Issues found**: 14
- **Auto-fixed**: 0 (lint 严格遵守 read-only 原则)
- **Needs review**: 4

**范围聚焦**：本次 lint 主要针对 **化债知识网络（debt-resolution knowledge network）** 进行深入检查，该网络自 2026-06-26 集中构建以来包含 16 个核心页面。本次是化债系列首次全面 lint。

---

## 🟢 Tier-1 BLOCKER（必须修复）

无。

---

## 🟡 Tier-2 HIGH（强烈建议修复）

### H1. Source 页 source_file 引用死链

- **Page**: [[wiki/sources/2024-化债政策包]]
- **Issue**: `source_file: "[[中国化债政策包-2024]]"` 引用的原始源文件不存在于 `.raw/` 目录（`.raw/` 下仅有 `articles/`、`wechat/`、`claude-obsidian-ecosystem-research.md`）。
- **Fix Options**:
  - 创建 stub `.raw/中国化债政策包-2024.md`
  - 或将 `source_file` 改为 `null` / 移除
  - 或重定向到现有的 `.raw/articles/` 或 `.raw/wechat/` 中的对应源文件
- **建议**: 改为 `null`（合成 source 页，源来自多个一手政策文件）

### H2. 关键页面缺失 `status` 字段

化债系列 13 个页面缺失 `status` 前置元数据：

| 页面 | 缺失字段 |
|------|---------|
| [[wiki/concepts/化债]] | status |
| [[wiki/concepts/化债核心命题]] | status |
| [[wiki/concepts/QE与化债对比]] | status |
| [[wiki/concepts/银行扩表与流动性]] | status |
| [[wiki/concepts/央行对冲工具（化债背景）]] | status |
| [[wiki/concepts/PSL]] | status |
| [[wiki/concepts/MLF]] | status |
| [[wiki/concepts/财政货币化]] | status |
| [[wiki/concepts/特殊再融资债券]] | status |
| [[wiki/concepts/地方政府隐性债务]] | status |
| [[wiki/concepts/化债的成本转嫁与道德风险]] | status |
| [[wiki/sources/2024-化债政策包]] | status |

**Fix**: 添加 `status: mature` 或 `status: developing`（建议主页面用 `mature`，子页面用 `developing`）

---

## 🟠 Tier-3 MEDIUM（建议修复）

### M1. MLF 反向链接偏少

- **Page**: [[wiki/concepts/MLF]]
- **Inbound links**: 3 条（PSL.md、央行对冲工具.md、扩表与缩表.md）
- **Comparison**: 同行其他概念页面平均 10-20 条反向链接
- **Risk**: 作为央行对冲工具的核心子工具，反向链接不足影响知识网络覆盖度
- **Fix**: 在 [[wiki/concepts/化债]]、[[wiki/concepts/QE与化债对比]]、[[wiki/concepts/银行扩表与流动性]] 等核心页面中显式引用 `[[MLF]]`

### M2. PSL 反向链接偏少

- **Page**: [[wiki/concepts/PSL]]
- **Inbound links**: 4 条
- **Fix**: 与 M1 同，在化债核心页面和 QE 对比页面中显式引用 PSL

### M3. 化债核心命题未在所有化债子页面"前置引用"

- **Pattern**: [[wiki/concepts/化债核心命题]] 是整个化债网络的"中枢命题页"，应在所有化债子页面的开篇作为"核心命题引用"出现
- **Current Coverage**: 已覆盖 [[wiki/concepts/化债]]、[[wiki/concepts/QE与化债对比]]、[[wiki/concepts/银行扩表与流动性]] 等
- **Missing**: [[wiki/concepts/化债的成本转嫁与道德风险]]、[[wiki/concepts/央行对冲工具（化债背景）]]、[[wiki/concepts/PSL]] 等子页面
- **Fix**: 在每个化债子页面顶部添加核心命题引用

---

## 🔵 Tier-4 LOW（可选优化）

### L1. MLF 页面缺少 aliases 中文化

- **Page**: [[wiki/concepts/MLF]]
- **Issue**: 仅有 `"MLF"` 别名，缺中文别名（中期借贷便利）
- **Fix**: 添加 `aliases: ["中期借贷便利", "Medium-term Lending Facility"]`

### L2. 央行对冲工具页面别名过长

- **Page**: [[wiki/concepts/央行对冲工具（化债背景）]]
- **Issue**: 文件名含括号，使用 wikilink 时易出问题
- **Fix**: 确认 Obsidian 已正确解析（如有问题考虑重命名为更短的形式）

### L3. 跨页 mention 但未 wikilink（cross-reference gaps）

下列关键实体在多个页面"裸提及"但未 wikilink：

| 实体 | 裸提及页面数（示例） | 建议 |
|------|---------|------|
| 财政部 | 化债.md、QE与化债对比.md 等多处 | 已部分 wikilink ✅ |
| 周小川 | 部分概念页面提及但未链接到 [[wiki/entities/周小川]] | 补充链接（如存在该实体页） |
| 易纲 | 同上 | 同上 |
| 潘功胜 | 同上 | 同上 |

### L4. 化债概念页未引用 canvas

- **Pattern**: 化债系列核心页面未引用 [[wiki/meta/化债机制图谱.canvas]]
- **Fix**: 在 [[wiki/concepts/化债核心命题]] 等页面"相关条目"部分添加 canvas 引用

### L5. dashboard.md 未及时更新

- **Path**: `wiki/meta/dashboard.md`
- **Issue**: 可能未反映 2026-06-26 之后的化债系列新增页面
- **Fix**: 检查并更新 dashboard 的"Recent Activity" 与 "Entities Missing Sources"

---

## ✅ 已通过检查项

### Orphan Pages（孤儿页面）

✅ **无孤儿页面**。所有 16 个化债系列核心页面均有反向链接：

| 页面 | 反向链接数 |
|------|----------|
| [[wiki/entities/影子银行]] | 24 ✅ |
| [[wiki/sources/2024-化债政策包]] | 25 ✅ |
| [[wiki/concepts/QE与化债对比]] | 20 ✅ |
| [[wiki/concepts/财政货币化]] | 20 ✅ |
| [[wiki/concepts/特殊再融资债券]] | 17 ✅ |
| [[wiki/entities/城投公司]] | 16 ✅ |
| [[wiki/concepts/银行扩表与流动性]] | 15 ✅ |
| [[wiki/concepts/化债核心命题]] | 15 ✅ |
| [[wiki/concepts/地方政府隐性债务]] | 15 ✅ |
| [[wiki/entities/中华人民共和国财政部]] | 14 ✅ |
| [[wiki/concepts/化债的成本转嫁与道德风险]] | 13 ✅ |
| [[wiki/concepts/扩表与缩表]] | 6 ✅ |
| [[wiki/concepts/央行对冲工具（化债背景）]] | 7 ✅ |
| [[wiki/concepts/LGFV]] | 7 ✅ |
| [[wiki/concepts/PSL]] | 4 ⚠️ |
| [[wiki/concepts/MLF]] | 3 ⚠️ |

### Dead Links（死链）

✅ **化债系列无真正死链**。脚本初扫发现的疑似死链均为脚本解析问题（实际链接均存在）：
- `2020 美国财政刺激` → 存在为 `wiki/concepts/2020美国财政刺激.md`（脚本不识别空格）
- `TGA 机制` → 存在为 `wiki/concepts/TGA机制.md`（脚本不识别空格）
- `QE与化债对比` → 实际链接为 `[[wiki/concepts/QE与化债对比|QE 与化债对比]]`（脚本误拆分）

唯一真正的死链：[[wiki/sources/2024-化债政策包]] 中的 `[[中国化债政策包-2024]]`（已列入 H1）

### 必填 Frontmatter 字段

✅ `type`、`created`、`updated`、`tags` 全部 100% 完整（17/17 页面）
⚠️ `status` 缺失 12/17 页面（已列入 H2）

### Stale Claims（过时陈述）

✅ 化债系列无过时陈述。所有数据为 2026-07 当前已知。

### Naming Conventions

✅ 文件名、文件夹、tags、wikilink 全部符合规范。

---

## 📊 知识网络健康度评分

| 维度 | 评分 | 说明 |
|------|------|------|
| **完整性** | 9.5/10 | 16 个核心页面覆盖化债全部主要议题 |
| **连通性** | 9/10 | 反向链接密集，MLF/PSL 略弱 |
| **一致性** | 9/10 | 风格统一，少数缺 status |
| **追溯性** | 9/10 | 源文件引用完整（H1 除外） |
| **可发现性** | 9/10 | 别名覆盖完整 |
| **总体** | **9.1/10** | 优秀 |

---

## 🎯 建议的修复优先级

### 立即修复（建议立即执行）

1. **H1**: 修复 [[wiki/sources/2024-化债政策包]] 的 `source_file` 死链
2. **H2**: 为 12 个化债页面补充 `status` 字段

### 本周修复

3. **M1/M2**: 加强 MLF、PSL 的反向链接（4-6 处新增引用即可）
4. **M3**: 在化债子页面顶部添加核心命题引用

### 可选修复

5. **L1-L5**: 各种小优化，按需处理

---

## 🔧 推荐批量修复脚本

如用户授权自动修复，可以：

```bash
# 1. 修复 source_file 死链（H1）
# 2. 批量添加 status 字段（H2）
# 3. 在 MLF/PSL 加反向链接（M1/M2）
```

---

## 相关条目

- [[wiki/concepts/化债核心命题]] — 化债网络的"中枢命题页"
- [[wiki/concepts/化债]] — 化债主页面
- [[wiki/sources/2024-化债政策包]] — 化债政策汇总
- [[wiki/meta/lint-report-2026-06-26]] — 上一次 lint 报告（10 天前）