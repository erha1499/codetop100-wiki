---
rank: 55
id: "2"
title: 两数相加
difficulty: 中等
tags: [链表, 模拟]
freq: 133
link: https://leetcode.cn/problems/add-two-numbers/
desc: 两个逆序存储数字的链表相加，返回同样逆序存储的和。
---
## 思路

- 链表版竖式加法。逆序存储正好从个位开始，直接从头节点往后加。
- `p1`、`p2` 遍历两个链表，`p` 构造结果，`c` 是进位。每轮 `val = c + p1.val + p2.val`，新节点存 `val % 10`，进位 `val / 10`。
- `dummy` 省去头节点的特判。

## 易错点

- 循环条件是 `p1 != null || p2 != null || c > 0`：两个链表都走完了还可能剩一个进位（`5 + 5 = 10`）。
- 某个链表先走完时不能再取它的 `val`，要判空。

## 代码

```python
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = p = ListNode(-1)
        p1, p2, c = l1, l2, 0
        while p1 or p2 or c:
            val = c
            if p1:
                val += p1.val
                p1 = p1.next
            if p2:
                val += p2.val
                p2 = p2.next
            p.next = ListNode(val % 10)
            p = p.next
            c = val // 10
        return dummy.next
```

```java
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(-1), p = dummy;
        ListNode p1 = l1, p2 = l2;
        int c = 0;
        while (p1 != null || p2 != null || c > 0) {
            int val = c;
            if (p1 != null) {
                val += p1.val;
                p1 = p1.next;
            }
            if (p2 != null) {
                val += p2.val;
                p2 = p2.next;
            }
            p.next = new ListNode(val % 10);
            p = p.next;
            c = val / 10;
        }
        return dummy.next;
    }
}
```

**复杂度**：时间 O(max(m, n))，空间 O(1)（不计答案）。
