---
rank: 96
id: "207"
title: 课程表
difficulty: 中等
tags: [图, DFS, BFS]
freq: 69
link: https://leetcode.cn/problems/course-schedule/
desc: 给定课程之间的先修关系，判断能否修完所有课程（即有向图中是否无环）。
---
## 思路

- 本质：**判断有向图有没有环**。先建邻接表，`[cur, pre]` 表示先修 `pre` 才能修 `cur`，建边 `pre → cur`。
- **DFS 判环**：两个标记数组——
  - `visited`：这个点搜过了，不用再搜；
  - `onPath`：这个点在**当前这条 DFS 路径**上。
  - 走到一个 `onPath` 为真的点，说明绕回了自己的祖先，有环。离开节点时把 `onPath` 复位。
- **BFS 拓扑排序**：统计每个点的入度，入度为 0 的先入队；出队一个就把它指向的点入度减一，减到 0 的入队。最后出队的点数等于课程数就无环。

## 易错点

- `onPath` 离开节点时必须复位，`visited` 不用。只用一个 `visited` 会把「从别的路径访问过」误判成环。
- 图可能不连通，每个点都要作为起点 DFS 一次。
- 边的方向别建反：`graph[pre].add(cur)`。

## 代码

### 写法一：DFS 判环

```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for cur, pre in prerequisites:
            graph[pre].append(cur)           # pre -> cur
        visited = [False] * numCourses
        on_path = [False] * numCourses
        found = False                        # 是否发现环

        def dfs(i):
            nonlocal found
            if found:
                return
            if on_path[i]:                   # 绕回当前路径上的点：有环
                found = True
                return
            if visited[i]:
                return
            visited[i] = on_path[i] = True
            for course in graph[i]:
                dfs(course)
            on_path[i] = False               # 离开节点

        for i in range(numCourses):
            dfs(i)
        return not found
```

```java
class Solution {
    private List<Integer>[] graph;
    private boolean[] onPath, visited;
    private boolean found = false;               // 是否发现环

    public boolean canFinish(int numCourses, int[][] prerequisites) {
        graph = new List[numCourses];
        for (int i = 0; i < numCourses; i++) graph[i] = new ArrayList<>();
        for (int[] edge : prerequisites) {
            graph[edge[1]].add(edge[0]);         // pre -> cur
        }
        onPath = new boolean[numCourses];
        visited = new boolean[numCourses];
        for (int i = 0; i < numCourses; i++) dfs(i);
        return !found;
    }

    private void dfs(int i) {
        if (found) return;
        if (onPath[i]) {                         // 绕回当前路径上的点：有环
            found = true;
            return;
        }
        if (visited[i]) return;
        visited[i] = true;
        onPath[i] = true;
        for (int course : graph[i]) dfs(course);
        onPath[i] = false;                       // 离开节点
    }
}
```

### 写法二：BFS 拓扑排序

```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for cur, pre in prerequisites:
            graph[pre].append(cur)
            indegree[cur] += 1
        q = deque(i for i in range(numCourses) if indegree[i] == 0)
        count = 0                            # 已经能修完的课程数
        while q:
            i = q.popleft()
            count += 1
            for course in graph[i]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    q.append(course)
        return count == numCourses
```

```java
class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) graph.add(new ArrayList<>());
        int[] indegree = new int[numCourses];
        for (int[] edge : prerequisites) {
            graph.get(edge[1]).add(edge[0]);
            indegree[edge[0]]++;
        }
        Deque<Integer> q = new ArrayDeque<>();
        for (int i = 0; i < numCourses; i++) {
            if (indegree[i] == 0) q.offer(i);
        }
        int count = 0;                           // 已经能修完的课程数
        while (!q.isEmpty()) {
            int i = q.poll();
            count++;
            for (int course : graph.get(i)) {
                if (--indegree[course] == 0) q.offer(course);
            }
        }
        return count == numCourses;
    }
}
```

**复杂度**：时间 O(V + E)，空间 O(V + E)。
