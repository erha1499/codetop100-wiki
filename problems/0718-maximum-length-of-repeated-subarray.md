---
rank: 94
id: "718"
title: 最长重复子数组
difficulty: 中等
tags: [动态规划]
freq: 71
link: https://leetcode.cn/problems/maximum-length-of-repeated-subarray/
desc: 求两个整数数组中最长的公共子数组（要求连续）的长度。
---
## 思路

- `dp[i][j]`：**以 `nums1[i-1]` 和 `nums2[j-1]` 结尾**的最长公共子数组长度。
- 这两个数相等：`dp[i][j] = dp[i-1][j-1] + 1`；不相等：以它们结尾的公共子数组不存在，`dp[i][j] = 0`。
- 答案是整张表里的最大值。

## 易错点

- 和 [1143 最长公共子序列](#/1143) 的区别：子数组必须连续，所以不相等时是 **0**，而不是 `max(上, 左)`；答案也不是 `dp[m][n]`，要取全表最大值。
- `dp` 多开一行一列，下标 `i` 对应元素 `i - 1`。

## 代码

```python
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        res = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    res = max(res, dp[i][j])
        return res
```

```java
class Solution {
    public int findLength(int[] nums1, int[] nums2) {
        int m = nums1.length, n = nums2.length;
        int[][] dp = new int[m + 1][n + 1];
        int res = 0;
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (nums1[i - 1] == nums2[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                    res = Math.max(res, dp[i][j]);
                }
            }
        }
        return res;
    }
}
```

**复杂度**：时间 O(mn)，空间 O(mn)（可压成一维，内层要倒序遍历）。
