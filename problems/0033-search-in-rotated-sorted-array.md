---
rank: 13
id: "33"
title: 搜索旋转排序数组
difficulty: 中等
tags: [二分]
freq: 323
link: https://leetcode.cn/problems/search-in-rotated-sorted-array/
desc: 在旋转过的升序数组（无重复元素）中查找 target 的下标，要求 O(log n)。
---
## 思路

- 二分。用 `nums[mid]` 和 `nums[right]` 比较，判断哪一半有序：
  - `nums[mid] > nums[right]`：`mid` 在左边的大值段，`[left, mid]` 有序；
  - 否则 `mid` 在右边的小值段，`[mid, right]` 有序。
- 再看 `target` 是否落在有序的那一半里，决定丢掉哪一半。

## 易错点

- 循环条件 `left <= right`：找具体元素，`left == right` 时那个位置还没检查。
- 前面已经判过 `nums[mid] == target`，所以收缩时可以放心 `mid ± 1`。
- 判断 `target` 在有序半边内时，靠 `mid` 的一侧是开的（`target < nums[mid]`），靠边界的一侧是闭的（`nums[left] <= target`）。

## 代码

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > nums[right]:              # [left, mid] 有序
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:                                    # [mid, right] 有序
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
```

```java
class Solution {
    public int search(int[] nums, int target) {
        int left = 0, right = nums.length - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == target) return mid;
            if (nums[mid] > nums[right]) {               // [left, mid] 有序
                if (nums[left] <= target && target < nums[mid]) right = mid - 1;
                else left = mid + 1;
            } else {                                     // [mid, right] 有序
                if (nums[mid] < target && target <= nums[right]) left = mid + 1;
                else right = mid - 1;
            }
        }
        return -1;
    }
}
```

**复杂度**：时间 O(log n)，空间 O(1)。
