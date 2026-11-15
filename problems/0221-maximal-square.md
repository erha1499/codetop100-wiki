---
rank: 75
id: "221"
title: 最大正方形
difficulty: 中等
tags: [动态规划, 矩阵]
freq: 89
link: https://leetcode.cn/problems/maximal-square/
desc: 在由 '0' 和 '1' 组成的矩阵中，找出只含 '1' 的最大正方形，返回面积。
---
## 思路

- `dp[i+1][j+1]`：**以 `matrix[i][j]` 为右下角**的全 1 正方形的最大边长。`dp` 多开一行一列，省掉越界判断。
- `matrix[i][j] == '1'` 时，能撑多大取决于左、上、左上三个位置里最小的那个：
  `dp[i+1][j+1] = min(dp[i+1][j], dp[i][j+1], dp[i][j]) + 1`。
- 用 `res` 记最大边长，返回 `res * res`。

## 易错点

- 下标偏移：`matrix[i][j]` 对应 `dp[i+1][j+1]`。
- 矩阵里是字符 `'1'`，不是数字 1。
- 题目要的是面积，别直接返回边长。

## 代码

```python
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    dp[i + 1][j + 1] = 1 + min(dp[i + 1][j],    # 左
                                               dp[i][j + 1],    # 上
                                               dp[i][j])        # 左上
                    res = max(res, dp[i + 1][j + 1])
        return res * res
```

```java
class Solution {
    public int maximalSquare(char[][] matrix) {
        int m = matrix.length, n = matrix[0].length;
        int[][] dp = new int[m + 1][n + 1];
        int res = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == '1') {
                    dp[i + 1][j + 1] = 1 + Math.min(dp[i][j],                          // 左上
                                           Math.min(dp[i + 1][j], dp[i][j + 1]));      // 左、上
                    res = Math.max(res, dp[i + 1][j + 1]);
                }
            }
        }
        return res * res;
    }
}
```

**复杂度**：时间 O(mn)，空间 O(mn)。
