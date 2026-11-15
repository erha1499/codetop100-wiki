---
rank: 77
id: "179"
title: 最大数
difficulty: 中等
tags: [排序, 字符串, 贪心]
freq: 85
link: https://leetcode.cn/problems/largest-number/
desc: 把一组非负整数重新排列，拼成一个最大的数，以字符串返回。
---
## 思路

- 全部转成字符串后**自定义排序**：比较的不是 `a` 和 `b` 本身，而是两种拼法 `a + b` 和 `b + a` 谁大——`a + b` 更大就让 `a` 排前面。
- 排完直接拼接。
- 不能用普通的字符串降序：`"3"` 和 `"30"`，降序会把 `"30"` 放前面得到 `303`，但 `330` 更大。

## 易错点

- 比较器方向：Java 写 `(b + a).compareTo(a + b)` 是「拼起来大的在前」；写反就成了最小数。
- 全是 0 时排序后第一个是 `"0"`，直接返回 `"0"`，否则会得到 `"000"`。
- 结果可能远超 `long`，全程用字符串。

## 代码

```python
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def cmp(a, b):                       # 相当于 Java 的 (b + a).compareTo(a + b)
            if a + b > b + a:
                return -1                    # a 排前面
            if a + b < b + a:
                return 1
            return 0

        strs = sorted(map(str, nums), key=cmp_to_key(cmp))
        return "0" if strs[0] == "0" else "".join(strs)
```

```java
class Solution {
    public String largestNumber(int[] nums) {
        String[] strs = new String[nums.length];
        for (int i = 0; i < nums.length; i++) {
            strs[i] = String.valueOf(nums[i]);
        }
        Arrays.sort(strs, (a, b) -> (b + a).compareTo(a + b));   // 拼起来大的排前面
        if (strs[0].equals("0")) return "0";
        StringBuilder sb = new StringBuilder();
        for (String s : strs) sb.append(s);
        return sb.toString();
    }
}
```

**复杂度**：时间 O(n log n)（每次比较 O(位数)），空间 O(n)。
