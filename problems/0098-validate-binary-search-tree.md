---
rank: 83
id: "98"
title: 验证二叉搜索树
difficulty: 中等
tags: [二叉树, DFS]
freq: 84
link: https://leetcode.cn/problems/validate-binary-search-tree/
desc: 判断一棵二叉树是否是有效的二叉搜索树（左子树全部 < 根 < 右子树全部）。
---
## 思路

- **上下界递归**：每个节点带一个合法的开区间 `(left, right)`，节点值必须落在里面；往左走把上界收紧成当前值，往右走把下界收紧成当前值。
- **中序遍历**：BST 的中序序列严格递增，遍历时记住上一个访问的值 `pre`，当前值必须大于它。

## 易错点

- 只比较「左孩子 < 根 < 右孩子」是不够的：右子树里的每一个节点都要大于根，所以要传区间。
- 严格不等，相等也不合法。
- 节点值可能就是 `Integer.MIN_VALUE` / `MAX_VALUE`：Java 的初始边界和 `pre` 都要用 `long`。

## 代码

### 写法一：上下界递归

```python
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, left, right):          # root 子树的值都必须在 (left, right) 内
            if not root:
                return True
            if not left < root.val < right:
                return False
            return dfs(root.left, left, root.val) and dfs(root.right, root.val, right)

        return dfs(root, -inf, inf)
```

```java
class Solution {
    public boolean isValidBST(TreeNode root) {
        return dfs(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }

    // root 子树的值都必须在 (left, right) 内
    private boolean dfs(TreeNode root, long left, long right) {
        if (root == null) return true;
        if (root.val <= left || root.val >= right) return false;
        return dfs(root.left, left, root.val) && dfs(root.right, root.val, right);
    }
}
```

### 写法二：中序遍历

```python
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        pre = -inf                           # 中序遍历中上一个访问的值

        def inorder(node):
            nonlocal pre
            if not node:
                return True
            if not inorder(node.left):
                return False
            if node.val <= pre:
                return False
            pre = node.val
            return inorder(node.right)

        return inorder(root)
```

```java
class Solution {
    private long pre = Long.MIN_VALUE;       // 中序遍历中上一个访问的值

    public boolean isValidBST(TreeNode root) {
        if (root == null) return true;
        if (!isValidBST(root.left)) return false;
        if (root.val <= pre) return false;
        pre = root.val;
        return isValidBST(root.right);
    }
}
```

**复杂度**：时间 O(n)，空间 O(h)。
