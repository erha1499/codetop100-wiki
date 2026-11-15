---
rank: 87
id: "113"
title: 路径总和 II
difficulty: 中等
tags: [二叉树, 回溯]
freq: 78
link: https://leetcode.cn/problems/path-sum-ii/
desc: 找出所有从根到叶子、节点值之和等于 targetSum 的路径。
---
## 思路

- DFS + 回溯：`path` 记录当前从根走下来的路径，`dfs(node, s)` 表示走到 `node` 之前路径和是 `s`。
- 进入节点：加进 `path`，累加和；如果是**叶子**且和等于目标，把 `path` 的拷贝存入结果。
- 递归左右子树；离开节点前把它从 `path` 里移除。

## 易错点

- 必须是根到**叶子**：和够了还要判断左右孩子都为空。
- 存结果要拷贝 `path`。
- 回溯不能忘。到叶子记录答案后不要提前 `return`，否则跳过了下面的移除，路径会乱。
- 节点值可能为负，不能因为和已经超过目标就剪枝。

## 代码

```python
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res, path = [], []

        def dfs(node, s):
            if not node:
                return
            s += node.val
            path.append(node.val)
            if s == targetSum and not node.left and not node.right:
                res.append(path[:])
            dfs(node.left, s)
            dfs(node.right, s)
            path.pop()                       # 回溯

        dfs(root, 0)
        return res
```

```java
class Solution {
    private final List<List<Integer>> res = new ArrayList<>();
    private final LinkedList<Integer> path = new LinkedList<>();

    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        dfs(root, 0, targetSum);
        return res;
    }

    private void dfs(TreeNode node, int s, int targetSum) {
        if (node == null) return;
        int sum = s + node.val;
        path.add(node.val);
        if (sum == targetSum && node.left == null && node.right == null) {
            res.add(new ArrayList<>(path));
        }
        dfs(node.left, sum, targetSum);
        dfs(node.right, sum, targetSum);
        path.removeLast();                   // 回溯
    }
}
```

**复杂度**：时间 O(n²)（最坏每条路径拷贝一次），空间 O(h)（不计答案）。
