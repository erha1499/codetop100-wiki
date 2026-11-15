---
rank: 76
id: "234"
title: 回文链表
difficulty: 简单
tags: [链表, 双指针]
freq: 88
link: https://leetcode.cn/problems/palindrome-linked-list/
desc: 判断单链表是否是回文链表。
---
## 思路

和 [143 重排链表](#/143) 同一套组合：

1. 快慢指针找中点（`slow` 停在前半段最后一个节点）；
2. 反转后半段；
3. 两个指针分别从头和反转后的后半段出发，逐个比较。

## 易错点

- `fast` 从 `head.next` 出发：奇数长度时 `slow` 停在正中间，偶数长度时停在前半段末尾，两种情况都从 `slow.next` 开始反转。
- 后半段长度 ≤ 前半段（奇数时中间节点留在前半段，不用比），所以比到 `p2` 走完为止。
- 面试可能会追问「恢复原链表」：比完后把后半段再反转一次接回去。

## 代码

```python
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head.next
        while fast and fast.next:            # slow 停在前半段最后一个
            slow = slow.next
            fast = fast.next.next
        p1, p2 = head, self.reverse(slow.next)
        slow.next = None
        while p2:                            # 后半段不比前半段长
            if p1.val != p2.val:
                return False
            p1, p2 = p1.next, p2.next
        return True

    def reverse(self, head):
        pre, cur = None, head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre, cur = cur, nxt
        return pre
```

```java
class Solution {
    public boolean isPalindrome(ListNode head) {
        ListNode slow = head, fast = head.next;
        while (fast != null && fast.next != null) {      // slow 停在前半段最后一个
            slow = slow.next;
            fast = fast.next.next;
        }
        ListNode p1 = head, p2 = reverse(slow.next);
        slow.next = null;
        while (p2 != null) {                             // 后半段不比前半段长
            if (p1.val != p2.val) return false;
            p1 = p1.next;
            p2 = p2.next;
        }
        return true;
    }

    private ListNode reverse(ListNode head) {
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
