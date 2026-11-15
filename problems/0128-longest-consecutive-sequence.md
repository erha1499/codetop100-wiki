---
rank: 66
id: "128"
title: 最长连续序列
difficulty: 中等
tags: [哈希表, 数组]
freq: 97
link: https://leetcode.cn/problems/longest-consecutive-sequence/
desc: 求未排序数组中数字连续的最长序列的长度（不要求在原数组里相邻），要求 O(n)。
---
## 思路

- 全部放进 `HashSet`，O(1) 查找。
- **只从「序列的起点」开始往右数**：`num - 1` 不在集合里，`num` 才是起点；然后不断看 `cur + 1` 在不在集合里。
- 每个数最多被「往右数」经过一次，所以总共是 O(n)。

## 易错点

- 不判断起点、对每个数都往右数，会退化成 O(n²)。
- **遍历集合而不是原数组**：原数组有大量重复时，同一个起点会被反复扩展而超时。

## 代码

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        res = 0
        for num in num_set:
            if num - 1 in num_set:           # 不是起点，跳过
                continue
            cur = num
            while cur + 1 in num_set:
                cur += 1
            res = max(res, cur - num + 1)
        return res
```

```java
class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for (int num : nums) set.add(num);
        int res = 0;
        for (int num : set) {
            if (set.contains(num - 1)) continue;     // 不是起点，跳过
            int cur = num;
            while (set.contains(cur + 1)) cur++;
            res = Math.max(res, cur - num + 1);
        }
        return res;
    }
}
```

**复杂度**：时间 O(n)，空间 O(n)。
