---
rank: 92
id: "139"
title: 单词拆分
difficulty: 中等
tags: [动态规划, 字符串, 哈希表]
freq: 72
link: https://leetcode.cn/problems/word-break/
desc: 判断字符串 s 能否被拆分成若干个字典中的单词（单词可以重复使用）。
---
## 思路

- 拆分型 DP。
- **自顶向下**：`dp(i)` = 后缀 `s[i:]` 能否被拆分。从 `i` 开始枚举第一个单词的长度，如果 `s[i, i+len)` 在字典里并且 `dp(i + len)` 为真，就成立。`i` 走到末尾返回 true。
- **自底向上**：`dp[i]` = 前缀 `s[:i]` 能否被拆分。枚举最后一个单词的起点 `j`：`dp[j]` 为真且 `s[j:i]` 在字典里，则 `dp[i]` 为真。`dp[0] = true`。
- 字典先转成 `HashSet`，查询 O(1)。

## 易错点

- 不加备忘录会重复递归同一个位置，超时。
- Java 的备忘录要区分三种状态（未计算 / false / true），不能只用 boolean 数组。
- 只问「能不能」，找到一种拆法就可以返回。

## 代码

### 写法一：记忆化递归

```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)

        @cache
        def dp(i):                           # s[i:] 能否被拆分
            if i == len(s):
                return True
            for j in range(i + 1, len(s) + 1):
                if s[i:j] in word_set and dp(j):
                    return True
            return False

        return dp(0)
```

```java
class Solution {
    private int[] memo;                      // -1 未计算，0 false，1 true
    private final Set<String> wordSet = new HashSet<>();

    public boolean wordBreak(String s, List<String> wordDict) {
        memo = new int[s.length()];
        Arrays.fill(memo, -1);
        wordSet.addAll(wordDict);
        return dp(s, 0);
    }

    // s[i..] 能否被拆分
    private boolean dp(String s, int i) {
        if (i == s.length()) return true;
        if (memo[i] != -1) return memo[i] == 1;
        for (int len = 1; i + len <= s.length(); len++) {
            if (wordSet.contains(s.substring(i, i + len)) && dp(s, i + len)) {
                memo[i] = 1;
                return true;
            }
        }
        memo[i] = 0;
        return false;
    }
}
```

### 写法二：自底向上

```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)
        dp = [True] + [False] * n            # dp[i]：s[:i] 能否被拆分
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        return dp[n]
```

```java
class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        Set<String> wordSet = new HashSet<>(wordDict);
        int n = s.length();
        boolean[] dp = new boolean[n + 1];   // dp[i]：s 的前 i 个字符能否被拆分
        dp[0] = true;
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j < i; j++) {
                if (dp[j] && wordSet.contains(s.substring(j, i))) {
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[n];
    }
}
```

**复杂度**：时间 O(n²) 个状态转移（每次取子串另算 O(n)），空间 O(n)。
