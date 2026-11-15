---
rank: 34
id: "93"
title: 复原IP地址
difficulty: 中等
tags: [回溯, 字符串]
freq: 188
link: https://leetcode.cn/problems/restore-ip-addresses/
desc: 给一串数字，返回所有可能的合法 IP 地址（四段，每段 0~255，不能有前导 0）。
---
## 思路

- 回溯切四段：每次从位置 `i` 开始切出 1~3 位作为一段放进 `path`，递归切下一段。
- 每段的合法条件：长度 ≤ 3；数值 ≤ 255；不能有前导 0（单独一个 `"0"` 可以）。
- `path` 有 4 段时，只有恰好把字符串用完才是答案。

## 易错点

- 结束条件要同时满足「四段」和「用完整个字符串」，否则会出现 `1.2.3` 或者后面还剩字符的情况。
- 前导 0 的判断：长度大于 1 且首位是 `'0'`。
- 整体长度不在 `[4, 12]` 可以直接返回空。

## 代码

```python
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res, path = [], []
        if not 4 <= len(s) <= 12:
            return res

        def dfs(i):
            if len(path) == 4:
                if i == len(s):                      # 四段且刚好用完
                    res.append(".".join(path))
                return
            for j in range(i, min(i + 3, len(s))):   # 每段最多 3 位
                num = s[i:j + 1]
                if (len(num) > 1 and num[0] == "0") or int(num) > 255:
                    break
                path.append(num)
                dfs(j + 1)
                path.pop()

        dfs(0)
        return res
```

```java
class Solution {
    private final List<String> res = new ArrayList<>();
    private final LinkedList<String> path = new LinkedList<>();

    public List<String> restoreIpAddresses(String s) {
        if (s.length() < 4 || s.length() > 12) return res;
        dfs(s, 0);
        return res;
    }

    private void dfs(String s, int i) {
        if (path.size() == 4) {
            if (i == s.length()) res.add(String.join(".", path));   // 四段且刚好用完
            return;
        }
        for (int j = i; j < s.length() && j < i + 3; j++) {         // 每段最多 3 位
            String num = s.substring(i, j + 1);
            if ((num.length() > 1 && num.charAt(0) == '0') || Integer.parseInt(num) > 255) break;
            path.add(num);
            dfs(s, j + 1);
            path.removeLast();
        }
    }
}
```

**复杂度**：时间 O(3⁴)，最多四层、每层三种切法，接近常数；空间 O(1)（不计答案）。
