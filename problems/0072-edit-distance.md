---
rank: 29
id: "72"
title: 编辑距离
difficulty: 困难
tags: [动态规划, 字符串]
freq: 208
link: https://leetcode.cn/problems/edit-distance/
desc: 求把 word1 变成 word2 最少需要多少次操作（插入、删除、替换一个字符）。
---
## 思路

- `dp[i][j]`：`word1` 前 `i` 个字符变成 `word2` 前 `j` 个字符的最少操作数。
- 看最后一个字符 `word1[i-1]` 和 `word2[j-1]`：
  - 相等：什么都不做，`dp[i][j] = dp[i-1][j-1]`；
  - 不等：三种操作取最小再加 1——替换 `dp[i-1][j-1]`、删除 `dp[i-1][j]`、插入 `dp[i][j-1]`。
- 初始化：`dp[i][0] = i`（全删），`dp[0][j] = j`（全插）。
- 自顶向下的想法一样：`dp(i, j)` 表示后缀 `word1[i:]` 变成 `word2[j:]` 的最少操作数，一个串走完时返回另一个串剩下的长度。

## 易错点

- `dp` 开 `(m+1) × (n+1)`，下标 `i` 表示「前 i 个」，对应字符是 `i - 1`。
- 删除 / 插入对应哪个下标：删 `word1` 的字符 → `i` 退一步；往 `word1` 插一个字符去匹配 `word2[j-1]` → `j` 退一步。
- 不能贪心：只看下一个字符是否相同不够，必须枚举三种操作。

## 代码

### 写法一：自底向上

```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j - 1],   # 替换
                                       dp[i - 1][j],       # 删除
                                       dp[i][j - 1])       # 插入
        return dp[m][n]
```

```java
class Solution {
    public int minDistance(String word1, String word2) {
        int m = word1.length(), n = word2.length();
        int[][] dp = new int[m + 1][n + 1];
        for (int i = 0; i <= m; i++) dp[i][0] = i;
        for (int j = 0; j <= n; j++) dp[0][j] = j;
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (word1.charAt(i - 1) == word2.charAt(j - 1)) {
                    dp[i][j] = dp[i - 1][j - 1];
                } else {
                    dp[i][j] = 1 + Math.min(dp[i - 1][j - 1],            // 替换
                                   Math.min(dp[i - 1][j], dp[i][j - 1])); // 删除 / 插入
                }
            }
        }
        return dp[m][n];
    }
}
```

### 写法二：自顶向下（记忆化搜索）

```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def dp(i, j):                        # word1[i:] 变成 word2[j:] 的最少操作数
            if j == len(word2):
                return len(word1) - i        # 只能删
            if i == len(word1):
                return len(word2) - j        # 只能插
            if word1[i] == word2[j]:
                return dp(i + 1, j + 1)
            return 1 + min(dp(i + 1, j),     # 删除
                           dp(i + 1, j + 1), # 替换
                           dp(i, j + 1))     # 插入

        return dp(0, 0)
```

```java
class Solution {
    private int[][] memo;

    public int minDistance(String word1, String word2) {
        memo = new int[word1.length()][word2.length()];
        for (int[] row : memo) Arrays.fill(row, -1);
        return dp(word1, 0, word2, 0);
    }

    // word1[i..] 变成 word2[j..] 的最少操作数
    private int dp(String word1, int i, String word2, int j) {
        if (j == word2.length()) return word1.length() - i;    // 只能删
        if (i == word1.length()) return word2.length() - j;    // 只能插
        if (memo[i][j] != -1) return memo[i][j];
        int res;
        if (word1.charAt(i) == word2.charAt(j)) {
            res = dp(word1, i + 1, word2, j + 1);
        } else {
            res = 1 + Math.min(dp(word1, i + 1, word2, j),               // 删除
                      Math.min(dp(word1, i + 1, word2, j + 1),           // 替换
                               dp(word1, i, word2, j + 1)));             // 插入
        }
        return memo[i][j] = res;
    }
}
```

**复杂度**：时间 O(mn)，空间 O(mn)（自底向上可用滚动数组压到 O(n)）。
