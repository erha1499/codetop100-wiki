---
rank: 24
id: "54"
title: 螺旋矩阵
difficulty: 中等
tags: [矩阵, 模拟]
freq: 262
link: https://leetcode.cn/problems/spiral-matrix/
desc: 按顺时针螺旋顺序返回矩阵中的所有元素。
---
## 思路

- 维护还没遍历的矩形的四条边界 `up / down / left / right`。
- 每轮按「上边 → 右边 → 下边 → 左边」走一圈，每走完一条边就收缩对应的边界。
- 循环条件直接用「结果数量 `< m * n`」，装满就停，最稳。

## 易错点

- 每条边遍历前都要判断边界是否还合法（`up <= down`、`left <= right`）：只剩一行或一列时，不判断会把同一行 / 列走两遍。
- 走完一条边立刻收缩，后面的边才不会重复访问拐角。

## 代码

```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        up, down, left, right = 0, m - 1, 0, n - 1
        res = []
        while len(res) < m * n:
            if up <= down:                           # 上边：从左到右
                for j in range(left, right + 1):
                    res.append(matrix[up][j])
                up += 1
            if left <= right:                        # 右边：从上到下
                for i in range(up, down + 1):
                    res.append(matrix[i][right])
                right -= 1
            if up <= down:                           # 下边：从右到左
                for j in range(right, left - 1, -1):
                    res.append(matrix[down][j])
                down -= 1
            if left <= right:                        # 左边：从下到上
                for i in range(down, up - 1, -1):
                    res.append(matrix[i][left])
                left += 1
        return res
```

```java
class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        int m = matrix.length, n = matrix[0].length;
        int up = 0, down = m - 1, left = 0, right = n - 1;
        List<Integer> res = new ArrayList<>();
        while (res.size() < m * n) {
            if (up <= down) {                            // 上边：从左到右
                for (int j = left; j <= right; j++) res.add(matrix[up][j]);
                up++;
            }
            if (left <= right) {                         // 右边：从上到下
                for (int i = up; i <= down; i++) res.add(matrix[i][right]);
                right--;
            }
            if (up <= down) {                            // 下边：从右到左
                for (int j = right; j >= left; j--) res.add(matrix[down][j]);
                down--;
            }
            if (left <= right) {                         // 左边：从下到上
                for (int i = down; i >= up; i--) res.add(matrix[i][left]);
                left++;
            }
        }
        return res;
    }
}
```

**复杂度**：时间 O(mn)，空间 O(1)（不计答案）。
