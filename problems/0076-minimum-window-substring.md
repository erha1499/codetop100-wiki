---
rank: 51
id: "76"
title: 最小覆盖子串
difficulty: 困难
tags: [滑动窗口, 哈希表]
freq: 136
link: https://leetcode.cn/problems/minimum-window-substring/
desc: 在 s 中找出包含 t 全部字符（含重复）的最短子串，没有则返回空串。
---
## 思路

- 滑动窗口 + 计数，窗口左闭右开 `[left, right)`。两张表：`need` 记 `t` 里每个字符要几个，`window` 记窗口里这些字符有几个。
- `valid`：有多少**种**字符的数量已经达标。`valid == need.size()` 时窗口覆盖了 `t`。
- 右扩：字符 `c` 进窗口，若在 `need` 里则计数加一，刚好等于需要的数量时 `valid++`。
- 窗口合法时不断左缩：先更新最短答案，再把左边字符 `d` 移出——移出前数量刚好等于需要的数量，则 `valid--`。

## 易错点

- Java 里 `window.get(c)` 和 `need.get(c)` 都是 `Integer` 对象，必须用 `.equals()` 比较；`==` 比的是引用，只有 -128~127 走缓存，数量一大就错。
- 左缩时顺序：**先判断 `valid` 要不要减，再把数量减一**。
- 更新答案要在左缩之前（此时窗口还合法），长度是 `right - left`。

## 代码

```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)                    # t 中每个字符需要几个
        window = defaultdict(int)            # 窗口中这些字符有几个
        left = right = valid = 0             # valid：数量已达标的字符种数
        start, length = 0, inf
        while right < len(s):
            c = s[right]                     # 右扩
            right += 1
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            while valid == len(need):        # 窗口合法就左缩
                if right - left < length:
                    start, length = left, right - left
                d = s[left]
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return "" if length == inf else s[start:start + length]
```

```java
class Solution {
    public String minWindow(String s, String t) {
        Map<Character, Integer> need = new HashMap<>();      // t 中每个字符需要几个
        Map<Character, Integer> window = new HashMap<>();    // 窗口中这些字符有几个
        for (char c : t.toCharArray()) {
            need.put(c, need.getOrDefault(c, 0) + 1);
        }
        int left = 0, right = 0, valid = 0;                  // valid：数量已达标的字符种数
        int start = 0, len = Integer.MAX_VALUE;
        while (right < s.length()) {
            char c = s.charAt(right++);                      // 右扩
            if (need.containsKey(c)) {
                window.put(c, window.getOrDefault(c, 0) + 1);
                if (window.get(c).equals(need.get(c))) valid++;
            }
            while (valid == need.size()) {                   // 窗口合法就左缩
                if (right - left < len) {
                    start = left;
                    len = right - left;
                }
                char d = s.charAt(left++);
                if (need.containsKey(d)) {
                    if (window.get(d).equals(need.get(d))) valid--;
                    window.put(d, window.get(d) - 1);
                }
            }
        }
        return len == Integer.MAX_VALUE ? "" : s.substring(start, start + len);
    }
}
```

**复杂度**：时间 O(m + n)，空间 O(字符集)。
