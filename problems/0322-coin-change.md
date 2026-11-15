---
rank: 50
id: "322"
title: 零钱兑换
difficulty: 中等
tags: [动态规划]
freq: 136
link: https://leetcode.cn/problems/coin-change/
desc: 用给定面额的硬币（每种无限个）凑出金额 amount，求最少硬币数，凑不出返回 -1。
---
## 思路

- 完全背包求最小个数。`dp[i]`：凑出金额 `i` 最少需要几枚硬币。
- 对每个金额 `i` 枚举最后一枚硬币 `coin`：`dp[i] = min(dp[i], dp[i - coin] + 1)`。
- `dp[0] = 0`；其余初始化成一个「不可能」的大数 `amount + 1`（最多也就 `amount` 枚 1 元硬币）。

## 易错点

- `i - coin < 0` 时这枚硬币用不上，跳过。
- 最后 `dp[amount]` 还是 `amount + 1` 说明无解，返回 -1。
- Java 别用 `Integer.MAX_VALUE` 当初始值，`+ 1` 会溢出成负数。

## 代码

```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)     # amount + 1 表示凑不出
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return -1 if dp[amount] == amount + 1 else dp[amount]
```

```java
class Solution {
    public int coinChange(int[] coins, int amount) {
        int[] dp = new int[amount + 1];
        Arrays.fill(dp, amount + 1);         // amount + 1 表示凑不出
        dp[0] = 0;
        for (int i = 1; i <= amount; i++) {
            for (int coin : coins) {
                if (i - coin < 0) continue;
                dp[i] = Math.min(dp[i], dp[i - coin] + 1);
            }
        }
        return dp[amount] == amount + 1 ? -1 : dp[amount];
    }
}
```

**复杂度**：时间 O(amount × 硬币种数)，空间 O(amount)。
