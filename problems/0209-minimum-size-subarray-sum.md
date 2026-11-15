---
rank: 90
id: "209"
title: 长度最小的子数组
difficulty: 中等
tags: [滑动窗口]
freq: 74
link: https://leetcode.cn/problems/minimum-size-subarray-sum/
desc: 在正整数数组中找出和 ≥ target 的最短连续子数组的长度，不存在返回 0。
---
## 思路

- 数组全是正数 → 窗口扩大和变大、缩小和变小，有单调性，可以用滑动窗口。
- 窗口左闭右开 `[left, right)`：`right` 右移把数加进 `window`；只要 `window >= target` 就更新最短长度，然后收缩 `left`，直到不满足为止。

## 易错点

- 收缩用 `while`，要一直缩到不满足条件。
- 左闭右开，长度是 `right - left`。
- 没有合法窗口时返回 0，不是初始的最大值。
- 有负数就不能用滑动窗口了（那是前缀和 + 单调队列的题）。

## 代码

```python
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = right = window = 0
        res = inf
        while right < len(nums):
            window += nums[right]
            right += 1
            while window >= target:          # 满足条件就尽量收缩
                res = min(res, right - left)
                window -= nums[left]
                left += 1
        return 0 if res == inf else res
```

```java
class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int left = 0, right = 0, window = 0;
        int res = Integer.MAX_VALUE;
        while (right < nums.length) {
            window += nums[right++];
            while (window >= target) {       // 满足条件就尽量收缩
                res = Math.min(res, right - left);
                window -= nums[left++];
            }
        }
        return res == Integer.MAX_VALUE ? 0 : res;
    }
}
```

**复杂度**：时间 O(n)，空间 O(1)。
