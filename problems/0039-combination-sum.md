---
rank: 70
id: "39"
title: 组合总和
difficulty: 中等
tags: [回溯]
freq: 96
link: https://leetcode.cn/problems/combination-sum/
desc: 从无重复元素的数组中选数（每个数可重复选），返回所有和为 target 的组合。
---
## 思路

- 回溯枚举组合：`path` 是当前组合，`target` 是还差多少，`start` 控制只往后选（避免 `[2,3]` 和 `[3,2]` 重复）。
- **可以重复选**：递归时传 `i` 而不是 `i + 1`，下一层还能再选当前这个数。
- `target == 0` 时收集答案。
- 剪枝：先排序，一旦 `target - num < 0`，后面的数更大，直接 `break`。

## 易错点

- 传 `i` 还是 `i + 1` 是这题和「每个数只能用一次」（40 组合总和 II）的唯一区别。
- 没排序时只能 `continue`，排了序才能 `break`。
- 收集答案要拷贝 `path`。

## 代码

```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res, path = [], []

        def dfs(target, start):
            if target == 0:
                res.append(path[:])
                return
            for i in range(start, len(candidates)):
                num = candidates[i]
                if target - num < 0:         # 已排序，后面的更大
                    break
                path.append(num)
                dfs(target - num, i)         # 传 i：当前数可以重复选
                path.pop()

        dfs(target, 0)
        return res
```

```java
class Solution {
    private final List<List<Integer>> res = new ArrayList<>();
    private final LinkedList<Integer> path = new LinkedList<>();

    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        Arrays.sort(candidates);
        dfs(candidates, target, 0);
        return res;
    }

    private void dfs(int[] candidates, int target, int start) {
        if (target == 0) {
            res.add(new ArrayList<>(path));
            return;
        }
        for (int i = start; i < candidates.length; i++) {
            int num = candidates[i];
            if (target - num < 0) break;             // 已排序，后面的更大
            path.add(num);
            dfs(candidates, target - num, i);        // 传 i：当前数可以重复选
            path.removeLast();
        }
    }
}
```

**复杂度**：时间上界 O(n^(target/min))，实际远小于此；空间 O(target/min)（递归深度）。
