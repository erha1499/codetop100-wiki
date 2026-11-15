---
rank: 57
id: "41"
title: 缺失的第一个正数
difficulty: 困难
tags: [数组, 哈希表]
freq: 116
link: https://leetcode.cn/problems/first-missing-positive/
desc: 找出未排序数组中没有出现的最小正整数，要求 O(n) 时间、O(1) 额外空间。
---
## 思路

- 长度为 `n` 的数组，答案只可能在 `[1, n + 1]`：`1 ~ n` 全出现了答案是 `n + 1`，否则是其中缺的最小那个。
- **原地哈希：用下标 `x - 1` 位置的正负号，表示数字 `x` 有没有出现过。**
  1. 先清理：`<= 0` 或 `> n` 的数不影响答案，统一改成 `n + 1`（这样全是正数了）；
  2. 遍历：对每个 `x = |nums[i]|`，若 `x <= n`，把 `nums[x - 1]` 改成负数；
  3. 再遍历：第一个仍为正数的位置 `i` 说明 `i + 1` 没出现过；全为负则返回 `n + 1`。

## 易错点

- 第 2 步取数要用绝对值：当前位置可能已经被前面的数字标成负数了。
- 标记时写 `-|nums[x - 1]|`，不要直接取反——同一个数出现两次会被翻回正数。
- 另一种等价做法是「把 `x` 交换到下标 `x - 1`」，同样是原地哈希。

## 代码

```python
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):                   # 1. 无效数字统一改成 n + 1
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1
        for i in range(n):                   # 2. x 出现过 -> 把下标 x - 1 标成负数
            x = abs(nums[i])
            if x <= n:
                nums[x - 1] = -abs(nums[x - 1])
        for i in range(n):                   # 3. 第一个没被标记的位置
            if nums[i] > 0:
                return i + 1
        return n + 1
```

```java
class Solution {
    public int firstMissingPositive(int[] nums) {
        int n = nums.length;
        for (int i = 0; i < n; i++) {        // 1. 无效数字统一改成 n + 1
            if (nums[i] <= 0 || nums[i] > n) nums[i] = n + 1;
        }
        for (int i = 0; i < n; i++) {        // 2. x 出现过 -> 把下标 x - 1 标成负数
            int x = Math.abs(nums[i]);
            if (x <= n) nums[x - 1] = -Math.abs(nums[x - 1]);
        }
        for (int i = 0; i < n; i++) {        // 3. 第一个没被标记的位置
            if (nums[i] > 0) return i + 1;
        }
        return n + 1;
    }
}
```

**复杂度**：时间 O(n)，空间 O(1)。
