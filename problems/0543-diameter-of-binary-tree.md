---
rank: 85
id: "543"
title: 二叉树的直径
difficulty: 简单
tags: [二叉树, DFS]
freq: 82
link: https://leetcode.cn/problems/diameter-of-binary-tree/
desc: 求二叉树的直径：任意两个节点之间最长路径的边数。
---
## 思路

- 直径**不一定经过根**，所以要枚举每个节点当「拐点」：经过它的最长路径 = 左子树深度 + 右子树深度。
- 后序遍历求深度的同时，用 `l + r` 更新全局最大值；函数本身返回深度 `max(l, r) + 1`。
- 和 [124 最大路径和](#/124) 是同一个模型：返回值是「单边」，全局答案是「两边加起来」。

## 易错点

- 统计的是边数，所以是 `l + r`，不是 `l + r + 1`。
- 函数返回的是深度，不是直径。

## 代码

```python
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def depth(root):
            nonlocal res
            if not root:
                return 0
            l, r = depth(root.left), depth(root.right)
            res = max(res, l + r)            # 以 root 为拐点的路径边数
            return max(l, r) + 1

        depth(root)
        return res
```

```java
class Solution {
    private int res = 0;

    public int diameterOfBinaryTree(TreeNode root) {
        depth(root);
        return res;
    }

    private int depth(TreeNode root) {
        if (root == null) return 0;
        int l = depth(root.left), r = depth(root.right);
        res = Math.max(res, l + r);          // 以 root 为拐点的路径边数
        return Math.max(l, r) + 1;
    }
}
```

**复杂度**：时间 O(n)，空间 O(h)。
