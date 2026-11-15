---
rank: 81
id: "560"
title: 和为K的子数组
difficulty: 中等
tags: [哈希表, 前缀和]
freq: 84
link: https://leetcode.cn/problems/subarray-sum-equals-k/
desc: 统计数组中和恰好为 k 的连续子数组的个数（元素可以为负）。
---
## 思路

- **前缀和 + 两数之和**。子数组 `nums[j+1..i]` 的和 = `s[i] - s[j]`，要它等于 `k`，就是找前面有多少个前缀和等于 `s[i] - k`。
- 遍历时维护当前前缀和 `s`，用哈希表 `cnt` 记录「每个前缀和出现过几次」：先把 `cnt[s - k]` 加进答案，再把 `s` 记进表里。
- 初始化 `cnt[0] = 1`：一个元素都不取时前缀和是 0，用来统计从下标 0 开始的子数组。

## 易错点

- 不能用滑动窗口：有负数，窗口和不单调。
- `cnt[0] = 1` 不能漏。
- 表里存的是**次数**不是「有没有」：同一个前缀和出现几次，就能和当前位置配出几个子数组。
- 先查再存：否则 `k = 0` 时会把自己和自己配上。

## 代码

```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int)               # 前缀和 -> 出现次数
        cnt[0] = 1
        res = s = 0
        for x in nums:
            s += x
            res += cnt[s - k]
            cnt[s] += 1
        return res
```

```java
class Solution {
    public int subarraySum(int[] nums, int k) {
        Map<Integer, Integer> cnt = new HashMap<>();     // 前缀和 -> 出现次数
        cnt.put(0, 1);
        int res = 0, s = 0;
        for (int x : nums) {
            s += x;
            res += cnt.getOrDefault(s - k, 0);
            cnt.put(s, cnt.getOrDefault(s, 0) + 1);
        }
        return res;
    }
}
```

**复杂度**：时间 O(n)，空间 O(n)。
