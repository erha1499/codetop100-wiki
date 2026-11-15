---
rank: 11
id: "21"
title: 合并两个有序链表
difficulty: 简单
tags: [链表]
freq: 336
link: https://leetcode.cn/problems/merge-two-sorted-lists/
desc: 把两个升序链表合并成一个升序链表。
---
## 思路

- **虚拟头节点 + 双指针**：`p1`、`p2` 各指一个链表，谁小就把谁接到 `p` 后面。
- 一个走完后，另一个剩下的部分本来就有序，直接整段接上。
- `dummy` 免去单独处理头节点，最后返回 `dummy.next`。

## 代码

```python
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = p = ListNode(-1)
        p1, p2 = list1, list2
        while p1 and p2:
            if p1.val < p2.val:
                p.next = p1
                p1 = p1.next
            else:
                p.next = p2
                p2 = p2.next
            p = p.next
        p.next = p1 or p2                    # 剩下的整段接上
        return dummy.next
```

```java
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode dummy = new ListNode(-1), p = dummy;
        ListNode p1 = list1, p2 = list2;
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
        p.next = p1 != null ? p1 : p2;       // 剩下的整段接上
        return dummy.next;
    }
}
```

**复杂度**：时间 O(m + n)，空间 O(1)。
