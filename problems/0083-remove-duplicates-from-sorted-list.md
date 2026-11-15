---
rank: 97
id: "83"
title: 删除排序链表中的重复元素
difficulty: 简单
tags: [链表]
freq: 69
link: https://leetcode.cn/problems/remove-duplicates-from-sorted-list/
desc: 删除升序链表中的重复元素，让每个值只保留一个节点。
---
## 思路

- 链表有序，相同的值一定挨在一起。
- `cur` 站在当前节点上，只要下一个节点的值和它相同，就把下一个节点跳过；删干净了再往后走。
- 头节点不会被删，所以不需要 `dummy`（对比 [82](#/82)：重复的全删，头可能被删）。

## 易错点

- 删掉一个之后不能马上移动 `cur`：后面可能还有相同的值，要用 `while` 删完。
- 循环条件要保证 `cur` 和 `cur.next` 都不为空。

## 代码

```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur and cur.next:
            while cur.next and cur.val == cur.next.val:      # 把后面相同的都跳过
                cur.next = cur.next.next
            cur = cur.next
        return head
```

```java
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        ListNode cur = head;
        while (cur != null && cur.next != null) {
            while (cur.next != null && cur.val == cur.next.val) {   // 把后面相同的都跳过
                cur.next = cur.next.next;
            }
            cur = cur.next;
        }
        return head;
    }
}
```

**复杂度**：时间 O(n)，空间 O(1)。
