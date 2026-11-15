---
rank: 26
id: "141"
title: 环形链表
difficulty: 简单
tags: [链表, 双指针]
freq: 259
link: https://leetcode.cn/problems/linked-list-cycle/
desc: 判断链表中是否有环。
---
## 思路

- 快慢指针（Floyd 判圈）：`slow` 每次一步，`fast` 每次两步。
- 有环：进环后是追及问题，`fast` 每轮比 `slow` 多走一步，环长有限，一定追上。
- 无环：`fast` 先走到 `null`。

## 易错点

- 循环条件 `fast != null && fast.next != null`：要走两步，两个都得判；`slow` 在后面，不用判。
- 先走再比较（起点两个指针本来就相等）。
- 比的是节点引用，不是值。

## 代码

```python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False
```

```java
public class Solution {
    public boolean hasCycle(ListNode head) {
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) return true;
        }
        return false;
    }
}
```

**复杂度**：时间 O(n)，空间 O(1)。
