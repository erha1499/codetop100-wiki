---
rank: 68
id: "64"
title: 最小路径和
difficulty: 中等
tags: [动态规划, 矩阵]
freq: 97
link: https://leetcode.cn/problems/minimum-path-sum/
desc: 从网格左上角走到右下角，每次只能向右或向下，求路径上数字之和的最小值。
---
## 思路

- `dp[i][j]`：从 `(0, 0)` 走到 `(i, j)` 的最小路径和。
- 只能从上边或左边过来：`dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])`。
- 初始化：`dp[0][0] = grid[0][0]`；第一行只能从左边来，第一列只能从上边来，各自累加。
- 自顶向下也可以：`dp(x, y)` 递归到 `(0, 0)`，加记忆化。

## 易错点

- 第一行、第一列要单独初始化，不能直接套转移公式（没有上边 / 左边）。
- 转移时别漏了加当前格子 `grid[i][j]`。

## 代码

```python
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(1, m):                # 第一列：只能从上边来
            dp[i][0] = grid[i][0] + dp[i - 1][0]
        for j in range(1, n):                # 第一行：只能从左边来
            dp[0][j] = grid[0][j] + dp[0][j - 1]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])
        return dp[m - 1][n - 1]
```

```java
class Solution {
    public int minPathSum(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        int[][] dp = new int[m][n];
        dp[0][0] = grid[0][0];
        for (int i = 1; i < m; i++) dp[i][0] = grid[i][0] + dp[i - 1][0];   // 第一列：只能从上边来
        for (int j = 1; j < n; j++) dp[0][j] = grid[0][j] + dp[0][j - 1];   // 第一行：只能从左边来
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                dp[i][j] = grid[i][j] + Math.min(dp[i - 1][j], dp[i][j - 1]);
            }
        }
        return dp[m - 1][n - 1];
    }
}
```

**复杂度**：时间 O(mn)，空间 O(mn)（可压成一维 O(n)）。
