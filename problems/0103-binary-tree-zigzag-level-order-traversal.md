---
rank: 21
id: "103"
title: 二叉树的锯齿形层次遍历
difficulty: 中等
tags: [二叉树, BFS]
freq: 272
link: https://leetcode.cn/problems/binary-tree-zigzag-level-order-traversal/
desc: 层序遍历二叉树，但每层交替方向：先从左到右，下一层从右到左。
---
## 思路

- 还是 [102](#/102) 的层序遍历模板，只是**每层决定往结果里插入的方向**。
- 用 `flag` 记录方向：从左往右 → 尾插；从右往左 → 头插。每层结束 `flag` 取反。
- 入队顺序不用变，始终左孩子先、右孩子后，锯齿只体现在这一层的值怎么放。

## 易错点

- 头插需要双端结构：Java 把每层声明成 `LinkedList<Integer>` 才有 `addFirst`；Python 用 `deque.appendleft`。
- `flag` 每层翻一次，不是每个节点翻一次。

## 代码

```python
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res, q, flag = [], deque([root]), False
        while q:
            level = deque()
            for _ in range(len(q)):
                cur = q.popleft()
                if flag:
                    level.appendleft(cur.val)    # 从右往左：头插
                else:
                    level.append(cur.val)        # 从左往右：尾插
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            res.append(list(level))
            flag = not flag
        return res
```

```java
class Solution {
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<>();
        if (root == null) return res;
        Deque<TreeNode> q = new ArrayDeque<>();
        q.offer(root);
        boolean flag = false;
        while (!q.isEmpty()) {
            int sz = q.size();
            LinkedList<Integer> level = new LinkedList<>();
            for (int i = 0; i < sz; i++) {
                TreeNode cur = q.poll();
                if (flag) level.addFirst(cur.val);   // 从右往左：头插
                else level.addLast(cur.val);         // 从左往右：尾插
                if (cur.left != null) q.offer(cur.left);
                if (cur.right != null) q.offer(cur.right);
            }
            res.add(level);
            flag = !flag;
        }
        return res;
    }
}
```

**复杂度**：时间 O(n)，空间 O(n)。
