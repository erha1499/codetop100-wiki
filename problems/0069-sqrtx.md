---
rank: 45
id: "69"
title: x 的平方根
difficulty: 简单
tags: [二分, 数学]
freq: 150
link: https://leetcode.cn/problems/sqrtx/
desc: 求非负整数 x 的平方根的整数部分（不能用内置开方函数）。
---
## 思路

- **二分**：答案是满足 `k * k <= x` 的最大 `k`，在 `[0, x]` 上二分。`mid * mid <= x` 时 `mid` 是候选答案，记到 `res` 里再往右找更大的；否则往左。
- **牛顿迭代**：求 `r² = x`，从 `r = x` 出发反复令 `r = (r + x / r) / 2`，直到 `r * r <= x`。全程用整数除法，不用处理浮点精度。

## 易错点

- Java 里 `mid * mid` 会溢出 `int`：写 `(long) mid * mid`。注意 `long num = mid * mid` 没用——右边先按 `int` 算完溢出了才转。
- 二分找的是「最后一个满足条件的」，用 `res` 记录候选最不容易写错。
- 牛顿迭代 `x = 0` 时会除零，要特判。

## 代码

### 写法一：二分

```python
class Solution:
    def mySqrt(self, x: int) -> int:
        left, right, res = 0, x, 0
        while left <= right:
            mid = (left + right) // 2
            if mid * mid <= x:
                res = mid                    # mid 合法，继续往右找更大的
                left = mid + 1
            else:
                right = mid - 1
        return res
```

```java
class Solution {
    public int mySqrt(int x) {
        int left = 0, right = x, res = 0;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if ((long) mid * mid <= x) {
                res = mid;                   // mid 合法，继续往右找更大的
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return res;
    }
}
```

### 写法二：牛顿迭代

```python
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        r = x
        while r * r > x:
            r = (r + x // r) // 2
        return r
```

```java
class Solution {
    public int mySqrt(int x) {
        if (x == 0) return 0;
        long r = x;
        while (r * r > x) {
            r = (r + x / r) / 2;
        }
        return (int) r;
    }
}
```

**复杂度**：时间 O(log x)，空间 O(1)。
