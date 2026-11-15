---
rank: 37
id: "4"
title: 寻找两个正序数组的中位数
difficulty: 困难
tags: [二分, 数组]
freq: 175
link: https://leetcode.cn/problems/median-of-two-sorted-arrays/
desc: 求两个有序数组合并后的中位数，要求 O(log(m+n))。
---
## 思路

- **二分的是划分位置，不是值**。把两个数组各切一刀：`nums1` 左边 `i` 个，`nums2` 左边 `j` 个，要求
  - 左半边总个数 = `(m + n + 1) / 2`（所以 `j` 由 `i` 决定）；
  - 左半边所有数 ≤ 右半边所有数，即 `left1 <= right2` 且 `left2 <= right1`。
- 在 `nums1` 上二分 `i`：
  - `left1 > right2`：`nums1` 左边拿多了，`hi = i - 1`；
  - `left2 > right1`：`nums1` 左边拿少了，`lo = i + 1`；
  - 否则划分正确：总长奇数答案是 `max(left1, left2)`，偶数是 `(max(left1, left2) + min(right1, right2)) / 2`。

## 易错点

- 先保证 `nums1` 是较短的那个：二分更快，更重要的是保证 `j` 不越界。
- 一刀切在数组最左 / 最右时，那一侧没有元素：左边缺就用 `-∞`，右边缺就用 `+∞`，省掉一堆 if。
- `i` 的范围是 `[0, m]`（m+1 种切法），循环条件 `lo <= hi`。
- Java 偶数情况除以 `2.0`，别做整数除法。

## 代码

```python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        lo, hi = 0, m
        while lo <= hi:
            i = (lo + hi) // 2               # nums1 左边取 i 个
            j = (m + n + 1) // 2 - i         # nums2 左边取 j 个
            left1 = nums1[i - 1] if i > 0 else -inf
            right1 = nums1[i] if i < m else inf
            left2 = nums2[j - 1] if j > 0 else -inf
            right2 = nums2[j] if j < n else inf
            if left1 > right2:
                hi = i - 1
            elif left2 > right1:
                lo = i + 1
            elif (m + n) % 2:
                return max(left1, left2)
            else:
                return (max(left1, left2) + min(right1, right2)) / 2
        return 0.0
```

```java
class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        if (nums1.length > nums2.length) return findMedianSortedArrays(nums2, nums1);
        int m = nums1.length, n = nums2.length;
        int lo = 0, hi = m;
        while (lo <= hi) {
            int i = lo + (hi - lo) / 2;          // nums1 左边取 i 个
            int j = (m + n + 1) / 2 - i;         // nums2 左边取 j 个
            int left1 = i > 0 ? nums1[i - 1] : Integer.MIN_VALUE;
            int right1 = i < m ? nums1[i] : Integer.MAX_VALUE;
            int left2 = j > 0 ? nums2[j - 1] : Integer.MIN_VALUE;
            int right2 = j < n ? nums2[j] : Integer.MAX_VALUE;
            if (left1 > right2) {
                hi = i - 1;
            } else if (left2 > right1) {
                lo = i + 1;
            } else if ((m + n) % 2 != 0) {
                return Math.max(left1, left2);
            } else {
                return (Math.max(left1, left2) + Math.min(right1, right2)) / 2.0;
            }
        }
        return 0;
    }
}
```

**复杂度**：时间 O(log min(m, n))，空间 O(1)。
