---
rank: 22
id: "92"
title: 反转链表 II
difficulty: 中等
tags: [链表]
freq: 271
link: https://leetcode.cn/problems/reverse-linked-list-ii/
desc: 反转链表中第 left 到第 right 个节点（位置从 1 开始），返回头节点。
---
## 思路

- 三步：找到反转区间的前驱 `pre` → 用「反转前 n 个节点」的模板反转 → 接回去。
- `reverseN(head, n)`：三指针反转前 n 个；循环结束时 `cur` 正好是第 n+1 个节点，`head.next = cur` 就把反转后的尾（原来的头）接上了后面。
- `pre.next = reverseN(pre.next, right - left + 1)` 接上前面。

## 易错点

- `left == 1` 时头节点会变：用 `dummy` 统一处理，`pre` 从 `dummy` 出发走 `left - 1` 步。
- `reverseN` 里 `head.next = cur` 这句是核心，漏了后半段就丢了。

## 代码

```python
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        pre = dummy
        for _ in range(left - 1):            # pre 停在第 left 个节点的前一个
            pre = pre.next
        pre.next = self.reverseN(pre.next, right - left + 1)
        return dummy.next

    def reverseN(self, head, n):
        """反转以 head 开头的前 n 个节点，返回新头，并接好后面的部分"""
        pre, cur = None, head
        for _ in range(n):
            nxt = cur.next
            cur.next = pre
            pre, cur = cur, nxt
        head.next = cur                      # 原头变成尾，接上第 n+1 个节点
        return pre
```

```java
class Solution {
    public ListNode reverseBetween(ListNode head, int left, int right) {
        ListNode dummy = new ListNode(-1, head), pre = dummy;
        for (int i = 1; i < left; i++) {         // pre 停在第 left 个节点的前一个
            pre = pre.next;
        }
        pre.next = reverseN(pre.next, right - left + 1);
        return dummy.next;
    }

    // 反转以 head 开头的前 n 个节点，返回新头，并接好后面的部分
    private ListNode reverseN(ListNode head, int n) {
        ListNode pre = null, cur = head;
        while (n-- > 0) {
            ListNode nxt = cur.next;
            cur.next = pre;
            pre = cur;
            cur = nxt;
        }
        head.next = cur;                         // 原头变成尾，接上第 n+1 个节点
        return pre;
    }
}
```

**复杂度**：时间 O(n)，空间 O(1)。
