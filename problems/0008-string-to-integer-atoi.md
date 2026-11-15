---
rank: 54
id: "8"
title: 字符串转换整数 (atoi)
difficulty: 中等
tags: [字符串, 模拟]
freq: 134
link: https://leetcode.cn/problems/string-to-integer-atoi/
desc: 实现 atoi：把字符串转成 32 位有符号整数，处理空格、符号、非数字截断和溢出。
---
## 思路

一个指针从左到右，按固定顺序处理四件事：

1. 跳过前导空格；
2. 读符号（至多一个 `+` 或 `-`）；
3. 读连续的数字，遇到非数字立即停；
4. 溢出时截断到 `[-2³¹, 2³¹ - 1]`。

## 易错点

- 全是空格 / 空串：跳完空格要判越界，返回 0。
- 符号只认一个：`"+-12"` 读完 `+` 后遇到 `-` 不是数字，直接停，结果 0。
- Java 的溢出判断：先记 `last = res`，算完 `res = res * 10 + num` 后如果 `res / 10 != last` 就是溢出了，按符号返回边界值。也可以在乘之前判断 `res > (Integer.MAX_VALUE - num) / 10`。
- Python 整数不会溢出，读完后统一夹到范围内即可。

## 代码

```python
class Solution:
    def myAtoi(self, s: str) -> int:
        n, index = len(s), 0
        while index < n and s[index] == " ":         # 1. 前导空格
            index += 1
        if index == n:
            return 0
        sign = 1
        if s[index] in "+-":                         # 2. 符号
            sign = -1 if s[index] == "-" else 1
            index += 1
        res = 0
        while index < n and "0" <= s[index] <= "9":  # 3. 数字，遇到非数字就停
            res = res * 10 + int(s[index])
            index += 1
        return max(-2 ** 31, min(sign * res, 2 ** 31 - 1))   # 4. 截断
```

```java
class Solution {
    public int myAtoi(String s) {
        int len = s.length(), index = 0;
        while (index < len && s.charAt(index) == ' ') {      // 1. 前导空格
            index++;
        }
        if (index == len) return 0;
        int sign = 1;
        if (s.charAt(index) == '+') {                        // 2. 符号
            index++;
        } else if (s.charAt(index) == '-') {
            sign = -1;
            index++;
        }
        int res = 0;
        while (index < len) {                                // 3. 数字，遇到非数字就停
            char c = s.charAt(index);
            if (c < '0' || c > '9') break;
            int last = res;
            res = res * 10 + (c - '0');
            if (res / 10 != last) {                          // 4. 溢出了，截断
                return sign == 1 ? Integer.MAX_VALUE : Integer.MIN_VALUE;
            }
            index++;
        }
        return sign * res;
    }
}
```

**复杂度**：时间 O(n)，空间 O(1)。
