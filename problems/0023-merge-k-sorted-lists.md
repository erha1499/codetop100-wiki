---
rank: 23
id: "23"
title: 合并K个排序链表
difficulty: 困难
tags: [链表, 分治, 堆]
freq: 264
link: https://leetcode.cn/problems/merge-k-sorted-lists/
desc: 把 k 个升序链表合并成一个升序链表。
---
## 思路

- **分治**（类似归并排序）：`traverse(lo, hi)` 表示合并 `lists[lo..hi]` 并返回头节点；拆成左右两半各自合并，再用 [21](#/21) 的方法合并两条。
- **小顶堆**：堆里放每条链表当前的头节点，每次弹出最小的接到结果后面，再把它的 `next` 入堆。堆里最多 k 个节点。
- 为什么不顺序合并 `((l1+l2)+l3)+…`：前面合出来的长链表被反复遍历，O(Nk)。分治每层总共处理 N 个节点，共 log k 层。

## 易错点

- `lists` 为空数组要先返回空；数组里也可能有空链表（堆写法入堆前要判空）。
- Python 的堆不能直接比较 `ListNode`：放 `(val, 链表下标, node)`，`val` 相同时用下标决胜，轮不到比节点。

## 代码

### 写法一：分治

```python
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        def traverse(lo, hi):                # 合并 lists[lo..hi]
            if lo == hi:
                return lists[lo]
            mid = (lo + hi) // 2
            return self.mergeTwoLists(traverse(lo, mid), traverse(mid + 1, hi))

        return traverse(0, len(lists) - 1)

    def mergeTwoLists(self, p1, p2):
        dummy = p = ListNode(-1)
        while p1 and p2:
            if p1.val <= p2.val:
                p.next = p1
                p1 = p1.next
            else:
                p.next = p2
                p2 = p2.next
            p = p.next
        p.next = p1 or p2
        return dummy.next
```

```java
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists.length == 0) return null;
        return traverse(lists, 0, lists.length - 1);
    }

    // 合并 lists[lo..hi]
    private ListNode traverse(ListNode[] lists, int lo, int hi) {
        if (lo == hi) return lists[lo];
        int mid = lo + (hi - lo) / 2;
        return mergeTwoLists(traverse(lists, lo, mid), traverse(lists, mid + 1, hi));
    }

    private ListNode mergeTwoLists(ListNode p1, ListNode p2) {
        ListNode dummy = new ListNode(-1), p = dummy;
        while (p1 != null && p2 != null) {
            if (p1.val <= p2.val) {
                p.next = p1;
                p1 = p1.next;
            } else {
                p.next = p2;
                p2 = p2.next;
            }
            p = p.next;
        }
        p.next = p1 != null ? p1 : p2;
        return dummy.next;
    }
}
```

### 写法二：小顶堆

```python
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = [(node.val, i, node) for i, node in enumerate(lists) if node]
        heapq.heapify(heap)
        dummy = p = ListNode(-1)
        while heap:
            _, i, node = heapq.heappop(heap)
            p.next = node
            p = p.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        return dummy.next
```

```java
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        PriorityQueue<ListNode> pq = new PriorityQueue<>((a, b) -> a.val - b.val);
        for (ListNode head : lists) {
            if (head != null) pq.offer(head);
        }
        ListNode dummy = new ListNode(-1), p = dummy;
        while (!pq.isEmpty()) {
            ListNode node = pq.poll();
            p.next = node;
            p = p.next;
            if (node.next != null) pq.offer(node.next);
        }
        return dummy.next;
    }
}
```

**复杂度**：两种写法时间都是 O(N log k)（N 为节点总数）；空间分治 O(log k)（递归栈），堆 O(k)。
