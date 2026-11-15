---
rank: 40
id: "199"
title: 二叉树的右视图
difficulty: 中等
tags: [二叉树, BFS, DFS]
freq: 161
link: https://leetcode.cn/problems/binary-tree-right-side-view/
desc: 返回从右侧看二叉树时能看到的节点值（每层最右边的节点），从上到下。
---
## 思路

- 问题就是找每层最右边的节点。
- **BFS**：层序遍历时**先右孩子后左孩子**入队，这样每层第一个出队的（`i == 0`）就是最右节点。
- **DFS**：按「根 → 右 → 左」的顺序走，并带上深度。第一次到达某个深度（`depth == res.size()`）时遇到的一定是这层最右的节点。

## 易错点

- BFS 的入队顺序必须是右 → 左，否则 `i == 0` 拿到的是最左节点（或者保持左 → 右，取每层最后一个）。
- DFS 必须先递归右子树。

## 代码

### 写法一：BFS

```python
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res, q = [], deque([root])
        while q:
            for i in range(len(q)):
                cur = q.popleft()
                if i == 0:                   # 每层第一个出队的就是最右节点
                    res.append(cur.val)
                if cur.right:
                    q.append(cur.right)
                if cur.left:
                    q.append(cur.left)
        return res
```

```java
class Solution {
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        if (root == null) return res;
        Deque<TreeNode> q = new ArrayDeque<>();
        q.offer(root);
        while (!q.isEmpty()) {
            int sz = q.size();
            for (int i = 0; i < sz; i++) {
                TreeNode cur = q.poll();
                if (i == 0) res.add(cur.val);            // 每层第一个出队的就是最右节点
                if (cur.right != null) q.offer(cur.right);
                if (cur.left != null) q.offer(cur.left);
            }
        }
        return res;
    }
}
```

### 写法二：DFS

```python
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node, depth):
            if not node:
                return
            if depth == len(res):            # 第一次到达这一层
                res.append(node.val)
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 0)
        return res
```

```java
class Solution {
    private final List<Integer> res = new ArrayList<>();

    public List<Integer> rightSideView(TreeNode root) {
        dfs(root, 0);
        return res;
    }

    private void dfs(TreeNode node, int depth) {
        if (node == null) return;
        if (depth == res.size()) res.add(node.val);      // 第一次到达这一层
        dfs(node.right, depth + 1);
        dfs(node.left, depth + 1);
    }
}
```

**复杂度**：时间 O(n)；空间 BFS O(n)（队列），DFS O(h)（递归栈）。
