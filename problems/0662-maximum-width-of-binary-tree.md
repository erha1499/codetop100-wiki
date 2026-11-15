---
rank: 82
id: "662"
title: 二叉树最大宽度
difficulty: 中等
tags: [二叉树, BFS, DFS]
freq: 84
link: https://leetcode.cn/problems/maximum-width-of-binary-tree/
desc: 求二叉树的最大宽度：每层最左和最右非空节点之间的长度，中间的空位也算。
---
## 思路

- 关键在**编号**：按满二叉树给节点编号，节点 `code` 的左孩子是 `2 * code`、右孩子是 `2 * code + 1`。同一层的宽度 = `最右编号 - 最左编号 + 1`，中间缺的节点自然被算进去。
- **BFS**：队列里带着编号做层序遍历，每层用队头、队尾的编号算宽度。
- **DFS**：带着 `depth` 和 `code` 先左后右遍历，用哈希表记每层第一次遇到的编号（就是该层最左节点），每到一个节点用 `code - minCode[depth] + 1` 更新答案。

## 易错点

- 宽度不是这一层的节点个数。
- 编号每层翻倍，树深了会超出 `int` / `long`：BFS 里把每层的编号都减去该层起点再往下传，就不会一直变大。（Java 即使溢出，同层编号相减的结果仍然正确，因为答案保证在 int 范围内。）
- DFS 必须先左后右，否则每层第一次遇到的不是最左节点。

## 代码

### 写法一：BFS

```python
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res, q = 0, deque([(root, 0)])       # (节点, 编号)
        while q:
            start = q[0][1]
            res = max(res, q[-1][1] - start + 1)
            for _ in range(len(q)):
                node, code = q.popleft()
                code -= start                # 减去本层起点，防止编号越来越大
                if node.left:
                    q.append((node.left, code * 2))
                if node.right:
                    q.append((node.right, code * 2 + 1))
        return res
```

```java
class Solution {
    public int widthOfBinaryTree(TreeNode root) {
        int res = 0;
        Deque<TreeNode> q = new ArrayDeque<>();
        Deque<Integer> codes = new ArrayDeque<>();       // 与 q 同步进出，存节点编号
        q.offer(root);
        codes.offer(0);
        while (!q.isEmpty()) {
            int sz = q.size(), start = codes.peekFirst();
            res = Math.max(res, codes.peekLast() - start + 1);
            for (int i = 0; i < sz; i++) {
                TreeNode cur = q.poll();
                int code = codes.poll() - start;         // 减去本层起点，防止编号越来越大
                if (cur.left != null) {
                    q.offer(cur.left);
                    codes.offer(code * 2);
                }
                if (cur.right != null) {
                    q.offer(cur.right);
                    codes.offer(code * 2 + 1);
                }
            }
        }
        return res;
    }
}
```

### 写法二：DFS

```python
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        min_code = {}                        # depth -> 该层最左节点的编号

        def dfs(node, code, depth):
            nonlocal res
            if not node:
                return
            if depth not in min_code:        # 先左后右，第一次到这层的就是最左节点
                min_code[depth] = code
            res = max(res, code - min_code[depth] + 1)
            dfs(node.left, code * 2, depth + 1)
            dfs(node.right, code * 2 + 1, depth + 1)

        dfs(root, 1, 0)
        return res
```

```java
class Solution {
    private int res = 0;
    private final Map<Integer, Integer> minCode = new HashMap<>();   // depth -> 该层最左节点的编号

    public int widthOfBinaryTree(TreeNode root) {
        dfs(root, 1, 0);
        return res;
    }

    private void dfs(TreeNode node, int code, int depth) {
        if (node == null) return;
        minCode.putIfAbsent(depth, code);                // 先左后右，第一次到这层的就是最左节点
        res = Math.max(res, code - minCode.get(depth) + 1);
        dfs(node.left, code * 2, depth + 1);
        dfs(node.right, code * 2 + 1, depth + 1);
    }
}
```

**复杂度**：时间 O(n)，空间 O(n)。
