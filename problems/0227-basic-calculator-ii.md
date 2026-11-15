---
rank: 95
id: "227"
title: 基本计算器 II
difficulty: 中等
tags: [栈, 字符串]
freq: 70
link: https://leetcode.cn/problems/basic-calculator-ii/
desc: 计算只含非负整数、+ - * / 和空格的表达式的值，除法向零取整。
---
## 思路

- **双栈（通用模板）**：`nums` 放数字和中间结果，`ops` 放还没执行的运算符。
  - 数字：连续读完整个多位数，压入 `nums`；
  - 运算符：**先把栈顶优先级 ≥ 它的运算都算掉**，再把它入栈；
  - `(`：直接入 `ops` 当边界；`)`：一直算到遇到 `(`，再把 `(` 弹掉；
  - 遍历完把 `ops` 里剩下的算完。
  - 本题没有括号，保留括号处理是为了能直接复用到 224、772。
- **单栈（只针对本题）**：记住每个数**前面**的运算符 `op`。数读完时：`+` 压入 `num`，`-` 压入 `-num`，`*` `/` 把栈顶弹出来和 `num` 算完再压回去。最后把栈里的数加起来。

## 易错点

- 优先级比较用 `>=` 不是 `>`：同级运算要从左往右算（`8/4/2`）。
- `nums` 先压一个 0，处理表达式以 `-` 开头的情况；`(` 后面紧跟 `+` / `-` 时同样补 0。
- 除法向零取整：Python 的 `//` 是向下取整（`-3 // 2 == -2`），要自己处理符号或用 `int(a / b)`；Java 的 `/` 本身就向零取整。
- 单栈写法里，最后一个数后面没有运算符了，要在末尾补一个 `+` 触发最后一次结算。

## 代码

### 写法一：双栈

```python
class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        n = len(s)
        priority = {"+": 1, "-": 1, "*": 2, "/": 2}
        nums = [0]                           # 补 0，处理表达式开头的正负号
        ops = []

        def calc():
            b, a = nums.pop(), nums.pop()
            op = ops.pop()
            if op == "+":
                res = a + b
            elif op == "-":
                res = a - b
            elif op == "*":
                res = a * b
            else:
                q = abs(a) // abs(b)         # 向零取整
                res = -q if (a < 0) != (b < 0) else q
            nums.append(res)

        i = 0
        while i < n:
            c = s[i]
            if c.isdigit():
                num = 0
                while i < n and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                nums.append(num)
                continue                     # i 已经指向数字之后
            if c == "(":
                ops.append(c)
            elif c == ")":
                while ops[-1] != "(":
                    calc()
                ops.pop()
            else:
                if c in "+-" and i > 0 and s[i - 1] == "(":
                    nums.append(0)
                while ops and ops[-1] != "(" and priority[ops[-1]] >= priority[c]:
                    calc()                   # 先算掉优先级更高或相同的
                ops.append(c)
            i += 1
        while ops:
            calc()
        return nums[-1]
```

```java
class Solution {
    private final Deque<Integer> nums = new ArrayDeque<>();
    private final Deque<Character> ops = new ArrayDeque<>();

    public int calculate(String s) {
        s = s.replace(" ", "");
        int n = s.length();
        nums.push(0);                                    // 补 0，处理表达式开头的正负号
        int i = 0;
        while (i < n) {
            char c = s.charAt(i);
            if (Character.isDigit(c)) {
                int num = 0;
                while (i < n && Character.isDigit(s.charAt(i))) {
                    num = num * 10 + (s.charAt(i++) - '0');
                }
                nums.push(num);
                continue;                                // i 已经指向数字之后
            }
            if (c == '(') {
                ops.push(c);
            } else if (c == ')') {
                while (ops.peek() != '(') calc();
                ops.pop();
            } else {
                if ((c == '+' || c == '-') && i > 0 && s.charAt(i - 1) == '(') nums.push(0);
                while (!ops.isEmpty() && ops.peek() != '(' && priority(ops.peek()) >= priority(c)) {
                    calc();                              // 先算掉优先级更高或相同的
                }
                ops.push(c);
            }
            i++;
        }
        while (!ops.isEmpty()) calc();
        return nums.peek();
    }

    private int priority(char op) {
        return op == '+' || op == '-' ? 1 : 2;
    }

    private void calc() {
        int b = nums.pop(), a = nums.pop();
        char op = ops.pop();
        if (op == '+') nums.push(a + b);
        else if (op == '-') nums.push(a - b);
        else if (op == '*') nums.push(a * b);
        else nums.push(a / b);                           // Java 的 / 向零取整
    }
}
```

### 写法二：单栈

```python
class Solution:
    def calculate(self, s: str) -> int:
        stack, num, op = [], 0, "+"          # op：当前数字前面的运算符
        for c in s + "+":                    # 末尾补一个 +，触发最后一次结算
            if c.isdigit():
                num = num * 10 + int(c)
            elif c != " ":
                if op == "+":
                    stack.append(num)
                elif op == "-":
                    stack.append(-num)
                elif op == "*":
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))     # 向零取整
                op, num = c, 0
        return sum(stack)
```

```java
class Solution {
    public int calculate(String s) {
        Deque<Integer> stack = new ArrayDeque<>();
        int num = 0;
        char op = '+';                                   // 当前数字前面的运算符
        s = s + "+";                                     // 末尾补一个 +，触发最后一次结算
        for (char c : s.toCharArray()) {
            if (Character.isDigit(c)) {
                num = num * 10 + (c - '0');
            } else if (c != ' ') {
                if (op == '+') stack.push(num);
                else if (op == '-') stack.push(-num);
                else if (op == '*') stack.push(stack.pop() * num);
                else stack.push(stack.pop() / num);
                op = c;
                num = 0;
            }
        }
        int res = 0;
        for (int x : stack) res += x;
        return res;
    }
}
```

**复杂度**：时间 O(n)，空间 O(n)。
