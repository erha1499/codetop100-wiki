---
rank: 98
id: "283"
title: 移动零
difficulty: 简单
tags: [双指针, 数组]
freq: 68
link: https://leetcode.cn/problems/move-zeroes/
desc: 把数组里所有的 0 原地移到末尾，同时保持非零元素的相对顺序。
---
## 思路

- 双指针：`i` 负责遍历，`start0` 指向**下一个非零元素应该放的位置**。数组始终分三段：`[0, start0)` 是已归位的非零元素，`[start0, i)` 全是 0，`[i, n)` 还没看。
- 遇到 0 只移动 `i`；遇到非零元素就和 `nums[start0]` 交换，然后 `start0` 右移。
- 为什么顺序不乱：非零元素是按扫描顺序依次归位的。`start0 < i` 时被换出去的一定是 0；`start0 == i` 时是自己和自己换。

## 易错点

- 必须原地操作。
- 也可以写成「先把非零元素依次覆盖到前面，再把后面全部填 0」，交换的写法一趟就够。

## 代码

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        start0 = 0                           # 下一个非零元素应放入的位置
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[start0] = nums[start0], nums[i]
                start0 += 1
```

```java
class Solution {
    public void moveZeroes(int[] nums) {
        int start0 = 0;                      // 下一个非零元素应放入的位置
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != 0) {
                int temp = nums[i];
                nums[i] = nums[start0];
                nums[start0] = temp;
                start0++;
            }
        }
    }
}
```

**复杂度**：时间 O(n)，空间 O(1)。
