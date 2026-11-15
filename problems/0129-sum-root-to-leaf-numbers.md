---
rank: 63
id: "129"
title: 求根到叶子节点数字之和
difficulty: 中等
tags: [二叉树, DFS]
freq: 100
link: https://leetcode.cn/problems/sum-root-to-leaf-numbers/
desc: 每条从根到叶子的路径拼成一个数字，求所有这些数字的和。
---
## 思路

- DFS 往下走，路径上的数字按十进制拼接：`path = path * 10 + node.val`（每下一层相当于原数左移一位）。
- 走到叶子节点（左右孩子都为空）时，把当前 `path` 加进结果。

## 易错点

- 只在**叶子**节点累加，不是在空节点累加（否则只有一个孩子的节点会被多算）。
- `path` 当参数往下传时，每层有自己的副本，不用回溯。如果写成全局变量，递归返回前要撤销：`path = (path - node.val) / 10`，否则会污染兄弟节点的路径。

## 代码

```python
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node, path):
            nonlocal res
            if not node:
                return
            path = path * 10 + node.val
            if not node.left and not node.right:     # 叶子
                res += path
                return
            dfs(node.left, path)
            dfs(node.right, path)

        dfs(root, 0)
        return res
```

```java
class Solution {
    private int res = 0;

    public int sumNumbers(TreeNode root) {
        dfs(root, 0);
        return res;
    }

    private void dfs(TreeNode node, int path) {
        if (node == null) return;
        path = path * 10 + node.val;
        if (node.left == null && node.right == null) {   // 叶子
            res += path;
            return;
        }
        dfs(node.left, path);
        dfs(node.right, path);
    }
}
```

**复杂度**：时间 O(n)，空间 O(h)。
