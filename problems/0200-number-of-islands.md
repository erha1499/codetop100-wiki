---
rank: 10
id: "200"
title: 岛屿数量
difficulty: 中等
tags: [图, DFS, BFS, 矩阵]
freq: 337
link: https://leetcode.cn/problems/number-of-islands/
desc: 统计由 '1' 组成的四连通岛屿的数量。
---
## 思路

- **连通块计数 + Flood Fill**：遍历网格，遇到 `'1'` 就是一座新岛，`res++`，然后用 DFS / BFS 把整座岛淹成 `'0'`。
- 还能看到 `'1'` 说明它没被之前的岛淹过，一定是新连通块。
- 同类：[695 岛屿的最大面积](#/695)、飞地数量、被围绕的区域、腐烂的橘子。

## 易错点

- DFS 终止条件：越界，或者当前格不是 `'1'`（海水 / 已访问）。
- BFS 要在**入队时**就标记，出队时才标记会重复入队。
- 网格里是字符 `'1'` 不是数字 1。

## 代码

### DFS

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(x, y):
            if not (0 <= x < m and 0 <= y < n) or grid[x][y] != "1":
                return
            grid[x][y] = "0"                 # 淹掉
            dfs(x - 1, y)
            dfs(x + 1, y)
            dfs(x, y - 1)
            dfs(x, y + 1)

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    res += 1
                    dfs(i, j)
        return res
```

```java
class Solution {
    public int numIslands(char[][] grid) {
        int res = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == '1') {
                    res++;
                    dfs(grid, i, j);
                }
            }
        }
        return res;
    }

    private void dfs(char[][] grid, int x, int y) {
        if (x < 0 || x >= grid.length || y < 0 || y >= grid[0].length || grid[x][y] != '1') return;
        grid[x][y] = '0';                        // 淹掉
        dfs(grid, x - 1, y);
        dfs(grid, x + 1, y);
        dfs(grid, x, y - 1);
        dfs(grid, x, y + 1);
    }
}
```

### BFS

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != "1":
                    continue
                res += 1
                grid[i][j] = "0"             # 入队时就淹掉
                q = deque([(i, j)])
                while q:
                    x, y = q.popleft()
                    for nx, ny in (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1):
                        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == "1":
                            grid[nx][ny] = "0"
                            q.append((nx, ny))
        return res
```

```java
class Solution {
    private static final int[][] DIRS = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

    public int numIslands(char[][] grid) {
        int m = grid.length, n = grid[0].length, res = 0;
        Deque<int[]> q = new ArrayDeque<>();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] != '1') continue;
                res++;
                grid[i][j] = '0';                // 入队时就淹掉
                q.offer(new int[]{i, j});
                while (!q.isEmpty()) {
                    int[] cur = q.poll();
                    for (int[] d : DIRS) {
                        int nx = cur[0] + d[0], ny = cur[1] + d[1];
                        if (nx < 0 || nx >= m || ny < 0 || ny >= n || grid[nx][ny] != '1') continue;
                        grid[nx][ny] = '0';
                        q.offer(new int[]{nx, ny});
                    }
                }
            }
        }
        return res;
    }
}
```

**复杂度**：时间 O(mn)，空间最坏 O(mn)（递归栈 / 队列）。
