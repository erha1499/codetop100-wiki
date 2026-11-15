---
rank: 12
id: "102"
title: 二叉树的层序遍历
difficulty: 中等
tags: [二叉树, BFS]
freq: 334
link: https://leetcode.cn/problems/binary-tree-level-order-traversal/
desc: 按层从左到右输出二叉树的节点值，每层一个列表。
---
## 思路

- 层序遍历 = **BFS + 队列**。
- 每轮先记下当前队列大小 `sz`，只处理这 `sz` 个节点——正好是一整层；处理时把左右孩子入队。
- 这个模板直接套：[103 锯齿形](#/103)、[199 右视图](#/199)、[662 最大宽度](#/662)、107、637、994。

## 易错点

- `sz` 必须在 for 循环前取：循环里孩子入队后 `q.size()` 会变。
- 空树直接返回空列表。

## 代码

```python
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res, q = [], deque([root])
        while q:
            level = []
            for _ in range(len(q)):          # 当前层的节点数
                cur = q.popleft()
                level.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            res.append(level)
        return res
```

```java
class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<>();
        if (root == null) return res;
        Deque<TreeNode> q = new ArrayDeque<>();
        q.offer(root);
        while (!q.isEmpty()) {
            int sz = q.size();                   // 当前层的节点数
            List<Integer> level = new ArrayList<>();
            for (int i = 0; i < sz; i++) {
                TreeNode cur = q.poll();
                level.add(cur.val);
                if (cur.left != null) q.offer(cur.left);
                if (cur.right != null) q.offer(cur.right);
            }
            res.add(level);
        }
        return res;
    }
}
```

**复杂度**：时间 O(n)，空间 O(n)。
