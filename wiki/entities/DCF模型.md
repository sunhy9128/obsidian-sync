---
title: DCF模型
created: 2026-04-29
updated: 2026-05-21
type: entity
status: developing
sources: "[]"
aliases:
  - "DCF"
  - "Discounted Cash Flow Model"
  - "Discounted Cash Flow"
  - "DCF Valuation"
  - "DCF Analysis"
  - "折现现金流模型"
  - "现金流折现模型"
  - "Free Cash Flow DCF"
tags:
  - entity
---

# DCF模型

> 折现现金流估值方法

## 核心定义

DCF模型（Discounted Cash Flow Model，折现现金流模型）是一种基于未来现金流折现的公司估值方法，通过预测企业未来的自由现金流并将其折现到当前时点来确定企业价值。

## 计算公式

$$企业价值 = \sum_{t=1}^{n} \frac{FCF_t}{(1+r)^t}$$

其中：
- $FCF_t$ = 第t年的自由现金流
- $r$ = 折现率（通常为加权平均资本成本WACC）
- $n$ = 预测期

## 估值步骤

1. 预测未来N年的自由现金流（FCF）
2. 确定终值（Terminal Value）
3. 确定折现率（WACC）
4. 将未来现金流折现到现值
5. 加总得到企业价值

## 优缺点

### 优点
- 理论基础扎实
- 适用于多种企业
- 考虑时间价值

### 缺点
- 依赖大量假设
- 对折现率敏感
- 预测期选择影响结果

## 相关概念

- [[折现率]]
- [[久期]]
- [[成长股vs价值股]]