---
rank: 32
id: "42"
title: 接雨水
difficulty: 困难
tags: [双指针, 数组]
freq: 201
link: https://leetcode.cn/problems/trapping-rain-water/
desc: 给定柱子高度数组，求下雨后能接多少雨水。
---
## 思路

- 位置 `i` 能接的水 = `min(左边最高, 右边最高) - height[i]`。
- 双指针：`l_max` 是 `[0, left]` 的最高柱子，`r_max` 是 `[right, n-1]` 的最高柱子。
- **谁小处理谁**：`l_max < r_max` 时，`left` 位置的水量已经确定是 `l_max - height[left]`（右边再高也不影响 min），处理完 `left++`；否则对称地处理 `right`。

## 易错点

- 先更新 `l_max` / `r_max`，再算水量，否则可能出现负数。
- 循环条件 `left < right`。

## 代码

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        l_max = r_max = res = 0
        while left < right:
            l_max = max(l_max, height[left])
            r_max = max(r_max, height[right])
            if l_max < r_max:
                res += l_max - height[left]
                left += 1
            else:
                res += r_max - height[right]
                right -= 1
        return res
```

```java
class Solution {
    public int trap(int[] height) {
        int left = 0, right = height.length - 1;
        int lMax = 0, rMax = 0, res = 0;
        while (left < right) {
            lMax = Math.max(lMax, height[left]);
            rMax = Math.max(rMax, height[right]);
            if (lMax < rMax) {
                res += lMax - height[left];
                left++;
            } else {
                res += rMax - height[right];
                right--;
            }
        }
        return res;
    }
}
```

**复杂度**：时间 O(n)，空间 O(1)。
