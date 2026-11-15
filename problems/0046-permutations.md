---
rank: 14
id: "46"
title: 全排列
difficulty: 中等
tags: [回溯]
freq: 306
link: https://leetcode.cn/problems/permutations/
desc: 返回不含重复数字的数组的所有排列。
---
## 思路

- 回溯模板题：每个位置都尝试放一个还没用过的数。
- 三件套：**路径** `path`（已选的数）、**选择列表**（`visited[i]` 为 false 的数）、**结束条件**（`path` 长度等于 n）。
- 框架：`for 选择 in 选择列表: 做选择 → 递归 → 撤销选择`。

## 易错点

- 收集答案时必须拷贝一份 `path`，否则存进去的是同一个引用。
- 撤销选择要成对：`path` 弹出 + `visited` 复位。
- 排列每层都从 0 开始枚举、靠 `visited` 排除；组合 / 子集（[78](#/78)、[39](#/39)）才用 `start`。

## 代码

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, path = [], []
        visited = [False] * len(nums)

        def traverse():
            if len(path) == len(nums):
                res.append(path[:])          # 拷贝
                return
            for i in range(len(nums)):
                if visited[i]:
                    continue
                path.append(nums[i])         # 做选择
                visited[i] = True
                traverse()
                visited[i] = False           # 撤销选择
                path.pop()

        traverse()
        return res
```

```java
class Solution {
    private final List<List<Integer>> res = new ArrayList<>();
    private final LinkedList<Integer> path = new LinkedList<>();
    private boolean[] visited;

    public List<List<Integer>> permute(int[] nums) {
        visited = new boolean[nums.length];
        traverse(nums);
        return res;
    }

    private void traverse(int[] nums) {
        if (path.size() == nums.length) {
            res.add(new ArrayList<>(path));      // 拷贝
            return;
        }
        for (int i = 0; i < nums.length; i++) {
            if (visited[i]) continue;
            path.add(nums[i]);                   // 做选择
            visited[i] = true;
            traverse(nums);
            visited[i] = false;                  // 撤销选择
            path.removeLast();
        }
    }
}
```

**复杂度**：时间 O(n · n!)，空间 O(n)（递归栈 + path + visited，不计答案）。
