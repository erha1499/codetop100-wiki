---
rank: 36
id: "82"
title: 删除排序链表中的重复元素 II
difficulty: 中等
tags: [链表]
freq: 187
link: https://leetcode.cn/problems/remove-duplicates-from-sorted-list-ii/
desc: 删除升序链表中所有出现重复的数字（一个都不留），只保留原本只出现一次的节点。
---
## 思路

- 和 [83](#/83) 的区别：83 重复的保留一个，这题重复的全删——头节点也可能被删，所以要 `dummy`。
- `cur` 始终站在「已确定保留」的最后一个节点上，往后看两个节点：
  - `cur.next` 和 `cur.next.next` 值相同 → 记下这个值 `val`，把后面所有等于 `val` 的节点全部删掉；
  - 不同 → `cur.next` 是唯一的，`cur` 后移。

## 易错点

- 删完一段重复后**不要移动 `cur`**：新的 `cur.next` 可能又是一段重复，要留在原地继续检查。
- 循环条件 `cur.next != null && cur.next.next != null`，少一个就空指针。

## 代码

```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-101, head)
        cur = dummy
        while cur.next and cur.next.next:
            val = cur.next.val
            if val == cur.next.next.val:
                while cur.next and cur.next.val == val:      # 整段删掉，cur 不动
                    cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next
```

```java
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        ListNode dummy = new ListNode(-101, head), cur = dummy;
        while (cur.next != null && cur.next.next != null) {
            int val = cur.next.val;
            if (val == cur.next.next.val) {
                while (cur.next != null && cur.next.val == val) {   // 整段删掉，cur 不动
                    cur.next = cur.next.next;
                }
            } else {
                cur = cur.next;
            }
        }
        return dummy.next;
    }
}
```

**复杂度**：时间 O(n)，空间 O(1)。
