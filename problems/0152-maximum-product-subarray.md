---
rank: 72
id: "152"
title: 乘积最大子数组
difficulty: 中等
tags: [动态规划]
freq: 91
link: https://leetcode.cn/problems/maximum-product-subarray/
desc: 求乘积最大的非空连续子数组的乘积。
---
## 思路

- 和 [53 最大子数组和](#/53) 的区别：乘法遇到负数会让**最小值翻身变成最大值**，所以要同时维护两个状态：
  - `dpMax`：以 `nums[i]` 结尾的最大乘积；
  - `dpMin`：以 `nums[i]` 结尾的最小乘积。
- 每个位置三个候选：自己重新开始 `nums[i]`、接在最大值后面 `dpMax * nums[i]`、接在最小值后面 `dpMin * nums[i]`。`dpMax` 取三者最大，`dpMin` 取三者最小。
- 只依赖前一个位置，压成两个变量。

## 易错点

- 压成变量后注意更新顺序：先把旧的 `dpMin`（或 `dpMax`）存下来，否则算第二个时用到的是刚更新过的值。
- 遇到 0 乘积断开，「自己重新开始」这个候选保证了能从下一个数重新起头。
- 答案是过程中 `dpMax` 的最大值；初始化用 `nums[0]` 而不是 0 或 1。

## 代码

```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp_min = dp_max = res = nums[0]
        for x in nums[1:]:
            last_min = dp_min                # 先存旧值
            dp_min = min(last_min * x, dp_max * x, x)
            dp_max = max(last_min * x, dp_max * x, x)
            res = max(res, dp_max)
        return res
```

```java
class Solution {
    public int maxProduct(int[] nums) {
        int dpMin = nums[0], dpMax = nums[0], res = nums[0];
        for (int i = 1; i < nums.length; i++) {
            int lastMin = dpMin;             // 先存旧值
            dpMin = Math.min(nums[i], Math.min(lastMin * nums[i], dpMax * nums[i]));
            dpMax = Math.max(nums[i], Math.max(lastMin * nums[i], dpMax * nums[i]));
            res = Math.max(res, dpMax);
        }
        return res;
    }
}
```

**复杂度**：时间 O(n)，空间 O(1)。
