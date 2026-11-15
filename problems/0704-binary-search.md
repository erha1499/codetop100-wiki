---
rank: 42
id: "704"
title: 二分查找
difficulty: 简单
tags: [二分]
freq: 153
link: https://leetcode.cn/problems/binary-search/
desc: 在升序数组中查找 target，返回下标，不存在返回 -1。
---
## 思路

- 闭区间 `[l, r]` 的二分模板：
  - `nums[mid] == target` 返回；
  - `nums[mid] > target`，目标在左边，`r = mid - 1`；
  - `nums[mid] < target`，目标在右边，`l = mid + 1`。
- 循环结束还没找到就是不存在。

## 易错点

- 闭区间的一整套要配齐：`r = n - 1`、`while (l <= r)`、`mid ± 1`。
- Java 求中点写 `l + (r - l) / 2`，防止 `l + r` 溢出。

## 代码

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1
```

```java
class Solution {
    public int search(int[] nums, int target) {
        int l = 0, r = nums.length - 1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (nums[mid] == target) return mid;
            if (nums[mid] > target) r = mid - 1;
            else l = mid + 1;
        }
        return -1;
    }
}
```

**复杂度**：时间 O(log n)，空间 O(1)。
