---
rank: 61
id: "394"
title: 字符串解码
difficulty: 中等
tags: [栈, 字符串]
freq: 103
link: https://leetcode.cn/problems/decode-string/
desc: 解码形如 3[a2[c]] 的字符串：k[xxx] 表示 xxx 重复 k 次，可以嵌套。
---
## 思路

- 遇到 `[` 进入新的一层，遇到 `]` 回到上一层——用**两个栈**模拟递归：一个存「进括号之前已经拼好的字符串」，一个存「这层括号的重复次数」。
- 逐字符处理，`cur` 是当前层正在拼的字符串，`k` 是正在读的数字：
  - 数字：`k = k * 10 + 数字`；
  - `[`：把 `k` 和 `cur` 分别压栈，然后都清空，开始拼括号里的内容；
  - `]`：弹出 `prev` 和 `times`，`cur = prev + cur × times`；
  - 字母：接到 `cur` 后面。

## 易错点

- 数字可能有多位（`10[a]`），要累加，不能只读一位。
- `[` 之后必须把 `cur` 和 `k` 都重置，否则上一层的内容会混进来。
- `]` 之后记得把拼好的结果赋回 `cur`。

## 代码

```python
class Solution:
    def decodeString(self, s: str) -> str:
        str_stack, cnt_stack = [], []
        k, cur = 0, ""
        for c in s:
            if c.isdigit():
                k = k * 10 + int(c)
            elif c == "[":
                cnt_stack.append(k)
                str_stack.append(cur)
                k, cur = 0, ""
            elif c == "]":
                prev, times = str_stack.pop(), cnt_stack.pop()
                cur = prev + cur * times
            else:
                cur += c
        return cur
```

```java
class Solution {
    public String decodeString(String s) {
        Deque<String> strStack = new ArrayDeque<>();
        Deque<Integer> cntStack = new ArrayDeque<>();
        int k = 0;
        StringBuilder cur = new StringBuilder();
        for (char c : s.toCharArray()) {
            if (Character.isDigit(c)) {
                k = k * 10 + (c - '0');
            } else if (c == '[') {
                cntStack.push(k);
                strStack.push(cur.toString());
                k = 0;
                cur = new StringBuilder();
            } else if (c == ']') {
                StringBuilder sb = new StringBuilder(strStack.pop());
                int times = cntStack.pop();
                for (int i = 0; i < times; i++) sb.append(cur);
                cur = sb;
            } else {
                cur.append(c);
            }
        }
        return cur.toString();
    }
}
```

**复杂度**：时间 O(解码后的长度)，空间 O(解码后的长度)。
