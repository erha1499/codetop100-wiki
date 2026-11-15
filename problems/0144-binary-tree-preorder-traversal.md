---
rank: 84
id: "144"
title: 二叉树的前序遍历
difficulty: 简单
tags: [二叉树, 栈]
freq: 84
link: https://leetcode.cn/problems/binary-tree-preorder-traversal/
desc: 返回二叉树的前序遍历（根 → 左 → 右）。
---
## 思路

- **递归**：访问当前节点 → `dfs(左)` → `dfs(右)`。
- **迭代**：用栈模拟。弹出一个节点就访问它，然后**先压右孩子、再压左孩子**——栈后进先出，左孩子会先被弹出来。

## 易错点

- 迭代的压栈顺序是右 → 左。
- 空节点不入栈；空树直接返回空列表。
- 中序的迭代写法不一样，见 [94](#/94)。

## 代码

### 写法一：递归

```python
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(root):
            if not root:
                return
            res.append(root.val)             # 根
            dfs(root.left)                   # 左
            dfs(root.right)                  # 右

        dfs(root)
        return res
```

```java
class Solution {
    private final List<Integer> res = new ArrayList<>();

    public List<Integer> preorderTraversal(TreeNode root) {
        dfs(root);
        return res;
    }

    private void dfs(TreeNode root) {
        if (root == null) return;
        res.add(root.val);                   // 根
        dfs(root.left);                      // 左
        dfs(root.right);                     // 右
    }
}
```

### 写法二：迭代

```python
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res, stack = [], [root]
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            if cur.right:                    # 先压右，再压左
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        return res
```

```java
class Solution {
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        if (root == null) return res;
        Deque<TreeNode> stack = new ArrayDeque<>();
        stack.push(root);
        while (!stack.isEmpty()) {
            TreeNode cur = stack.pop();
            res.add(cur.val);
            if (cur.right != null) stack.push(cur.right);    // 先压右，再压左
            if (cur.left != null) stack.push(cur.left);
        }
        return res;
    }
}
```

**复杂度**：时间 O(n)，空间 O(h)。
