---
rank: 80
id: "240"
title: 搜索二维矩阵 II
difficulty: 中等
tags: [矩阵, 双指针]
freq: 85
link: https://leetcode.cn/problems/search-a-2d-matrix-ii/
desc: 在每行从左到右递增、每列从上到下递增的矩阵中查找 target。
---
## 思路

- 从**右上角**出发做排除法。右上角的数是所在行的最大值、所在列的最小值：
  - 当前值 `> target`：这一列下面的都更大，整列排除，`j--`；
  - 当前值 `< target`：这一行左边的都更小，整行排除，`i++`；
  - 相等就找到了。
- 每一步排除一行或一列，最多走 `m + n` 步。从左下角出发同理。

## 易错点

- 起点只能是右上角或左下角。左上角（往右往下都变大）和右下角（都变小）没法判断该往哪走。
- 循环条件 `i < m && j >= 0`。

## 代码

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n - 1                      # 右上角
        while i < m and j >= 0:
            cur = matrix[i][j]
            if cur == target:
                return True
            if cur > target:
                j -= 1                       # 排除这一列
            else:
                i += 1                       # 排除这一行
        return False
```

```java
class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int m = matrix.length, n = matrix[0].length;
        int i = 0, j = n - 1;                // 右上角
        while (i < m && j >= 0) {
            int cur = matrix[i][j];
            if (cur == target) return true;
            if (cur > target) j--;           // 排除这一列
            else i++;                        // 排除这一行
        }
        return false;
    }
}
```

**复杂度**：时间 O(m + n)，空间 O(1)。
