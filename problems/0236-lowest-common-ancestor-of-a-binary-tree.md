---
rank: 20
id: "236"
title: 二叉树的最近公共祖先
difficulty: 中等
tags: [二叉树, DFS]
freq: 272
link: https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/
desc: 找出二叉树中两个节点 p、q 的最近公共祖先。
---
## 思路

- 后序遍历，自底向上回传结果。函数含义：在以 `root` 为根的子树里找 `p`、`q`。
- `root` 为空或者就是 `p` / `q`：直接返回 `root`。
- 递归左右子树得到 `l`、`r`：
  - 都不为空 → `p`、`q` 分居两侧，当前 `root` 就是最近公共祖先；
  - 只有一边不为空 → 答案在那一边，把它往上传；
  - 都为空 → 返回空。

## 易错点

- 一个节点可以是自己的祖先：遇到 `p` 或 `q` 立即返回、不再往下找——如果另一个在它的子树里，它本身就是答案。
- 必须是后序：要先知道左右子树各自有没有找到，才能判断当前节点。

## 代码

```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root is p or root is q:
            return root
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        if l and r:                          # 一边一个，root 就是答案
            return root
        return l or r                        # 只有一边找到（或都没找到）
```

```java
class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null || root == p || root == q) return root;
        TreeNode l = lowestCommonAncestor(root.left, p, q);
        TreeNode r = lowestCommonAncestor(root.right, p, q);
        if (l != null && r != null) return root;     // 一边一个，root 就是答案
        return l != null ? l : r;                    // 只有一边找到（或都没找到）
    }
}
```

**复杂度**：时间 O(n)，空间 O(h)（递归栈）。
