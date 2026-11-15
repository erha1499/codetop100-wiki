---
rank: 65
id: "695"
title: 岛屿的最大面积
difficulty: 中等
tags: [图, DFS, BFS, 矩阵]
freq: 97
link: https://leetcode.cn/problems/max-area-of-island/
desc: 求网格中最大的岛屿面积（由 1 组成的四连通块的格子数）。
---
## 思路

- 和 [200 岛屿数量](#/200) 一样是 Flood Fill：遍历网格，遇到 `1` 就把整座岛淹掉，只是这次要**数淹了多少格**，取最大值。
- **DFS**：函数返回从 `(i, j)` 出发淹掉的格子数 = `1 + 四个方向的结果之和`。
- **BFS**：每座岛一个队列，出队一个 `area++`。

## 易错点

- 原地把访问过的格子置 0，否则重复访问 / 死循环。
- DFS 的越界判断放最前面；BFS 入队时就置 0。
- 这题网格是数字 `1`，[200](#/200) 是字符 `'1'`。

## 代码

### 写法一：DFS

```python
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(i, j):                       # 返回从 (i, j) 淹掉的面积
            if not (0 <= i < m and 0 <= j < n) or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            return 1 + dfs(i - 1, j) + dfs(i + 1, j) + dfs(i, j - 1) + dfs(i, j + 1)

        return max(dfs(i, j) for i in range(m) for j in range(n))
```

```java
class Solution {
    public int maxAreaOfIsland(int[][] grid) {
        int res = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == 1) res = Math.max(res, dfs(grid, i, j));
            }
        }
        return res;
    }

    // 返回从 (i, j) 淹掉的面积
    private int dfs(int[][] grid, int i, int j) {
        if (i < 0 || j < 0 || i >= grid.length || j >= grid[0].length || grid[i][j] == 0) return 0;
        grid[i][j] = 0;
        return 1 + dfs(grid, i - 1, j) + dfs(grid, i + 1, j) + dfs(grid, i, j - 1) + dfs(grid, i, j + 1);
    }
}
```

### 写法二：BFS

```python
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                grid[i][j] = 0               # 入队时就标记
                q, area = deque([(i, j)]), 0
                while q:
                    x, y = q.popleft()
                    area += 1
                    for nx, ny in (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1):
                        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                            grid[nx][ny] = 0
                            q.append((nx, ny))
                res = max(res, area)
        return res
```

```java
class Solution {
    private static final int[][] DIRS = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

    public int maxAreaOfIsland(int[][] grid) {
        int m = grid.length, n = grid[0].length, res = 0;
        Deque<int[]> q = new ArrayDeque<>();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 0) continue;
                grid[i][j] = 0;                  // 入队时就标记
                q.offer(new int[]{i, j});
                int area = 0;
                while (!q.isEmpty()) {
                    int[] cur = q.poll();
                    area++;
                    for (int[] d : DIRS) {
                        int x = cur[0] + d[0], y = cur[1] + d[1];
                        if (x < 0 || x >= m || y < 0 || y >= n || grid[x][y] == 0) continue;
                        grid[x][y] = 0;
                        q.offer(new int[]{x, y});
                    }
                }
                res = Math.max(res, area);
            }
        }
        return res;
    }
}
```

**复杂度**：时间 O(mn)，空间最坏 O(mn)。
