---
rank: 78
id: "14"
title: 最长公共前缀
difficulty: 简单
tags: [字符串]
freq: 85
link: https://leetcode.cn/problems/longest-common-prefix/
desc: 求字符串数组中所有字符串的最长公共前缀。
---
## 思路

- **纵向扫描**（按列比较）：以 `strs[0]` 为基准，从左到右枚举下标 `i`，检查所有字符串的第 `i` 个字符。
- 只要有一个字符串长度不够，或者字符不一样，`[0, i)` 就是答案。
- 基准串扫完都没问题，答案就是基准串本身。

## 易错点

- 外层循环是字符下标、内层循环是各个字符串，别写反。
- 先判越界（`i >= s.length()`）再取字符。

## 代码

```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s0 = strs[0]
        for i, c in enumerate(s0):
            for s in strs:
                if i >= len(s) or s[i] != c:
                    return s0[:i]
        return s0
```

```java
class Solution {
    public String longestCommonPrefix(String[] strs) {
        String s0 = strs[0];
        for (int i = 0; i < s0.length(); i++) {
            char c = s0.charAt(i);
            for (String s : strs) {
                if (i >= s.length() || s.charAt(i) != c) {
                    return s0.substring(0, i);
                }
            }
        }
        return s0;
    }
}
```

**复杂度**：时间 O(字符总数)，空间 O(1)。
