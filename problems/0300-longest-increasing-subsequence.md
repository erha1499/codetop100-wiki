---
rank: 19
id: "300"
title: 最长上升子序列
difficulty: 中等
tags: [动态规划, 二分]
freq: 276
link: https://leetcode.cn/problems/longest-increasing-subsequence/
desc: 求数组中最长严格递增子序列的长度。
---
## 思路

- **DP，O(n²)**：`dp[i]` = 以 `nums[i]` 结尾的最长递增子序列长度；枚举前面的 `j`，`nums[j] < nums[i]` 时 `dp[i] = max(dp[i], dp[j] + 1)`。答案是所有 `dp[i]` 的最大值。
- **贪心 + 二分，O(n log n)**：`tail[i]` = 长度为 `i + 1` 的递增子序列的最小结尾。结尾越小，后面越容易接。
  - `tail` 一定递增，所以对每个 `num` 二分找第一个 `>= num` 的位置换掉它；找不到（比所有结尾都大）就接在末尾，长度加一。

## 易错点

- 严格递增：DP 里是 `nums[j] < nums[i]`；二分里是找第一个 `>= num`（`tail[mid] < num` 才右移），写成 `<=` 会把重复元素也算进去。
- `tail` 的长度是答案，但 `tail` 本身不一定是一个真实的子序列。

## 代码

### 写法一：DP

```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
```

```java
class Solution {
    public int lengthOfLIS(int[] nums) {
        int n = nums.length, res = 1;
        int[] dp = new int[n];
        Arrays.fill(dp, 1);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[j] < nums[i]) dp[i] = Math.max(dp[i], dp[j] + 1);
            }
            res = Math.max(res, dp[i]);
        }
        return res;
    }
}
```

### 写法二：贪心 + 二分

```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tail = []                            # tail[i]：长度 i+1 的递增子序列的最小结尾
        for num in nums:
            i = bisect_left(tail, num)       # 第一个 >= num 的位置
            if i == len(tail):
                tail.append(num)
            else:
                tail[i] = num
        return len(tail)
```

```java
class Solution {
    public int lengthOfLIS(int[] nums) {
        int[] tail = new int[nums.length];       // tail[i]：长度 i+1 的递增子序列的最小结尾
        int res = 0;
        for (int num : nums) {
            int left = 0, right = res;           // 在 [0, res) 找第一个 >= num 的位置
            while (left < right) {
                int mid = left + (right - left) / 2;
                if (tail[mid] < num) left = mid + 1;
                else right = mid;
            }
            tail[left] = num;
            if (left == res) res++;
        }
        return res;
    }
}
```

**复杂度**：DP 时间 O(n²)；贪心 + 二分时间 O(n log n)；空间都是 O(n)。
