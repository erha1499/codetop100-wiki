---
rank: 38
id: "142"
title: 环形链表 II
difficulty: 中等
tags: [链表, 双指针]
freq: 171
link: https://leetcode.cn/problems/linked-list-cycle-ii/
desc: 返回链表开始入环的第一个节点，无环返回 null。
---
## 思路

- 第一阶段同 [141](#/141)：快慢指针判断有没有环，有环时停在相遇点。
- 第二阶段：一个指针回到 `head`，另一个留在相遇点，**同速**前进，再次相遇的位置就是环入口。
- 推导：设头到入口 `a`，入口到相遇点 `b`，环剩余 `c`。`fast` 走的路是 `slow` 的两倍：`2(a + b) = a + b + n(b + c)` → `a = (n - 1)(b + c) + c`。即从头走 `a` 步 = 从相遇点走 `c` 步再绕若干圈，都到入口。

## 易错点

- 相遇点 ≠ 环入口，不能直接返回。
- 第二阶段两个指针都是一次一步。
- 无环（`fast` 走到头）要返回 `null`。

## 代码

```python
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:                 # 有环：一个回到头，同速再走
                p1, p2 = head, slow
                while p1 is not p2:
                    p1 = p1.next
                    p2 = p2.next
                return p1
        return None
```

```java
public class Solution {
    public ListNode detectCycle(ListNode head) {
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) {              // 有环：一个回到头，同速再走
                ListNode p1 = head, p2 = slow;
                while (p1 != p2) {
                    p1 = p1.next;
                    p2 = p2.next;
                }
                return p1;
            }
        }
        return null;
    }
}
```

**复杂度**：时间 O(n)，空间 O(1)。
