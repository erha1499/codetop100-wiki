---
rank: 100
id: "169"
title: 多数元素
difficulty: 简单
tags: [数组]
freq: 68
link: https://leetcode.cn/problems/majority-element/
desc: 找出数组中出现次数超过 n/2 的元素（题目保证存在）。
---
## 思路

- **摩尔投票**：不同的元素两两抵消，多数元素最后一定剩下。
- 维护候选 `res` 和血量 `hp`（还没被抵消掉的候选个数，不是它的出现次数）：
  - `hp == 0`：前面的全部抵消完了，当前元素当新候选，`hp = 1`；
  - 遇到和候选相同的：`hp + 1`；
  - 遇到不同的：抵消一个，`hp - 1`。
- 为什么对：多数元素的个数比其它所有元素加起来还多，就算每个其它元素都拿去抵消它，它仍有剩余；其它元素互相抵消更不影响。

## 易错点

- 只有「保证存在多数元素」时才能直接返回候选；不保证的话要再遍历一次验证次数。
- 更直接的做法：哈希表计数 O(n) 空间，或者排序后取中间元素 O(n log n)。

## 代码

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, hp = 0, 0
        for num in nums:
            if hp == 0:
                res, hp = num, 1
            else:
                hp += 1 if res == num else -1
        return res
```

```java
class Solution {
    public int majorityElement(int[] nums) {
        int res = 0, hp = 0;
        for (int num : nums) {
            if (hp == 0) {
                res = num;
                hp = 1;
            } else {
                hp += res == num ? 1 : -1;
            }
        }
        return res;
    }
}
```

**复杂度**：时间 O(n)，空间 O(1)。
