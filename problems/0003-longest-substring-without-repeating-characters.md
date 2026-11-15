---
rank: 1
id: "3"
title: 无重复字符的最长子串
difficulty: 中等
tags: [滑动窗口, 哈希表]
freq: 1228
link: https://leetcode.cn/problems/longest-substring-without-repeating-characters/
desc: 求字符串中不含重复字符的最长子串的长度。
---
## 思路

- 滑动窗口，左闭右开 `[l, r)`，`window` 记录窗口内每个字符的出现次数。
- 右边进一个字符 `c` → 只要 `window[c] > 1` 就一直收缩左边 → 窗口合法后更新答案。
- 进 `c` 之前窗口无重复，所以进来之后**只有 `c` 可能重复**，不用检查整个表。

## 易错点

- 收缩用 `while` 不是 `if`：`"abcb"` 要连续移出 `a`、`b`。
- 先收缩、再更新答案；长度是 `r - l`（`r` 已经自增过）。

## 代码

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {}                      # 字符 -> 窗口内出现次数
        l = r = res = 0
        while r < len(s):
            c = s[r]
            r += 1
            window[c] = window.get(c, 0) + 1
            while window[c] > 1:         # 只有刚进来的 c 可能重复
                window[s[l]] -= 1
                l += 1
            res = max(res, r - l)        # 左闭右开，长度 r - l
        return res
```

```java
class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> window = new HashMap<>();   // 字符 -> 窗口内出现次数
        int l = 0, r = 0, res = 0;
        while (r < s.length()) {
            char c = s.charAt(r++);
            window.merge(c, 1, Integer::sum);
            while (window.get(c) > 1) {                     // 只有刚进来的 c 可能重复
                window.merge(s.charAt(l++), -1, Integer::sum);
            }
            res = Math.max(res, r - l);                     // 左闭右开，长度 r - l
        }
        return res;
    }
}
```

**复杂度**：时间 O(n)（左右指针都只向右走），空间 O(字符集)。
