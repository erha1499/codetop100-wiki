---
rank: 89
id: "198"
title: 打家劫舍
difficulty: 中等
tags: [动态规划]
freq: 77
link: https://leetcode.cn/problems/house-robber/
desc: 一排房子不能偷相邻的两间，求能偷到的最大金额。
---
## 思路

- 本质：从数组里选若干个不相邻的数，使和最大。
- 对每间房只有两个选择：
  - 偷：拿 `nums[i]`，相邻的那间不能偷；
  - 不偷：直接看剩下的。
- 自底向上：`dp[i]` = 前 `i` 间房的最大金额，`dp[i] = max(dp[i-1], nums[i-1] + dp[i-2])`。只依赖前两项，压成两个变量。
- 自顶向下：`dp(i)` = 从第 `i` 间开始往后偷的最大金额，`dp(i) = max(nums[i] + dp(i+2), dp(i+1))`，越界返回 0。

## 易错点

- 两种写法的状态定义方向相反（前缀 / 后缀），转移式别混用。
- 压成变量后更新顺序：先算出新值，再整体往后挪。
- 延伸：213 房子围成一圈（拆成两段分别算）、337 树形。

## 代码

### 写法一：滚动变量

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2 = prev1 = 0                    # dp[i-2], dp[i-1]
        for x in nums:
            prev2, prev1 = prev1, max(prev1, x + prev2)   # 不偷 / 偷
        return prev1
```

```java
class Solution {
    public int rob(int[] nums) {
        int prev2 = 0, prev1 = 0;            // dp[i-2], dp[i-1]
        for (int x : nums) {
            int cur = Math.max(prev1, x + prev2);    // 不偷 / 偷
            prev2 = prev1;
            prev1 = cur;
        }
        return prev1;
    }
}
```

### 写法二：记忆化递归

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def dp(i):                           # 从第 i 间开始偷的最大金额
            if i >= len(nums):
                return 0
            return max(nums[i] + dp(i + 2), dp(i + 1))

        return dp(0)
```

```java
class Solution {
    private int[] memo;

    public int rob(int[] nums) {
        memo = new int[nums.length];
        Arrays.fill(memo, -1);
        return dp(nums, 0);
    }

    // 从第 i 间开始偷的最大金额
    private int dp(int[] nums, int i) {
        if (i >= nums.length) return 0;
        if (memo[i] != -1) return memo[i];
        return memo[i] = Math.max(nums[i] + dp(nums, i + 2), dp(nums, i + 1));
    }
}
```

**复杂度**：时间 O(n)；空间滚动变量 O(1)，记忆化 O(n)。
