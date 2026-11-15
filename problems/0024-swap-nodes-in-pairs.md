---
rank: 91
id: "24"
title: 两两交换链表中的节点
difficulty: 中等
tags: [链表]
freq: 73
link: https://leetcode.cn/problems/swap-nodes-in-pairs/
desc: 两两交换链表中相邻的节点（交换节点本身，不是交换值），返回头节点。
---
## 思路

- 就是 [25 K 个一组翻转](#/25) 在 k = 2 时的特例：处理前两个节点，后面的交给递归。
- 递归：不足两个节点直接返回；否则第二个节点 `newHead` 成为新头，原来的 `head` 变成这一组的尾，接上 `swapPairs(第三个节点)` 的结果。
- 迭代：`dummy` + 前驱 `pre`，每次把 `pre` 后面的两个节点 `a`、`b` 交换，然后 `pre` 跳到 `a`（交换后它在后面）。

## 易错点

- 递归里要先用 `newHead.next` 求出后面的结果，再改 `newHead.next`，否则后面的链表丢了。
- 迭代的三步改指针有先后顺序，画一下 `pre → a → b → 后面` 再写。

## 代码

### 写法一：递归

```python
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        new_head = head.next
        head.next = self.swapPairs(new_head.next)    # 原头变成这组的尾，接上后面的结果
        new_head.next = head
        return new_head
```

```java
class Solution {
    public ListNode swapPairs(ListNode head) {
        if (head == null || head.next == null) return head;
        ListNode newHead = head.next;
        head.next = swapPairs(newHead.next);         // 原头变成这组的尾，接上后面的结果
        newHead.next = head;
        return newHead;
    }
}
```

### 写法二：迭代

```python
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        pre = dummy
        while pre.next and pre.next.next:
            a, b = pre.next, pre.next.next           # pre -> a -> b -> ...
            a.next = b.next
            b.next = a
            pre.next = b                             # pre -> b -> a -> ...
            pre = a
        return dummy.next
```

```java
class Solution {
    public ListNode swapPairs(ListNode head) {
        ListNode dummy = new ListNode(-1, head), pre = dummy;
        while (pre.next != null && pre.next.next != null) {
            ListNode a = pre.next, b = a.next;       // pre -> a -> b -> ...
            a.next = b.next;
            b.next = a;
            pre.next = b;                            // pre -> b -> a -> ...
            pre = a;
        }
        return dummy.next;
    }
}
```

**复杂度**：时间 O(n)；空间递归 O(n)，迭代 O(1)。
