---
rank: 33
id: "19"
title: 删除链表的倒数第N个节点
difficulty: 中等
tags: [链表, 双指针]
freq: 190
link: https://leetcode.cn/problems/remove-nth-node-from-end-of-list/
desc: 删除链表的倒数第 n 个节点，返回头节点。
---
## 思路

- 快慢指针 + `dummy`：`fast` 从 `head` 先走 n 步，然后 `slow` 从 `dummy` 出发，两人一起走。
- `fast` 走到 `null` 时，`slow` 正好停在**待删节点的前一个**，`slow.next = slow.next.next` 删掉。

## 易错点

- `slow` 必须从 `dummy` 出发：这样才停在前驱上，也才能统一处理删除头节点的情况。
- 返回 `dummy.next`，不是 `head`（`head` 可能被删了）。

## 代码

```python
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = head
        for _ in range(n):
            fast = fast.next
        slow = dummy
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next           # slow 是待删节点的前一个
        return dummy.next
```

```java
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummy = new ListNode(0, head);
        ListNode fast = head;
        while (n-- > 0) {
            fast = fast.next;
        }
        ListNode slow = dummy;
        while (fast != null) {
            fast = fast.next;
            slow = slow.next;
        }
        slow.next = slow.next.next;          // slow 是待删节点的前一个
        return dummy.next;
    }
}
```

**复杂度**：时间 O(n)，空间 O(1)。
