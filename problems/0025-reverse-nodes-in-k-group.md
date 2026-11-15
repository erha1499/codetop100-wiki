---
rank: 5
id: "25"
title: K 个一组翻转链表
difficulty: 困难
tags: [链表]
freq: 541
link: https://leetcode.cn/problems/reverse-nodes-in-k-group/
desc: 每 k 个节点一组翻转链表，最后不足 k 个的保持原样。
---
## 思路

- 递归：先让 `b` 从 `head` 走 k 步，走不满说明不足 k 个，直接返回 `head`。
- 反转 `[a, b)` 这一组，得到新头 `newHead`；反转后 `a` 变成这组的尾。
- `a.next = reverseKGroup(b, k)` 接上后面递归处理好的部分，返回 `newHead`。
- 「反转 `[a, b)`」就是 [206](#/206) 的迭代写法，把终止条件从 `null` 换成 `b`。

## 易错点

- 先数够 k 个再反转；不足 k 个要原样返回（不是返回 `null`）。
- 反转的是左闭右开 `[a, b)`，循环条件 `cur != b`。
- 递归深度 n/k；要求 O(1) 额外空间时改成迭代：用 `dummy` + 每组的前驱节点 `pre`，逐组「反转 + 接回」。

## 代码

```python
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        a = b = head
        for _ in range(k):                   # b 走到下一组的头；不足 k 个直接返回
            if not b:
                return head
            b = b.next
        new_head = self.reverse(a, b)        # 反转 [a, b)，反转后 a 是这组的尾
        a.next = self.reverseKGroup(b, k)
        return new_head

    def reverse(self, a, b):
        """反转左闭右开区间 [a, b)，返回新头"""
        pre, cur = None, a
        while cur is not b:
            nxt = cur.next
            cur.next = pre
            pre, cur = cur, nxt
        return pre
```

```java
class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        ListNode a = head, b = head;
        for (int i = 0; i < k; i++) {            // b 走到下一组的头；不足 k 个直接返回
            if (b == null) return head;
            b = b.next;
        }
        ListNode newHead = reverse(a, b);        // 反转 [a, b)，反转后 a 是这组的尾
        a.next = reverseKGroup(b, k);
        return newHead;
    }

    // 反转左闭右开区间 [a, b)，返回新头
    private ListNode reverse(ListNode a, ListNode b) {
        ListNode pre = null, cur = a;
        while (cur != b) {
            ListNode nxt = cur.next;
            cur.next = pre;
            pre = cur;
            cur = nxt;
        }
        return pre;
    }
}
```

**复杂度**：时间 O(n)，空间 O(n/k)（递归栈）。
