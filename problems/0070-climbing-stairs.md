---
rank: 52
id: "70"
title: 爬楼梯
difficulty: 简单
tags: [动态规划]
freq: 135
link: https://leetcode.cn/problems/climbing-stairs/
desc: 每次可以爬 1 或 2 个台阶，求爬到第 n 阶有多少种不同的方法。
---
## 思路

- 到第 `n` 阶的最后一步要么从 `n - 1` 上来，要么从 `n - 2` 上来：`f(n) = f(n-1) + f(n-2)`，就是斐波那契。
- 边界：`f(1) = 1`，`f(2) = 2`。
- 只依赖前两项，用两个变量滚动即可；记忆化递归是同一个式子的自顶向下写法。

## 易错点

- `f(2) = 2`（1+1 或直接 2），和标准斐波那契的起点不同。
- 不加记忆化的暴力递归是指数级。

## 代码

### 写法一：滚动变量

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1                          # f(0), f(1)
        for _ in range(n - 1):
            a, b = b, a + b
        return b
```

```java
class Solution {
    public int climbStairs(int n) {
        int a = 1, b = 1;                    // f(0), f(1)
        for (int i = 2; i <= n; i++) {
            int c = a + b;
            a = b;
            b = c;
        }
        return b;
    }
}
```

### 写法二：记忆化递归

```python
class Solution:
    @cache
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)
```

```java
class Solution {
    private int[] memo;

    public int climbStairs(int n) {
        memo = new int[n + 1];
        return climb(n);
    }

    private int climb(int n) {
        if (n <= 2) return n;
        if (memo[n] != 0) return memo[n];
        return memo[n] = climb(n - 1) + climb(n - 2);
    }
}
```

**复杂度**：时间 O(n)；空间滚动变量 O(1)，记忆化 O(n)。
