---
rank: 79
id: "48"
title: 旋转图像
difficulty: 中等
tags: [矩阵]
freq: 85
link: https://leetcode.cn/problems/rotate-image/
desc: 把 n×n 矩阵原地顺时针旋转 90 度。
---
## 思路

- 旋转 = **两次翻转**。顺时针 90° 有两种等价的组合：
  - 沿主对角线翻转（转置）→ 每一行左右翻转；
  - 沿副对角线翻转 → 上下翻转。
- 其它角度同理：逆时针 90° = 转置 → 上下翻转；180° = 上下翻转 → 每行左右翻转。
- 坐标关系：主对角线 `(i, j) ↔ (j, i)`；副对角线 `(i, j) ↔ (n-1-j, n-1-i)`。

## 易错点

- 对角线翻转只遍历对角线一侧（主对角线 `j > i`，副对角线 `j < n - 1 - i`），遍历整个矩阵会换两次、等于没换。
- 必须原地改，不能新开矩阵。

## 代码

### 写法一：转置 + 左右翻转

```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n):                   # 沿主对角线翻转
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for row in matrix:                   # 每行左右翻转
            row.reverse()
```

```java
class Solution {
    public void rotate(int[][] matrix) {
        int n = matrix.length;
        for (int i = 0; i < n; i++) {                // 沿主对角线翻转
            for (int j = i + 1; j < n; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }
        for (int[] row : matrix) {                   // 每行左右翻转
            for (int l = 0, r = n - 1; l < r; l++, r--) {
                int temp = row[l];
                row[l] = row[r];
                row[r] = temp;
            }
        }
    }
}
```

### 写法二：副对角线翻转 + 上下翻转

```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n):                   # 沿副对角线翻转
            for j in range(n - 1 - i):
                matrix[i][j], matrix[n - 1 - j][n - 1 - i] = matrix[n - 1 - j][n - 1 - i], matrix[i][j]
        matrix.reverse()                     # 上下翻转
```

```java
class Solution {
    public void rotate(int[][] matrix) {
        int n = matrix.length;
        for (int i = 0; i < n; i++) {                // 沿副对角线翻转
            for (int j = 0; j < n - 1 - i; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[n - 1 - j][n - 1 - i];
                matrix[n - 1 - j][n - 1 - i] = temp;
            }
        }
        for (int i = 0; i < n / 2; i++) {            // 上下翻转：直接交换行引用
            int[] temp = matrix[i];
            matrix[i] = matrix[n - 1 - i];
            matrix[n - 1 - i] = temp;
        }
    }
}
```

**复杂度**：时间 O(n²)，空间 O(1)。
