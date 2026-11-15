---
rank: 88
id: "62"
title: 不同路径
difficulty: 中等
tags: [动态规划]
freq: 78
link: https://leetcode.cn/problems/unique-paths/
desc: m×n 的网格，从左上角走到右下角，每次只能向右或向下，问有多少条不同的路径。
---
## 思路

- `dp(x, y)`：从 `(0, 0)` 走到 `(x, y)` 的路径数。只能从上边或左边过来：`dp(x, y) = dp(x-1, y) + dp(x, y-1)`。
- 边界：第一行、第一列都只有一条路，返回 1。
- 自顶向下加备忘录，或者自底向上填表；每个格子只依赖上边和左边，可以压成一维数组。

## 易错点

- 目标是 `dp(m - 1, n - 1)`，下标从 0 开始。
- 备忘录用 0 表示「没算过」是可以的，因为路径数不可能是 0。
- 一维写法里 `dp[j] += dp[j - 1]`：加号左边的旧 `dp[j]` 是上边的值，`dp[j - 1]` 是左边的值。

## 代码

### 写法一：记忆化递归

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def dp(x, y):                        # 走到 (x, y) 的路径数
            if x == 0 or y == 0:
                return 1
            return dp(x - 1, y) + dp(x, y - 1)

        return dp(m - 1, n - 1)
```

```java
class Solution {
    private int[][] memo;

    public int uniquePaths(int m, int n) {
        memo = new int[m][n];
        return dp(m - 1, n - 1);
    }

    // 走到 (x, y) 的路径数
    private int dp(int x, int y) {
        if (x == 0 || y == 0) return 1;
        if (memo[x][y] != 0) return memo[x][y];
        return memo[x][y] = dp(x - 1, y) + dp(x, y - 1);
    }
}
```

### 写法二：一维 DP

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n                         # 第一行全是 1
        for _ in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]           # 上边（旧 dp[j]）+ 左边
        return dp[-1]
```

```java
class Solution {
    public int uniquePaths(int m, int n) {
        int[] dp = new int[n];
        Arrays.fill(dp, 1);                  // 第一行全是 1
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                dp[j] += dp[j - 1];          // 上边（旧 dp[j]）+ 左边
            }
        }
        return dp[n - 1];
    }
}
```

**复杂度**：时间 O(mn)；空间记忆化 O(mn)，一维 DP O(n)。
