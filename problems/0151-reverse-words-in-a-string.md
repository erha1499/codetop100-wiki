---
rank: 59
id: "151"
title: 翻转字符串里的单词
difficulty: 中等
tags: [字符串, 双指针]
freq: 107
link: https://leetcode.cn/problems/reverse-words-in-a-string/
desc: 反转字符串中单词的顺序，并去掉首尾和单词之间多余的空格。
---
## 思路

- 反转的是**单词顺序**，不是字符；同时要处理首尾空格和连续空格。
- **库函数**：按空白切分 → 反转单词列表 → 用单个空格拼起来。
- **双指针**（面试官不让用 split 时）：先去掉首尾空格，`i`、`j` 从右往左扫——`i` 往左走到单词前的空格，`[i + 1, j]` 就是一个单词；取出来后 `i` 跳过中间的连续空格，`j = i` 指向下一个单词的结尾。

## 易错点

- Java 的 `trim()` 不改原字符串，要写 `s = s.trim()`。
- Java 切分用 `split("\\s+")`（一个或多个空白），而且要先 `trim()`，否则开头会多一个空串。Python 的 `split()` 不带参数就已经处理好了多余空格。
- 双指针写法里中间可能有多个空格，要用 `while` 跳过。

## 代码

### 写法一：库函数

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])
```

```java
class Solution {
    public String reverseWords(String s) {
        String[] words = s.trim().split("\\s+");
        Collections.reverse(Arrays.asList(words));
        return String.join(" ", words);
    }
}
```

### 写法二：双指针

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        res = []
        i = j = len(s) - 1
        while i >= 0:
            while i >= 0 and s[i] != " ":    # i 走到单词前的空格
                i -= 1
            res.append(s[i + 1:j + 1])
            while i >= 0 and s[i] == " ":    # 跳过单词间的空格
                i -= 1
            j = i
        return " ".join(res)
```

```java
class Solution {
    public String reverseWords(String s) {
        s = s.trim();
        StringBuilder res = new StringBuilder();
        int i = s.length() - 1, j = i;
        while (i >= 0) {
            while (i >= 0 && s.charAt(i) != ' ') i--;    // i 走到单词前的空格
            res.append(s, i + 1, j + 1).append(' ');
            while (i >= 0 && s.charAt(i) == ' ') i--;    // 跳过单词间的空格
            j = i;
        }
        return res.toString().trim();
    }
}
```

**复杂度**：时间 O(n)，空间 O(n)。
