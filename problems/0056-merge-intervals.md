---
rank: 27
id: "56"
title: 合并区间
difficulty: 中等
tags: [排序, 数组]
freq: 251
link: https://leetcode.cn/problems/merge-intervals/
desc: 合并所有重叠的区间，返回不重叠的区间列表。
---
## 思路

- 区间题套路：**先按左端点排序**。
- 遍历每个区间 `cur`，和结果集最后一个区间 `last` 比：
  - `cur[0] <= last[1]`：有重叠，把 `last` 的右端点更新成两者较大的；
  - 否则不相交，`cur` 作为新区间加入结果。

## 易错点

- 判断重叠是 `<=`：`[1,4]` 和 `[4,5]` 端点相接也算重叠。
- 合并时右端点取 `max`：`[1,4]` 和 `[2,3]` 合并后还是 `[1,4]`。

## 代码

```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        for cur in intervals[1:]:
            last = res[-1]
            if cur[0] <= last[1]:
                last[1] = max(last[1], cur[1])
            else:
                res.append(cur)
        return res
```

```java
class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> a[0] - b[0]);
        LinkedList<int[]> res = new LinkedList<>();
        res.add(intervals[0]);
        for (int i = 1; i < intervals.length; i++) {
            int[] cur = intervals[i], last = res.getLast();
            if (cur[0] <= last[1]) {
                last[1] = Math.max(last[1], cur[1]);
            } else {
                res.add(cur);
            }
        }
        return res.toArray(new int[0][]);
    }
}
```

**复杂度**：时间 O(n log n)（排序），空间 O(log n)（不计答案）。
