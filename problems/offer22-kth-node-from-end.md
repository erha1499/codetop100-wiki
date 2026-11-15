---
rank: 62
id: "剑指 Offer 22"
title: 链表中倒数第k个节点
difficulty: 简单
tags: [链表, 双指针]
freq: 103
link: https://leetcode.cn/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof/
desc: 返回链表的倒数第 k 个节点（现为 LCR 140 训练计划 II，参数名是 cnt）。
---
## 思路

- 快慢指针拉开固定间隔：`fast` 先走 `cnt` 步，然后 `fast` 和 `p` 一起走。
- `fast` 走到 `null` 时，`p` 正好在倒数第 `cnt` 个节点。
- 和 [19](#/19) 是同一个套路：那题要删除，所以多一个 `dummy` 让慢指针停在前驱；这题只要找到，不需要 `dummy`。

## 易错点

- 第二个循环的条件是 `fast != null`，写成 `fast.next != null` 会错一位。
- 题目保证 `cnt` 不超过链表长度；`cnt == 长度` 时 `fast` 直接走到 `null`，返回 `head`，正确。

## 代码

```python
class Solution:
    def trainingPlan(self, head: Optional[ListNode], cnt: int) -> Optional[ListNode]:
        fast = head
        for _ in range(cnt):                 # fast 先走 cnt 步
            fast = fast.next
        p = head
        while fast:
            fast = fast.next
            p = p.next
        return p
```

```java
class Solution {
    public ListNode trainingPlan(ListNode head, int cnt) {
        ListNode fast = head;
        while (cnt-- > 0) {                  // fast 先走 cnt 步
            fast = fast.next;
        }
        ListNode p = head;
        while (fast != null) {
            fast = fast.next;
            p = p.next;
        }
        return p;
    }
}
```

**复杂度**：时间 O(n)，空间 O(1)。
