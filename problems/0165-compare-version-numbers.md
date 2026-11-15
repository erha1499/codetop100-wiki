---
rank: 39
id: "165"
title: 比较版本号
difficulty: 中等
tags: [字符串, 双指针]
freq: 167
link: https://leetcode.cn/problems/compare-version-numbers/
desc: 比较两个用 . 分隔的版本号：version1 大返回 1，小返回 -1，相等返回 0。
---
## 思路

- **split**：按 `.` 切开，逐段转成整数比较；某个版本号段数不够就当 0。
- **双指针**（不用 split，O(1) 额外空间）：两个指针各自读出一段数字（读到 `.` 或末尾为止，边读边累加成整数），比较后各跳过一个 `.`，继续下一段。

## 易错点

- Java 的 `split` 参数是正则，`.` 要写成 `"\\."`。
- 循环条件是「或」：较长的版本号后面还有段要比（`1.0.1` vs `1`）。
- 转成整数比较，自然忽略前导 0（`1.01` == `1.001`）。

## 代码

### 写法一：split

```python
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1, v2 = version1.split("."), version2.split(".")
        for i in range(max(len(v1), len(v2))):
            num1 = int(v1[i]) if i < len(v1) else 0
            num2 = int(v2[i]) if i < len(v2) else 0
            if num1 != num2:
                return 1 if num1 > num2 else -1
        return 0
```

```java
class Solution {
    public int compareVersion(String version1, String version2) {
        String[] v1 = version1.split("\\."), v2 = version2.split("\\.");
        for (int i = 0; i < v1.length || i < v2.length; i++) {
            int num1 = i < v1.length ? Integer.parseInt(v1[i]) : 0;
            int num2 = i < v2.length ? Integer.parseInt(v2[i]) : 0;
            if (num1 != num2) return num1 > num2 ? 1 : -1;
        }
        return 0;
    }
}
```

### 写法二：双指针

```python
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        m, n = len(version1), len(version2)
        i = j = 0
        while i < m or j < n:
            num1 = 0
            while i < m and version1[i] != ".":
                num1 = num1 * 10 + int(version1[i])
                i += 1
            num2 = 0
            while j < n and version2[j] != ".":
                num2 = num2 * 10 + int(version2[j])
                j += 1
            if num1 != num2:
                return 1 if num1 > num2 else -1
            i += 1                           # 跳过 '.'
            j += 1
        return 0
```

```java
class Solution {
    public int compareVersion(String version1, String version2) {
        int m = version1.length(), n = version2.length();
        int i = 0, j = 0;
        while (i < m || j < n) {
            int num1 = 0;
            while (i < m && version1.charAt(i) != '.') {
                num1 = num1 * 10 + (version1.charAt(i++) - '0');
            }
            int num2 = 0;
            while (j < n && version2.charAt(j) != '.') {
                num2 = num2 * 10 + (version2.charAt(j++) - '0');
            }
            if (num1 != num2) return num1 > num2 ? 1 : -1;
            i++;                             // 跳过 '.'
            j++;
        }
        return 0;
    }
}
```

**复杂度**：时间 O(m + n)；空间 split O(m + n)，双指针 O(1)。
