---
rank: 28
id: "415"
title: 字符串相加
difficulty: 简单
tags: [字符串, 模拟]
freq: 246
link: https://leetcode.cn/problems/add-strings/
desc: 两个用字符串表示的非负整数相加，返回字符串形式的和（不能直接转成整数）。
---
## 思路

- 模拟竖式加法：两个指针从两个字符串末尾往前走，每位算 `n1 + n2 + 进位`，个位留下、十位进位。
- 某个字符串走完了就当它这一位是 0，统一逻辑。
- 结果是从低位到高位追加的，最后反转。
- 同套路：[2 两数相加](#/2)、[43 字符串相乘](#/43)。

## 易错点

- 最后的进位别漏（`"999" + "1"`）：把 `c > 0` 也放进循环条件最省事。
- 字符转数字：Java 是 `ch - '0'`。

## 代码

```python
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j, c = len(num1) - 1, len(num2) - 1, 0
        res = []
        while i >= 0 or j >= 0 or c:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0
            c, n = divmod(n1 + n2 + c, 10)
            res.append(str(n))
            i -= 1
            j -= 1
        return "".join(reversed(res))
```

```java
class Solution {
    public String addStrings(String num1, String num2) {
        StringBuilder res = new StringBuilder();
        int i = num1.length() - 1, j = num2.length() - 1, c = 0;
        while (i >= 0 || j >= 0 || c > 0) {
            int n1 = i >= 0 ? num1.charAt(i) - '0' : 0;
            int n2 = j >= 0 ? num2.charAt(j) - '0' : 0;
            int sum = n1 + n2 + c;
            res.append(sum % 10);
            c = sum / 10;
            i--;
            j--;
        }
        return res.reverse().toString();
    }
}
```

**复杂度**：时间 O(max(m, n))，空间 O(1)（不计答案）。
