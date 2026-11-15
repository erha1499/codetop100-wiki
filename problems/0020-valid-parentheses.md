---
rank: 17
id: "20"
title: 有效的括号
difficulty: 简单
tags: [栈, 字符串]
freq: 301
link: https://leetcode.cn/problems/valid-parentheses/
desc: 判断只含三种括号的字符串是否有效（类型匹配且顺序正确）。
---
## 思路

- 栈：左括号入栈；遇到右括号，看栈顶是不是与它配对的左括号，是就弹出，不是或栈空就 `false`。
- 最后栈为空才算全部匹配。

## 易错点

- 遇到右括号时要先判栈空（如 `"]"`）。
- 结尾别忘了判栈空（如 `"(("`）。

## 代码

```python
class Solution:
    def isValid(self, s: str) -> bool:
        left_of = {")": "(", "]": "[", "}": "{"}
        stack = []
        for c in s:
            if c not in left_of:             # 左括号
                stack.append(c)
            elif stack and stack[-1] == left_of[c]:
                stack.pop()
            else:
                return False
        return not stack
```

```java
class Solution {
    public boolean isValid(String s) {
        Deque<Character> stack = new ArrayDeque<>();
        for (char c : s.toCharArray()) {
            if (c == '(' || c == '[' || c == '{') {
                stack.push(c);
            } else if (!stack.isEmpty() && stack.peek() == leftOf(c)) {
                stack.pop();
            } else {
                return false;
            }
        }
        return stack.isEmpty();
    }

    private char leftOf(char c) {
        if (c == ')') return '(';
        if (c == ']') return '[';
        return '{';
    }
}
```

**复杂度**：时间 O(n)，空间 O(n)。
