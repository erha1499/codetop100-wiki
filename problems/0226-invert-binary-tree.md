---
rank: 99
id: "226"
title: 翻转二叉树
difficulty: 简单
tags: [二叉树, DFS, BFS]
freq: 68
link: https://leetcode.cn/problems/invert-binary-tree/
desc: 翻转二叉树：把每个节点的左右子树交换，得到镜像。
---
## 思路

- 对每个节点交换它的左右孩子就行。交换的是节点引用，不是节点值。
- **递归**：`dfs(root)` 的含义是「翻转以 `root` 为根的子树并返回它的根」。先翻转左右子树，再把两棵翻转好的子树交换。
- **迭代**：用队列（或栈）遍历所有节点，出队一个就交换它的左右孩子，再把非空孩子入队。只要每个节点都访问到，不需要分层。

## 易错点

- 递归函数要返回 `root`，否则父节点接到的是空，子树就丢了。
- 先存下两个递归结果再赋值；写成 `root.left = dfs(root.right)` 之后再用 `root.left` 就已经被改掉了。

## 代码

### 写法一：递归

```python
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        l = self.invertTree(root.left)       # 翻转原左子树
        r = self.invertTree(root.right)      # 翻转原右子树
        root.left, root.right = r, l
        return root
```

```java
class Solution {
    public TreeNode invertTree(TreeNode root) {
        if (root == null) return null;
        TreeNode l = invertTree(root.left);      // 翻转原左子树
        TreeNode r = invertTree(root.right);     // 翻转原右子树
        root.left = r;
        root.right = l;
        return root;
    }
}
```

### 写法二：BFS

```python
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        q = deque([root])
        while q:
            node = q.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return root
```

```java
class Solution {
    public TreeNode invertTree(TreeNode root) {
        if (root == null) return null;
        Deque<TreeNode> q = new ArrayDeque<>();
        q.offer(root);
        while (!q.isEmpty()) {
            TreeNode node = q.poll();
            TreeNode temp = node.left;
            node.left = node.right;
            node.right = temp;
            if (node.left != null) q.offer(node.left);
            if (node.right != null) q.offer(node.right);
        }
        return root;
    }
}
```

**复杂度**：时间 O(n)；空间递归 O(h)，BFS O(n)。
