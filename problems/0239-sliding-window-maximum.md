---
rank: 41
id: "239"
title: 滑动窗口最大值
difficulty: 困难
tags: [滑动窗口, 单调队列]
freq: 160
link: https://leetcode.cn/problems/sliding-window-maximum/
desc: 大小为 k 的窗口从左滑到右，返回每个窗口里的最大值。
---
## 思路

- 维护一个**单调递减队列**，队头永远是当前窗口的最大值。三个操作：
  - `push(x)`：入队前把队尾所有比 `x` 小的弹掉——只要 `x` 还在窗口里，它们永远当不了最大值；
  - `max()`：取队头；
  - `pop(x)`：窗口最左边的元素 `x` 要滑出去时，**只有它等于队头才弹**（不等说明它早就被更大的压掉了，不在队列里）。
- 遍历到 `i`：先 `push(nums[i])`；窗口满了（`i >= k - 1`）就记录 `max()`，再 `pop(nums[i - k + 1])`。

## 易错点

- `push` 时弹队尾用严格小于 `<`：相等的要留着，否则 `pop` 时会把还在窗口里的那个相同值误删。
- 需要两端都能操作的结构：Python `deque`，Java `ArrayDeque` / `LinkedList`。
- 另一种常见写法是队列里存下标，用 `q[0] <= i - k` 判断过期。

## 代码

```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q, res = deque(), []                 # 队列里的值单调递减，队头最大
        for i, x in enumerate(nums):
            while q and q[-1] < x:           # push：压掉队尾比 x 小的
                q.pop()
            q.append(x)
            if i >= k - 1:                   # 窗口已满
                res.append(q[0])             # max
                if q[0] == nums[i - k + 1]:  # pop：滑出的元素是队头才弹
                    q.popleft()
        return res
```

```java
class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        Deque<Integer> q = new ArrayDeque<>();           // 队列里的值单调递减，队头最大
        int[] res = new int[nums.length - k + 1];
        for (int i = 0; i < nums.length; i++) {
            while (!q.isEmpty() && q.peekLast() < nums[i]) {   // push：压掉队尾比它小的
                q.pollLast();
            }
            q.offerLast(nums[i]);
            if (i >= k - 1) {                            // 窗口已满
                res[i - k + 1] = q.peekFirst();          // max
                if (q.peekFirst() == nums[i - k + 1]) {  // pop：滑出的元素是队头才弹
                    q.pollFirst();
                }
            }
        }
        return res;
    }
}
```

**复杂度**：时间 O(n)（每个元素最多入队、出队各一次），空间 O(k)。
