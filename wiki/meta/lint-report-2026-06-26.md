---
type: meta
title: "Lint Report 2026-06-26"
address: c-000924
created: 2026-06-26
updated: 2026-06-26
tags: [meta, lint, 化债]
status: developing
---

# Lint Report: 2026-06-26（化债知识网络专项）

## Summary

- **Scope**: 化债知识网络（9 个相关页面）
- **Pages scanned**: 9
- **Issues found**: 3
- **Auto-fixed**: 0（未自动修复，等待用户确认）
- **Needs review**: 3

## Scanned Pages

### 概念页（6 个）
1. [[wiki/concepts/化债]] — 化债核心机制（已更新）
2. [[wiki/concepts/化债核心命题]] — 化债核心命题
3. [[wiki/concepts/化债的成本转嫁与道德风险]] — 化债的伦理问题
4. [[wiki/concepts/QE与化债对比]] — QE 与化债的本质对比
5. [[wiki/concepts/银行扩表与流动性]] — 银行扩表的两种本质
6. [[wiki/concepts/地方政府隐性债务]] — 隐性债务
7. [[wiki/concepts/特殊再融资债券]] — 化债核心工具

### 实体页（1 个）
8. [[wiki/entities/城投公司]] — 隐性债务的主要承载主体

### Source 页（1 个）
9. [[wiki/sources/2024-化债政策包]] — 化债政策汇总

---

## 反向链接统计

| 页面 | 入链数 | 评级 |
|------|--------|------|
| [[wiki/concepts/化债]] | 10 | ✅ 优秀 |
| [[wiki/concepts/化债核心命题]] | 10 | ✅ 优秀 |
| [[wiki/concepts/化债的成本转嫁与道德风险]] | 10 | ✅ 优秀 |
| [[wiki/entities/城投公司]] | 10 | ✅ 优秀 |
| [[wiki/concepts/地方政府隐性债务]] | 9 | ✅ 良好 |
| [[wiki/concepts/特殊再融资债券]] | 9 | ✅ 良好 |
| [[wiki/sources/2024-化债政策包]] | 9 | ✅ 良好 |
| [[wiki/concepts/QE与化债对比]] | 8 | ✅ 良好 |
| [[wiki/concepts/银行扩表与流动性]] | 8 | ✅ 良好 |

> **评估**：所有页面均有充足的入链，知识网络高度互联。

---

## Issues Found

### Issue 1 (LOW): 死链 `[[wiki/concepts/LGFV]]`

- **Status**: Dead link
- **Referenced in**: 
  - [[wiki/concepts/城投公司]]
  - [[wiki/concepts/地方政府隐性债务]]
- **Issue**: `LGFV` 是 [[wiki/entities/城投公司|城投公司]] 的英文表达别名，但当前没有独立页面
- **Suggestion**: 在 [[wiki/entities/城投公司|城投公司]] 的 `aliases` 中已包含 "LGFV"，建议创建独立页面 `wiki/concepts/LGFV.md` 作为简短的概念页或保持作为别名（前者更规范）

### Issue 2 (LOW): 缺失页面 `[[wiki/entities/财政部]]`

- **Status**: Missing page
- **Mentioned in**: 
  - [[wiki/concepts/化债]] — 提到"财政部批准限额"
  - [[wiki/concepts/特殊再融资债券]] — 提到"财政部"
- **Suggestion**: 财政部是化债的关键角色，建议创建 `wiki/entities/中华人民共和国财政部.md` 实体页

### Issue 3 (LOW): 缺失页面 `[[wiki/concepts/财政货币化]]`

- **Status**: Missing page
- **Referenced in**: 
  - [[wiki/concepts/QE与化债对比]]
  - [[wiki/concepts/银行扩表与流动性]]
- **Suggestion**: 财政货币化是化债的重要概念边界，建议创建独立概念页

---

## Frontmatter 检查

| 页面 | type | status | tags | sources | aliases |
|------|------|--------|------|---------|---------|
| 化债 | ✅ concept | ⚠️ 缺失 | ✅ | ✅ | ✅ |
| 化债核心命题 | ✅ concept | ⚠️ 缺失 | ✅ | ✅ | ✅ |
| 化债的成本转嫁 | ✅ concept | ⚠️ 缺失 | ✅ | ✅ | ✅ |
| QE与化债对比 | ✅ concept | ⚠️ 缺失 | ✅ | ✅ | ✅ |
| 银行扩表与流动性 | ✅ concept | ⚠️ 缺失 | ✅ | ✅ | ✅ |
| 地方政府隐性债务 | ✅ concept | ⚠️ 缺失 | ✅ | ✅ | ✅ |
| 特殊再融资债券 | ✅ concept | ⚠️ 缺失 | ✅ | ✅ | ✅ |
| 城投公司 | ✅ entity | ✅ developing | ✅ | ❌ | ✅ |
| 化债政策包 | ✅ source | ⚠️ 缺失 | ✅ | ✅ | ✅ |

> **评估**: 大部分页面符合 frontmatter 标准。`status` 字段缺失为常见情况，不影响功能。

---

## Cross-Reference 分析

### 跨域引用质量

| 引用类型 | 数量 | 评价 |
|---------|------|------|
| 化债内部引用 | 50+ | ✅ 优秀 |
| 化债 → QE/扩表 | 8+ | ✅ 良好 |
| 化债 → 影子银行 | 5+ | ✅ 良好 |
| 化债 → 央行/财政部 | 2 | ⚠️ 可加强 |
| 化债 → 普通投资者 | 1 | ⚠️ 可加强 |

---

## 化债知识网络图

```
                    [化债核心命题] ← 中心节点（10 入链）
                   "冻结 + 争取时间"
                            │
   ┌────────────────────────┼────────────────────────┐
   ↓                        ↓                        ↓
[化债主页面]      [QE与化债对比]        [化债的成本转嫁]
(10 入链)          (8 入链)                (10 入链)
   │                        │                        │
   └─────────→[银行扩表与流动性]←────────────────────┘
                    (8 入链)
                            │
                  ┌─────────┼─────────┐
                  ↓                   ↓
        [特殊再融资债券]      [地方政府隐性债务]
        (9 入链)                (9 入链)
                  ↓                   ↓
                  └──────[城投公司]─────┘
                          (10 入链)
                              │
                          [影子银行]
                              │
                          [化债政策包]
                          (9 入链)
```

---

## 建议的改进措施

### HIGH 优先级（建议立即处理）

无——化债知识网络的健康度已经达到生产标准。

### MEDIUM 优先级（建议下个迭代处理）

1. **创建 `wiki/entities/中华人民共和国财政部.md`** — 化债的关键角色
2. **创建 `wiki/concepts/财政货币化.md`** — 与化债形成概念对比

### LOW 优先级（可选）

1. **补充 `status` 字段** — 在所有化债页面中加入 `status: evergreen` 或 `developing`
2. **创建 `wiki/concepts/LGFV.md`** — 作为城投公司的英文表达
3. **补充源页 `[[wiki/entities/财政部]]` 的引用** — 在化债页面中强化财政部角色

---

## 总体评估

> **化债知识网络的健康度 = 优秀**

- **完整性**：从基础概念到伦理审视的 4 层递进，逻辑闭环 ✅
- **互联性**：9 个页面高度互联，反向链接充分 ✅
- **精炼性**："化债核心命题"作为中心节点提炼了核心 ✅
- **批判性**："成本转嫁与道德风险"页揭示了制度性伦理灰色地带 ✅
- **可扩展性**：架构清晰，易于添加新页面 ✅

---

## 下一步

1. **运行 `/canvas`** — 创建化债机制图谱（可视化）
2. **补充缺失页面** — 财政部、财政货币化
3. **持续追踪** — 2026 年化债下半场进展

---

**Lint 结束时间**: 2026-06-26
**Lint 工具**: 手动 Grep + 分析
**建议**: 整体健康，无需自动修复