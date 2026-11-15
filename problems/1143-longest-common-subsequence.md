---
rank: 30
id: "1143"
title: 最长公共子序列
difficulty: 中等
tags: [动态规划, 字符串]
freq: 203
link: https://leetcode.cn/problems/longest-common-subsequence/
desc: 求两个字符串的最长公共子序列的长度（子序列不要求连续）。
---
## 思路

- `dp[i][j]`：`text1` 前 `i` 个字符和 `text2` 前 `j` 个字符的 LCS 长度。
- 看最后一个字符：
  - 相等：这个字符一定可以算进 LCS，`dp[i][j] = dp[i-1][j-1] + 1`；
  - 不等：两个字符不可能同时在 LCS 里，丢掉其中一个，`dp[i][j] = max(dp[i-1][j], dp[i][j-1])`。
- 第 0 行、第 0 列是空串，天然为 0，不用初始化。
- 自顶向下的写法结构同 [72](#/72)：`dp(i, j)` 表示两个后缀的 LCS，一方走完返回 0。

## 易错点

- 不等时不用考虑 `dp[i-1][j-1]`：它不会比另外两个更大。
- 和 [718 最长重复子数组](#/718) 区分：子数组要求连续，不等时直接是 0；子序列不等时取 max。

## 代码

```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[m][n]
```

```java
class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        int m = text1.length(), n = text2.length();
        int[][] dp = new int[m + 1][n + 1];
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (text1.charAt(i - 1) == text2.charAt(j - 1)) {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                } else {
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }
        return dp[m][n];
    }
}
```

**复杂度**：时间 O(mn)，空间 O(mn)（可用滚动数组压到 O(n)）。
