---
rank: 25
id: "143"
title: 重排链表
difficulty: 中等
tags: [链表, 双指针]
freq: 259
link: https://leetcode.cn/problems/reorder-list/
desc: 把链表 L0→L1→…→Ln 原地重排成 L0→Ln→L1→Ln-1→…。
---
## 思路

三个链表模板的组合：

1. **快慢指针找中点**：`slow` 停在前半段的最后一个节点，从这里断开成两条。
2. **反转后半段**（[206](#/206)）。
3. **交替合并**：前半段取一个、后半段取一个。

## 易错点

- 找中点的循环条件用 `fast.next != null && fast.next.next != null`，这样 `slow` 停在前半段末尾（前半段长度 ≥ 后半段）。
- 一定要 `slow.next = null` 断开，否则合并时成环。
- 合并时先存两边的 `next` 再改指针。

## 代码

```python
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast.next and fast.next.next:          # slow 停在前半段最后一个
            slow, fast = slow.next, fast.next.next
        l2 = self.reverseList(slow.next)
        slow.next = None                             # 断开
        l1 = head
        while l1 and l2:                             # 交替合并
            p1, p2 = l1.next, l2.next
            l1.next = l2
            l2.next = p1
            l1, l2 = p1, p2

    def reverseList(self, head):
        pre, cur = None, head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre, cur = cur, nxt
        return pre
```

```java
class Solution {
    public void reorderList(ListNode head) {
        ListNode slow = head, fast = head;
        while (fast.next != null && fast.next.next != null) {   // slow 停在前半段最后一个
            slow = slow.next;
            fast = fast.next.next;
        }
        ListNode l1 = head, l2 = reverseList(slow.next);
        slow.next = null;                                       // 断开
        while (l1 != null && l2 != null) {                      // 交替合并
            ListNode p1 = l1.next, p2 = l2.next;
            l1.next = l2;
            l2.next = p1;
            l1 = p1;
            l2 = p2;
        }
    }

    private ListNode reverseList(ListNode head) {
        ListNode pre = null, cur = head;
        while (cur != null) {
            ListNode nxt = cur.next;
            cur.next = pre;
            pre = cur;
            cur = nxt;
        }
        return pre;
    }
}
```

**复杂度**：时间 O(n)，空间 O(1)。
