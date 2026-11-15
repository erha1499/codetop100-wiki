---
rank: 71
id: "104"
title: 二叉树的最大深度
difficulty: 简单
tags: [二叉树, DFS, BFS]
freq: 92
link: https://leetcode.cn/problems/maximum-depth-of-binary-tree/
desc: 求二叉树的最大深度（根到最远叶子的节点数）。
---
## 思路

- **DFS**：一棵树的深度 = `1 + max(左子树深度, 右子树深度)`，空树为 0。后序思想：先算左右，再汇总到当前节点。
- **BFS**：层序遍历，每处理完一层 `depth++`。

## 易错点

- 空树返回 0，不是 1。
- BFS 里 `depth++` 在每层的 for 循环结束之后；同样要先记下 `sz = q.size()`。

## 代码

### 写法一：DFS

```python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
```

```java
class Solution {
    public int maxDepth(TreeNode root) {
        if (root == null) return 0;
        return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
    }
}
```

### 写法二：BFS

```python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        depth, q = 0, deque([root])
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            depth += 1                       # 一层结束
        return depth
```

```java
class Solution {
    public int maxDepth(TreeNode root) {
        if (root == null) return 0;
        int depth = 0;
        Deque<TreeNode> q = new ArrayDeque<>();
        q.offer(root);
        while (!q.isEmpty()) {
            int sz = q.size();
            for (int i = 0; i < sz; i++) {
                TreeNode cur = q.poll();
                if (cur.left != null) q.offer(cur.left);
                if (cur.right != null) q.offer(cur.right);
            }
            depth++;                         // 一层结束
        }
        return depth;
    }
}
```

**复杂度**：时间 O(n)；空间 DFS O(h)，BFS O(n)。
