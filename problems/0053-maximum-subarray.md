---
rank: 7
id: "53"
title: 最大子数组和
difficulty: 中等
tags: [动态规划]
freq: 382
link: https://leetcode.cn/problems/maximum-subarray/
desc: 求和最大的连续子数组的和。
---
## 思路

- `dp[i]`：**以 `nums[i]` 结尾**的最大子数组和。
- 两种选择：接在前面后面，或者自己重新开始 → `dp[i] = max(nums[i], dp[i-1] + nums[i])`。
- 本质：前面的和是负数就丢掉。`dp[i]` 只依赖 `dp[i-1]`，压成一个变量。

## 易错点

- 答案是所有 `dp[i]` 的最大值，不是 `dp[n-1]`。
- `res` 初始化成 `nums[0]` 而不是 0（全负数时答案是负的）。

## 代码

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = res = nums[0]
        for x in nums[1:]:
            dp = max(x, dp + x)        # 自己重新开始 or 接在前面后面
            res = max(res, dp)
        return res
```

```java
class Solution {
    public int maxSubArray(int[] nums) {
        int dp = nums[0], res = nums[0];
        for (int i = 1; i < nums.length; i++) {
            dp = Math.max(nums[i], dp + nums[i]);   // 自己重新开始 or 接在前面后面
            res = Math.max(res, dp);
        }
        return res;
    }
}
```

**复杂度**：时间 O(n)，空间 O(1)。
