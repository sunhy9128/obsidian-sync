# Wiki Lint 报告

**扫描时间**: 2026-07-21 11:34  
**扫描范围**: 969 个文件

---

## 📊 整体状态

| 指标 | 数值 | 严重程度 |
|------|------|----------|
| 总文件数 | 969 | - |
| 孤立页面（孤儿） | 109 | 🟡 中 |
| 断链目标 | 478 | 🔴 高 |
| 断链引用次数 | 2855 | 🔴 高 |
| 元数据缺失 | 606 | 🟡 中 |
| 地址错误 | 14 | 🟡 中 |
| **总问题数** | **1207** | - |

---

## 🔴 高优先级：Top 15 断链目标

| 排名 | 目标页面 | 引用次数 | 建议操作 |
|------|----------|---------|---------|
| 1 | `wiki/concepts/扩表与缩表` | 75 | 已存在？检查路径 |
| 2 | `wiki/concepts/化债` | 72 | 已存在？检查路径 |
| 3 | `wiki/entities/ECB` | 46 | 检查实体页面 |
| 4 | `wiki/entities/IMF` | 43 | 检查实体页面 |
| 5 | `wiki/concepts/1998香港金融保卫战` | 41 | 检查路径 |
| 6 | `wiki/concepts/2008全球金融危机` | 40 | 检查路径 |
| 7 | `wiki/entities/美联储` | 40 | 检查实体页面 |
| 8 | `wiki/concepts/量化宽松` | 39 | 检查路径 |
| 9 | `wiki/concepts/2013年钱荒` | 38 | 检查路径 |
| 10 | `wiki/concepts/欧元区主权债务危机` | 35 | 检查路径 |
| 11 | `wiki/concepts/财政货币化` | 35 | 检查路径 |
| 12 | `wiki/entities/中国央行` | 35 | 检查实体页面 |
| 13 | `wiki/concepts/化债核心命题` | 30 | 检查路径 |
| 14 | `wiki/sources/2024-化债政策包` | 29 | 检查来源页面 |
| 15 | `wiki/concepts/2020年3月流动性危机` | 28 | 检查路径 |

---

## 🟡 中优先级：孤立页面（孤儿页面）

共 **109 个页面**未被任何其他页面引用。建议检查是否需要建立链接或删除。

**部分列表**:
- `wiki/comparisons/中俄联合声明2021vs2026.md`
- `wiki/comparisons/港股vs美股vsA股.md`
- `wiki/comparisons/美联储vs中国央行.md`
- `wiki/concepts/DR007.md`
- `wiki/concepts/HBM.md`
- `wiki/concepts/LGFV.md`
- `wiki/concepts/Rentenmark改革.md`
- `wiki/concepts/SHIBOR.md`
- `wiki/concepts/TGA机制.md`
- `wiki/concepts/主权财富基金.md`
- `wiki/concepts/借股票池.md`
- `wiki/concepts/动态对冲.md`
- `wiki/concepts/卖空机制.md`
- `wiki/concepts/国产替代.md`
- `wiki/concepts/国债缓冲机制.md`

---

## 🟡 中优先级：元数据缺失

共 **606 个页面**缺少 `tags` 字段。建议批量补充。

**部分列表**:
- `wiki/analysis/基金年中排名对A股影响机制.md`
- `wiki/analysis/基金行业2025H1排名分析.md`
- `wiki/comparisons/Wiki vs RAG.md`
- `wiki/concepts/1998香港金融保卫战.md`
- `wiki/concepts/2013年钱荒.md`
- `wiki/concepts/301调查.md`
- `wiki/concepts/A股市场结构.md`
- `wiki/concepts/CAPM资本资产定价模型.md`
- `wiki/concepts/CPI与通胀.md`

---

## 🟠 地址冲突（需手动处理）

| 文件1 | 文件2 | 地址 |
|-------|-------|------|
| `wiki/concepts/_1.md` | `wiki/meta/lint-report-2026-07-17.md` | c-000952 |
| `wiki/concepts/主权财富基金.md` | `wiki/meta/2026-04-14-claude-seo-v190-session.md` | c-000911 |
| `wiki/concepts/特里芬难题.md` | `wiki/entities/特里芬难题.md` | c-000718 |
| `wiki/concepts/美元周期.md` | `wiki/index.md` | c-000908 |
| `wiki/concepts/美元潮汐.md` | `wiki/hot.md` | c-000907 |
| `wiki/concepts/美元潮汐历史案例.md` | `wiki/entities/淡马锡.md` | c-000910 |
| `wiki/concepts/脆弱五国（Fragile Five）.md` | `wiki/log.md` | c-000909 |
| `wiki/entities/GIC.md` | `wiki/meta/2026-04-14-community-cta-rollout.md` | c-000912 |
| `wiki/entities/中投.md` | `wiki/meta/2026-04-15-release-report-session.md` | c-000913 |
| `wiki/entities/挪威主权基金.md` | `wiki/meta/2026-04-15-slides-and-release-session.md` | c-000914 |

**计数器漂移**（建议重置）:
- c-001003, c-001001, c-001002, c-001004

---

## 📝 建议修复步骤

1. **紧急**: 解决地址冲突（手动修改其中一个文件的 `address` 字段）
2. **高优**: 修复 `wiki/concepts/化债` 和 `wiki/concepts/扩表与缩表` 的断链
3. **中优**: 为孤立页面建立适当的内部链接
4. **低优**: 批量补充元数据缺失页面的 tags

---

*报告生成时间: 2026-07-21 11:34*
