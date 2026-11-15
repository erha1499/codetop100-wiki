---
rank: 53
id: "43"
title: 字符串相乘
difficulty: 中等
tags: [字符串, 模拟]
freq: 134
link: https://leetcode.cn/problems/multiply-strings/
desc: 两个用字符串表示的非负整数相乘，返回字符串形式的积（不能直接转成整数）。
---
## 思路

- 模拟竖式乘法。`m` 位 × `n` 位，结果最多 `m + n` 位，用 `int[m + n]` 存每一位。
- `num1[i] * num2[j]` 的结果落在两个位置：低位 `res[i + j + 1]`，进位 `res[i + j]`。
- 从低位往高位两层循环，每次 `mul = n1 * n2 + res[i + j + 1]`（加上这个位置已有的值），个位留在 `res[i + j + 1]`，十位累加到 `res[i + j]`。
- 最后跳过前导 0 拼成字符串。

## 易错点

- 数组长度是 `m + n`，不是 `m + n - 1`（`99 * 99 = 9801`）。
- `mul` 要加上当前位置的旧值；进位是 `+=` 不是 `=`。
- 结果全是 0（有一个乘数是 `"0"`）时返回 `"0"`，不是空串。

## 代码

```python
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m, n = len(num1), len(num2)
        res = [0] * (m + n)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j]) + res[i + j + 1]
                res[i + j + 1] = mul % 10    # 个位留下
                res[i + j] += mul // 10      # 进位累加到高一位
        s = "".join(map(str, res)).lstrip("0")
        return s or "0"
```

```java
class Solution {
    public String multiply(String num1, String num2) {
        int m = num1.length(), n = num2.length();
        int[] res = new int[m + n];
        for (int i = m - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                int mul = (num1.charAt(i) - '0') * (num2.charAt(j) - '0') + res[i + j + 1];
                res[i + j + 1] = mul % 10;   // 个位留下
                res[i + j] += mul / 10;      // 进位累加到高一位
            }
        }
        StringBuilder sb = new StringBuilder();
        int k = 0;
        while (k < res.length && res[k] == 0) k++;   // 跳过前导 0
        for (; k < res.length; k++) sb.append(res[k]);
        return sb.length() == 0 ? "0" : sb.toString();
    }
}
```

**复杂度**：时间 O(mn)，空间 O(m + n)。
