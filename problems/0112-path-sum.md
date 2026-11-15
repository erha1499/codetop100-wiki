---
rank: 93
id: "112"
title: 路径总和
difficulty: 简单
tags: [二叉树, DFS]
freq: 72
link: https://leetcode.cn/problems/path-sum/
desc: 判断二叉树中是否存在一条从根到叶子的路径，节点值之和等于 targetSum。
---
## 思路

- 每往下走一步，把目标减去当前节点的值，问题变成「在子树里找和为剩余值的根到叶子路径」。
- 走到**叶子**时，看剩余值是否正好等于叶子的值。
- 左右子树有一边成立即可。
- 要输出所有路径就是 [113](#/113)，那题需要 `path` + 回溯。

## 易错点

- 必须在叶子处判断：路径走到一半和就够了不算。
- 空树返回 false（即使 `targetSum` 是 0）。
- 节点值可能为负，不能因为超过目标就提前剪枝。

## 代码

```python
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:         # 叶子
            return root.val == targetSum
        rest = targetSum - root.val
        return self.hasPathSum(root.left, rest) or self.hasPathSum(root.right, rest)
```

```java
class Solution {
    public boolean hasPathSum(TreeNode root, int targetSum) {
        if (root == null) return false;
        if (root.left == null && root.right == null) {   // 叶子
            return root.val == targetSum;
        }
        int rest = targetSum - root.val;
        return hasPathSum(root.left, rest) || hasPathSum(root.right, rest);
    }
}
```

**复杂度**：时间 O(n)，空间 O(h)。
