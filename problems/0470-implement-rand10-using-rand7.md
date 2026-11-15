---
rank: 67
id: "470"
title: 用 Rand7() 实现 Rand10()
difficulty: 中等
tags: [数学, 概率]
freq: 97
link: https://leetcode.cn/problems/implement-rand10-using-rand7/
desc: 只用等概率生成 1~7 的 rand7()，实现等概率生成 1~10 的 rand10()。
---
## 思路

- **等概率扩展 + 拒绝采样**。
- 两次 `rand7()` 拼成等概率的 `[1, 49]`：`num = (a - 1) * 7 + b`（把 7×7 的格子展平成一维）。
- 49 不是 10 的倍数：只接受前 40 个数，映射成 `num % 10 + 1`；落在 `[41, 49]` 就丢弃重来。
- 优化（废物利用，减少重抽次数）：
  - 被丢弃的 `[41, 49]` 有 9 个数，等价于一个 rand9，再乘一次 `rand7()` 得到 `[1, 63]`，接受前 60 个；
  - 剩下 `[61, 63]` 的 3 个数再乘一次得到 `[1, 21]`，接受前 20 个；剩 1 个数没法再利用，重来。

## 易错点

- 不能用 `rand7() + rand7()` 或直接 `% 10`：只有在大小是 10 的倍数的均匀区间上取模才等概率。
- `(a - 1) * 7 + b` 里的 `- 1` 不能丢，否则范围不是连续的 `[1, 49]`。

## 代码

### 写法一：拒绝采样

```python
class Solution:
    def rand10(self) -> int:
        while True:
            num = (rand7() - 1) * 7 + rand7()    # 均匀的 [1, 49]
            if num <= 40:
                return num % 10 + 1
```

```java
class Solution extends SolBase {
    public int rand10() {
        while (true) {
            int num = (rand7() - 1) * 7 + rand7();   // 均匀的 [1, 49]
            if (num <= 40) return num % 10 + 1;
        }
    }
}
```

### 写法二：复用被拒绝的数

```python
class Solution:
    def rand10(self) -> int:
        while True:
            num = (rand7() - 1) * 7 + rand7()            # [1, 49]
            if num <= 40:
                return num % 10 + 1
            num = (num - 40 - 1) * 7 + rand7()           # 剩 9 个数 -> [1, 63]
            if num <= 60:
                return num % 10 + 1
            num = (num - 60 - 1) * 7 + rand7()           # 剩 3 个数 -> [1, 21]
            if num <= 20:
                return num % 10 + 1
```

```java
class Solution extends SolBase {
    public int rand10() {
        while (true) {
            int num = (rand7() - 1) * 7 + rand7();       // [1, 49]
            if (num <= 40) return num % 10 + 1;
            num = (num - 40 - 1) * 7 + rand7();          // 剩 9 个数 -> [1, 63]
            if (num <= 60) return num % 10 + 1;
            num = (num - 60 - 1) * 7 + rand7();          // 剩 3 个数 -> [1, 21]
            if (num <= 20) return num % 10 + 1;
        }
    }
}
```

**复杂度**：期望 O(1)。写法一平均调用 rand7 约 2.45 次，写法二约 2.19 次。
