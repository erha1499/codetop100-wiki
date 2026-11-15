---
rank: 8
id: "5"
title: 最长回文子串
difficulty: 中等
tags: [字符串, 双指针]
freq: 366
link: https://leetcode.cn/problems/longest-palindromic-substring/
desc: 返回字符串中最长的回文子串。
---
## 思路

- **中心扩散**：回文一定有中心，枚举每个中心向两边扩。
- 两种中心都要试：奇数长度 `(i, i)`，偶数长度 `(i, i+1)`。
- 扩散函数只返回区间不返回字符串，最后统一截取一次。

## 易错点

- 循环退出时 `l`、`r` 已经越界或不相等，真正的回文是左闭右开 `[l+1, r)`，长度 `r - l - 1`。
- Java `substring(start, end)` 本身就是左闭右开，不用 `+1`。

## 代码

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def find(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return l + 1, r                  # 回文区间 [l+1, r)

        start = end = 0
        for i in range(len(s)):
            for l, r in (find(i, i), find(i, i + 1)):
                if r - l > end - start:
                    start, end = l, r
        return s[start:end]
```

```java
class Solution {
    public String longestPalindrome(String s) {
        int start = 0, end = 0;
        for (int i = 0; i < s.length(); i++) {
            int[] odd = find(s, i, i), even = find(s, i, i + 1);
            if (odd[1] - odd[0] > end - start) { start = odd[0]; end = odd[1]; }
            if (even[1] - even[0] > end - start) { start = even[0]; end = even[1]; }
        }
        return s.substring(start, end);
    }

    private int[] find(String s, int l, int r) {
        while (l >= 0 && r < s.length() && s.charAt(l) == s.charAt(r)) {
            l--;
            r++;
        }
        return new int[]{l + 1, r};          // 回文区间 [l+1, r)
    }
}
```

**复杂度**：时间 O(n²)，空间 O(1)。
