---
rank: 46
id: "148"
title: 排序链表
difficulty: 中等
tags: [链表, 排序, 分治]
freq: 149
link: https://leetcode.cn/problems/sort-list/
desc: 把链表按升序排序，要求 O(n log n)。
---
## 思路

- 链表排序用**归并**（快排依赖随机访问，不适合链表）：
  1. 快慢指针找中点；
  2. 从中点断开成两条；
  3. 递归排序左右两条；
  4. 合并两个有序链表（[21](#/21)）。
- 递归出口：空链表或只有一个节点，天然有序。

## 易错点

- `fast` 要从 `head.next` 出发，让 `slow` 停在**偏左**的中点。若 `fast = head`，两个节点时 `slow` 会停在第二个节点，切完左边还是原链表，无限递归。
- 必须 `slow.next = null` 断开。
- 合并完别忘了接上剩余的那段。

## 代码

```python
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        slow, fast = head, head.next         # fast 先走一步，slow 停在偏左的中点
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None                     # 断开
        p1, p2 = self.sortList(head), self.sortList(mid)
        dummy = p = ListNode(-1)             # 合并两个有序链表
        while p1 and p2:
            if p1.val < p2.val:
                p.next = p1
                p1 = p1.next
            else:
                p.next = p2
                p2 = p2.next
            p = p.next
        p.next = p1 or p2
        return dummy.next
```

```java
class Solution {
    public ListNode sortList(ListNode head) {
        if (head == null || head.next == null) return head;
        ListNode slow = head, fast = head.next;      // fast 先走一步，slow 停在偏左的中点
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        ListNode mid = slow.next;
        slow.next = null;                            // 断开
        return mergeTwoLists(sortList(head), sortList(mid));
    }

    private ListNode mergeTwoLists(ListNode p1, ListNode p2) {
        ListNode dummy = new ListNode(-1), p = dummy;
        while (p1 != null && p2 != null) {
            if (p1.val < p2.val) {
                p.next = p1;
                p1 = p1.next;
            } else {
                p.next = p2;
                p2 = p2.next;
            }
            p = p.next;
        }
        p.next = p1 != null ? p1 : p2;
        return dummy.next;
    }
}
```

**复杂度**：时间 O(n log n)，空间 O(log n)（递归栈）。
