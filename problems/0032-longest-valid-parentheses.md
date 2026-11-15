---
rank: 44
id: "32"
title: 最长有效括号
difficulty: 困难
tags: [栈, 动态规划, 字符串]
freq: 151
link: https://leetcode.cn/problems/longest-valid-parentheses/
desc: 求只含 '(' 和 ')' 的字符串中，最长有效括号子串的长度。
---
## 思路

- **栈 + DP**：栈里放还没匹配的左括号**下标**；`dp[i]` 表示以 `s[i-1]` 结尾的最长有效括号长度（多开一位）。
  - 遇到 `)` 且栈非空：弹出与它匹配的左括号下标 `leftIndex`，这一段长 `i - leftIndex + 1`；
  - 再加上紧挨在 `leftIndex` 前面的有效长度 `dp[leftIndex]`，就把 `"()" + "()"` 这样的相邻段拼起来了：`dp[i + 1] = i - leftIndex + 1 + dp[leftIndex]`。
- **双向计数，O(1) 空间**：`left`、`right` 数左右括号。
  - 从左往右扫：`left == right` 时更新答案 `2 * right`；`right > left` 说明右括号多了，这段作废，两个都清零。
  - 只扫一遍会漏掉左括号一直偏多的情况（如 `"(()"`），所以再从右往左扫一遍，条件对称（`left > right` 时清零）。

## 易错点

- 栈存下标不存字符，要靠下标算长度。
- `dp` 多开一位：`dp[leftIndex]` 正好是 `leftIndex` 前一个字符结尾的长度，不用处理 `leftIndex - 1` 越界。
- 有效子串一定以 `)` 结尾，只有遇到 `)` 才计算；栈空说明这个 `)` 配不上，跳过。
- 双向计数只能求长度，还原不了具体子串。

## 代码

### 写法一：栈 + DP

```python
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stk = []                             # 未匹配的左括号下标
        dp = [0] * (len(s) + 1)              # dp[i]：以 s[i-1] 结尾的最长有效长度
        for i, c in enumerate(s):
            if c == "(":
                stk.append(i)
            elif stk:
                left_index = stk.pop()
                dp[i + 1] = i - left_index + 1 + dp[left_index]   # 本段 + 前面紧挨着的一段
        return max(dp)
```

```java
class Solution {
    public int longestValidParentheses(String s) {
        Deque<Integer> stk = new ArrayDeque<>();     // 未匹配的左括号下标
        int[] dp = new int[s.length() + 1];          // dp[i]：以 s[i-1] 结尾的最长有效长度
        int res = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                stk.push(i);
            } else if (!stk.isEmpty()) {
                int leftIndex = stk.pop();
                dp[i + 1] = i - leftIndex + 1 + dp[leftIndex];   // 本段 + 前面紧挨着的一段
                res = Math.max(res, dp[i + 1]);
            }
        }
        return res;
    }
}
```

### 写法二：双向计数

```python
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res = 0
        left = right = 0
        for c in s:                          # 从左往右：右括号多了就作废
            if c == "(":
                left += 1
            else:
                right += 1
            if left == right:
                res = max(res, 2 * right)
            elif right > left:
                left = right = 0
        left = right = 0
        for c in reversed(s):                # 从右往左：左括号多了就作废
            if c == "(":
                left += 1
            else:
                right += 1
            if left == right:
                res = max(res, 2 * left)
            elif left > right:
                left = right = 0
        return res
```

```java
class Solution {
    public int longestValidParentheses(String s) {
        int res = 0, left = 0, right = 0;
        for (int i = 0; i < s.length(); i++) {           // 从左往右：右括号多了就作废
            if (s.charAt(i) == '(') left++;
            else right++;
            if (left == right) res = Math.max(res, 2 * right);
            else if (right > left) left = right = 0;
        }
        left = right = 0;
        for (int i = s.length() - 1; i >= 0; i--) {      // 从右往左：左括号多了就作废
            if (s.charAt(i) == '(') left++;
            else right++;
            if (left == right) res = Math.max(res, 2 * left);
            else if (left > right) left = right = 0;
        }
        return res;
    }
}
```

**复杂度**：时间都是 O(n)；空间栈 + DP 为 O(n)，双向计数 O(1)。
