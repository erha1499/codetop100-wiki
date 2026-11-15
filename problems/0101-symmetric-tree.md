---
rank: 69
id: "101"
title: 对称二叉树
difficulty: 简单
tags: [二叉树, DFS, BFS]
freq: 97
link: https://leetcode.cn/problems/symmetric-tree/
desc: 判断二叉树是否轴对称（左右子树互为镜像）。
---
## 思路

- 问题转化成：判断两棵树 `l`、`r` 是否互为**镜像**——根的值相等，且 `l.left ↔ r.right`、`l.right ↔ r.left` 分别互为镜像。
- **递归**：`check(l, r)`。两个都空 → true；只有一个空或值不等 → false；否则递归比较外侧一对和内侧一对。
- **迭代**：队列里永远成对放「应该互为镜像」的两个节点，每次弹两个出来比较，再按镜像顺序把它们的孩子成对入队。

## 易错点

- 先判「都空」，再判「一个空或值不等」，顺序反了会空指针。
- 迭代入队顺序：`u.left` 配 `v.right`，`u.right` 配 `v.left`。
- 迭代要把 `null` 也入队：Java 的 `ArrayDeque` **不允许放 null**，这里要用 `LinkedList`。

## 代码

### 写法一：递归

```python
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check(l, r):                     # l 和 r 是否互为镜像
            if not l and not r:
                return True
            if not l or not r or l.val != r.val:
                return False
            return check(l.left, r.right) and check(l.right, r.left)

        return check(root.left, root.right)
```

```java
class Solution {
    public boolean isSymmetric(TreeNode root) {
        return check(root.left, root.right);
    }

    // l 和 r 是否互为镜像
    private boolean check(TreeNode l, TreeNode r) {
        if (l == null && r == null) return true;
        if (l == null || r == null || l.val != r.val) return false;
        return check(l.left, r.right) && check(l.right, r.left);
    }
}
```

### 写法二：迭代

```python
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        q = deque([(root.left, root.right)])         # 成对存放应互为镜像的节点
        while q:
            u, v = q.popleft()
            if not u and not v:
                continue
            if not u or not v or u.val != v.val:
                return False
            q.append((u.left, v.right))
            q.append((u.right, v.left))
        return True
```

```java
class Solution {
    public boolean isSymmetric(TreeNode root) {
        Queue<TreeNode> q = new LinkedList<>();      // 要放 null，不能用 ArrayDeque
        q.offer(root.left);
        q.offer(root.right);
        while (!q.isEmpty()) {
            TreeNode u = q.poll(), v = q.poll();     // 成对取出应互为镜像的节点
            if (u == null && v == null) continue;
            if (u == null || v == null || u.val != v.val) return false;
            q.offer(u.left);
            q.offer(v.right);
            q.offer(u.right);
            q.offer(v.left);
        }
        return true;
    }
}
```

**复杂度**：时间 O(n)，空间 O(n)。
