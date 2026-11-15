---
rank: 43
id: "22"
title: 括号生成
difficulty: 中等
tags: [回溯, 字符串]
freq: 152
link: https://leetcode.cn/problems/generate-parentheses/
desc: 生成 n 对括号的所有有效组合。
---
## 思路

- 回溯 + 剪枝。`l`、`r` 是**还剩**多少个左、右括号可用，`path` 是当前拼出来的串。
- 每一步两个选择：放 `(`（`l - 1`）或放 `)`（`r - 1`）。
- 剪枝：
  - `l < 0 || r < 0`：用超了；
  - `l > r`：剩下的左括号比右括号多，说明已经放的右括号比左括号多，后面怎么补都不合法。
- `l == 0 && r == 0` 时收集答案。有了 `l > r` 的剪枝，生成的一定合法，不用再校验。

## 易错点

- `l > r` 是按「剩余数量」说的；如果变量记的是「已用数量」，条件要反过来（已用右括号 > 已用左括号）。
- Java 用 `StringBuilder` 做 `path`，撤销选择是 `deleteCharAt(path.length() - 1)`。

## 代码

```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, path = [], []

        def dfs(l, r):                       # l、r：剩余的左、右括号数
            if l < 0 or r < 0 or l > r:
                return
            if l == 0 and r == 0:
                res.append("".join(path))
                return
            path.append("(")
            dfs(l - 1, r)
            path.pop()
            path.append(")")
            dfs(l, r - 1)
            path.pop()

        dfs(n, n)
        return res
```

```java
class Solution {
    private final List<String> res = new ArrayList<>();
    private final StringBuilder path = new StringBuilder();

    public List<String> generateParenthesis(int n) {
        dfs(n, n);
        return res;
    }

    // l、r：剩余的左、右括号数
    private void dfs(int l, int r) {
        if (l < 0 || r < 0 || l > r) return;
        if (l == 0 && r == 0) {
            res.add(path.toString());
            return;
        }
        path.append('(');
        dfs(l - 1, r);
        path.deleteCharAt(path.length() - 1);
        path.append(')');
        dfs(l, r - 1);
        path.deleteCharAt(path.length() - 1);
    }
}
```

**复杂度**：时间 O(4ⁿ / √n)（卡特兰数），空间 O(n)（不计答案）。
