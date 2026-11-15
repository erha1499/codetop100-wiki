---
rank: 16
id: "88"
title: 合并两个有序数组
difficulty: 简单
tags: [双指针, 数组]
freq: 305
link: https://leetcode.cn/problems/merge-sorted-array/
desc: 把有序数组 nums2 原地合并进有序数组 nums1（nums1 末尾已预留 n 个空位）。
---
## 思路

- 利用 `nums1` 末尾的空位，**三个指针从后往前**，谁大放谁。
- `p1 = m - 1`、`p2 = n - 1` 指向两个数组的有效末尾，`p = m + n - 1` 指向待填位置。
- 从后往前填不会覆盖 `nums1` 里还没处理的数；从前往后会。

## 易错点

- 循环只需看 `p2 >= 0`：`nums2` 放完后，`nums1` 剩下的本来就在正确位置，不用再拷。
- `p1` 可能先走完（如 `m = 0`），比较前要判 `p1 >= 0`。

## 代码

```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1, p2, p = m - 1, n - 1, m + n - 1
        while p2 >= 0:
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
```

```java
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int p1 = m - 1, p2 = n - 1, p = m + n - 1;
        while (p2 >= 0) {
            if (p1 >= 0 && nums1[p1] > nums2[p2]) {
                nums1[p--] = nums1[p1--];
            } else {
                nums1[p--] = nums2[p2--];
            }
        }
    }
}
```

**复杂度**：时间 O(m + n)，空间 O(1)。
