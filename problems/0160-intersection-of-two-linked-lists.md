---
rank: 31
id: "160"
title: 相交链表
difficulty: 简单
tags: [链表, 双指针]
freq: 203
link: https://leetcode.cn/problems/intersection-of-two-linked-lists/
desc: 找出两个单链表相交的起始节点，不相交返回 null。
---
## 思路

- 双指针同时出发：`p1` 走 A，`p2` 走 B；走到末尾后分别跳到对方的头继续走。
- 两人走过的总路程都是 `A独有 + 公共 + B独有`，所以会同时到达相交点。
- 不相交时，两人各走 `m + n` 步后同时变成 `null`，循环一样结束，返回 `null`。

## 易错点

- 比较的是节点引用（`p1 == p2`），不是节点值。
- 切换条件是「`p1` 自己为空」时跳到对方头，不是 `p1.next` 为空——否则不相交时死循环。

## 代码

```python
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p1, p2 = headA, headB
        while p1 is not p2:
            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA
        return p1
```

```java
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        ListNode p1 = headA, p2 = headB;
        while (p1 != p2) {
            p1 = p1 == null ? headB : p1.next;
            p2 = p2 == null ? headA : p2.next;
        }
        return p1;
    }
}
```

**复杂度**：时间 O(m + n)，空间 O(1)。
