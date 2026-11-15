---
rank: 3
id: "206"
title: 反转链表
difficulty: 简单
tags: [链表]
freq: 762
link: https://leetcode.cn/problems/reverse-linked-list/
desc: 反转单链表，返回新的头节点。
---
## 思路

- **迭代**：`pre / cur / nxt` 三指针滚动，每轮只做一件事——把 `cur.next` 指向 `pre`，然后整体后移。
- **递归**：先反转后面的链表拿到新头 `last`，再把当前节点接到尾部：`head.next.next = head; head.next = null`。

## 易错点

- 迭代必须先存 `nxt` 再改指针，否则断链；最后返回 `pre`（此时 `cur` 为空）。
- 递归别忘了 `head.next = null`，否则头两个节点成环。

## 代码

### 迭代

```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre, cur = None, head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre, cur = cur, nxt
        return pre
```

```java
class Solution {
    public ListNode reverseList(ListNode head) {
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

### 递归

```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        last = self.reverseList(head.next)   # last 始终是反转后的新头
        head.next.next = head
        head.next = None
        return last
```

```java
class Solution {
    public ListNode reverseList(ListNode head) {
        if (head == null || head.next == null) return head;
        ListNode last = reverseList(head.next);   // last 始终是反转后的新头
        head.next.next = head;
        head.next = null;
        return last;
    }
}
```

**复杂度**：时间 O(n)；空间迭代 O(1)，递归 O(n)（栈）。
