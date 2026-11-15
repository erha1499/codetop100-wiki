---
rank: 60
id: "34"
title: 在排序数组中查找元素的第一个和最后一个位置
difficulty: 中等
tags: [二分]
freq: 104
link: https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/
desc: 在非递减数组中找 target 的第一个和最后一个位置，不存在返回 [-1, -1]，要求 O(log n)。
---
## 思路

- 两次二分找左右边界，都用闭区间 `[left, right]`：
  - **左边界** = 第一个 `>= target` 的位置：`nums[mid] < target` 往右，否则（`>=`）收缩右边界 `right = mid - 1`。循环结束时 `left` 就是它。
  - **右边界** = 最后一个 `<= target` 的位置：`nums[mid] > target` 往左，否则（`<=`）收缩左边界 `left = mid + 1`。循环结束时 `right` 就是它。
- 两个边界都要验证：下标没越界，且该位置的值确实等于 `target`。

## 易错点

- 找到 `nums[mid] == target` 时不能直接返回，要继续往边界那一侧收缩。
- 左边界返回 `left`，右边界返回 `right`，别记反：循环结束时 `left = right + 1`。
- `target` 不存在时，`left` / `right` 落在插入点附近甚至越界（`left == n` 或 `right == -1`），所以必须先判越界再比较值。

## 代码

```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.leftBound(nums, target), self.rightBound(nums, target)]

    def leftBound(self, nums, target):       # 第一个 >= target 的位置
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left if left < len(nums) and nums[left] == target else -1

    def rightBound(self, nums, target):      # 最后一个 <= target 的位置
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return right if right >= 0 and nums[right] == target else -1
```

```java
class Solution {
    public int[] searchRange(int[] nums, int target) {
        return new int[]{leftBound(nums, target), rightBound(nums, target)};
    }

    // 第一个 >= target 的位置
    private int leftBound(int[] nums, int target) {
        int left = 0, right = nums.length - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] < target) left = mid + 1;
            else right = mid - 1;
        }
        return left < nums.length && nums[left] == target ? left : -1;
    }

    // 最后一个 <= target 的位置
    private int rightBound(int[] nums, int target) {
        int left = 0, right = nums.length - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] > target) right = mid - 1;
            else left = mid + 1;
        }
        return right >= 0 && nums[right] == target ? right : -1;
    }
}
```

**复杂度**：时间 O(log n)，空间 O(1)。
