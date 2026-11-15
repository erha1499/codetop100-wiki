---
rank: 15
id: "1"
title: 两数之和
difficulty: 简单
tags: [哈希表]
freq: 306
link: https://leetcode.cn/problems/two-sum/
desc: 在数组中找出和为 target 的两个数，返回它们的下标。
---
## 思路

- 一次遍历 + 哈希表，存的是「**我需要的数 → 我的下标**」：遍历到 `x` 时登记 `need[target - x] = i`。
- 后面遇到某个数正好在表里，说明它就是前面某个数等的那个，直接配对返回。
- 等价的常见写法是存 `数 → 下标`，查 `target - x` 在不在表里。

## 易错点

- **先查再存**：反过来的话 `[3, 3], target = 6` 这类会自己配自己。

## 代码

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        need = {}                            # 需要的数 -> 等它的那个下标
        for i, x in enumerate(nums):
            if x in need:
                return [need[x], i]
            need[target - x] = i
        return []
```

```java
class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> need = new HashMap<>();   // 需要的数 -> 等它的那个下标
        for (int i = 0; i < nums.length; i++) {
            if (need.containsKey(nums[i])) {
                return new int[]{need.get(nums[i]), i};
            }
            need.put(target - nums[i], i);
        }
        return new int[0];
    }
}
```

**复杂度**：时间 O(n)，空间 O(n)。
