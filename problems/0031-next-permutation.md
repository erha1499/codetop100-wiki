---
rank: 49
id: "31"
title: 下一个排列
difficulty: 中等
tags: [数组, 双指针]
freq: 137
link: https://leetcode.cn/problems/next-permutation/
desc: 原地把数组改成字典序的下一个排列；已经是最大排列则变成最小排列。
---
## 思路

目标是「刚好大一点」的排列，三步：

1. 从右往左找第一个升序位置 `i`（`nums[i] < nums[i+1]`）。`i` 右边是一段降序，已经是这些数能排出的最大值，只能让第 `i` 位变大。
2. 从右往左找第一个比 `nums[i]` 大的数 `nums[j]`——后缀降序，所以它是比 `nums[i]` 大的数里最小的。交换 `i`、`j`。
3. 交换后后缀仍然降序，把它反转成升序，让后面尽可能小。

## 易错点

- 找 `i` 和找 `j` 的比较都带等号（`>=`）：有重复元素时相等不算「更大」。
- 整个数组降序时找不到 `i`（`i == -1`），跳过交换，`reverse(i + 1, n - 1)` 正好是整体反转，不用特判。

## 代码

```python
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:     # 1. 从右往左找第一个升序位置
            i -= 1
        if i >= 0:
            j = n - 1
            while nums[i] >= nums[j]:                # 2. 从右往左找第一个比 nums[i] 大的
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        lo, hi = i + 1, n - 1                        # 3. 反转后缀
        while lo < hi:
            nums[lo], nums[hi] = nums[hi], nums[lo]
            lo += 1
            hi -= 1
```

```java
class Solution {
    public void nextPermutation(int[] nums) {
        int n = nums.length, i = n - 2;
        while (i >= 0 && nums[i] >= nums[i + 1]) {   // 1. 从右往左找第一个升序位置
            i--;
        }
        if (i >= 0) {
            int j = n - 1;
            while (nums[i] >= nums[j]) {             // 2. 从右往左找第一个比 nums[i] 大的
                j--;
            }
            swap(nums, i, j);
        }
        for (int lo = i + 1, hi = n - 1; lo < hi; lo++, hi--) {   // 3. 反转后缀
            swap(nums, lo, hi);
        }
    }

    private void swap(int[] nums, int i, int j) {
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
}
```

**复杂度**：时间 O(n)，空间 O(1)。
