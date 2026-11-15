---
rank: 47
id: "94"
title: 二叉树的中序遍历
difficulty: 简单
tags: [二叉树, 栈]
freq: 144
link: https://leetcode.cn/problems/binary-tree-inorder-traversal/
desc: 返回二叉树的中序遍历（左 → 根 → 右）。
---
## 思路

- **递归**：`dfs(左)` → 访问当前节点 → `dfs(右)`。
- **迭代（栈模拟递归）**：一路向左把节点压栈；到头后弹出一个节点访问它，然后转向它的右子树，重复。
- **Morris（O(1) 空间）**：不用栈，借用「左子树最右节点」的空右指针记住回来的路。对当前节点 `root`：
  - 没有左子树：访问 `root`，走向右边；
  - 有左子树：找到左子树的最右节点 `pre`（中序前驱）。
    - `pre.right` 为空 → 第一次来：连上 `pre.right = root`，进入左子树；
    - `pre.right == root` → 第二次回来，左子树已经走完：拆掉线索，访问 `root`，走向右边。

## 易错点

- 迭代的循环条件是 `root != null || 栈非空`，必须是「或」：`root` 为空时栈里可能还有节点；栈空时 `root` 可能还带着右子树。
- Morris 找前驱时循环条件要带上 `pre.right != root`，否则顺着线索绕圈。

## 代码

### 写法一：递归

```python
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)

        dfs(root)
        return res
```

```java
class Solution {
    private final List<Integer> res = new ArrayList<>();

    public List<Integer> inorderTraversal(TreeNode root) {
        if (root == null) return res;
        inorderTraversal(root.left);
        res.add(root.val);
        inorderTraversal(root.right);
        return res;
    }
}
```

### 写法二：迭代

```python
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res, stk = [], []
        while root or stk:
            while root:                      # 一路向左压栈
                stk.append(root)
                root = root.left
            root = stk.pop()
            res.append(root.val)
            root = root.right                # 转向右子树
        return res
```

```java
class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        Deque<TreeNode> stk = new ArrayDeque<>();
        while (root != null || !stk.isEmpty()) {
            while (root != null) {           // 一路向左压栈
                stk.push(root);
                root = root.left;
            }
            root = stk.pop();
            res.add(root.val);
            root = root.right;               // 转向右子树
        }
        return res;
    }
}
```

### 写法三：Morris

```python
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        while root:
            if root.left:
                pre = root.left              # 找中序前驱：左子树的最右节点
                while pre.right and pre.right is not root:
                    pre = pre.right
                if not pre.right:            # 第一次来：建线索，进左子树
                    pre.right = root
                    root = root.left
                    continue
                pre.right = None             # 第二次回来：拆线索
            res.append(root.val)
            root = root.right
        return res
```

```java
class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        while (root != null) {
            if (root.left != null) {
                TreeNode pre = root.left;            // 找中序前驱：左子树的最右节点
                while (pre.right != null && pre.right != root) {
                    pre = pre.right;
                }
                if (pre.right == null) {             // 第一次来：建线索，进左子树
                    pre.right = root;
                    root = root.left;
                    continue;
                }
                pre.right = null;                    // 第二次回来：拆线索
            }
            res.add(root.val);
            root = root.right;
        }
        return res;
    }
}
```

**复杂度**：时间都是 O(n)；空间递归 / 迭代 O(h)，Morris O(1)。
