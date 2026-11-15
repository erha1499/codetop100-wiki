---
rank: 58
id: "78"
title: 子集
difficulty: 中等
tags: [回溯]
freq: 108
link: https://leetcode.cn/problems/subsets/
desc: 返回不含重复元素的数组的所有子集。
---
## 思路

- 回溯树上的**每个节点都是一个答案**：进入递归时就把当前 `path` 记下来，不用等到叶子。
- `start` 控制只往后选，避免回头选出重复的组合（`[1,2]` 和 `[2,1]`）。
- 循环里还是三步：选 `nums[i]` → 递归 `i + 1` → 撤销。

## 易错点

- 收集答案要拷贝 `path`。
- 递归传 `i + 1` 不是 `start + 1`。
- Java 里 `List` 接口（Java 21 之前）没有 `removeLast()`：要么声明成 `LinkedList`，要么写 `path.remove(path.size() - 1)`。

## 代码

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, path = [], []

        def dfs(start):
            res.append(path[:])              # 每个节点都是答案
            for i in range(start, len(nums)):
                path.append(nums[i])
                dfs(i + 1)
                path.pop()

        dfs(0)
        return res
```

```java
class Solution {
    private final List<List<Integer>> res = new ArrayList<>();
    private final LinkedList<Integer> path = new LinkedList<>();

    public List<List<Integer>> subsets(int[] nums) {
        dfs(nums, 0);
        return res;
    }

    private void dfs(int[] nums, int start) {
        res.add(new ArrayList<>(path));      // 每个节点都是答案
        for (int i = start; i < nums.length; i++) {
            path.add(nums[i]);
            dfs(nums, i + 1);
            path.removeLast();
        }
    }
}
```

**复杂度**：时间 O(n · 2ⁿ)，空间 O(n)（不计答案）。
