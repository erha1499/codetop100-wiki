---
rank: 74
id: "110"
title: 平衡二叉树
difficulty: 简单
tags: [二叉树, DFS]
freq: 90
link: https://leetcode.cn/problems/balanced-binary-tree/
desc: 判断二叉树是否平衡：每个节点的左右子树高度差都不超过 1。
---
## 思路

- 后序 DFS 求每个节点的高度，回溯时顺便检查 `|左高 - 右高| <= 1`。
- `dfs` 返回的是**高度**；是否平衡记在全局变量 `res` 里，一旦发现不平衡就置为 false。
- 剪枝：`res` 已经是 false 时直接返回，不用再算。

## 易错点

- 必须每个节点都检查，只看根节点的左右高度差是不够的。
- 自顶向下「对每个节点分别求左右高度」是 O(n²)；后序一次遍历、边求高度边判断才是 O(n)。
- 不用全局变量的写法：用返回值 `-1` 表示「这棵子树已经不平衡」，一路往上传。

## 代码

```python
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True

        def dfs(root):                       # 返回子树高度
            nonlocal res
            if not root or not res:
                return 0
            left_depth, right_depth = dfs(root.left), dfs(root.right)
            if abs(left_depth - right_depth) > 1:
                res = False
            return 1 + max(left_depth, right_depth)

        dfs(root)
        return res
```

```java
class Solution {
    private boolean res = true;

    public boolean isBalanced(TreeNode root) {
        dfs(root);
        return res;
    }

    // 返回子树高度
    private int dfs(TreeNode root) {
        if (root == null || !res) return 0;
        int leftDepth = dfs(root.left), rightDepth = dfs(root.right);
        if (Math.abs(leftDepth - rightDepth) > 1) res = false;
        return 1 + Math.max(leftDepth, rightDepth);
    }
}
```

**复杂度**：时间 O(n)，空间 O(h)。
