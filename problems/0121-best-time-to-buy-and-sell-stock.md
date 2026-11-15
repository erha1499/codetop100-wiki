---
rank: 18
id: "121"
title: 买卖股票的最佳时机
difficulty: 简单
tags: [贪心, 动态规划]
freq: 282
link: https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/
desc: 只能买卖一次股票，求最大利润（赚不到返回 0）。
---
## 思路

- 枚举卖出日：在第 i 天卖，一定是在它之前的最低价买入最赚。
- 一次遍历维护两个量：`cost` = 到目前为止的最低价，`profit` = 到目前为止的最大利润。
- 每天先更新 `cost`，再用 `prices[i] - cost` 更新 `profit`。

## 易错点

- 必须先买后卖，所以 `cost` 只能来自当前及之前的价格。
- `profit` 初始为 0（赚不到就不交易）。

## 代码

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cost, profit = inf, 0
        for p in prices:
            cost = min(cost, p)
            profit = max(profit, p - cost)
        return profit
```

```java
class Solution {
    public int maxProfit(int[] prices) {
        int cost = Integer.MAX_VALUE, profit = 0;
        for (int p : prices) {
            cost = Math.min(cost, p);
            profit = Math.max(profit, p - cost);
        }
        return profit;
    }
}
```

**复杂度**：时间 O(n)，空间 O(1)。
