---
rank: 35
id: "124"
title: 二叉树中的最大路径和
difficulty: 困难
tags: [二叉树, DFS]
freq: 187
link: https://leetcode.cn/problems/binary-tree-maximum-path-sum/
desc: 求二叉树中任意节点到任意节点的路径的最大和（路径至少含一个节点，不能分叉）。
---
## 思路

- 树形 DP + 后序遍历。每个节点做两件事：
  1. **当拐点**：左贡献 + 自己 + 右贡献，更新全局答案 `res`；
  2. **向父节点汇报**：只能带一条边，`root.val + max(l, r)`。
- `dfs(root)` 的含义：`root` 往下的**单边**路径最多能给父节点贡献多少；贡献为负就返回 0，表示「不要这条边」。
- 因为返回值已经和 0 取过 max，拿到的 `l`、`r` 一定 ≥ 0，可以直接用。

## 易错点

- `dfs` 的返回值不是答案，答案在全局变量里。
- 返回给父节点时不能左右都选（路径不能分叉）。
- `res` 初始化成最小值而不是 0（节点可能全为负）；更新 `res` 时也不能和 0 取 max。

## 代码

```python
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -inf

        def dfs(root):                       # root 往下的单边路径能提供的最大贡献（至少为 0）
            nonlocal res
            if not root:
                return 0
            l, r = dfs(root.left), dfs(root.right)
            res = max(res, root.val + l + r)         # root 当拐点
            return max(root.val + max(l, r), 0)      # 负贡献就不要

        dfs(root)
        return res
```

```java
class Solution {
    private int res = Integer.MIN_VALUE;

    public int maxPathSum(TreeNode root) {
        dfs(root);
        return res;
    }

    // root 往下的单边路径能提供的最大贡献（至少为 0）
    private int dfs(TreeNode root) {
        if (root == null) return 0;
        int l = dfs(root.left), r = dfs(root.right);
        res = Math.max(res, root.val + l + r);           // root 当拐点
        return Math.max(root.val + Math.max(l, r), 0);   // 负贡献就不要
    }
}
```

**复杂度**：时间 O(n)，空间 O(h)。
