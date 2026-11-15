---
rank: 86
id: "162"
title: 寻找峰值
difficulty: 中等
tags: [二分]
freq: 80
link: https://leetcode.cn/problems/find-peak-element/
desc: 找出数组中任意一个峰值（严格大于左右相邻元素）的下标，数组两端之外视为负无穷，要求 O(log n)。
---
## 思路

- 只要任意一个峰值，不用找最高的：**二分时永远往更高的一侧走**。
- 比较 `nums[m]` 和 `nums[m + 1]`：
  - `nums[m] < nums[m + 1]`：右边是上坡，往右走一定能遇到峰值（一直涨到头，最后一个元素也是峰值，因为界外是 -∞），`l = m + 1`；
  - `nums[m] > nums[m + 1]`：右边是下坡，`m` 自己或它左边一定有峰值，`r = m`。
- 区间收缩到一个点就是答案。

## 易错点

- 用闭区间 `[0, n - 1]` + `while (l < r)`：此时 `m < r <= n - 1`，访问 `m + 1` 不会越界。若写成左闭右开 `r = n`，就要额外判断 `m == n - 1`。
- 下坡时是 `r = m`，不是 `m - 1`：`m` 自己可能就是峰值。

## 代码

```python
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] < nums[m + 1]:        # 上坡，峰值在右边
                l = m + 1
            else:                            # 下坡，m 或它左边有峰值
                r = m
        return l
```

```java
class Solution {
    public int findPeakElement(int[] nums) {
        int l = 0, r = nums.length - 1;
        while (l < r) {
            int m = l + (r - l) / 2;
            if (nums[m] < nums[m + 1]) {     // 上坡，峰值在右边
                l = m + 1;
            } else {                         // 下坡，m 或它左边有峰值
                r = m;
            }
        }
        return l;
    }
}
```

**复杂度**：时间 O(log n)，空间 O(1)。
