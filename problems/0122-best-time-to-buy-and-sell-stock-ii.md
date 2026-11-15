---
rank: 73
id: "122"
title: 买卖股票的最佳时机 II
difficulty: 简单
tags: [贪心]
freq: 91
link: https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/
desc: 可以多次买卖股票（同一时间最多持有一股），求最大利润。
---
## 思路

- 目标是吃掉所有上涨段的利润。
- 一段连续上涨 `p1 → pn` 的收益 `pn - p1` 等于每天差值之和 `(p2 - p1) + (p3 - p2) + …`。
- 所以策略就是：**只要今天比昨天贵，就把这一天的差价加进答案**；否则不动。

## 易错点

- 不要去找「最低点买、最高点卖」，那是 [121](#/121) 只能交易一次的思路。
- 通用解法是状态机 DP（持有 / 不持有两个状态），带冷冻期、手续费、限制次数的变体要用它。

## 代码

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i - 1]
            if diff > 0:
                res += diff
        return res
```

```java
class Solution {
    public int maxProfit(int[] prices) {
        int res = 0;
        for (int i = 1; i < prices.length; i++) {
            int diff = prices[i] - prices[i - 1];
            if (diff > 0) res += diff;
        }
        return res;
    }
}
```

**复杂度**：时间 O(n)，空间 O(1)。
